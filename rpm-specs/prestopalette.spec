
Name:		prestopalette
Version:	0.1.31
Release:	7%{?dist}
Summary:	An artist's tool for creating harmonious color palettes

License:	MIT
URL:		https://github.com/PrestoPalette/PrestoPalette
Source0:	https://github.com/PrestoPalette/PrestoPalette/archive/%{version}/%{version}.tar.gz#/prestopalette-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/PrestoPalette/PrestoPalette-Packaging/master/Fedora/PrestoPalette.appdata.xml#/PrestoPalette.appdata.xml
Source2:	https://raw.githubusercontent.com/PrestoPalette/PrestoPalette-Packaging/master/Fedora/Icon.png#/PrestoPalette.png

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gcc-c++

%{?fedora:BuildRequires: qt5-devel}

%{?el7:BuildRequires: qt5-qtbase-devel}
%{?el7:BuildRequires: qt5-qtmultimedia-devel}
%{?el7:BuildRequires: tar}

%description
%{name} is an artist's tool for creating harmonious color palettes.

%prep
%autosetup -n PrestoPalette-%{version}

%build
%qmake_qt5 -config release PrestoPalette.pro && \
%make_build all
cat > PrestoPalette.desktop <<EOF
[Desktop Entry]
Name=PrestoPalette
Comment=An artist's tool for creating harmonious color palettes
Exec=PrestoPalette
Icon=%{_datadir}/pixmaps/PrestoPalette.png
Terminal=false
Type=Application
Categories=Graphics
EOF

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/{applications,pixmaps,metainfo}
install -Dp -m 755 build/release/PrestoPalette %{buildroot}/%{_bindir}
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications PrestoPalette.desktop
appstream-util validate-relax --nonet %{SOURCE1}
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/metainfo/
install -Dp -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/

%files
%{_bindir}/PrestoPalette
%{_datadir}/applications/PrestoPalette.desktop
%{_datadir}/metainfo/PrestoPalette.appdata.xml
%{_datadir}/pixmaps/PrestoPalette.png
%license LICENSE

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Darryl T. Agostinelli <dagostinelli@gmail.com> 0.1.31-4
- Corrected bodhi lint check against desktop file regarding multiple primary categories

 Wed Jul 18 2018 Darryl T. Agostinelli <dagostinelli@gmail.com> 0.1.31-3
- Corrected bodhi lint check against desktop file regarding icon name with an extension

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Darryl T. Agostinelli <dagostinelli@gmail.com> 0.1.31-1
- Created the .spec file for version 0.1.31
