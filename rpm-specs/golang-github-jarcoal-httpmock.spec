# Generated by go2rpm 1
%bcond_without check

# https://github.com/jarcoal/httpmock
%global goipath         github.com/jarcoal/httpmock
Version:                1.0.6

%gometa

%global common_description %{expand:
HTTP mocking for Golang.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        HTTP mocking for Golang

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
* Wed Sep 09 15:08:22 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.6-1
- Initial package
