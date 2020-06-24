Name:           gobby05
Version:        0.5.0
Release:        16.20171023.gite5c2d14%{?dist}
Summary:        Collaborative editor supporting multiple documents

License:        GPLv2+
URL:            https://github.com/gobby/gobby/wiki
#Source0:        http://releases.0x539.de/gobby/gobby-#{version}.tar.gz
Source0:        https://github.com/gobby/gobby/archive/e5c2d14/gobby-e5c2d14.tar.gz
# 2017-10-20: submitted upstream:
# https://github.com/gobby/gobby/pull/151
Patch0:         gobby-gtksource.patch
# 2017-10-20: submitted upstream:
# https://github.com/gobby/gobby/pull/152
Patch1:         gobby-compileerrors.patch

BuildRequires:  gcc-c++
BuildRequires:  gtkmm30-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  libinfinity-gtk-devel
BuildRequires:  libxml++-devel
BuildRequires:  intltool
# For desktop-file-install
BuildRequires: desktop-file-utils
# For gnome docs at /usr/share/gnome/help
BuildRequires:  gnome-doc-utils
# For /usr/bin/scrollkeeper-config (otherwise it failed on F20/Rawhide)
BuildRequires:  rarian-compat

Requires: ca-certificates

%description
Gobby is a free collaborative editor supporting multiple documents in one
session and a multi-user chat. It runs on Microsoft Windows, Mac OS X, Linux
and other Unix-like platforms.

%prep
%setup -q -n gobby-e5c2d145d020e080c8612f80a3d123f3a024a13a
%patch0 -p1 -b .gtksource
%patch1 -p1 -b .compileerrors


%build
./autogen.sh
# Build in C++11 mode as glibmm headers use C++11 features. This can be dropped
# when GCC in Fedora switches to C++11 by default (with GCC 6, most likely).
export CXXFLAGS="%{optflags} -std=c++11"
%configure --with-gtk3
make %{?_smp_mflags}


%install
%make_install
%find_lang gobby05
make ChangeLog


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/gobby-0.5.desktop


%files -f gobby05.lang
# FIXME: Check whether a README is added again later
%doc AUTHORS ChangeLog COPYING NEWS TODO
%{_bindir}/gobby-0.5
%{_datadir}/applications/gobby-0.5.desktop
%dir %{_datadir}/gobby-0.5/
%{_datadir}/gobby-0.5/icons/
%{_datadir}/icons/HighContrastLargePrint/48x48/apps/gobby-0.5.png
%{_datadir}/icons/HighContrastLargePrint/scalable/apps/gobby-0.5.svg
%{_datadir}/icons/HighContrastLargePrintInverse/48x48/apps/gobby-0.5.png
%{_datadir}/icons/HighContrastLargePrintInverse/scalable/apps/gobby-0.5.svg
%{_datadir}/icons/hicolor/48x48/apps/gobby-0.5.png
%{_datadir}/icons/hicolor/scalable/apps/gobby-0.5.svg
%{_mandir}/man1/gobby-0.5.1*
%{_datadir}/appdata/gobby-0.5.appdata.xml
%{_datadir}/glib-2.0/schemas/de.0x539.gobby.gschema.xml
%doc %{_datadir}/gnome/help/gobby/
%doc %{_datadir}/omf/gobby/gobby-C.omf


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-16.20171023.gite5c2d14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-15.20171023.gite5c2d14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14.20171023.gite5c2d14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13.20171023.gite5c2d14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12.20171023.gite5c2d14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Till Maas <opensource@till.name> - 0.5.0-11.20171023.gite5c2d14
- Update to snapshot to work with new libinfinity version
- Remove patch to use system CAs (this is now default)
- Add patches to remove some compile warnings
- mention gschema file in %%files

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 11 2015 Kevin Fenzi <kevin@scrye.com> 0.5.0-5
- Rebuild for c++11

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.0-3
- Use system ca-certificates (#1227163)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Oct 04 2014 Till Maas <opensource@till.name> - 0.5.0-1
- Update to new release
- Remove upstreamed patches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.94-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.4.94-7
- Fix FTBFS with gtksourceview-3.10 (#1106698)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.94-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.94-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Till Maas <opensource@till.name> - 0.4.94-4
- Do not clean the buildroot in %%install
- Use %%make_install

* Thu Jul 11 2013 Till Maas <opensource@till.name> - 0.4.94-3
- Remove executable flag from source file

* Tue Jun 11 2013 Till Maas <opensource@till.name> - 0.4.94-2
- Add new patch to compile on Rawhide/F20
- Build GNOME docs

* Sun Jul 22 2012 Till Maas <opensource@till.name> - 0.4.94-1
- Initial spec for Fedora
