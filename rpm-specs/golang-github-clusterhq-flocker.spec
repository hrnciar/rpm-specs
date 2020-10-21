# Generated by go2rpm
# int overflow, upstream is literally a dead company
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/clusterhq/flocker-go
%global goipath         github.com/clusterhq/flocker-go
%global commit          2b8b7259d3139c96c4a6871031355808ab3fd3b3

%gometa

%global common_description %{expand:
The package Flocker will let you easily interact with a Flocker Control
Service.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Flocker Go library

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 21:39:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190629git2b8b725
- Initial package
