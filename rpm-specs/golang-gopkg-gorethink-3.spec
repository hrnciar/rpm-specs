# Generated by go2rpm
%bcond_without check

# https://github.com/rethinkdb/rethinkdb-go
%global goipath         gopkg.in/gorethink/gorethink.v3
%global forgeurl        https://github.com/rethinkdb/rethinkdb-go
Version:                3.0.5

%gometa

%global common_description %{expand:
Package Rethinkdb-go implements a Go driver for RethinkDB.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Go language driver for RethinkDB

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/hailocab/go-hostpool)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/suite)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(gopkg.in/fatih/pool.v2)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
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
# .: exit with no error message?
# encoding: https://github.com/rethinkdb/rethinkdb-go/issues/465
# internal/reql_tests: needs network
%gocheck -d . -d encoding -d internal/reql_tests
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 20:21:39 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.5-1
- Initial package
