# Generated by go2rpm 1
# Cyclic with github.com/jackc/pgx/v4, disabling tests for bootstrapping
%bcond_with check

# https://github.com/jackc/pgtype
%global goipath         github.com/jackc/pgtype
Version:                1.4.2

%gometa

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(github.com/jackc/pgx/v4\\)$

%global goipathsex      github.com/jackc/pgtype/testutil

%global common_description %{expand:
pgtype implements Go types for over 70 PostgreSQL types. pgtype is the type
system underlying the https://github.com/jackc/pgx PostgreSQL driver. These
types support the binary format for enhanced performance with pgx. They also
support the database/sql Scan and Value interfaces and can be used with
https://github.com/lib/pq.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md pgxtype/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go types for over 70 PostgreSQL types

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gofrs/uuid)
BuildRequires:  golang(github.com/jackc/pgconn)
BuildRequires:  golang(github.com/jackc/pgio)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/shopspring/decimal)
BuildRequires:  golang(golang.org/x/xerrors)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/jackc/pgx/v4)
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
* Sat Jul 25 13:51:09 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.2-1
- Initial package