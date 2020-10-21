Name:           fritzing
Version:        0.9.2b
Release:        21%{?dist}
Summary:        Electronic Design Automation software; from prototype to product

License:        GPLv3+
URL:            http://fritzing.org/
Source0:        https://github.com/fritzing/%{name}-app/archive/%{version}.tar.gz#/%{name}-app-%{version}.tar.gz
Source1:        https://github.com/fritzing/%{name}-parts/archive/%{version}.tar.gz#/%{name}-parts-%{version}.tar.gz
# Fedora-specific patch to disable internal auto-updating feature.
Patch0:         fritzing-disable-autoupdate.patch

# Unbundle Quazip
Patch1:         fritzing-quazip5.patch

# Fix python hashbang for parts-management scripts
Patch2:         fritzing-parts-fix-python.patch

# Remove references to example sketches that use twitter4j library
Patch3:         fritzing-remove-twitter4j.patch

BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)

# Have to manually specify zlib dependency here for now (BZ#1634468)
BuildRequires:  quazip-qt5-devel
BuildRequires:  pkgconfig(zlib)

BuildRequires:  desktop-file-utils libappstream-glib gcc-c++ boost-devel

Requires:       electronics-menu
Requires:       google-droid-sans-fonts
Requires:       google-droid-sans-mono-fonts

%description
Fritzing is a free software tool to support designers, artists and
hobbyists to work creatively with interactive electronics.

%prep
%setup -q -n %{name}-app-%{version}
# We use the unbundled version of quazip.
rm -f pri/quazip.pri
rm -rf src/lib/quazip

# The TwitterSaurus examples use (a bundled) twitter4j library, whose license
# is incompatible with Fedora.
rm -f sketches/core/Fritzing Creator Kit DE+EN/creator-kit-*/Fritzing/TwitterSaurus.fzz
rm -f sketches/core/Fritzing Creator Kit DE+EN/creator-kit-*/Processing/twitter4j-core-2.2.5.jar
rm -rf sketches/core/Fritzing Creator Kit DE+EN/creator-kit-*/Processing/TwitterSaurus*
rm -f sketches/core/obsolete/TwitterSaurus.fzz

rmdir parts
%setup -q -T -D -a 1 -n %{name}-app-%{version}
%patch0 -p1 -b .disable-updates
%patch1 -p1 -b .quazip5
%patch2 -p1 -b .parts-fix-python
%patch3 -p1 -b .remove-twitter4j
mv %{name}-parts-%{version} parts

%build
%{qmake_qt5} DEFINES=QUAZIP_INSTALLED
make %{?_smp_mflags} V=1

%install
make install INSTALL_ROOT=%{buildroot}

# A few files in /usr/share/fritzing end up executable.
find %{buildroot}%{_datadir}/%{name} -type f -exec %{__chmod} 644 {} \;
find %{buildroot}%{_datadir}/%{name} -type d -exec %{__chmod} 755 {} \;

# Icon is dumped in /usr/share/icons by default, need to move it.
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps

desktop-file-install --dir=%{buildroot}%{_datadir}/applications fritzing.desktop

mkdir -p %{buildroot}%{_datadir}/appdata
cp fritzing.appdata.xml %{buildroot}%{_datadir}/appdata

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/fritzing.appdata.xml

%files
%doc readme.md LICENSE.GPL2 LICENSE.GPL3 LICENSE.CC-BY-SA
%{_bindir}/Fritzing
%{_datadir}/appdata/fritzing.appdata.xml
%{_datadir}/applications/fritzing.desktop
%{_datadir}/pixmaps/fritzing.png
%{_datadir}/%{name}
%{_mandir}/man?/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Ed Marshall <esm@logic.net> - 0.9.2b-16
- Update Qt5 dependencies, remove unnecessary dependency on minizip.
- Add zlib-devel dependency for now.

* Tue Sep 04 2018 Pavel Raiskup <praiskup@redhat.com> - 0.9.2b-16
- rebuild against minizip-compat-devel, rhbz#1609830, rhbz#1615381

