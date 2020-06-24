%global packname devtools
%global rlibdir  %{_datadir}/R/library

# Not available yet.
%bcond_with suggests

%if %{without suggests}
%global __suggests_exclude ^R\\((BiocManager)\\)
%endif

Name:             R-%{packname}
Version:          2.1.0
Release:          2%{?dist}
Summary:          Tools to Make Developing R Packages Easier

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-usethis >= 1.5.0
# Imports:   R-callr, R-cli, R-digest, R-git2r >= 0.23.0, R-httr >= 0.4, R-jsonlite, R-memoise >= 1.0.0, R-pkgbuild >= 1.0.3, R-pkgload >= 1.0.2, R-rcmdcheck >= 1.3.3, R-remotes >= 2.1.0, R-roxygen2 >= 6.1.1, R-rstudioapi >= 0.7, R-sessioninfo >= 1.1.1, R-stats, R-testthat >= 2.1.1, R-tools, R-utils, R-withr
# Suggests:  R-BiocManager, R-bitops, R-covr >= 3.2.0, R-crayon, R-curl >= 0.9, R-evaluate, R-foghorn >= 1.1.0, R-gmailr > 0.7.0, R-knitr, R-lintr >= 0.2.1, R-mockery, R-pingr, R-MASS, R-pkgdown, R-Rcpp >= 0.10.0, R-rhub >= 1.0.2, R-rmarkdown, R-rversions, R-spelling >= 1.1, R-whisker
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-usethis >= 1.5.0
BuildRequires:    R-callr
BuildRequires:    R-cli
BuildRequires:    R-digest
BuildRequires:    R-git2r >= 0.23.0
BuildRequires:    R-httr >= 0.4
BuildRequires:    R-jsonlite
BuildRequires:    R-memoise >= 1.0.0
BuildRequires:    R-pkgbuild >= 1.0.3
BuildRequires:    R-pkgload >= 1.0.2
BuildRequires:    R-rcmdcheck >= 1.3.3
BuildRequires:    R-remotes >= 2.1.0
BuildRequires:    R-roxygen2 >= 6.1.1
BuildRequires:    R-rstudioapi >= 0.7
BuildRequires:    R-sessioninfo >= 1.1.1
BuildRequires:    R-stats
BuildRequires:    R-testthat >= 2.1.1
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-withr
%if %{with suggests}
BuildRequires:    R-BiocManager
%endif
BuildRequires:    R-bitops
BuildRequires:    R-crayon
BuildRequires:    R-curl >= 0.9
BuildRequires:    R-evaluate
BuildRequires:    R-foghorn >= 1.1.0
BuildRequires:    R-gmailr > 0.7.0
BuildRequires:    R-knitr
BuildRequires:    R-lintr >= 0.2.1
BuildRequires:    R-mockery
BuildRequires:    R-pingr
BuildRequires:    R-MASS
BuildRequires:    R-pkgdown
BuildRequires:    R-Rcpp >= 0.10.0
BuildRequires:    R-rhub >= 1.0.2
BuildRequires:    R-rmarkdown
BuildRequires:    R-rversions
BuildRequires:    R-spelling >= 1.1
BuildRequires:    R-whisker

%description
Collection of package development tools.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr[^,]+, //g' %{packname}/DESCRIPTION


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
%{rlibdir}/%{packname}/templates


%changelog
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
