# -*- rpm-spec -*-

# Default to skipping autoreconf.  Distros can change just this one line
# (or provide a command-line override) if they backport any patches that
# touch configure.ac or Makefile.am.
%{!?enable_autotools:%global enable_autotools 0}

%define with_spice 0
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 6
%define with_spice 1
%endif

%define with_govirt 0
%if 0%{?fedora} > 19 || 0%{?rhel} >= 7
%define with_govirt 1
%endif

Name: virt-viewer
Version: 9.0
Release: 2%{?dist}%{?extra_release}
Summary: Virtual Machine Viewer
License: GPLv2+
URL: http://virt-manager.org/
Source0: http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
Requires: openssh-clients
Requires(post):   %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%if 0%{?enable_autotools}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool
%endif

BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0) >= 2.40
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(libvirt) >= 0.10.0
BuildRequires: pkgconfig(libvirt-glib-1.0) >= 0.1.8
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires: pkgconfig(gtk-vnc-2.0) >= 0.4.0
BuildRequires: pkgconfig(vte-2.91)
%if %{with_spice}
BuildRequires: pkgconfig(spice-client-gtk-3.0) >= 0.35
BuildRequires: pkgconfig(spice-protocol) >= 0.12.7
%endif
BuildRequires: /usr/bin/pod2man
BuildRequires: intltool
%if %{with_govirt}
BuildRequires: pkgconfig(govirt-1.0) >= 0.3.3
%endif

%if 0%{?fedora} >= 20
Obsoletes: spice-client < 0.12.3-2
%endif


%description
Virtual Machine Viewer provides a graphical console client for connecting
to virtual machines. It uses the GTK-VNC or SPICE-GTK widgets to provide
the display, and libvirt for looking up VNC/SPICE server details.

%prep
%setup -q

%build

%if 0%{?enable_autotools}
autoreconf -if
%endif

%if %{with_spice}
%define spice_arg --with-spice-gtk
%else
%define spice_arg --without-spice-gtk
%endif

%if %{with_govirt}
%define govirt_arg --with-ovirt
%endif

%configure %{spice_arg} %{govirt_arg} --with-vte --with-buildid=%{release} --disable-update-mimedb
%__make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%__make install  DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}


