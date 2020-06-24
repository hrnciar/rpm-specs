%global packname pkgdown
%global packver  1.5.1
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((leaflet|rticles)\\)

# Tests and vignettes use the network.
%bcond_with network

# Not available yet.
%global with_loop 0

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          Make Static HTML Documentation for a Package

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-callr >= 2.0.2, R-cli, R-crayon, R-desc, R-digest, R-evaluate, R-fs >= 1.3.0, R-fansi, R-highlight, R-httr, R-magrittr, R-MASS, R-memoise, R-openssl, R-purrr, R-processx, R-rematch2, R-rlang >= 0.3.0, R-rmarkdown >= 1.1.9007, R-rstudioapi, R-tibble, R-tools, R-whisker, R-withr, R-xml2 >= 1.3.1, R-yaml
# Suggests:  R-covr, R-htmlwidgets, R-jsonlite, R-knitr, R-leaflet, R-pkgload >= 1.0.2, R-testthat >= 2.1.0, R-rticles, R-rsconnect
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-callr >= 2.0.2
BuildRequires:    R-cli
BuildRequires:    R-crayon
BuildRequires:    R-desc
BuildRequires:    R-digest
BuildRequires:    R-evaluate
BuildRequires:    R-fs >= 1.3.0
BuildRequires:    R-fansi
BuildRequires:    R-highlight
BuildRequires:    R-httr
BuildRequires:    R-magrittr
BuildRequires:    R-MASS
BuildRequires:    R-memoise
BuildRequires:    R-openssl
BuildRequires:    R-purrr
BuildRequires:    R-processx
BuildRequires:    R-rematch2
BuildRequires:    R-rlang >= 0.3.0
BuildRequires:    R-rmarkdown >= 1.1.9007
BuildRequires:    R-rstudioapi
BuildRequires:    R-tibble
BuildRequires:    R-tools
BuildRequires:    R-whisker
BuildRequires:    R-withr
BuildRequires:    R-xml2 >= 1.3.1
BuildRequires:    R-yaml
BuildRequires:    R-htmlwidgets
BuildRequires:    R-jsonlite
BuildRequires:    R-knitr
BuildRequires:    R-pkgload >= 1.0.2
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-rsconnect
%if %{with_loop}
BuildRequires:    R-leaflet
BuildRequires:    R-rticles
%endif

%description
Generate an attractive and useful website from a source package. pkgdown
converts your documentation, vignettes, README, and more to HTML making it easy
to share information about your package online.


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
%if %{without network}
ARGS='--no-tests --no-vignettes'
%endif
%if %{with_loop}
%{_bindir}/R CMD check %{packname} $ARGS
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} $ARGS
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
%{rlibdir}/%{packname}/assets
%{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/templates


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.1-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.1-1
- Update to latest version

* Thu Mar 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-2
- Exclude Suggests for unavailable packages

* Wed Sep 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version

* Sun Sep 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- initial package for Fedora
