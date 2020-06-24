Name:          dianara
Summary:       Pump.io application for the desktop
Version:       1.4.3
Release:       2%{?dist}
License:       GPLv2+
URL:           https://jancoding.wordpress.com/dianara/
Source0:       http://download.savannah.gnu.org/releases/dianara/dianara-v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel, qt5-qtsvg-devel
BuildRequires: kf5-sonnet-devel, kf5-kwidgetsaddons-devel
BuildRequires: qoauth-qt5-devel
BuildRequires: file-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: qca-qt5-ossl%{?_isa}
Requires: hicolor-icon-theme

%description
Dianara is a pump.io client, a desktop application that allows users
to manage their Pump.io social networking accounts without the need
to use a web browser, and provides many features not available
in the standard web interface.

%prep
%autosetup -n %{name}-v%{version}

%build
mkdir build && pushd build
%{qmake_qt5} ../Dianara.pro \
 QMAKE_CFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_CXXFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_LFLAGS="$RPM_LD_FLAGS"
%make_build
popd

%install
%make_install -C build INSTALL_ROOT=$RPM_BUILD_ROOT

rename org.nongnu.%{name} %{name} $RPM_BUILD_ROOT%{_datadir}/applications/org.nongnu.%{name}.desktop
rename org.nongnu.%{name} %{name} $RPM_BUILD_ROOT%{_metainfodir}/org.nongnu.dianara.appdata.xml

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%files
%license LICENSE
%doc README BUGS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}*.xml
%{_mandir}/man1/dianara.*
%{_datadir}/icons/hicolor/32x32/apps/dianara.png
%{_datadir}/icons/hicolor/64x64/apps/dianara.png

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Antonio Trande <sagitter@fedoraproject.org> 1.4.3-1
- Release 1.4.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Antonio Trande <sagitter@fedoraproject.org> 1.4.2-1
- Release 1.4.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.1-3
- Remove obsolete scriptlets

* Mon Jan 01 2018 Antonio Trande <sagitter@fedoraproject.org> 1.4.1-2
- Fix scriptles

* Sat Dec 30 2017 Antonio Trande <sagitter@fedoraproject.org> 1.4.1-1
- First package
