# Generated by go2rpm 1
%bcond_without check

# https://github.com/zclconf/go-cty
%global goipath         github.com/zclconf/go-cty
Version:                1.6.1

%gometa

%global common_description %{expand:
A type system for dynamic values in Go applications.}

%global golicenses      LICENSE
%global godocs          docs README.md CHANGELOG.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A type system for dynamic values in Go applications

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/apparentlymart/go-textseg/v12/textseg)
BuildRequires:  golang(github.com/vmihailenco/msgpack/v4)
BuildRequires:  golang(github.com/vmihailenco/msgpack/v4/codes)
BuildRequires:  golang(golang.org/x/text/unicode/norm)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
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
* Tue Sep 08 18:05:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.1-1
- Initial package
