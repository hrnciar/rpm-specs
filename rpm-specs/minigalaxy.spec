Name:           minigalaxy
Version:        0.9.4
Release:        3%{?dist}
Summary:        GOG client for Linux that lets you download and play your GOG Linux games
BuildArch:      noarch

# CC-BY:        Logo image (data/minigalaxy.png)
License:        GPLv3+ and CC-BY
URL:            https://github.com/sharkwouter/minigalaxy
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel >= 3.30
BuildRequires:  python3dist(requests)

Requires:       hicolor-icon-theme
Requires:       python3-requests
Requires:       webkit2gtk3

Recommends:     dosbox
Recommends:     wine
Recommends:     wine-dxvk

Suggests:       scummvm

%description
A simple GOG client for Linux that lets you download and play your GOG Linux
games.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE THIRD-PARTY-LICENSES.md
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/


%changelog
* Fri Jun 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.4-3
- Add weak dep: wine-dxvk

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.9

* Mon Apr 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.4-1
- Update to 0.9.4
- Add weak dep: wine | Since version 0.9.4 'minigalaxy' can run Windows games

* Tue Mar 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.3-1
- Update to 0.9.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.2-1
- Update to 0.9.2
- Add new weak deps
- Add AppData manifest

* Fri Dec 27 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-2
- Update to 0.9.1

* Fri Dec 27 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.0-3
- Initial package
