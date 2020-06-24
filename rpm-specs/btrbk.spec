%define __python %{__python3}

Name:           btrbk
Version:        0.28.3
Release:        2%{?dist}
Summary:        Tool for creating snapshots and remote backups of btrfs sub-volumes
License:        GPLv3+
URL:            https://digint.ch/btrbk/
Source0:        https://digint.ch/download/%{name}/releases/%{name}-%{version}.tar.xz
#Source0:        https://github.com/digint/%%{name}/archive/v%%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  systemd perl-generators
BuildRequires:  rubygem-asciidoctor asciidoc xmlto

Requires:       btrfs-progs >= 4.12
Requires:       mbuffer

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       openssh-clients pv
%else
Recommends:     openssh-clients pv
%endif


%description
Backup tool for btrfs sub-volumes, using a configuration file, allows
creation of backups from multiple sources to multiple destinations,
with ssh and flexible retention policy support (hourly, daily,
weekly, monthly)


%prep
%autosetup
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +


%install
make DESTDIR=%{buildroot} \
    install-bin \
    install-systemd \
    install-share \
    install-man \
    install-doc \
    install-etc

mkdir __doc
mv %{buildroot}/%{_docdir}/btrbk/* __doc/
rm -rf %{buildroot}/%{_docdir}/btrbk

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/btrbk

%files
%doc __doc/*
%config(noreplace) %{_sysconfdir}/btrbk
%license COPYING
%{_sbindir}/btrbk
%{_unitdir}/btrbk.*
%{_datadir}/btrbk
%{_mandir}/man1/btrbk.1*
%{_mandir}/man1/ssh_filter_btrbk.1*
%{_mandir}/man5/btrbk.conf.5*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Michael Goodwin <xenithorb@fedoraproject.org> - 0.28.3-1
- Update to 0.28.3 (#1692924)
- Update build deps to include `rubygem-asciidoctor`
- Update rumtime deps to include `mbuffer` replacing `pv`

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.27.0-1
- Update to 0.27.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.26.1-3
- rebuilt

* Mon Mar 26 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.26.1-2
- Force correct python3 path:
  https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3#Transition_Steps

* Tue Mar 06 2018 Michael Goodwin <xenithorb@fedoraproject.org> - 0.26.1-1
- Update to 0.26.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.26.0-1
- Update to 0.26.0 (#1501520)
  - Assorted bugfixes
- MIGRATION NEEDED: For raw targets see ChangeLog in docs, or:
   - https://github.com/digint/btrbk/blob/v0.26.0/ChangeLog
- Resume deprecated from "-r" to "replace"

* Mon Jul 31 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.25.1-1
- Update to 0.25.1 (#1476626)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Michael Goodwin <xenithorb@fedoraproject.org> - 0.25.0-4
- Removed perl from Requires, auto-generated
- Removed %%{?systemd_requires}, for scriptlets only

* Wed Jul  5 2017 Mike Goodwin <xenithorb@fedoraproject.org> - 0.25.0-3
- License was GPLv3+ not GPLv3
- Add perl-generators for BuildRequires
- Add -p to all install commands in Makefile and in spec (with sed)
  - Patch submitted upstream: https://github.com/digint/btrbk/pull/164
- Fix if statement for RHEL detection
- Spelling of subvolumes -> sub-volumes to satisfy rpmlint
- Removed %%{?perl_default_filter} macro, unnecessary

* Wed Jul  5 2017 Mike Goodwin <xenithorb@fedoraproject.org> - 0.25.0-2
- Added a more verbose description per the developer
- Changed Source0 to the official source tarball
- Include pv as a weak dependency, as well as openssh-clients
- Add if statement because <= RHEL7 doesn't have Recommends:

* Tue Jul  4 2017 Mike Goodwin <xenithorb@fedoraproject.org> - 0.25.0-1
- Initial packaging
