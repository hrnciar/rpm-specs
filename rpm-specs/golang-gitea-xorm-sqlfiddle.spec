# Generated by go2rpm 1
# Needs network
%bcond_with check

# https://gitea.com/xorm/sqlfiddle
%global goipath         gitea.com/xorm/sqlfiddle
%global commit          62ce714f951af41ba61ec543afe292425b74910d
%global repo            sqlfiddle
%global archivename     %{repo}-%{commit}
%global archiveext      tar.gz
%global archiveurl      %{forgeurl}/archive/%{commit}.%{archiveext}
%global topdir          %{repo}
%global extractdir      %{repo}
%global scm             git

%gometa

%global common_description %{expand:
This Go library is aimed to provide an API to operate http://sqlfiddle.com/.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Sqlfiddle unofficial API for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Fri Sep 18 02:29:56 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200918git62ce714
- Initial package
