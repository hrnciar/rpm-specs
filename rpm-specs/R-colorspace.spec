%global packname  colorspace
%global packvers  1.4-1
%global rlibdir  %{_libdir}/R/library

%global __suggests_exclude ^R\\((kernlab|rcartocolor|scico|shinyjs|vcd|viridis|wesanderson)\\)

# Not yet available.
%global with_suggests 0

Name:             R-%{packname}
Version:          1.4.1
Release:          6%{?dist}
Summary:          A Toolbox for Manipulating and Assessing Colors and Palettes

License:          BSD
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packvers}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-graphics, R-grDevices, R-stats
# Suggests:  R-datasets, R-utils, R-KernSmooth, R-MASS, R-kernlab, R-mvtnorm, R-vcd, R-tcltk, R-shiny, R-shinyjs, R-ggplot2, R-dplyr, R-scales, R-grid, R-png, R-jpeg, R-knitr, R-rmarkdown, R-RColorBrewer, R-rcartocolor, R-scico, R-viridis, R-wesanderson
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-stats
%if %{with_suggests}
BuildRequires:    R-datasets
BuildRequires:    R-utils
BuildRequires:    R-KernSmooth
BuildRequires:    R-MASS
BuildRequires:    R-kernlab
BuildRequires:    R-mvtnorm
BuildRequires:    R-vcd
BuildRequires:    R-tcltk
BuildRequires:    R-shiny
BuildRequires:    R-shinyjs
BuildRequires:    R-ggplot2
BuildRequires:    R-dplyr
BuildRequires:    R-scales
BuildRequires:    R-grid
BuildRequires:    R-png
BuildRequires:    R-jpeg
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-RColorBrewer
BuildRequires:    R-rcartocolor
BuildRequires:    R-scico
BuildRequires:    R-viridis
BuildRequires:    R-wesanderson
%endif

%description
Carries out mapping between assorted color spaces including RGB, HSV,
HLS, CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB and polar CIELAB.
Qualitative, sequential, and diverging color palettes based on HCL colors
are provided along with corresponding ggplot2 color scales. Color palette
choice is aided by an interactive app (with either a Tcl/Tk or a shiny
GUI) and shiny apps with an HCL color picker and a color vision
deficiency emulator. Plotting functions for displaying and assessing
palettes include color swatches, visualizations of the HCL space, and
trajectories in HCL and/or RGB spectrum. Color manipulation functions
include: desaturation, lightening/darkening, mixing, and simulation of
color vision deficiencies (deutanomaly, protanomaly, tritanomaly).


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes --no-examples
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
%{rlibdir}/%{packname}/cvdemulator
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/hclcolorpicker
%{rlibdir}/%{packname}/hclwizard
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.3.2-2
- rebuild for R 3.5.0

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.2-1
- initial package for Fedora
