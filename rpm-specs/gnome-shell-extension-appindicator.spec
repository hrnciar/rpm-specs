%global uuid    appindicatorsupport@rgcjonas.gmail.com

Name:           gnome-shell-extension-appindicator
Version:        33
Release:        1%{?dist}
Summary:        AppIndicator/KStatusNotifierItem support for GNOME Shell

License:        GPLv2
URL:            https://github.com/ubuntu/gnome-shell-extension-appindicator
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       gnome-shell >= 3.14.0

%description
This extension integrates Ubuntu AppIndicators and KStatusNotifierItems (KDE's
blessed successor of the systray) into GNOME Shell.

You can use gnome-tweaks (additional package) or run in terminal:

  gnome-extensions enable %uuid


%prep
%autosetup


%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -axv *.js metadata.json interfaces-xml \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/


%files
%license LICENSE
%doc README.md AUTHORS.md
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Tue Mar 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 33-1
- Update to 33

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 30-7
- Initial package
