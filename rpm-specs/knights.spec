Name:		knights
Version:	20.04.2
Release:	1%{?dist}
Summary:	A chess board for KDE

# KDE e.V. may determine that future GPL versions are accepted
License: GPLv2 or GPLv3
URL:		https://github.com/KDE/knights/
Source0:	https://github.com/KDE/knights/archive/v%{version}/knights-%{version}.tar.gz
Patch0:		knights-desktop-exec-key.patch   
BuildRequires:	libkdegames-devel
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kplotting-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  qt5-qtsvg-devel

Requires:	gnuchess

%description
Knights is a chess board for KDE that supports playing against
computer engines that support the XBoard protocol like GNUChess and also
multiplayer games over the internet on FICS. It features automatic rule
checking, themes, and nice animations


%prep
%setup -q

%patch0 -p0

%build
mkdir build
pushd build
%cmake_kf5 ..
popd

make %{?_smp_mflags} -C build


%install
make install/fast DESTDIR=%{buildroot} -C build

desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.knights.desktop

%files
%doc README* ChangeLog DESIGN doc/
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/org.kde.Knights.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf5_datadir}/applications/org.kde.knights.desktop
%{_sysconfdir}/xdg/%{name}*
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/kxmlgui5/knights/knightsui.rc
%{_datadir}/metainfo/org.kde.knights.appdata.xml
%exclude %{_datadir}/doc/HTML/
%{_datadir}/qlogging-categories5/knights.categories

%changelog
* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.04.2-1
- 20.04.2

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.04.1-1
- 20.04.1

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.04.0-1
- 20.04.0

* Fri Apr 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.03.90-1
- 20.03.90

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.03.80-1
- 20.03.80

* Thu Mar 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 19.12.3-1
- 19.12.3

* Fri Feb 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 19.12.1-1
- 19.12.1

* Thu Dec 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.12.0-1
- 19.12.0

* Mon Dec 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.11.90-1
- 19.11.90

* Mon Nov 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.11.80-1
- 19.11.80

* Thu Nov 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.08.3-1
- 19.08.3

* Fri Oct 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.08.2-1
- 19.08.2

* Thu Sep 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.08.1-1
- 19.08.1

* Fri Aug 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.08.0-1
- 19.08.0

* Fri Aug 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.07.90-1
- 19.07.90

* Wed Jul 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.07.80-1
- 19.07.80

* Thu Jul 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.04.3-1
- 19.04.3

* Thu Jun 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.04.2-1
- 19.04.2

* Thu May 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.04.1-1
- 19.04.1

* Thu Apr 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.04.0-1
- 19.04.0

* Fri Apr 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.03.90-1
- 19.03.90

* Fri Mar 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.03.80-1
- 19.03.80

* Thu Mar 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 18.12.3-1
- 18.12.3

* Fri Feb 08 2019 Gwyn Ciesla <limburgher@gmail.com> - 18.12.2-1
- 18.12.2

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 18.12.1-1
- 18.12.1

* Mon Nov 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.11.80-1
- 18.11.80

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.0-13
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Jon Ciesla <limburgher@gmail.com> - 2.5.0-7
- libkdegames rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 03 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-2
- do safer out-of-src-tree build
- add minimal/versioned kdelibs4 dep
- drop .desktop permissions hack (rpmlint be darned, it's legit)
- use %%find_lang --with-kde
- use %%_kde4_iconsdir consistently

* Thu Aug 30 2012 Julian Aloofi <julian@fedoraproject.org> 2.5.0-1
- update to latest upstream release
- remove the patch for building against the new KDEgames API

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Julian Aloofi <julian@fedoraproject.org> 2.4.2-2
- apply patch to build against the new KDEgames API
- removed the buildroot tag

* Mon Apr 30 2012 Julian Aloofi <julian@fedoraproject.org> 2.4.2-1
- update to latest upstream release

* Sat Nov 12 2011 Julian Aloofi <julian@fedoraproject.org> 2.4.0-1
- update to latest upstream release

* Mon Jun 13 2011 Julian Aloofi <julian@fedoraproject.org> 2.3.2-1
- update to latest upstream release

* Mon Mar 21 2011 Julian Aloofi <julian@fedoraproject.org> 2.3.1-1
- update to latest upstream release

* Fri Mar 11 2011 Julian Aloofi <julian@fedoraproject.org> 2.3.0-1
- update to latest upstream release

* Sun Feb 13 2011 Julian Aloofi <julian@fedoraproject.org> 2.2.0-4
- fix permissions of the desktop file

* Mon Feb 07 2011 Julian Aloofi <julian@fedoraproject.org> 2.2.0-3
- clarification on the license tag

* Mon Feb 07 2011 Julian Aloofi <julian@fedoraproject.org> 2.2.0-2
- using macros in Source0
- build with the proper make flags

* Mon Jan 31 2011 Julian Aloofi <julian@fedoraproject.org> 2.2.0-1
- initial package
