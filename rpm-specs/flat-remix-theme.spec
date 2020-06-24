%global vergit  20191224

Name:           flat-remix-theme
Version:        0.0.%{vergit}
Release:        2%{?dist}
Summary:        Pretty simple theme inspired on material design

License:        GPLv3+
URL:            https://drasite.com/flat-remix-gtk
Source:         https://github.com/daniruiz/flat-remix-gtk/archive/%{vergit}/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       flat-remix-gtk2-theme
Requires:       flat-remix-gtk3-theme
Requires:       flat-remix-icon-theme
Recommends:     gnome-shell-theme-flat-remix

%global _description %{expand:
Flat Remix GTK theme is a pretty simple GTK window theme inspired on material
design following a modern design using "flat" colors with high contrasts and
sharp borders.

Themes:
- Flat Remix GTK
- Flat Remix GTK Dark
- Flat Remix GTK Darker
- Flat Remix GTK Darkest

Variants:
- Solid: Theme without transparency
- No Border: Darkest theme without white window border}

%description %{_description}

This meta package contains complete Flat Remix theme.


%package     -n flat-remix-gtk2-theme
Summary:        GTK+ 2 support for the Flat Remix GTK theme
Requires:       adwaita-gtk2-theme
Requires:       gtk2%{?_isa}
Recommends:     flat-remix-gtk3-theme

%description -n flat-remix-gtk2-theme %{_description}

This package contains GTK+ 2 theme.


%package     -n flat-remix-gtk3-theme
Summary:        GTK+ 3 support for the Flat Remix GTK theme
Requires:       gtk3%{?_isa}
Recommends:     flat-remix-gtk2-theme
Suggests:       flat-remix-theme

%description -n flat-remix-gtk3-theme %{_description}

This package contains GTK+ 3 theme.


%prep
%autosetup -n flat-remix-gtk-%{vergit}


%install
%make_install


%files
%{_datadir}/themes/*/cinnamon/
%{_datadir}/themes/*/index.theme
%{_datadir}/themes/*/metacity-1/
%{_datadir}/themes/*/xfwm4/
%dir %{_datadir}/themes/*/

%files -n flat-remix-gtk2-theme
%license LICENSE
%doc README.md CHANGELOG
%{_datadir}/themes/*/gtk-2.0/
%dir %{_datadir}/themes/*/

%files -n flat-remix-gtk3-theme
%license LICENSE
%doc README.md CHANGELOG
%{_datadir}/themes/*/gtk-3.0/
%dir %{_datadir}/themes/*/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20191224-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20191224-1
- Update to 20191224

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190901-1
- Update to 20190901

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190604-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190604-1
- Update to 20190604

* Sat May 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190503-3
- Initial package
