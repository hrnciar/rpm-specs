%undefine __cmake_in_source_build

%global buildno 20
%global buildid build%{buildno}
# The game contains a copy of these fonts, we replaces these with symlinks to the system versions of these fonts
%global fonts font(amiri) font(dejavusans) font(dejavusansmono) font(dejavuserif) font(widelands) font(lklug) font(wenquanyimicrohei)

Name:           widelands
Version:        0
Release:        0.80.%{buildid}%{?dist}
Summary:        Open source realtime-strategy game

License:        GPLv2+
URL:            http://www.widelands.org
Source0:        https://launchpad.net/widelands/%{buildid}/%{buildid}/+download/widelands-%{buildid}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         widelands-build19-ppc64le.patch
Patch1:         widelands-build20-gcc91.patch
Patch2:         widelands-build20-gcc10.patch
Patch3:         widelands-build20-boost173.patch

BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: boost-devel >= 1.48.0
BuildRequires: cmake
BuildRequires: ctags
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: gettext
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: libpng-devel
# For the %%build part generating the symlinks
BuildRequires: fontconfig %{fonts}
Requires:      hicolor-icon-theme %{fonts}

%description
Widelands is an open source (GPLed), realtime-strategy game, using SDL and
other free libraries, which is still under development. Widelands is inspired
by Settlers II (Bluebyte) and is partly similar to it, so if you know it, you
perhaps will have a thought, what Widelands is all about.


%prep
%autosetup -p1 -n widelands-%{buildid}


%build
LDFLAGS=-lGL
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_bindir} \
    -DWL_INSTALL_BASEDIR=%{_prefix}/share/%{name} \
    -DWL_INSTALL_DATADIR=%{_prefix}/share/%{name} \
    -DOPTION_BUILD_WEBSITE_TOOLS=OFF \
    %{nil}
%cmake_build


%install
%cmake_install

for i in 16 32 48 64 128; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps
  ln -s /usr/share/%{name}/images/logos/wl-ico-${i}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

pushd $RPM_BUILD_ROOT
# Replace fonts with system fonts. We used to have symlinks directly from
# i18n/fonts/<widelands-name> to the /usr/share/fonts/<system-font-name> dir
# but with recent font packaging changes this no longer works because e.g.
# Widelands expects all DejaVu fonts in a single dir, where as now there are
# separate /usr/share/fonts dirs for the sans, sans-mono and serif versions.
#
# Replacing the symlinks at the dir level with keeping the
# i18n/fonts/<widelands-name> directory and then putting symlinks to the
# invidual font-files inside that directory does not work, because on upgrade
# that would mean replacing a symlink with a dir which breaks horribly.
# So for those cases where we used to have a symlink, we create a new dir
# under i18n/fonts with a different name, with symlinks to the individual
# files in that dir; and then point the symlink to this new dir, to avoid
# the replace a symlink with a dir problem.
rm -r usr/share/%{name}/i18n/fonts/amiri
mkdir usr/share/%{name}/i18n/fonts/amiri-fonts
ln -s amiri-fonts usr/share/%{name}/i18n/fonts/amiri
ln -s $(fc-match -f "%{file}" "amiri") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-regular.ttf
ln -s $(fc-match -f "%{file}" "amiri:bold") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-bold.ttf
ln -s $(fc-match -f "%{file}" "amiri:italic") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-slanted.ttf
ln -s $(fc-match -f "%{file}" "amiri:bold:italic") \
  usr/share/%{name}/i18n/fonts/amiri-fonts/amiri-boldslanted.ttf