%files -f %{name}.lang
%doc README.md COPYING AUTHORS ChangeLog NEWS
%{_bindir}/%{name}
%{_bindir}/remote-viewer
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/devices/*
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/appdata/remote-viewer.appdata.xml
%{_datadir}/mime/packages/virt-viewer-mime.xml
%{_mandir}/man1/virt-viewer.1*
%{_mandir}/man1/remote-viewer.1*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May  1 2020 Daniel P. Berrangé <berrange@redhat.com> - 9.0-1
- Update to 9.0 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 8.0-2
- Compile with VTE support

* Fri Mar 29 2019 Daniel P. Berrangé <berrange@redhat.com> - 8.0-1
- Update to 8.0 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 Daniel P. Berrangé <berrange@redhat.com> - 7.0-1
- Update to 7.0 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Fabiano Fidêncio <fidencio@fedoraproject.org> - 6.0-5
- Add missing patch for spice-controller so being removed

* Thu Jun 28 2018 Daniel P. Berrangé <berrange@redhat.com> - 6.0-4
- Rebuild for spice-controller so being removed

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.0-2
- Remove obsolete scriptlets

* Tue Aug 15 2017 Daniel P. Berrange <berrange@redhat.com> - 6.0-1
- Update to 6.0 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Daniel P. Berrange <berrange@redhat.com> - 5.0-1
- Update to 5.0 release

* Wed Oct 05 2016 Christophe Fergeau <cfergeau@redhat.com> 4.0-2
- Add upstream patch fixing virt-viewer window gradually getting bigger and
  bigger

* Thu Jun 30 2016 Daniel P. Berrange <berrange@redhat.com> - 4.0-1
- Update to 4.0 release

* Wed Jun 22 2016 Christophe Fergeau <cfergeau@redhat.com> - 3.0-3
- Rebuild for spice-gtk ABI break

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Fabiano Fidêncio <fidencio@redhat.com> - 3.0-1
- Update to 3.0 release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Daniel P. Berrange <berrange@redhat.com> - 2.0-1
- Update to 2.0 release

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> - 1.0-3
- update/optimize mime scriptlets

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Daniel P. Berrange <berrange@redhat.com> - 1.0-1
- Update to 1.0 release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Christophe Fergeau <cfergeau@redhat.com> 0.6.0-1
- Update to 0.6.0 release

* Tue Nov 26 2013 Christophe Fergeau <cfergeau@redhat.com> 0.5.7-2
- Rebuild for new libgovirt

* Wed Jul 31 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.7-1
- Update to 0.5.7 release

* Thu May 23 2013 Christophe Fergeau <cfergeau@redhat.com> - 0.5.6-2
- Mark remote-viewer as replacing spice-client

* Wed May  1 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.6-1
- Update to 0.5.6 release

* Wed Feb 13 2013 Daniel P. Berrange <berrange@redhat.com> - 0.5.5-1
- Update to 0.5.5 release

* Fri Dec 14 2012 Cole Robinson <crobinso@redhat.com> - 0.5.4-3
- Fix crash after entering spice password (bz #880381)

* Sat Oct 13 2012 Chris Tyler <chris@tylers.info> - 0.5.4-2
- Enabled spice support for ARM archs

* Mon Sep 17 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.4-1
- Update to 0.5.4 release

* Fri Sep 14 2012 Hans de Goede <hdegoede@redhat.com> - 0.5.3-6
- Rebuild for spice-gtk ABI breakage (previous spice-gtk build was borked)

* Tue Sep 11 2012 Hans de Goede <hdegoede@redhat.com> - 0.5.3-5
- Rebuild for spice-gtk ABI breakage

* Fri Sep  7 2012 Hans de Goede <hdegoede@redhat.com> - 0.5.3-4
- Rebuild for spice-gtk soname change

* Mon Aug 13 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.3-3
- Rebuild for spice-gtk soname change

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.3-1
- Update to 0.5.3 release

* Fri Mar  9 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.2-1
- Update to 0.5.2 release

* Fri Feb 17 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.1-1
- Update to 0.5.1 release

* Tue Feb 14 2012 Daniel P. Berrange <berrange@redhat.com> - 0.5.0-1
- Update to 0.5.0 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.2-1
- Update to 0.4.2 release

* Sun Aug 14 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-3
- More ssh tunnelling port fixes

* Fri Aug 12 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-2
- Fix ssh tunnelling

* Thu Aug  4 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.1-1
- Update to 0.4.1 release

* Tue Aug  2 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.0-2
- Rebuild for accidental spice-glib soname change

* Tue Jul 12 2011 Daniel P. Berrange <berrange@redhat.com> - 0.4.0-1
- Update to 0.4.0 release
- Switch build to GTK3 instead of GTK2

* Tue May 31 2011 Daniel P. Berrange <berrange@redhat.com> - 0.3.1-2
- Rebuild for spice-glib ABI breakage

* Wed May 11 2011 Karsten Hopp <karsten@redhat.com> 0.3.1-1.1
- spice-gtk is x86 x86_64 only, don't require it on other archs

* Mon Feb 21 2011 Daniel P. Berrange <berrange@redhat.com> - 0.3.1-1
- Update to 0.3.1 release

* Mon Feb 21 2011 Daniel P. Berrange <berrange@redhat.com> - 0.3.0-1
- Update to 0.3.0 and enable SPICE

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 15 2010 Daniel P. Berrange <berrange@redhat.com> - 0.2.1-1
- Update to 0.2.1 release

* Wed Jul 29 2009 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-1.fc12
- Update to 0.2.0 release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Daniel P. Berrange <berrange@redhat.com> - 0.0.3-5.fc12
- Fix auth against libvirt (rhbz #499594)
- Fix confusion of VNC credentials (rhbz #499595)
- Correct keyboard grab handling (rhbz #499362)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.3-3.fc10
- fix conditional comparison
- remove file dep

* Wed Jun 25 2008 Daniel P. Berrange <berrange@redhat.com> - 0.0.3-2.fc10
- Rebuild for GNU TLS ABI bump

* Mon Mar 10 2008 Daniel P. Berrange <berrange@redhat.com> - 0.0.3-1.fc9
- Updated to 0.0.3 release

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.2-4
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Daniel P. Berrange <berrange@redhat.com> - 0.0.2-3.fc9
- Set domain name as window title
- Hide input for passwd fields during auth

* Mon Oct 15 2007 Daniel P. Berrange <berrange@redhat.com> - 0.0.2-2.fc8
- Change TLS x509 credential name to sync with libvirt

* Tue Aug 28 2007 Daniel P. Berrange <berrange@redhat.com> - 0.0.2-1.fc8
- Added support for remote console access

* Fri Aug 17 2007 Daniel P. Berrange <berrange@redhat.com> - 0.0.1-2.fc8
- Restrict built to x86 & ia64 because libvirt is only on those arches

* Wed Aug 15 2007 Daniel P. Berrange <berrange@redhat.com> - 0.0.1-1.fc8
- First release
