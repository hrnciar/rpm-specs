# Generated by go2rpm
%bcond_without check

# https://github.com/fsouza/go-dockerclient
%global goipath         github.com/fsouza/go-dockerclient
Version:                1.6.5

%gometa

%global common_description %{expand:
This package presents a client for the Docker remote API. It also provides
support for the extensions in the Swarm API.

This package also provides support for docker's network API, which is a simple
passthrough to the libnetwork remote API.}

%global golicenses      DOCKER-LICENSE LICENSE
%global godocs          AUTHORS README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Go client for the Docker remote API

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/docker/docker/api/types/registry)
BuildRequires:  golang(github.com/docker/docker/api/types/swarm)
BuildRequires:  golang(github.com/docker/docker/pkg/archive)
BuildRequires:  golang(github.com/docker/docker/pkg/fileutils)
BuildRequires:  golang(github.com/docker/docker/pkg/homedir)
BuildRequires:  golang(github.com/docker/docker/pkg/jsonmessage)
BuildRequires:  golang(github.com/docker/docker/pkg/stdcopy)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/gorilla/mux)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 17:56:27 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.6.5-1
- Update to 1.6.5

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-2
- Add Obsoletes for old name

* Thu May 23 01:02:53 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.0-1
- Release 1.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-24.git2350d7b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-23.git2350d7b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-22.git2350d7b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-21.git2350d7b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-20.git2350d7b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.2.1-19.git2350d7b
- No docker on ppc64 so far
  related: #1215656

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-18.git2350d7b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-17.git2350d7b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-16.git2350d7b
- https://fedoraproject.org/wiki/Changes/golang1.6

* Tue Feb 09 2016 jchaloup <jchaloup@redhat.com> - 0.2.1-15.git2350d7b
- Add missing [B]R not reported by 'gofed lint'
  related: #1215656

* Mon Feb 08 2016 jchaloup <jchaloup@redhat.com> - 0.2.1-14.git2350d7b
- don't import bundled deps
  related: #1215656

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13.git2350d7b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 jchaloup <jchaloup@redhat.com> - 0.2.1-12.git2350d7b
- vendor directory was renamed to external
  related: #1215656

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0.2.1-11.git2350d7b
- Bump to upstream 2350d7bc12bb04f2d7d6824c7718012b1397b760
  related: #1215656

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0.2.1-10.gitf95d189
- Update to spec-2.1
  related: #1215656

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0.2.1-9.gitf95d189
- Update spec file to spec-2.0
  related: #1215656

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8.gitf95d189
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 jchaloup <jchaloup@redhat.com> - 0.2.1-7.gitf95d189
- Add missing Provides
  related: #1215656

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 0.2.1-6.gitf95d189
- Bump to upstream f95d189acbfcb8628482decdb662d30bc74913e8
  related: #1215656

* Mon Apr 27 2015 jchaloup <jchaloup@redhat.com> - 0.2.1-5.git0dfe1f1
- Bump to upstream 0dfe1f16045e9e460430ee10ec1dea8d86c9bd9f
  resolves: #1215656

* Wed Jan 28 2015 jchaloup <jchaloup@redhat.com> - 0.2.1-4.git0758f40
- Bump to upstream 0758f407f25a8df60c540b0ec758905192687e14
  related: #1085840

* Wed Dec 24 2014 jchaloup <jchaloup@redhat.com> - 0.2.1-3.git15d2c6e
- Bump to b52383442df766febf51f9f858ee311f69a2f264
  related: #1085840

* Thu Oct 16 2014 lsm5@riseup.net - 0.2.1-2.git15d2c6e
- update to latest upstream commit

* Mon Sep 29 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.1-1.git0236a64
- update to upstream commit 0236a64c6c4bd563ec277ba00e370cc753e1677c
- don't own dirs owned by golang, don't redefine gopath
- preserve timestamps of copied files

* Tue Jul 22 2014 Colin Walters <walters@redhat.com>
- Update to newer version for Kubernetes work

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitd639515
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Initial package
