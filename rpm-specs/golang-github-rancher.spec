# Generated by go2rpm
%bcond_without check

# https://github.com/rancher/go-rancher
%global goipath         github.com/rancher/go-rancher
Version:                0.1.0
%global commit          222ed122ed79d4facfa1bfbb24772530e0f9f900

%gometa

%global common_description %{expand:
Go language bindings for Rancher API.}

%global golicenses      LICENSE
%global godocs          docs README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Go language bindings for Rancher API

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gorilla/context)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/Sirupsen/logrus)
BuildRequires:  golang(gopkg.in/yaml.v2)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 22:26:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1.20190702git222ed12
- Initial package
