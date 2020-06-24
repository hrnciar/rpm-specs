# Generated by go2rpm
%bcond_without check

# https://github.com/go-openapi/jsonreference
%global goipath         github.com/go-openapi/jsonreference
Version:                0.19.0

%gometa

%global common_description %{expand:
Fork of gojsonreference with support for structs.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Gojsonreference with support for structs

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-openapi/jsonpointer)
BuildRequires:  golang(github.com/PuerkitoBio/purell)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 21:56:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.0-1
- Initial package