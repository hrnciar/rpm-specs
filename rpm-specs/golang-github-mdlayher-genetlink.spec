# Generated by go2rpm
# Needs netlink
%bcond_with check

# https://github.com/mdlayher/genetlink
%global goipath         github.com/mdlayher/genetlink
%global commit          4cdc5dab577ca87055f659bb0065ee223105eb1e

%gometa

%global common_description %{expand:
Package genetlink implements generic netlink interactions and data types.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Generic netlink interactions and data types

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         0001-skip-arch-dependent-test-on-s390x.patch

BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/mdlayher/netlink)
BuildRequires:  golang(github.com/mdlayher/netlink/nlenc)
BuildRequires:  golang(github.com/mdlayher/netlink/nltest)
BuildRequires:  golang(golang.org/x/net/bpf)
BuildRequires:  golang(golang.org/x/sys/unix)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 14:28:04 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20190523git4cdc5da
- Bump to commit 4cdc5dab577ca87055f659bb0065ee223105eb1e

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git76fecce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.3.git76fecce
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git76fecce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Paul Gier <pgier@redhat.com> - 0-0.1.20180515git76fecc
- First package for Fedora
