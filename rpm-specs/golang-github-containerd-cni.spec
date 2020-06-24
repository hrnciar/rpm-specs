# Generated by go2rpm
%bcond_without check

# https://github.com/containerd/go-cni
%global goipath         github.com/containerd/go-cni
%global commit          49fbd9b210f3c8ee3b7fd3cd797aabaf364627c1

%gometa

%global common_description %{expand:
A generic CNI library to provide APIs for CNI plugin interactions. The library
provides APIs to:

 - Load CNI network config from different sources
 - Setup networks for container namespace
 - Remove networks from container namespace
 - Query status of CNI network plugin initialization}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles      "${vendor[@]}"

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Generic CNI library to provide APIs for CNI plugin interactions

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

# BuildRequires:  golang(github.com/containernetworking/cni/libcni)
# BuildRequires:  golang(github.com/containernetworking/cni/pkg/types)
# BuildRequires:  golang(github.com/containernetworking/cni/pkg/types/current)
BuildRequires:  golang(github.com/pkg/errors)

%if %{with check}
# Tests
# BuildRequires:  golang(github.com/containernetworking/cni/pkg/types/020)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
%endif

%description
%{common_description}

%gopkg

%prep
# Have to use vendor github.com/containernetworking/cni because newer is not
# compatible
%goprep -k

%install
mapfile -t vendor <<< $(find vendor -type f)
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Apr 01 2020 Olivier Lemasle <o.lemasle@gmail.com> - 0-0.4
- Update to commit 49fbd9b210f3c8ee3b7fd3cd797aabaf364627c1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 23:20:37 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190627git891c2a4
- Initial package