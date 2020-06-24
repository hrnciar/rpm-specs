%global man_ver_curr %(rpm -q man-pages --queryformat "%{VERSION}")
# This version number must always be taken from a gettext message
# in the section 2 or 3 man pages in the tarball.
%global man_ver_repl 4.09

Summary:        German man pages from the Linux Documentation Project
Name:           man-pages-de
Version:        1.22
Release:        9%{?dist}
License:        GPLv3+
URL:            http://manpages-de.alioth.debian.org/
Source:         http://alioth.debian.org/projects/manpages-de/download/manpages-de-%{version}.tar.xz
# Due to lack of a Debian upstream source, it can't be added to Git
Source1:        package-cleanup.1.po
Patch0:         cpio.1.po.diff

BuildArch:      noarch
Supplements:    (man-pages and langpacks-de)

BuildRequires:  bzip2
BuildRequires:  cpio
BuildRequires:  ddate
BuildRequires:  deltarpm
BuildRequires:  findutils
BuildRequires:  hostname
BuildRequires:  info
%if 0%{?fedora} < 31
BuildRequires:  isdn4k-utils
%endif
BuildRequires:  less
BuildRequires:  man-pages
BuildRequires:  nfs-utils
BuildRequires:  parted
BuildRequires:  po4a
BuildRequires:  recutils
BuildRequires:  rpm
BuildRequires:  systemd
BuildRequires:  tar
BuildRequires:  util-linux
BuildRequires:  vorbis-tools
BuildRequires:  wodim
BuildRequires:  xz
BuildRequires:  yum-utils

%description
Manual pages from the Linux Documentation Project, translated into
German.

%prep

%setup -q -n manpages-de-%{version}
%patch0
cp -p %{SOURCE1} po/man1

# some man pages are now shipped with procps-ng
pushd po/man1
rm -f {free.1.po,uptime.1.po}
mv -f rename.ul.1.po rename.1.po
mv -f cal.ul.1.po cal.1.po
popd

pushd english/links
rm -f procps.links
popd

# match the current version number of man-pages on the target system
%__sed -i.fix_ver 's|part of release %{man_ver_repl} of the Linux|part of release %{man_ver_curr} of the Linux|g' po/man*/*.po
%__sed -i.fix_ver 's|Veröffentlichung %{man_ver_repl} des Projekts|Veröffentlichung %{man_ver_curr} des Projekts|g' po/man*/*.po

# remove non-free man-pages
rm po/man2/getitimer.2.po*
rm po/man2/sysinfo.2.po*

