# Generated by go2rpm
%bcond_without check

# https://github.com/docker/go-events
%global goipath         github.com/docker/go-events
%global commit          9461782956ad83b30282bf90e31fa6a70c255ba9

%gometa

%global common_description %{expand:
The Docker Events package implements a composable event distribution package for
Go.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Composable event distribution for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/sirupsen/logrus)

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

* Sat May 04 16:57:55 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627git9461782
- Initial package