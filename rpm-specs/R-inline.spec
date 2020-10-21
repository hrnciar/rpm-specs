%global packname inline

Name:		R-%{packname}
Version:	0.3.16
Release:	1%{?dist}
Summary:	Functions to Inline C, C++, Fortran Function Calls from R

License:	LGPLv2+
URL:		https://cran.r-project.org/package=%{packname}
Source0:	%{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	R-core-devel

%if %{?fedora}%{!?fedora:0} >= 31 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	R-rpm-macros
%else
Requires:	R-core
%endif

%description
Functionality to dynamically define R functions and S4 methods with
'inlined' C, C++ or Fortran code supporting the .C and .Call calling
conventions.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_datadir}/R/library %{packname}
rm -f %{buildroot}%{_datadir}/R/library/R.css

%check
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/NEWS.Rd
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help

%changelog
* Wed Oct 14 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.16-1
- Update to version 0.3.16

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.15-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.15-6
- Unify specfile

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.15-5
- Remove explicit dependencies provided by automatic dependency generator

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.15-4
- Rebuild with automatic Provides

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.3.15-1
- Update to version 0.3.15

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.3.14-1
- Initial package creation
