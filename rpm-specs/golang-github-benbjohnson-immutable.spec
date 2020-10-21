# Generated by go2rpm 1
%bcond_without check

# https://github.com/benbjohnson/immutable
%global goipath         github.com/benbjohnson/immutable
Version:                0.2.0

%gometa

%global common_description %{expand:
This repository contains immutable collection types for Go. It includes List,
Map, and SortedMap implementations. Immutable collections can provide efficient,
lock free sharing of data by requiring that edits to the collections return new
collections.

The collection types in this library are meant to mimic Go built-in collections
such asslice and map. The primary usage difference between Go collections and
immutable collections is that immutable collections always return a new
collection on mutation so you will need to save the new reference.

Immutable collections are not for every situation, however, as they can incur
additional CPU and memory overhead. Please evaluate the cost/benefit for your
particular project.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Immutable collections for Go

License:        MIT
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jan 26 23:32:46 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
