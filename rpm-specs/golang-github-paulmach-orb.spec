# Generated by go2rpm 1
%ifarch x86_64
%bcond_without check
%endif

# https://github.com/paulmach/orb
%global goipath         github.com/paulmach/orb
Version:                0.1.6

%gometa

%global common_description %{expand:
Types and utilities for working with 2d geometry in Golang.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Types and utilities for working with 2d geometry in Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/pkg/errors)

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
* Mon Aug 17 10:07:01 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.6-1
- Initial package
