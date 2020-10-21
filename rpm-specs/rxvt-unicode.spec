Name:           rxvt-unicode
Version:        9.22
Release:        25%{?dist}
Summary:        Unicode version of rxvt

License:        GPLv3
URL:            http://software.schmorp.de/
Source0:        http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2
Source1:        rxvt-unicode.desktop
Patch0:         rxvt-unicode-9.21-Fix-hard-coded-wrong-path-to-xsubpp.patch
Patch1:         rxvt-unicode-0001-Prefer-XDG_RUNTIME_DIR-over-the-HOME.patch

# for autosetup
BuildRequires:  git

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  ncurses ncurses-base ncurses-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  perl-devel, perl-generators, perl(ExtUtils::Embed)
BuildRequires:  startup-notification-devel
%if 0%{?fedora} > 13 || !0%{?rhel}
BuildRequires:  gdk-pixbuf2-devel
%endif
%if 0%{?fedora} >= 15
BuildRequires:  libev-source
%endif
Requires:       startup-notification
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# We just provide a single binary now.
Obsoletes:      rxvt-unicode-ml <= 9.22-17
Obsoletes:      rxvt-unicode-256color <= 9.22-17
Obsoletes:      rxvt-unicode-256color-ml <= 9.22-17

# There's only one rxvt in the distro; this is the last one
Obsoletes:      rxvt <= 2.7.10-36

%description
rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%autosetup -S git

%if 0%{?fedora} >= 15
rm -rf libev
ln -s %{_datadir}/libev-source libev
%endif

%build
%configure \
 --enable-keepscrolling \
 --enable-selectionscrolling \
 --enable-pointer-blank \
 --enable-utmp \
 --enable-wtmp \
 --enable-lastlog \
 --enable-unicode3 \
 --enable-combining \
 --enable-xft \
 --enable-font-styles \
%if 0%{?fedora} > 13
 --enable-pixbuf \
%endif
 --enable-transparency \
 --enable-fading \
 --enable-rxvt-scroll \
 --enable-next-scroll \
 --enable-xterm-scroll \
 --enable-perl \
 --enable-mousewheel \
 --enable-xim \
 --with-codesets=all \
 --enable-slipwheeling \
 --enable-smart-resize \
 --enable-frills \
 --disable-iso14755 \
 --enable-startup-notification \
 --enable-256-color \
 --with-term=rxvt-unicode-256color

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# install desktop files
desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
  --vendor=fedora \
%endif
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# create compat symlinks
pushd $RPM_BUILD_ROOT/%{_bindir}
ln -s urxvt rxvt
ln -s urxvt urxvt-ml
ln -s urxvtc urxvt-mlc
ln -s urxvtd urxvt-mld
ln -s urxvt urxvt256c
ln -s urxvtc urxvt256cc
ln -s urxvtd urxvt256cd
ln -s urxvt urxvt256c-ml
ln -s urxvtc urxvt256c-mlc
ln -s urxvtd urxvt256c-mld
popd

