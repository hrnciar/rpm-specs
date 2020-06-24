# Generated by go2rpm 1
%bcond_without check

# https://github.com/viant/afs
%global goipath         github.com/viant/afs
Version:                0.16.1

%gometa

%global common_description %{expand:
Abstract File Storage.}

%global golicenses      LICENSE.txt NOTICE.txt
%global godocs          example CHANGELOG.md README.md TODO.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Abstract File Storage

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-errors/errors)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/viant/toolbox)
BuildRequires:  golang(github.com/viant/toolbox/storage)
BuildRequires:  golang(golang.org/x/crypto/ssh)

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
* Thu Feb 13 01:28:15 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.16.1-1
- Initial package