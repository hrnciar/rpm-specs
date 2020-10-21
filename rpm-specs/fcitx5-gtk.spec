%global forgeurl https://github.com/fcitx/fcitx5-gtk
%global commit 8835e96d9ce0620b930d3f4ef7db73ceae4f029c
%forgemeta

Name:           fcitx5-gtk
Version:        0
Release:        0.4%{?dist}
Summary:        Gtk im module and glib based dbus client library
License:        LGPLv2+
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Fcitx5Utils)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Gtk im module and glib based dbus client library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel%{?_isa}

%description devel
Development files for fcitx5-gtk.

%prep
%forgesetup

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install

%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/libFcitx5GClient.so.5.*
%{_libdir}/libFcitx5GClient.so.1
%{_libdir}/gtk-*/*/immodules/im-fcitx5.so
%{_libdir}/girepository-1.0/FcitxG-1.0.typelib

%files devel
%{_includedir}/Fcitx5/GClient/
%{_libdir}/cmake/Fcitx5GClient
%{_libdir}/libFcitx5GClient.so
%{_libdir}/pkgconfig/Fcitx5GClient.pc
%{_datadir}/gir-1.0/


%changelog
* Wed Sep 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.4
- upstream commit 8835e96d9ce0620b930d3f4ef7db73ceae4f029c

* Sat Sep 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.3
- Rebuild for fcitx5
- Upstream commit 0e59f66318faafc3856465a80bf42376aa5b56dc

* Sun Aug 16 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.2.20200811gitfc335f1
- rebuilt

* Wed Aug 12 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0-0.1.20200811gitfc335f1
- initial package
