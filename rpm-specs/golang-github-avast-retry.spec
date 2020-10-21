# Generated by go2rpm 1
%bcond_without check

# https://github.com/avast/retry-go
%global goipath         github.com/avast/retry-go
Version:                2.6.1

%gometa

%global common_description %{expand:
Simple golang library for retry mechanism.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple golang library for retry mechanism

License:        MIT
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
* Sat Sep 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.1-1
- Initial package for Fedora