# Generated by go2rpm
%bcond_without check
%bcond_without bootstrap

# https://github.com/go-openapi/analysis
%global goipath         github.com/go-openapi/analysis
Version:                0.19.0

%gometa

%global common_description %{expand:
A foundational library to analyze an OAI specification document for easier
reasoning about the content.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Openapi specification object model analyzer

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-openapi/jsonpointer)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)

%if %{without bootstrap}
%if %{with check}
# Tests
BuildRequires:  golang(github.com/go-openapi/loads/fmts)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 00:41:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.0-1
- Initial package