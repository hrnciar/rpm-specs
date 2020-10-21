Name:           malcontent
Version:        0.8.0
Release:        5%{?dist}
Summary:        Parental controls implementation

License:        LGPLv2+
URL:            https://gitlab.freedesktop.org/pwithnall/malcontent/
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-testing-0)
BuildRequires:  pam-devel

Requires: polkit

# Descriptions mostly gathered from:
# https://github.com/endlessm/malcontent/blob/debian-master/debian/control

%description
libmalcontent implements parental controls support which can be used by
applications to filter or limit the access of child accounts to inappropriate
content.

%package control
Summary:        Parental Controls UI

%description control
This package contains a user interface for querying and setting parental
controls for users.

%package pam
Summary:        Parental Controls PAM Module

%description pam
This package contains a PAM module which prevents logins for users who have
exceeded their allowed computer time.

%package tools
Summary:        Parental Controls Tools

%description tools
This package contains tools for querying and updating the parental controls
settings for users.

%package ui-devel
Summary:        Development files for libmalcontent-ui
Requires:       %{name}-ui-libs%{?_isa} = %{version}-%{release}

%description ui-devel
This package contains the pkg-config file and development headers
for libmalcontent-ui.

%package ui-libs
Summary:        Libraries for %{name}

%description ui-libs
This package contains libmalcontent-ui.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the pkg-config file and development headers
for %{name}.

%package libs
Summary:        Libraries for %{name}

%description libs
This package contains libmalcontent.

%prep
%autosetup -p1

%build
%meson -Dui=enabled
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.freedesktop.MalcontentControl.appdata.xml

%files -f %{name}.lang
%license COPYING COPYING-DOCS
%doc README.md
%{_datadir}/accountsservice/interfaces/
%{_datadir}/dbus-1/interfaces/
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/polkit-1/rules.d/com.endlessm.ParentalControls.rules

%files control
%license COPYING
%doc README.md
%{_bindir}/malcontent-control
%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.MalcontentControl.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.freedesktop.MalcontentControl-symbolic.svg
%{_datadir}/metainfo/org.freedesktop.MalcontentControl.appdata.xml

%files pam
%license COPYING
%{_libdir}/security/pam_malcontent.so

%files tools
%license COPYING
%{_bindir}/malcontent-client
%{_mandir}/man8/malcontent-client.8.*

%files ui-devel
%license COPYING
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/MalcontentUi-0.gir
%{_libdir}/libmalcontent-ui-0.so
%{_includedir}/malcontent-ui-0/
%{_libdir}/pkgconfig/malcontent-ui-0.pc

%files ui-libs
%license COPYING
%doc README.md
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/MalcontentUi-0.typelib
%{_libdir}/libmalcontent-ui-0.so.*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Malcontent-0.gir
%{_includedir}/malcontent-0/
%{_libdir}/libmalcontent-0.so
%{_libdir}/pkgconfig/malcontent-0.pc

%files libs
%license COPYING
%doc README.md
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/Malcontent-0.typelib
%{_libdir}/libmalcontent-0.so.*

%changelog
* Tue Sep 08 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-5
+ malcontent-0.8.0-5
- More review comments

* Mon Sep 07 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-4
+ malcontent-0.8.0-4
- Fix more review comments again

* Fri Sep 04 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-3
+ malcontent-0.8.0-3
- Fix more review comments

* Fri Aug 28 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-2
+ malcontent-0.8.0-2
- Fix review comments

* Thu Jul 23 2020 Bastien Nocera <bnocera@redhat.com> - 0.8.0-1
+ malcontent-0.8.0-1
- First package
