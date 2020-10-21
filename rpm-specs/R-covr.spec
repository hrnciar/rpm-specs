%global packname covr
%global packver  3.5.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.5.1
Release:          1%{?dist}
Summary:          Test Coverage for Packages

License:          GPLv3 and MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-digest, R-stats, R-utils, R-jsonlite, R-rex, R-httr, R-crayon, R-withr >= 1.0.2, R-yaml
# Suggests:  R-R6, R-curl, R-knitr, R-rmarkdown, R-htmltools, R-DT >= 0.2, R-testthat, R-rlang, R-rstudioapi >= 0.2, R-xml2 >= 1.0.0, R-parallel, R-memoise, R-mockery
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-digest
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-jsonlite
BuildRequires:    R-rex
BuildRequires:    R-httr
BuildRequires:    R-crayon
BuildRequires:    R-withr >= 1.0.2
BuildRequires:    R-yaml
BuildRequires:    R-R6
BuildRequires:    R-curl
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-htmltools
BuildRequires:    R-DT >= 0.2
BuildRequires:    R-testthat
BuildRequires:    R-rlang
BuildRequires:    R-rstudioapi >= 0.2
BuildRequires:    R-xml2 >= 1.0.0
BuildRequires:    R-parallel
BuildRequires:    R-memoise
BuildRequires:    R-mockery

# MIT; inst/www/shared/bootstrap
Provides:         bundled(xstatic-bootstrap-common) = 3.3.5
# MIT; inst/www/shared/highlight.js
Provides:         bundled(js-highlight) = 6.2

%description
Track and report code coverage for your package and (optionally) upload the
results to a coverage service like 'Codecov' <https://codecov.io> or
'Coveralls' <https://coveralls.io>. Code coverage is a measure of the amount of
code being exercised by a set of tests. It is an indirect measure of test
quality and completeness. This package is compatible with any testing
methodology or framework and tracks coverage of both R code and compiled
C/C++/FORTRAN code.


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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/www


%changelog
* Wed Sep 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.5.1-1
- Update to latest version (#1879773)

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.5.0-1
- initial package for Fedora
