Summary:       Qt based JACK control application
Name:          qjackctl
Version:       0.6.2
Release:       1%{?dist}
URL:           http://qjackctl.sourceforge.net
Source0:       http://downloads.sourceforge.net/qjackctl/files/%{name}-%{version}.tar.gz
License:       GPLv2+
Requires:      hicolor-icon-theme

Source20:      qmake-qt5.sh

# Appdata fix. Upstreamable
Patch0:        qjackctl-appdata-fix.patch

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: portaudio-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtx11extras-devel

%description
Qjackctl is a simple application to control the JACK sound server daemon,
specific for the Linux Audio Desktop infrastructure. It provides a simple GUI
dialog for setting several JACK daemon parameters, which are properly saved
between sessions, and a way to control the status of the audio server daemon.
With time, this primordial interface has become richer by including a enhanced
patchbay and connection control features.

%prep
%setup -q
%patch0 -p1 -b .appdata_fix

# configure hard-codes prepending searches of /usr (already implicit, causes problems),
# and /usr/local (not needed here), so force it's non-use -- rex
sed -i.ac_with_paths -e "s|^ac_with_paths=.*|ac_with_paths=|g" configure


%build
CFLAGS="%{optflags}"; export CFLAGS
CXXFLAGS="%{optflags}"; export CXXFLAGS
LDFLAGS="%{?__global_ldflags}"; export LDFLAGS

# force use of custom/local qmake, to inject proper build flags (above)
install -m755 -D %{SOURCE20} bin/qmake-qt5
PATH=`pwd`/bin:%{_qt5_bindir}:$PATH; export PATH

%configure \
           --enable-jack-version \
           --localedir=%{_datadir}/%{name}/locale/

make %{?_smp_mflags} QMAKE=`pwd`/bin/qmake-qt5

%install
make DESTDIR=%{buildroot} install

desktop-file-install \
  %{buildroot}%{_datadir}/applications/qjackctl.desktop

# Handle locale's
%find_lang %{name} --with-qt

%files -f qjackctl.lang
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/qjackctl
%dir %{_datadir}/qjackctl/
%{_datadir}/icons/hicolor/32x32/apps/qjackctl.png
%{_datadir}/icons/hicolor/scalable/apps/qjackctl.svg
%{_datadir}/applications/qjackctl.desktop
%{_mandir}/man1/%{name}*
%{_datadir}/metainfo/qjackctl.appdata.xml

%changelog
* Sun Jun 21 2020 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.6.2-1
- New version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.5-2
- Appdata fix

* Sun Nov 25 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.5-1
- New version

* Tue Sep 25 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.4-1
- New version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Remove obsolete scriptlets

* Fri Jan 05 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.0-1
- New version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.4-1
- New version

* Tue May 24 2016 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.2-1
- New version

* Fri Feb 19 2016 Rex Dieter <rdieter@fedoraproject.org> 0.4.1-2
- workaround configure hard-coding /usr

* Thu Feb 18 2016 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.1-1
- New version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0.3.12-4
- use qmake-qt4 wrapper to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.12-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Nov 29 2014 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.12-1
- New version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.10-1
- New version

* Sun Feb 10 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3.9-4
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/24
- some specfile cleanup

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.9-2
- Re-enable parallel build

* Fri May 18 2012 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.9-1
- New version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 02 2011 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.8-1
- New version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.7-1
- New version. Drop upstreamed patch.
- Some cleanup in he specfile.
- Enable portaudio support.

* Fri Mar 12 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.6-1
- New version

* Sat Feb 13 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.5-3
- Fix DSO linking

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.3.5-2
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Fri Oct 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.5-1
- Update to 0.3.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 0.3.4-1
- Update to 0.3.4
- Update scriptlets according to the new guidelines
- Use %%global instead of %%define per new guidelines
- Fix locale dir
- Fix mixed tabs&spaces issues

* Fri Apr 10 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.3.3-3
- Fix close button not shown with Qt 4.5 (#494471)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 08 2008 Anthony Green <green@redhat.com> 0.3.3-1
- Upgrade source.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.1a-6
- Autorebuild for GCC 4.3

* Mon Nov 12 2007 Anthony Green <green@redhat.com> 0.3.1a-5
- Force use of qmake-qt4 again.  I'm getting closer.

* Mon Nov 12 2007 Anthony Green <green@redhat.com> 0.3.1a-4
- Force use of qmake-qt4 again.

* Mon Nov 12 2007 Anthony Green <green@redhat.com> 0.3.1a-3
- Force use of qmake-qt4.

* Mon Nov 12 2007 Anthony Green <green@redhat.com> 0.3.1a-2
- Fix BuildRequires for qt4.

* Mon Nov 12 2007 Anthony Green <green@redhat.com> 0.3.1a-1
- New upstream.
- Tweak License.

* Thu Sep 14 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.20-7
- fixed typo in patch filename

* Thu Sep 14 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.20-6
- mass rebuild
- added patch to add support for freebob backend (thanks to Anthony Green)
- added hicolor-icon-theme requirement

* Sun Jun 18 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.20-5
- move icon to freedesktop location, don't use makeinstall macro, add
  icon cache scripts

* Wed May 17 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.20-4
- more extras spec file cleanup

* Fri May 12 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.20-3
- spec file cleanup for Fedora Extras, added desktop-file-utils
  to build requirements (not there in Fedora's build system)

* Wed May  3 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.20-2
- added Planet CCRMA desktop categories

* Mon Mar 27 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.20-1
- updated to 0.2.20

* Mon Jan 23 2006 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.19a-1
- updated to 0.2.19a

* Tue Jun 21 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.17-1
- updated to 0.2.17

* Tue Feb  8 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.15-2
- added fix from Rui for segfaults

* Sun Feb  6 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.15-1
- updated to 0.2.15
- keep jackstart as the default startup program for kernel 2.4.x

* Sun Jan 23 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.14-1
- updated to 0.2.14

* Thu Dec 16 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- spec file tweaks

* Sun Dec  5 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.13-1
- updated to 0.2.13

* Mon Oct 11 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.12a-1
- updated to 0.2.12a

* Wed Sep 22 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.11-1
- updated to 0.2.11

* Sun Jul  4 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.9-1
- updated to 0.2.9

* Fri Apr 30 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.8-1
- updated to 0.2.8

* Wed Apr 21 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.7b-1
- updated to 0.2.7b

* Mon Feb 16 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.5-1
- updated to 0.2.5

* Thu Feb  5 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.4-1
- updated to 0.2.4

* Wed Jan 21 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.3a-1
- updated to 0.2.3a

* Fri Dec 12 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.0-1
- updated to 0.2.0

* Wed Nov 26 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.3-1
- updated to 0.1.3

* Tue Nov 18 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.2-1
- updated to 0.1.2

* Thu Oct 30 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.1-1
- updated to 0.1.1

* Fri Oct 10 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.9a-1
- updated to 0.0.9a

* Thu Sep 25 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.9-1
- updated to 0.0.9 (release often indeed!)

* Mon Sep 22 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.8-1
- updated to 0.0.8
- added explicit jack version requirement

* Mon Sep 15 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.7-1
- updated to 0.0.7

* Fri Sep  5 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.5-1
- updated to 0.0.5

* Fri Aug 29 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.4-1
- updated to 0.0.4, updated release tags

* Fri Aug  8 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.3-1
- updated to 0.0.3

* Wed Aug  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.2-1
- updated to 0.0.2

* Wed Jul 30 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.0.1-1
- initial build
