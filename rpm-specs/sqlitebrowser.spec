Name:           sqlitebrowser
Version:        3.12.0
Release:        1%{?dist}
Summary:        Create, design, and edit SQLite database files

License:        GPLv3+ or MPLv2.0
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Unbundle bundled libraries
Patch0:         sqlitebrowser_unbundle.patch

BuildRequires:  antlr-C++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qcustomplot-qt5-devel
BuildRequires:  qhexedit2-qt5-devel
BuildRequires:  sqlite-devel
BuildRequires:  qscintilla-qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       hicolor-icon-theme

%description
SQLite Database Browser is a high quality, visual, open source tool to create,
design, and edit database files compatible with SQLite.


%prep
%autosetup -p1

# Unbundle
rm -rf libs/{qcustomplot-source,qhexedit,qscintilla}


%build
%cmake \
    -DUSE_QT5=1 \
    -DENABLE_TESTING=1 \
    -DFORCE_INTERNAL_QCUSTOMPLOT=OFF \
    -DFORCE_INTERNAL_QHEXEDIT=OFF \
    -DQT_INCLUDE_DIR=%{_includedir}/qt5 .
%make_build


%install
%make_install
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.desktop.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%check
%make_build test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.desktop.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png


%changelog
* Tue Jun 16 2020 Sandro Mani <manisandro@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Sandro Mani <manisandro@gmail.com> - 3.11.2-1
- Update to 3.11.2

* Tue Feb 19 2019 Sandro Mani <manisandro@gmail.com> - 3.11.1-1
- Update to 3.11.1

* Sun Feb 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.11.0-3
- rebuild (qscintilla)

* Tue Feb 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 3.11.0-2
- rebuild (qscintilla)

* Mon Feb 11 2019 Sandro Mani <manisandro@gmail.com> - 3.11.0-1
- Update to 3.11.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Sandro Mani <manisandro@gmail.com> - 3.10.1-5
- Backport fix for sqlitebrowser window getting restored as soon as minimized (#1561976)

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 3.10.1-4
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.10.1-2
- Remove obsolete scriptlets

* Thu Sep 21 2017 Sandro Mani <manisandro@gmail.com> - 3.10.1-1
- Update to 3.10.1

* Sun Aug 20 2017 Sandro Mani <manisandro@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.9.1-5
- rebuild (qscintilla), drop (qt4) BR: qscintilla-devel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Sandro Mani <manisandro@gmail.com> - 3.9.1-3
- Rebuild (qhexedit2)

* Wed Nov 09 2016 Sandro Mani <manisandro@gmail.com> - 3.9.1-2
- Rebuild (qhexedit2)

* Mon Oct 03 2016 Sandro Mani <manisandro@gmail.com> - 3.9.1-1
- Update to 3.9.1

* Mon Sep 05 2016 Sandro Mani <manisandro@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 27 2015 Sandro Mani <manisandro@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Nov 17 2015 Sandro Mani <manisandro@gmail.com> - 3.7.0-3
- Fix stack overflow due to signal infinite loop (#1282792)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Sandro Mani <manisandro@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Wed May 20 2015 Sandro Mani <manisandro@gmail.com> - 3.6.0-2
- Rebuild (qhexedit2)

* Thu Apr 30 2015 Sandro Mani <manisandro@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Mon Feb 09 2015 Sandro Mani <manisandro@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Mon Feb 02 2015 Sandro Mani <manisandro@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Sun Dec 28 2014 Sandro Mani <manisandro@gmail.com> - 3.4.0-2
- Rebuild (qcustomplot)

* Fri Oct 31 2014 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Sun Aug 10 2014 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Initial package
