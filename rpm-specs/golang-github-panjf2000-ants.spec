# Generated by go2rpm 1
%bcond_without check

# https://github.com/panjf2000/ants
%global goipath         github.com/panjf2000/ants
Version:                2.4.0

%gometa

%global common_description %{expand:
ants implements a goroutine pool with fixed capacity, managing and recycling
a massive number of goroutines, allowing developers to limit the number of
goroutines in your concurrent programs.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md CODE_OF_CONDUCT.md README.md\\\
                        README_ZH.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Goroutine pool in Go

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
* Sun May 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.0-1
- Initial package
