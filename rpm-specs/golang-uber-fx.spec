# Generated by go2rpm 1
# Tests do not work within Mock
%bcond_with check

# https://github.com/uber-go/fx
%global goipath         go.uber.org/fx
%global forgeurl        https://github.com/uber-go/fx
Version:                1.13.1

%gometa

%global common_description %{expand:
A dependency injection based application framework for Go.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md CHANGELOG.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A dependency injection based application framework for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(go.uber.org/dig)
BuildRequires:  golang(go.uber.org/multierr)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.uber.org/goleak)
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
* Tue Sep 08 18:22:10 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.13.1-1
- Initial package