%files
%doc README.FAQ
%doc INSTALL
%doc doc/README.xvt
%doc doc/etc
%doc doc/changes.txt
%license COPYING
%{_bindir}/rxvt
%{_bindir}/urxvt
%{_bindir}/urxvtc
%{_bindir}/urxvtd
%{_bindir}/urxvt-ml
%{_bindir}/urxvt-mlc
%{_bindir}/urxvt-mld
%{_bindir}/urxvt256c
%{_bindir}/urxvt256cc
%{_bindir}/urxvt256cd
%{_bindir}/urxvt256c-ml
%{_bindir}/urxvt256c-mlc
%{_bindir}/urxvt256c-mld
%{_mandir}/man1/urxvt.1*
%{_mandir}/man1/urxvtc.1*
%{_mandir}/man1/urxvtd.1*
%{_mandir}/man1/urxvt-background.1*
%{_mandir}/man1/urxvt-bell-command.1*
%{_mandir}/man1/urxvt-block-graphics-to-ascii.1*
%{_mandir}/man1/urxvt-clipboard-osc.1*
%{_mandir}/man1/urxvt-confirm-paste.1*
%{_mandir}/man1/urxvt-digital-clock.1*
%{_mandir}/man1/urxvt-eval.1*
%{_mandir}/man1/urxvt-example-refresh-hooks.1*
%{_mandir}/man1/urxvt-extensions.1*
%{_mandir}/man1/urxvt-keysym-list.1*
%{_mandir}/man1/urxvt-kuake.1*
%{_mandir}/man1/urxvt-matcher.1*
%{_mandir}/man1/urxvt-option-popup.1*
%{_mandir}/man1/urxvt-overlay-osc.1*
%{_mandir}/man1/urxvt-readline.1*
%{_mandir}/man1/urxvt-remote-clipboard.1*
%{_mandir}/man1/urxvt-searchable-scrollback.1*
%{_mandir}/man1/urxvt-selection-autotransform.1*
%{_mandir}/man1/urxvt-selection-pastebin.1*
%{_mandir}/man1/urxvt-selection-popup.1*
%{_mandir}/man1/urxvt-selection-to-clipboard.1*
%{_mandir}/man1/urxvt-selection.1*
%{_mandir}/man1/urxvt-tabbed.1*
%{_mandir}/man1/urxvt-xim-onthespot.1*
%{_mandir}/man3/urxvtperl.3*
%{_mandir}/man7/urxvt.7*
%{_datadir}/applications/*rxvt-unicode.desktop
%{_libdir}/urxvt

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 9.22-24
- Perl 5.32 rebuild

* Wed Apr 15 2020 Robbie Harwood <rharwood@redhat.com> - 9.22-23
- Restore accidentally remove 256 color capability
- Resolves: #1824204

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Robbie Harwood <rharwood@redhat.com> - 9.22-21
- Correctly package previous symlink and update obsoletes versions

* Fri Jan 03 2020 Robbie Harwood <rharwood@redhat.com> - 9.22-20
- Obsolete and provide compat symlinks for rxvt

* Tue Dec 03 2019 Robbie Harwood <rharwood@redhat.com> - 9.22-19
- Correct symlinks
- Resolves: #1777912

* Wed Oct 30 2019 Robbie Harwood <rharwood@redhat.com> - 9.22-18
- Drop the -terminfo subpackage after coordination with ncurses.

* Thu Oct 24 2019 Robbie Harwood <rharwood@redhat.com> - 9.22-17
- Merge all {,256}{,ml} variants into one package (with compat symlinks)
- Resolves: #1669302
- Resolves: #1732589

* Wed Oct 23 2019 Robbie Harwood <rharwood@redhat.com> - 9.22-16
- Enable startup notifications
- Resolves: #1428830

* Sun Oct 13 2019 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 9.22-15
- split terminfo into noarch package (rhbz#949921)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 9.22-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Björn Esser <besser82@fedoraproject.org> - 9.22-11
- Add BuildRequires: gcc-c++, fixes FTBFS (#1606287)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 9.22-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 9.22-7
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 9.22-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 9.22-2
- Perl 5.24 rebuild

* Thu Feb 25 2016 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- version upgrade

* Wed Feb 17 2016 Till Maas <opensource@till.name> - 9.21-8
-  Do not overwrite CFLAGS or LDFLAGS with make, they are already set by
   %%configure and -lfontconfig is added in upstream Makefile. Overwriting
   LDFLAGS breaks hardening as PIE.
- Use %%license

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 9.21-5
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 9.21-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 03 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 9.21-3
- update license to GPLv3

* Sat Jan 03 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 9.21-2
- add patch from Maciej Borzecki to fix gnome-shell matching
  (rhbz#1031368)

* Fri Jan 02 2015 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 9.21-1
- version upgrade (rhbz#830236)

* Wed Dec 17 2014 Peter Lemenkov <lemenkov@gmail.com> - 9.20-6
- Don't use HOME for storing control socket. Use XDG directory instead.

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 9.20-5
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 9.20-2
- There is no need for the patches below, as they change the behavior of our
  package and break the principle of least astonishment.
- Remove Fedora-specific patch to scroll up/down one line. Any users wanting
  this behavior can create their own key bindings.
- Remove Fedora-specific patch to open new tabs with Control-t. Any users
  wanting this behavior can create their own key bindings.
- The popular 'tabbed' extension can now work properly (#1096791).

* Thu May 01 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 9.20-1
- update to upstream release 9.20, which includes a fix for security bug
  CVE-2014-3121 (#1093287, #1093288, #1093289)
- include man pages for new extension (selection-to-clipboard)

* Thu Oct 31 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.19-1
- version upgrade

* Tue Sep 10 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.18-5
- fix tabbed extension

* Sun Aug 18 2013 Paul Howarth <paul@city-fan.org> - 9.18-4
- fix xsubpp path leading to FTBFS (#993374)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 9.18-2
- Perl 5.18 rebuild

* Tue Mar 26 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.18-1
- version upgrade

* Wed Mar 20 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.17-1
- version upgrade

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 9.16-3
- Remove vendor from desktop files for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.16-1
- version upgrade
- cleanup manpages

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 9.15-2
- Perl 5.16 rebuild

* Sun Jan 22 2012 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.15-1
- version upgrade

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.14-1
- version ugprade
- drop screen patch (upstream)
- disable libAfterImage as it is deprecated

* Fri Nov 18 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.12-5
- use icon from fd.org standard (rhbz#754939)

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 9.12-4
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 9.12-3
- Perl mass rebuild

* Wed Jul 06 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.12-2
- fix segfault (rhbz#711137)

* Mon Jul 04 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.12-1
- version upgrade
- fix key definition (rhbz#718506)

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 9.10-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.10-2
- switch back to shift scroll (#667980)
- open new tab on Ctrl+t
- build with libev-source on f15+ (#672396)

* Sun Dec 19 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.10-1
- version upgrade

* Mon Nov 29 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.09-4
- include terminfo for 256color version for now

* Thu Nov 18 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.09-3
- re-add frills build option for standard versions
- bind scrolling actions to crtl+up/down/pgup/pgdown as shift will break the
  tabbing support

* Mon Nov 15 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.09-2
- Rework to provide four versions:
- standard (rxvt-unicode)
- multi-language support (rxvt-unicode-ml)
- 256color version (rxvt-unicode-256color)
- 256color multi-language (rxvt-unicode-256color-ml)

* Sun Nov 14 2010 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.09-1
- version upgrade (fixes #581373)
- allow scrolling with mod+up/down (#510944)
- fixup desktop file (#617519)
- spec file cleanups

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 9.07-2
- Mass rebuild with perl-5.12.0

* Thu Dec 31 2009 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.07-1
- version upgrade

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 9.06-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 9.06-3
- Fix FTBFS: added rxvt-unicode-gcc44.patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.06-1
- version upgrade

* Mon Jun 16 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.05-1
- version upgrade

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com>
- 9.02-2
- add Requires for versioned perl (libperl.so)

* Thu Feb 21 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.02-1
- version upgrade

* Mon Feb 11 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de> - 9.0-2
- Rebuilt for gcc43

* Sat Jan 26 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.0-1
- version upgrade

* Thu Dec 27 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.9-1
- version upgrade

* Mon Dec 17 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.8-1
- version upgrade

* Wed Dec 12 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.5a-2
- remove utempter patch for now

* Thu Nov 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.5a-1
- version upgrade

* Wed Nov 07 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.4-2
- fix #368921 (Rxvt.backgroundPixmap needs libAfterImage support BR now)
- add patch for utempter support

* Sun Oct 28 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.4-1
- version upgrade

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.3-1
- version upgrade
- new license tag

* Sat Jun 02 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.2-1
- version upgrade (#239421)

* Sun Jan 21 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.1-2
- drop terminfo file it is included in ncurses now

* Fri Dec 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.1-1
- version upgrade

* Thu Nov 02 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.0-1
- version upgrade

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.9-2
- FE6 rebuild

* Tue Aug 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.9-1
- version upgrade

* Tue Jul 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.8-1
- version upgrade

* Tue Feb 21 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.7-1
- version upgrade

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.6-2
- Rebuild for Fedora Extras 5

* Fri Feb 10 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.6-1
- version upgrade

* Tue Jan 31 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.5-1
- version upgrade

* Sat Jan 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.4-1
- version upgrade

* Fri Jan 27 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.3a-1
- version upgrade

* Mon Jan 23 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.2-1
- version upgrade (should resolve #178561)

* Thu Jan 19 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.1-1
- version upgrade

* Sat Jan 14 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.0-1
- version upgrade

* Thu Jan 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.3-1
- version upgrade

* Tue Jan 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.2-1 
- version upgrade

* Wed Dec 28 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.1-1
- version upgrade

* Sun Dec 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.0-1
- version upgrade

* Sun Dec 18 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.9-1
- version upgrade

* Fri Nov 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.8-2
- modular xorg integration

* Tue Oct 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.8-1
- version upgrade

* Sun Oct 16 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-3
- enable frills (#170965)

* Sat Sep 17 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-2
- enable iso14755 (#168548)

* Tue Aug 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-1
- version upgrade

* Sun Jun 05 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-3
- add dist

* Thu Jun 02 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-2
- minor cleanups

* Thu May 12 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-1
- Version upgrade (5.5)

* Mon Mar 28 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:5.3-1
- Version upgrade (5.3)

* Wed Feb 09 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- Initial RPM release.
