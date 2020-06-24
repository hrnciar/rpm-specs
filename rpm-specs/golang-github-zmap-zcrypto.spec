# Generated by go2rpm 1
%bcond_without check
%bcond_with bootstrap

# https://github.com/zmap/zcrypto
%global goipath         github.com/zmap/zcrypto
%global commit          4d171263147247189025e53b13fd2d5828d59755

%gometa

%global goipaths0       github.com/zmap/zcrypto
%global goipathsex0     github.com/zmap/zcrypto/verifier

%if %{without bootstrap}
%global goipaths1       github.com/zmap/zcrypto/verifier
%endif

%global common_description %{expand:
Liberal Go TLS + X.509 Library for Research.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md ct/README.md x509/README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Liberal Go TLS + X.509 Library for Research

# Upstream license specification: Apache-2.0
# Main library: ASL 2.0
# Code from Google: ISC
# util/isURL.go: MIT
License:        ASL 2.0 and ISC and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/mreiferson/go-httpclient)
BuildRequires:  golang(github.com/op/go-logging)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/weppos/publicsuffix-go/publicsuffix)
BuildRequires:  golang(github.com/zmap/rc2)
%if %{without bootstrap}
BuildRequires:  golang(github.com/zmap/zcertificate)
%endif
BuildRequires:  golang(golang.org/x/crypto/chacha20poly1305)
BuildRequires:  golang(golang.org/x/net/context)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
# https://github.com/zmap/zcrypto/issues/211
%if %{with bootstrap}
%gocheck -d verifier -d x509 -d tls
%else
%gocheck -d x509 -d tls
%endif
%endif

%gopkgfiles

%changelog
* Fri Jun 19 18:51:25 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20200619git4d17126
- Bump to commit 4d171263147247189025e53b13fd2d5828d59755

* Tue Feb 04 23:23:46 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20200204git127181a
- Bump to commit 127181aff13da671788fc183661626ebe235389e

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 21:42:12 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190729git9051775
- Initial package