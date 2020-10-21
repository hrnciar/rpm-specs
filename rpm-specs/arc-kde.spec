Name:           arc-kde
Version:        20180614
Release:        5%{?dist}
Summary:        Port of the popular GTK theme Arc for the Plasma 5 desktop

License:        GPLv3 and CC-BY-SA
URL:            https://github.com/PapirusDevelopmentTeam/arc-kde
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Recommends:     %{name}-kvantum
Recommends:     %{name}-decorations
Recommends:     %{name}-konsole
Recommends:     %{name}-konversation
Recommends:     %{name}-wallpapers
Recommends:     %{name}-yakuake
Recommends:     papirus-icon-theme


%description
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

In this package you'll find:

 - Aurorae Themes
 - Konsole Color Schemes
 - Konversation Themes
 - Kvantum Themes
 - Plasma Color Schemes
 - Plasma Desktop Themes
 - Plasma Look-and-Feel Settings
 - Wallpapers
 - Yakuake Skins
 - Extra tools


%package kvantum
Summary:    Arc-KDE Kvantum theme
License:    GPLv3
BuildArch:  noarch
Requires:   kvantum

%description kvantum
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the ArcDark ard ArcDarker Kvantum theme.


%package decorations
Summary:    Arc-KDE Aurorae theme
License:    GPLv3
BuildArch:  noarch

%description decorations
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Aurorae window decorations.


%package konsole
Summary:    Arc-KDE Konsole theme
License:    GPLv3
BuildArch:  noarch

%description konsole
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the ArcDark Konsole theme.


%package konversation
Summary:    Arc-KDE Konversation theme
License:    GPLv3
BuildArch:  noarch

%description konversation
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Konversation theme.


%package wallpapers
Summary:    Arc-KDE wallpapers
License:    CC-BY-SA
BuildArch:  noarch

%description wallpapers
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Arc wallpapers.


%package yakuake
Summary:    Arc-KDE Yakuake theme
License:    GPLv3
BuildArch:  noarch

%description yakuake
This is a port of the popular GTK theme Arc for Plasma 5 desktop with a few 
additions and extras.

This package contains the Yakuake theme.


%prep
%autosetup

cp wallpapers/Arc-Dark/LICENSE LICENSE-wallpapers


%build
# Nothing to build


%install
%make_install


%files
%license LICENSE LICENSE-wallpapers
%doc AUTHORS README.md
%{_datadir}/color-schemes/*.colors
%{_datadir}/plasma/desktoptheme/Arc-Color
%{_datadir}/plasma/desktoptheme/Arc-Dark
%{_datadir}/plasma/look-and-feel/com.github.varlesh.arc-dark


%files decorations
%license LICENSE
%{_datadir}/aurorae/themes/Arc
%{_datadir}/aurorae/themes/Arc-Dark


%files konsole
%license LICENSE
%{_datadir}/konsole/*.colorscheme


%files konversation
%license LICENSE
%{_datadir}/konversation/themes/papirus
%{_datadir}/konversation/themes/papirus-dark


%files kvantum
%license LICENSE
%{_datadir}/Kvantum/Arc
%{_datadir}/Kvantum/ArcDark
%{_datadir}/Kvantum/ArcDarker


%files wallpapers
%license LICENSE-wallpapers
%{_datadir}/wallpapers/Arc
%{_datadir}/wallpapers/Arc-Dark


%files yakuake
%license LICENSE
%{_datadir}/yakuake/skins/arc
%{_datadir}/yakuake/skins/arc-dark


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180614-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180614-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180614-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180614-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 20180614-1
- Initial release
