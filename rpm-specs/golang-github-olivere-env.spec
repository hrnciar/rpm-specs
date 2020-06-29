# Generated by go2rpm 1
%bcond_without check

# https://github.com/olivere/env
%global goipath         github.com/olivere/env
Version:                1.1.0

%gometa

%global common_description %{expand:
Simplify reading environment variables.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Reading environment variables

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
* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
