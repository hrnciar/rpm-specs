# Generated by go2rpm
%bcond_without check

# https://github.com/go-playground/validator
%global goipath         gopkg.in/go-playground/validator.v8
%global forgeurl        https://github.com/go-playground/validator
Version:                8.18.2

%gometa

%global common_description %{expand:
Package Validator implements value validations for structs and individual fields
based on tags.

It can also handle Cross-Field and Cross-Struct validation for nested structs
and has the ability to dive into arrays and maps of any type.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Go struct and field validation

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/go-playground/assert.v1)
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 15:49:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 8.18.2-1
- Initial package
