%global _privatelibs libgom-1[.]0[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

Name:           gnome-online-miners
Version:        3.34.0
Release:        2%{?dist}
Summary:        Crawls through your online content

License:        GPLv2+ and LGPLv2+ and MIT
URL:            https://wiki.gnome.org/Projects/GnomeOnlineMiners
Source0:        https://download.gnome.org/sources/%{name}/3.34/%{name}-%{version}.tar.xz

BuildRequires:  gfbgraph-devel
BuildRequires:  glib2-devel >= 2.35.1
BuildRequires:  gnome-online-accounts-devel >= 3.8.0
BuildRequires:  grilo-devel >= 0.3.0
BuildRequires:  libgdata-devel >= 0.15.2
BuildRequires:  libzapojit-devel >= 0.0.2
BuildRequires:  pkgconfig
BuildRequires:  tracker-devel >= 0.17.2

Requires:       dbus
Requires:       grilo-plugins
Requires:       gvfs >= 1.18.3

%description
GNOME Online Miners provides a set of crawlers that go through your online
content and index them locally in Tracker. It has miners for Facebook, Flickr,
Google, OneDrive and Nextcloud.


%prep
%setup -q

%build
%configure \
  --disable-silent-rules \
  --disable-static

make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete

# Use %%doc instead.
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%files
%license COPYING
%doc AUTHORS
%doc NEWS
%doc README
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Facebook.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Flickr.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.GData.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.MediaServer.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Owncloud.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Zpj.service

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libgom-1.0.so

%{_libexecdir}/gom-facebook-miner
%{_libexecdir}/gom-flickr-miner
%{_libexecdir}/gom-gdata-miner
%{_libexecdir}/gom-media-server-miner
%{_libexecdir}/gom-owncloud-miner
%{_libexecdir}/gom-zpj-miner


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Wed Aug 09 2017 Debarshi Ray <rishi@fedoraproject.org> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 06 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Use license macro for COPYING

* Fri Sep 02 2016 Debarshi Ray <rishi@fedoraproject.org> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 17 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Kalev Lember <klember@redhat.com> - 3.14.3-4
- Build with grilo 0.3
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.14.3-2
- Release bump to retain the upgrade path

* Mon May 04 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.14.3-1
- Update to 3.14.3

* Tue Apr 28 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.14.2-2
- Rebuild for libgdata soname bump

* Tue Apr 14 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.14.2-1
- Update to 3.14.2

* Tue Dec 16 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.14.1-1
- Update to 3.14.1
- Bump libgdata BuildRequires to reflect reality

* Wed Sep 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0
- Ship NEWS instead of ChangeLog

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Adam Williamson <awilliam@redhat.com> - 3.12.0-2
- rebuild for new libgdata

* Sun Mar 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Wed Feb 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.90-1
- Update to 3.11.90

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Mon Jan 20 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.11.4-1
- Update to 3.11.4.

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Fri Nov 22 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.11.2-1
- Update to 3.11.2.

* Fri Nov 22 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.2-1
- Update to 3.10.2.

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.90-1
- Update to 3.9.90.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.4-3
- Filter out the private library from requires.

* Fri Jul 19 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.4-2
- Use %%{_libexecdir}.
- Filter out the private library from provides.

* Tue Jul 09 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.4-1
- Initial spec.
