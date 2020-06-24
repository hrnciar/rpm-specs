%global sum Graphical user interface to version control systems

Name:           rabbitvcs
Version:        0.17.1
Release:        16%{?dist}
Summary:        %{sum}

License:        GPLv2+
URL:            http://rabbitvcs.org
Source0:        https://github.com/rabbitvcs/rabbitvcs/archive/v%{version}/rabbitvcs-%{version}.tar.gz

Patch0:         rabbitvcs-ignore-post-install.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  /usr/bin/pathfix.py

%description
RabbitVCS is a set of graphical tools written to provide simple
and straightforward access to the version control systems you use.

%package        core
Summary:        Common package of RabbitVCS
Requires:       meld
Requires:       git
Requires:       mercurial
Requires:       subversion
# rhbz#1226816 - Gedit plugin not working with Gedit later than version 3.12
Obsoletes:      rabbitvcs-gedit < %{version}-%{release}

%description    core
Contains files shared between the RabbitVCS extensions.

%package -n python3-rabbitvcs
Summary:        %{sum}
%{?python_provide:%python_provide python3-rabbitvcs}
Requires:       %{name}-core = %{version}-%{release}
Requires:       python3-configobj
Requires:       python3-dulwich
Requires:       python3-gobject
Requires:       python3-pysvn
Requires:       python3-simplejson
Requires:       python3-tkinter

%description -n python3-rabbitvcs
RabbitVCS is a set of graphical tools written to provide simple
and straightforward access to the version control systems you use.

%package        cli
Summary:        CLI extension for RabbitVCS
BuildArch:      noarch
Requires:       %{name}-core = %{version}-%{release}

%description    cli
A command line command to use RabbitVCS

%package        caja
Summary:        Caja extension for RabbitVCS
# caja needs python3 for plugins
Requires:       python3-rabbitvcs = %{version}-%{release}
Requires:       python3-dbus
Requires:       python3-caja
Requires:       caja

%description    caja
An extension for Caja to allow better integration with the 
source control system.

%package        nautilus
Summary:        Nautilus extension for RabbitVCS
# nautilus needs python3 for plugins
Requires:       python3-rabbitvcs = %{version}-%{release}
Requires:       python3-dbus
Requires:       nautilus-python
Requires:       nautilus

%description    nautilus
An extension for Nautilus to allow better integration with the 
source control system.

%package        nemo
Summary:        Nemo extension for RabbitVCS
# nemo needs python3 for plugins
Requires:       python3-rabbitvcs = %{version}-%{release}
Requires:       python3-dbus
Requires:       python3-nemo
Requires:       nemo

%description    nemo
An extension for Nemo to allow better integration with the 
source control system.

%package        thunar
Summary:        Thunar extension for RabbitVCS
# thunar needs python3 for plugins
Requires:       python3-rabbitvcs = %{version}-%{release}
Requires:       python3-dbus
Requires:       thunarx-python
Requires:       thunar

%description    thunar
An extension for Thunar to allow better integration with the 
source control system.

%prep
%autosetup -p1
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%py3_build

%install
%py3_install
install -p -m0755 clients/cli/rabbitvcs -D %{buildroot}%{_bindir}/rabbitvcs
install -p -m0644 clients/caja/RabbitVCS.py -D %{buildroot}%{_datadir}/caja-python/extensions/RabbitVCS.py
install -p -m0644 clients/nautilus-3.0/RabbitVCS.py -D %{buildroot}%{_datadir}/nautilus-python/extensions/RabbitVCS.py
install -p -m0644 clients/nemo/RabbitVCS.py -D %{buildroot}%{_datadir}/nemo-python/extensions/RabbitVCS.py
install -p -m0644 clients/thunar/RabbitVCS.py -D %{buildroot}%{_datadir}/thunarx-python/extensions/RabbitVCS.py

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/rabbitvcs

%find_lang RabbitVCS

