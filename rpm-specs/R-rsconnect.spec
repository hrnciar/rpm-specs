%global packname  rsconnect
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((plumber)\\)

# Not yet available.
%global with_suggests 0

Name:             R-%{packname}
Version:          0.8.16
Release:          3%{?dist}
Summary:          Deployment Interface for R Markdown Documents and Shiny Applications

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-curl, R-digest, R-jsonlite, R-openssl, R-packrat >= 0.4.8-1, R-rstudioapi >= 0.5, R-yaml >= 2.1.5
# Suggests:  R-RCurl, R-callr, R-httpuv, R-knitr, R-plumber >= 0.3.2, R-reticulate, R-rmarkdown >= 1.1, R-shiny, R-sourcetools, R-testthat, R-xtable
# LinkingTo:
# Enhances:

BuildArch:        noarch

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-curl
BuildRequires:    R-digest
BuildRequires:    R-jsonlite
BuildRequires:    R-openssl
BuildRequires:    R-packrat >= 0.4.8.1
BuildRequires:    R-rstudioapi >= 0.5
BuildRequires:    R-yaml >= 2.1.5
BuildRequires:    R-RCurl
BuildRequires:    R-callr
BuildRequires:    R-httpuv
BuildRequires:    R-knitr
%if %{with_suggests}
BuildRequires:    R-plumber >= 0.3.2
%endif
BuildRequires:    R-reticulate
BuildRequires:    R-rmarkdown >= 1.1
BuildRequires:    R-shiny
BuildRequires:    R-sourcetools
BuildRequires:    R-testthat
BuildRequires:    R-xtable

%description
Programmatic deployment interface for 'RPubs', 'shinyapps.io', and 'RStudio
Connect'. Supported content types include R Markdown documents, Shiny
applications, Plumber APIs, plots, and static web content.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Remove bundled fallback cert store.
rm inst/cert/cacert.pem
sed -i -e '/cacert.pem/d' MD5

# Remove extra shebang.
sed -i -e '1d' inst/resources/environment.py
popd


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
%{rlibdir}/%{packname}/cert
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/resources


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.16-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.16-1
- Update to latest version

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.15-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.13-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.13-1
- initial package for Fedora
