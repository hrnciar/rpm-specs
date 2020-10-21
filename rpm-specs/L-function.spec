Name:		L-function
Version:	1.23
Release:	29%{?dist}
Summary:	C++ L-function class library and command line interface
License:	GPLv2+
Source0:	http://oto.math.uwaterloo.ca/~mrubinst/L_function_public/CODE/L-1.23.tar.gz
# From sage tarball, lcalc spkg, debian directory
Source1:	lcalc.1
URL:		http://oto.math.uwaterloo.ca/~mrubinst/L_function_public/L.html
BuildRequires:  gcc-c++
BuildRequires:	gmp-devel
BuildRequires:	pari-devel

### Sagemath patches
# Fix minor code issues that clang warns about; gcc does not warn, but apply
# the fixes anyway for parity with sagemath
Patch0:		clang.patch
# Fix malformed default parameter declarations for compatibility with gcc 4.9+
Patch1:		lcalc-1.23_default_parameters_1.patch
# Fix malformed default parameter declarations for compatibility with gcc 5+
Patch2:		lcalc-1.23_default_parameters_2.patch
# Fix the lcalc_to_double definition
Patch3:		Lcommon.h.patch
# Fix various Makefile issues
Patch4:		Makefile.patch
# Fixes for compatibility with pari 2.7+ and 2.9+
Patch5:		pari-2.7.patch
# Fix the pari include path
Patch6:		pari_include.patch
# Tell pari to use less memory
Patch7:		pari-mem.patch
# Add a missing include of time.h
Patch8:		time.h.patch
# Fix some declarations related to the std namespace
Patch9:		using_namespace_std.patch
### End of Sagemath patches

### Fedora patches
# Update obsolete uses of strstream to modern stringstream
Patch100:	stringstream.patch

%description
C++ L-function class library and command line interface.

%package	devel
Summary:	Development libraries/headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Headers and libraries for development with %{name}.

%prep
%autosetup -p1 -n L-%{version}

# Clean up unnecessary and prebuilt files
rm -f .*DS_Store
rm -f include/*.{swap.crap,bak}
rm -f include/.*{DS_Store,.swp}
rm -f src/.*{DS_Store,.swp}
rm -f src/{Makefile.old,libLfunction.a}

# Give the library an soname, use Fedora link flags, and do not override Fedora
# build flags
sed -e 's|/lib/|/%{_lib}/|g' \
 -e "s|\(DYN_OPTION=shared\)|\1 -Wl,-soname=libLfunction.so.%{version} $RPM_LD_FLAGS|" \
 -e 's/^\([[:blank:]]*MACHINE_SPECIFIC_FLAGS = \).*/\1-ffast-math -fPIC/' \
 -i src/Makefile

# Fix end of line encodings
sed -i -e 's/\r//' src/example_programs/example.cc

%build
pushd src
    # Create link before library is created
    ln -sf libLfunction.so.%{version} libLfunction.so
    make %{?_smp_mflags} all EXTRA="$RPM_OPT_FLAGS"
popd
rm -f src/example_programs/example

%install
mkdir -p $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir},%{_mandir}/man1}
pushd src
    make INSTALL_DIR="$RPM_BUILD_ROOT%{_prefix}" install
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
    pushd example_data_files
	for sample in *; do
	    install -p -m644 $sample $RPM_BUILD_ROOT%{_datadir}/%{name}/$sample
	done
    popd
    install -m644 example_programs/example.cc \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/example.cc
popd
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1
install -m755 src/libLfunction.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libLfunction.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libLfunction.so
# Correct permissions
chmod 644 $RPM_BUILD_ROOT%{_includedir}/libLfunction/*.h

%files
%doc CONTRIBUTORS
%doc COPYING
%doc README
%{_bindir}/lcalc
%{_libdir}/libLfunction.so.%{version}
%{_mandir}/man1/*

%files devel
%doc %{_datadir}/%{name}
%{_includedir}/libLfunction
%{_libdir}/libLfunction.so

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jerry James <loganjerry@gmail.com> - 1.23-25
- Discard our patches in favor of sagemath's patches for ease of maintenance
- Add -stringstream patch to avoid deprecated APIs

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.23-24
- Rebuild for pari 2.11.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.23-22
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov  9 2016 Paul Howarth <paul@city-fan.org> - 1.23-17
- Add patch to build with pari 2.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.23-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Feb  8 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.23-13
- Correct problems with sagemath build with gcc 5.0.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.23-10
- Add Debian patch to rebuild with pari 2.7.
- Add patch to build with gcc 4.9.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.23-6
- Build with $RPM_OPT_FLAGS and %%{_smp_mflags} (regression in -5).
- Build with $RPM_LD_FLAGS.

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.23-5
- Merge with duplicate review request #821195 that had changelog
  + Correct license tag.
  + Install example source code.
  + Add %%post sections for library.
  + Build lcalc with openmp support.
  + Rename to L to match upstream tarball.
  + Add proper documentation to main package.
  + Remove the "see also" section of lcalc.1 as there is no info page.
  + Initial lcalc spec.
- Do not provide %%{name}-static as no such library is/was installed.
- Install CONTRIBUTORS as documentation.
- Remove %%defattr usage.

* Sat Apr 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.23-4
- Fix build failure (since F-11!) 

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Conrad Meyer <konrad@tylerc.org> - 1.23-1
- Bump to latest upstream.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Conrad Meyer <konrad@tylerc.org> - 1.2-3
- Add missing BR on pari-devel.

* Sat Mar 14 2009 Conrad Meyer <konrad@tylerc.org> - 1.2-2
- Include headers in -devel subpackage.
- Include PARI support.

* Sat Nov 8 2008 Conrad Meyer <konrad@tylerc.org> - 1.2-1
- Initial package.
