%global         srcname stomppy

Name:           stomppy
Version:        5.0.1
Release:        3%{?dist}
Summary:        Python stomp client for messaging

License:        ASL 2.0
URL:            https://github.com/kwoli/stomp.py
Source0:        https://files.pythonhosted.org/packages/source/s/stomp.py/stomp.py-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
stomp.py is a Python client library for accessing messaging servers 
(such as ActiveMQ or JBoss Messaging) using the STOMP protocol. It can also
be run as a standalone, command-line client for testing.

%package -n python3-stomppy
Summary:        Python stomp client for messaging for python3
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-stomppy
stomp.py is a Python client library for accessing messaging servers 
(such as ActiveMQ or JBoss Messaging) using the STOMP protocol. It can also
be run as a standalone, command-line client for testing.

This module is for the python3.

%prep
%autosetup -n stomp.py-%{version}

%build
%py3_build

%install
%py3_install

%check
#%%{__python3} setup.py test

%files -n python3-%{srcname}
%{python3_sitelib}/*
%{_bindir}/stomp
%doc CHANGELOG stomp.log.conf
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.1-3
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 9 2020 Steve Traylen <steve.traylen@cern.ch> - 5.0.1-1
- Update to 5.0.1

* Mon Jan 6 2020 Steve Traylen <steve.traylen@cern.ch> - 5.0.0-1
- Update to 5.0.0

* Tue Oct 1 2019 Steve Traylen <steve.traylen@cern.ch> - 4.1.22-1
- Update to 4.1.22

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.21-5
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.21-3
- Subpackage python2-stomppy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Steve Traylen <steve.traylen@cern.ch> - 4.1.21-1
- Update to 4.1.21

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.20-2
- Rebuilt for Python 3.7

* Wed May 16 2018 Steve stable URL for source
- Update to 4.1.20, Use better URL for Source.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 2 2017 Steve Traylen <steve.traylen@cern.ch> - 4.1.18-1
- Update to 4.1.19

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 7 2017 Steve Traylen <steve.traylen@cern.ch> - 4.1.17-4
- Typo in package summary

* Tue Apr 4 2017 Steve Traylen <steve.traylen@cern.ch> - 4.1.17-3
- Version provides

* Tue Apr 4 2017 Steve Traylen <steve.traylen@cern.ch> - 4.1.17-2
- Correct name of obsoleted package.

* Thu Mar 23 2017 Steve Traylen <steve.traylen@cern.ch> - 4.1.17-1
- User modern puppet 2 and 3 macros.
- Update to 4.1.17

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.1.11-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.11-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 24 2016 Steve Traylen <steve.traylen@cern.ch> - 4.1.11-1
- Update to 4.1.11

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 3 2015 Steve Traylen <steve.traylen@cern.ch> - 4.1.8-1
- Update to 4.1.8
- Delete incompatible and unused file backwardsock25.py on python3.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 4 2015 Steve Traylen <steve.traylen@cern.ch> - 4.0.16-1
- Update to 4.0.16

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 27 2014 Lubomir Rintel <lkundrak@v3.sk> - 3.1.6-2
- No python3 on el7

* Wed Oct 9 2013 Steve Traylen <steve.traylen@cern.ch.com> - 3.1.6-1
- Update to 3.1.6, upstream moved to github.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 3.0.5-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Steve Traylen <steve.traylen@cern.ch.com> - 3.0.5-1
- Update to 3.0.5

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 6 2011 Steve Traylen <steve.traylen@cern.ch.com> - 3.0.3-1
- Update to 3.0.3

* Tue Aug 24 2010 Steve Traylen <steve.traylen@cern.ch.com> - 3.0.2-0.1.a
- Update to source to 3.0.2a, a pre-release of 3.0.2.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 3.0.1-0.2.beta2.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri May 14 2010 Steve Traylen <steve.traylen@cern.ch> -  3.0.1-0.2.beta2
- Build with correct file this time.

* Thu May 13 2010 Steve Traylen <steve.traylen@cern.ch> -  3.0.1-0.1.beta2
- Update to 3.0.2beta2
- Add new CHANGELOG and README files.
- Add python3 support.
- Remove python-rm-bang-python.patch, no longer a file to patch even.

* Wed Sep 30 2009 Steve Traylen <steve.traylen@cern.ch> -  2.0.4-1
- Update to 2.0.4
  remove patch to allow building with out network.

* Wed Sep 30 2009 Steve Traylen <steve.traylen@cern.ch> -  2.0.2-3
- Remove some dos line feeds

* Tue Sep 29 2009 Steve Traylen <steve.traylen@cern.ch> -  2.0.2-2
- Add patch to allow build without working network.

* Mon Sep 7 2009 Steve Traylen <steve.traylen@cern.ch> -  2.0.2-1
- Initial version.

