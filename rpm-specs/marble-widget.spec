
Name:    marble-widget
Summary: Marble Widget Library for Qt4 
Epoch:   1
Version: 15.08.3
Release: 62%{?dist}

License: LGPLv2+
URL:     http://marble.kde.org/
Source0: http://download.kde.org/stable/applications/%{version}/src/marble-%{version}.tar.xz

## upstreamable patches
Patch50: marble-15.08.3-BUILD_MARBLE_PLUGINS.patch
Patch51: marble-15.08.0-qt4.patch
Patch52: marble-15.08.3-astro.patch

## upstream patches

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: kde-filesystem
BuildRequires: pkgconfig(phonon)
BuildRequires: pkgconfig(QtGui)
# may be optional -- rex
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: marble-astro-devel

Obsoletes: kdeedu-marble-libs < 4.7.0-10
Provides:  kdeedu-marble-libs = %{version}-%{release}
Obsoletes: marble-libs < 1:15.08.0
Provides:  marble-libs = %{epoch}:%{version}-%{release}
Provides:  marble-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides:  marble-part = %{version}-%{release}
Provides:  marble-part%{?_isa} = %{version}-%{release}

Requires:  marble-widget-data
Requires:  kde-filesystem

%description
%{summary}.

%package devel
Summary: Development files for Marble Widget
# headers currently install to same location.
# TODO: explore possibility of moving them to not conflict
Conflicts: marble-widget-qt5-devel
# # when split occurred (long ago)
Conflicts: kdeedu-devel < 4.7.0-10
Obsoletes: marble-devel < 1:15.08.0
Provides:  marble-devel = %{epoch}:%{version}-%{release}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n marble-%{version}

%patch50 -p1 -b .BUILD_MARBLE_PLUGINS
%patch51 -p1 -b .qt4
%patch52 -p1 -b .astro


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. \
  -DBUILD_MARBLE_APPS:BOOL=OFF \
  -DBUILD_MARBLE_PLUGINS:BOOL=OFF \
  -DBUILD_MARBLE_TESTS:BOOL=OFF \
  -DBUILD_TESTING:BOOL=OFF \
  -DCMAKE_MODULES_INSTALL_PATH:PATH="%{_kde4_appsdir}/cmake/modules" \
  -DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
  -DMARBLE_PLUGIN_PATH:PATH="%{_libdir}/kde4/plugins/marble" \
  -DQT5BUILD=OFF \
  -DWITH_DESIGNER_PLUGIN:BOOL=OFF

make %{?_smp_mflags}
popd


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/src/lib/marble

# install FindMarble.cmake by hand
install -m644 -p -D \
  %{_target_platform}/FindMarble.cmake \
  %{buildroot}%{_kde4_appsdir}/cmake/modules/FindMarble.cmake


%ldconfig_scriptlets

%files
%license LICENSE.txt
%{_kde4_libdir}/libmarblewidget.so.22
%{_kde4_libdir}/libmarblewidget.so.0.21.*

%files devel
%{_kde4_appsdir}/cmake/modules/FindMarble.cmake
%{_includedir}/marble/
%{_kde4_libdir}/libmarblewidget.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:15.08.3-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.08.3-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Rex Dieter <rdieter@fedoraproject.org> 1:15.08.3-52
- Requires: kde-filesystem

* Sun Jan 10 2016 Rex Dieter <rdieter@fedoraproject.org> 1:15.08.3-51
- %%license LICENSE.txt
- remove reference to unused marble-data subpkg
- -devel: Conflicts: marble-widget-qt5-devel
- update URL, simplify Source0 URL

* Wed Dec 23 2015 Rex Dieter <rdieter@fedoraproject.org> 1:15.08.3-50
- first try as standalone marble-widget
