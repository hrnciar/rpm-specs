# Generated by go2rpm 1
%bcond_without check

# https://github.com/alexflint/go-arg
%global goipath         github.com/alexflint/go-arg
Version:                1.3.0

%gometa

%global common_description %{expand:
Struct-based argument parsing in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Struct-based argument parsing

License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alexflint/go-scalar)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Apr 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Initial package

