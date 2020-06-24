Name:           libfplll
Version:        5.3.2
Release:        2%{?dist}
Summary:        LLL-reduces euclidean lattices
License:        LGPLv2+
URL:            https://github.com/fplll/fplll
Source0:        https://github.com/fplll/fplll/releases/download/%{version}/fplll-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(qd)

%description
fplll contains several algorithms on lattices that rely on
floating-point computations. This includes implementations of the
floating-point LLL reduction algorithm, offering different
speed/guarantees ratios. It contains a 'wrapper' choosing the
estimated best sequence of variants in order to provide a guaranteed
output as fast as possible. In the case of the wrapper, the
succession of variants is oblivious to the user. It also includes
a rigorous floating-point implementation of the Kannan-Fincke-Pohst
algorithm that finds a shortest non-zero lattice vector, and the BKZ
reduction algorithm.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qd-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains a static library for %{name}.


%package        tools
Summary:        Command line tools that use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools package contains command-line tools that expose
the functionality of %{name}.


%prep
%autosetup -p1 -n fplll-%{version}

# Fix broken test for a bool type
sed -e '/#ifndef bool/,/#endif/d' \
    -e '/#ifndef false/,/#endif/d' \
    -e '/#if false/,/#endif/d' \
    -e '/#ifndef true/,/#endif/d' \
    -e '/#if true/,/#endif/d' \
    -e '/ac_cv_type__Bool/s/\$ac_includes_default/#include <stdbool.h>/' \
    -i configure

%build
%configure --disable-silent-rules LIBS=-lpthread

# Eliminate hardcoded rpaths, and workaround libtool moving all -Wl options
# after the libraries to be linked
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool

%make_build

# Build the man pages
cd fplll
export LD_LIBRARY_PATH=$PWD/.libs
help2man -N -o ../fplll.1 ./fplll
help2man -N -o ../latsieve.1 ./latsieve
help2man -N -o ../latticegen.1 ./latticegen
cd -

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p *.1 %{buildroot}%{_mandir}/man1

%check
LD_LIBRARY_PATH=$PWD/src/.libs make check


%files
%doc NEWS README.md
%license COPYING
%{_libdir}/libfplll.so.6*
%{_datadir}/fplll/

%files devel
%{_includedir}/fplll.h
%{_includedir}/fplll/
%{_libdir}/libfplll.so
%{_libdir}/pkgconfig/fplll.pc

%files static
%{_libdir}/*.a

%files tools
%{_bindir}/*
%{_mandir}/man1/fplll.1*
%{_mandir}/man1/latsieve.1*
%{_mandir}/man1/latticegen.1*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 5.3.2-1
- Version 5.3.2

* Tue Dec 17 2019 Jerry James <loganjerry@gmail.com> - 5.3.1-1
- Version 5.3.1
- All patches have been upstreamed; drop them all

* Thu Nov 28 2019 Jerry James <loganjerry@gmail.com> - 5.3.0-1
- Version 5.3.0

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 5.2.1-5
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 5.2.1-1
- New upstream release (bz 1499072)
- Update URL
- Drop upstreamed -rounding patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 5.1.0-1
- New upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 5.0.3-1
- New upstream release
- Add a -static library for Macaulay2, which needs to control constructor order

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug  9 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.0.5-1
- Update to version required by sagemath 7.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0.4-6
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Jerry James <loganjerry@gmail.com> - 4.0.4-5
- Update project URL
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Jerry James <loganjerry@gmail.com> - 4.0.4-1
- New upstream release
- All patches have been upstreamed

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 4.0.3-1
- New upstream release

* Tue Mar 26 2013 Jerry James <loganjerry@gmail.com> - 4.0.2-2
- Add support for aarch64 (bz 925727)

* Mon Jan 28 2013 Jerry James <loganjerry@gmail.com> - 4.0.2-1
- New upstream release

* Sat Oct 20 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.0.1-2
- Add extra compatibility support with fplll3 (#868579)

* Thu Sep 27 2012 Jerry James <loganjerry@gmail.com> - 4.0.1-1
- New upstream release
- Separate binaries into a -tools subpackage
- Modernize the spec file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.12-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.12-4.2
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.12-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.0.12-2.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 3.0.12-2.1
- rebuild with new gmp

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 8 2009 Conrad Meyer <konrad@tylerc.org> - 3.0.12-1
- Bump to new version (3.0.12).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Conrad Meyer <konrad@tylerc.org> - 3.0.11-1
- Bump to new version (3.0.11).

* Fri Oct 17 2008 Conrad Meyer <konrad@tylerc.org> - 3.0.9-2
- Rename 'generate' binary to 'fplll_generate'.
- Move generically-named header files to fplll subdirectory of includedir.
- Add %%check.

* Sun Oct 12 2008 Conrad Meyer <konrad@tylerc.org> - 3.0.9-1
- Initial package.
