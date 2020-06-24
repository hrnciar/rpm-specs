%global packname lintr
%global packver  2.0.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          A 'Linter' for R Code

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-rex, R-crayon, R-codetools, R-cyclocomp, R-testthat >= 2.2.1, R-digest, R-rstudioapi >= 0.2, R-httr >= 1.2.1, R-jsonlite, R-knitr, R-stats, R-utils, R-xml2 >= 1.0.0, R-xmlparsedata >= 1.0.3
# Suggests:  R-rmarkdown, R-mockery
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-rex
BuildRequires:    R-crayon
BuildRequires:    R-codetools
BuildRequires:    R-cyclocomp
BuildRequires:    R-testthat >= 2.2.1
BuildRequires:    R-digest
BuildRequires:    R-rstudioapi >= 0.2
BuildRequires:    R-httr >= 1.2.1
BuildRequires:    R-jsonlite
BuildRequires:    R-knitr
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-xml2 >= 1.0.0
BuildRequires:    R-xmlparsedata >= 1.0.3
BuildRequires:    R-rmarkdown
BuildRequires:    R-mockery

%description
Checks adherence to a given style, syntax errors and possible semantic
issues.  Supports on the fly checking of R code edited with 'RStudio IDE',
'Emacs', 'Vim', 'Sublime Text' and 'Atom'.


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
%{rlibdir}/%{packname}/example/
%{rlibdir}/%{packname}/rstudio/
%{rlibdir}/%{packname}/syntastic/


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.0.1-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- initial package for Fedora
