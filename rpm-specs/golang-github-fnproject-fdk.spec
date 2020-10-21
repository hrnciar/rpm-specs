# Generated by go2rpm 1
%bcond_without check

# https://github.com/fnproject/fdk-go
%global goipath         github.com/fnproject/fdk-go
Version:                0.0.2

%gometa

%global common_description %{expand:
Go language helper funcs for fn.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go language helper funcs for fn

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Thu Jul 30 19:47:05 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.2-1
- Initial package