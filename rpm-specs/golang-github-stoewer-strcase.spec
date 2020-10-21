# Generated by go2rpm 1
%bcond_without check

# https://github.com/stoewer/go-strcase
%global goipath         github.com/stoewer/go-strcase
Version:                1.2.0

%gometa

%global common_description %{expand:
Convert snake case, camel case and kebap case strings.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Convert snake case, camel case and kebap case strings

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
* Mon Jul 27 14:51:16 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Initial package