# remove man-pages that are shipped with xz-lzma-compat.
rm po/man1/xz{diff,grep,less,more}.1.po*

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS CHANGES README
%license COPYRIGHT LICENSE
%{_mandir}/de/man?/*

%changelog
* Wed Apr 01 2020 Björn Esser <besser82@fedoraproject.org> - 1.22-9
- Remove man-pages that are shipped with xz-lzma-compat
- Update macros

* Wed Feb 26 2020 Than Ngo <than@redhat.com> - 1.22-8
- Fixed FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Mario Blättermann <mario.blaettermann@gmail.com> - 1.22-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Mario Blättermann <mario.blaettermann@gmail.com> - 1.21-1
- New upstream version

* Thu Sep 29 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.16-1
- New upstream version

* Tue Sep 13 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.15-1
- New upstream version

* Mon Jun 13 2016 Tom Callaway <spot@fedoraproject.org> - 1.12-3
- remove non-free man-pages (bz1334281)

* Sun May 29 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.12-2
- Fix upstream version of man-pages

* Wed Mar 23 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 1.11-1
- New upstream version

* Sun Feb 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.9-4
- Add Supplements: for https://fedoraproject.org/wiki/Packaging:Langpacks guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.9-2
- Rebuilt for po4a-0.47

* Sun Jul 05 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.9.1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3.g7c4902d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 1.8-2.g7c4902d
- Git checkout from 2015-03-26
- New build requirements: bzip2, deltarpm, rpm, systemd, xz, yum-utils

* Tue Oct 28 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 1.8-1
- New upstream release
- Huge patch for cpio.1.po because upstream ships a sparse version
- Readded cal.1.po, tarball contains now the BSD version ncal.1
- Readded ddate.1.po
- New build requirement: cpio

* Sun Oct 05 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 1.7-4
- Patch for cal.1.po to fix a typo
- Some %%global definitions
- Fix version number in all man-pages based files so that the string
  can be translated
- Some spec file cleanup

* Sat Oct 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.7-3
- exclude man-pages also contained in procps-ng >= 3.3.10
- Resolves: rhbz#1149306 - File conflicts with procps-ng

* Wed Sep 24 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 1.7-2
- Removed procps-ng from BR because that project now maintains
  its own translated man pages

* Sat Jul 19 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 1.7-1
- New upstream release
- New build requirement: ddate
- Renamed ncal.1.po to cal.1.po
- Removed systemd BR, the file init.1.po refers to the SysVinit man page

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 1.5-1
- New upstream release

* Mon Dec 30 2013 Mario Blättermann <mario.blaettermann@gmail.com> - 1.4-3
- Added new build requirements

* Mon Dec 23 2013 Mario Blättermann <mario.blaettermann@gmail.com> - 1.4-2
- Added systemd build requirement to let init.1 be translated
- Removed man-db from BR

* Fri Nov 15 2013 Mario Blättermann <mario.blaettermann@gmail.com> - 1.4-1
- New upstream version

* Fri Nov 15 2013 Mario Blättermann <mario.blaettermann@gmail.com> - 1.3-1
- Switch to new project homepage and new sources
- Remove the patches
- No file conflicts witch man-db anymore
- Changed license from GPL+ to GPLv3+
- Some spec cleanup

* Thu Jul 25 2013 Adel Gadllah <adel.gadllah@gmail.com> - 0.5-10
- Really fix directory ownership

* Thu Jul 25 2013 Adel Gadllah <adel.gadllah@gmail.com> - 0.5-9
- Fix directory ownership

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug  5 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.5-4
- delete man pages conflicting with man-db (#583731)
- convert COPYRIGHT README to utf8

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 07 2007 Marcela Maslanova <mmaslano@redhat.com> 0.5-2
- 451337 fix license and vendor

* Wed Mar 07 2007 Marcela Maslanova <mmaslano@redhat.com> 0.5-1
- merge review, update on new version
- rhbz#226123

* Wed Jul 26 2006 Ivana Varekova <varekova@redhat.com> 0.4-11
- fix bug 196453 - remove newgrp.1 man page

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Aug  5 2005 Ivana Varekova <varekova@redhat.com> 0.4-10
- fix bug 141160 - ps 5 man page problem
- fix bug 156262 - nfs 5 man page typos

* Wed Sep 29 2004 Leon Ho <llch@edhat.com>
- rebulit
              
* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Akira TAGOH <tagoh@redhat.com> 0.4-7
- removed apropos.1, man.1, whatis.1, and man.config.5, because the latest man contains those manpages.

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 0.4-6
- Convert all manpages to utf-8.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.4-5
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.4-4
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 13 2002 Trond Eivind Glomsrřd <teg@redhat.com> 0.4-1
- 0.4

* Tue Aug 14 2001 Tim Powers <timp@redhat.com>
- rebuilt to hopefully fix rpm verify problem

* Mon Aug 13 2001 Trond Eivind Glomsrřd <teg@redhat.com>
- Rebuild (should fix #51677)

* Thu Aug  2 2001 Trond Eivind Glomsrřd <teg@redhat.com>
- Own /usr/share/man/de

* Thu May 31 2001 Trond Eivind Glomsrřd <teg@redhat.com>
- 0.3
- Added URL, changed location
- Remove --local-file option from the German man(1) (#39211)

* Sun Apr  8 2001 Trond Eivind Glomsrřd <teg@redhat.com>
- Remove hostname.1, it's now part of net-tools

* Tue Apr  3 2001 Trond Eivind Glomsrřd <teg@redhat.com>
- Some fixes to the roff sources (#34183)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Mon Jun 19 2000 Matt Wilson <msw@redhat.com>
- defattr root

* Sun Jun 11 2000 Trond Eivind Glomsrřd <teg@redhat.com>
- use %%{_mandir} and %%{_tmppath} 

* Mon May 15 2000 Trond Eivind Glomsrřd <teg@redhat.com>
- first build
