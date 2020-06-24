%global packname  websocket
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          'WebSocket' Client Library

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
# For testing only.
Source1:          echo.py
# https://github.com/rstudio/websocket/issues/59
Patch0001:        0001-Unbundle-websocketpp.patch
# For no-network testing.
Patch0002:        0002-Use-local-echo-server-for-testing-websockets.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp, R-R6, R-later
# Suggests:  R-testthat, R-knitr, R-rmarkdown
# LinkingTo: R-Rcpp, R-BH, R-AsioHeaders
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-R6
BuildRequires:    R-later
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-BH-devel
BuildRequires:    R-AsioHeaders-devel
BuildRequires:    pkgconfig(openssl)
BuildRequires:    pkgconfig(websocketpp)
BuildRequires:    python3dist(websockets)

%description
Provides a WebSocket client interface for R. WebSocket is a protocol for
low-overhead real-time communication:
<https://en.wikipedia.org/wiki/WebSocket>.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Unbundle websocketpp
%patch0001 -p1
# Disable network usage
%patch0002 -p1

# Fix executable bit
chmod -x man/figures/websocket_logo.svg
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{__python3} %SOURCE1 &
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


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
