Name:       gsmartcontrol
Version:    1.1.3
Release:    6%{?dist}
Summary:    Graphical user interface for smartctl

# Note that the "Whatever" license is effectively the MIT license.  See email
# from Tom Callaway to Fedora-legal-list on 18-APR-2011.
License:    (GPLv2 or GPLv3) and BSD and zlib and Boost and MIT

URL:        http://gsmartcontrol.sourceforge.net
Source0:    https://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtkmm30-devel
BuildRequires:  pcre-devel
BuildRequires:  desktop-file-utils
Requires:       smartmontools >= 5.43
Requires:       hicolor-icon-theme

%description
GSmartControl is a graphical user interface for smartctl (from
smartmontools package), which is a tool for querying and controlling
SMART (Self-Monitoring, Analysis, and Reporting Technology) data on
modern hard disk drives. It allows you to inspect the drive's SMART
data to determine its health, as well as run various tests on it.

%prep
%autosetup -p1
autoreconf -fiv


%build
%configure --docdir=%{_pkgdocdir}
%make_build

%install
%make_install
#Correct shebang
sed -i 's|/usr/bin/env bash|/usr/bin/bash|' %{buildroot}%{_bindir}/%{name}-root


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%{_bindir}/%{name}-root
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/polkit-1/actions/org.%{name}.policy
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-root.1.*
%{_pkgdocdir}
%{_datadir}/metainfo/gsmartcontrol.appdata.xml

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.3-1
- Update to 1.1.3

* Tue Oct 10 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Thu Sep 21 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.0-2
- Drop consolehelper

* Tue Sep 12 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.0-1
- Update to 1.1.0
- Drop pcrecpp patch
- Cleanup spec

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Mon Jun 19 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Sat Jun 17 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May 11 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.0-1
- Update to 0.9.0
- Update source url

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 28 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.8.7-10
- Use system pcrecpp (#1119134)
- Require usermode-gtk (#1368430)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.7-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.8.7-4
- Install docs to %%{_pkgdocdir} where available (#993808).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Eric Smith <eric@brouhaha.com>  0.8.7-1
- Update to latest upstream.
- Dropped patches 1 and 2.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.8.6-6
- Rebuild against PCRE 8.30

* Mon Jan 16 2012 Eric Smith <eric@brouhaha.com>  0.8.6-5
- Patch to compile with GCC 4.7.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Eric Smith <eric@brouhaha.com>  0.8.6-3
- Patch to work around deprecated g_static_mutex.

* Sat Dec 03 2011 Eric Smith <eric@brouhaha.com>  0.8.6-2
- Updated per package review comments.

* Sat Oct 08 2011 Eric Smith <eric@brouhaha.com>  0.8.6-1
- Updated to latest upstream release.
- Removed obsolte BuildRoot tag, clean section, defattr, etc.
- Added runtime requirements for smartmontools and hicolor-icon-theme,
  per the suggestions in the package review (bug 697247).

* Mon Apr 18 2011 Eric Smith <eric@brouhaha.com>  0.8.5-2
- Changed "Whatever" to "MIT" in license tag, based on Tom Callaway's
  post to Fedora-legal-list.

* Sun Apr 17 2011 Eric Smith <eric@brouhaha.com>  0.8.5-1
- Initial version
