%global orig_name org.kde.plasma.translator

Name:           plasma-applet-translator
Version:        0.7
Release:        1%{?dist}
Summary:        Plasma 5 applet for translate-shell

License:        MIT
URL:            https://store.kde.org/p/1395666
Source0:        http://qml.i-glu4it.ru/%{orig_name}_%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils

Requires:       translate-shell
Requires:       plasma-workspace

%description
Easy to use translation plasmoid (GUI for translate-shell package).

%prep
%autosetup -n %{orig_name}


%build


%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}
cp -r contents %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/
install -pm 644 metadata.desktop %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%files
%license LICENSE
# %doc add-docs-here
%{_datadir}/plasma/plasmoids/%{orig_name}

%changelog
* Mon Aug 31 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.7-1
- Update to 0.7

* Mon Aug 10 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.5-1
- Update to 0.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.4-1
- Update to 0.4

* Fri Jul 10 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.3-1
- Update to 0.3

* Sun Jun 28 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.2-1
- Update to 0.2

* Wed Jun 24 2020 Vasiliy Glazov <vascom2@gmail.com> - 0.1-1
- Initial packaging
