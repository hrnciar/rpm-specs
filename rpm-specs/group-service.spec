Name:          group-service
Version:       1.2.0
Release:       3%{?dist}
Summary:       Dbus Group management CLI tool
License:       GPLv3+ 
URL:           https://github.com/zhuyaliang/%{name}

# downloading the tarball
# spectool -g group-service.spec
Source0:       %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: gettext
BuildRequires: systemd-devel
BuildRequires: dbus-devel
BuildRequires: libxcrypt-devel
BuildRequires: meson
BuildRequires: polkit-devel
%if 0%{?fedora} && 0%{?fedora} >= 30
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd
%endif

%{?systemd_requires}

%description
Dbus Group management CLI tool

%package devel
Summary:  Support for developing back-ends for group-service
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files needed for
group-service back-ends development.


%prep
%autosetup -p1

%if (0%{?fedora} && 0%{?fedora} == 28) || 0%{?el8}
sed -i s/"meson_version : '>=0.50.0',"/"meson_version : '>=0.46.0',"/g meson.build
%endif

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome --all-name

%post
%systemd_post group-admin-daemon.service

%preun
%systemd_preun group-admin-daemon.service

%postun
%systemd_postun group-admin-daemon.service


%files -f %{name}.lang
%doc README.md
%license COPYING
%{_sysconfdir}/dbus-1/system.d/org.group.admin.conf
%{_libdir}/libgroup-service.so.1*
%{_libexecdir}/group-admin-daemon
%{_datadir}/dbus-1/interfaces/org.group.admin.list.xml
%{_datadir}/dbus-1/interfaces/org.group.admin.xml
%{_datadir}/dbus-1/system-services/org.group.admin.service
%{_datadir}/polkit-1/actions/org.group.admin.policy
%{_unitdir}/group-admin-daemon.service

%files devel
%{_includedir}/group-service-1.0/
%{_libdir}/libgroup-service.so
%{_libdir}/pkgconfig/group-service.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.2.0-1
- update to  1.2.0

* Fri Sep 27 2019 Thomas Batten <stenstorpmc@gmail.com> - 1.1.0-7
- force older meson version on el8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.1.0-5
- Rebuild with Meson fix for #1699099

* Mon Mar 25 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.0-4
- add upsream patch to fix soname version

* Sat Mar 23 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.0-3
- update tarball and drop patch
- update shared libraries packaging

* Sat Mar 23 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.0-2
- fix source link
- fix description
- fix packaging shared libraries
- add upstream patch to fix include dir

* Mon Mar 18 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.1.0-1
- initial package build

