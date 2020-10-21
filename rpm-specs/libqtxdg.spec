Name:           libqtxdg
Summary:        QtXdg, a Qt5 implementation of XDG standards
Version:        3.5.0
Release:        5%{?dist}
License:        LGPLv2+
URL:            http://lxqt.org
Source0:        https://github.com/lxqt/libqtxdg/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  file-devel
BuildRequires:  lxqt-build-tools
Requires:       xdg-user-dirs
Requires:       xdg-utils
Obsoletes:      libqtxdg-qt5 <= 1.1.0

%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif

%description
%{summary}.

%package devel
Summary:        Qt - development files for qtxdg
Obsoletes:      libqtxdg-qt5-devel <= 1.1.0
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files used for developing and building software that uses qtxdg.


%prep
%setup -q

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif

%cmake3 -DPULL_TRANSLATIONS=NO

%cmake_build

%if 0%{?el7}
EOF
%endif
%install
%cmake_install

%ldconfig_scriptlets

%files
%doc AUTHORS
%license COPYING
%{_libdir}/libQt5Xdg.so.3*
%{_libdir}/libQt5XdgIconLoader.so.3*
%{_bindir}/qtxdg-mat

%files devel
%{_libdir}/libQt5Xdg.so
%{_libdir}/libQt5XdgIconLoader.so
%{_libdir}/pkgconfig/Qt5Xdg.pc
%{_libdir}/pkgconfig/Qt5XdgIconLoader.pc
%{_includedir}/qt5xdg/
%{_includedir}/qt5xdgiconloader/
%{_datadir}/cmake/qt5xdg/
%{_datadir}/cmake/qt5xdgiconloader/
%{_qt5_archdatadir}/plugins/iconengines/libQt5XdgIconPlugin.so

%changelog
* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 3.5.0-5
- rebuild (qt5)

* Tue Aug 11 2020 Zamir SUN <sztsian@gmail.com> - 3.5.0-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Zamir SUN <sztsian@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.3.1-9
- rebuild (qt5)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.1-7
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.1-6
- rebuild (qt5)

* Fri Sep 20 2019 Zamir SUN <sztsian@gmail.com> - 3.3.1-5
- Modify to improve compatibility with epel7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.1-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 3.3.1-2
- rebuild (qt5)

* Mon Apr 15 2019 Zamir SUN <zsun@fedoraproject.org>  - 3.3.1-1
- Update to 3.3.1

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.3.0-2
- rebuild (Qt5)

* Tue Feb 12 2019 Zamir SUN <zsun@fedoraproject.org>  - 3.3.0-1
- Prepare for LXQt 0.14.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-3
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 3.2.0-2
- rebuild (qt5)

* Fri Aug 03 2018 Zamir SUN <zsun@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-14
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-13
- rebuild (qt5)

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-12
- .spec cleanup, BR: gcc-c++, use %%license %%make_build

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 2.0.0-11
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 2.0.0-9
- rebuild (qt5)

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-8
- rebuild (qt5)

* Thu Oct 19 2017 Christian Dersch <lupinix@mailbox.org> - 2.0.0-7
- rebuilt

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-6
- BR: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 2.0.0-2
- Add proper dependencies to xdg-utils and xdg-user-dirs

* Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - * Sun Sep 25 2016 Helio Chissini de Castro <helio@kde.org> - 2.0.0-1
- New upstream release tied to lxqt 0.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Helio Chissini de Castro <helio@kde.org> - 1.3.0-2
- Prepare to use new cmake3 package from epel

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 1.3.0-1
- New upstream release
- No more Qt4 releases

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Helio Chissini de Castro <helio@kde.org> - 1.2.0-1
- New upstream version

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 1.1.0-4
- Rebuild (gcc5)

* Thu Feb 12 2015 Helio Chissini de Castro <helio@kde.org> - 1.1.0-3
- Restore Qt4 due to maintenance of RazorQt

* Wed Feb 11 2015 Helio Chissini de Castro <helio@kde.org> - 1.1.0-2
- Upstream patch for qiconfix

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 1.1.0-1
- New upstream version 1.1.0
- Only Qt5 now

* Thu Oct 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-1
- libqtxdg-1.0.0, soname bump (#1147204)

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.5.3-4
- Provide qt4 support (#1147204)
- rename libqtxdg-qt4 -> libqtxdg, libqtxdg-qt4-devel -> libqtxdg to ease/simplify upgrade path
- use %%find_lang for translations
- -devel: drop cmake dep

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.5.3-1
- Update to a later upstream release

* Tue Dec 03 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.5.0-1
- Initial packaging
