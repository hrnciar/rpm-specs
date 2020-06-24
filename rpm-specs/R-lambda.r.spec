%global packname lambda.r
%global packver 1.2.4

Name:             R-%{packname}
Version:          %{packver}
Release:          3%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{packver}.tar.gz
License:          LGPLv3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Summary:          Modeling data with functional programming
BuildRequires:    R-devel >= 3.0.0, tetex-latex, R-RUnit, R-testit, R-formatR
BuildArch:        noarch

%description
A language extension to efficiently write functional programs in R. Syntax
extensions include multi-part function definitions, pattern matching,
guard statements, built-in (optional) type safety.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_datadir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/R

%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.4-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Tom Callaway <spot@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-2
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 31 2019 Tom Callaway <spot@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 1.2-1
- update to 1.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.1.9-1
- initial package
