# Font-lock support of message bodies was added (Source1) from 
# http://de.geocities.com/ulf_jasper/emacs.html on 10th February 2007.

# Note on building VM with support for bbdb: if support for VM in BBDB is
# required, then the source elisp for VM must be installed at build time. If
# support for BBDB is required in VM, then the BBDB source elisp must be present
# at build time. Hence there is a circular BuildRequires and bootstrapping is
# required. The way to do this is (i) build emacs-vm without BuildRequires:
# emacs-bbdb (ii) build emacs-bbdb with BuildRequires: emacs-vm (iii)
# rebuild emacs-vm with BuildRequires: emacs-bbdb. Or vice versa.
%global bbdbsupport 1

%global pkgdir %{_emacs_sitelispdir}/vm
%global etcdir %{_datadir}/emacs/vm
%global pixmapdir %{etcdir}/pixmaps
%global initfile %{_emacs_sitestartdir}/vm-mode-init.el

Summary: Emacs VM mail reader
Summary(sv): Emacs postläsare VM
Name: emacs-vm
Version: 8.2.0
%global date 20190602
Release: 0.5.%{date}bzr%{?dist}
License: GPLv2+
URL: https://launchpad.net/vm
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  bzr branch lp:vm emacs-vm-YYYYMMDD
#  tar --exclude=.bzr -cJf emacs-vm-YYYYMMDD.tar.xz emacs-vm-YYYYMMDD
Source0: %{name}-%{date}.tar.xz
Source1: emacs-vm.metainfo.xml

Requires: emacs(bin) >= %{_emacs_version}
BuildRequires: autoconf
BuildRequires: gcc
BuildRequires: emacs texinfo texinfo-tex
BuildRequires: libappstream-glib

%if %{bbdbsupport}
BuildRequires: emacs-bbdb
Requires: emacs-bbdb
%endif

%description
VM (View Mail) is an Emacs subsystem that allows UNIX mail to be read
and disposed of within Emacs.  Commands exist to do the normal things
expected of a mail user agent, such as generating replies, saving
messages to folders, deleting messages and so on.  There are other
more advanced commands that do tasks like bursting and creating
digests, message forwarding, and organizing message presentation
according to various criteria. 

%description -l sv
VM (View Mail) är ett undersystem för Emacs som gör att UNIX e-post
kan läsas och hanteras inifrån Emacs.  Det finns kommandon för att
göra de vanliga sakerna som förväntas av ett postprogram, såsom skapa
svar, spara meddelanden till mappar, radera meddelanden och så vidare.
Det finns andra mer avancerade kommandon som gör saker som att
splittra upp eller skapa sammandrag, vidarebefordra meddelanden och
organisera presentationen av meddelanden enligt olika kriterier.

%prep
%autosetup -n %{name}-%{date}
# The documentation is in Latin 1, but "makeinfo" apparently requires
# UTF-8 nowadays.
# https://bugs.launchpad.net/vm/+bug/1861896
iconv --from-code=ISO-8859-1 --to-code=UTF-8 -o vm.texinfo info/vm.texinfo
mv vm.texinfo info

%build
autoconf
%configure --with-etcdir=%{etcdir} --with-docdir=%{_pkgdocdir}
make

%install
make install DESTDIR=%{buildroot}

# Copy source lisp files into buildroot
(cd lisp ; install -p -m 644 *.el %{buildroot}%{pkgdir})

