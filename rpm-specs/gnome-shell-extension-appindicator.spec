%global uuid appindicatorsupport@rgcjonas.gmail.com

Name: gnome-shell-extension-appindicator
Version: 34
Release: 1%{?dist}
Summary: AppIndicator/KStatusNotifierItem support for GNOME Shell
BuildArch: noarch

License: GPLv2
URL: https://github.com/ubuntu/gnome-shell-extension-appindicator
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: gnome-shell >= 3.14.0

%description
This extension integrates Ubuntu AppIndicators and KStatusNotifierItems (KDE's
blessed successor of the systray) into GNOME Shell.

You can use gnome-tweaks (additional package) or run in terminal:

  gnome-extensions enable %uuid


%prep
%autosetup -p1


%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -axv *.js metadata.json interfaces-xml \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/


%files
%license LICENSE
%doc README.md AUTHORS.md
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Sat Sep 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 34-1
- Update to 34

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 33-1
- Update to 33

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 30-7
- Initial package
