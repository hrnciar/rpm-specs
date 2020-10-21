%global packname bench
%global packver  1.1.1
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((ggbeeswarm|ggplot2|ggridges)\\)

# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_without bootstrap

Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          High Precision Timing of R Expressions

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-glue, R-methods, R-pillar, R-profmem, R-rlang >= 0.2.0, R-stats, R-tibble, R-utils
# Suggests:  R-covr, R-dplyr, R-forcats, R-ggbeeswarm, R-ggplot2, R-ggridges, R-mockery, R-parallel, R-scales, R-testthat, R-tidyr >= 0.8.1, R-vctrs, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-glue
BuildRequires:    R-methods
BuildRequires:    R-pillar
BuildRequires:    R-profmem
BuildRequires:    R-rlang >= 0.2.0
BuildRequires:    R-stats
BuildRequires:    R-tibble
BuildRequires:    R-utils
BuildRequires:    R-mockery
BuildRequires:    R-parallel
BuildRequires:    R-testthat
%if %{without bootstrap}
BuildRequires:    R-dplyr
BuildRequires:    R-forcats
BuildRequires:    R-ggbeeswarm
BuildRequires:    R-ggplot2
BuildRequires:    R-ggridges
BuildRequires:    R-scales
BuildRequires:    R-tidyr >= 0.8.1
BuildRequires:    R-vctrs
BuildRequires:    R-withr
%endif

%description
Tools to accurately benchmark and analyze execution times for R expressions.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
# RMySQL/RPostgreSQL are old wrappers, so won't be packaged by me at least.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


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
%{rlibdir}/%{packname}/examples
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Sun Sep 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
