%global git_repo    candy-icons
%global git_url     https://github.com/EliverLara/%{git_repo}
%global git_commit  4be1a05e38e80a145132fc6ac26fe5ae0f9ace34
%global git_date    20200620

%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:8})

Name:           candy-icon-theme
Version:        0
Release:        13.%{git_date}git%{git_commit_short}%{?dist}
Summary:        Sweet gradient icon theme

License:        GPLv3
URL:            https://www.opendesktop.org/p/1305251/
Source0:        %{git_url}/archive/%{git_commit}/%{git_repo}-%{git_commit}.tar.gz

BuildArch:      noarch

Requires:       breeze-icon-theme
Requires:       elementary-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme
Requires:       mint-x-icons

%description
Candy Icons is a simplistic, vector, gradient icon theme.


%prep
%autosetup -n %{git_repo}-%{git_commit}

# Use a prettier name for the theme
sed \
  -e 's|^Name=candy-icons$|Name=Candy Icons|' \
  -i index.theme


%build
# Nothing to do here


%install
CANDY_DIR="%{buildroot}%{_datadir}/icons/Candy"
install -m 755 -d "${CANDY_DIR}"
install -m 644 index.theme "${CANDY_DIR}/"

cp -a apps/ "${CANDY_DIR}/"
cp -a places/ "${CANDY_DIR}/"

touch "${CANDY_DIR}/icon-theme.cache"


%transfiletriggerin -- %{_datadir}/icons/Candy
gtk-update-icon-cache --force %{_datadir}/icons/Candy &>/dev/null || :


%files
%license LICENSE

%dir %{_datadir}/icons/Candy
%{_datadir}/icons/Candy/index.theme
%{_datadir}/icons/Candy/**/*
%ghost %{_datadir}/icons/Candy/icon-theme.cache


%changelog
* Tue Jun 23 2020 Artur Iwicki <fedora@svgames.pl> - 0.13.20200620git4be1a05e
- Update to latest upstream snapshot

* Wed May 20 2020 Artur Iwicki <fedora@svgames.pl> - 0.12.20200514git9d5b05d0
- Update to latest upstream snapshot

* Fri Apr 24 2020 Artur Iwicki <fedora@svgames.pl> - 0.11.20200423git3fbc68f8
- Update to latest upstream snapshot
- Do not move the files around, stick to upstream directory hierarchy
- Add dependency on breeze-icon-theme

* Fri Apr 17 2020 Artur Iwicki <fedora@svgames.pl> - 0-10.20200403gita9a4cdf7
- Update to latest upstream snapshot

* Sun Mar 22 2020 Artur Iwicki <fedora@svgames.pl> - 0-9.20200312gitfc3fbcad
- Upate to latest upstream snapshot

* Fri Feb 21 2020 Artur Iwicki <fedora@svgames.pl> - 0-8.20200220gita6e938f8
- Update to latest upstream snapshot

* Sun Feb 02 2020 Artur Iwicki <fedora@svgames.pl> - 0-7.20200131git8f853b2e
- Update to latest upstream snapshot
- Fix symlinks not being preserved in packaging

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20200110git4e63197c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Artur Iwicki <fedora@svgames.pl> - 0-5.20200110git4e63197c
- Update to latest upstream snapshot

* Sat Dec 21 2019 Artur Iwicki <fedora@svgames.pl> - 0-4.20191220gitd8f73028
- Update to latest upstream snapshot

* Wed Dec 11 2019 Artur Iwicki <fedora@svgames.pl> - 0-3.20191210gitd68a12e8
- Update to latest upstream snapshot
- Preserve timestamps for icon files

* Sat Nov 30 2019 Artur Iwicki <fedora@svgames.pl> - 0-2.20191129gite14463b4
- Update to latest upstream snapshot
- Change "Requires:" to match "Inherits=" from index.theme

* Fri Nov 15 2019 Artur Iwicki <fedora@svgames.pl> - 0-1.20191113gita9f7014e
- Initial packaging
