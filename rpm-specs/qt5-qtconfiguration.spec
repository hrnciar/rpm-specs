
%global qt_module qtconfiguration

%undefine __cmake_in_source_build

Summary:        Qt5 - QtConfiguration module
Name:           qt5-%{qt_module}
Version:        0.3.1
Release:        13%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License:        LGPLv2 with exceptions or GPLv3 with exceptions
URL:            https://github.com/mauios/qtconfiguration
Source0:        http://downloads.sourceforge.net/project/mauios/hawaii/%{qt_module}/%{qt_module}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  cmake

%description
Settings API with change notifications.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}

%description devel
%{summary}.


%prep
%setup -q -n %{qt_module}-%{version}


%build
%cmake

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%{_libdir}/libqtconfiguration.so.0*
%{_libdir}/hawaii
%license LICENSE.FDL
%license LICENSE.GPL
%license LICENSE.LGPL
%doc README.md

%files devel
%{_includedir}/QtConfiguration/
%{_libdir}/libqtconfiguration.so
%{_libdir}/cmake/QtConfiguration/


%changelog
* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-14
- FTBFS, use new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-9
- drop hard-coded qt5-qbase runtime dep
- use %%license, %%make_build macros

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.3.1-1
* Update to latest version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.3.0-1
- Update to latest version

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 17 2013 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.2.1-1
- Upstream switched from qmake to cmake
- Update to latest version

* Tue Sep 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-3
- Get rid of extra library links (Christopher Meng, #1011501)
- Drop irrelevant license file (Christopher Meng, #1011501)

* Tue Sep 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-2
- Incorporate some review fixes (Christopher Meng, #1011501)

* Thu Sep 12 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.0-1
- Initial packaging
