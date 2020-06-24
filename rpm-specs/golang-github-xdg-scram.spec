# Generated by go2rpm
%bcond_without check

# https://github.com/xdg/scram
%global goipath         github.com/xdg/scram
%global commit          7eeb5667e42c09cb51bf7b7c28aea8c56767da90

%gometa

%global common_description %{expand:
Package Scram provides client and server implementations of the Salted Challenge
Response Authentication Mechanism (SCRAM) described in RFC-5802 and RFC-7677.

It includes both client and server side support.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go implementation of rfc-5802 salted challenge response authentication mechanism

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/xdg/stringprep)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 21:09:06 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190623git7eeb566
- Initial package