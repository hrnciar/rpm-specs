%global packname profvis
%global packver  0.3.6
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.6
Release:          6%{?dist}
Summary:          Interactive Visualizations for Profiling R Code

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-htmlwidgets >= 0.3.2, R-stringr
# Suggests:  R-knitr, R-ggplot2, R-rmarkdown, R-testthat, R-devtools, R-shiny, R-htmltools
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-htmlwidgets >= 0.3.2
BuildRequires:    R-stringr
BuildRequires:    R-knitr
BuildRequires:    R-ggplot2
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-devtools
BuildRequires:    R-shiny
BuildRequires:    R-htmltools

Provides:         bundled(js-highlight) = 6.2.0
Provides:         bundled(js-jquery1) = 1.12.4
Provides:         bundled(js-d3) = 3.5.6

%description
Interactive visualizations for profiling R code.


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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/htmlwidgets
%license %{rlibdir}/%{packname}/htmlwidgets/lib/d3/LICENSE
%license %{rlibdir}/%{packname}/htmlwidgets/lib/highlight/LICENSE
%{rlibdir}/%{packname}/shinymodule


%changelog
* Thu Aug 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.6-6
- Re-bundle js-jquery1, fixes rhbz#1866721

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.6-3
- rebuild for R 4

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.6-2
- Fix link to jQuery

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.6-1
- initial package for Fedora
