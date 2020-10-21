Name:           flyingsaucersattack
Version:        1.20h
Release:        13%{?dist}
Summary:        Shoot down the attacking UFOs and to save the city
# Engine is MIT, resources are CC-BY-SA-4.0
License:        MIT and CC-BY-SA
URL:            http://www.dennisbusch.de/fsa.php
Source0:        http://www.dennisbusch.de/software/fsa/fuga120h.zip
Source1:        %{name}.png
Source2:        %{name}.desktop
Source3:        %{name}.appdata.xml
# Note upstream is not interested in taking unix porting patches
Patch0:         flyingsaucersattack-1.20h-unixify.patch
BuildRequires:  gcc-c++
BuildRequires:  allegro-devel dumb-devel desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
F.S.A. (Flying Saucers Attack) aka F.U.G.A. (Fliegende Untertassen greifen an)
is a kind of mixture between two old Atari2600 games.
It comes in German and English language.

You'll see a screen with your city that you have to save against 30 Alien
attack waves in three different difficulty levels.

You shoot attacking UFOs with two cannons positioned at the left and right
borders of the screen. The UFOs will first bomb away all your buildings then
send in little green men to dig tunnels to blow your cannons which results
in a game over.


%prep
%setup -q -n fuga120h
%patch0 -p1 -b .unix
for i in docs/*; do
  sed -i 's/\r//' $i;
done


%build
# Note -Wno-format-security is to work around the custom translation system
# All format strings passed to printf are actually const strings
%make_build -C sources \
  CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations -Wno-deprecated -Wno-write-strings -Wno-unused-result -Wno-format-security"


%install
%make_install -C sources
# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml



%files
%doc docs/*
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20h-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20h-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Hans de Goede <hdegoede@redhat.com> - 1.20h-3
- Minor specfile cleanups (rhbz#1303349)

* Sat Feb 27 2016 Hans de Goede <hdegoede@redhat.com> - 1.20h-2
- Fix a few spelling errors in the description (rhbz#1303349)
- Fix gcc6 compiler warnings

* Sat Jan 30 2016 Hans de Goede <hdegoede@redhat.com> - 1.20h-1
- Initial Fedora package
