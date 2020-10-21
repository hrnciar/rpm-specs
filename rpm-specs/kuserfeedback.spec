%undefine __cmake_in_source_build
Name:    kuserfeedback
Summary: Framework for collecting user feedback for apps via telemetry and surveys
Version: 1.0.0
Release: 4%{?dist}

License: MIT
URL:     https://invent.kde.org/libraries/%{name}
Source0: https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: kf5-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Charts)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5PrintSupport)

Requires:      qt5-qtbase
Requires:      qt5-qtdeclarative
Requires:      kf5-kdeclarative

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase
Requires:       qt5-qtbase-devel
Requires:       cmake-filesystem

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        console
Summary:        Analytics and administration tool for UserFeedback servers
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    console
Analytics and administration tool for UserFeedback servers.


%prep
%autosetup -p1
mkdir %{_target_platform}


%build
%{cmake_kf5} -DENABLE_DOCS:BOOL=OFF
%cmake_build


%install
%cmake_install
%{find_lang} userfeedbackconsole5 --with-qt
%{find_lang} userfeedbackprovider5 --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/UserFeedbackConsole.desktop


%files -f userfeedbackprovider5.lang
%doc README.md
%license COPYING.LIB
%{_sysconfdir}/xdg/org_kde_UserFeedback.categories
%{_bindir}/userfeedbackctl
%{_libdir}/libKUserFeedbackCore.so.1*
%{_libdir}/libKUserFeedbackWidgets.so.1*
%dir %{_kf5_qmldir}/org/kde/userfeedback
%{_kf5_qmldir}/org/kde/userfeedback/qmldir
%{_kf5_qmldir}/org/kde/userfeedback/libKUserFeedbackQml.so


%files devel
%{_includedir}/KUserFeedback/
%{_libdir}/libKUserFeedbackCore.so
%{_libdir}/libKUserFeedbackWidgets.so
%dir %{_kf5_libdir}/cmake/KUserFeedback
%{_kf5_libdir}/cmake/KUserFeedback/KUserFeedback*.cmake
%{_kf5_archdatadir}/mkspecs/modules/qt_KUserFeedback*.pri


%files console -f userfeedbackconsole5.lang
%{_bindir}/UserFeedbackConsole
%{_datadir}/applications/UserFeedbackConsole.desktop


%changelog
* Sun Sep 20 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-4
- one more rebuild

* Sat Sep 19 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-3
- rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-1
- first spec for version 1.0.0

