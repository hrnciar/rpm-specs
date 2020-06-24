
# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
# some tests known to fail, ping upstream
#global tests 1
%endif

Name:    kproperty
Summary: Property editing framework with editor widget
Version: 3.2.0
Release: 1%{?dist}

License: LGPLv2+
Url:     https://community.kde.org/KProperty
Source0: http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz

## upstreamable patches
# fix/sanitize pkgconfig deps
Patch100: kproperty-3.0.2-pkgconfig.patch

BuildRequires: gcc-c++

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5WidgetsAddons)

# autodeps
BuildRequires: cmake
BuildRequires: pkgconfig

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
A property editing framework with editor widget similar to what is
known from Qt Designer.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF5GuiAddons)
Requires: cmake(KF5WidgetsAddons)
%description devel
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

%find_lang_kf5 kpropertycore_qt
%find_lang_kf5 kpropertywidgets_qt
cat *_qt.lang  > all.lang


%check
## tests have known failures, TODO: consult upstream
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
#xvfb-run -a \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f all.lang
%license COPYING.LIB
%{_libdir}/libKPropertyCore3.so.4*
%{_libdir}/libKPropertyWidgets3.so.4*
# .rcc icon resources
# not sure if this is needed at runtime for sure or not, but it's relatively
# small currently, so can't hurt -- rex
%{_datadir}/kproperty3/

%files devel
%{_includedir}/KPropertyCore3/
%{_libdir}/libKPropertyCore3.so
%{_libdir}/cmake/KPropertyCore3/
%{_libdir}/pkgconfig/KPropertyCore3.pc

%{_includedir}/KPropertyWidgets3/
%{_libdir}/libKPropertyWidgets3.so
%{_libdir}/cmake/KPropertyWidgets3/
%{_libdir}/pkgconfig/KPropertyWidgets3.pc


%changelog
* Mon Feb 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.94-1
- 3.0.94

* Fri Aug 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-4
- move rcc icon resources to main/runtime pkg

* Sat Aug 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- fix pkgconfig harder

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- fix/sanitize pkgconfig deps

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> -  3.0.1-1
- first try
