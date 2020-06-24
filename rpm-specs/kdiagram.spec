
# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kdiagram
Summary: Powerful libraries (KChart, KGantt) for creating business diagrams
Version: 2.7.0
Release: 1%{?dist}

License: GPLv2+

Url:     https://api.kde.org/extragear-api/graphics-apidocs/kdiagram/html/
Source0: http://download.kde.org/stable/kdiagram/%{version}/kdiagram-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

# For AutoReq cmake-filesystem
BuildRequires: cmake

%description
Powerful libraries (KChart, KGantt) for creating business diagrams.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Svg)
Requires: cmake(Qt5Widgets)
Requires: cmake(Qt5PrintSupport)
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

%find_lang_kf5 kchart_qt
%find_lang_kf5 kgantt_qt
cat kchart_qt.lang kgantt_qt.lang > %{name}.lang


%check
## tests have known failures, TODO: consult upstream
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
make test ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSE.GPL.txt
%{_kf5_libdir}/libKChart.so.2*
%{_kf5_libdir}/libKGantt.so.2*

%files devel
%{_includedir}/KChart/
%{_includedir}/KGantt/
%{_includedir}/kchart_version.h
%{_includedir}/kgantt_version.h
%{_kf5_libdir}/libKChart.so
%{_kf5_libdir}/libKGantt.so
%{_kf5_libdir}/cmake/KChart/
%{_kf5_libdir}/cmake/KGantt/
%{_kf5_archdatadir}/mkspecs/modules/qt_KChart.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGantt.pri


%changelog
* Tue Apr 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.7.0-1
- 2.7.0

* Mon Apr 13 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.6.3-1
- 2.6.3

* Sun Mar 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.6.2-1
- 2.6.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.6.1-1
- 2.6.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 2.6.0-7
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 2.6.0-4
- Add -devel dependencies

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.6.0-2
- add library scriptlets, reduce test time to 20 sec

* Sat Dec 31 2016 Rex Dieter <rdieter@math.unl.edu> - 2.6.0-1
- kdiagram-2.6.0

