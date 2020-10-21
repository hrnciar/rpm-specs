# Generated by go2rpm 1
%bcond_without check

# https://github.com/cockroachdb/redact
%global goipath         github.com/cockroachdb/redact
Version:                1.0.5

%gometa

%global common_description %{expand:
Utilities to redact Go strings for confidentiality.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Utilities to redact Go strings for confidentiality

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
* Wed Sep 09 00:20:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.5-1
- Initial package
