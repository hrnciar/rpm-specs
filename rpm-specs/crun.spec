Summary: OCI runtime written in C
Name: crun
Version: 0.13
Release: 2%{?dist}
Source0: https://github.com/containers/crun/releases/download/%{version}/%{name}-%{version}.tar.gz
License: GPLv3+
URL: https://github.com/containers/crun

# We always run autogen.sh
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: python
BuildRequires: git
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: python3-libmount
BuildRequires: libtool
BuildRequires: go-md2man
Provides: oci-runtime = 2

%description
crun is a runtime for running OCI containers

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%configure --disable-silent-rules

%make_build

%install
%make_install
rm -rf $RPM_BUILD_ROOT/usr/lib*

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Wed Apr 15 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.13-2
- release bump for correct upgrade path

* Thu Mar 05 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.13-1
- built version 0.13

* Mon Feb 17 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.2.1-1
- built version 0.12.2.1

* Mon Feb 17 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.2-1
- built version 0.12.2

* Thu Feb 6 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.1-1
- built version 0.12.1

* Mon Feb 3 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12-1
- built version 0.12

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.11-1
- built version 0.11

* Mon Nov 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.6-1
- built version 0.10.6

* Sun Nov 10 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.5-2
- built version 0.10.5
- fix CVE-2019-18837

* Sun Nov 10 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.5-1
- built version 0.10.5

* Thu Oct 31 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.4-1
- built version 0.10.4

* Tue Oct 29 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.3-1
- built version 0.10.3

* Mon Oct 7 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.2-1
- built version 0.10.2

* Fri Oct 4 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.1-1
- built version 0.10.1

* Tue Oct 1 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10-1
- built version 0.10

* Fri Sep 13 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.9.1-1
- built version 0.9.1

* Wed Sep 11 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.9-1
- built version 0.9

* Tue Sep 10 2019 Jindrich Novy <jnovy@redhat.com> - 0.8-3
- Add versioned oci-runtime provide.

* Mon Sep 9 2019 Dan Walsh <dwalsh@redhat.com> - 0.8-2
- Add provides oci-runtime

* Mon Aug 19 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.8-1
- built version 0.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.7-1
- built version 0.7

* Tue Jun 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.6-1
- built version 0.6
