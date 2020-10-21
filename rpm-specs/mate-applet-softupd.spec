# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build	1

%global	gitowner	assen-totin
%global gitproject	mate-applet-softupd

%if 0%{?rel_build}
%global ver		0.4.8
%global rlse		1
%global src		https://github.com/%{gitowner}/%{gitproject}/archive/%{ver}.tar.gz#/%{name}-%{ver}.tar.gz
%global homedir		%{gitproject}-%{ver}
%else
%global commit		e10002975b2ab664e266ce98433a4924b93e707e
%global commit_date	20190318
%global shortcommit	%(c=%{commit};echo ${c:0:7})
%global ver		0.4.8
%global rlse		0.1.git%{commit_date}.%{shortcommit}
%global src		https://github.com/%{gitowner}/%{gitproject}/archive/%{commit}.tar.gz#/%{name}-%{ver}-%{commit_date}-%{shortcommit}.tar.gz
%global homedir		%{gitproject}-%{commit}
%endif

%if 0%{?rhel} > 0 && 0%{?rhel} <= 7
%global installer	yumex
%global installer_exec	yumex
%global backend		PackageKit
%global backendreq	PackageKit-glib-devel
%else
%global installer	dnfdragora-gui
%global installer_exec	dnfdragora
%global backend		dnf
%global backendreq	%{nil}
%endif

Name:		mate-applet-softupd
Version:	%{ver}
Release:	%{rlse}%{?dist}.2
Summary:	MATE Software Update Applet
License:	GPLv2+
URL:		http://www.zavedil.com/mate-software-updates-applet/
Source:		%{src}

BuildRequires:	gcc
BuildRequires:	mate-panel-devel >= 1.3.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	gettext-devel
BuildRequires:	autoconf automake
BuildRequires:	%{backend} %{backendreq}
BuildRequires:	%{installer}
Requires:	%{backend}
Requires:	%{installer}


%description
Software updates notification applet for the MATE desktop environment.


%prep
%autosetup -n %{homedir} -p 1
./autogen.sh


%build
%configure --enable-notify=libnotify					\
	   --enable-backend=%{backend}					\
	   --enable-installer=%{installer_exec}
%{make_build}


%install
%{make_install}

#	Do not install doc files: they are handled as rpm doc files.
rm -rf $RPM_BUILD_ROOT%{_docdir}

%find_lang %{name}


%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/bin/touch --nocreate %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ]
then	/bin/touch --nocreate %{_datadir}/icons/hicolor &>/dev/null
	/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif


%files -f %{name}.lang
%doc AUTHORS BUGS COPYING ChangeLog README TODO
%{_libexecdir}/softupd_applet
%{_datadir}/pixmaps/applet_softupd_on.png
%{_datadir}/pixmaps/applet_softupd_off.png
%{_datadir}/icons/hicolor/16x16/apps/applet_softupd.png
%{_datadir}/icons/hicolor/22x22/apps/applet_softupd.png
%{_datadir}/icons/hicolor/24x24/apps/applet_softupd.png
%{_datadir}/icons/hicolor/32x32/apps/applet_softupd.png
%{_datadir}/mate-panel/applets/org.mate.applets.SoftupdApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.SoftupdApplet.service


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan  8 2020 Patrick Monnerat <patrick@monnerat.net> 0.4.8-1
- New upstream release.
- Provision git snapshot config in spec file.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar  7 2018  Patrick Monnerat <patrick@monnerat.net> 0.4.7-1
- New upstream release.
- "Modernize" spec file.
- BR gcc.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 0.4.6-1
- New upstream release
- Drop old patches, merged upstream

* Sat Mar 25 2017 Björn Esser <besser82@fedoraproject.org> - 0.4.5-1
- New upstream release
- Drop old patches, merged upstream
- Change to release tarball on github

* Fri Mar 24 2017 Björn Esser <besser82@fedoraproject.org> - 0.4.3-3
- Replace Yumex-DNF with dnfdragora
- Add patch from upstream-pr for supporting dnfdragora

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Patrick Monnerat <patrick@monnerat.net> 0.4.3-1
- New upstream release.
- Use dnf backend when available.
- Patch "nopkgkit" to remove unconditional PackageKit build requirement.
- Patch "checkdnf" to properly check for dnf backend presence.
- Use modern make install macro.
- update package-manager version logic for epel7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Patrick Monnerat <pm@datasphere.ch> 0.4.2-1
- New upstream release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  1 2015 Patrick Monnerat <pm@datasphere.ch> 0.3.0-1
- New upstream release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Patrick Monnerat <pm@datasphere.ch> 0.2.11-1
- New upstream release.
- Stop timers on applet destroy.
  https://bugzilla.redhat.com/show_bug.cgi?id=1086989

* Wed Dec 11 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.2.10-2
- Add %%{?_isa} to PackageKit Requires to avoid arch-independent deps on
  PackageKit causing multiarch conflicts (#972571).

* Mon Nov 11 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.10-1
- New upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.8-1
- New upstream release.

* Fri May 10 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.7-1
- New upstream release.

* Tue Apr 16 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.5-4
- Patch "notify" for Mate 1.6 to replace use of obsolete "libmatenotify" by
  "libnotify".

* Tue Mar 12 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.5-3
- Patch "morefrench" to add a missing french translation string.

* Mon Mar 11 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.5-2
- Update according to https://bugzilla.redhat.com/show_bug.cgi?id=919469#c2

* Fri Mar  8 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.5-1
- New upstream release.
- Patch "misc" fixes various discrepancies.

* Wed Mar  6 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.4-1
- New upstream release.
- Patch "badvarset" to fix a variable setting in configure.ac.

* Tue Mar  5 2013 Patrick Monnerat <pm@datasphere.ch> 0.2.2-1
- Initial Fedora rpm spec file.
- Patch "lmpa4" to migrate to libmatepanelapplet-4.0.
- Patch "cflags" to allow external specification of compilation/linking options.
- Patch "nowarnings" to suppress compilation warnings.
- Patch "french" to implement a french translation.
