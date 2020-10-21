# Generated by go2rpm
%bcond_with check

# https://github.com/hanwen/go-fuse
%global goipath         github.com/hanwen/go-fuse
Version:                2.0.3

%gometa

%global godevelheader %{expand:
Requires:        fuse-devel}

%global goaltipaths     github.com/hanwen/go-fuse/v2

%global common_description %{expand:
FUSE bindings for Go.}

%global golicenses LICENSE
%global godocs     README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        FUSE bindings for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  fuse-devel

%if %{with check}
# Tests
BuildRequires:  golang(github.com/kylelemons/godebug/pretty)
BuildRequires:  golang(golang.org/x/sync/errgroup)
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
* Mon Jul 27 13:51:47 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Thu May 21 2020 Brian (bex) Exelbierd <bex@pobox.com> - 1.0.1-0.20190319git161a164
- Upgrade to final 1.0 series commit - no official release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 22:18:49 CEST 2019 Brian (bex) Exelbierd <bex@pobox.com> - 1.0.0-1
- Initial package
