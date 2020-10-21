%global packname usethis
%global packver  1.6.3
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.6.3
Release:          1%{?dist}
Summary:          Automate Package and Project Setup

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Skip-some-more-tests-if-offline.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-clipr >= 0.3.0, R-cli, R-crayon, R-curl >= 2.7, R-desc, R-fs >= 1.3.0, R-gh >= 1.1.0, R-git2r >= 0.23, R-glue >= 1.3.0, R-purrr, R-rematch2, R-rlang >= 0.4.3, R-rprojroot >= 1.2, R-rstudioapi, R-stats, R-utils, R-whisker, R-withr, R-yaml
# Suggests:  R-covr, R-knitr, R-magick, R-pkgdown >= 1.4.0, R-rmarkdown, R-roxygen2, R-spelling >= 1.2, R-styler >= 1.2.0, R-testthat >= 2.1.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-clipr >= 0.3.0
BuildRequires:    R-cli
BuildRequires:    R-crayon
BuildRequires:    R-curl >= 2.7
BuildRequires:    R-desc
BuildRequires:    R-fs >= 1.3.0
BuildRequires:    R-gh >= 1.1.0
BuildRequires:    R-git2r >= 0.23
BuildRequires:    R-glue >= 1.3.0
BuildRequires:    R-purrr
BuildRequires:    R-rematch2
BuildRequires:    R-rlang >= 0.4.3
BuildRequires:    R-rprojroot >= 1.2
BuildRequires:    R-rstudioapi
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-whisker
BuildRequires:    R-withr
BuildRequires:    R-yaml
BuildRequires:    R-knitr
BuildRequires:    R-magick
BuildRequires:    R-pkgdown >= 1.4.0
BuildRequires:    R-rmarkdown
BuildRequires:    R-roxygen2
BuildRequires:    R-spelling >= 1.2
BuildRequires:    R-styler >= 1.2.0
BuildRequires:    R-testthat >= 2.1.0

%description
Automate package and project setup tasks that are otherwise performed manually.
This includes setting up unit testing, test coverage, continuous integration,
Git, GitHub, licenses, Rcpp, RStudio projects, and more.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/templates


%changelog
* Fri Sep 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-1
- Update to latest version (#1880138)

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.1-1
- Update to latest version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.1-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- initial package for Fedora
