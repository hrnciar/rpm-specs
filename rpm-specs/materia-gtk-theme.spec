# WIP: split into sub packages

%global vergit 20200916

Name:           materia-gtk-theme
Version:        0.0.%{vergit}
Release:        1%{?dist}
Summary:        Material Design theme for GNOME/GTK based desktop environments
BuildArch:      noarch

License:        GPLv2
URL:            https://github.com/nana-4/materia-theme
Source0:        %{url}/archive/v%{vergit}/%{name}-%{version}.tar.gz

BuildRequires:  gnome-shell
BuildRequires:  sassc

Requires:       filesystem

Suggests:       flat-remix-icon-theme
Suggests:       papirus-icon-theme

%description
Materia is a Material Design theme for GNOME/GTK based desktop environments.

It supports GTK 2, GTK 3, GNOME Shell, Budgie, Cinnamon, MATE, Unity, Xfce,
LightDM, GDM, Chrome theme, etc.


%prep
%autosetup -n materia-theme-%{vergit} -p1


%install
./install.sh -d %{buildroot}%{_datadir}/themes
find %{buildroot}%{_datadir}/themes -name "COPYING" -exec rm -rf {} \;
find %{buildroot}%{_datadir}/themes -name "index.theme" -exec chmod -x {} \;


%files
%license COPYING
%doc README.md HACKING.md TODO.md
%{_datadir}/themes/Materia*/


%changelog
* Wed Sep 16 21:53:06 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200916-1
- Update to 20200916

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200320-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200320-1
- Update to 20200320

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20191017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20191017-1
- Update to 20191017

* Tue Sep 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190912-1
- Initial package
