# Review: https://bugzilla.redhat.com/show_bug.cgi?id=442270

# Review at https://bugzilla.redhat.com/show_bug.cgi?id=540034

%global git_snapshot 0

%if 0%{?git_snapshot}
%global git_rev 87c368d79eddf272cd356837256495168c5c72a2
%global git_date 20110328
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version %{git_date}git%{git_short}
%endif

# Source0 was generated as follows: 
# git clone git://lxde.git.sourceforge.net/gitroot/lxde/%{name}
# cd %{name}
# git archive --format=tar --prefix=%{name}/ %{git_short} | bzip2 > %{name}-%{?git_version}.tar.bz2

%undefine        __brp_mangle_shebangs
%undefine        _changelog_trimtime

Name:           lxde-common
Version:        0.99.2
Release:        13%{?git_version:.%{?git_version}}%{?dist}
Summary:        Default configuration files for LXDE

License:        GPLv2+
URL:            http://lxde.sourceforge.net/
%if 0%{?git_snapshot}
Source0:        %{name}-%{?git_version}.tar.bz2
%else
Source0:        http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
Source1:        lxde-lock-screen.desktop
Source2:        lxde-desktop-preferences.desktop
# Custom gtkrc
Source10:	gtkrc.custom
# Distro specific patches
Patch10:        %{name}-0.99.2-pcmanfm-config.patch
Patch11:        %{name}-0.99.2-lxpanel-config.patch
Patch12:        %{name}-0.5.5-openbox-menu.patch
Patch13:        %{name}-0.3.2.1-logout-banner.patch
Patch15:        %{name}-0.5.5-vendor.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1638808
# https://sourceforge.net/p/lxde/bugs/868/
Patch16:        %{name}-0.99.2-office-no-sal-variable.patch

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
# because of some patches:
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  intltool
Requires:       lxsession >= 0.4.0
Requires:       lxpanel pcmanfm openbox xdg-utils 
Requires:       lxmenu-data
Requires:       xorg-x11-server-utils
Requires:       xorg-x11-xinit
# needed because of new gdm
Requires:       xprop
# Use vendor's artwork
Requires:       system-logos
%if 0%{?fedora} < 9
Requires:       desktop-backgrounds-basic
%else
Requires:       desktop-backgrounds-compat
%endif
Obsoletes:      %{name}-data <= 0.3.2.1-5
# needed because the lxde-common and lxde-common-data 
# required each other with full n-v-r on F-11
Provides:       %{name} = 0.3.2.1-4.fc11
Provides:       %{name}-data = 0.3.2.1-4.fc11
BuildArch:      noarch

%description
This package contains the configuration files for LXDE, the Lightweight X11 
Desktop Environment.


%prep
%setup -q %{?git_version:-n %{name}}

%patch10 -p1 -b .orig
%patch11 -p1 -b .orig2
%patch12 -p1 -b .orig3
%patch13 -p1 -b .logout-banner
%patch15 -p1 -b .vendor
%if 0%{?fedora} >= 29
%endif
%patch16 -p1 -b .office

# Fedora >= 19 doesn't use vendor prefixes for desktop files. Instead of
# maintaining two patches we just strip the prefixes from the files we just
# patched with patch 100.
%if (0%{?fedora} && 0%{?fedora} >= 19) || (0%{?rhel} && 0%{?rhel} >= 7)
sed -i 's|id=fedora-|id=|' lxpanel/panel.in
%endif

# Calling autotools must be done before executing
# configure if needed
autoreconf -fi

%build
%configure


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL='install -p'
desktop-file-install                                           \
      --remove-key=Encoding                                    \
      --dir=%{buildroot}%{_datadir}/applications               \
      lxde-logout.desktop
desktop-file-install                                           \
      --dir=%{buildroot}%{_datadir}/applications               \
      %{SOURCE1}
# cannot use desktop-file-utils because it is out of date
install -pm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/

#install custom gtkrc
mkdir -p %{buildroot}%{_sysconfdir}/xdg/lxsession/gtk-2.0
install -cpm 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/xdg/lxsession/gtk-2.0/gtkrc


