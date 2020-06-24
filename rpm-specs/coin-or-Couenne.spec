%global		module		Couenne

%global		with_asl	1
%global		with_mpi	0

Name:		coin-or-%{module}
Summary:	An exact solver for nonconvex MINLPs
Version:	0.5.8
Release:	2%{?dist}
License:	EPL-1.0
URL:		https://projects.coin-or.org/%{module}
Source0:	http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
BuildRequires:	coin-or-Bonmin-doc
BuildRequires:	coin-or-Cbc-doc
BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	help2man
BuildRequires:	pkgconfig(bonmin)
BuildRequires:	pkgconfig(nauty)
%if %{with_asl}
BuildRequires:	mp-devel
%endif
%if %{with_mpi}
BuildRequires:	openmpi-devel
BuildRequires:	scalapack-openmpi-devel
BuildRequires:	openssh-clients
%endif

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

# Fix mixed signed/unsigned operations
Patch1:		%{name}-signed.patch

%description
Couenne (Convex Over and Under ENvelopes for Nonlinear Estimation) is a
branch&bound algorithm to solve Mixed-Integer Nonlinear Programming (MINLP)
problems of the form:
      min f0(x,y)
             fi(x,y) <= 0     i=1,2..., m
             x in Rn, y in Zp

where all fi(x,y) are, in general, nonlinear functions.

Couenne aims at finding global optima of nonconvex MINLPs. It implements
linearization, bound reduction, and branching methods within a
branch-and-bound framework. Its main components are:

  * an expression library;
  * separation of linearization cuts;
  * branching rules;
  * bound tightening methods.

%package	devel
Summary:	Development files for %{name}
Requires:	coin-or-Bonmin-devel
Requires:	libnauty-devel%{?_isa}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	coin-or-Bonmin-doc
Requires:	coin-or-Cbc-doc
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n %{module}-%{version}

# We only want HTML output from doxygen
sed -i 's/\(GENERATE_LATEX.*= \)YES/\1NO/' doxydoc/doxygen.conf.in

# The pkgconfig file lists transitive dependencies.  Those are necessary when
# using static libraries, but not with shared libraries.
sed -i 's/ @COUENNELIB_PCLIBS@/\nLibs.private:&/' couenne.pc.in

%build
%if %{with_mpi}
%_openmpi_load
%endif
%configure	\
%if %{with_asl}
	--with-asl-incdir="%{_includedir}/asl" \
	--with-asl-lib="-lasl -lmp -lipoptamplinterface -lbonminampl" \
%endif
	--with-nauty-incdir="%{_includedir}/nauty" \
	--with-nauty-lib="-lnauty"

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
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE,couenne_addlibs.txt}
cp -a doxydoc/{html,*.tag} %{buildroot}%{_docdir}/%{name}
cp -p doc/couenne-user-manual.pdf %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N src/main/.libs/couenne > \
  %{buildroot}%{_mandir}/man1/couenne.1

%check
%if %{with_mpi}
%_openmpi_load
%endif
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH make test

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/couenne
%dir %{_pkgdocdir}/
%{_pkgdocdir}/README
%{_pkgdocdir}/AUTHORS
%{_libdir}/libCouenne.so.1
%{_libdir}/libCouenne.so.1.*
%{_libdir}/libCouenneReadnl.so.1
%{_libdir}/libCouenneReadnl.so.1.*
%{_mandir}/man1/couenne.1*

%files devel
%{_includedir}/coin/*
%{_libdir}/libCouenne.so
%{_libdir}/libCouenneReadnl.so
%{_libdir}/pkgconfig/couenne.pc

%files doc
%{_pkgdocdir}/couenne-user-manual.pdf
%{_pkgdocdir}/html/
%{_pkgdocdir}/couenne_doxy.tag

%changelog
* Tue Jun  2 2020 Jerry James <loganjerry@gmail.com> - 0.5.8-2
- Rebuild for nauty 2.7.1

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 0.5.8-1
- Release 0.5.8
- Drop upstreamed -format patch
- Make the -doc subpackage be arch-specific to work around FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 0.5.7-2
- Update project URL
- Eliminate unnecessary BRs and Rs
- Build with nauty support
- Add -format patch
- Force libtool to not defeat -Wl,--as-needed
- Be explicit about library versions as required by latest guidelines
- Filter out unnecessary Libs values from pkgconfig files
- Package doxygen tag file to enable cross-linking

* Tue Apr 09 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.5.7-1
- Release 0.5.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.5.6-17
- Remove Group tags

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.5.6-15
- Rebuild for Ipopt-3.12.10

* Fri Feb 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.5.6-14
- Rebuild for Ipopt-3.12.9
- Rebuild against openblas

* Thu Feb 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.5.6-13
- Add gcc gcc-c++ BR

* Fri Feb 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.5.6-12
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 29 2017 Antonio Trande <sagitterATfedoraproject.org> - 0.5.6-10
- Rebuild for MUMPS-5.1.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Antonio Trande <sagitterATfedoraproject.org> - 0.5.6-7
- Rebuild for MUMPS-5.1.1 (after a bug-fix)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5.6-5
- Rebuild for newer mumps

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.6-3
- Rebuild (Power64)

* Tue Aug 02 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5.6-2
- Rebuild for newer mumps

* Wed Mar 16 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5.6-1
- Update to latest upstream release
- Correct FTBFS in rawhide (#1307387)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5.2-6
- Full rebuild of coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar  1 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5.2-3
- Rediff patches (#894606#c15)
- Use license macro (#894606#c14)
- Do not mix rpm macros and rpm shell variables (#894606#c14)

* Sat Feb 28 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5.2-2
- Correct make check.

* Sat Feb 28 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.5.2-1
- Update to latest upstream release.

* Sat Sep 20 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.7-1
- Update to latest upstream release
- Remove module name from description
- Create doc subpackage

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.3-4
- Update to run make check (#894610#c4).

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.3-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.3-2
- Rename package to coin-or-Couenne.
- Do not package Thirdy party data or data without clean license.

* Sat Sep 29 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.4.3-1
- Initial coinor-Couenne spec.
