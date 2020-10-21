Name: memavaild
Version: 0.5
Release: 2%{?dist}
Summary: Improve responsiveness during heavy swapping
BuildArch: noarch

License: MIT
URL: https://github.com/hakavlad/memavaild
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: systemd-rpm-macros

Requires: python3 >= 3.3

%description
Improve responsiveness during heavy swapping: keep amount of available memory.


%prep
%autosetup -p1

# Drop non-RPM stuff from Makefile install stage
sed -i 's|base units useradd chcon daemon-reload|base units|' Makefile

sed -i 's|/env python3|/python3|' memavaild


%install
%make_install \
    DOCDIR=%{_pkgdocdir} \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir} \
    SYSTEMDUNITDIR=%{_unitdir}


%pre
# Create memavaild user
getent passwd %{name} >/dev/null || \
    useradd -r -s /sbin/nologin \
    -c "Improve responsiveness during heavy swapping" %{name}
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
%{_datadir}/%{name}/
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service


%changelog
* Tue Oct  6 17:27:54 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5-2
- build: drop %{?systemd_requires} macros
- build: drop custom patch in favour of sed

* Wed Sep 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5-1
- Update to 0.5

* Tue Sep 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.1-2
- Initial package
