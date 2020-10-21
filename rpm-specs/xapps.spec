Name:           xapps
Version:        1.8.10
Release:        1%{?dist}
Summary:        Common files for XApp desktop apps

License:        LGPLv2+
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://packages.linuxmint.com/pool/main/f/flags/flags_1.0.2.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  libgnomekbd-devel
BuildRequires:  meson
BuildRequires:  pygobject3-devel
BuildRequires:  vala

Requires:       fpaste
%if 0%{?fedora}
Requires:       inxi
%endif
Requires:       python3-xapps-overrides%{?_isa} = %{version}-%{release}
Requires:       xdg-utils
Obsoletes:      python2-xapps-overrides < %{version}-%{release}

%description
This package includes files that are shared between several XApp
apps (i18n files and configuration schemas).

%package        mate
Summary:        Mate status applet with HIDPI support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mate
Mate status applet with HIDPI support

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development libraries and header files for
developing XApp apps.

%package     -n python3-xapps-overrides
Summary:        Python%{python3_version} files for %{name}

Requires:       python3-gobject-base%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-gobject

Provides:       python3-xapps-overrides = %{version}-%{release}
Provides:       python3-xapps-overrides%{?_isa} = %{version}-%{release}

%description -n python3-xapps-overrides
Python%{python3_version} files for XApp apps.

%prep
%autosetup -p1 -n xapp-%{version}

%build
%meson -D deprecated_warnings=false
%meson_build

%install
%meson_install
tar -xf %{SOURCE1} -C %{buildroot}%{_datadir} --strip 3
rm %{buildroot}%{_datadir}/format

find %buildroot -name '*.la' -exec rm -f {} ';'

%{_bindir}/desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/xapp-sn-watcher.desktop

%find_lang xapp

%ldconfig_scriptlets


%files -f xapp.lang
%license COPYING
%doc README.md
%{_sysconfdir}/xdg/autostart/xapp-sn-watcher.desktop
%{_bindir}/pastebin
%{_bindir}/upload-system-info
%{_bindir}/xfce4-set-wallpaper
%{_libdir}/libxapp.so.*
%{_libdir}/girepository-1.0/XApp-1.0.typelib
%dir %{_libexecdir}/xapps/
%{_libexecdir}/xapps/sn-watcher/
%{_datadir}/dbus-1/services/org.x.StatusNotifierWatcher.service
%{_datadir}/iso-flag-png/
%{_datadir}/glib-2.0/schemas/org.x.apps.*.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg

%files mate
%{_libexecdir}/xapps/*.py
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateXAppStatusAppletFactory.service
%{_datadir}/mate-panel/applets/org.x.MateXAppStatusApplet.mate-panel-applet

%files devel
%{_includedir}/*
%{_libdir}/libxapp.so
%{_libdir}/pkgconfig/xapp.pc
%{_datadir}/gir-1.0/XApp-1.0.gir
%{_datadir}/glade/catalogs/xapp-glade-catalog.xml
%{_datadir}/vala/vapi/xapp.vapi
%{_datadir}/vala/vapi/xapp.deps

%files -n python3-xapps-overrides
%{python3_sitearch}/gi/overrides/XApp.py
%{python3_sitearch}/gi/overrides/__pycache__/XApp.cpython-%{python3_version_nodots}*.py*

%changelog
* Wed Sep  9 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.10-1
- Update to 1.8.10 release

* Sat Aug 15 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.9-1
- Update to 1.8.9 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.8-1
- Update to 1.8.8 release

* Sat Jun 06 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.7-1
- Update to 1.8.7 release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.6-2
- Rebuilt for Python 3.9

* Sat May 23 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.6-1
- Update to 1.8.6 release

* Thu May 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.5-1
- Update to 1.8.5 release

* Wed May 13 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.4-2
- Fix sn-watcher issue

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 1.8.4-1
- Update to 1.8.4 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.6.10-1
- Update to 1.6.10 release

* Thu Jan 09 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.6.9-1
- Update to 1.6.9 release

* Wed Dec 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.8-1
- Update to 1.6.8 release

* Tue Dec 10 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.7-1
- Update to 1.6.7 release

* Sat Dec 07 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.6-1
- Update to 1.6.6 release

* Fri Nov 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.5-1
- Update to 1.6.5 release

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.4-1
- Update to 1.6.4 release

* Tue Nov 26 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.3-1
- Update to 1.6.3 release

* Fri Nov 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.2-1
- Update to 1.6.2 release

* Tue Nov 19 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.1-2
- Add Mate status applet

* Sat Nov 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.1-1
- Update to 1.6.1 release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.4.9-1
- Update to 1.4.9 release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.8-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.4.8-1
- Update to 1.4.8 release

* Sun Jun 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.4.7-1
- Update to 1.4.7 release

* Fri Jun 14 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.4.6-1
- Update to 1.4.6 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.5-1
- Update to 1.4.5 release

* Tue Nov 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.4-1
- Update to 1.4.4 release

* Tue Nov 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.2-1
- Update to 1.4.2 release

* Mon Nov 12 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.1-1
- Update to 1.4.1 release

* Mon Nov 05 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-2
- Add Obsoletes python2-xapps-overrides to main package

* Tue Oct 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Update to 1.4.0 release

* Sun Oct 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-2
- Drop EPEL/RHEL support
- Drop python2 support

* Wed Aug 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.2-1
- Update to 1.2.2 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.7

* Sun Jun 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-2
- Fix rhbz#1589423

* Sun May 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- Update to 1.2.1 release

* Mon Apr 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- Update to 1.2.0 release

* Mon Apr 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-0.2.20180311gite5ca157
- Update to latest git

* Fri Mar 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-0.1.20180309gitfea3ca8
- Fix version

* Fri Mar 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.5-0.3.20180309gitfea3ca8
- Update to latest git

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-0.2.20180203git83d0f77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.5-0.1.20180203git83d0f77
- Update to latest git

* Sat Nov 25 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-13
- Add a base preferences dialog

* Mon Nov 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-12
- Fix Requires for F26

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-11
- Fix Requires for EPEL7

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-10
- Fix globbing of __pycache__

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-9
- Fix Python3 macro again

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-8
- Fix archful Requires

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-7
- Fix Python3 macro

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-6
- Fix build

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-5
- Adaptions for EPEL7

* Mon Nov 13 2017 Troy Curtis, Jr <troycurtisjr@gmail.com> - 1.0.4-4
- Have python2-xapps-overrides require xapps instead of the other way around.
- Use python macros

* Sat Nov 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-3
- Add requires python2-gobject-base

* Thu Oct 26 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-2
- build python XApp overrides

* Tue Oct 24 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-1
- update to 1.0.4 release

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-6
- Preserve mode of files when changing hashbang

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-5
- Use Python2 on epel

* Mon Aug 28 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.3-4
- Fix requires for epel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.3-1
- update to 1.0.3 release
- add build requires gtk-doc

* Thu Feb 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-5
- Add python3-gobject-base instead of python-gobject-base

* Thu Feb 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-4
- Add some upstream fixes

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Rebuild for Python 3.6

* Mon Nov 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-1
- update to 1.0.2 release

* Sat Nov 05 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.3.gita8d5277
- update to latest git

* Tue Oct 11 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.2.git0f28d18
- fix review issues

* Sat Oct 08 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.1.git7e7567a
- first build
