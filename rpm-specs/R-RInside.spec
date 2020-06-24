%global packname RInside

Name:		R-%{packname}
Version:	0.2.16
Release:	2%{?dist}
Summary:	C++ Classes to Embed R in C++ (and C) Applications

License:	GPLv2+
URL:		https://cran.r-project.org/package=%{packname}
Source0:	%{url}&version=%{version}#/%{packname}_%{version}.tar.gz
#		Adapt RInsideLdFlags function to Fedora packaging (no static
#		library, shared library moved to default library path)
Patch0:		%{name}-LdFlags.patch

BuildRequires:	R-core-devel
BuildRequires:	R-Rcpp-devel

%if %{?fedora}%{!?fedora:0} >= 31 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	R-rpm-macros
%else
Requires:	R-core%{?_isa}
Requires:	R-Rcpp%{?_isa}
%endif

%description
The RInside packages makes it easier to have "R inside" your C++
application by providing a C++ wrapper class providing the R
interpreter.

%package devel
Summary:	RInside Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	R-core-devel%{?_isa}
Requires:	R-Rcpp-devel%{?_isa}

%description devel
Header files for RInside.

%package examples
Summary:	RInside Examples
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description examples
Numerous examples are provided in the nine sub-directories of the
examples directory of the installed package: standard, mpi (for
parallel computing), qt (showing how to embed RInside inside a Qt GUI
application), wt (showing how to build a "web-application" using the
Wt toolkit), armadillo (for RInside use with RcppArmadillo), eigen
(for RInside use with RcppEigen) and 'c_interface' for a basic C
interface and 'Ruby' illustration.

%prep
%setup -q -c
%patch0 -p0

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css
rm -rf %{packname}/inst/lib

rm %{buildroot}%{_libdir}/R/library/%{packname}/lib/lib%{packname}.a
mv %{buildroot}%{_libdir}/R/library/%{packname}/lib/lib%{packname}.so \
   %{buildroot}%{_libdir}
rmdir %{buildroot}%{_libdir}/R/library/%{packname}/lib

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/NEWS.Rd
%doc %{_libdir}/R/library/%{packname}/THANKS
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/lib%{packname}.so

%files devel
%{_libdir}/R/library/%{packname}/include

%files examples
%{_libdir}/R/library/%{packname}/examples

%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.2.16-2
- rebuild for R 4

* Fri Mar 20 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.16-1
- New release 0.2.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.15-5
- Unify specfile

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.15-4
- Remove explicit dependencies provided by automatic dependency generator

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.15-3
- Rebuild with automatic Provides

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.15-1
- New release 0.2.15

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.2.14-7
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.14-5
- Rebuild for R-Rcpp 0.12.14

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 0.2.14-2
- rebuild for R 3.4.0

* Mon May 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.14-1
- New release 0.2.14
- Drop patches R-RInside-ExcludeVars.patch and R-RInside-ldflags.patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 10 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2.13-3
- Rebuild for R-Rcpp 0.12.4

* Wed Mar 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2.13-2
- Adapt RInsideLdFlags function to Fedora packaging

* Fri Feb 05 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2.13-1
- Initial package creation