%files
%doc AUTHORS COPYING
%dir %{_sysconfdir}/xdg/lxsession/LXDE/
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/autostart
%config(noreplace) %{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf
%dir %{_sysconfdir}/xdg/lxsession/gtk-2.0
%{_sysconfdir}/xdg/lxsession/gtk-2.0/gtkrc
%dir %{_sysconfdir}/xdg/pcmanfm/
%config(noreplace) %{_sysconfdir}/xdg/pcmanfm/LXDE/pcmanfm.conf
%{_bindir}/startlxde
%{_bindir}/lxde-logout
%{_bindir}/openbox-lxde
%{_datadir}/lxde/
%config(noreplace) %{_sysconfdir}/xdg/lxpanel/LXDE
%config(noreplace) %{_sysconfdir}/xdg/openbox/LXDE
%{_mandir}/man1/*.1.gz
%{_datadir}/xsessions/LXDE.desktop
%{_datadir}/applications/lxde-*.desktop


%changelog
* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 0.99.2-13
- Require xprop not xorg-x11-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Adam Williamson <awilliam@redhat.com> - 0.99.2-11
- Change desktop.conf icon theme to Adwaita (bug 1853462)

* Thu May  7 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.99.2-10
- Install custom gtkrc to enable gtk-menu-images by default (bug 1830588)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.99.2-6
- No longer set SAL_USE_VCLPLUGIN for office (bug 1638808), F-29+ for now

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.99.2-1
- 0.99.2

* Tue Mar  1 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.99.1-1
- 0.99.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.99.0-1
- 0.99.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-0.11.20110328git87c368d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-0.10.20110328git87c368d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 26 2013  Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-0.9.20110328git87c368d7
- Fix conditional to actually apply the fix for the quicklauncher (#1028063)

* Tue Nov 26 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-0.8.20110328git87c368d7
- Fix lxpanel quicklauncher icons (#1028063)
- Remove netstat and cpu plugins from default panel config
- Minor lxpanel config file tweaks
- Improve English comment of "Lock Screen" launcher

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-0.7.20110328git87c368d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-0.6.20110328git87c368d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-0.5.20110328git87c368d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-0.4.20110328git87c368d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 11 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-0.3
- Drop pulseaudio patch (fixes #713292)

* Tue Apr 05 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-0.2
- Switch to Adwaita GTK theme

* Mon Mar 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-0.1
- Update to git snapshot to get rid of all upstreamed patches
- Fix pcmanfm config file location
- Adjust distro specific config files for F15

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4-3
- Fix backdrop-image.patch for F14 artwork (#635398)

* Sun Jun 13 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.4-2
- Adjusting autostart to respect pcmanfm 0.9.7 side rename
  (that pcmanfm2 binary was renamed to pcmanfm) (#603468)
- Explicitly call autotools before configure

* Thu Apr 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4-1
- Bump version to 0.5.4 to indicate changes for pcmanfm2
- Adjustments for recent Goddard artwork changes

* Thu Mar 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-3
- Updates for pcmanfm2

* Tue Dec 15 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-2
- Restore toggle functionality of the show deskop plugin
- Drop requirement for obsolete lxde-settings-daemon

* Fri Dec 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Tue Oct 27 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-2
- Final tweaks for the LXDE Spin

* Sat Jul 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2
- Disable OLPC keyboard shortcuts for now, they interfere with OpenOffice
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 13 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-3
- Add XO keyboard shortcuts

* Sat Jun 13 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-2
- Include logout and screenlock buttons (#503919)

* Mon May 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Mon May 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4-2
- Fix Provides to allow proper upgrade

* Tue Apr 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4-1
- Update to 0.4
- Require lxmenu-data and lxde-settings-daemon
- Drop obsolete config file /etc/xdg/lxsession/LXDE/default

* Fri Mar 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2.1-4
- Workaround for new gdm
- Add Pulseaudio support
- Add mixer plugin to the panel
- Require xdg-utils

* Fri Oct 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2.1-3
- Require fedora-icon-theme and system-logos

* Thu Oct 09 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2.1-2
- Rebase patches for rpm's new fuzz=0 behaviour

* Thu Jul 10 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2.1-1
- Update to 0.3.2.1
- Switch from ROXTerm to LXterminal
- Rebased most patches
- Add mixer to the panel 

* Mon Apr 14 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0.1-2
- Make a separate package for lxde-icon-theme

* Sat Apr 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0.1-1
- Update to 0.3.0.1
- Use distros default artwork

* Sat Mar 29 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.0.0-1
- Initial Fedora RPM
- Use roxterm instead of gnome-terminal and xterm
- Patch default panel config
