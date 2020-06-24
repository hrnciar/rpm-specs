Name:           xarchon
Version:        0.50
Release:        33%{?dist}
Summary:        Arcade board game
License:        GPL+
URL:            http://xarchon.seul.org/
Source0:        http://xarchon.seul.org/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         %{name}-fonts.patch
Patch1:         %{name}-destdir.patch
Patch2:         http://ftp.debian.org/debian/pool/main/x/%{name}/%{name}_0.50-10.1.diff.gz
Patch3:         xarchon-0.50-gcc43.patch
BuildRequires:  gcc gcc-c++ gtk+-devel esound-devel libXpm-devel
BuildRequires:  desktop-file-utils ImageMagick libappstream-glib
Requires:       hicolor-icon-theme

%description
XArchon is a chess with a twist board game.


%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}
convert -resize 64x64 data/icon.xpm %{name}.png


%install
%make_install INSTALL="install -p"

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_mandir}/man6/%{name}.6.gz


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Hans de Goede <hdegoede@redhat.com> - 0.50-31
- Fix FTBFS (rhbz#1676225)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.50-27
- Remove obsolete scriptlets

* Sun Jan 14 2018 Hans de Goede <hdegoede@redhat.com> - 0.50-26
- Re-enable esound support, it is the only supported sound output (#1534185)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Hans de Goede <hdegoede@redhat.com> - 0.50-22
- Add appdata

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.50-20
- drop esound support

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 0.50-18
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.50-14
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Hans de Goede <hdegoede@redhat.com> 0.50-9
- Update description for new trademark guidelines

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.50-7
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.50-6
- Fix compilation with gcc 4.3

* Fri Aug 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.50-5
- Update Debian patch set to 0.50-10.1

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.50-4
- Rebuild for buildId
- Update license tag for new license tag guidelines compliance

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.50-3  
- FE6 Rebuild

* Sat May 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.50-2
- consistent use of %%{name} (everywhere).
- Add BR: libXPM-devel
- Drop NEWS from %%doc as it contains no relevant information.

* Thu May 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.50-1
- Pick xarchon up from Ville and submit it for Review as Ville doens't
  have the time for this.

* Tue Mar 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.50-0.2
- Fix build with gcc >= 3.4 (partially from Debian).
- Install icon to %%{_datadir}/icons/hicolor.

* Sat May 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.50-0.1
- Rebuild for FC4.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.50-0.fdr.3
- Install data into %%{_datadir}/games/xarchon.
- Remove #---- section markers.

* Sun Jun  1 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.50-0.fdr.2
- Spec cleanups.

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.50-0.fdr.1
- Update to current Fedora guidelines.

* Fri Feb  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.50-1.fedora.1
- First Fedora release.
