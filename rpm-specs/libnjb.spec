# SPEC file for libnjb, primary target is the Fedora Extras
# RPM repository.

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		libnjb
Version:	2.2.7
Release:	21%{?dist}
Summary:	A software library for talking to the Creative Nomad Jukeboxes and Dell DJs
URL:		http://libnjb.sourceforge.net/

Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:	BSD
BuildRequires:  gcc
BuildRequires:	libusb-devel
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	doxygen
BuildRequires:	systemd

%description
This package provides a software library for communicating with the
Creative Nomad Jukebox line of MP3 players.

%package examples
Summary:        Example programs for libnjb
Requires:       %{name} = %{version}-%{release}

%description examples
This package provides example programs for communicating with the
Creative Nomad Jukebox and Dell DJ line of MP3 players.

%package devel
Summary:        Development files for libnjb
Requires:       %{name} = %{version}-%{release}
# doc subpackage removed in newer releases, and included
# in the -devel package.
Provides:	libnjb-doc
Obsoletes:	libnjb-doc <= 2.2-1
Requires:	libusb-devel
Requires:	zlib-devel
Requires:	ncurses-devel

%description devel
This package provides development files for the libnjb
library for Creative Nomad/Zen/Jukebox and Dell DJ line of MP3 players.

%prep
%setup -q

%build
%configure --disable-static --program-prefix=njb-
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT pkgdocdir=%{_pkgdocdir}
# Remove libtool archive remnant
rm -f $RPM_BUILD_ROOT%{_libdir}/libnjb.la
# Install udev rules file.
install -p -D -m0644 libnjb.rules $RPM_BUILD_ROOT%{_udevrulesdir}/60-libnjb.rules
# Copy documentation to a good place
install -p -m 644 AUTHORS ChangeLog ChangeLog-old FAQ \
        INSTALL HACKING $RPM_BUILD_ROOT%{_pkgdocdir}
