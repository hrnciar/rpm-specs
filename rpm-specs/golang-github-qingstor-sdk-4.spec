# Generated by go2rpm 1
%bcond_without check

# https://github.com/qingstor/qingstor-sdk-go
%global goipath         github.com/qingstor/qingstor-sdk-go/v4
Version:                4.1.0

%gometa

%global goaltipaths     github.com/yunify/qingstor-sdk-go

%global common_description %{expand:
The official QingStor SDK for the Go programming language.}

%global golicenses      LICENSE specs/qingstor/LICENSE
%global godocs          docs AUTHORS CHANGELOG.md README.md README_zh-CN.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        The official QingStor SDK for the Go programming language

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pengsrc/go-shared/convert)
BuildRequires:  golang(github.com/qingstor/log)
BuildRequires:  golang(github.com/qingstor/log/level)
BuildRequires:  golang(gopkg.in/yaml.v2)

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
* Fri Sep 18 02:55:13 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.1.0-1
- Initial package
