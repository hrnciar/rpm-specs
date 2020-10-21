%global commit      2d8102084eaf194f04076ec6949feacb0eb4a1ba
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20180927

Name:           suru-icon-theme
Version:        0
Release:        6.%{date}git%{shortcommit}%{?dist}
Summary:        Suru icon and cursor set

# For a breakdown of the licensing, see COPYING LICENSE_CCBYSA LICENSE_GPL3
License:        GPLv3 and CC-BY-SA
URL:            https://snwh.org/suru
Source0:        https://github.com/snwh/suru-icon-theme/tarball/%{commit}#/%{name}-%{version}%{date}git%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  meson

Requires:       adwaita-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
This project is a revitalization of the Suru icon set that was designed for
Ubuntu Touch. The principles and styles created for Suru now serve as the basis
for a new FreeDesktop icon theme.

%prep
%autosetup -n snwh-%{name}-%{shortcommit}

%build
%meson
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}%{_datadir}
touch %{buildroot}/%{_datadir}/icons/Suru/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Suru
gtk-update-icon-cache --force %{_datadir}/icons/Suru &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/Suru
gtk-update-icon-cache --force %{_datadir}/icons/Suru &>/dev/null || :

%files
%doc AUTHORS README.md CONTRIBUTING.md
%license COPYING LICENSE_CCBYSA LICENSE_GPL3
%{_datadir}/icons/Suru
%ghost %{_datadir}/icons/Suru/icon-theme.cache

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20180927git2d81020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20180927git2d81020
- Update spec file

* Thu Jul 12 2018 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20180927git2d81020
- Initial package