# Touch generated files to make them always have the same time stamp.
touch -r configure.ac \
      $RPM_BUILD_ROOT%{_pkgdocdir}/html/* \
      $RPM_BUILD_ROOT%{_includedir}/*.h \
      $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc
# Remove the Doxygen HTML documentation, this get different
# each time it is generated and thus creates multiarch conflicts.
# I don't want to pre-generate it but will instead wait for upstream
# to find a suitable solution that will always bring the same files,
# or that Doxygen is fixed not to do this.
#rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/*.so.*
%{_udevrulesdir}/*

%files examples
%{_bindir}/*

%files devel
%{_libdir}/*.so
%dir %{_pkgdocdir}
%{_pkgdocdir}/*
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@laptop> - 2.2.7-11
- Move rules for to %%{_udevrulesdir} (#1226702)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.2.7-8
- Additional fix for unversioned docdirs (#1106046)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 25 2011 Linus Walleij <triad@df.lth.se> 2.2.7-1
- New upstream release, fixing longstanding bug. Nuke HAL support.
* Wed Jun 15 2011 Linus Walleij <triad@df.lth.se> 2.2.6-10
- Tag libnjb devices with a specific ID for autodetection
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sat Dec 4 2010 Linus Walleij <triad@df.lth.se> 2.2.6-8
- Fix up ages old udev rules to match latest standards.
* Sat Dec 4 2010 Linus Walleij <triad@df.lth.se> 2.2.6-7
- Rebuild for new glibc, think this is good.
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Fri Jul 11 2008 Linus Walleij <triad@df.lth.se> 2.2.6-4
- Loose console permissions. See if docs build fine again.
* Sat Feb 9 2008 Linus Walleij <triad@df.lth.se> 2.2.6-3
- Rebuild for GCC 4.3.
* Wed Oct 24 2007 Linus Walleij <triad@df.lth.se> 2.2.6-2
- Flat out KILL the Doxygen HTML docs to resolve multiarch conflicts.
  Either upstream (that's me!) needs to work around the HTML files being 
  different each time OR Doxygen must stop generating anchors that
  hash the system time, creating different files with each generation.
  Pre-generating the docs is deemed silly. (Someone will disagree.)
* Wed Sep 5 2007 Linus Walleij <triad@df.lth.se> 2.2.6-1
- Long overdue upstream release.
- Shape up udev rules so they look like the libsane stuff.
- Add HAL FDI file.
* Fri Aug 17 2007 Linus Walleij <triad@df.lth.se> 2.2.5-4
- Fixup libnjb udev rules to work with new udev and HAL.
* Mon Aug 28 2006 Linus Walleij <triad@df.lth.se> 2.2.5-3
- Rebuild for Fedora Extras 6.
* Tue Feb 14 2006 Linus Walleij <triad@df.lth.se> 2.2.5-2
- Rebuild for Fedora Extras 5.
* Sun Jan 29 2006 Linus Walleij <triad@df.lth.se> 2.2.5-1
- New upstream release.
* Wed Jan 25 2006 Linus Walleij <triad@df.lth.se> 2.2.4-2
- Fix udev problem, let go of hotplug, fix console perms.
- Still working on libusb vs udev issues.
* Wed Oct 12 2005 Linus Walleij <triad@df.lth.se> 2.2.4-1
- New upstream release.
* Mon Sep 19 2005 Linus Walleij <triad@df.lth.se> 2.2.3-1
- New upstream release.
* Tue Sep 6 2005 Linus Walleij <triad@df.lth.se> 2.2.2-1
- New upstream release.
* Thu Aug 11 2005 Linus Walleij <triad@df.lth.se> 2.2.1-7
- Forgot one extraneous docdir, removing it.
* Wed Aug 10 2005 Linus Walleij <triad@df.lth.se> 2.2.1-6
- Even more fixes after more feedback from Michael.
* Tue Aug 9 2005 Linus Walleij <triad@df.lth.se> 2.2.1-5
- More fixes after feedback from Michael Schwendt.
* Sun Aug 7 2005 Linus Walleij <triad@df.lth.se> 2.2.1-4
- More fixes after feedback from Ralf Corsepius.
* Sat Aug 6 2005 Linus Walleij <triad@df.lth.se> 2.2.1-3
- Remove unnecessary macros.
* Mon Aug 1 2005 Linus Walleij <triad@df.lth.se> 2.2.1-2
- More work on Fedora compliance.
* Sat Jul 30 2005 Linus Walleij <triad@df.lth.se> 2.2.1-1
- Fedora extrafication, created a -devel package.
* Mon Jun 27 2005 Linus Walleij <triad@df.lth.se> 2.2-1
- Fixed a lot of RPM modernization for 2.2 release
* Mon May 23 2005 Linus Walleij <triad@df.lth.se> 2.1.2-1
- Interrim 2.1.2 release. Fixed program prefix.
* Fri May 13 2005 Linus Walleij <triad@df.lth.se> 2.1.1-1
- Interrim 2.1.1 release. Fixed library versioning.
* Tue May 10 2005 Linus Walleij <triad@df.lth.se> 2.1-1
- Final 2.1 release. Removed the checkings for old hotplug versions.
* Fri Mar 4 2005 Ed Welch <ed_welch@inbox.net> 2.0-1mdk
- Mandrake rpm for final 2.0 release.
* Wed Mar 2 2005 Linus Walleij <triad@df.lth.se> 2.0-1
- Final 2.0 release.
* Mon Feb 21 2005 Linus Walleij <triad@df.lth.se> 2.0-0.RC1
- Release candidate 1 for 2.0.
* Tue Feb 8 2005 Linus Walleij <triad@df.lth.se> 2.0-0.20050208
- Third CVS snapshot for the pre-2.0 series.
* Thu Jan 20 2005 Linus Walleij <triad@df.lth.se> 2.0-0.20050120
- Second CVS snapshot for the pre-2.0 series.
* Mon Jan 10 2005 Linus Walleij <triad@df.lth.se> 2.0-0.20050110
- A CVS snapshot for the first pre-2.0 series.
* Tue Nov 30 2004 Linus Walleij <triad@df.lth.se> 1.3-0.20041130
- A CVS snapshot for the new API and all.
* Wed Sep 29 2004 Linus Walleij <triad@df.lth.se> 1.2-0.20040929
- A CVS snapshot, much needed, which also works
* Fri Sep 24 2004 Linus Walleij <triad@df.lth.se> 1.2-0.20040924
- A CVS snapshot, much needed.
* Tue May 25 2004 Linus Walleij <triad@df.lth.se> 1.1-1
- Added hook to redistribute pkgconfig module
* Sun Apr 25 2004 Linus Walleij <triad@df.lth.se> 1.1-1
- Final 1.1 release!
* Wed Apr 21 2004 Linus Walleij <triad@df.lth.se> 1.0.2-0.20040421
- A new CVS snapshot.
* Fri Apr 9 2004 Linus Walleij <triad@df.lth.se> 1.0.2-0.20040409
- A new CVS snapshot.
* Sun Feb 22 2004 Linus Walleij <triad@df.lth.se> 1.0.2-0.20040222
- A new CVS snapshot. Adressing several bugs.
* Fri Jan 9 2004 Linus Walleij <triad@df.lth.se> 1.0.1-0.20040109
- A new CVS release adressing bugs, better numbering scheme
* Tue Dec 9 2003 Linus Walleij <triad@df.lth.se> 1.0.1-1
- Addressed some issues in 1.0
* Tue Dec 9 2003 Linus Walleij <triad@df.lth.se> 1.0-2
- Second package for samples
* Sat Dec 6 2003 Linus Walleij <triad@df.lth.se> 1.0-1
- Final 1.0 release
* Sun Aug 17 2003 Linus Walleij <triad@df.lth.se> 1.1.0b-6
- Seventh RPM
* Sun Aug 17 2003 Linus Walleij <triad@df.lth.se> 1.1.0b-5
- Sixth RPM
* Thu Jul 31 2003 Linus Walleij <triad@df.lth.se> 1.1.0b-4
- Fifth RPM
* Wed Jun 11 2003 Linus Walleij <triad@df.lth.se> 1.1.0b-3
- Fourth RPM.
* Mon Apr 21 2003 Linus Walleij <triad@df.lth.se> 1.1.0b-2
- Third RPM, big improvements in hotplug installation.
* Sun Mar 30 2003 Linus Walleij <triad@df.lth.se> 1.1.0b
- Second CVS RPM
* Thu Dec 26 2002 Dwight Engen <dengen40@yahoo.com> 0.9.1
- First RPM'ed
