# Generated by go2rpm
%bcond_without check

# https://github.com/casbin/casbin
%global goipath         github.com/casbin/casbin
Version:                1.8.1

%gometa

%global common_description %{expand:
Casbin is a powerful and efficient open-source access control library for Golang
projects. It provides support for enforcing authorization based on various
access control models.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Authorization library that supports access control models in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/Knetic/govaluate)

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 16:20:30 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.1-1
- Initial package