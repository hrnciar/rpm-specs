%global srcname SiriKali
%global srcurl  https://github.com/mhogomchungu/%{name}

Name:           sirikali
Version:        1.4.4
Release:        1%{?dist}
Summary:        GUI front end to encfs,cryfs,gocryptfs and securefs
# generally GPLv2+, BSD for tasks and NetworkAccessManager folders
License:        GPLv2+ and BSD
URL:            http://mhogomchungu.github.io/%{name}

Source0:        %{srcurl}/releases/download/%{version}/%{srcname}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: json-devel
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(lxqt-wallet)

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)

BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
Requires:      hicolor-icon-theme

Recommends:    fuse-encfs

%description
%{srcname} is a Qt/C++ GUI front end to encfs,cryfs,gocryptfs and securefs.


%prep
%autosetup -p1 -n%{srcname}-%{version}
# collect licenses
cp -p src/3rdParty/tasks/LICENSE LICENSE-tasks
cp -p src/3rdParty/NetworkAccessManager/LICENSE LICENSE-NetworkAccessManager
# unbundle
pushd src/3rdParty
rm -rv json* lxqt_wallet
popd
sed -i -r 's:".*(json.hpp)":"\1":' CMakeLists.txt
sed -i 's:3rdParty/json:json:' src/%{name}.cpp

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%cmake .. -DQT5=true \
 -DNOKDESUPPORT=true -DNOSECRETSUPPORT=false \
 -DINTERNAL_LXQT_WALLET=false

%install
%make_install -C %{_target_platform}
# ugly, we don't want any prefix to desktop file
mv %{buildroot}%{_datadir}/applications/*%{name}.desktop\
 %{buildroot}%{_datadir}/applications/%{name}.desktop ||:
chmod -x %{buildroot}%{_datadir}/applications/*.desktop
%find_lang %{name} --with-qt --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%license COPY* LICENSE* GPLv*
%doc README.md ABOUT* changelog
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/%{name}*.1*


%changelog
* Mon Jun 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.4-1
- 1.4.4

* Wed Apr 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.4.3-1
- 1.4.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.2-1
- 1.4.2

* Mon Nov 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- 1.4.1

* Sun Sep 08 2019 Raphael Groner <projects.rg@smart.ms> - 1.3.9-1
- new version

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 1.3.8-1
- new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.6-1
- new version

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.3.4-3
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.4-2
- Rebuild for new binutils

* Thu Jul 26 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.4-1
- bump to 1.3.4, fix FTBFS
- try harder to add all license texts

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.3-1
- new version
- drop upstream patches, due to incl.
- add license breakdown for 3rdParty folders

* Wed Feb 07 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.2-2
- drop obsolete scriptlets
- drop explicit file permission
- include upstreamed patches

* Sat Jan 13 2018 Raphael Groner <projects.rg@smart.ms> - 1.3.2-1
- new version
- drop BSD because unbundled json
- unbundle lxqt_wallet

* Tue Jul 11 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.9-1
- new version
- unbundle json

* Mon Jun 12 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.7.1.20170611git
- new version
- use git snapshot to include latest upstream patches
- include upstream patch to get full path of su binary
- distribute additonal files
- drop workaround for duplicated readme files
- fix length of line in description

* Sun Jun 04 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.5-2
- fix duplication of license documentation files
- reorder explicit ownership of folders
- fix file attributes of desktop file
- add weak dependency to fuse-encfs

* Wed Mar 01 2017 Raphael Groner <projects.rg@smart.ms> - 1.2.5-1
- adopt for Fedora
