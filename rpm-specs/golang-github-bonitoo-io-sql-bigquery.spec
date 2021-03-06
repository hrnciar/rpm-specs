# Generated by go2rpm 1
# Needs credentials for Google Cloud
%bcond_with check

# https://github.com/bonitoo-io/go-sql-bigquery
%global goipath         github.com/bonitoo-io/go-sql-bigquery
Version:                0.3.4

%gometa

%global common_description %{expand:
Go database/sql driver for Google BigQuery.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go database/sql driver for Google BigQuery

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/bigquery)
BuildRequires:  golang(google.golang.org/api/iterator)
BuildRequires:  golang(google.golang.org/api/option)

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
* Tue Sep 08 19:03:01 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.4-1
- Initial package
