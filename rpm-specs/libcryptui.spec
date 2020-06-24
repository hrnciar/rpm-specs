Name:    libcryptui
Version: 3.12.2
Release: 19%{?dist}
Summary: Interface components for OpenPGP

License: LGPLv2+
URL:     http://projects.gnome.org/seahorse/
Source0: http://download.gnome.org/sources/libcryptui/3.12/%{name}-%{version}.tar.xz
Patch0:  libcryptui-3.12.2-gpg22.patch
Patch1:  libcryptui-3.12.2-use-gcr.patch

BuildRequires: autoconf automake
BuildRequires: gnupg
BuildRequires: gobject-introspection-devel
BuildRequires: gpgme-devel
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gcr-3)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(sm)

%description
libcryptui is a library used for prompting for PGP keys.

%package devel
Summary: Header files required to develop with libcryptui
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The libcryptui-devel package contains the header files and developer
documentation for the libcryptui library.

%prep
%autosetup -p1
autoreconf --force --install

%build
%configure
%make_build

%install
%make_install
%find_lang cryptui --with-gnome --all-name

find ${RPM_BUILD_ROOT} -type f -name "*.a" -delete
find ${RPM_BUILD_ROOT} -type f -name "*.la" -delete

%files -f cryptui.lang
%license COPYING-LIBCRYPTUI
%doc AUTHORS NEWS README
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_datadir}/cryptui
%{_libdir}/libcryptui.so.*
%{_datadir}/dbus-1/services/*
%{_datadir}/pixmaps/cryptui
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*
%{_datadir}/GConf/gsettings/org.gnome.seahorse.recipients.convert
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.recipients.gschema.xml

%files devel
%{_libdir}/libcryptui.so
%{_libdir}/pkgconfig/*
%{_includedir}/libcryptui
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libcryptui
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 David King <amigadave@amigadave.com> - 3.12.2-17
- Use pkgconfig for BuildRequires
- Improve man page glob
- Use gcr instead of libgnome-keyring

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Pete Walter <pwalter@fedoraproject.org> - 3.12.2-15
- Modernize the spec file
- Fix gir and gtk-doc directory ownership

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.12.2-12
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.12.2-8
- Rebuild for gpgme 1.18

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.12.2-6
- Add gnupg dep to fix FTBFS
- Use %%licence

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Aug 28 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> -3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Tomas Bzatek <tbzatek@redhat.com> - 3.5.92-1
- Update to 3.5.92

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Silence rpm scriptlet output

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Fri Mar  9 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Thu Jan 26 2012 Tomas Bzatek <tbzatek@redhat.com> - 3.2.2-3
- Fix BuildRequires

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.2-1
- Update to 3.2.2

* Fri Nov 18 2011 Matthew Barnes <mbarnes@redhat.com> - 3.2.0-2
- Remove gtk-doc req in devel subpackage (RH bug #754500).

* Wed Sep 28 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Wed Jul 27 2011 Matthew Barnes <mbarnes@redhat.com> - 3.1.4-3
- Add upstream patch to avoid file conflicts with seahorse.

* Tue Jul 26 2011 Matthew Barnes <mbarnes@redhat.com> - 3.1.4-2
- Package review changes.

* Mon Jul 25 2011 Matthew Barnes <mbarnes@redhat.com> - 3.1.4-1
- Initial packaging.
