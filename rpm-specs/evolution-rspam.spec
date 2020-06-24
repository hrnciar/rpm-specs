Name: evolution-rspam
Summary: Evolution Plugin for reporting spam
Version: 0.6.0
Release: 28%{?dist}
License: GPLv2+
Source: http://gnome.eu.org/%{name}-%{version}.tar.xz
URL: http://gnome.eu.org/evo/index.php/Report_as_Spam

Patch0: evolution-rspam-0.6.0-evo38.patch
Patch1: evolution-rspam-0.6.0-convert-fix.patch
Patch2: evolution-rspam-0.6.0-globals-clash.patch
Patch3: evolution-rspam-0.6.0-evo312.patch
Patch4: evolution-rspam-0.6.0-evo313.patch
Patch5: evolution-rspam-0.6.0-evo3136.patch
Patch6: evolution-rspam-0.6.0-source-double-unref.patch
Patch7: evolution-rspam-0.6.0-activity-leak.patch
Patch8: evolution-rspam-0.6.0-evo3_23_2.patch

Requires: perl-Razor-Agent
Requires: pyzor
Requires: evolution

BuildRequires: gettext, evolution-devel, perl(XML::Parser), intltool, GConf2-devel
BuildRequires: autoconf, automake, gnome-common, libtool

%description
Rspam Evolution Plugin enables Evolution Mail client to report email messages
as spam to checksum-based and statistical filtering networks.
It supports Razor network, DCC, SpamCop and Pyzor.
This plugins requires a pretty new version of evolution to build.
See README for more information about required programs.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .evo38
%patch1 -p1 -b .convert-fix
%patch2 -p1 -b .globals-clash
%patch3 -p1 -b .evo312
%patch4 -p1 -b .evo313
%patch5 -p1 -b .evo3136
%patch6 -p1 -b .source-double-unref
%patch7 -p1 -b .activity-leak
%patch8 -p1 -b .evo3_23_2

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name \*\.la -print | xargs rm -f
%find_lang rspam

# remove old GConf schemas
#find $RPM_BUILD_ROOT/%{_sysconfdir}/gconf/schemas -name '*.schemas' -exec rm {} \;

%files -f rspam.lang
%{_datadir}/GConf/gsettings/evolution-rspam.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.evolution-rspam.gschema.xml
%{_datadir}/evolution/ui/*.ui
%{_libdir}/evolution/plugins/org-gnome-sa-rspam.eplug
%{_libdir}/evolution/plugins/liborg-gnome-sa-rspam.so
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc NEWS
%doc README
%doc TODO

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Milan Crha <mcrha@redhat.com> - 0.6.0-26
- Rebuild for newer evolution-data-server

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.6.0-25
- Remove obsolete requirements for %%post/%%pre/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Milan Crha <mcrha@redhat.com> - 0.6.0-22
- Rebuild for newer evolution-data-server

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 0.6.0-21
- Rebuilt for evolution-data-server soname bump

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Milan Crha <mcrha@redhat.com> - 0.6.0-17
- Add a patch to build against evolution-data-server 3.23.2

* Mon Sep 26 2016 Milan Crha <mcrha@redhat.com> - 0.6.0-16
- Build against latest evolution, to drop dependency on webkitgtk3

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 0.6.0-15
- Rebuild for newer evolution-data-server

* Thu Jun 30 2016 Milan Crha <mcrha@redhat.com> - 0.6.0-14
- Add patch for RH bug #1350887 (Reporting spam leaks Activity and Message)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 19 2015 Milan Crha <mcrha@redhat.com> - 0.6.0-12
- Add patch for RH bug #1254256 (ESource double unref)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 Milan Crha <mcrha@redhat.com> - 0.6.0-10
- Add patch to a build break against evolution 3.13.3
- Add patch to a build break against evolution 3.13.6
- Rebuild against newer evolution (changed folder structure)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Milan Crha <mcrha@redhat.com> - 0.6.0-7
- Add patch to build break against evolution 3.12

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 02 2013 Milan Crha <mcrha@redhat.com> - 0.6.0-5
- Add patch for Red Hat bug #886881 (global variable clash with evolution-rss)

* Thu May 02 2013 Milan Crha <mcrha@redhat.com> - 0.6.0-4
- Add patch for Red Hat bug #887246 (.convert file causes crash of GConf)

* Fri Feb 22 2013 Milan Crha <mcrha@redhat.com> - 0.6.0-3
- Add patch to be buildable against evolution 3.7.90

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 12 2012 Lucian Langa <cooly@gnome.eu.org> - 0.6.0-1
- new upstream release

* Thu Aug 09 2012 Lucian Langa <cooly@gnome.eu.org> - 0.5.0-1
- new upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Lucian Langa <cooly@gnome.eu.org> - 0.4.0-1
- drop path - fixed upstream
- new upstream release

* Fri Jun 24 2011 Milan Crha <mcrha@redhat.com> - 0.3.0-2
- Adapt to recent evolution release

* Fri May 13 2011 Lucian Langa <cooly@gnome.eu.org> - 0.3.0-1
- new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Lucian Langa <cooly@gnome.eu.org> - 0.2.0-1
- drop patch1 - fixed upstream
- new upstream release

* Mon Oct 11 2010 Milan Crha <mcrha@redhat.com> - 0.1.1-1
- update to 0.1.1 upstream release
- add patch to build against evolution-data-server 2.91.0

* Fri Jul 09 2010 Lucian Langa <cooly@gnome.eu.org> - 0.1.0-1
- new upstream release

* Fri Jul 02 2010 Lucian Langa <cooly@gnome.eu.org> - 0.0.99-3.20100702git
- update to latest git snapshot

* Wed Apr 28 2010 Lucian Langa <cooly@gnome.eu.org> - 0.0.99-2.20100428git
- update to latest git snapshot

* Wed Jan 06 2010 Lucian Langa <cooly@gnome.eu.org> - 0.0.99-1.20100106git
- update to latest git snapshot

* Thu Sep 03 2009 Lucian Langa <cooly@gnome.eu.org> - 0.0.10-1
- drop patch0 (fixed upstream)
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 06 2009 Lucian Langa <cooly@gnome.eu.org> - 0.0.8-3
- fix for bug #492319

* Fri Mar 20 2009 Lucian Langa <cooly@gnome.eu.org> - 0.0.8-2
- update BR

* Tue Mar 17 2009 Lucian Langa <cooly@gnome.eu.org> - 0.0.8-1
- update to 0.0.8 release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.0.6-4
- fix for #458818

* Mon Jul 14 2008 Lucian Langa <lucilanga@gnome.org> - 0.0.6-3
- misc cleanups

* Wed Jul 09 2008 Lucian Langa <lucilanga@gnome.org> - 0.0.6-2
- package name change
- misc cleanups

* Tue Feb 12 2008 Lucian Langa <lucilanga@gnome.org> - 0.0.6-1
- buildroot and url updates

* Sun Jan 27 2008 Lucian Langa <lucilanga@gnome.org>
- Updated to fedora build requires

* Tue Mar 13 2007 cooly <cooly@mips.edu.ms>
- Updated description

* Sun Feb 04 2007 root <root@mayday>
- Initial spec file created by autospec ver. 0.8 with rpm 3 compatibility
