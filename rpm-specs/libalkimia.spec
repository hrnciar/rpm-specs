
# uncomment to enable bootstrap mode
#global bootstrap 1

%if ! 0%{?bootstrap}
%global docs 1
%global tests 1
%endif

%if 0%{?fedora} && 0%{?fedora} < 31
%global qt4 1
%endif
#global plasma 1

Name:    libalkimia
Summary: Financial library
Version: 8.0.3
Release: 1%{?dist}

License: LGPLv2+
URL:     https://kmymoney.org/
Source0: http://download.kde.org/stable/alkimia/%{version}/alkimia-%{version}.tar.xz

## upstream patches

## upstreamable patches
# allow use of gmp even if mpir is present
Patch101: alkimia-7.0.1-use_gmp.patch
# FTBFS when qt4 is not enabled
Patch102: alkimia-8.0.3-appdata_install_dir.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config
# KF5
BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5Plasma)
# Qt5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5WebKitWidgets)

# Qt4
%if 0%{?qt4}
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtDBus)
BuildRequires: pkgconfig(QtDeclarative)
BuildRequires: pkgconfig(QtTest)
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: kdelibs4-devel
# keep qt4 build unconditionally using gmp
BuildRequires: gmp-devel
%endif

# %%check
%if 0%{?tests}
BuildRequires: dbus-x11 xorg-x11-server-Xvfb
%endif

# qt5 build conditional
%ifarch ppc64le
# mpir not built on ppc64le... yet, only gmp available
BuildRequires: gmp-devel
%global gmp gmp
%else
BuildRequires: mpir-devel
%global gmp mpir
%endif

%if 0%{?docs}
BuildRequires: doxygen
%endif

%description
%{summary}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gmp-devel
%description devel
%{summary}.

%package        qt5
Summary:        Accounts framework Qt5 bindings
%description    qt5
%{summary}.

%package        qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       %{gmp}-devel
%description    qt5-devel
%{summary}.

%package        doc
Summary:        API Documentation for %{name}
BuildArch:      noarch
%description    doc
%{summary}.


%prep
%autosetup -n alkimia-%{version} -p1


%build
## Qt5
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{cmake} .. \
  %{!?plasma:-DBUILD_APPLETS:BOOL=OFF} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
popd

%make_build -C %{_target_platform}-qt5

## docs
%if 0%{?docs}
# auto-update doxygen configuration
doxygen -u %{_target_platform}-qt5/src/libalkimia.doxygen
make libalkimia_apidoc -C %{_target_platform}-qt5
%endif

## Qt4
%if 0%{?qt4}
mkdir %{_target_platform}-qt4
pushd %{_target_platform}-qt4
%{cmake} .. \
  -DBUILD_APPLETS:BOOL=OFF \
  -DBUILD_QT4:BOOL=1 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DUSE_GMP:BOOL=1
popd

%make_build -C %{_target_platform}-qt4
%endif


%install
%if 0%{?qt4}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt4
%endif
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5

%if 0%{?docs}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a %{_target_platform}-qt5/src/apidocs/html/ %{buildroot}%{_pkgdocdir}/
%endif

## unpackaged files
%if ! 0%{?plasma}
rm -fv  %{buildroot}%{_kf5_datadir}/locale/*/LC_MESSAGES/plasma*
%endif

#find_lang onlinequoteseditor
#find_lang alkimia
%find_lang %{name} --all-name


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libalkimia5)" = "%{version}"
%if 0%{?qt4}
test "$(pkg-config --modversion libalkimia)" = "%{version}"
%endif
%if 0%{?tests}
%if 0%{?qt4}
time \
xvfb-run -a dbus-launch --exit-with-session \
make test ARGS="-E alkonlinequotestest --output-on-failure --timeout 20" -C %{_target_platform}-qt4 ||:
%endif
time \
xvfb-run -a dbus-launch --exit-with-session \
make test ARGS="-E alkonlinequotestest --output-on-failure --timeout 20" -C %{_target_platform}-qt5 ||:
%endif


%if 0%{?qt4}
%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license COPYING*
%{_libdir}/libalkimia.so.8*
%{_kde4_datadir}/alkimia/

%{_qt4_plugindir}/imports/org/kde/alkimia/

%{_kde4_bindir}/onlinequoteseditor
%{_kde4_datadir}/applications/org.kde.onlinequoteseditor.desktop
%{_kde4_datadir}/kde4/config/*-quotes.knsrc
%{_kde4_iconsdir}/*/*/apps/onlinequoteseditor.*

%files devel
%{_libdir}/libalkimia.so
%{_includedir}/alkimia/Qt4/
%{_libdir}/cmake/LibAlkimia-8.0/
%{_libdir}/pkgconfig/libalkimia.pc
%endif

%ldconfig_scriptlets qt5

%files qt5 -f %{name}.lang
%doc README.md
%license COPYING*
%{_libdir}/libalkimia5.so.8*
%{_kf5_datadir}/alkimia5/

%{_kf5_qmldir}/org/kde/alkimia/

%{_kf5_bindir}/onlinequoteseditor5
%{_kf5_datadir}/applications/org.kde.onlinequoteseditor5.desktop
%{_kf5_datadir}/icons/*/*/apps/onlinequoteseditor5.*
%{_kf5_sysconfdir}/xdg/*-quotes.knsrc

%files qt5-devel
%dir %{_includedir}/alkimia/
%{_includedir}/alkimia/Qt5/
%{_libdir}/libalkimia5.so
%{_libdir}/pkgconfig/libalkimia5.pc
%{_libdir}/cmake/LibAlkimia5-8.0/

%if 0%{?docs}
%files doc
%dir %{_pkgdocdir}/
%doc %{_pkgdocdir}/html
%endif


%changelog
* Mon May 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 8.0.3-1
- 8.0.3

* Mon May 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 8.0.2-3
- -doc: drop dep on main pkg (#1833984)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Rex Dieter <rdieter@fedoraproject.org> - 8.0.2-1
- 8.0.2
- drop qt4 support f31+

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 7.0.2-1
- 7.0.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 7.0.1-4
- pull in upstream(ed) patches

* Thu Mar 29 2018 Rex Dieter <rdieter@fedoraproject.org> - 7.0.1-3
- -qt4: make kde4 kmymoney buildable again
- -qt4: use gmp unconditionally (as previous alkimia v5 used gmp)

* Mon Mar 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 7.0.1-2
- -devel: Requires: (gmp,mpir)-devel

* Sun Mar 18 2018 Rex Dieter <rdieter@fedoraproject.org> -  7.0.1-1
- 7.0.1
- -qt5 support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0.0-1
- libalkimia-5.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.3.2-7
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.3.2-1
- 4.3.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 02 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.1-4
- rebuild (gmp)

* Mon Aug 22 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.1-3
- .spec cosmetics

* Sat Aug 20 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.1-2
- BR: gmp-devel
- %%check : don't ignore errors

* Sat Aug 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.1-1
- 4.3.1

* Tue Jun 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.3.0-1
- first try


