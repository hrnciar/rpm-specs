# Generated by go2rpm 1
%bcond_without check

# https://github.com/go-logr/zapr
%global goipath         github.com/go-logr/zapr
Version:                0.2.0

%gometa

%global common_description %{expand:
A logr implementation using Zap.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A logr implementation using Zap

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-logr/logr)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/zapcore)

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
* Mon Aug 17 14:02:07 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-1
- Initial package
