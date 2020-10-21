%global packname import
%global packver  1.2.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          An Import Mechanism for R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-knitr, R-rmarkdown, R-magrittr, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-magrittr
BuildRequires:    R-testthat

%description
Alternative mechanism for importing objects from packages and R modules.
The syntax allows for importing multiple objects with a single command in
an expressive way. The import package bridges some of the gap between using
library (or require) and direct (single-object) imports. Furthermore the
imported objects are not placed in the current environment.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Sep 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Update to latest version (#1882439)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-2
- Fix some file line endings

* Tue Apr 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
