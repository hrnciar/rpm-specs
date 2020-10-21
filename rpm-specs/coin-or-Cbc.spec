%global		module		Cbc

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:		coin-or-%{module}
Summary:	Coin-or branch and cut
Version:	2.10.5
Release:	4%{?dist}
License:	EPL-1.0
URL:		https://github.com/coin-or/%{module}
Source0:	%{url}/archive/releases/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	coin-or-Cgl-doc
BuildRequires:	coin-or-Clp-doc
BuildRequires:	coin-or-DyLP-doc
BuildRequires:	coin-or-Vol-doc
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	mp-devel
BuildRequires:	MUMPS-devel
BuildRequires:  %{blaslib}-devel
BuildRequires:	pkgconfig(cgl)
BuildRequires:	pkgconfig(clp)
BuildRequires:	pkgconfig(coindatamiplib3)
BuildRequires:	pkgconfig(coindatanetlib)
BuildRequires:	pkgconfig(dylp)
BuildRequires:	pkgconfig(nauty)
BuildRequires:	pkgconfig(vol)

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Avoid empty #define if svnversion is available at configure time
Patch1:		%{name}-svnversion.patch

# Do not catch polymorphic exceptions by value
Patch2:		%{name}-exception.patch

# Fix a possible buffer overflow
Patch3:		%{name}-overflow.patch

# Fix a mixed signed/unsigned operation
Patch4:		%{name}-signed.patch

%description
Cbc (Coin-or branch and cut) is an open-source mixed integer programming
solver written in C++. It can be used as a callable library or using a
stand-alone executable. It can be called through AMPL (natively), GAMS
(using the links provided by the "Optimization Services" and "GAMSlinks"
projects), MPL (through the "CoinMP" project), AIMMS (through the "AIMMSlinks"
project), or "PuLP".

Cbc links to a number of other COIN projects for additional functionality,
including:

   * Clp (the default solver for LP relaxations)
   * Cgl (for cut generation)
   * CoinUtils (for reading input files and various utilities)

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Cgl-devel%{?_isa}
Requires:	coin-or-Clp-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Cgl-doc
Requires:	coin-or-Clp-doc
Requires:	coin-or-DyLP-doc
Requires:	coin-or-Vol-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{module}-releases-%{version}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @CBCLIB_PCLIBS@/\nLibs.private:&/' Cbc/cbc.pc.in

%build
%configure \
  --with-asl-incdir=%{_includedir}/asl \
  --with-asl-lib=-lasl \
  --with-blas-incdir=%{_includedir}/%{blaslib} \
  --with-blas-lib=-l%{blaslib} \
  --with-glpk-incdir=%{_includedir} \
  --with-glpk-lib=-lglpk \
  --with-lapack-incdir=%{_includedir}/%{blaslib} \
  --with-lapack-lib=-l%{blaslib} \
  --with-mumps-incdir=%{_includedir}/MUMPS \
  --with-mumps-lib=-ldmumps \
  --with-nauty-incdir=%{_includedir}/nauty \
  --with-nauty-lib=-lnauty

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build all doxydoc

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,cbc_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%ldconfig_scriptlets

%files
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/README
%{_bindir}/cbc
%{_libdir}/libCbc.so.3
%{_libdir}/libCbc.so.3.*
%{_libdir}/libCbcSolver.so.3
%{_libdir}/libCbcSolver.so.3.*
%{_libdir}/libOsiCbc.so.3
%{_libdir}/libOsiCbc.so.3.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libCbc.so
%{_libdir}/libCbcSolver.so
%{_libdir}/libOsiCbc.so
%{_libdir}/pkgconfig/cbc.pc
%{_libdir}/pkgconfig/osi-cbc.pc

%files		doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/cbc_doxy.tag

%changelog
* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.10.5-4
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  2 2020 Jerry James <loganjerry@gmail.com> - 2.10.5-2
- Rebuild for nauty 2.7.1

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 2.10.5-1
- Version 2.10.5

* Thu Feb 20 2020 Jerry James <loganjerry@gmail.com> - 2.10.4-1
- Version 2.10.4
- Drop upstreamed -sizeof patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 2.10.3-1
- Update to latest upstream release (bz 1461035)
- Update project URL
- Change License from EPL to EPL-1.0
- Eliminate unnecessary BRs and Rs
- Add -exception, -overflow, -signed, and -sizeof patches
- Build with asl and nauty support
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Filter out unnecessary Libs values from pkgconfig files
- Package doxygen tag file to enable cross-linking
- Run tests on ARM again

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.9.8-9
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 2.9.8-3
- Rebuild for glpk 4.61

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 15 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.8-1
- Update to latest upstream release (#1312515)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 11 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.7-1
- Update to latest upstream release (#1270499)

* Fri Sep 25 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.6-1
- Update to latest upstream release (#1265641)

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.5-3
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.5-1
- Update to latest upstream release (#1227748)

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.4-1
- Update to latest upstream release (#1201062)

* Sun Mar  1 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.2-5
- Install CbcParam.hpp not CbcParam.cpp.

* Sat Feb 28 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.2-4
- Install header required by coin-or-Dip.

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.2-3
- Intermediate build disabling %%check for arm only.

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.2-2
- Rebuild to ensure using latest C++ abi changes.

* Mon Feb  9 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.9.2-1
- Update to latest upstream release (#1116569).

* Sun Aug 31 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.8.12-3
- Rebuild to ensure packages are built in proper order.

* Sat Aug 30 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.8.12-1
- Update to latest upstream release (#1116569#c2).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.8.10-1
- Update to latest upstream release (#1116569).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.8.9-1
- Update to latest upstream release.

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.8.5-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.7.7-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.7.7-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.7.7-2
- Rename package to coin-or-Cbc.
- Do not package Thirdy party data or data without clean license.

* Thu Sep 27 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.7.7-1
- Initial coinor-Cbc spec.
