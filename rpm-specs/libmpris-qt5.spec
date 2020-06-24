%global repo qtmpris

Name:           libmpris-qt5
Summary:        Qt and QML MPRIS interface and adaptor
Version:        1.0.0
Release:        2%{?dist}
License:        LGPLv2+
URL:            https://git.merproject.org/mer-core/%{repo}
Source0:        https://git.merproject.org/mer-core/%{repo}/-/archive/%{version}/%{repo}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(dbusextended-qt5)

%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_libdir}/lib*.so.1*

%files devel
%dir %{_qt5_includedir}/MprisQt/
%{_qt5_includedir}/MprisQt/Mpris
%{_qt5_includedir}/MprisQt/MprisQt
%{_qt5_includedir}/MprisQt/MprisPlayer
%{_qt5_includedir}/MprisQt/MprisController
%{_qt5_includedir}/MprisQt/MprisManager
%{_qt5_includedir}/MprisQt/mpris.h
%{_qt5_includedir}/MprisQt/mprisqt.h
%{_qt5_includedir}/MprisQt/mprisplayer.h
%{_qt5_includedir}/MprisQt/mpriscontroller.h
%{_qt5_includedir}/MprisQt/mprismanager.h
%dir %{_qt5_qmldir}/org/nemomobile/
%dir %{_qt5_qmldir}/org/nemomobile/mpris/
%{_qt5_qmldir}/org/nemomobile/mpris/%{name}-qml-plugin.so
%{_qt5_qmldir}/org/nemomobile/mpris/plugins.qmltypes
%{_qt5_qmldir}/org/nemomobile/mpris/qmldir
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.0.0-1
- Release 1.0.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 mosquito <sensor.wen@gmail.com> - 0.1.0-1
- Initial package build
