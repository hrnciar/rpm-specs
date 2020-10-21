# Generated by go2rpm 1
%bcond_without check

# https://github.com/matrix-org/gomatrix
%global goipath         github.com/matrix-org/gomatrix
%global commit          e5578b12c7522e551e7ffcf4e4cc008b1b4f3250

%gometa

%global common_description %{expand:
A Golang Matrix client.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Golang Matrix client

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
* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200717gite5578b1
- Initial package
