# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

Name:		0ad-data
Version:	0.0.23b
Release:	4%{?dist}
Summary:	The Data Files for 0 AD
License:	CC-BY-SA
Url:		http://play0ad.com
Source:		http://releases.wildfiregames.com/0ad-%{version}-alpha-unix-data.tar.xz
BuildRequires:	unzip
Requires:	dejavu-sans-fonts
Requires:	dejavu-sans-mono-fonts
BuildArch:	noarch

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

This package contains the 0ad data files.

%prep
%setup -q -n 0ad-%{version}-alpha

%build
pushd binaries/data/mods/public
    mkdir tmp
    pushd tmp
        unzip -x ../public.zip
	cp -a art/LICENSE.txt ../../../../../LICENSE-art.txt
	cp -a audio/LICENSE.txt ../../../../../LICENSE-audio.txt
        rm -fr *
    popd
    rm -fr tmp
popd

%install
%__mkdir_p %{buildroot}%{_datadir}
%__rm -f tools/fontbuilder/fonts/*.ttf
%__mv binaries/data %{buildroot}%{_datadir}/0ad

%files
%license LICENSE-art.txt LICENSE-audio.txt
%{_datadir}/0ad

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Pete Walter <pwalter@fedoraproject.org> - 0.0.23b-1
- Update to 0.0.23b

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.23-1
- Update to 0.0.23

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.22-1
- Update to 0.0.22

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.21-1
- Update to 0.0.21

* Sat Apr 02 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.0.20-1
- Update to 0.0.20

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.19-1
- 0.0.19

* Sun Nov 22 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.19-0.1.rc2
- 0.0.19-rc2

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.18-1
- Update to latest upstream release

* Sun Oct 12 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.17-1
- Update to latest upstream release

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.16-1
- Update to latest upstream release

* Fri Dec 27 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.15-1
- Update to latest upstream release

* Thu Sep  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.14-1
- Update to latest upstream release

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 3 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.13-1
- Update to latest upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.12-1
- Update to latest upstream release

* Tue Sep 25 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-3
- Install LICENSE.txt files in proper documentation directory.

* Tue Sep 11 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-2
- Install license files (#823102)
- Clarify this package are the 0ad data files (#823102)
- Use system dejavu-sans fonts.

* Sat Sep 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-1
- Update to latest upstream release

* Sat May 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-1
- Correct package license.
- Update to latest upstream release.

* Tue May 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11339-1
- Initial 0ad-data spec.
