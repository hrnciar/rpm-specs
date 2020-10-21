Name:			tuxcut
Version:		5.1
Release:		13%{?dist}
URL:			https://bitbucket.org/a_atalla/tuxcut/overview
Summary:		Arpspoof attacks protector
License:		GPLv3
Source0:		https://bitbucket.org/a_atalla/tuxcut/downloads/%{name}-%{version}-src.tar.gz
Source1:		tuxcut.desktop
Source2:		tuxcut
Source3:		org.ojuba.pkexec.tuxcut.policy
BuildRequires:	ImageMagick
BuildRequires:	perl-interpreter
BuildRequires:	desktop-file-utils
BuildRequires:	python2
Requires:		PyQt4
Requires:		arp-scan
Requires:		arptables_jf
Requires:		dsniff
Requires:		polkit
Requires:		wondershaper
Requires:		hicolor-icon-theme
BuildArch:		noarch

%description
TuxCut is a utility that protect linux computers againest arpspoof attacks

Features:
	- Hide your machine (ip/MAC) from arp scanner utilities.
	- list all the live host in your LAN.
	- cut the connection between any live host and the gateway.
	- use wondershaper to limit your upload or download speed.
 
%prep
%setup -qc %{name}-%{version}
# fix resum error
perl -pi -le 'print "		self.resume_all()" if $. == 85' tuxcut_core.py

# fix error No such file or directory: 'ui/MainWindow.ui'
perl -pi -w -e 's|ui/MainWindow.ui|%{_datadir}/tuxcut/ui/MainWindow.ui|g;' tuxcut_core.py

# Specific env to python2
perl -pi -w -e 's|#!/usr/bin/env python|#!%{__python2}|g;' tuxcut.py

# remove executable permission to allow build on rawhide
chmod a-x tuxcut.py

%build
#nothing to build

%install
mkdir -p %{buildroot}/{%{_datadir}/tuxcut,%{_bindir}}

cp -ar * %{buildroot}%{_datadir}/tuxcut
install -pDm0755 %{SOURCE1} %{buildroot}%{_datadir}/applications/tuxcut.desktop
install -pDm0755 %{SOURCE2} %{buildroot}%{_bindir}/tuxcut
install -pDm0644 pix/tuxcut.png %{buildroot}%{_datadir}/pixmaps/tuxcut.png
install -pDm0644 %{SOURCE3} %{buildroot}%{_datadir}/polkit-1/actions/org.ojuba.pkexec.tuxcut.policy
desktop-file-install %{buildroot}%{_datadir}/applications/tuxcut.desktop

# Install icon
for res in 16x16 22x22 24x24 32x32 36x36 48x48 64x64 72x72 96x96; do \
  mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/{${res},scalable}/apps
  convert -size 400x400 pix/tuxcut.png -resize ${res} %{buildroot}/%{_datadir}/icons/hicolor/${res}/apps/tuxcut.png
done;


%files
%{_bindir}/tuxcut
%{_datadir}/applications/tuxcut.desktop
%{_datadir}/icons/hicolor/*/apps/tuxcut.png
%{_datadir}/pixmaps/tuxcut.png
%{_datadir}/polkit-1/actions/org.ojuba.pkexec.tuxcut.policy
%{_datadir}/tuxcut
%exclude %{_datadir}/tuxcut/LICENSE
%exclude %{_datadir}/tuxcut/README
%doc LICENSE README

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 5.1-8
- rebuilt to fix FTBFS on rawhide + spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Mosaab Alzoubi <moceap@hotmail.com> - 5.1-1
- Update release.
- New upstream URL method.
- Tweak %%prep for new release.
- Use upstream icon.
- Update bin/tuxcut.

* Sun Dec 1 2013 Mosaab Alzoubi <moceap@hotmail.com> - 5.0-15
- Fix BRs.

* Fri Nov 29 2013 Mosaab Alzoubi <moceap@hotmail.com> - 5.0-14
- Move documents into %%doc files.
- Add hicolor-icon-theme to requires.
- Add executable permission to tuxcut.desktop :).
- Update summary in desktop file.
- Specific env to python2 in both run.py and tuxcut in bindir.
- Add python2-devel to BRs.

* Thu Nov 28 2013 Mosaab Alzoubi <moceap@hotmail.com> - 5.0-13
- Update summary line.
- Update description.
- General tweaks.
- Remove %%defattr line.
- Add icon cache update operation.

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 5.0-12
- To zero warnings by rpmlint.
- Fix summary line.

* Fri Oct 11 2013 Mosaab Alzoubi <moceap@hotmail.com> - 5.0-11
- Add mark of source URL.

* Fri Oct 11 2013 Mosaab Alzoubi <moceap@hotmail.com> - 5.0-10
- Full exit from opt dir.
- Add rule to polkit.

* Thu Oct 10 2013 Mosaab Alzoubi <moceap@hotmail.com> - 5.0-9
- Fixes to be compatible with Fedora rules.

* Mon Mar 18 2013 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 5.0-1
- update

* Fri Oct 26 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 4.1-1
- update

* Sun Jul 08 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 4.0-1
- update

* Thu Jun 14 2012 Muhammad Shaban <Mr.Muhammad@linuxac.org> - 3.2-1
- initial package
