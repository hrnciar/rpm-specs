%global framework kirigami

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 1.1.0
Release: 13%{?dist}
Summary: QtQuick plugins to build user interfaces based on the KDE UX guidelines

License: LGPLv2+
#URL:    https://quickgit.kde.org/?p=%{framework}.git
URL:     https://techbase.kde.org/Kirigami
Source0: http://download.kde.org/stable/kirigami/%{framework}-%{version}.tar.xz

# filter qml provides
%global __provides_exclude_from ^%{_kf5_qmldir}/.*\\.so$

BuildRequires: extra-cmake-modules
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-rpm-macros
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtsvg-devel

# upgrade path from OBS packages
Obsoletes: kirigami < 1.1.0
Provides:  kirigami = %{version}-%{release}

%if 0%{?tests}
%if 0%{?fedora}
BuildRequires: appstream
%endif
%endif

Requires:      kf5-filesystem >= %{version}
Requires:      qt5-qtquickcontrols%{?_isa}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
# upgrade path from OBS packages
Obsoletes:      kirigami-devel < 1.1.0
Provides:       kirigami-devel = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} .. \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang_kf5 libkirigamiplugin_qt


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f libkirigamiplugin_qt.lang
# README is currently only build instructions, omit for now
#doc README.md
%license LICENSE*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kirigami/

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_Kirigami.pri
%{_kf5_libdir}/cmake/KF5Kirigami/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-9
- use %%make_build %%ldconfig_scriptlets
- use %%find_lang_kf5, fixes FTBFS (#1582897)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Rex Dieter <rdieter@math.unl.edu> - 1.1.0-4
- filter qml provides

* Wed Sep 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-3
- Obsoletes/Provides: kirigami(-devel)

* Tue Sep 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-2
- drop cmake() style deps (not universally available in rhel)

* Tue Sep 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Fri Sep 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.2-2
- refresh spec/srpm for review

* Thu Sep 22 2016 Rex Dieter <rdieter@fedoraproject.org> -  1.0.2-1
- first try

