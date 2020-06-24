Summary: Zile Is Lossy Emacs
Name: zile
Version: 2.4.14
Release: 5%{?dist}
License: GPLv3+
URL: http://www.gnu.org/software/%{name}/
Source0: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: ncurses-devel gc-devel help2man autoconf automake

%description
Zile is a small Emacs clone. Zile is a customizable, self-documenting
real-time open-source display editor. Zile was written to be as
similar as possible to Emacs; every Emacs user should feel at home.

%prep
%autosetup

iconv -f iso-8859-1 -t utf-8 -o THANKS{.utf8,}
touch -r THANKS{,.utf8}
mv THANKS{.utf8,}

%build
autoreconf --force --install
%configure
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
# Remove unversioned doc directory; doc files will be installed into
# versioned doc directory by doc directive in files section.
rm -rf $RPM_BUILD_ROOT/usr/share/doc/zile

%files
%doc AUTHORS ChangeLog NEWS README THANKS FAQ src/dotzile.sample
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 15 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.14-1
- update to new upstream release 2.4.14, fixes rhbz #1504463
- spec cleanup and modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.13-1
- Rebuilt for new upstream release 2.4.13, fixes rhbz #1385997

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Eric Smith <eric@brouhaha.com> - 2.4.11-1
- Updated to 2.4.11

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Eric Smith <eric@brouhaha.com> - 2.4.9-1
- Updated to 2.4.9

* Mon Apr 29 2013 Eric Smith <eric@brouhaha.com> - 2.3.21-9
- Added --install option to autoreconf.

* Mon Apr 29 2013 Eric Smith <eric@brouhaha.com> - 2.3.21-8
- Added missing BuildRequires for autoconf, automake.

* Mon Apr 29 2013 Eric Smith <eric@brouhaha.com> - 2.3.21-7
- Add autoreconf in prep section to support aarch64 (Bug #926862).

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 2.31.21-5
- Fix gets call for glibc-2.16 changes

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 2.3.21-1
- Updated to 2.3.21

* Mon Jul 05 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 2.3.17-1
- Updated to 2.3.17

* Mon May 17 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 2.3.16-1
- Updated to 2.3.16

* Mon May 03 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 2.3.15-1
- Updated to 2.3.15

* Fri Dec 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 2.3.14-1
- Updated to 2.3.14

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 2.3.9-1
- Updated to 2.3.9

* Mon Apr 13 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 2.3.6-1
- Updated to 2.3.6 (Check changelog for details)
- Added help2man in BuildRequires and adjusted %%files

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 2.3.0-1
- Updated to 2.3.0

* Thu Aug 14 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 2.2.61-2
- Fixed License, Required field & macro inconsistency
- Latest release 2.2.61

* Mon Aug 11 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 2.2.61-1
- Latest release 2.2.59
- fixed license  and THANKS file encoding

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 2.2.19-4
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.19-3
- Autorebuild for GCC 4.3

* Wed Dec 12 2007 Miroslav Lichvar <mlichvar@redhat.com> - 2.2.19-2
- Remove libtermcap-devel from BuildRequires (#231199).

* Mon Sep 11 2006 Jeff Carlson <jeff@ultimateevil.org> - 2.2.19-1
- Bump to latest release.

* Fri Apr 28 2006 Jeff Carlson <jeff@ultimateevil.org> - 2.2.13-2
- Bump to rebuild

* Thu Apr 27 2006 Jeff Carlson <jeff@ultimateevil.org> - 2.2.13-1
- Bump to latest release.

* Wed Aug 24 2005 Jeff Carlson <jeff@ultimateevil.org> - 2.2.4-2
- Another BuildRequires.

* Thu Aug 18 2005 Jeff Carlson <jeff@ultimateevil.org> - 2.2.4-1
- Bump to latest release.
- Supposed to fix x86_64 crash.

* Thu Aug 18 2005 Jeff Carlson <jeff@ultimateevil.org> - 2.2.1-5
- Caught another BuildRequires.

* Thu Aug 18 2005 Jeff Carlson <jeff@ultimateevil.org> - 2.2.1-4
- Added missed BuildRequires.

* Fri Aug 12 2005 Jeff Carlson <jeff@ultimateevil.org> - 2.2.1-3
- Multiple fixups recommended by spot.

* Wed Jul 13 2005 Jeff Carlson <jeff@ultimateevil.org> - 2.2.1-2
- Don't package "dir" in infodir.

* Wed Jul 13 2005 Jeff Carlson <jeff@ultimateevil.org> - 2.2.1-1
- Initial build.

