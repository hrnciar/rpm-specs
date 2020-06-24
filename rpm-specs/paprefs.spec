Name:           paprefs
Version:        1.1
Release:        6%{?dist}
Summary:        Management tool for PulseAudio

License:        GPLv2+
URL:            http://freedesktop.org/software/pulseaudio/%{name}
Source0:        http://freedesktop.org/software/pulseaudio/%{name}/%{name}-%{version}.tar.xz
Patch0:         0001-Fix-ustring-initialization-from-a-NULL-pointer.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtkmm30-devel
BuildRequires:  lynx
BuildRequires:  meson
BuildRequires:  pulseaudio-libs-devel

Requires:       pulseaudio-module-gsettings
Suggests:       PackageKit-session-service
Suggests:       gnome-packagekit-common

%description
PulseAudio Preferences (paprefs) is a simple GTK based configuration dialog
for the PulseAudio sound server.

%prep
%autosetup -p1

%build
%meson -Dlynx=true
%meson_build

%install
%meson_install

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%license LICENSE
%doc %{_target_platform}/doc/README
%{_bindir}/paprefs
%dir %{_datadir}/paprefs
%{_datadir}/paprefs/paprefs.glade
%{_datadir}/applications/paprefs.desktop


%changelog
* Mon Apr 27 2020 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-6
- Fix crash when attempting to install a module using a patch from upstream git
  (RH #1715245)

* Thu Apr 09 2020 Michael J Gruber <mjg@fedoraproject.org> - 1.1-5
- remove (indirect) KDE dependency (bz #1754307)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.1-1
- Update to 1.1
- Drop upstreamed patch
- Drop dbus-glib BuildRequires

* Thu Nov 15 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.0-2
- Added Suggests: gnome-packagekit-common in an attempt to fix rh #1627765

* Mon Jul 30 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1.0-1
- Update to 1.0
- Port module-combine-sink patch to 1.0
- Drop upstreamed modules-path.patch
- Fix incorrect dates in %%changelog
- Switch to meson
- Clean up and modernise the .spec file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.10-9
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 01 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.10-6
- Use module-combine-sink instead of module-combine

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.10-3
- Pulled some changes from upstream git to avoid a rebuild every PA release (RH #870899)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.10-1
- Incorporate changes from Julian Sikorski (belegdol) (#827764):
  * update to 0.9.10
  * update URL and source fields; switch to xz tarball
  * drop obsoleted Group, Buildroot, %%clean and %%defattr
- Further spec clean-ups (buildroot-cleanup-on-install, indentation)
- Hard-coded dependency on build-time PulseAudio version dropped

* Thu May 17 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.9-12
- rebuild(pulseaudio)

* Sun Feb  5 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.9-11
- Make pulseaudio runtime dependency versioned

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.9-9
- Rebuild for pulseaudio 0.9.23 (F-16) / 1.1 (F-17)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Lubmir Rintel <lkundrak@v3.sk> 0.9.9-7
- Rebuild for pulseaudio-0.9.22

* Tue Feb 23 2010 Rex Dieter <rdieter@fedoraproject.org> 0.9.9-6
- Requires: PackageKit-session-service (#561437)

* Mon Jan 25 2010 Lennart Poettering <lpoetter@redhat.com> 0.9.9-5
- Rebuild to make sure we look for /usr/lib/pulse-0.9.21/modules/xxx instead of /usr/lib/pulse-0.9.19/modules/xxx
- https://bugzilla.redhat.com/show_bug.cgi?id=528557

* Wed Oct 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-4
- Fix mistag

* Wed Oct 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-3
- Rebuild to make sure we look for /usr/lib/pulse-0.9.19/modules/xxx instead of /usr/lib/pulse-0.9.16/modules/xxx

* Thu Sep 10 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-2
- Final 0.9.9 release

* Tue Aug 25 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-1.git20090825
- Add dbus-glib to deps

* Tue Aug 25 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.9-0.git20090825
- Snapshot

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.8-1
- Update to 0.9.8

* Sun Mar 15 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.9.7-5
- Try harder when looking for modules

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 9 2008 Matthias Clasen <mclasen@redhat.com> 0.9.7-3
- Handle locales properly

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.7-2
- Include intltool in deps

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.7-1
- Update to 0.9.7

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.6-4
- Include unowned directory /usr/share/paprefs

* Thu Mar 27 2008 Christopher Aillon <caillon@redhat.com> - 0.9.6-3
- Add compile patch for GCC 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.6-2
- Autorebuild for GCC 4.3

* Wed Nov 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> 0.9.6-1
- Update to 0.9.6

* Tue Sep 25 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.6-0.2.svn20070925
- Update SVN snapshot

* Thu Aug 16 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.6-0.1.svn20070816
- Get snapshot from SVN

* Mon Jul 2 2007 Eric Moret <eric.moret@epita.fr> 0.9.5-2
- Update license field

* Wed Jan 10 2007 Eric Moret <eric.moret@epita.fr> 0.9.5-1
- Initial package for Fedora
