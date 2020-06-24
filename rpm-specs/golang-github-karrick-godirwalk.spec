# Generated by go2rpm
%bcond_without check

# https://github.com/karrick/godirwalk
%global goipath         github.com/karrick/godirwalk
Version:                1.10.3

%gometa

%global common_description %{expand:
Godirwalk is a library for traversing a directory tree on a file system..}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Fast directory traversal for Golang

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 18:38:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.10.3-1
- Initial package
