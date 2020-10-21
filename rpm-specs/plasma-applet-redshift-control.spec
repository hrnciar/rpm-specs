%undefine __cmake_in_source_build

Name:           plasma-applet-redshift-control
Version:        1.0.18
Release:        9%{?dist}
Summary:        Plasma 5 applet for redshift 

License:        GPLv2+
URL:            https://github.com/kotelnik/plasma-applet-redshift-control
Source0:        %{url}/archive/v%{version}.tar.gz

# Patch to unbundle fontawesome fonts
Patch0:         plasma-applet-redshift-control-unbundle-font.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-rpm-macros

Requires:       fontawesome-fonts
Requires:       kf5-filesystem
Requires:       plasma-desktop
Requires:       redshift


%description
Plasma 5 applet for controlling redshift (screen temperature modifying).
It allowes basic redshift settings and fast manual temperature control
by mouse wheel.


%prep
%setup -q -n %{name}-%{version}
# Remove bundled font
%patch0 -p1
rm -f package/contents/fonts/fontawesome-webfont-4.3.0.ttf
rmdir package/contents/fonts

%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install
make install DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang %{name} --all-name


%files -f %{name}.lang
%license LICENSE
%exclude %{_kf5_metainfodir}/*.appdata.xml
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.redshiftControl.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kde.redshiftControl/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 1.0.18-4
- fix location of appdata file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Christian Dersch <lupinix@mailbox.org> - 1.0.18-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 06 2016 Christian Dersch <lupinix@fedoraproject.org> - 1.0.17-1
- Initial package

