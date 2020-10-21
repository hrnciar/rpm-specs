Name: prelockd
Version: 0.8
Release: 2%{?dist}
Summary: Lock binaries and libraries in memory to improve system responsiveness
BuildArch: noarch

License: MIT
URL: https://github.com/hakavlad/prelockd
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?rhel} >= 7
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

Requires: python3 >= 3.3

%description
prelockd is a daemon that locks memory mapped binaries and libraries in memory
to improve system responsiveness under low-memory conditions.


%prep
%autosetup -p1

# Drop non-RPM stuff from Makefile install stage
sed -i 's|base units useradd chcon daemon-reload|base units|' Makefile

sed -i 's|/env python3|/python3|' %{name}


%install
%make_install \
    DOCDIR=%{_pkgdocdir} \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir} \
    SYSTEMDUNITDIR=%{_unitdir}

%pre
# Create prelockd user
getent passwd %{name} >/dev/null || \
    useradd -r -s /sbin/nologin \
    -c "Lock binaries and libraries in memory to improve system responsiveness" %{name}
exit 0


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%{_pkgdocdir}/
%{_sbindir}/%{name}
%{_sharedstatedir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service


%changelog
* Mon Oct 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8-2
- build: make 'systemd-rpm-macros' conditional due epel7 support

* Sun Oct 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8-1
- build(update): 0.8

* Tue Oct  6 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7-2
- build: drop %{?systemd_requires} macros
- build: drop custom patch in favour of sed

* Tue Oct  6 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7-1
- build(update): 0.7

* Sun Oct  4 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6-1
- Initial package
