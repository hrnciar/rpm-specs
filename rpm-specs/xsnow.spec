Name:           xsnow
Version:        3.0.3
Release:        1%{?dist}
Summary:        Let it snow on your desktop

License:        GPLv3+
URL:            https://sourceforge.net/projects/xsnow/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXext-devel
BuildRequires:  libxml2-devel
BuildRequires:  gtk3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
Xsnow is a X Window application that will snow on the desktop background.
Santa and his reindeer will complete your festive-season feeling.
Xsnow runs in GNOME, KDE, FVWM and desktops that are derived from those.


%prep
%autosetup

# Fix Makefile
sed -i 's!$(exec_prefix)/games!$(exec_prefix)/bin!' src/Makefile.in


%build
%configure
%make_build


%install
%make_install

# Fix desktop file
desktop-file-install \
  --delete-original \
  --set-icon=%{name} \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install AppData file
install -d %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man6/%{name}.6*
%{_metainfodir}/%{name}.appdata.xml
%license COPYING
%doc AUTHORS README


%changelog
* Sun Aug 09 2020 Andrea Musuruane <musuruan@gmail.com> - 3.0.3-1
- Updated to new upstream release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Andrea Musuruane <musuruan@gmail.com> - 2.0.22-1
- Updated to new upstream release

* Wed May 20 2020 Andrea Musuruane <musuruan@gmail.com> - 2.0.21-1
- Updated to new upstream release

* Fri Feb 07 2020 Andrea Musuruane <musuruan@gmail.com> - 2.0.17-1
- Updated to new upstream release

* Fri Feb 07 2020 Andrea Musuruane <musuruan@gmail.com> - 2.0.16-1
- Updated to new upstream release

* Wed Feb 05 2020 Andrea Musuruane <musuruan@gmail.com> - 2.0.15-3
- Fix FTBFS for F32

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Andrea Musuruane <musuruan@gmail.com> - 2.0.15-1
- Updated to new upstream release

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.42-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.42-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.42-24
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Sat Jul 28 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.42-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.42-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.42-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.42-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.42-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.42-18
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.42-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 12 2009 Andrea Musuruane <musuruan@gmail.com> 1.42-16
- first release for RPM Fusion
- updated package to Fedora guidelines
- used Debian patches

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Than Ngo <than@redhat.com> 1.42-14
- cleanup codes, #116665

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Nov 26 2003 Than Ngo <than@redhat.com> 1.42-12
- BuildRequires on XFree86-devel

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Nov  7 2002 Than Ngo <than@redhat.com> 1.42-9
- fix unpackaged files issue

* Mon Aug 26 2002 Than Ngo <than@redhat.com> 1.42-8
- get rid of desktop file (bug #69556)
 
* Wed Jul 24 2002 Than Ngo <than@redhat.com> 1.42-7
- desktop file issue (bug #69556)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr 24 2002 Than Ngo <than@redhat.com> 1.42-4
- add missing icon

* Mon Feb 25 2002 Than Ngo <than@redhat.com> 1.42-3
- rebuild in new enviroment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 21 2001 Than Ngo <than@redhat.com> 1.42-1
- update to 1.42
- add Url
- fix bug #53192, #53194, #52132

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- built for the distro

* Tue Nov 7 2000 Than Ngo <than@redhat.com>
- clean up specfile

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Thu Jul 13 2000 Than Ngo <than@redhat.de>
- rebuilt

* Thu Jun 01 2000 Than Ngo <than@redhat.de>
- rebuild for 7.0
- gzip man page
- remove wmconfig/xsnow, add xsnow.desktop

* Tue Jul 27 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Mon Dec 20 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