* Tue Aug 28 2018 Ed Marshall <esm@logic.net> - 0.9.2b-15
- Remove pre-built Twitter4J libraries with proprietary JSON.org license.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Ed Marshall <esm@logic.net> - 0.9.2b-13
- Add BuildRequires for gcc-c++ per packaging guidelines.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Ed Marshall <esm@logic.net> - 0.9.2b-11
- Patch script in parts library so python bytecompilation succeeds.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.2b-6
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9.2b-4
- use %%qmake_qt5 to ensure proper build flags

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.2b-3
- Rebuilt for Boost 1.60

* Sun Dec 27 2015 Ed Marshall <esm@logic.net> - 0.9.2b-2
- Modify build to use quazip-qt5 rather than quazip.
- Use upstream-provided .appdata.xml and .desktop files.

* Sat Dec  5 2015 Ed Marshall <esm@logic.net> - 0.9.2b-1
- Updated to 0.9.2b release.

* Sat Dec  5 2015 Ed Marshall <esm@logic.net> - 0.9.0b-8
- Update to .appdata.xml and .desktop files.

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.9.0b-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0b-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.9.0b-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0b-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.9.0b-2
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.8.7b-1
- Rebuild for boost 1.55.0

* Sun Feb 16 2014 Ed Marshall <esm@logic.net> - 0.8.7b-0
- Updated to 0.8.7b release.

* Sat Aug 10 2013 Ed Marshall <esm@logic.net> - 0.8.3b-0
- Updated to 0.8.3b release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.12b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.7.12b-2
- Rebuild for boost 1.54.0

* Mon Feb 25 2013 Ed Marshall <esm@logic.net> - 0.7.12b-1
- Updated to 0.7.12b release.
- Internal quazip is now configurable, boost is no longer bundled.
- Panelizer include fixes merged upstream.
- Backported missing parts.db fix no longer needed.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.11b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Ed Marshall <esm@logic.net> - 0.7.11b-2
- Backport upstream patch for gracefully handling missing parts database.

* Mon Jan  7 2013 Ed Marshall <esm@logic.net> - 0.7.11b-1
- Updated to 0.7.11b release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7.5b-1
- Updated to 0.7.5b release.
- Update patches
- Cleanup and modernise spec

* Sat Mar 10 2012 Ed Marshall <esm@logic.net> - 0.7.1b-1
- Updated to 0.7.1b release.

* Fri Feb  3 2012 Ed Marshall <esm@logic.net> - 0.7.0b-1
- Add Droid font requirement.
- Updated to 0.7.0b release.

* Wed Jan  4 2012 Ed Marshall <esm@logic.net> - 0.6.5b-2
- Make rpmlint happier with line-endings on documentation.

* Wed Jan  4 2012 Ed Marshall <esm@logic.net> - 0.6.5b-1
- Updated to 0.6.5b release.

* Tue Dec 20 2011 Ed Marshall <esm@logic.net> - 0.6.4b-2
- Add LICENSE.CC-BY-SA to package.
- Add minizip-devel as a build dependency.

* Sat Dec 17 2011 Ed Marshall <esm@logic.net> - 0.6.4b-1
- Updated to 0.6.4b release.

* Thu Feb 24 2011 Ed Marshall <esm@logic.net> - 0.5.2b-1
- Updated to 0.5.2b release.

* Thu Feb 17 2011 Ed Marshall <esm@logic.net> - 0.5.1b-3
- Add patch to remove auto-update feature.

* Tue Feb 15 2011 Ed Marshall <esm@logic.net> - 0.5.1b-2
- Fixed hard-coded path to qtlockedfile qmake project file (fixes x86_64).

* Tue Feb 15 2011 Ed Marshall <esm@logic.net> - 0.5.1b-1
- Updated to 0.5.1b release
- Don't manually strip resulting executables
- Don't bundle third-party libraries; use Fedora-provided libs
- Provide CXXFLAGS to qmake
- Updated summary to be a little closer to the Fritzing tagline

* Mon Feb 14 2011 Ed Marshall <esm@logic.net> - 0.5.0b-1
- Updated to latest release
- zlib patch included upstream, removed from RPM

* Mon Dec 6 2010 Ed Marshall <esm@logic.net> - 0.4.3b-1
- Updated to latest release
- Added desktop file, and install icon
- Include man page (from Debian)
- Patch to set application folder location to /usr/share/fritzing, instead of
  being relative to the binary directory (from Debian)

* Tue Jul 7 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.5b-1
- initial package for Fedora
