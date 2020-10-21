# Generated by go2rpm 1
%bcond_without check

# https://github.com/alecthomas/kong-hcl/v2
%global goipath         github.com/alecthomas/kong-hcl/v2
Version:                2.0.0

%gometa

%global common_description %{expand:
This is version 2.x of this package which uses the HCL2 library. For most config
files it should be a drop-in replacement, but for any codebases using
konghcl.DecodeValue() you will need to update your Go structs to include HCL
tags.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A Kong configuration loader for HCL

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alecthomas/kong)
BuildRequires:  golang(github.com/alecthomas/repr)
BuildRequires:  golang(github.com/hashicorp/hcl)
BuildRequires:  golang(github.com/hashicorp/hcl/v2)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/gohcl)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hclparse)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hclsyntax)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/zclconf/go-cty/cty)

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
* Tue Aug 11 17:44:12 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- Initial package