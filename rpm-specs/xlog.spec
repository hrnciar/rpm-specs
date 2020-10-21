Name:          xlog
Version:       2.0.19
Release:       3%{?dist}
Summary:       Logging program for Hamradio Operators

License:       GPLv3
URL:           http://www.nongnu.org/xlog/
Source0:       http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:        %{name}-2.0.19-no-error.patch
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gtk2-devel
BuildRequires: hamlib-devel
BuildRequires: shared-mime-info
BuildRequires: gettext-devel
BuildRequires: desktop-file-utils

%description
xlog is a logging program for amateur radio operators. The log is stored
into a text file. QSO's are presented in a list. Items in the list can be
added, deleted or updated. For each contact, dxcc information is displayed
and bearings and distance is calculated, both short and long path.
xlog supports trlog, adif, cabrillo, edit, twlog and editest files.

%prep
%setup -q
%patch0 -p1 -b .no-error
#fix bogus .desktop file
sed -i -e "s/Utility;Database;HamRadio;GTK/Network;HamRadio;GTK/g" $RPM_BUILD_DIR/%{name}-%{version}/data/desktop/xlog.desktop
sed -i -e "s/.png//g" $RPM_BUILD_DIR/%{name}-%{version}/data/desktop/xlog.desktop

%build
autoreconf -vif
%configure CFLAGS="%{optflags} -lm" --enable-hamlib --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/mimeinfo.cache

%find_lang %{name}

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        $RPM_BUILD_ROOT%{_datadir}/applications/xlog.desktop

%files -f %{name}.lang
%doc AUTHORS data/doc/BUGS ChangeLog COPYING NEWS README data/doc/TODO data/doc/manual data/doc/KEYS data/glabels
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dxcc
%{_datadir}/%{name}/maps
%{_datadir}/pixmaps/*
%{_datadir}/icons/gnome-mime-text-x-%{name}.png
%{_datadir}/icons/%{name}-icon.png
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_mandir}/man?/*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.19-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.19-1
- New version
  Resolves: rhbz#1834548

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 2.0.13-11
- Rebuild for hamlib 4.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Richard Shaw <hobbes1069@gmail.com> - 2.0.13-2
- Rebuild for hamlib 3.1.

* Mon Feb 15 2016 Lucian Langa <lucilanga@gnome.eu.org> - 2.0.13-1
- cadd patch to deactivate Werror
- doc files packaging fixes
- drop gnomeprint BR
- update to latest upstream

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.11-4
- update mime scriptlets

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Lucian Langa <cooly@gnome.eu.org> - 2.0.11-1
- update to latest upstream
- specfile cleanup

* Tue Aug 06 2013 Lucian Langa <cooly@gnome.eu.org> - 2.0.6-3
- use unversioned doc directory

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 02 2013 Lucian Langa <cooly@gnome.eu.org> - 2.0.6-1
- fix bogus log entries
- drop missing files
- new upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.0.5-2
- Rebuild for new libpng

* Sat Mar 05 2011 Lucian Langa <cooly@gnome.eu.org> - 2.0.5-1
- new upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 30 2010 Lucian Langa <cooly@gnome.eu.org> - 2.0.4-1
- update source and URL
- new upstream release

* Sun Oct 25 2009 Lucian Langa <cooly@gnome.eu.org> - 2.0.3-3
- fix desktop file #530845

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Lucian Langa <cooly@gnome.eu.org> - 2.0.3-1
- new upstream release

* Thu Jun 25 2009 Lucian Langa <cooly@gnome.eu.org> - 2.0.2-1
- new upstream release

* Mon Mar 09 2009 Lucian Langa <cooly@gnome.eu.org> - 2.0.1-1
- new upstream release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Lucian Langa <cooly@gnome.eu.org> - 2.0-1
- add --docdir option
- remove m4 creation
- drop patch0 (fixed upstream)
- new upstream release

* Wed Dec 10 2008 Lucian Langa <cooly@gnome.eu.org> - 1.8.1-3
- modify patch to correctly display documentation

* Sun Nov 23 2008 Lucian Langa <cooly@gnome.eu.org> - 1.8.1-2
- fix for RH #472619: drop mimeinfo.cache

* Mon Sep 22 2008 Lucian Langa <cooly@gnome.eu.org> - 1.8.1-1
- new upstream versuion
- change category to HamRadio

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.7-4
- include /usr/share/xlog

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 1.7-3
- fix rh bug 458817

* Wed Jul 16 2008 Lucian Langa <cooly@gnome.eu.org> - 1.7-2
- Proper documentation packing
- Misc cleanups

* Thu Feb 28 2008 Robert 'Bob' Jensen 1.7-1
- Upstream Version bump
- Submit for review

* Mon Dec 10 2007 Robert 'Bob' Jensen 1.6.2-2
- SPEC file clean up

* Mon Dec 10 2007 Robert 'Bob' Jensen 1.6.2-1
- Upstream Version bump

* Wed Nov 28 2007 Robert 'Bob' Jensen 1.6.1-2
- License update

* Wed Nov 28 2007 Robert 'Bob' Jensen 1.6.1-1
- Upstream Version bump to solve License issue in wwl.c

* Thu Nov 22 2007 Sindre Pedersen Bjørdal <foolish@guezz.net> 1.6-3
- Fix mimeinfo scriptlet
- Add desktop-file-utils shebang
- Fix .desktop file
- Update files list
- Update license
- Add gettext and shared-mime-info BRs

* Thu Nov 22 2007 Robert 'Bob' Jensen 1.6-2
- Fix BRs

* Mon Nov 19 2007 Robert 'Bob' Jensen 1.6-1
- Current xlog 1.6 requires gtk+-2.0 >= 2.12.0
- Build xlog 1.5 for F7

* Mon Nov 19 2007 Robert 'Bob' Jensen 1.3.1-1
- Initial Fedora spec
- use Joop's spec from version 1.3.1 as a base
