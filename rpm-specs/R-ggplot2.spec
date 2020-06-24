%global packname  ggplot2
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((Hmisc|maptools|profvis|quantreg|sf|vdiffr)\\)

%bcond_with check

# Not available or loops.
%global with_suggests 0

Name:             R-%{packname}
Version:          3.2.1
Release:          3%{?dist}
Summary:          Create Elegant Data Visualisations Using the Grammar of Graphics

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Patch0001:        0001-Don-t-run-Hmisc-examples.patch
Patch0002:        0002-Skip-vdiffr-tests-if-not-installed.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-digest, R-grDevices, R-grid, R-gtable >= 0.1.1, R-lazyeval, R-MASS, R-mgcv, R-reshape2, R-rlang >= 0.3.0, R-scales >= 0.5.0, R-stats, R-tibble, R-viridisLite, R-withr >= 2.0.0
# Suggests:  R-covr, R-dplyr, R-ggplot2movies, R-hexbin, R-Hmisc, R-knitr, R-lattice, R-mapproj, R-maps, R-maptools, R-multcomp, R-munsell, R-nlme, R-profvis, R-quantreg, R-rgeos, R-rmarkdown, R-rpart, R-sf >= 0.7-3, R-svglite >= 1.2.0.9001, R-testthat >= 0.11.0, R-vdiffr >= 0.3.0
# LinkingTo:
# Enhances:

BuildArch:        noarch

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-digest
BuildRequires:    R-grDevices
BuildRequires:    R-grid
BuildRequires:    R-gtable >= 0.1.1
BuildRequires:    R-lazyeval
BuildRequires:    R-MASS
BuildRequires:    R-mgcv
BuildRequires:    R-reshape2
BuildRequires:    R-rlang >= 0.3.0
BuildRequires:    R-scales >= 0.5.0
BuildRequires:    R-stats
BuildRequires:    R-tibble
BuildRequires:    R-viridisLite
BuildRequires:    R-withr >= 2.0.0
BuildRequires:    R-hexbin
BuildRequires:    R-knitr
BuildRequires:    R-lattice
BuildRequires:    R-mapproj
BuildRequires:    R-maps
BuildRequires:    R-multcomp
BuildRequires:    R-munsell
BuildRequires:    R-nlme
BuildRequires:    R-rgeos
BuildRequires:    R-rmarkdown
BuildRequires:    R-rpart
BuildRequires:    R-testthat >= 0.11.0
%if %{with_suggests} || %{fedora} > 29
BuildRequires:    R-dplyr
BuildRequires:    R-ggplot2movies
BuildRequires:    R-svglite >= 1.2.0.9001
%endif
%if %{with_suggests}
BuildRequires:    R-Hmisc
BuildRequires:    R-maptools
BuildRequires:    R-profvis
BuildRequires:    R-quantreg
BuildRequires:    R-sf >= 0.7.3
BuildRequires:    R-vdiffr >= 0.3.0
%endif

%description
A system for 'declaratively' creating graphics, based on "The Grammar of
Graphics". You provide the data, tell 'ggplot2' how to map variables to
aesthetics, what graphical primitives to use, and it takes care of the
details.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%if ! %{with_suggests}
%patch0001 -p1
%patch0002 -p1
%endif

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
%if %{with check}
export LANG=C.UTF-8
%if %{with_suggests} || %{fedora} > 29
ARGS=--ignore-vignettes
%else
ARGS="--no-examples --ignore-vignettes"
%endif
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} $ARGS
%endif
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 3.2.1-3
- ignore vignettes... actually, just disable check
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.1-1
- Update to latest version

* Wed Mar 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.0-1
- initial package for Fedora
