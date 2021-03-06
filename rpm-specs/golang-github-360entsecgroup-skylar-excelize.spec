# Generated by go2rpm 1
%ifarch x86_64
%bcond_without check
%endif

# https://github.com/360EntSecGroup-Skylar/excelize
%global goipath         github.com/360EntSecGroup-Skylar/excelize
Version:                2.3.0

%gometa

%global common_description %{expand:
Golang library for reading and writing Microsoft Excel (XLSX) files.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        PULL_REQUEST_TEMPLATE.md README.md README_zh.md\\\
                        SECURITY.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang library for reading and writing Microsoft Excel (XLSX) files

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# Go 1.15: Compatible with Go 1.15
Patch0:         https://github.com/360EntSecGroup-Skylar/excelize/commit/c3e92a51d744bc8420e0626b06ee3a0efd030341.patch#/0001-Compatible-with-Go-1.15.patch

BuildRequires:  golang(github.com/mohae/deepcopy)
BuildRequires:  golang(github.com/xuri/efp)
BuildRequires:  golang(golang.org/x/net/html/charset)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(golang.org/x/image/tiff)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Aug 17 09:59:19 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.3.0-1
- Initial package
