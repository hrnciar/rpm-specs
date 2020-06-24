%global commit      36b97689cfaa2e20344590d4b01e079149106fc8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20200414
%global giturl      https://github.com/keeferrourke/%{name}

%global themename   La-Capitaine

Name:           la-capitaine-icon-theme
Version:        0.6.1
Release:        7.%{date}git%{shortcommit}%{?dist}
Summary:        Icon pack designed to integrate with most desktop environments

# For a breakdown of the licensing, see COPYING and LICENSE
License:        GPLv3+ and MIT
URL:            https://krourke.org/projects/art/la-capitaine-icon-theme
Source0:        %{giturl}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  fdupes

Requires:       adwaita-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
La Capitaine is an icon pack — designed to integrate with most desktop
environments. The set of icons takes inspiration from the latest iterations of
macOS and Google's Material Design through the use of visually pleasing
gradients, shadowing, and simple icon geometry.


%prep
%autosetup -n %{name}-%{commit}

# Remove executable bit
find -executable -type f -exec chmod -x {} +


%install
mkdir -p            %{buildroot}%{_datadir}/icons/%{themename}
cp -rp actions      %{buildroot}%{_datadir}/icons/%{themename}
cp -rp animations   %{buildroot}%{_datadir}/icons/%{themename}
cp -rp apps         %{buildroot}%{_datadir}/icons/%{themename}
cp -rp devices      %{buildroot}%{_datadir}/icons/%{themename}
cp -rp emblems      %{buildroot}%{_datadir}/icons/%{themename}
cp -rp emotes       %{buildroot}%{_datadir}/icons/%{themename}
cp -rp mimetypes    %{buildroot}%{_datadir}/icons/%{themename}
cp -rp panel        %{buildroot}%{_datadir}/icons/%{themename}
cp -rp places       %{buildroot}%{_datadir}/icons/%{themename}
cp -rp status       %{buildroot}%{_datadir}/icons/%{themename}
install -Dpm0644 index.theme %{buildroot}%{_datadir}/icons/%{themename}/index.theme

# Remove all logos except Fedora
find    %{buildroot}%{_datadir}/icons/%{themename}/apps/scalable/distributor-logo* \
    ! -name 'distributor-logo-fedora.svg' -type f -exec rm {} +
mv      %{buildroot}%{_datadir}/icons/%{themename}/apps/scalable/distributor-logo-fedora.svg \
        %{buildroot}%{_datadir}/icons/%{themename}/apps/scalable/distributor-logo.svg

# Remove all logos except GNOME and Red Hat
find    %{buildroot}%{_datadir}/icons/%{themename}/places/scalable/distributor-logo* \
    ! -name '{distributor-logo-gnome.svg,distributor-logo-redhat.svg}' -type f -exec rm {} +

%fdupes -s %{buildroot}%{_datadir}

touch %{buildroot}/%{_datadir}/icons/%{themename}/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/%{themename}
gtk-update-icon-cache --force %{_datadir}/icons/%{themename} &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/%{themename}
gtk-update-icon-cache --force %{_datadir}/icons/%{themename} &>/dev/null || :


%files
%license COPYING LICENSE
%doc README.md Credits.md Thanks.md
%{_datadir}/icons/%{themename}/
%ghost %{_datadir}/icons/%{themename}/icon-theme.cache


%changelog
* Mon Jun 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-7.20200414git36b9768
- Update to latest git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6.20200105git90b4015
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-5.20200105git90b4015
- Update to latest git snapshot

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-4.20190904gitef79681
- Update to latest git snapshot

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3.20190418gitbc48265
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.1-2.20190418gitbc48265
- Initial package
