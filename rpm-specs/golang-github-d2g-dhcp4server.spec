# Generated by go2rpm
%bcond_without check

# https://github.com/d2g/dhcp4server
%global goipath         github.com/d2g/dhcp4server
%global commit          7d4a0a7f59a572d629ba5f49634b35c7fac7967e

%gometa

%global common_description %{expand:
DHCP Server for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        DHCP Server for Go

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/d2g/dhcp4)
BuildRequires:  golang(golang.org/x/net/ipv4)

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 01:01:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627git7d4a0a7
- Initial package
