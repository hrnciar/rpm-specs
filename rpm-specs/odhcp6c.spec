%global commit f575351cbb3defc0bf52680c9082912a6c264374
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20200416
%global _hardened_build 1

Name: odhcp6c
Version: 0
Release: 0.5.%{date}git%{shortcommit}%{?dist}
Summary: Embedded DHCPv6 and RA client
# License is GPLv2 except:
# ./src/md5.c: ISC
# ./src/md5.h: ISC
License: GPLv2 and ISC
URL: https://git.openwrt.org/?p=project/odhcp6c.git
# Source fetched from git:
# git clone https://git.openwrt.org/project/odhcp6c.git
# cd odhcp6c
# git archive --format=tar.gz --prefix=odhcp6c-f575351cbb3defc0bf52680c9082912a6c264374/ f575351cbb3defc0bf52680c9082912a6c264374 >../odhcp6c-f575351cbb3defc0bf52680c9082912a6c264374.tar.gz
Source0: %{name}-%{commit}.tar.gz
Source1: odhcp6c@.service
BuildRequires: cmake
BuildRequires: gcc
%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
odhcp6c is a minimal DHCPv6 and Router Advertisement client for use in embedded
Linux systems, especially routers. It compiles to only about 35 KB.

%prep
%autosetup -n %{name}-%{commit}

%build
%{cmake} .
%{make_build}

%install
install -D -p -m 0755 odhcp6c %{buildroot}%{_sbindir}/odhcp6c
install -D -p -m 0755 odhcp6c-example-script.sh %{buildroot}%{_sysconfdir}/odhcp6c/odhcp6c-example-script.sh
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/odhcp6c@.service

%files
%doc README odhcp6c-example-script.sh
%license COPYING
%{_sbindir}/odhcp6c
%dir %{_sysconfdir}/odhcp6c
%{_sysconfdir}/odhcp6c/odhcp6c-example-script.sh
%{_unitdir}/odhcp6c@.service

%changelog
* Wed Jun 24 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.5.20200416gitf575351
- Install preserving time stamps
- Own /etc/odhcp6c dir

* Tue Apr 21 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.4.20200416gitf575351
- Install in multi-user.target
- Update description

* Sat Apr 18 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.3.20200416gitf575351
- Harden service

* Sat Apr 18 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.2.20200416gitf575351
- Order service unit after network-pre.target
- Fix build in epel

* Thu Apr 16 2020 Juan Orti Alcaine <jortialc@redhat.com> - 0-0.1.20200416gitf575351
- Initial release
