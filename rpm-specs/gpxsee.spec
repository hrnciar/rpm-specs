%global appname GPXSee

Name:           gpxsee
Version:        7.30
Release:        1%{?dist}
Summary:        GPS log file viewer and analyzer

License:        GPLv3
URL:            http://www.gpxsee.org/

Source0:        https://github.com/tumic0/%{appname}/archive/%{version}/%{appname}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Recommends:     qt5-qtpbfimageformat


%description
GPS log file viewer and analyzer with support for
GPX, TCX, KML, FIT, IGC and NMEA files.


%prep
%autosetup -n %{appname}-%{version}


%build
lrelease-qt5 %{name}.pro
%{qmake_qt5} PREFIX=/usr %{name}.pro
%make_build


%install
make install INSTALL_ROOT=%{buildroot}

# appdata
install -p -m 644 -D pkg/appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

# localization
%find_lang %{name} --with-qt


%files -f %{name}.lang
%license licence.txt
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/csv/
%{_datadir}/%{name}/maps/
%dir %{_datadir}/%{name}/translations
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml


%changelog
* Tue Jun 02 2020 Nikola Forró <nforro@redhat.com> - 7.30-1
- Update to version 7.30
  resolves: #1842047

* Mon Apr 20 2020 Nikola Forró <nforro@redhat.com> - 7.29-1
- Update to version 7.29
  resolves: #1825626

* Tue Apr 07 2020 Nikola Forró <nforro@redhat.com> - 7.28-1
- Update to version 7.28
  resolves: #1821027

* Mon Mar 30 2020 Nikola Forró <nforro@redhat.com> - 7.27-1
- Update to version 7.27
  resolves: #1818511

* Thu Mar 05 2020 Nikola Forró <nforro@redhat.com> - 7.25-1
- Update to version 7.25
  resolves: #1810297

* Mon Mar 02 2020 Nikola Forró <nforro@redhat.com> - 7.24-1
- Update to version 7.24
  resolves: #1808914

* Thu Feb 20 2020 Nikola Forró <nforro@redhat.com> - 7.23-1
- Update to version 7.23
  resolves: #1804139

* Thu Feb 13 2020 Nikola Forró <nforro@redhat.com> - 7.22-1
- Update to version 7.22
  resolves: #1802326

* Wed Feb 12 2020 Nikola Forró <nforro@redhat.com> - 7.21-1
- Update to version 7.21
  resolves: #1795072

* Tue Jan 28 2020 Nikola Forró <nforro@redhat.com> - 7.20-1
- Update to version 7.20
  resolves: #1795072

* Tue Jan 14 2020 Nikola Forró <nforro@redhat.com> - 7.19-1
- Update to version 7.19
  resolves: #1790242

* Tue Nov 19 2019 Nikola Forró <nforro@redhat.com> - 7.18-1
- Update to version 7.18
  resolves: #1773117

* Wed Nov 06 2019 Nikola Forró <nforro@redhat.com> - 7.17-1
- Update to version 7.17
  resolves: #1768080

* Tue Oct 29 2019 Nikola Forró <nforro@redhat.com> - 7.16-1
- Update to version 7.16
  resolves: #1766422

* Tue Oct 08 2019 Nikola Forró <nforro@redhat.com> - 7.15-1
- Update to version 7.15
  resolves: #1758792

* Mon Sep 30 2019 Nikola Forró <nforro@redhat.com> - 7.14-1
- Update to version 7.14
  resolves: #1756742

* Mon Sep 02 2019 Nikola Forró <nforro@redhat.com> - 7.13-1
- Update to version 7.13
  resolves: #1748008

* Mon Aug 19 2019 Nikola Forró <nforro@redhat.com> - 7.12-1
- Update to version 7.12
  resolves: #1742109

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Nikola Forró <nforro@redhat.com> - 7.10-1
- Update to version 7.10
  resolves: #1727700

* Tue Jun 18 2019 Nikola Forró <nforro@redhat.com> - 7.9-1
- Update to version 7.9
  resolves: #1720866

* Sun Jun 02 2019 Nikola Forró <nforro@redhat.com> - 7.8-1
- Update to version 7.8
  resolves: #1715247

* Thu May 23 2019 Nikola Forró <nforro@redhat.com> - 7.7-1
- Update to version 7.7
  resolves: #1711584

