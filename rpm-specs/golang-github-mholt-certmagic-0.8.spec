# Generated by go2rpm 1
%bcond_without check

# https://github.com/mholt/certmagic
%global goipath         github.com/mholt/certmagic-0.8
%global forgeurl        https://github.com/mholt/certmagic
Version:                0.8.3

%gometa

%global goname          golang-github-mholt-certmagic-0.8
%global godevelname     golang-github-mholt-certmagic-devel-0.8

%global common_description %{expand:
Automatic HTTPS for any Go program: fully-managed TLS certificate issuance and
renewal.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Automatic HTTPS for any Go program: fully-managed TLS certificate issuance and renewal

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-acme/lego/v3/acme)
BuildRequires:  golang(github.com/go-acme/lego/v3/certcrypto)
BuildRequires:  golang(github.com/go-acme/lego/v3/certificate)
BuildRequires:  golang(github.com/go-acme/lego/v3/challenge)
BuildRequires:  golang(github.com/go-acme/lego/v3/challenge/dns01)
BuildRequires:  golang(github.com/go-acme/lego/v3/challenge/http01)
BuildRequires:  golang(github.com/go-acme/lego/v3/challenge/tlsalpn01)
BuildRequires:  golang(github.com/go-acme/lego/v3/lego)
BuildRequires:  golang(github.com/go-acme/lego/v3/registration)
BuildRequires:  golang(github.com/klauspost/cpuid)
BuildRequires:  golang(golang.org/x/crypto/ocsp)

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|github.com/mholt/certmagic|github.com/mholt/certmagic-0.8|' $(find . -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Aug 18 19:53:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.3-1
- Initial package