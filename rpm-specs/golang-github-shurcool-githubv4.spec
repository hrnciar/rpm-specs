# Generated by go2rpm 1
%bcond_without check

# https://github.com/shurcooL/githubv4
%global goipath         github.com/shurcooL/githubv4
%global commit          f27d2ca7f6d535f7e35dd817493104814423eb48

%gometa

%global common_description %{expand:
Package githubv4 is a client library for accessing GitHub GraphQL API v4
(https://developer.github.com/v4/).}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Package githubv4 is a client library for accessing GitHub GraphQL API v4

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/shurcooL/graphql)
BuildRequires:  golang(golang.org/x/oauth2)

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
* Fri Sep 04 19:20:27 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20200904gitf27d2ca
- Initial package
