%global packname bookdown
%global packver  0.21
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.21
Release:          1%{?dist}
Summary:          Authoring Books and Technical Documents with R Markdown

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-htmltools >= 0.3.6, R-knitr >= 1.22, R-rmarkdown >= 2.4, R-xfun >= 0.13, R-tinytex >= 0.12, R-yaml >= 2.1.19
# Suggests:  R-htmlwidgets, R-rstudioapi, R-miniUI, R-rsconnect >= 0.4.3, R-servr >= 0.13, R-shiny, R-testit >= 0.9, R-tufte, R-webshot
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-htmltools >= 0.3.6
BuildRequires:    R-knitr >= 1.22
BuildRequires:    R-rmarkdown >= 2.4
BuildRequires:    R-xfun >= 0.13
BuildRequires:    R-tinytex >= 0.12
BuildRequires:    R-yaml >= 2.1.19
BuildRequires:    R-htmlwidgets
BuildRequires:    R-rstudioapi
BuildRequires:    R-miniUI
BuildRequires:    R-rsconnect >= 0.4.3
BuildRequires:    R-servr >= 0.13
BuildRequires:    R-shiny
BuildRequires:    R-testit >= 0.9
BuildRequires:    R-tufte
# Not available
# BuildRequires:    R-webshot

%description
Output formats and utilities for authoring books and technical documents with R
Markdown.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/resources
%{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/templates


%changelog
* Tue Oct 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.21-1
- Update to latest version (#1887703)

* Fri Jun 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.20-1
- initial package for Fedora
