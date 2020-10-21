Name:          maliit-plugins
Version:       0.94.2
Release:       17%{?dist}
Summary:       Input method plugins

License:       BSD
URL:           http://maliit.org/
Source0:       http://maliit.org/releases/%{name}/%{name}-%{version}.tar.bz2
Patch0:        olpc_xo_layout_modifications.patch

BuildRequires: dbus-devel
BuildRequires: doxygen
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: maliit-framework-devel
BuildRequires: qt-devel

%description
Maliit provides a flexible and cross-platform input method plugins. It has a
plugin-based client-server architecture where applications act as clients and
communicate with the Maliit server via input context plugins. The communication
link currently uses D-Bus.

%prep
%setup -q
%patch0 -p1 -b .olpc-layouts

%build
%{qmake_qt4} -r CONFIG+=notests CONFIG+=disable-nemo-keyboard LIBDIR=%{_libdir} MALIIT_DEFAULT_PROFILE=olpc-xo

make %{?_smp_mflags} V=1

%install
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot}

find %{buildroot} -name '*.moc' -exec rm -rf {} ';'
find %{buildroot} -name '*.gitignore' -exec rm -rf {} ';'
find %{buildroot} -name '*.olpc-layouts' -exec rm -rf {} ';'

chmod 0644 %{buildroot}%{_bindir}/maliit-keyboard*

%ldconfig_scriptlets

%files
%doc LICENSE README VERSION
%{_bindir}/maliit-keyboard*
%{_libdir}/maliit/plugins/libmaliit-keyboard-plugin.so
%{_datadir}/maliit/plugins
%doc %{_datadir}/doc/maliit-plugins/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.94.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.94.2-7
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.94.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.2-1
- New 0.94.2 release

* Sat Feb  9 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.94.0-1
- 0.94.0 release

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.1-2
- Remove old layout patch backups

* Fri Nov  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.1-1
- 0.93.1 release

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.0-3
- Remove old layout patch backups

* Wed Oct 31 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.0-2
- update OLPC keyboard layouts patch

* Mon Oct 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.93.0-1
- 0.93.0 and update OLPC keyboard layouts patch

* Tue Oct 16 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-3
- Update layout patches

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-2
- Add patch for olpc XO-Touch keyboard layouts

* Thu Sep 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.5-1
- 0.92.5 and review fixups

* Tue Aug 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.92.4-1
- Initial packaging
