# Generated by go2rpm 1
# https://gitea.com/xorm/core/issues/56
%bcond_with check

# https://gitea.com/xorm/core
%global goipath         xorm.io/core
%global forgeurl        https://gitea.com/xorm/core
Version:                0.7.0
%global repo            core
%global archivename     %{repo}-%{version}
%global archiveext      tar.gz
%global archiveurl      %{forgeurl}/archive/v%{version}.%{archiveext}
%global topdir          %{repo}
%global extractdir      %{repo}
%global scm             git

%gometa

%global goaltipaths     github.com/go-xorm/core

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-xorm-core-devel < 0.7.0-1
}

%global common_description %{expand:
Core is a lightweight wrapper of sql.DB.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Lightweight & Compatible wrapper of database/sql

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# switch from MySQL to sqlite3 for testing (no server needed)
Patch0:         sqlite3-test-default.patch

%if %{with check}
# Tests
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 17:33:57 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Release 0.7.0

* Wed Jul 03 17:29:51 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.3-2
- Refresh SPEC

* Mon Jun 24 2019 Nathan Scott <nathans@redhat.com> - 0.6.3-1
- Update to latest Golang packaging guidelines
- Update to latest upstream release

* Fri Mar 15 2019 Nathan Scott <nathans@redhat.com> - 0.6.2-1
- First package for Fedora