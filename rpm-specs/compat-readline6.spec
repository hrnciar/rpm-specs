Summary: A library for editing typed command lines
Name: compat-readline6
Version: 6.3
Release: 19%{?dist}
License: GPLv3+
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz

Patch5: readline6.3-upstream-patches1-6.patch
# add workaround for problem in gdb
# in new version of readline needs to be deleted
# bz701131
Patch8: readline-6.2-gdb.patch
# fix file permissions, remove RPATH, use CFLAGS
Patch9: readline-6.2-shlib.patch
Patch10: readline-6.3-config.patch

Requires(post): info
Requires(preun): info
BuildRequires:  gcc
BuildRequires: ncurses-devel
BuildRequires: git

%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

%package devel
Summary: Files needed to develop programs which use the readline library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: ncurses-devel%{?_isa}
Requires(post): info
Requires(preun): info

%description devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.

%package static
Summary: Static libraries for the readline library
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
The readline-static package contains the static version of the readline
library.

%prep
%autosetup -n readline-%{version} -p1

%build
export CPPFLAGS="-I%{_includedir}/ncurses"
%configure
%make_build

%install
%make_install

# Move stuff under private dirs to not conflict with original subpackage
mkdir %{buildroot}%{_libdir}/readline6
mv %{buildroot}%{_libdir}/*.{a,so} %{buildroot}%{_libdir}/readline6/
pushd %{buildroot}%{_libdir}/readline6
  for f in *.so; do
    ln -sf ../$f.6 $f
  done
popd
mv %{buildroot}%{_includedir}/readline{,6}

rm -rf %{buildroot}%{_datadir}/readline
rm -rf %{buildroot}%{_docdir}/readline

rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_mandir}

%ldconfig_scriptlets

%files
%license COPYING
%doc CHANGES NEWS README USAGE
%{_libdir}/libreadline.so.6*
%{_libdir}/libhistory.so.6*

%files devel
%{_includedir}/readline6/
%{_libdir}/readline6/libreadline.so
%{_libdir}/readline6/libhistory.so

%files static
%{_libdir}/readline6/libreadline.a
%{_libdir}/readline6/libhistory.a

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 6.3-18
- Fix configure test for MUST_REINSTALL_SIGLHANDLERS
  compromised by LTO

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Siteshwar Vashisht <svashisht@redhat.com> - 6.3-10
- Fix requires tag for static subpackage

* Wed Jan 11 2017 Siteshwar Vashisht <svashisht@redhat.com> - 6.3-9
- Create compatibility package for Readline 6
  Related: #1376611

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 13 2015 Miroslav Lichvar <mlichvar@redhat.com> 6.3-7
- fix building with new rpm
- rebuild for new ncurses

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Tom Callaway <spot@fedoraproject.org> - 6.3-4
- fix license handling

* Tue Jul 22 2014 jchaloup <jchaloup@redhat.com> - 6.3-3
- related: #1071336
  new rebase for readline 6.3

* Wed Jul  2 2014 Paul Howarth <paul@city-fan.org> - 6.3-2
- resolves: #1115432
  fix 0003-add-TTY-input-audit-support.patch not to revert readline version
  number to 6.2

* Thu Jun 19 2014 Jan Chaloupka <jchaloup@redhat.com> - 6.3-1
- resolves: #1071336
  rebase 6.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 jchaloup <jchaloup@redhat.com> - 6.2-9
- resolves: #1077026
  Security patch for debug functions

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Lukáš Nykrýn <lnykryn@redhat.com> - 6.2-7
- fix aarch64 build (#926433)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Lukas Nykryn <lnykryn@redhat.com> 6.2-4
- temporary fix for problem with gdb, wait for y/n (#701131)

* Wed Aug 31 2011 Lukas Nykryn <lnykryn@redhat.com> 6.2-3
- isxdigit is no longer defined as macro ic c++ (#723299)

* Tue Mar 01 2011 Miroslav Lichvar <mlichvar@redhat.com> 6.2-2
- include patch 001

* Tue Feb 15 2011 Miroslav Lichvar <mlichvar@redhat.com> 6.2-1
- update to 6.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Miroslav Lichvar <mlichvar@redhat.com> 6.1-3
- include patches 001, 002 (#657758)
- add TTY input audit support (#244350)

* Wed Feb 17 2010 Lubomir Rintel <lkundrak@v3.sk> 6.1-2
- fix the version number in header

* Tue Jan 12 2010 Miroslav Lichvar <mlichvar@redhat.com> 6.1-1
- update to 6.1

* Tue Aug 25 2009 Miroslav Lichvar <mlichvar@redhat.com> 6.0-3
- include patch 004
- suppress install-info errors (#515910)
- remove dir* in infodir after install (#492097)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Miroslav Lichvar <mlichvar@redhat.com> 6.0-1
- update to 6.0
- include patches 001, 002, 003

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Mar 23 2008 Jan Kratochvil <jan.kratochvil@redhat.com> - 5.2-13
- Fix the previous %%changelog entry authorship.

* Sun Mar 23 2008 Jan Kratochvil <jan.kratochvil@redhat.com> - 5.2-12
- Fix excessive prompts on CTRL-C abort while the prompt is being printed.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.2-11
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Miroslav Lichvar <mlichvar@redhat.com> 5.2-10
- move libreadline to /lib

* Thu Jan 03 2008 Miroslav Lichvar <mlichvar@redhat.com> 5.2-9
- include upstream patches 008-011

* Mon Nov 05 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-8
- fix cursor position when prompt has one invisible character (#358231)
- merge review fixes (#226361)
- fix source URL

* Mon Aug 27 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-7
- include patches 005, 006, 007

* Wed Aug 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-6
- update license tag

* Tue May 29 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-5
- include patches 5.2-003, 5.2-004

* Thu Mar 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-4
- apply 5.2-002 patch

* Thu Mar 15 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-3
- link libreadline with libtinfo (#232277)
- include upstream 5.2-001 patch
- move static libraries to -static subpackage, spec cleanup

* Thu Nov 30 2006 Miroslav Lichvar <mlichvar@redhat.com> 5.2-2
- require ncurses-devel instead of libtermcap-devel

* Mon Nov 13 2006 Miroslav Lichvar <mlichvar@redhat.com> 5.2-1
- update to 5.2 (#213795)
- use CFLAGS when linking (#199374)
- package docs and examples (#172497)
- spec cleanup

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.1-1.1
- rebuild

* Mon Jul 10 2006 Jindrich Novy <jnovy@redhat.com> 5.1-1
- update to readline-5.1
- apply new proposed upstream patches for 5.1 (001-004)
- drop "read -e" patch, applied upstream

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.0-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.0-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 5.0-3
- Rebuild for new GCC.

* Tue Jan 18 2005 Tim Waugh <twaugh@redhat.com> 5.0-2
- Fix line-wrapping (bug #145329).
- Apply "read -e" patch from bash package.

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 5.0-1
- 5.0 (bug #144835).

* Mon Nov 29 2004 Tim Waugh <twaugh@redhat.com> 4.3-14
- Added URL tag (bug #141106).

* Thu Sep  2 2004 Jeremy Katz <katzj@redhat.com> - 4.3-13
- rebuild so that static linking against readline will work on ppc64 
  without dot symbols

* Mon Jun 28 2004 Tim Waugh <twaugh@redhat.com> 4.3-12
- Build requires libtool (bug #126589).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Nov 28 2003 Thomas Woerner <twoerner@redhat.com> 4.3-9
- removed rpath

* Thu Nov  6 2003 Tim Waugh <twaugh@redhat.com> 4.3-8
- Apply upstream patches (bug #109240 among others).

* Wed Jun 25 2003 Tim Waugh <twaugh@redhat.com>
- devel package requires libtermcap-devel (bug #98015).

* Wed Jun 25 2003 Tim Waugh <twaugh@redhat.com> 4.3-7
- Fixed recursion loop (bug #92372).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst
- BuildRequires autoconf only

* Wed Aug 07 2002 Phil Knirsch <pknirsch@redhat.com> 4.3-3
- Fixed Esc-O-M stack overflow bug.

* Mon Jul 22 2002 Phil Knirsch <pknirsch@redhat.com> 4.3-1
- Updated to latest readline release 4.3

* Thu Jul 11 2002 Phil Knirsch <pknirsch@redhat.com> 4.2a-7
- Fixed problem with alpha build.

* Wed Jul 10 2002 Phil Knirsch <pknirsch@redhat.com>
- Fixed utf8 problem (originally observed in bash).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 4.2a-6
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com> 4.2a-5
- automated rebuild

* Wed Mar 20 2002 Trond Eivind Glomsrød <teg@redhat.com> 4.2a-4
- Use autoconf 2.53, not 2.52

* Mon Mar  4 2002 Bernhard Rosenkraenzer <bero@redhat.com> 4.2a-3
- Rebuild

* Mon Nov 26 2001 Matt Wilson <msw@redhat.com> 4.2a-2
- removed the manual symlinking of .so, readline handles this by itself
- call only %%makeinstall, not %%makeinstall install install-shared as
  this makes bogus .old files in the buildroot

* Tue Nov 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 4.2a-1
- 4.2a

* Tue Oct  2 2001 Bernhard Rosenkraenzer <bero@redhat.com> 4.2-4
- Work around autoconf bug

* Mon Oct  1 2001 Bernhard Rosenkraenzer <bero@redhat.com> 4.2-3
- Don't use readline's internal re-implementation of strpbrk on systems
  that have strpbrk - the system implementation is faster and better maintained.

* Tue Aug  7 2001 Bernhard Rosenkraenzer <bero@redhat.com> 4.2-2
- Make sure headers can be included from C++ applications (#51131)
  (Patch based on Debian's with the bugs removed ;) )

* Wed May 09 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 4.2 and adapt patches

* Fri Apr  6 2001 Nalin Dahyabhai <nalin@redhat.com>
- change the paths listed for the header files in the man page to reflect
  the location changes from previous versions (#35073)
- note that "on" is acceptable instead of "On" in the man page (#21327)

* Thu Mar  8 2001 Preston Brown <pbrown@redhat.com>
- fix reading of end key termcap value (@7 is correct, was kH) (#30884)

* Tue Jan 30 2001 Nalin Dahyabhai <nalin@redhat.com>
- mark the man page as currently out-of-date (#25294)

* Thu Sep  7 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging (64bit systems need to use libdir).

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- summaries from specspo.

* Wed Aug  2 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- use "rm -f" in specfile

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun  5 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Tue Mar 21 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 4.1

* Thu Feb 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 4.0

* Fri Apr 09 1999 Michael K. Johnson <johnsonm@redhat.com>
- added guard patch from Taneli Huuskonen <huuskone@cc.helsinki.fi>

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.2.1

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- don't package /usr/info/dir

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- added proper sonames

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- updated to readline 2.1

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc
