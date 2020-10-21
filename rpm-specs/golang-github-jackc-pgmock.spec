# Generated by go2rpm 1
%bcond_without check

# https://github.com/jackc/pgmock
%global goipath         github.com/jackc/pgmock
%global commit          13a1b77aafa2641ad31b655a18e8c3605ef55e2d

%gometa

%global common_description %{expand:
Pgmockproxy is a PostgreSQL proxy that logs the messages back and forth between
the PostgreSQL client and server. This can aid in building a mocking script by
running commands against a real server to observe the results. It can also be
used to debug applications that speak the PostgreSQL wire protocol without
needing to use a tool like Wireshark.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Mock a PostgreSQL server

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jackc/pgproto3/v2)

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
* Wed Sep 09 12:07:20 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200909git13a1b77
- Initial package