# Create initialization file.
install -d %{buildroot}/%{_emacs_sitestartdir}
cat > %{buildroot}/%{initfile} <<EOF
;; Startup settings for VM
(setq vm-toolbar-pixmap-directory "%{pixmapdir}")
(setq vm-image-directory "%{pixmapdir}")
(require 'vm-autoloads)

;; Settings for u-vm-color.el 
(require 'u-vm-color)
(add-hook 'vm-summary-mode-hook 'u-vm-color-summary-mode)
(add-hook 'vm-select-message-hook 'u-vm-color-fontify-buffer)

(defadvice vm-fill-paragraphs-containing-long-lines
    (after u-vm-color activate)
    (u-vm-color-fontify-buffer))
EOF
# Metainfo
install -d %{buildroot}%{_datadir}/metainfo
cp -p %{SOURCE1} %{buildroot}%{_datadir}/metainfo

%check
appstream-util validate-relax --nonet \
	       %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%doc README.headers-only
%doc %{_infodir}/*
%license COPYING
%{_bindir}/*
%{pkgdir}
%{etcdir}
%{_pkgdocdir}
%{initfile}
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
* Tue Feb  4 2020 Göran Uddeborg <goeran@uddeborg.se> - 8.2.0-0.5.20190602bzr
- Convert the vm.texinfo file to UTF-8, current texinfo seems to require that.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-0.4.20190602bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-0.3.20190602bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun  2 2019 Göran Uddeborg <goeran@uddeborg.se> - 8.2.0-0.2.20190602bzr
- Upgrade to latest BZR.  Fixes boguous questions about external viewer when
  showing bounce messages.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-0.2.20180911bzr
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Göran Uddeborg <goeran@uddeborg.se> - 8.2.0-0.1.20180911bzr
- Upgrade to 8.2.x branch.  It is formally under "development", but works
  better than the 8.1.2 "stable" version.
- Drop all patches as they are fixed in the new version.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-22
- Emacs lisp fix for extraneous &optional; became an error in emacs 26
- Use the autosetup macro to prepare.

* Sat Jun 16 2018 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-21
- Remove texinfo scriptlets, they are no longer needed.

* Sun Feb 18 2018 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-20
- Add an explicit build requirement on gcc.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-18
- Metainfo added.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug  2 2016 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-14
- Avoid URL-decoding the "body" of a mailto URL twice.

* Tue Mar 22 2016 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-13
- Reviewed and updated script requires. (BZ #1319108)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-8
- Use more modern browsers in menus and defaults. (BZ #968056)

* Mon May 20 2013 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-7
- Remove some duplicates in the files section.
- Remove clean section no longer needed.
- Remove defattr declaration no longer needed.
- Swedish translation of summary and description added.
- Update comments to reflect that .el files are now included in the base
  package rather than the -el subpackage.
- The Obsoletes/Provides declaration for the -el subpackage are no longer
  needed in F20.

* Sun May 19 2013 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-6
- Patch texinfo files so they can be formatted with texinfo 5.

* Wed May 15 2013 Göran Uddeborg <goeran@uddeborg.se> - 8.1.2-5
- Apply upstreams patch to fit changed signature of mail-user-agent (Bz 960295)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun  5 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.1.2-2
- Change BuildRequires for emacs-bbdb-el to emacs-bbdb

* Wed May 30 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.1.2-1
- Update to version 8.1.2
- Remove separate emacs-vm-el sub-package to comply with updated 
  packaging guidelines

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar  8 2011 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.1.1-3
- Replace define with global in macro definitions

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 26 2010 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.1.1-1
- Update to version 8.1.1
- Fix source URL

* Thu Apr  1 2010 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.1.0-1
- Update to version 8.1.0 final
- Remove -fno-var-tracking-assignments from CFLAGS once more

* Tue Feb  9 2010 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.1.0-0.3.beta2
- Add missing version.txt file to file list

* Tue Feb  9 2010 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.1.0-0.2.beta2
- Update to 8.1.0-beta2

* Sat Dec 26 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.1.0-0.1.beta
- Update to 8.1.0 beta version

* Sat Dec 26 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.14-2
- Add -fno-var-tracking-assignments to CFLAGS to allow build to complete (gcc
  bug http://gcc.gnu.org/PR41371)

* Fri Dec 18 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.14-1
- Update to 8.0.14
- Drop old macros for emacspackaging and use _emacs macros
- Remove BuildRoot definition
- No longer delete buildroot at beginning of install

* Wed Sep 16 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.12-6
- Bump release to fix up cvs problem

* Wed Sep 16 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.12-5
- Add patch to fix charset recognition with emacs 23
- Bump minimum emacs to version 23.1
- Rebuild against emacs 23.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec  3 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.12-3
- Add patch to make vm-decode-postponed-mime-message autoloaded (BZ 474728)

* Wed Nov 19 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.12-2
- Re-add u-vm-color.el to lisp/Makefile.in
- Fix spec file typo in install command that installs the uncompiled lisp files

* Fri Nov  7 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.12-1
- Update to version 8.0.12
- Remove u-vm-color.el (now included with upstream VM)
- Remove hack to add vm-revno.el to lisp files
- Drop devo number stuff, since upstream seems to have stopped using the
  revision number in the release tarball name (finally!) 

* Mon Sep 29 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.11.581-2
- Add vm-revno.el to lisp files

* Sat Sep 27 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.11.581-1
- Update to 8.0.11-581

* Wed Jul 30 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.10.575-1
- Update to version 8.0.10-575
- Update BuildRoot to preferred mktemp variant

* Sun Mar 23 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.9.544-1
- Update to 8.0.9-544
- Update u-vm-color.el to version 2.10
- Remove patch needed for 8.0.7

* Tue Feb 12 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.7.522-2
- Bump release and rebuild for GCC 4.3

* Sun Jan 13 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.7.522-1
- Update to version 8.0.7-522
- Add patch to fix correct display of redistributed flag (BZ #428248)

* Sun Nov 18 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.5.504-2
- Add -p option to install when copying source elisp files into buildroot to
  preserve mtimes (BZ #389081)

* Sun Nov 11 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.5.504-1
- Update to version 8.0.5
- Remove patch to fix Makefile from 8.0.3

* Sat Oct 13 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.3.495-7
- Fix typo in emacs_startdir macro
- Add ability to build with BBDB support

* Sun Sep  9 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.3.495-6
- Fix typo with start file creation

* Sun Sep  9 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.3.495-5
- Add BuildRequires: emacs since emacs-el doesn't pull this in

* Sat Sep  8 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.3.495-4
- Update for agreement with packaging guidelines - add versioned
  emacs requirement
- If no pkg-config is found, revert to sensible defaults

* Thu Aug 30 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.3.495-3
- Fix problem with vm-autoloads.el RH BZ #262361 

* Wed Aug 22 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.3.495-2
- Add BuildRequires: texinfo-tex to ensure building of pdf docs

* Tue Aug 21 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.3.495-1
- Update to release 8.0.3

* Mon Aug  6 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.2.482-4
- Bump release
- Fix previous changelog entry

* Sat Aug  4 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.2.482-3
- Clarify license

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 8.0.2.482-2
- Rebuild for RH #249435

* Sun Jul 22 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.2.482-1
- Update to bugfix release 8.0.2

* Thu Jun 28 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.1.465-1
- Update to bugfix release 8.0.1 (fixes BZ #245780)

* Tue Jun 26 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.0.453-1
- Ensure files in /usr/bin have exec bit set properly (BZ #245740)

* Tue Jun 19 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 8.0.0.453-1
- Update to version 8.0.0 devo 453 which removes the need for thr vmrf patch
- No longer need to bundle vcard stuff as that is included upstream
- Spec file cleanups
- No longer use separate pixmaps

* Thu May 17 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 7.19.devo282-11
- Fix missnaming of startup file
- Fix changelog entry

* Sun Mar 18 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 7.19.devo282-10
- Fixed error in specification of Source0

* Sun Mar 18 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 7.19.devo282-9
- Redefine version to include vmrf patch version (devo282)
- Remove pointless %%{pkg} macro
- Add new pixmaps with better sizing (still ugly though)
- Renamed the vmrf patch to include the version

* Sat Feb 10 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 7.19-8
- Added u-vm-color.el from http://de.geocities.com/ulf_jasper/emacs.html
- Added vcard support from http://www.splode.com/users/friedman/software/emacs-lisp/
- Fixed name of info files in pre and post scripts

* Sat Feb  3 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 7.19-5
- Add patch from http://www.robf.de/Hacking/elisp/ (resolves bug 224501)
- Ensure CFLAGS="$RPM_OPT_FLAGS" (bug 225101)

* Mon Aug 28 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 7.19-4
- Bump release for FC-6 mass rebuild

* Tue Jun 20 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 7.19-3
- Change group to Applications/Internet
- Add release tag to the Requires for the -el package

* Tue May 23 2006 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 7.19-2
- Clean up spec file

* Fri Sep  2 2005 Jonathan Underwood <jonathan.underwood@gmail.com> - 7.19-1.fc4.jgu
- Initial build
- Generate vm-mode-init.el
- Separate out *.el files into -el package
- Added patch to remove warnings in the decode and encode programs
