%global		module		Clp

# Avoid circular dependencies on first build
%bcond_with bootstrap

Name:		coin-or-%{module}
Summary:	Coin-or linear programming
Version:	1.17.6
Release:	2%{?dist}
License:	EPL-1.0
URL:		https://github.com/coin-or/%{module}
Source0:	%{url}/archive/releases/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	coin-or-Data-Netlib
BuildRequires:	coin-or-Osi-doc
BuildRequires:	gcc-c++
BuildRequires:	doxygen
BuildRequires:	MUMPS-devel
%if %{without bootstrap}
BuildRequires:	pkgconfig(cbc)
%endif
BuildRequires:	pkgconfig(osi)
BuildRequires:	pkgconfig(readline)
BuildRequires:	suitesparse-devel

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix a bad static cast
Patch1:		%{name}-bad-cast.patch

# Fix a parameter which is not defined when building with Cbc support.
Patch2:		%{name}-param.patch

# Catch polymorphic errors by reference rathern than by value
Patch3:		%{name}-catch.patch

# Fix a bad sprintf that overwrites its own output
Patch4:		%{name}-sprintf.patch

# Increase buffer sizes to avoid sprintf overflow
Patch5:		%{name}-overflow.patch

# Fix mixed signed-unsigned comparisons
Patch6:		%{name}-signed.patch

# Do not use the AVX2 instructions
Patch7:		%{name}-no-avx.patch

%description
Clp (Coin-or linear programming) is an open-source linear programming
solver written in C++. It is primarily meant to be used as a callable
library, but a basic, stand-alone executable version is also available.

%package	devel
Summary:	Development files for %{name}
%if %{without bootstrap}
Requires:	coin-or-Cbc-devel%{?_isa}
%endif
Requires:	coin-or-Osi-devel%{?_isa}
Requires:	readline-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Osi-doc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%setup -q -n %{module}-releases-%{version}
%patch0 -p1
%patch1 -p1
%if %{without bootstrap}
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%if %{without bootstrap}
export CPPFLAGS="-DCOIN_HAS_CBC -DCOIN_HAS_NTY -I$PWD/src/OsiClp"
%endif
%configure \
  --with-amd-incdir=%{_includedir}/suitesparse \
  --with-amd-lib=-lamd \
  --with-cholmod-incdir=%{_includedir}/suitesparse \
  --with-cholmod-lib=-lcholmod \
  --with-glpk_incdir=%{_includedir} \
  --with-glpk-lib=-lglpk \
  --with-mumps-incdir=%{_includedir}/MUMPS \
  --with-mumps-lib="-ldmumps -lmpiseq" \
%if %{without bootstrap}
  LIBS="-lCbc"
%endif

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
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,clp_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ -ldmumps.*//' %{buildroot}%{_libdir}/pkgconfig/clp.pc

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%ldconfig_scriptlets

%files
%license LICENSE
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/README
%{_bindir}/clp
%{_libdir}/libClp.so.1
%{_libdir}/libClp.so.1.*
%{_libdir}/libClpSolver.so.1
%{_libdir}/libClpSolver.so.1.*
%{_libdir}/libOsiClp.so.1
%{_libdir}/libOsiClp.so.1.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/libClp.so
%{_libdir}/libClpSolver.so
%{_libdir}/libOsiClp.so
%{_libdir}/pkgconfig/clp.pc
%{_libdir}/pkgconfig/osi-clp.pc

%files		doc
%{_docdir}/%{name}/html
%{_docdir}/%{name}/clp_doxy.tag

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 Jerry James <loganjerry@gmail.com> - 1.17.6-1
- Version 1.17.6

* Sun Apr 12 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.17.5-2
- Rebuilt for MUMPS 5.3

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 1.17.5-1
- Version 1.17.5
- Drop unnecessary libnauty BR

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jul 30 2019 Adam Williamson <awilliam@redhat.com> - 1.17.3-3
- Rebuild in non-bootstrap mode

* Tue Jul 30 2019 Adam Williamson <awilliam@redhat.com> - 1.17.3-2
- Bootstrap build for mumps soname bump

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.17.3-1
- Rebuild in non-bootstrap mode

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.17.3-0
- Update to latest upstream release (bz 1461031, 1603677)
- Update project URL
- Change License from EPL to EPL-1.0
- Eliminate unnecessary BRs and Rs
- Build with Cbc, MUMPS, nauty, and suitesparse
- Build in bootstrap mode
- Add -bad-cast, -badcolumn, -param, -catch, -sprintf, -overflow, -signed,
  and -no-avx patches
- Eliminate rpath from the library
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Filter out unnecessary Libs values from pkgconfig files
- Package doxygen tag file to enable cross-linking

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.10-1
- Update to latest upstream release (#1308278)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 11 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.9-1
- Update to latest upstream release (#1270497)

* Fri Sep 25 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.8-1
- Update to latest upstream release (#1257923)
- Remove no longer needed patch to prevent coin-or-OS crash in %%check

* Mon Jun 22 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.6-5
- Correct crash on coin-or-OS check

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.6-4
- Bump release.

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.6-3
- Full rebuild or coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.6-1
- Update to latest upstream release (#1201068)

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.3-2
- Rebuild to ensure using latest C++ abi changes.

* Mon Feb  9 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.3-1
- Update to latest upstream release (#1190729).

* Sat Feb 07 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.1-1
- Update to latest upstream release (#1159475).

* Sun Aug 31 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.10-2
- Rebuild to ensure packages are built in proper order.

* Sat Aug 30 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.10-1
- Update to latest upstream release (#1133195#c2).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.7-1
- Update to latest upstream release (#1089923).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov  4 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.3-3
- Correct source url path (#894587#c7).
- Add coin-or-CoinUtils-devel requires to the devel package (#894587#c7).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.3-2
- Use proper _smp_flags macro (#894586#c6).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.3-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.14.8-1
- Update to latest upstream release.

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.14.7-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.14.7-2
- Rename package to coin-or-Clp.
- Do not package Thirdy party data or data without clean license.

* Thu Sep 27 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.14.7-1
- Initial coinor-Clp spec.
