%undefine __cmake_in_source_build

%global commit ee9a1eee9dc810b33b931601203051d841bc3e7a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		qxkb
Version:	0.5.1
Release:	3%{?dist}
License:	GPLv2
Url:		https://github.com/disels/qxkb
Source0:	https://github.com/disels/qxkb/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Summary:	Qt keyboard layout switcher
BuildRequires:	cmake, desktop-file-utils
# libxkbfile-devel
BuildRequires:	pkgconfig(xkbfile)
# qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Core)
# qt5-qtsvg-devel
BuildRequires:	pkgconfig(Qt5Svg)
# qt5-qtx11extras-devel
BuildRequires:	pkgconfig(Qt5X11Extras)
# qt5-linguist
BuildRequires:	qt5-linguist
#BuildRequires:	pkgconfig(Qt5LinguistTools)

%description
The keypad switch written on Qt5.
Uses setxkbmap.
The interface repeats kxkb.
Can use svg icon for indicate language layer.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 TI_Eugene <ti.eugene@gmail.com> 0.5.1-1
- Version bump
- Switched to Qt5

* Wed Aug 21 2019 TI_Eugene <ti.eugene@gmail.com> 0.4.6-16
- Homepage and source URLs fixed

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.6-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.6-2
- cmake flags removed

* Mon Apr 01 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.6-1
- initial packaging for Fedora
