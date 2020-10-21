%global packname devtools
%global packver  2.3.2
%global rlibdir  %{_datadir}/R/library

# Not available yet.
%bcond_with suggests

%if %{without suggests}
%global __suggests_exclude ^R\\((BiocManager)\\)
%endif

Name:             R-%{packname}
Version:          2.3.2
Release:          1%{?dist}
Summary:          Tools to Make Developing R Packages Easier

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-usethis >= 1.6.3
# Imports:   R-callr >= 3.4.4, R-cli >= 2.0.2, R-covr >= 3.5.1, R-desc >= 1.2.0, R-DT >= 0.15, R-ellipsis >= 0.3.1, R-httr >= 1.4.2, R-jsonlite >= 1.7.1, R-memoise >= 1.1.0, R-pkgbuild >= 1.1.0, R-pkgload >= 1.1.0, R-rcmdcheck >= 1.3.3, R-remotes >= 2.2.0, R-rlang >= 0.4.7, R-roxygen2 >= 7.1.1, R-rstudioapi >= 0.11, R-rversions >= 2.0.2, R-sessioninfo >= 1.1.1, R-stats, R-testthat >= 2.3.2, R-tools, R-utils, R-withr >= 2.2.0
# Suggests:  R-BiocManager >= 1.30.10, R-curl >= 4.3, R-digest >= 0.6.25, R-foghorn >= 1.3.1, R-gmailr >= 1.0.0, R-knitr >= 1.29, R-lintr >= 2.0.1, R-MASS, R-mockery >= 0.4.2, R-pingr >= 2.0.1, R-pkgdown >= 1.6.1, R-rhub >= 1.1.1, R-rmarkdown >= 2.3, R-spelling >= 2.1
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-usethis >= 1.6.3
BuildRequires:    R-callr >= 3.4.4
BuildRequires:    R-cli >= 2.0.2
BuildRequires:    R-covr >= 3.5.1
BuildRequires:    R-desc >= 1.2.0
BuildRequires:    R-DT >= 0.15
BuildRequires:    R-ellipsis >= 0.3.1
BuildRequires:    R-httr >= 1.4.2
BuildRequires:    R-jsonlite >= 1.7.1
BuildRequires:    R-memoise >= 1.1.0
BuildRequires:    R-pkgbuild >= 1.1.0
BuildRequires:    R-pkgload >= 1.1.0
BuildRequires:    R-rcmdcheck >= 1.3.3
BuildRequires:    R-remotes >= 2.2.0
BuildRequires:    R-rlang >= 0.4.7
BuildRequires:    R-roxygen2 >= 7.1.1
BuildRequires:    R-rstudioapi >= 0.11
BuildRequires:    R-rversions >= 2.0.2
BuildRequires:    R-sessioninfo >= 1.1.1
BuildRequires:    R-stats
BuildRequires:    R-testthat >= 2.3.2
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-withr >= 2.2.0
%if %{with suggests}
BuildRequires:    R-BiocManager >= 1.30.10
%endif
BuildRequires:    R-curl >= 4.3
BuildRequires:    R-digest >= 0.6.25
BuildRequires:    R-foghorn >= 1.3.1
BuildRequires:    R-gmailr >= 1.0.0
BuildRequires:    R-knitr >= 1.29
BuildRequires:    R-lintr >= 2.0.1
BuildRequires:    R-MASS
BuildRequires:    R-mockery >= 0.4.2
BuildRequires:    R-pingr >= 2.0.1
BuildRequires:    R-pkgdown >= 1.6.1
BuildRequires:    R-rhub >= 1.1.1
BuildRequires:    R-rmarkdown >= 2.3
BuildRequires:    R-spelling >= 2.1

%description
Collection of package development tools.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/rstudio


%changelog
* Fri Sep 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.2-1
- Update to latest version (#1880296)

* Sun Aug 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.1-1
- Update to latest version (rhbz#1823027)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.1.0-2
- rebuild for R 4

* Sat Feb 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Sat Feb 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-3
- Remove explicit runtime requirements

* Thu Jun 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Fix incorrect files list

* Wed May 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- initial package for Fedora
