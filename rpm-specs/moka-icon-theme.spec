%global commit      c0355ea31e5cfdb6b44d8108f602d66817546a09
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190530

%global tname       Moka

Name:           moka-icon-theme
Version:        5.4.0
Release:        3.%{date}git%{shortcommit}%{?dist}
Summary:        Moka Icon Theme

License:        CC-BY-SA and GPLv3
URL:            https://snwh.org/moka
Source0:        https://github.com/snwh/%{name}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  meson
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
Moka is a stylized FreeDesktop icon set, created with simplicity in mind.
It uses simple geometry & bright colours and has been designed and optimized to
achieve the a pixel-perfect look for your desktop.

Also, one of the most comprehensive icon sets available, Moka provides thousands
of icons for many applications. So no matter which Linux desktop you are using,
Moka has you covered.


%prep
%autosetup -p1 -n %{name}-%{commit}
chmod 644 COPYING LICENSE_CC-BY-SA LICENSE_GPL \
    README.md AUTHORS CONTRIBUTING.md


%build
%meson
%meson_build


%install
%meson_install
chmod -x %{buildroot}%{_datadir}/icons/%{tname}/index.theme


%transfiletriggerin -- %{_datadir}/icons/%{tname}
gtk-update-icon-cache --force %{_datadir}/icons/%{tname} &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{tname}
gtk-update-icon-cache --force %{_datadir}/icons/%{tname} &>/dev/null || :


%files
%license COPYING LICENSE_CC-BY-SA LICENSE_GPL
%doc README.md AUTHORS CONTRIBUTING.md
%{_datadir}/icons/%{tname}
%ghost %{_datadir}/icons/%{tname}/icon-theme.cache


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3.20190530gitc0355ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 5.4.0-2.20190530gitc0355ea
- Minor packaging fixes

* Tue Sep 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 5.4.0-1.20190530gitc0355ea
- Update to latest git snapshot
- Switch to Meson build system
- Packaging fixes

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep  4 2017 Allisson Azevedo <allisson@gmail.com> - 5.3.6-1
- Initial RPM release
