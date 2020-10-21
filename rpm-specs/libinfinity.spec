%bcond_without gnome

%global libversion 0.7

Name:           libinfinity
Version:        0.7.1
Release:        10%{?dist}
Summary:        Library implementing the infinote protocol

License:        LGPLv2+
URL:            http://gobby.0x539.de/trac/wiki/Infinote/Libinfinity
Source0:        http://releases.0x539.de/libinfinity/libinfinity-%{version}.tar.gz
Source1:        http://releases.0x539.de/libinfinity/libinfinity-%{version}.tar.gz.sig
Source2:        gpgkey-728834F3B8D552ED25CC1B1FB1C71544BF1D92C7.gpg

BuildRequires:  avahi-devel
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  libxml2-devel
BuildRequires:  libgsasl-devel
%if %{with gnome}
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
%endif
BuildRequires:  chrpath
BuildRequires:  gettext
BuildRequires:  pam-devel
BuildRequires:  libdaemon-devel
# For source verification with gpgv
BuildRequires:  gpg
BuildRequires:  gcc-c++

%description
libinfinity is an implementation of the Infinote protocol written in GObject-based C.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       avahi-devel
Requires:       glib2-devel
Requires:       gnutls-devel
Requires:       libxml2-devel
Requires:       libgsasl-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with gnome}
%package        gtk
Summary:        GTK widgets for libinfinity

%description    gtk
Widgets and dialogs for libinfinity in GTK3.


%package        gtk-devel
Summary:        Development files for %{name}-gtk
Requires:       %{name}-gtk = %{version}-%{release}
Requires:       pkgconfig
Requires:       libinfinity-devel
Requires:       gtk3-devel

%description    gtk-devel
The %{name}-gtk-devel package contains libraries and header files for
developing applications that use %{name}-gtk.
%endif

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for the %{name} libraries.


%package -n     infinoted
Summary:        Server for the infinote protocol

%description -n infinoted
Server daemon for the infinote protocol.


%prep
gpgv --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q


%build
%configure \
%if %{with gnome}
    --with-gtk3=yes \
%endif
    --disable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}-%{libversion}
chrpath -d %{buildroot}%{_bindir}/infinoted-%{libversion}
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-autosave.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-certificate-auth.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-dbus.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-directory-sync.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-document-stream.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-linekeeper.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-logging.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-note-chat.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-note-text.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-record.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-traffic-logging.so
chrpath -d %{buildroot}%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-transformation-protection.so
chrpath -d %{buildroot}%{_libdir}/libinfinoted-plugin-manager-%{libversion}.so.0.0.0
chrpath -d %{buildroot}%{_libdir}/libinftext-%{libversion}.so.0.0.0
%if %{with gnome}
chrpath -d %{buildroot}%{_libdir}/libinfgtk-%{libversion}.so.0.0.0
chrpath -d %{buildroot}%{_libdir}/libinftextgtk-%{libversion}.so.0.0.0
%endif

