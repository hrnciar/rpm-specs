Name:           maliit-framework
Version:        0.94.2
Release:        21%{?dist}
Summary:        Input method framework

License:        LGPLv2
URL:            http://maliit.org/
Source0:        http://maliit.org/releases/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: gtk-doc
BuildRequires: hunspell-devel
BuildRequires: libX11-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: qt-devel
BuildRequires: systemd-devel

%description
Maliit provides a flexible and cross-platform input method framework. It has a
plugin-based client-server architecture where applications act as clients and
communicate with the Maliit server via input context plugins. The communication
link currently uses D-Bus.

%package qt4
Summary: Input method module for Qt 4 based on Maliit framework
Requires: %{name}%{?_isa} = %{version}-%{release}

%description qt4
Input method module for Qt 4 based on Maliit framework.

%package gtk2
Summary: Input method module for GTK+ 2 based on Maliit framework
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gtk2
Input method module for GTK+ 2 based on Maliit framework.

%package gtk3
Summary: Input method module for GTK+ 3 based on Maliit framework
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gtk3
Input method module for GTK+ 3 based on Maliit framework.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package docs
Summary: Documentation files for %{name}

%description docs
This package contains developer documentation for %{name}.

%package examples
Summary: Tests and examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk3%{?_isa} = %{version}-%{release}
Requires: %{name}-qt4%{?_isa} = %{version}-%{release}

%description examples
This package contains tests and examples for %{name}.

%prep
%setup -q
sed -i 's/ -O0//' config.pri

# Fix shebang of maliit-exampleapp-gtk3-python.py executable to avoid depending on Python 2.
sed -i '1s=^#!/usr/bin/env python=#!/usr/bin/python3=' examples/apps/gtk3-python/maliit-exampleapp-gtk3-python.py

%build

%{qmake_qt4} -r MALIIT_VERSION=%{version} PREFIX=%{_prefix} \
             BINDIR=%{_bindir} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir} \
             MALIIT_ENABLE_MULTITOUCH=true MALIIT_DEBUG=disabled \
             CONFIG+=disable-gtk-cache-update CONFIG+=disable-preedit \
             CONFIG+=enable-hunspell CONFIG+=enable-dbus-activation \
	     CONFIG+=disable-background-translucency

make %{?_smp_mflags} V=1

%install
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot}

find %{buildroot} -name '.moc' -delete
find %{buildroot} -name '.gitignore' -delete

# e.g. maliit-plugins package stores files in there
mkdir -p %{buildroot}%{_datadir}/maliit

%ldconfig_scriptlets

%files
%license LICENSE.LGPL
%doc README NEWS
%{_bindir}/maliit-server
%{_libdir}/libmaliit*.so.*
%dir %{_libdir}/maliit
%dir %{_libdir}/maliit/plugins
%dir %{_libdir}/maliit/plugins/factories
%{_libdir}/maliit/plugins/factories/libmaliit-plugins-quick-factory.so
%{_libdir}/girepository-1.0/Maliit-1.0.typelib
%{_datadir}/maliit/
%{_datadir}/dbus-1/services/org.maliit.server.service

%files qt4
%{_libdir}/qt4/plugins/inputmethods/libmaliit*

%files gtk2
%{_libdir}/gtk-2.0/2.10.0/immodules/libim-maliit.so

%files gtk3
%{_libdir}/gtk-3.0/3.0.0/immodules/libim-maliit.so

%files devel
%{_includedir}/maliit/
%{_libdir}/libmaliit*.so
%{_libdir}/pkgconfig/maliit*.pc
%{_libdir}/qt4/mkspecs/features/maliit*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Maliit-1.0.gir

%files docs
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/maliit/
%{_datadir}/doc/maliit-framework/html

%files examples
%{_bindir}/maliit-example*
%{_libdir}/maliit-framework-tests

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 04 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 0.94.2-16
- Fix Python shebang in examples subpackage to avoid depending on Python2

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.94.2-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.94.2-9
- use %%qmake_qt4 macro to ensure proper build flags

* Sun Jul 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.2-8
- Fix ftbfs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.94.2-5
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.94.2-3
- Fix duplicate documentation (#1001288)
- Add BR graphviz for /usr/bin/dot (missing images in documentation)
- Fix summaries, descriptions and Group tags of IM module subpackages
- Fix directory ownership

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.2-1
- New 0.94.2 release

* Wed Jan 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.1-1
- New 0.94.1 release

* Fri Jan 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.0-1
- New 0.94.0 release

* Fri Nov  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.1-1
- New 0.93.1 release

* Mon Oct 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.0-1
- New 0.93.0 release

* Tue Oct  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5.1-1
- 0.95.2.1 to add support for detecting tablet mode changes

* Thu Oct  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-2
- Fix the updating of the gtk2 IM module cache

* Thu Sep 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-1
- New 0.92.5 release, update based on review comments

* Tue Aug 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.4-1
- Initial packaging
