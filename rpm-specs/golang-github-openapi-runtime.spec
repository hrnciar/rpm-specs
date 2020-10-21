# Generated by go2rpm
%bcond_without check
%bcond_with bootstrap

# https://github.com/go-openapi/runtime
%global goipath         github.com/go-openapi/runtime
Version:                0.19.20

%gometa

%global goipaths0       github.com/go-openapi/runtime
%global goipathsex0     github.com/go-openapi/runtime/middleware

%if %{without bootstrap}
%global goipaths1       github.com/go-openapi/runtime/middleware
%endif

%global common_description %{expand:
The runtime component for use in codegeneration or as untyped usage.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Openapi runtime interfaces

# Upstream license specification: MIT and Apache-2.0
License:        MIT and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/go-openapi/analysis)
BuildRequires:  golang(github.com/go-openapi/errors)
BuildRequires:  golang(github.com/go-openapi/loads)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)
%if %{without bootstrap}
BuildRequires:  golang(github.com/go-openapi/validate)
%endif
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(gopkg.in/yaml.v2)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/go-openapi/loads/fmts)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
%if %{with bootstrap}
%gocheck -d middleware -d client -d internal/testing/simplepetstore
%else
%gocheck
%endif
%endif

%gopkgfiles

%changelog
* Thu Jul 30 17:00:36 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.20-1
- Update to 0.19.20

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 00:55:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.19.0-1
- Initial package
