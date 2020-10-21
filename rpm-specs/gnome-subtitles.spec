Name:           gnome-subtitles
Version:        1.6
Release:        6%{?dist}
Summary:        Subtitle editor for Gnome

#Files under src/External/NCharDet are MPLv1.1 or GPLv2+ or LGPLv2+
License:        GPLv2+ and (MPLv1.1 or GPLv2+ or LGPLv2+)
URL:            http://gnome-subtitles.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gnome-doc-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  mono-devel
BuildRequires:  mono-web
BuildRequires:  perl(XML::Parser)

Requires:       enchant
Requires:       gstreamer1-plugins-good-gtk
Requires:       hicolor-icon-theme
Requires:       mono-locale-extras

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Gnome Subtitles is a subtitle editor for the GNOME desktop. It supports the
most common text-based subtitle formats and allows for subtitle editing,
translation and synchronization.

%prep
%autosetup


%build
%configure
%make_build


%install
%make_install
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GnomeSubtitles.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/org.gnome.GnomeSubtitles.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.GnomeSubtitles.gschema.xml
%{_datadir}/help/*/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/org.gnome.GnomeSubtitles.appdata.xml


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-4
- Add missing gstreamer1-plugins-good-gtk dependency (RH #1819653)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-2
- Add enchant dependency (RH #1750161)

* Thu Sep 05 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.6-1
- Update to 1.6

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.5-1
- Update to 1.5
- Add itstool to BuildRequires
- Add hicolor-icon-theme to Requires

* Sun Apr 07 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.4-5
- Add mono-web to BuildRequires
- Drop obsolete --disable-schemas-install %%configure switch

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.4-4
- Remove obsolete requirements for %%post/%%pre/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.4-1
- Updated to 1.4
- Modernised the spec file
- Dropped upstreamed patch and appstream file
- Dropped obsolete scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- mono rebuild for aarch64 support

* Mon Feb 15 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1.3-9
- Patched to use mcs as dmcs is no longer available

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-6
- Rebuild (mono4)

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.3-5
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Julian Sikorski <belegdol@fedoraproject.org> - 1.3-1
- Updated to 1.3
- Updated BRs to gstreamer-1.0
- De-vendorised the .desktop file

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Julian Sikorski <belegdol@fedoraproject.org> - 1.2-2
- Rebuilt for gcc-4.7
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Tue Aug 23 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1.2-1
- Updated to 1.2
- Updated the URL

* Fri Feb 25 2011 Dan Horák <dan[at]danny.cz> - 1.1-3
- updated the supported arch list

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 31 2010 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-1
- Updated to 1.1
- Dropped security fix, it is now included in the source

* Sun Oct 03 2010 Julian Sikorski <belegdol@fedoraproject.org> - 1.0-3
- Switched to upstreams approach for the security fix
- Use the new macros properly

* Thu Sep 30 2010 Julian Sikorski <belegdol@fedoraproject.org> - 1.0-2
- Fixed security vulnrerability CVE-2010-3357
- Updated scriptlets to the latest spec
- Dropped scrollkeeper BR

* Sat Feb 20 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 1.0-1
- Updated to 1.0

* Thu Jan 14 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.1-3
- Actually do what the changelog says

* Thu Jan 14 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.1-2
- Added mono-locale-extras to Requires (fixes gnome bug #606905)

* Sun Nov 01 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.9.1-1
- Updated to 0.9.1
- Dropped the SMP build patch
- Added desktop-database scriptlets
- Re-enabled parallel make
- Updated the License tag
- Added intltool to BuildRequires, removed explicit gettext

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.8-10
- ExcludeArch sparc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Xavier lamien <laxathom@fedoraproject.org> - 0.8-8
- Build arch ppc64.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8-6
- don't use smp_mflags

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8-5
- rebuild against new gnome-sharp

* Sat Jul  5 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8-4
- Another rebuild
- Patched SMP build failure

* Mon May 26 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8-3
- Rebuilt to fix broken deps

* Sun May 18 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8-2
- Added sublib-devel to BuildRequires

* Sat May 17 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8-1
- Updated to 0.8
- Dropped upstreamed patches
- Dropped SMP build, seems to cause problems
- Added missing %%doc
- Added wildcard to manpage install location

* Fri Mar 28 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.7.2-2
- Added patch fixing empty debuginfo issue
- Added ExcludeArch: ppc64
- Replaced make and rm invocations with macros

* Tue Jan 15 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.7.2-1
- Initial RPM release
