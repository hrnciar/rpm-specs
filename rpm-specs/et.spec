%global _firewalld_dir %{_prefix}/lib/firewalld

Name:           et
Version:        6.0.7
Release:        2%{?dist}
Summary:        Remote shell that survives IP roaming and disconnect

License:        ASL 2.0
URL:            https://mistertea.github.io/EternalTerminal/
Source0:        https://github.com/MisterTea/EternalTerminal/archive/et-v%{version}.tar.gz
Source1:        et.xml
Patch0:         et-6.0.5-full_protobuf.patch
BuildRequires:  boost-devel
BuildRequires:  cmake3
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  libsodium-devel
BuildRequires:  libutempter-devel
BuildRequires:  ncurses-devel
BuildRequires:  protobuf-compiler
%if 0%{?fedora}
BuildRequires:  protobuf-lite-devel
%else
BuildRequires:  protobuf-devel
%endif
BuildRequires:  systemd

%{?systemd_requires}

%description
Eternal Terminal (ET) is a remote shell that automatically reconnects without
interrupting the session.


%prep
%setup -q -n EternalTerminal-et-v%{version}
%if 0%{?fedora}
%else
%patch0 -p1
%endif


%build
%cmake3 .
%make_build


%install
%make_install
mkdir -p \
  %{buildroot}%{_unitdir} \
  %{buildroot}%{_sysconfdir} \
  %{buildroot}%{_firewalld_dir}/services
install -m 0644 -p systemctl/et.service %{buildroot}%{_unitdir}/et.service
install -m 0644 -p etc/et.cfg %{buildroot}%{_sysconfdir}/et.cfg
install -m 0644 %{SOURCE1} %{buildroot}%{_firewalld_dir}/services/et.xml


%check
ctest3 -V %{?_smp_mflags}


%post
%systemd_post et.service
%firewalld_reload

%preun
%systemd_preun et.service

%postun
%systemd_postun_with_restart et.service
%firewalld_reload


%files
%license LICENSE
%doc README.md
%{_bindir}/et
%{_bindir}/etserver
%{_bindir}/etterminal
%{_bindir}/htm
%{_bindir}/htmd
%dir %{_firewalld_dir}
%dir %{_firewalld_dir}/services
%{_firewalld_dir}/services/et.xml
%config(noreplace) %{_sysconfdir}/et.cfg
%{_unitdir}/et.service


%changelog
* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 6.0.7-2
- Rebuilt for protobuf 3.12

* Tue Mar  3 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.7-1
- Update to 6.0.7

* Tue Feb 18 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.6-1
- Update to 6.0.6

* Sat Feb  1 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.5-1
- Update to 6.0.5
- Build for EPEL 8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec  1 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.4-1
- Update to 6.0.4

* Sun Sep 22 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 6.0.3-1
- Update to 6.0.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.1.10-1
- Update to 5.1.10

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jason Gauci <jgmath2000@gmail.com> - 5.1.9-1
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.9

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.1.8-3
- Rebuild for protobuf 3.6

* Wed Oct 31 2018 Sérgio Basto <sergio@serjux.com> - 5.1.8-2
- Make it possible build it on EPEL 7

* Mon Oct 29 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.1.8-1
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.8

* Wed Oct 17 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.1.7-1%{?dist}
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.7
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.6

* Tue Oct  9 2018 Jason Gauci <jgmath2000@gmail.com> - 5.1.5-2%{?dist}
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.5
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.4
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.3
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.2
- https://github.com/MisterTea/EternalTerminal/releases/tag/et-v5.1.1

* Fri Aug 24 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.1.0-1%{?dist}
- Update to 5.1.0

* Tue Aug 14 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.0.7-2%{?dist}
- add BR on gcc-c++

* Thu Aug  9 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 5.0.7-1%{?dist}
- Initial package
