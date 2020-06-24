Name:		megaglest-data
Version:	3.13.0
Release:	2%{?dist}
Summary:	Mega Glest data files
License:	CC-BY-SA
Url:		http://megaglest.org/
Source0:	https://github.com/MegaGlest/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
Obsoletes:	glest-data <= 3.2.2

%description
MegaGlest is an entertaining free (freeware and free software) and
open source cross-platform 3D real-time strategy (RTS) game, where
you control the armies of one of seven different factions: Tech,
Magic, Egypt, Indians, Norsemen, Persian or Romans. The game is
setup in one of 17 naturally looking settings, which -like the
unit models- are crafted with great appreciation for detail.
A lot of additional game data can be downloaded from within the
game at no cost.

%prep
%setup -q -n megaglest-%{version}

%build
mkdir -p build
pushd build
    %cmake								\
	-DMEGAGLEST_ICON_INSTALL_PATH=%{_datadir}/icons			\
	..
    make %{?_smp_mflags}
popd

%install
make install DESTDIR=${RPM_BUILD_ROOT} -C build
rm -fr ${RPM_BUILD_ROOT}%{_datadir}/megaglest/docs
for image in `ls $RPM_BUILD_ROOT%{_datadir}/megaglest/icons`; do
    [ -e $RPM_BUILD_ROOT%{_datadir}/$image ] ||
	ln -sf %{_datadir}/icons/$image $RPM_BUILD_ROOT%{_datadir}/megaglest
done
for file in megaglest megaglest_editor megaglest_g3dviewer; do
    desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/$file.desktop
done

# remove Debian style menu file
rm $RPM_BUILD_ROOT%{_datadir}/menu/megaglest

%files
%doc docs/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/megaglest*.desktop
%{_datadir}/icons/megaglest.*
%dir %{_datadir}/megaglest
%{_datadir}/megaglest/data/
%{_datadir}/megaglest/maps/
%{_datadir}/megaglest/scenarios/
%{_datadir}/megaglest/techs/
%{_datadir}/megaglest/tilesets/
%{_datadir}/megaglest/tutorials/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.13.0-1
- Update to latest upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 24 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.12.0-1
- Update to latest upstream release
- Install desktop and icons as they are no longer in the main package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.11.1-1
- Update to latest upstream release.
- Update description from upstream webpage.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.9.1-1
- Update to latest upstream release.

* Tue Nov 19 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.9.0-1
- Update to latest upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-2
- Rebuild for proper glest-data upgrade (#891875).

* Fri Nov 23 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.7.1-1
- Update to latest upstream release.

* Fri Jul 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-3
- Make again package owner of base data directory.
- Install documentation as %%doc (#817315).

* Fri Jul 6 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-2
- Mark documentation files as %%doc (#828544).
- Use sourceforce link format as specified in the fedora wiki (#828544).

* Fri Jun  1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.6.0.3-1
- Initial megaglest-data spec.
