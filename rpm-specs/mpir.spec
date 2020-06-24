Name:			mpir
Version:		3.0.0
Release:		8%{?dist}
Summary:		A library for arbitrary precision arithmetic

License:		LGPLv3+
URL:			http://mpir.org/
Source0:		http://mpir.org/%{name}-%{version}.tar.bz2
# Enable aarch64 support
Patch0:			%{name}-aarch64.patch

# ppc64 assembly has not yet been ported to little endian
ExcludeArch:		ppc64le

BuildRequires:		gcc-c++
BuildRequires:		m4
BuildRequires:		texinfo-tex
BuildRequires:		yasm

%description
MPIR is an open source multiprecision integer library derived from
version 4.2.1 of the GMP (GNU Multi Precision) project.

%package  		devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0

# Convert ISO-8859-1 files to UTF-8, preserving timestamps
for fil in NEWS doc/devel/projects.html doc/devel/tasks.html; do
  iconv --from=ISO-8859-1 --to=UTF-8 $fil -o $fil.conv
  sed -i 's/charset=iso-8859-1/charset=UTF-8/' $fil
  touch -r $fil $fil.conv
  mv -f $fil.conv $fil
done

# Update texinfo.tex
cp -p %{_texmf_main}/tex/texinfo/texinfo.tex doc

%build
%configure --disable-static --enable-cxx --with-yasm=%{_bindir}/yasm \
  CCAS="gcc -c -Wa,--noexecstack" \
  LIBS="-lrt" \
  LDFLAGS="$RPM_LD_FLAGS -Wl,--as-needed -Wl,-z,noexecstack"

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g.*\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Compile
export LD_LIBRARY_PATH=$PWD/.libs
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_infodir}/dir
mv doc/devel doc/html

%check
export LD_LIBRARY_PATH=$PWD/.libs
make check

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%license COPYING COPYING.LIB
%{_libdir}/*.so.*

%files devel
%doc doc/html doc/isa_abi_headache
%{_includedir}/*
%{_libdir}/*.so
%{_infodir}/mpir.info*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 3.0.0-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Jerry James <loganjerry@gmail.com> - 2.7.2-1
- New upstream release (bz 1284140)

* Fri Nov 13 2015 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- New upstream release (bz 1281980)

* Wed Jul  1 2015 Jerry James <loganjerry@gmail.com> - 2.7.0-1
- New upstream release (bz 1236066)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.6.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 2.6.0-9
- Update URLs
- Use license macro
- Drop workaround for binutils bug, fixed in 2.24
- Combine libtool workarounds for -Wl,--as-needed

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Jerry James <loganjerry@gmail.com> - 2.6.0-5
- Add aarch64 support (bz 926173)

* Fri Feb 22 2013 Jerry James <loganjerry@gmail.com> - 2.6.0-4
- Add -test patch to fix a broken test

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec  5 2012 Jerry James <loganjerry@gmail.com> - 2.6.0-2
- Drop ExcludeArch; s390/s390x systems use the generic mpn support

* Fri Nov  9 2012 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- New upstream release
- Drop libtool typo fix; fixed upstream
- Fix libtool workaround for -Wl,--as-needed

* Thu Oct  4 2012 Jerry James <loganjerry@gmail.com> - 2.5.2-1
- New upstream release
- Link with -lrt to get the clock_* functions
- Convince libtool to use -Wl,--as-needed appropriately

* Wed Sep 12 2012 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- New upstream release
- License change to LPGLv3+
- Support for s390 / s390x has been dropped
- Minor spec file cleanups

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-8
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Dan Horák <dan[at]danny.cz> - 1.3.1-6
- add s390x support from GMP

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 16 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-4
- Fix the RHEL build

* Fri Mar 05 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-3
- Include HTML documentation
- Include demos

* Thu Mar 04 2010 Mark Chappell <tremble@fedoraproject.org> - 1.3.1-2
- Ensure consistent use of macros
- Avoid multilib conflict due to modified timestamp on AUTHORS doc
- Replace perl find and replace with sed

* Wed Feb 17 2010 M D Chappell <tremble@tremble.org.uk> - 1.3.1-1
- Initial build