%files -f RabbitVCS.lang core
%license COPYING
%{_pkgdocdir}/
%{_datadir}/rabbitvcs/
%{_datadir}/icons/hicolor/16x16/actions/rabbitvcs-push.png
%{_datadir}/icons/hicolor/scalable/*/*.svg

%files -n python3-rabbitvcs
%{python3_sitelib}/*

%files cli
%{_bindir}/rabbitvcs

%files caja
%{_datadir}/caja-python/extensions/*.py*

%files nautilus
%{_datadir}/nautilus-python/extensions/*.py*

%files nemo
%{_datadir}/nemo-python/extensions/*.py*

%files thunar
%{_datadir}/thunarx-python/extensions/*.py*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Pete Walter <pwalter@fedoraproject.org> - 0.17.1-13
- Switch thunar support to Python 3 in F32 (#1738160)
- Drop python2-rabbitvcs in F32 (#1738183)
- Update nautilus-python requires

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Pete Walter <pwalter@fedoraproject.org> - 0.17.1-9
- Switch nautilus support to Python 3 in F30
- Switch nemo support to Python 3 in F29 (#1638349)
- Switch caja support to Python 3 in F29 (#1563523)
- Remove gtk-update-icon-cache scriptlets

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.17.1-8
- Fix shebang handling.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.17.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.17.1-3
- Change Requires for nemo to python2-nemo

* Mon Aug 21 2017 Pete Walter <pwalter@fedoraproject.org> - 0.17.1-2
- Adjust for various python2 package renames

* Tue Aug 15 2017 Pete Walter <pwalter@fedoraproject.org> - 0.17.1-1
- Update to 0.17.1

* Mon Aug 14 2017 Pete Walter <pwalter@fedoraproject.org> - 0.17-1
- Update to 0.17

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-0.8.20160108gite8214e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-0.7.20160108gite8214e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.16.1-0.6.20160108gite8214e6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-0.5.20160108gite8214e6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 15 2016 Raphael Groner <projects.rg@smart.ms> - 0.16.1-0.4.20160108gite8214e6
- add Tkinter as dependency for python-six, rhbz#1304642

* Wed Feb 03 2016 Raphael Groner <projects.rg@smart.ms> - 0.16.1-0.3.20160108gite8214e6
- fix build conditional for epel7

* Wed Feb 03 2016 Raphael Groner <projects.rg@smart.ms> - 0.16.1-0.2.20160108gite8214e6
- add patch to fix import urlparse in python3
- workaround for a bug in modernize tool with boolean
- disable b0rken gedit plugin, rhbz#1226816

* Sat Jan 30 2016 Raphael Groner <projects.rg@smart.ms> - 0.16.1-0.1.20160108gite8214e6
- new upstream snapshot as pre-release
- port to python3
- mark all as noarch and adjust plugins pathes
- enable debuginfo
- add git and mercurial as dependencies
- fix some crashes with log command, rhbz#1141530
- fix vcs status features, rhbz#1083043
- enable caja plugin, rhbz#1096162
- make gedit plugin work, rhbz#1226816
- add nemo plugin

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 03 2014 Christopher Meng <rpm@cicku.me> - 0.16-1
- Update to 0.16

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 11 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.15.0.5-1
- Updated to 0.15.0.5, BZ 760682.
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- tar.gz → tar.bz2
- Adjusted the paths for Gnome 3
- Re-added Group, Jon Ciesla limburgher@gmail.com

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 21 2011 Juan Rodriguez <nushio@fedoraproject.org> - 0.14.2.1-3
- Adds a dependency to python-dulwich so the git plugin can work
- Removes rabbitvcs-git and rabbitvcs-svn

* Tue Sep 13 2011 Juan Rodriguez <nushio@fedoraproject.org> - 0.14.2.1-2
- Removes Nautilus dependency on rabbitvcs-core

* Tue Sep 13 2011 Juan Rodriguez <nushio@fedoraproject.org> - 0.14.2.1-1
- Updated package to 0.14.2.1
- Added Thunar Plugin

* Mon Feb 14 2011 Juan Rodriguez <nushio@fedoraproject.org> - 0.14.1.1-1
- Updated Package to 0.14.1.1
- Lots of speed improvements. 
- Git and SVN support separated and are now optional
- Changelog for 0.14.1.1: http://blog.rabbitvcs.org/archives/284
- Changelog for 0.14.1: http://blog.rabbitvcs.org/archives/280
- Changelog for 0.14: http://blog.rabbitvcs.org/archives/277

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.13.3-2
- Rebuild for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jun 16 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13.3-1
- Fixes a *lot* of bugs
- No longer forces English as the language
- Gedit plugin should work now

* Sun Jun 6 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13.2.1-2
- Fixes the package creation

* Sun Jun 6 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13.2.1-1
- Fixes a crash left by a debug flag.

* Mon May 31 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13.2-1
- Updated to version 0.13.2.

* Thu May 27 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13.1-3
- Now obsoletes rabbitvcs
- Fixes svg permission ownage

* Wed May 26 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13.1-2
- rabbitvcs-core is now noarch
- rabbitvcs-cli is now noarch

* Wed Apr 28 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13.1-1
- Rebased to 13.1

* Fri Mar 19 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13-2
- The split packages are now bundled into a single tarball. 
- Changed some requires versions. 
- Thunar and NautilusOld packages are no longer being provided. 
- Updated Python macros to the newly approved ones
- Changed URL, Summary and Descriptions for all packages / subpackages
- Package is no longer noarch

* Thu Feb 11 2010 Juan Rodriguez <nushio@fedoraproject.org> - 0.13-1
- Updated RabbitVCS to 0.13
- Split packages for nautilus, nautilus-old, thunar, gedit and cli
- Requires nautilus-python >= 0.5.2 so 64bit users can use rabbitvcs. 

* Thu Dec 17 2009 Juan Rodriguez <nushio@fedoraproject.org> - 0.12.1-2
- Cleaned up Icon Script
- Added AUTHORS, COPYING and MAINTAINERS

* Tue Dec 1 2009 Juan Rodriguez <nushio@fedoraproject.org> - 0.12.1-1
- Updated to RabbitVCS 0.12.1
- Added SSL Client Cert prompt 
- Updated "previous log message" UI behaviour
- Updated locale detection
- Improvements for packaging scripts

* Sat Oct 3 2009 Juan Rodriguez <nushio@fedoraproject.org> - 0.12-1
- Renamed from NautilusSVN to RabbitVCS to match upstream. 
- Calls gtk-update-icon-cache to regenerate the icon cache
