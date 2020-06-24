%global modname datanommer.commands

Name:           datanommer-commands
Version:        0.7.2
Release:        9%{?dist}
Summary:        Console commands for datanommer

License:        GPLv3+
URL:            https://pypi.io/project/%{modname}
Source0:        https://pypi.io/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-freezegun

BuildRequires:  python3-datanommer-models >= 0.4.1
BuildRequires:  python3-fedmsg-meta-fedora-infrastructure
BuildRequires:  python3-fedmsg-core
BuildRequires:  python3-sqlalchemy >= 0.7

Requires:       python3-datanommer-models >= 0.4.1
Requires:       python3-fedmsg-meta-fedora-infrastructure
Requires:       python3-fedmsg-core
Requires:       python3-sqlalchemy >= 0.7

%description
Console commands for datanommer.

%prep
%setup -q -n %{modname}-%{version}

# Remove upstream egg-info so that it gets rebuilt.
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%doc README.rst LICENSE
%{python3_sitelib}/datanommer/commands/
%{python3_sitelib}/%{modname}-%{version}*

%{_bindir}/datanommer-create-db
%{_bindir}/datanommer-latest
%{_bindir}/datanommer-stats
%{_bindir}/datanommer-dump

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-9
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-2
- Rebuilt for Python 3.7

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.7.2-1
- Convert to python3.

* Wed Apr 04 2018 Ralph Bean <rbean@redhat.com> - 0.7.1-1
- new version

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Ralph Bean <rbean@redhat.com> - 0.4.6-4
- Fix rhel conditionals again.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 16 2014 Ralph Bean <rbean@redhat.com> - 0.4.6-2
- Fix rhel conditionals.

* Mon Jun 09 2014 Ralph Bean <rbean@redhat.com> - 0.4.6-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Ralph Bean <rbean@redhat.com> - 0.4.5-1
- Fixes to unit tests for new fedmsg.
- Update links to upstream source.

* Mon Apr 22 2013 Ralph Bean <rbean@redhat.com> - 0.4.3-1
- More random bugfixes.

* Thu Feb 14 2013 Ralph Bean <rbean@redhat.com> - 0.4.2-1
- Latest upstream with a bugfix to datanommer-latest.

* Thu Feb 07 2013 Ralph Bean <rbean@redhat.com> - 0.4.1-1
- Latest upstream from Jessica Anderson.
- Various enhancements and bugfixes.
- New datanommer-latest command.
- Tests now require python-mock.
- New dep on fedmsg.meta Fedora Infrastructure plugin.

* Mon Oct 22 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-4
- Remove explicit versioned Conflicts with old datanommer.

* Fri Oct 12 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-3
- Remove unnecessary CFLAGS definition.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-2
- Remove upstream egg-info so that its gets rebuilt.

* Thu Oct 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.0-1
- Initial split out from the main datanommer package.