* Wed May 15 2019 Nikola Forró <nforro@redhat.com> - 7.6-1
- Update to version 7.6
  resolves: #1709052

* Tue Mar 19 2019 Nikola Forró <nforro@redhat.com> - 7.5-1
- Update to version 7.5
  resolves: #1689598

* Tue Mar 12 2019 Nikola Forró <nforro@redhat.com> - 7.4-1
- Update to version 7.4
  resolves: #1687195

* Tue Feb 19 2019 Nikola Forró <nforro@redhat.com> - 7.3-1
- Update to version 7.3
  resolves: #1678584

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Nikola Forró <nforro@redhat.com> - 7.2-1
- Update to version 7.2
  resolves: #1670181

* Thu Dec 20 2018 Nikola Forró <nforro@redhat.com> - 7.0-2
- Use upstream appdata.xml and fix license

* Wed Dec 19 2018 Nikola Forró <nforro@redhat.com> - 7.0-1
- Update to version 7.0

* Wed Nov 14 2018 Nikola Forró <nforro@redhat.com> - 6.3-1
- Update to version 6.3

* Tue Sep 25 2018 Nikola Forró <nforro@redhat.com> - 6.0-1
- Update to version 6.0

* Wed Aug 08 2018 Nikola Forró <nforro@redhat.com> - 5.16-1
- Update to version 5.16
  resolves: #1613850

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Nikola Forró <nforro@redhat.com> - 5.15-1
- Update to version 5.15
  resolves: #1597925

* Mon Jun 25 2018 Nikola Forró <nforro@redhat.com> - 5.14-1
- Update to version 5.14
  resolves: #1594527

* Wed May 30 2018 Nikola Forró <nforro@redhat.com> - 5.13-1
- Update to version 5.13
  resolves: #1583873

* Mon May 28 2018 Nikola Forró <nforro@redhat.com> - 5.12-1
- Update to version 5.12
  resolves: #1582680

* Wed May 16 2018 Nikola Forró <nforro@redhat.com> - 5.11-1
- Update to version 5.11
  resolves: #1578169

* Fri May 11 2018 Nikola Forró <nforro@redhat.com> - 5.10-1
- Update to version 5.10
  resolves: #1576614

* Fri Apr 20 2018 Nikola Forró <nforro@redhat.com> - 5.9-1
- Update to version 5.9
  resolves: #1569761

* Thu Apr 19 2018 Nikola Forró <nforro@redhat.com> - 5.8-1
- Update to version 5.8
  resolves: #1568190

* Tue Apr 10 2018 Nikola Forró <nforro@redhat.com> - 5.6-1
- Update to version 5.6
  resolves: #1565383

* Wed Mar 21 2018 Nikola Forró <nforro@redhat.com> - 5.5-1
- Update to version 5.5
  resolves: #1558277

* Tue Mar 13 2018 Nikola Forró <nforro@redhat.com> - 5.4-1
- Update to version 5.4
  resolves: #1554158

* Mon Mar 05 2018 Nikola Forró <nforro@redhat.com> - 5.3-1
- Update to version 5.3
  resolves: #1550750

* Tue Feb 27 2018 Nikola Forró <nforro@redhat.com> - 5.2-1
- Update to version 5.2
  resolves: #1548602

* Tue Feb 20 2018 Nikola Forró <nforro@redhat.com> - 5.1-2
- Add missing gcc-c++ build dependency

* Tue Feb 13 2018 Nikola Forró <nforro@redhat.com> - 5.1-1
- Update to version 5.1
  resolves: #1544278

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Nikola Forró <nforro@redhat.com> - 4.19-1
- Update to version 4.19
  resolves: #1531971

* Tue Dec 12 2017 Nikola Forró <nforro@redhat.com> - 4.17-1
- Update to version 4.17
  resolves: #1524743

* Fri Oct 20 2017 Nikola Forró <nforro@redhat.com> - 4.16-1
- Update to version 4.16

* Wed Oct 11 2017 Nikola Forró <nforro@redhat.com> - 4.15-2
- Do not buildrequire qt5-devel, qt5-qtbase-devel is sufficient
- Buildrequire qt5-linguist needed for lrelease-qt5

* Tue Oct 10 2017 Nikola Forró <nforro@redhat.com> - 4.15-1
- Initial package
  resolves: #1500524
