%global majorversion 0.7
%global libversion 0.700.8

Name:		xfdashboard
Version:	0.7.8
Release:	1%{?dist}
Summary:	GNOME shell like dashboard for Xfce

License:	GPLv2+
URL:		http://goodies.xfce.org/projects/applications/%{name}/start
Source0:	http://archive.xfce.org/src/apps/xfdashboard/%{majorversion}/%{name}-%{version}.tar.bz2

BuildRequires:	libwnck3-devel
BuildRequires:	clutter-devel
BuildRequires:	xfconf-devel
BuildRequires:	garcon-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	libtool
BuildRequires:	xfce4-dev-tools
BuildRequires:	libICE-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libXcomposite-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXinerama-devel

%description
Xfdashboard provides a GNOME shell dashboard like interface for use with Xfce
desktop. It can be configured to run to any keyboard shortcut and when executed
provides an overview of applications currently open enabling the user to switch
between different applications. The search feature works like Xfce's app finder
which makes it convenient to search for and start applications.

%package themes
Summary:	Themes for xfdashboard
Requires:	%{name}

%description themes
Additional themes for use with xfdashboard

%package devel
Summary:	Devel files for xfdashboard
Requires:	%{name} = %{version}-%{release}

%description devel
Development related files for xfdashboard

%prep
%setup -q

%build
export CFLAGS="%{optflags}"

%configure
%make_build

%install
%make_install

%find_lang %{name}

# remove .la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-settings.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}-settings
%{_datadir}/%{name}/bindings.xml
%{_datadir}/%{name}/preferences.ui
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_datadir}/themes/%{name}/*
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{libversion}
%{_libdir}/%{name}/plugins/clock-view.so
%{_libdir}/%{name}/plugins/gnome-shell-search-provider.so
%{_libdir}/%{name}/plugins/example-search-provider.so
%{_libdir}/%{name}/plugins/hot-corner.so
%{_libdir}/%{name}/plugins/middle-click-window-close.so

%files themes
%{_datadir}/themes/%{name}-*

%files devel
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/lib%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
* Tue Sep 22 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.8-1
- Update to 0.7.8

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.7-1
- Update to 0.7.7

* Fri Nov 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.6-1
- Update to 0.7.6

* Tue Aug 13 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.5-4
- Rebuild for xfce 4.14

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 09 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.5-1
- Update to 0.7.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.4-3
- Modernize spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.7.3-1
- update to 0.7.3. Fixes bug #1469327

* Mon May 15 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Tue Mar 07 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 07 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sat May 21 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Sat Apr 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.92-3
- Fix license file installation

* Thu Mar 31 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.92-2
- Update to correct libxfdashboard version
- Add macro for library versioning

* Thu Mar 31 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.92-1
- Bug fix update
- Minor UI change (configure button for plugins)

* Thu Mar 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.91-3
- Enabled live windows and multi-monitor support
- added BR: libxcomposite, libxinerama, libxdamage

* Tue Mar 22 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.91-2
- Update library version and fix typos

* Tue Mar 22 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.91-1
- Update to v0.5.91
- Drop upstreamed patch

* Sun Mar 06 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.90-3
- Fix bungled requires for devel subpackage

* Sat Mar 05 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.90-2
- Add upstream patch to enable hot fix initialization

* Sat Mar 05 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.90-1
- Update to latest upstream version
- Added devel subpackage
- Added xfdashboard libraries

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5
- Fixes bug #1303479

* Sat Dec 19 2015 Kevin Fenzi <kevin@scrye.com> - 0.5.4-1
- Update to 0.5.4. Fixes bug #1293031

* Sat Nov 14 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.3-1
- Update to latest upstream version (0.5.3)

* Thu Oct 08 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Tue Sep 08 2015 Kevin Fenzi <kevin@scrye.com> 0.5.1-1
- Update to 0.5.1. Fixes bug #1260818

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Kevin Fenzi <kevin@scrye.com> 0.5.0-1
- Update to 0.5.0

* Sat May 30 2015 Kevin Fenzi <kevin@scrye.com> 0.4.2-1
- Update to 0.4.2

* Sat May 30 2015 Kevin Fenzi <kevin@scrye.com> 0.4.1-1
- Update to 0.4.1 Fixes bug #1226500

* Sun Apr 12 2015 Kevin Fenzi <kevin@scrye.com> 0.4.0-1
- Update to 0.4.0 Fixes bug #1211005

* Sat Mar 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.91-1
- Update to 0.3.91
- Removed upstreamed patches
- Updated to source and URL to point to xfce project links

* Thu Mar 26 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.90-2
- Fix for crash due to missing icons

* Wed Mar 18 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.90-1
- Update to 0.3.90
- Removed patch for forcing X11 backend in clutter

* Mon Mar 09 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.9-4
- Force X11 backend for clutter

* Sun Mar 01 2015 Mukundan Ragavan <nonamedotc@gmail.com> - 0.3.9-3
- Rebuild from Xfce 4.12

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.3.9-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Feb 21 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.9-1
- Updated to 0.3.9
- Translatations added

* Sat Jan 24 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.8-1
- Update to 0.3.8

* Sat Jan 17 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7
- Bugfix update to 0.3.6

* Sat Jan 17 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6
- Added libxfce4util-devel as BR for building settings manager

* Mon Jan 12 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Thu Nov 27 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4
- Move additional themes provided to -themes subpackage

* Mon Oct 20 2014 Kevin Fenzi <kevin@scrye.com> 0.3.3-1
- Update to 0.3.3

* Mon Sep 08 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.2-1
- Updated to latest upstream version
- New features included

* Wed Sep 03 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.1-1
- Updated to latest upstream version

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.0-1
- Latest upstream version with bugfixes and enhancements
- Removed ChangeLog from doc

* Sun Jul 20 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.1-1
- Updated to latest upstream version

* Sat Jul 12 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.0-2
- Initial build for F22

* Wed Jun 11 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.0-1
- Updated to latest upstream release
- Added appdata file

* Wed Jun 04 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.92-1
- Updated to latest version
- Added application icons

* Tue May 20 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.91-1
- Fixed URL
- Updated to 0.1.91 - API change with this update
- Removed TODO
- Added BuildRequires for desktop-file-utils
- desktop file added - will show in XFCE menu
- desktop file for autostart added

* Fri May 02 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.90-1
- Update to 0.1.90
- multiple bug fixes and improvements

* Sun Mar 23 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.6-2
- Updated to 0.1.6
- Added xfdashboard.xml to files section

* Sun Mar 23 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.6-1
- Updated to 0.1.6

* Sat Mar 8 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.5-1
- Updated to latest release containing new enhancements

* Tue Feb 25 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.4-2
- Patch for enabling workspace switching added
- Upstream bug - issue#1 on github

* Mon Feb 24 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.4-1
- Updated to the latest upstream version
- Includes theming support (provides a default theme)

* Tue Feb 11 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.3-1
- Updated to the latest upstream version

* Mon Feb 10 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.2-3
- Corrected flags used for building the package
- Edited the description

* Sun Feb 02 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.2-2
- Corrected version used for packaging
- Added the doc files

* Wed Jan 29 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.3-1
- Initial build for Fedora
