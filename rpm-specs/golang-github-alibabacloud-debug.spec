%bcond_without check

# https://github.com/alibabacloud-go/debug
%global goipath         github.com/alibabacloud-go/debug
%global commit          9472017b5c6804c66e5d873fabd2a2a937b31e0b

%gometa

%global common_description %{expand:
Alibaba Cloud (Aliyun) Debug function for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Alibaba Cloud (Aliyun) Debug function for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

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
* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.4
- Update summary and description for clarity and consistency

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.3.20200728git9472017
- Update to release 3 of git commit 9472017 (#1811173)
- Enable check stage
- Clean changelog

* Fri Mar 06 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.2.20200304git9472017
- Remove build of debug binary example as this is a devel only package

* Wed Mar 04 2020 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20200304git9472017
- Add common_description and Summary

* Fri Nov 22 2019 Brandon Perkins <bperkins@redhat.com> - 0-0.1.20191122git9472017
- Initial package

