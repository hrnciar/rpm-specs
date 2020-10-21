# This package is arch-specific, because it computes properties of the system
# (such as endianness) and stores them in generated header files.  Hence, the
# files DO vary by platform.  However, there is no actual compiled code, so
# turn off debuginfo generation.
%global debug_package %{nil}

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:           fflas-ffpack
Version:        2.4.3
Release:        4%{?dist}
Summary:        Finite field linear algebra subroutines

License:        LGPLv2+
URL:            http://linbox-team.github.io/fflas-ffpack/
Source0:        https://github.com/linbox-team/%{name}/releases/download/%{version}/fflas_ffpack-%{version}.tar.bz2
# Fix memory leaks
# https://github.com/linbox-team/fflas-ffpack/pull/276
Patch0:         %{name}-mem-leak.patch

BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  givaro-devel
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  %{blaslib}-devel
BuildRequires:  tex(stmaryrd.sty)

# Although there are references to linbox-devel files in this package,
# linbox-devel Requires fflas-ffpack-devel, not the other way around.

%description
The FFLAS-FFPACK library provides functionality for dense linear algebra
over word size prime finite fields.

%package devel
Summary:        Header files for developing with fflas-ffpack
Requires:       givaro-devel%{?_isa}, gmp-devel%{?_isa}, %{blaslib}-devel%{?_isa}
Provides:       %{name}-static = %{version}-%{release}

%description devel
The FFLAS-FFPACK library provides functionality for dense linear algebra
over word size prime finite fields.  This package provides the header
files for developing applications that use FFLAS-FFPACK.

%package doc
Summary:        API documentation for fflas-ffpack
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Provides:       bundled(jquery)

%description doc
API documentation for fflas-ffpack.

%prep
%autosetup -p0 -n fflas_ffpack-%{version}
# Skip test-echelon for now due to failures.
# See https://github.com/linbox-team/fflas-ffpack/issues/282
sed -i '/^[[:blank:]]*test-echelon/d' tests/Makefile.am

# Do not use env
sed -i 's,%{_bindir}/env bash,%{_bindir}/bash,' fflas-ffpack-config.in

# Remove parts of the configure script that select non-default architectures
# and ABIs.
sed -i '/INSTR_SET/,/fabi-version/d' configure.ac

# Regenerate configure after monkeying with configure.ac
autoreconf -fi

%build
%configure --docdir=%{_docdir}/fflas-ffpack --disable-static --enable-openmp \
  --disable-simd --enable-doc \
  --with-blas-cflags="-I%{_includedir}/%{blaslib}" \
  --with-blas-libs="-l%{blaslib}"
chmod a+x fflas-ffpack-config
%make_build

# Build the developer documentation, too
cd doc
doxygen DoxyfileDev
cd ..

%install
%make_install

# Documentation is installed in the wrong place
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_prefix}/docs %{buildroot}%{_docdir}/%{name}-doc

# We don't want these files in with the doxygen-generated files
rm %{buildroot}%{_docdir}/%{name}-doc/%{name}-html/{AUTHORS,COPYING,INSTALL}

%check
export FLEXIBLAS=netlib
make check

%files devel
%doc AUTHORS ChangeLog README.md TODO
%license COPYING COPYING.LESSER
%{_bindir}/fflas-ffpack-config
%{_includedir}/fflas-ffpack/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%{_docdir}/%{name}-doc/

%changelog
* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.4.3-4
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov  1 2019 Jerry James <loganjerry@gmail.com> - 2.4.3-1
- New upstream release
- Drop upstreamed -const-void patch
- Add -mem-leak patch
- Switch from libopenblaso to libopenblasp due to test failures

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Jerry James <loganjerry@gmail.com> - 2.3.2-3
- Try again to switch from atlas to openblas
- Add -const-void patch from the sagemath developers

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 2.3.2-1
- New upstream release, fixes FTBFS (bz 1585225)
- Drop all patches
- Drop workarounds in the check script

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 2.2.2-8
- Rebuild after failed attempt to switch to openblas (s390x failures)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 2.2.2-5
- Remove dependency on /usr/bin/env

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan  6 2017 Jerry James <loganjerry@gmail.com> - 2.2.2-3
- Fix build on big endian platforms
- Disable ppc64 tests that fail due to an ATLAS bug (bz 1410633)

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 2.2.2-2
- Fix build on non-x86 platforms (bz 1373305)

* Fri Aug 12 2016 Jerry James <loganjerry@gmail.com> - 2.2.2-1
- New upstream release

* Tue Apr 12 2016 Jerry James <loganjerry@gmail.com> - 2.2.1-1
- New upstream release

* Fri Feb 26 2016 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Jerry James <loganjerry@gmail.com> - 1.6.0-10
- Note bundled jquery

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 1.6.0-9
- Rebuild for givaro 3.8.0
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Jerry James <loganjerry@gmail.com> - 1.6.0-6
- Rebuild for atlas 3.10.1

* Tue Jul 30 2013 Jerry James <loganjerry@gmail.com> - 1.6.0-5
- Adapt to Rawhide versionless _docdir change

* Wed Mar 27 2013 Jerry James <loganjerry@gmail.com> - 1.6.0-4
- Support building on aarch64 (bz 925336)
- Add more tex BRs due to TeXLive 2012 reorganization
- Ensure that __int64 is defined

* Fri Feb  8 2013 Jerry James <loganjerry@gmail.com> - 1.6.0-3
- Rebuild for givaro 3.7.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 3 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.0-1
- Update to latest upstream release.
- Remove gcc 4.7 patch already applied to upstream tarball.
- Rediff fflas-ffpack-debug patch.
- Remove fflas-ffpack-inline patch already applied to upstream tarball.
- Remove fflas-ffpack-64bit patch already applied to upstream tarball.

* Thu May  3 2012 Jerry James <loganjerry@gmail.com> - 1.4.3-3
- Add debug, inline, and 64bit patches

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 1.4.3-2
- Rebuild for GCC 4.7

* Tue Nov  1 2011 Jerry James <loganjerry@gmail.com> - 1.4.3-1
- New upstream version
- Tests have been fixed; restore %%check script

* Mon Aug 29 2011 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- New upstream version
- Tests are hopelessly broken; disable for now

* Thu May 26 2011 Jerry James <loganjerry@gmail.com> - 1.4.1-2
- Issues found on review:
- Fix license tag (fflasffpack-config is CeCILL-B)
- Add -doc subpackage
- More bad FSF addresses

* Tue May 24 2011 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Initial RPM
