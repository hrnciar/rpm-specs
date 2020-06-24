%{?python_enable_dependency_generator}
Name:		barman
Version:	2.10
Release:	3%{?dist}
Summary:	Backup and Recovery Manager for PostgreSQL

License:	GPLv3
Url:		http://www.pgbarman.org/
Source0:	https://files.pythonhosted.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz
Source1:	barman.cron
Source2:	barman.logrotate

BuildArch:      noarch
BuildRequires:	%{py3_dist setuptools}
BuildRequires:  python3-devel
Requires(pre):  shadow-utils
Requires:       /usr/bin/register-python-argcomplete
Requires:	rsync >= 3.0.4
Requires:       %{py3_dist barman} = %{version}

%description
Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%package -n barman-cli
Summary:	Client Utilities for Barman, Backup and Recovery Manager for PostgreSQL
Requires:	%{py3_dist barman} = %{version}
%description -n barman-cli
Client utilities for the integration of Barman in
PostgreSQL clusters.

Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%package -n python3-barman
Summary:	The shared libraries required for Barman family components
Requires:	%{py3_dist setuptools}, %{py3_dist psycopg2} >= 2.4.2, %{py3_dist argh} >= 0.21.2, %{py3_dist argcomplete}, python3-dateutil
%description -n python3-barman
Python libraries used by Barman.

Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.


%{?python_provide:%python_provide python3-%{srcname}}
%prep
%setup -q

# Change shebang in all relevant executable files in this directory and all subdirectories
find -type f -executable -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}/var/lib/barman
mkdir -p %{buildroot}/var/log/barman
mkdir -p %{buildroot}%{_sysconfdir}/barman/conf.d
install -pm 644 doc/barman.conf %{buildroot}%{_sysconfdir}/barman/barman.conf
install -pm 644 doc/barman.d/* %{buildroot}%{_sysconfdir}/barman/conf.d
install -pm 644 %SOURCE1 %{buildroot}%{_sysconfdir}/cron.d/barman
install -pm 644 %SOURCE2 %{buildroot}%{_sysconfdir}/logrotate.d/barman
install -Dpm 644 scripts/barman.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/barman
touch %{buildroot}/var/log/barman/barman.log

sed -i 's|/etc/barman.d|/etc/barman/conf.d|g' %{buildroot}%{_sysconfdir}/barman/barman.conf

%files
%license LICENSE
%doc NEWS README.rst
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man5/%{name}.5.gz
%config(noreplace) %{_sysconfdir}/barman/%{name}.conf
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/barman/conf.d/
%{_datadir}/bash-completion/completions/barman
%attr(700,barman,barman) %dir /var/lib/%{name}
%attr(755,barman,barman) %dir /var/log/%{name}
%attr(600,barman,barman) %ghost /var/log/%{name}/%{name}.log


%files -n barman-cli
%defattr(-,root,root)
%doc NEWS README.rst
%{_bindir}/barman-wal-archive
%{_bindir}/barman-wal-restore
%{_bindir}/barman-cloud-wal-archive
%{_bindir}/barman-cloud-backup
%doc %{_mandir}/man1/barman-wal-archive.1.gz
%doc %{_mandir}/man1/barman-wal-restore.1.gz
%doc %{_mandir}/man1/barman-cloud-wal-archive.1.gz
%doc %{_mandir}/man1/barman-cloud-backup.1.gz

%files -n python3-barman
%defattr(-,root,root)
%doc NEWS README.rst
%{python3_sitelib}/%{name}-%{version}%{?extra_version:%{extra_version}}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}/

%pre
getent group barman >/dev/null || groupadd -r barman
getent passwd barman >/dev/null || \
    useradd -r -g barman -d /var/lib/barman -s /bin/bash \
    -c "Backup and Recovery Manager for PostgreSQL" barman
exit 0

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.10-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.10-1
- RHBZ#1778773 Updated to 2.10 version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9-2
- Rebuilt for Python 3.8

* Tue Aug 18 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.9-1
- RHBZ#1742344 Updated to 2.9 version

* Tue Jul 30 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-6
- RHBZ#1734137 fix python_provide macro in the right block of spec file

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-4
- RHBZ#1721158 fix typo that breaks config file

* Wed Jun 19 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-3
- RHBZ#1721158 updated spec in order to split package as recommended by upstream

* Thu May 16 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-2
- Minor fixes over previous commit

* Thu May 16 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.8-1
- Update to 2.8 version (fixes RHBZ#1707150)

* Wed Mar 20 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.7-1
- Update to 2.7 version

* Mon Feb 18 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5-3
- Enable python dependency generator

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Francisco Javier Tsao Santín <tsao@gpul.org> - 2.5-1
- Update to 2.5 version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Devrim Gündüz <devrim@gunduz.org> - 2.1-1
- Update to 2.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-2
- Rebuild for Python 3.6

* Tue Oct 11 2016 Dominika Krejci <dkrejci@redhat.com> - 2.0
- Update to 2.0
- Switch to Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.3-8
- Update requires on python-argcomplete
- Move completion script to /usr

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 - Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.3-6
- Revert dependency on python-dateutil15 (#1183341)

* Mon Feb 02 2015 - Dale Macartney <dbmacartney@fedoraproject.org> - 1.3.3-5
- Replacing python-dateutil with python-dateutil15

* Wed Jan 21 2015 - Dale Macartney <dbmacartney@fedoraproject.org> - 1.3.3-4
- Resolve RPM dependencies with older version of python-dateutil

* Wed Jan 14 2015 - Dale Macartney <dbmacartney@fedoraproject.org> - 1.3.3-3
- Update barman to 1.3.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 1.3.1-1
- Update barman to 1.3.1

* Tue Feb 4 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 1.3.0-1
- Update barman to 1.3.0

* Wed Jan 15 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 1.2.3-9
- Corrected rpmlint warning permissions

* Tue Jan 14 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 1.2.3-7
- Change license from GPLv3 to GPLv3+

* Mon Jan 13 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 1.2.3-6
- Clean up of rpmlint errors

* Mon Jan 13 2014 - Dale Macartney <dbmacartney@fedoraproject.org> 1.2.3-5
- Remove non-required variables for older fedora/rhel releases.

* Wed Oct 16 2013 - Dale Macartney <dbmacartney@gmail.com> 1.2.3-4
- Clean up of package dependencies and removal of unnecessary variables

* Thu Oct 10 2013 - Dale Macartney <dbmacartney@gmail.com> 1.2.3-1
- Initial packaging for Fedora Project
