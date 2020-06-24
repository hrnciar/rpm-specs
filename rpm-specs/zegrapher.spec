%global altname ZeGrapher

Name:           zegrapher
Summary:        Free and opensource math graphing software
Version:        3.1
Release:        2%{?dist}
License:        GPLv3+

URL:            https://www.zegrapher.com/
Source0:        https://github.com/AdelKS/%{altname}/archive/v%{version}/%{altname}-%{version}.tar.gz

# https://github.com/AdelKS/ZeGrapher/issues/14
Patch0:         0001-Fix-issues-with-appdata-file.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
ZeGrapher is a plotting program for functions, sequences, parametric equations,
and tabular data. It has been designed to be as easy to use as possible.

ZeGrapher supports importing and exporting of tabular data from and to CSV files
and polynomial (regression) fits, plotting of tangents (the point can be
selected interactively). Calculation and plotting of derivatives and integrals
is also possible.

Plots can be exported in various image formats and as PDF files.

%prep
%autosetup -p1 -n %{altname}-%{version}
sed -i 's|^QMAKE_LFLAGS_RELEASE = -s|QMAKE_LFLAGS_RELEASE =|' ZeGrapher.pro

# https://github.com/AdelKS/ZeGrapher/pull/15
find . -type f -executable -exec chmod 0644 "{}" +;

%build
mkdir build && cd build
%qmake_qt5 ../ PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot} -C build

%find_lang %{altname} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{altname}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{altname}.appdata.xml

%files -f %{altname}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{altname}
%{_datadir}/appdata/%{altname}.appdata.xml
%{_datadir}/applications/%{altname}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{altname}.png
%dir %{_datadir}/%{altname}

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 20:40:10 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 3.1-1
- Update to 3.1 (#1787890)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.2-4
- Add missing BR for gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.2-2
- Remove obsolete scriptlets

* Wed Oct 11 2017 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.2-1
- Upstream release 3.0.2

* Tue Sep 26 2017 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-2
- Added patches to fix permissions, fix desktop file, add appdata and add install method

* Mon Sep 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.1-1
- Initial package.


