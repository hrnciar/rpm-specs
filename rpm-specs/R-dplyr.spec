%global packname dplyr
%global packver  0.8.5
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((Lahman|RMySQL|RPostgreSQL|broom)\\)

# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_without bootstrap

Name:             R-%{packname}
Version:          0.8.5
Release:          2%{?dist}
Summary:          A Grammar of Data Manipulation

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ellipsis, R-assertthat >= 0.2.0, R-glue >= 1.3.0, R-magrittr >= 1.5, R-methods, R-pkgconfig, R-R6, R-Rcpp >= 1.0.1, R-rlang >= 0.4.0, R-tibble >= 2.0.0, R-tidyselect >= 0.2.5, R-utils
# Suggests:  R-bit64, R-callr, R-covr, R-crayon >= 1.3.4, R-DBI, R-dbplyr, R-dtplyr, R-ggplot2, R-hms, R-knitr, R-Lahman, R-lubridate, R-MASS, R-mgcv, R-microbenchmark, R-nycflights13, R-rmarkdown, R-RMySQL, R-RPostgreSQL, R-RSQLite, R-testthat, R-withr, R-broom, R-purrr, R-readr
# LinkingTo: R-BH, R-plogr >= 0.2.0, R-Rcpp >= 1.0.1
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ellipsis
BuildRequires:    R-assertthat >= 0.2.0
BuildRequires:    R-glue >= 1.3.0
BuildRequires:    R-magrittr >= 1.5
BuildRequires:    R-methods
BuildRequires:    R-pkgconfig
BuildRequires:    R-R6
BuildRequires:    R-Rcpp-devel >= 1.0.1
BuildRequires:    R-rlang >= 0.4.0
BuildRequires:    R-tibble >= 2.0.0
BuildRequires:    R-tidyselect >= 0.2.5
BuildRequires:    R-utils
BuildRequires:    R-BH-devel
BuildRequires:    R-plogr-devel >= 0.2.0
BuildRequires:    R-bit64
BuildRequires:    R-callr
BuildRequires:    R-crayon >= 1.3.4
BuildRequires:    R-DBI
BuildRequires:    R-hms
BuildRequires:    R-knitr
BuildRequires:    R-lubridate
BuildRequires:    R-MASS
BuildRequires:    R-mgcv
BuildRequires:    R-microbenchmark
BuildRequires:    R-rmarkdown
BuildRequires:    R-RSQLite
BuildRequires:    R-testthat
BuildRequires:    R-withr
BuildRequires:    R-purrr
BuildRequires:    R-readr
%if %{without bootstrap}
BuildRequires:    R-dbplyr
BuildRequires:    R-dtplyr
BuildRequires:    R-ggplot2
BuildRequires:    R-Lahman
BuildRequires:    R-nycflights13
BuildRequires:    R-RMySQL
BuildRequires:    R-RPostgreSQL
BuildRequires:    R-broom
%endif

%description
A fast, consistent tool for working with data frame like objects, both in
memory and out of memory.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%if %{without bootstrap}
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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.5-2
- rebuild for R 4

* Sun Mar 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.5-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.4-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.3-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0.1-1
- initial package for Fedora
