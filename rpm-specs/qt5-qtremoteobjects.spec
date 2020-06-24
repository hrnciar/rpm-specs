%global qt_module qtremoteobjects

Summary: Qt5 - Qt Remote Objects
Name:    qt5-%{qt_module}
Version: 5.14.2
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel

%description
Qt Remote Objects (QtRO) is an inter-process communication (IPC) module developed for Qt.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%setup -q -n %{qt_module}-everywhere-src-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} .. \
  %{?_qt5_examplesdir:CONFIG+=qt_example_installs}

%make_build


%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}


%ldconfig_scriptlets

%files
%license LICENSE.*
%{_qt5_libdir}/libQt5RemoteObjects.so.5*
%{_qt5_bindir}/repc
## split out? -- rex
%{_qt5_qmldir}/QtQml/RemoteObjects/
%{_qt5_qmldir}/QtRemoteObjects/

%files devel
%{_qt5_headerdir}/QtRemoteObjects/
%{_qt5_headerdir}/QtRepParser/
%{_qt5_libdir}/libQt5RemoteObjects.so
%{_qt5_libdir}/libQt5RemoteObjects.prl
%{_qt5_libdir}/cmake/Qt5RemoteObjects/
%{_qt5_libdir}/cmake/Qt5RepParser
%{_qt5_libdir}/pkgconfig/Qt5RemoteObjects.pc
%{_qt5_archdatadir}/mkspecs/features/*
%{_qt5_archdatadir}/mkspecs/modules/*
%exclude %{_qt5_libdir}/libQt5RemoteObjects.la
%{_qt5_libdir}/Qt5RepParser.la
%{_qt5_libdir}/libQt5RepParser.prl
%{_qt5_libdir}/pkgconfig/Qt5RepParser.pc
%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif


%changelog
* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.14.2-1
- 5.14.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.13.2-1
- 5.13.2

* Tue Sep 24 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-1
- 5.12.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.4-1
- 5.12.4

* Tue Jun 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.3-1
- 5.12.3

* Fri Feb 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.12.1-1
- 5.12.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.3-1
- 5.11.3

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.2-1
- 5.11.2

* Sun Jul 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-3
- use %%{_qt5_archdatadir}/mkspecs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.1-1
- 5.11.1

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.11.0-1
- 5.11.0
- use %%ldconfig_scriptlets %%license %%make_build

* Sun Feb 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.1-1
- 5.10.1

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.0-2
- track private api usage

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.0-1
- 5.10.0

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.3-1
- 5.9.3

* Thu Nov 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.2-1
- 5.9.2

* Fri May 05 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.3
- Beta 3 upstream release.
