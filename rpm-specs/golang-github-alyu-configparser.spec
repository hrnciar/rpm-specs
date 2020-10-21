%bcond_without check

# https://github.com/alyu/configparser
%global goipath         github.com/alyu/configparser
%global commit          744e9a66e7bcb83ea09084b979ddd1efc1f2f418

%gometa

%global common_description %{expand:
Alibaba Cloud (Aliyun) INI configuration file parser for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Alibaba Cloud (Aliyun) INI configuration file parser for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  perl-Digest-SHA
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
* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.3
- Update summary and description for clarity and consistency

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.2.20200728git744e9a6
- Update to release 2 of git commit 744e9a6 (#1811179)
- Enable check stage
- Clean changelog

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191122git744e9a6
- Initial package

