
# koffice version to Obsolete
%global koffice_ver 3:2.3.70

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
# some known failures, ping upstream
%global tests 1
%endif

Name:    kexi
Summary: An integrated environment for managing data
Version: 3.1.0
Release: 7%{?dist}

License: GPLv2+

Url:     http://community.kde.org/Kexi

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%global majmin 3.1
%else
%global stable stable
%global majmin %(echo %{version} | cut -d. -f1,2)
%endif
Source0: http://download.kde.org/%{stable}/%{name}/src/%{name}-%{version}.tar.xz

## upstream patches (lookaside cache)
Patch5: 0005-Fix-build-with-Qt-5.11-missing-headers.patch
Patch6: kexi-3.1.0-FTBFS-QDate.patch

BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)

BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5WebKitWidgets)

BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: breeze-icon-theme-rcc
# needed at runtime too, apparently -- rex
Requires: breeze-icon-theme-rcc

# kdb/kproperty/kreport and kexi are all tied together
BuildRequires: cmake(KDb) >= %{version}
BuildRequires: cmake(KPropertyWidgets) >= %{version}
BuildRequires: cmake(KReport) >= %{version}

Requires: kdb%{?_isa} >= %{version}
Requires: kproperty%{?_isa} >= %{version}
Requires: kreport%{?_isa} >= %{version}

BuildRequires: cmake(Marble)

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes: koffice-kexi < %{koffice_ver}
Obsoletes: koffice-kexi-libs < %{koffice_ver}

Obsoletes: calligra-kexi < 3.0.0
Provides:  calligra-kexi = %{version}-%{release}

Obsoletes: calligra-kexi-map-form-widget < 3.0.0
#Provides:  calligra-kexi-map-form-widget = %{version}-%{release}

%description
Kexi is an integrated data management application.  It can be used for
creating database schemas, inserting data, performing queries, and
processing data. Forms can be created to provide a custom interface to
your data. All database objects – tables, queries and forms – are
stored in the database, making it easy to share data and design.

For additional database drivers take a look at kexi-driver-*

%package  libs
Summary:  Runtime libraries for %{name}
Obsoletes: calligra-kexi-libs < 3.0.0
Provides:  calligra-kexi-libs = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package spreadsheet-import
Summary: Spreadsheet-to-Kexi-table import plugin
Obsoletes: calligra-kexi-spreadsheet-import < 3.0.0
Provides:  calligra-kexi-spreadsheet-import = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description spreadsheet-import
%{summary}.


%prep
%autosetup -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF}
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name --with-html

## versioning silliness
# compat symlink
ln -s kexi-%{majmin} %{buildroot}%{_kf5_bindir}/kexi
# rename appdata/.desktop
mv %{buildroot}%{_kf5_metainfodir}/org.kde.kexi-%{majmin}.appdata.xml \
   %{buildroot}%{_kf5_metainfodir}/org.kde.kexi.appdata.xml
mv %{buildroot}%{_kf5_datadir}/applications/org.kde.kexi-%{majmin}.desktop \
   %{buildroot}%{_kf5_datadir}/applications/org.kde.kexi.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.kexi.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.kexi.desktop
## tests have known failures, TODO: consult upstream
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
#xvfb-run -a \
%make_build ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%files -f %{name}.lang
%license COPYING*
%{_kf5_bindir}/kexi
%{_kf5_bindir}/kexi-%{majmin}
%{_kf5_metainfodir}/org.kde.kexi.appdata.xml
%{_kf5_datadir}/applications/org.kde.kexi.desktop
%{_kf5_datadir}/kexi/

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libkexi*
%{_kf5_libdir}/libkformdesigner*
%{_qt5_plugindir}/kexi/


%changelog
* Mon Feb 17 2020 Than Ngo <than@redhat.com> - 3.1.0-7
- Fixed FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-3
- upstream buildfix (#1604485)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.94-1
- 3.0.94
- undo some of the versioning/parallel-install silliness

* Fri Oct 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- Requires: breeze-icon-theme-rcc (#1492881)

* Fri Aug 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- typo in kreport dependency

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2, bump kdb dep

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1.1-1
- 3.0.1.1 (fix translations)

* Wed Jun 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-2
- License: GPLv2+
- BR: breeze-icon-theme-rcc
- appdata/desktop file validation

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-1
- first try