rm -r usr/share/%{name}/i18n/fonts/DejaVu
mkdir usr/share/%{name}/i18n/fonts/dejavu-fonts
ln -s dejavu-fonts usr/share/%{name}/i18n/fonts/DejaVu
ln -s $(fc-match -f "%{file}" "sans") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans.ttf
ln -s $(fc-match -f "%{file}" "sans:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-Bold.ttf
ln -s $(fc-match -f "%{file}" "sans:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-Oblique.ttf
ln -s $(fc-match -f "%{file}" "sans:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSans-BoldOblique.ttf
ln -s $(fc-match -f "%{file}" "serif") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif.ttf
ln -s $(fc-match -f "%{file}" "serif:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-Bold.ttf
ln -s $(fc-match -f "%{file}" "serif:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-Italic.ttf
ln -s $(fc-match -f "%{file}" "serif:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSerif-BoldItalic.ttf
ln -s $(fc-match -f "%{file}" "monospace") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono.ttf
ln -s $(fc-match -f "%{file}" "monospace:bold") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-Bold.ttf
ln -s $(fc-match -f "%{file}" "monospace:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-Oblique.ttf
ln -s $(fc-match -f "%{file}" "monospace:bold:italic") \
  usr/share/%{name}/i18n/fonts/dejavu-fonts/DejaVuSansMono-BoldOblique.ttf

rm -r usr/share/%{name}/i18n/fonts/MicroHei
mkdir usr/share/%{name}/i18n/fonts/wqy-microhei-fonts
ln -s wqy-microhei-fonts usr/share/%{name}/i18n/fonts/MicroHei
ln -s $(fc-match -f "%{file}" "wenquanyimicrohei") \
   usr/share/%{name}/i18n/fonts/wqy-microhei-fonts/wqy-microhei.ttc

rm -r usr/share/%{name}/i18n/fonts/Sinhala
mkdir usr/share/%{name}/i18n/fonts/lklug-fonts
ln -s lklug-fonts usr/share/%{name}/i18n/fonts/Sinhala
ln -s $(fc-match -f "%{file}" "lklug") \
   usr/share/%{name}/i18n/fonts/lklug-fonts/lklug.ttf

rm -r usr/share/%{name}/i18n/fonts/Widelands/*
ln -s $(fc-match -f "%{file}" "widelands") \
   usr/share/%{name}/i18n/fonts/Widelands/Widelands.ttf

# Scripting magic to add proper %%lang() markings to the locale files
find usr/share/widelands/locale/ -maxdepth 1 -type d -name \*_\* | sed -n 's#\(usr/share/widelands/locale/\(.*\)_.*\)#%lang(\2) /\1#p' > %{_builddir}/widelands-%{buildid}/%{name}.files
find usr/share/widelands/locale/ -maxdepth 1 -type d ! -name "*_*" | sed -n -e 's#\(usr/share/widelands/locale/\(.\+\)\)#%lang(\2) /\1#p' >> %{_builddir}/widelands-%{buildid}/%{name}.files
find usr/share/widelands/ -mindepth 1 -maxdepth 1 -not -name locale | sed -n 's#\(usr/share/widelands/*\)#/\1#p' >> %{_builddir}/widelands-%{buildid}/%{name}.files
popd


%files -f %{name}.files
%doc ChangeLog CREDITS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.80.build20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Jonathan Wakely <jwakely@redhat.com> - 0-0.79.
- Rebuilt for Boost 1.73

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 0-0.78.build20
- Rebuild for ICU 67

* Thu Mar 19 2020 Hans de Goede <hdegoede@redhat.com> - 0-0.77.build20
- Stop replacing symlinks with dirs this breaks upgrades (rhbz 1806272)
- Use fc-match to generate font file symlinks to future proof the package
  against future font file-path or name changes (rhbz 1806272)

* Sat Mar  7 2020 Hans de Goede <hdegoede@redhat.com> - 0-0.76.build20
- Adjust Dejavu font symlinks for dejavu font package path changes
- Fix FTBFS (rhbz#1800251)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.75.build20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 0-0.74.build20
- Work around false positive uninitialized variable warning from gcc10

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0-0.73.build20
- Rebuild for ICU 65

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.72.build20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Hans de Goede <hdegoede@redhat.com> - 0-0.71.build20
- Update to new upstream Build20 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.70.build19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0-0.69.build19
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0-0.68.build19
- Rebuild for ICU 63

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0-0.67.build19
- Rebuilt for glew 2.1.0

* Tue Aug 14 2018 Hans de Goede <hdegoede@redhat.com> - 0-0.66.build19
- Fix FTBFS (rhbz#1606678)
- Add appdata

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.65.build19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0-0.64.build19
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0-0.63.build19
- Rebuild for ICU 61.1

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 0-0.62.build19
- require gcc, gcc-c++ for building
- FTBFS: build with --std=gnu++11 on ppc64le

* Thu Feb 08 2018 Hans de Goede <hdegoede@redhat.com> - 0-0.61.build19
- Update to new upstream Build19 release (rhbz#1397883)
- Strip 2012 and older changelog entries

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0-0.60.build18
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.59.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.58.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.57.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.56.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0-0.55.build18
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0-0.54.build18
- Rebuild for glew 2.0.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.53.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0-0.52.build18
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0-0.51.build18
- Rebuild for glew 1.13

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0-0.50.build18
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.49.build18
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0-0.48.build18
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.47.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.46.build18
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0-0.45.build18
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.44.build18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 0-0.43.build18
- Update to new upstream Build18 release (rhbz#1085517)
- Rebuild for new SDL_gfx

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.42.build17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0-0.41.build17
- Rebuild for boost 1.55.0

* Tue Dec 03 2013 Nils Philippsen <nils@redhat.com> - 0-0.40.build17
- use string literals as format strings (#1037384)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0-0.39.build17
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Hans de Goede <hdegoede@redhat.com> - 0-0.38.build17
- Build with compat-lua on f20+

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.37.build17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0-0.36.build17
- Rebuild for boost 1.54.0

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0-0.35.build17
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines
