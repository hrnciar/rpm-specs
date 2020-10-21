%bcond_without check

# https://github.com/alibabacloud-go/tea
%global goipath         github.com/alibabacloud-go/tea
Version:                1.1.11

%gometa

%global common_description %{expand:
Alibaba Cloud (Aliyun) support for TEA OpenAPI DSL.}

%global golicenses      LICENSE
%global godocs          README-CN.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Alibaba Cloud (Aliyun) support for TEA OpenAPI DSL

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/alibabacloud-go/debug/debug)
BuildRequires:  golang(golang.org/x/net/proxy)

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
* Mon Oct 19 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.11-1
- Update to version 1.1.11 (#1889458)

* Tue Sep 08 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.10-1
- Update to version 1.1.10 (#1876623)

* Sun Aug 23 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.8-1
- Update to version 1.1.8 (#1871444)

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.7-2
- Update summary and description for clarity and consistency

* Tue Jul 28 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.7-1
- Update to version 1.1.7 (#1811174)
- Enable check stage
- Clean changelog

* Thu Mar 05 2020 Brandon Perkins <bperkins@redhat.com> - 0.0.7-1
- Initial package

