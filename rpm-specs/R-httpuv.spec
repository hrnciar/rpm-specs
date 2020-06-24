%global packname httpuv
%global packver  1.5.4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Summary:          HTTP and WebSocket Server Library

# Main: GPLv2+; http-parser: MIT; sha1: Public Domain
License:          GPLv2+ and MIT and Public Domain
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Use-unbundled-libuv.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.11.0, R-utils, R-R6, R-promises, R-later >= 0.8.0
# Suggests:  R-testthat, R-callr, R-curl, R-websocket
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.11.0
BuildRequires:    R-utils
BuildRequires:    R-R6
BuildRequires:    R-promises
BuildRequires:    R-later-devel >= 0.8.0
BuildRequires:    R-testthat
BuildRequires:    R-callr
BuildRequires:    R-curl
BuildRequires:    R-websocket
BuildRequires:    R-BH-devel
# Hopefully will be removable in the later releases, but for now it includes
# some patches:
# https://github.com/rstudio/httpuv/pull/93#issuecomment-340802818
Provides:         bundled(http-parser) = 2.7.1
BuildRequires:    libuv-devel >= 1.37.0

%description
Provides low-level socket and protocol support for handling HTTP and
WebSocket requests directly from within R. It is primarily intended as a
building block for other packages, rather than making it particularly easy
to create complete web applications using httpuv alone. httpuv is built on
top of the libuv and http-parser C libraries, both of which were developed
by Joyent, Inc.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
rm -r src/libuv
sed -i '/libuv/d' MD5
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.4-1
- update to 1.5.4
- rebuild for R 4

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.3.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.1-1
- Update to latest version

* Sun Mar 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.0-1
- Update to latest version

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.5.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.5-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4.1-1
- Update to latest version

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.4.3-2
- rebuild for R 3.5.0

* Fri May 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-1
- Update to latest version

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version

* Mon Apr 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version
- Unbundle libuv

* Fri Mar 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.6.2-2
- Fix license and changelog

* Fri Mar 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.6.2-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.5-2
- Apply patch for CVE-2015-0278

* Tue Oct 31 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.5-1
- initial package for Fedora