%files -f %{name}-%{libversion}.lang
%doc AUTHORS ChangeLog COPYING
%{_libdir}/libinfinity-%{libversion}.so.0
%{_libdir}/libinfinity-%{libversion}.so.0.0.0
%{_libdir}/libinftext-%{libversion}.so.0
%{_libdir}/libinftext-%{libversion}.so.0.0.0
%{_datadir}/icons/hicolor/*/apps/infinote.*

%files devel
%{_includedir}/libinfinity-%{libversion}/
%{_includedir}/libinftext-%{libversion}/
%{_includedir}/libinfinoted-plugin-manager-%{libversion}/
%{_libdir}/libinfinity-%{libversion}.so
%{_libdir}/libinfinoted-plugin-manager-%{libversion}.so
%{_libdir}/libinftext-%{libversion}.so

%{_libdir}/pkgconfig/libinfinity-%{libversion}.pc
%{_libdir}/pkgconfig/libinfinoted-plugin-manager-%{libversion}.pc
%{_libdir}/pkgconfig/libinftext-%{libversion}.pc

%if %{with gnome}
%files gtk
%{_libdir}/libinfgtk-%{libversion}.so.0
%{_libdir}/libinfgtk-%{libversion}.so.0.0.0
%{_libdir}/libinftextgtk-%{libversion}.so.0
%{_libdir}/libinftextgtk-%{libversion}.so.0.0.0

%files gtk-devel
%{_includedir}/libinfgtk-%{libversion}/
%{_includedir}/libinftextgtk-%{libversion}/
%{_libdir}/libinfgtk-%{libversion}.so
%{_libdir}/libinftextgtk-%{libversion}.so
%{_libdir}/pkgconfig/libinfgtk-%{libversion}.pc
%{_libdir}/pkgconfig/libinftextgtk-%{libversion}.pc
%endif

%files doc
%{_datadir}/gtk-doc/html/libinfgtk-%{libversion}/
%{_datadir}/gtk-doc/html/libinfinity-%{libversion}/
%{_datadir}/gtk-doc/html/libinfinoted-plugin-manager-%{libversion}/
%{_datadir}/gtk-doc/html/libinftextgtk-%{libversion}/
%{_datadir}/gtk-doc/html/libinftext-%{libversion}/

%files -n infinoted
%{_bindir}/infinoted-%{libversion}
%dir %{_libdir}/infinoted-%{libversion}/
%dir %{_libdir}/infinoted-%{libversion}/plugins/
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-autosave.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-certificate-auth.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-dbus.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-directory-sync.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-document-stream.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-linekeeper.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-logging.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-note-chat.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-note-text.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-record.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-traffic-logging.so
%{_libdir}/infinoted-%{libversion}/plugins/libinfinoted-plugin-transformation-protection.so
%{_libdir}/libinfinoted-plugin-manager-%{libversion}.so.0
%{_libdir}/libinfinoted-plugin-manager-%{libversion}.so.0.0.0
%{_mandir}/man1/infinoted-*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 0.7.1-6
- Fix FTBFS bug #1604600

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Kevin Fenzi <kevin@scrye.com> - 0.7.1-1
- Update to 0.7.1. Fixes bugs #1423854 and #1411175
- Drop special cxxflags, gcc6 defaults to c++11

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Till Maas <opensource@till.name> - 0.7.0-1
- Update to new release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Kevin Fenzi <kevin@scrye.com> - 0.6.7-2
- Clean up global vs define

* Sat Oct 17 2015 Till Maas <opensource@till.name> - 0.6.7-1
- Update to new release
- Update GPG key

* Sun Oct 11 2015 Kevin Fenzi <kevin@scrye.com> 0.6.6-3
- Rebuild with stdc++11

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Till Maas <opensource@till.name> - 0.6.6-1
- Update to new release, fixes security issue:
  https://github.com/gobby/gobby/issues/61, #1221266

* Sun Nov 09 2014 Till Maas <opensource@till.name> - 0.6.4-1
- Update to new release

* Tue Oct 21 2014 Till Maas <opensource@till.name> - 0.6.3-1
- Update to new release

* Sat Sep 20 2014 Till Maas <opensource@till.name> - 0.6.2-1
- Update to new release

* Fri Aug 29 2014 Till Maas <opensource@till.name> - 0.6.1-1
- Update to new release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 13 2014 Till Maas <opensource@till.name> - 0.5.5-1
- Update to new release

* Mon Oct 14 2013 Till Maas <opensource@till.name> - 0.5.4-4
- re-enable gnome support for Fedora

* Sun Oct 13 2013 Till Maas <opensource@till.name> - 0.5.4-3
- Harden build

* Sat Oct 12 2013 Matěj Cepl <mcepl@redhat.com> - 0.5.4-2
- Make infinoted build on EL-6

* Sun Aug 25 2013 Till Maas <opensource@till.name> - 0.5.4-1
- Update to new bugfix release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Till Maas <opensource@till.name> - 0.5.3-1
- Update to new bugfix release
- Use finer globbing for manpage

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Till Maas <opensource@till.name> - 0.5.2-1
- Update to new release
- Update description

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.2-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Ben Boeckel <mathstuf@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Thu May 20 2010 Ben Boeckel <MathStuf@gmail.com> - 0.4.1-1
- Update to 0.4.1
- %%define the libversion suffix

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Ben Boeckel <MathStuf@gmail.com> 0.3.0-2
- Build everything (added gettext, avahi-devel, and gtk2-devel)
- Add gtk sub-packages

* Sat Jun 20 2009 Ben Boeckel <MathStuf@gmail.com> 0.3.0-1
- Initial package
