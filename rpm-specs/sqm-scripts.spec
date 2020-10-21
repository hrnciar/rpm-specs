Name: sqm-scripts
Version: 1.4.0
Release: 2%{?dist}
Summary: Traffic shaper scripts of the CeroWrt project
# License GPLv2 except these files:
# sqm-scripts-1.4.0/luci/sqm-cbi.lua: Apache License 2.0
# sqm-scripts-1.4.0/luci/sqm-controller.lua: Apache License 2.0
License: GPLv2 and ASL 2.0
URL: https://www.bufferbloat.net/projects/cerowrt/wiki/Smart_Queue_Management/
Source0: https://github.com/tohojo/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
"Smart Queue Management", or "SQM" is shorthand for an integrated network
system that performs better per-packet/per flow network scheduling, active
queue length management (AQM), traffic shaping/rate limiting, and QoS
(prioritization).

%prep
%autosetup

%build
%{make_build}

%install
%{make_install}

%files
%doc README.md
%dir %{_sysconfdir}/sqm
%{_sysconfdir}/sqm/default.conf
%config(noreplace) %{_sysconfdir}/sqm/sqm.conf
%{_bindir}/sqm
%{_prefix}/lib/sqm
%{_unitdir}/sqm@.service
%{_tmpfilesdir}/sqm.conf

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 23 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.0-1
- Initial release
