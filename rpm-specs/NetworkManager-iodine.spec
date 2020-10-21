%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%bcond_without libnm_glib
%else
# Disable the legacy version by default
%bcond_with libnm_glib
%endif

Summary: NetworkManager VPN plugin for iodine
Name: NetworkManager-iodine
Version: 1.2.0
Release: 11%{?dist}
License: GPLv2+
URL: https://honk.sigxcpu.org/piki/projects/network-manager-iodine
Source0: https://download.gnome.org/sources/NetworkManager-iodine/1.2/%{name}-1.2.0.tar.xz

BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1:1.1.0
BuildRequires: glib2-devel
BuildRequires: libtool intltool gettext
BuildRequires: libnma-devel >= 1.1.0
BuildRequires: libsecret-devel
Requires: shared-mime-info
Requires: iodine-client
Requires: dbus
Requires: NetworkManager >= 1:1.2.0-0.3

%if %with libnm_glib
BuildRequires: NetworkManager-glib-devel >= 1:1.1.0
BuildRequires: libnm-gtk-devel >= 0.9.9.0
%endif

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating VPN capabilities with
the iodine server and NetworkManager.

%package -n NetworkManager-iodine-gnome
Summary: NetworkManager VPN plugin for iodine - GNOME files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: nm-connection-editor

%description -n NetworkManager-iodine-gnome
This package contains software for integrating VPN capabilities with
the iodine server and NetworkManager (GNOME files).

%prep
%setup -q

%build
%configure \
        --disable-static \
%if %without libnm_glib
        --without-libnm-glib \
%endif
        --enable-more-warnings=yes
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la

%find_lang %{name}

%files -f %{name}.lang
%{_sysconfdir}/dbus-1/system.d/nm-iodine-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-iodine-service.name
%{_libexecdir}/nm-iodine-service
%{_libexecdir}/nm-iodine-auth-dialog
%doc AUTHORS NEWS
%license COPYING

%files -n NetworkManager-iodine-gnome
%{_libdir}/NetworkManager/lib*.so*
%dir %{_datadir}/gnome-vpn-properties/iodine
%{_datadir}/gnome-vpn-properties/iodine/nm-iodine-dialog.ui
%{_datadir}/appdata/network-manager-iodine.appdata.xml

%if %with libnm_glib
%{_sysconfdir}/NetworkManager/VPN/nm-iodine-service.name
%endif

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-5
- Drop libnm-glib for Fedora 28

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr 23 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-1
- Update to 1.2.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.2.20151023git23cf4d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.1.20151023git23cf4d1
- Update to 1.2 git snapshot with multiple connections support

* Mon Aug 31 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.1.20150901git384794c
- Update to 1.2 git snapshot with libnm-based properties plugin

* Tue Jul 14 2015 Dan Fruehauf<malkodan@gmail.com> - 0.0.5-2
- Fix dependencies (NetworkManager-gnome is gone)

* Sat Jul 11 2015 Dan Fruehauf<malkodan@gmail.com> - 0.0.5-1
- Release 0.0.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.4-2
- Removed auto required packages

* Fri Dec 13 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.4-1
- Changes for review

* Tue Dec 10 2013 Dan Fruehauf <malkodan@gmail.com> - 0.0.4-0.1.20131210gita2a90c6
- Initial spec release
