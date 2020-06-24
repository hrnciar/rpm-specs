# Generated by go2rpm 1
%bcond_without check

# https://github.com/yashtewari/glob-intersection
%global goipath         github.com/yashtewari/glob-intersection
%global commit          5c77d914dd0ba7bedca923f97232d37137e038f3

%gometa

%global common_description %{expand:
Go package to check if the set of strings matched by the intersection of two
regexp-style globs is non-empty.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Go package to check if the intersection of two regexp-style globs is non-empty

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pkg/errors)

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
* Sun Apr 05 16:09:30 CEST 2020 Olivier Lemasle <o.lemasle@gmail.com> - 0-0.1.20200405git5c77d91
- Initial package
