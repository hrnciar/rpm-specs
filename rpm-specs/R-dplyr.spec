%global packname dplyr
%global packver  1.0.2
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((Lahman|RMySQL|RPostgreSQL)\\)

# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_with bootstrap

Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          A Grammar of Data Manipulation

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ellipsis, R-generics, R-glue >= 1.3.2, R-lifecycle >= 0.2.0, R-magrittr >= 1.5, R-methods, R-R6, R-rlang >= 0.4.7, R-tibble >= 2.1.3, R-tidyselect >= 1.1.0, R-utils, R-vctrs >= 0.3.2
# Suggests:  R-bench, R-broom, R-callr, R-covr, R-DBI, R-dbplyr >= 1.4.3, R-knitr, R-Lahman, R-lobstr, R-microbenchmark, R-nycflights13, R-purrr, R-rmarkdown, R-RMySQL, R-RPostgreSQL, R-RSQLite, R-testthat >= 2.1.0, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ellipsis
BuildRequires:    R-generics
BuildRequires:    R-glue >= 1.3.2
BuildRequires:    R-lifecycle >= 0.2.0
BuildRequires:    R-magrittr >= 1.5
BuildRequires:    R-methods
BuildRequires:    R-R6
BuildRequires:    R-rlang >= 0.4.7
BuildRequires:    R-tibble >= 2.1.3
BuildRequires:    R-tidyselect >= 1.1.0
BuildRequires:    R-utils
BuildRequires:    R-vctrs >= 0.3.2
BuildRequires:    R-callr
BuildRequires:    R-DBI
BuildRequires:    R-knitr
BuildRequires:    R-lobstr
BuildRequires:    R-microbenchmark
BuildRequires:    R-purrr
BuildRequires:    R-rmarkdown
BuildRequires:    R-RSQLite
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-withr
%if %{without bootstrap}
BuildRequires:    R-bench
BuildRequires:    R-broom
BuildRequires:    R-dbplyr >= 1.4.3
BuildRequires:    R-nycflights13
%endif

Obsoletes: %{name}-devel < 0.8.5-4

%description
A fast, consistent tool for working with data frame like objects, both in
memory and out of memory.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
# Lahman is not yet packaged.
# RMySQL/RPostgreSQL are old wrappers, so won't be packaged by me at least.
sed -i \
    -e 's/covr, //g' \
    -e 's/Lahman, //g' \
    -e 's/RMySQL, RPostgreSQL, //g' \
    %{packname}/DESCRIPTION


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


%changelog
* Sat Sep 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version (#1841868)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.5-2
- rebuild for R 4
- broom is now an R package so it does not need to be excluded
- remove from BuildRequires other packages that are not yet available

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
