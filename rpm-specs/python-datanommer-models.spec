%global modname datanommer.models

Name:           python-datanommer-models
Version:        0.9.1
Release:        12%{?dist}
Summary:        SQLAlchemy models for datanommer

License:        GPLv3+
URL:            https://pypi.io/project/%{modname}
Source0:        https://pypi.io/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
SQLAlchemy models for datanommer.

%description %_description

%package -n datanommer-config
Summary: Config files for datanommer

%description -n datanommer-config
Config files for datanommer.

%package -n python3-datanommer-models
Summary: %summary

%{?python_provide:%python_provide python3-datanommer-models}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Just for the tests
BuildRequires:  python3-nose
BuildRequires:  python3-fedmsg-meta-fedora-infrastructure
BuildRequires:  python3-fedmsg-core
BuildRequires:  python3-alembic
BuildRequires:  python3-sqlalchemy >= 0.7

Requires:       datanommer-config
Requires:       python3-fedmsg-core
Requires:       python3-alembic
Requires:       python3-sqlalchemy >= 0.7

%description -n python3-datanommer-models %_description

%prep
%setup -q -n %{modname}-%{version}

# Disable the consumer by default.
# https://github.com/fedora-infra/datanommer/issues/55
sed -i 's/True/False/g' fedmsg.d/example-datanommer.py

# Also (temporarily), use a less insecure db uri by default
# https://github.com/fedora-infra/datanommer/issues/55
sed -i 's/\/\/tmp\/datanommer.db//' fedmsg.d/example-datanommer.py

# Remove upstream egg-info so that it gets rebuilt.
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

# For some reason, this namespace file doesn't get copied in rawhide.
%{__cp} datanommer/__init__.py* %{buildroot}%{python3_sitelib}/datanommer/.

# fedmsg owns this directory, but we're going to add a file.
%{__mkdir_p} %{buildroot}%{_sysconfdir}/fedmsg.d/
%{__cp} fedmsg.d/example-datanommer.py %{buildroot}%{_sysconfdir}/fedmsg.d/datanommer.py

# DB upgrade/downgrade scripts
%{__mkdir_p} %{buildroot}%{_datadir}/%{modname}/
%{__cp} alembic.ini %{buildroot}%{_datadir}/%{modname}/alembic.ini
%{__cp} -r alembic/ %{buildroot}%{_datadir}/%{modname}/alembic/

%check
%{__python3} setup.py test

%files -n datanommer-config
%doc README.rst LICENSE
%{_datadir}/%{modname}/
%config(noreplace) %{_sysconfdir}/fedmsg.d/datanommer.py*

%files -n python3-datanommer-models
%doc README.rst LICENSE
%{python3_sitelib}/datanommer/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-7
- Subpackage python2-datanommer-models has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4
- Rebuilt for Python 3.7

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.9.1-3
- Copy namespace file explicitly for python3.

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.9.1-2
- Python3 subpackage.

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.9.1-1
- new version

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.0-2
- Python 2 binary package renamed to python2-datanommer-models
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Tue Dec 12 2017 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- new version

* Wed Oct 04 2017 Ralph Bean <rbean@redhat.com> - 0.8.2-1
- new version

* Fri Aug 11 2017 Ralph Bean <rbean@redhat.com> - 0.8.1-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Ralph Bean <rbean@redhat.com> - 0.8.0-1
- new version

* Fri Mar 03 2017 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Ralph Bean <rbean@redhat.com> - 0.6.5-2
- Fix rhel conditional again..

* Mon Mar 16 2015 Ralph Bean <rbean@redhat.com> - 0.6.5-1
- new version

* Wed Jul 09 2014 Ralph Bean <rbean@redhat.com> - 0.6.4-2
- Fix rhel conditional for epel7.

* Tue Jun 10 2014 Ralph Bean <rbean@redhat.com> - 0.6.4-1
- Latest upstream with a bugfix to the optimized inserts stuff.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Ralph Bean <rbean@redhat.com> - 0.6.3-1
- Optimized inserts.

* Fri Feb 21 2014 Ralph Bean <rbean@redhat.com> - 0.6.1-2
- Added a new test dependency on python-fedmsg-meta-fedora-infrastructure

* Fri Feb 21 2014 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Expanded Message.grep API.

* Wed Sep 11 2013 Ian Weller <iweller@redhat.com> - 0.6.0-2
- Modernize old git messages
- Handle UUIDs/msg_ids from fedmsg

* Mon Aug 26 2013 Ralph Bean <rbean@redhat.com> - 0.5.0-2
- Disable the consumer by default.
- Use an in-memory database by default.

* Mon Aug 12 2013 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- Added source_name and source_version columns.
- Added possibility to disable paging in calls to .grep().

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.6-1
- Latest upstream.
- Added optional "defer" argument to the `grep` method.

* Thu May 16 2013 Ralph Bean <rbean@redhat.com> - 0.4.5-1
- Fix links to upstream source.
- Allow queries to 'grep' with no timespan.

* Tue May 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.4-1
- Added an 'order' argument to the 'grep' method.

* Mon Apr 22 2013 Ralph Bean <rbean@redhat.com> - 0.4.3-1
- Bugfixes to category assignment.
- New convenience classmethods on Message, User, and Package.
- Removed old BuildRequires on bunch, argparse, and orderedict.

* Thu Feb 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.2-1
- Latest upstream with improved alembic migration.

* Thu Feb 07 2013 Ralph Bean <rbean@redhat.com> - 0.4.1-1
- Latest upstream contributed by Jessica Anderson.
- Included alembic upgrade scripts in /usr/share/datanommer.models/

* Thu Nov 08 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-6
- Patch setup.py to pull in the correct sqlalchemy for el6.
- Add BR for python-argparse and python-ordereddict.

* Thu Nov 08 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-5
- Added temporary BR on python-bunch to get around an old moksha issue.

* Mon Oct 22 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-4
- Remove explicit versioned Conflicts with old datanommer.

* Fri Oct 12 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-3
- Remove unneccessary CFLAGS definition.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Remove upstream egg-info so that its gets rebuilt.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- Initial split out from the main datanommer package.
