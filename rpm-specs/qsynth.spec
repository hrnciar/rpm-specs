Summary:       Qt based Fluidsynth GUI front end
Name:          qsynth
Version:       0.6.2
Release:       1%{?dist}
URL:           http://qsynth.sourceforge.net
Source0:       http://downloads.sourceforge.net/qsynth/qsynth-%{version}.tar.gz

Patch0:        qsynth-fedora-defaults.patch
License:       GPLv2+
Requires:      hicolor-icon-theme
Requires:      soundfont2-default

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fluidsynth-devel
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-linguist

%description
QSynth is a fluidsynth GUI front-end application written in C++ around the Qt4
toolkit using Qt Designer. Eventually it may evolve into a softsynth management
application allowing the user to control and manage a variety of command line
softsynth but for the moment it wraps the excellent FluidSynth. FluidSynth is a
command line software synthesizer based on the Soundfont specification.

%prep
%setup -q
%patch0 -p1 -b .defaults

iconv --from=ISO88591 --to=UTF8 AUTHORS -o AUTHORS.tmp
touch -r AUTHORS AUTHORS.tmp
mv -f AUTHORS.tmp AUTHORS

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make DESTDIR=%{buildroot} install -C %{_target_platform}

# manpage
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -a qsynth.1 %{buildroot}/%{_mandir}/man1/

# appdata file
mkdir -p %{buildroot}/%{_datadir}/appdata/
cp -a src/appdata/qsynth.appdata.xml %{buildroot}/%{_datadir}/appdata/

# desktop file
desktop-file-install \
  --add-category="X-Synthesis" \
  %{buildroot}%{_datadir}/applications/qsynth.desktop

# Handle locale's
%find_lang %{name} --with-qt

# remove duplicate
rm %{buildroot}%{_datadir}/appdata/qsynth.appdata.xml

%files -f qsynth.lang
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/qsynth
%dir %{_datadir}/qsynth/
%dir %{_datadir}/qsynth/translations/
%{_datadir}/applications/qsynth.desktop
%{_datadir}/icons/hicolor/32x32/apps/qsynth.png
%{_datadir}/icons/hicolor/scalable/apps/qsynth.svg
%{_mandir}/*/man1/qsynth*
%{_datadir}/metainfo/qsynth.appdata.xml
%{_mandir}/man1/qsynth.1.gz



%changelog
* Sun Jun 21 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.6.2-1
- New version

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.5.4-5
- Rebuild against fluidsynth2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.5.4-1
- Update to 0.5.4

* Sun Nov 25 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.5.3-1
- Update to 0.5.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.5.0-1
- Update to 0.5.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.4.3-1
- Update to 0.4.3

* Tue May 24 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.4.1-1
- Update to 0.4.1. Drop upstreamed patch.

* Sat Feb 13 2016 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.4.0-1
- Update to 0.4.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.8-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Nov 29 2014 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.8-1
- Update to 0.3.8

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.7-1
- Update to 0.3.7

* Sun Feb 10 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.6-4
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/24
- some specfile cleanup

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 09 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.6-1
- Update to 0.3.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun May 09 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.5-1
- Update to 0.3.5

* Sat Feb 13 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.4-3
- Fix DSO linking failure RHBZ#564615
- Clean up the specfile from bits related to Fedora < 11

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 12 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.4-1
- Update to 0.3.4
- Update specfile for macro consistency
- Own %%{_datadir}/qsynth/locale
- Drop patches that are no longer needed

* Wed Apr 22 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.3.3-6.1
- Fix disttag comparison for F9

* Sat Apr 18 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.3-6
- Set Fedora defaults

* Fri Apr 17 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.3-5
- Fix locale path (#494470)
- Fix mixed spaces&tabs warnings
- Preserve timestamp of the file AUTHORS
- Replace %%define with %%global per new guidelines

* Fri Apr 10 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.3.3-4
- Fix close button not shown with Qt 4.5 (#494470)

* Sun Mar 22 2009 Robert Scheck <robert@fedoraproject.org> 0.3.3-3
- Rebuilt without %%{?_smp_mflags} as it isn't supported

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep  5 2008 Michel Salim <salimma@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2.5-8
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.5-7
- Autorebuild for GCC 4.3

* Thu Sep 14 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.5-6
- mass rebuild
- added hicolor-icon-theme requirement

* Tue Jul 25 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.5-5
- fluidsynth build dependency in extras changed to fluidsynth-devel

* Sun Jun 18 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.5-4
- move icon to freedesktop location, don't use makeinstall macro, add
  icon cache scripts, fill in missing releases in changelog entries,
  fix source url

* Thu Jun  8 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.5-3
- more tweaks for Fedora Extras, move desktop file to source1

* Fri May 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.5-2
- spec file tweaks for Fedora Extras submission

* Wed May  3 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.5-2
- add Planet CCRMA desktop categories

* Wed Apr  5 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.5-1
- updated to 0.2.5

* Fri Mar 31 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.4-1
- add fc5 dependencies

* Fri Nov 18 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.4-1
- updated to 0.2.4

* Tue Jun 28 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3-1
- updated to 0.2.3

* Wed Dec 29 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-1
- spec file cleanup

* Mon Oct 11 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.2-1
- updated to 0.2.2
- bitmap is now png instead of xpm
- fix typo in desktop_vendor define

* Fri Sep 24 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.1-1
- updated to 0.2.1

* Wed May 12 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-1
- added buildrequires

* Sun Feb 29 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-1
- updated to 0.1.3

* Wed Jan 21 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- updated to 0.1.0

* Wed Nov 26 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.2-1
- updated to 0.0.2
- use fmod when building under 7.3 (patch0)

* Wed Nov 26 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.1-1
- initial build
