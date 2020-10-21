%global _hardened_build 1
%global minorversion 1.3

Name:           xfce4-equake-plugin
Version:        1.3.8.1
Release:        12%{?dist}
Summary:        Plugin for the XFCE panel which monitors earthquakes
License:        GPLv2+
URL:            https://sourceforge.net/projects/equake/
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libcurl-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  xfce4-panel-devel
Requires:       hicolor-icon-theme
Requires:       xfce4-panel

%description
A panel plugin for the XFCE panel which monitors earthquakes and displays an
update each time a new earthquake occurs.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 1.3.8.1-8
- Rebuild (Xfce 4.13)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.8.1-6
- added gcc as BR

* Sat Feb 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.8.1-5
- Spec cleanup and modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.8.1-1
- Rebuilt for new upstream version 1.3.8.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.8-1
- Rebuilt for new upstream version 1.3.8

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.3.6-2
- Rebuild for Xfce 4.12

* Sat Feb 21 2015 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.6-1
- Rebuilt for new upstream version 1.3.6, fixes rhbz #1164472

* Sat Sep 20 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.5-1
- Rebuilt for new upstream version 1.3.5, fixes rhbz #1144400

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.4-1
- Initial RPM version 1.3.4
