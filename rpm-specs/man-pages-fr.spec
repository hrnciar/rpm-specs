%global REV_EXTRAS 0.8.1
%global REV_SUP 20080608
%global SUBREV 1

Summary:   French version of the Linux man-pages
Name:      man-pages-fr
Version:   3.70
Release:   20%{?dist}
License:   GPL+ and GPLv2 and GPLv2+ and LGPLv2+ and GPLv3+ and ImageMagick and ISC and Public Domain and BSD and MIT and ASL 2.0 and UCD and IBM and TCL and xinetd
URL:       https://alioth.debian.org/projects/perkamon/
Source0:   https://alioth.debian.org/frs/download.php/file/4119/%{name}-%{version}-%{SUBREV}.tar.xz
Source1:   http://www.delafond.org/traducmanfr/mansupfr.tar.bz2
Source2:   http://manpagesfr.free.fr/download/man-pages-extras-fr-%{REV_EXTRAS}.tar.bz2
Patch0:    phony-targets.patch
Patch1:    add-security-context-options-for-coreutils.patch
BuildArch: noarch

Requires: man-pages-reader 
Supplements: (man-pages and langpacks-fr)

%description
Manual pages from the man-pages Project, translated into French.
Also includes supplemental pages provided by Dr. Patrick Atlas and
Dr. Gerard Delafond.

%prep
%setup -q -c
%setup -q -D -T -a 1
%setup -q -D -T -a 2
%patch0 -p1 -b .phony-targets

# This is not a translation of the “rename” man page from util-linux
# but of the rename from Perl (https://bugzilla.redhat.com/show_bug.cgi?id=1574233)
mv pagesdeman/man1/{rename,perl_rename}.1

# pick up the supplemental pages

mv pagesdeman man-pages-sup-fr-%{REV_SUP}
mv -f man-pages-sup-fr-%{REV_SUP}/LISEZ_MOI man-pages-sup-fr-%{REV_SUP}/LISEZ_MOI.man-pages-sup-fr
cp -a man-pages-sup-fr-%{REV_SUP}/* .
rm -rf man-pages-sup-fr-%{REV_SUP}/

# The mgetty in fedora and rhel contains the patches
# mgetty-1.1.26-issue.patch and mgetty-1.1.31-issue-doc.patch which
# change some options of mgetty and document the change.  The
# mgettyfedora.8 is the fedora/rhel specific translation.  Overwrite
# the mgetty.8 manpage with the fedora/rhel specific version:
mv man8/mgettyfedora.8 man8/mgetty.8

cp -a man-pages-extras-fr-%{REV_EXTRAS}/* .
rm -rf man-pages-extras-fr-%{REV_EXTRAS}/
%patch1 -p1 -b .security-context-options-for-coreutils

# fix bug rh 495703, rhbz#1135541
for i in mail.1 yum.8 xinetd.8 du.1; do
  name=`echo ${i} | awk -F"." '{print$1}'`
  find . -name ${i} -exec sed -i "s/\(\(\.SH\) *SYNOPSIS\)/.br\n\2 Attention\\\\ :\nLa traduction de  cette page de manuel pour \"$name\" est obsolète par rapport à la version actuelle de \"$name\". Pour avoir la dernière version de la page de manuel, veuillez utiliser la version anglaise. La version anglaise est disponible avec la commande suivante :\n.nf\nLANG=en_US.UTF-8 man $name\n.fi\n\1/gi" {} \;
done

%build

%install
# Create all the directories to be sure this package owns them
for n in 1 2 3 4 5 6 7 8 9 ; do
  mkdir -p $RPM_BUILD_ROOT%{_mandir}/fr/man${n}
done

#Install the man pages
for i in fr/man?/*; do
  install -m 0644 -p "${i}" "$RPM_BUILD_ROOT%{_mandir}/${i}"
done

# Install pages from man-pages-extras-fr-%%{version}.tar.bz2:
make install-fedora DESTDIR=$RPM_BUILD_ROOT

# Install pages from mansupfr.tar.bz2:
for i in 1 2 3 4 5 6 7 8 9; do
    if [ -d man${i} ] ; then
        cd man${i};
        for j in *.${i}; do
            if [ ! -f $RPM_BUILD_ROOT%{_mandir}/fr/man${i}/$j ] ; then
                echo "installing $j"
                install -m 0644 -p "${j}" "$RPM_BUILD_ROOT%{_mandir}/fr/man${i}/${j}"
            else
                echo "$j already exists"
            fi
        done
        cd ..
    fi
done

# Remove obsolete yum man pages (https://bugzilla.redhat.com/show_bug.cgi?id=1581301)
rm -rf $RPM_BUILD_ROOT%{_mandir}/fr/man?/yum*
rm -rf $RPM_BUILD_ROOT%{_mandir}/fr/man?/repo-rss.1
rm -rf $RPM_BUILD_ROOT%{_mandir}/fr/man?/package-cleanup.1
rm -rf $RPM_BUILD_ROOT%{_mandir}/fr/man?/reposync.1
rm -rf $RPM_BUILD_ROOT%{_mandir}/fr/man?/repoquery.1

# Remove files already included in other packages
# This page is provided by LDP so we have to remove it from shadow-utils package
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man3/getspnam.3

# This page is provided by rpm package
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man8/rpm.8

# This page is provided by sitecopy package
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man1/sitecopy.1

# This page is provided by nmap package
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man1/nmap.1

# These pages are provided by the awesome package
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/awesome*

# These pages are provided by the procps-ng >= 3.3.10 package:
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/free.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/kill.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/pgrep.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/pkill.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/pmap.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/pwdx.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/skill.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/slabtop.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/tload.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/uptime.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/w.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/watch.1
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/sysctl.conf.5
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/pidof.8
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/sysctl.8
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man?/vmstat.8

# https://bugzilla.redhat.com/show_bug.cgi?id=1334283
# remove because these pages are maybe not completely free:
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man2/sysinfo.2
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man2/pciconfig_read.2
rm -f $RPM_BUILD_ROOT%{_mandir}/fr/man2/getitimer.2

#LANG=fr ./cree_index_man.sh $RPM_BUILD_ROOT%%{_mandir}/fr/

%files
%doc fr/README.fr LISEZ_MOI.man-pages-sup-fr Changements Changements.anciens Lisez_moi
%{_mandir}/fr/man?/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Mike FABIAN <mfabian@redhat.com> - 3.70-16
- Remove obsolete yum man pages
- Resolves rhbz#1581301

* Wed Jun 13 2018 Mike FABIAN <mfabian@redhat.com> - 3.70-15
- Move rename.1 from mansupfr.tar.bz2 to perl_rename.1
- Resolves rhbz#1574233

* Tue Mar 27 2018 Nikola Forró <nforro@redhat.com> - 3.70-14
- Remove pidof.8 since it is provided by procps-ng package (as pidof.1)

* Thu Feb 15 2018 Mike FABIAN <mfabian@redhat.com> - 3.70-13
- Fix invalid license tag in man-pages-fr
- Resolves rhbz#1524074

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 28 2016 Mike FABIAN <mfabian@redhat.com> - 3.70-8
- Fix typo and fix remaining wrong italic in mknod man page

* Tue Jun 28 2016 Mike FABIAN <mfabian@redhat.com> - 3.70-7
- Fix usage of bold and italic in the translations for the new options
  in coreutils

* Mon Jun 27 2016 Mike FABIAN <mfabian@redhat.com> - 3.70-6
- add translations for security context options in coreutils
  (see also rhbz#1263637)

* Thu May 19 2016 Mike FABIAN <mfabian@redhat.com> - 3.70-5
- Resolves: rhbz#1334283 - man-pages-fr included non-free docs.

* Sat Feb 27 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.70-4
- Add Supplements: for https://fedoraproject.org/wiki/Packaging:Langpacks guidelines
- Removed Group: tag

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 15 2014 Mike FABIAN <mfabian@redhat.com> - 3.70-1
- update to new upstream version man-pages-fr 3.70-1 (Resolves: rhbz#1152476)

* Sat Oct 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.66-4
- Clean the spec to follow preferred packaging guidelines

* Thu Sep 25 2014 Mike FABIAN <mfabian@redhat.com> - 3.66-3
- exclude man-pages also contained in procps-ng >= 3.3.10
- Resolves: rhbz#1146203 - File conflicts with procps-ng

* Thu Sep 04 2014 Mike FABIAN <mfabian@redhat.com> - 3.66-2
- Mark du.1 man-page as out-of-date (Resolves: rhbz#1135541)

* Mon Jul 21 2014 Mike FABIAN <mfabian@redhat.com> - 3.66-1
- update to new upstream version man-pages-fr 3.66-1 (Resolves: rhbz#1119269)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Mike FABIAN <mfabian@redhat.com> - 3.65-1
- update to new upstream version man-pages-fr 3.65-1 (Resolves: rhbz#1093660)

* Tue Sep 10 2013 Mike FABIAN <mfabian@redhat.com> - 3.54-1
- update to new upstream version man-pages-fr 3.54-1 (Resolves: rhbz#1011366)

* Tue Sep 10 2013 Mike FABIAN <mfabian@redhat.com> - 3.53-1
- update to new upstream version man-pages-fr 3.53-1 (Resolves: rhbz#1005970)

* Mon Aug 19 2013 Mike FABIAN <mfabian@redhat.com> - 3.52-2
- Fix download URL

* Sat Aug 10 2013 Mike FABIAN <mfabian@redhat.com> - 3.52-1
- update to new upstream version man-pages-fr 3.52-1 (Resolves: rhbz#994255)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Mike FABIAN <mfabian@redhat.com> - 3.45-3
- Fix wrong weekday names in .spec file discovered by rpmdiff/Brewtap
- Overwrite mgetty.8 with fedora/rhel specific mgettyfedora.8 man-page

* Thu Feb 21 2013 Mike FABIAN <mfabian@redhat.com> - 3.45-2
- Resolves: #913536 - awesome : Conflicts with man-pages-fr
- remove French awesome man-pages because they are already included
  in the awesome package.

* Wed Jan 30 2013 Mike FABIAN <mfabian@redhat.com> - 3.45-1
- Resolves: #905826 - Due to problems in the man-pages-fr.spec file
  and the Makefile in man-pages-extras-fr-0.8.1.tar.bz2,
  many French man-pages are not included in man-pages-fr
- fix Makefile, “make install” in the subdirectory “afaire” was
  not executed because the target had the same name as the directory
  and was not marked .PHONY
- install the man-pages from mansupfr.tar.bz2 unless an identical
  man-page is already installed by man-pages-fr-3.45-1.tar.bz2 or
  man-pages-extras-fr-0.8.1.tar.bz2
  (installing the above extra man-pages fixes #903048 because
  man-pages for “less”, “more”, “bash”, and “echo” are now available.
  A man-page for “man” is still not available, this should be added
  to the “man-db” package instead).
- edit also xinetd.8 man page with sed to make it clear that it is
  not up-to-date (for #891277 and #891278).
- fix sed pattern to add the notice that a man-page is not up-to-date
- suggest to use “LANG=en_US.UTF-8 man $name” instead of
  ”LANG=en man $name” to view English man-pages (“en” is an invalid locale)
- Resolves: #880076 (add license tags inherited from packages whose
  translated man-pages are included here)

* Wed Nov 21 2012 Jens Petersen <petersen@redhat.com> - 3.44-1
- update to man-pages-fr-3.44-1 and newer mansupfr tarball
- update main project url to Alioth perkamon

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> 3.23-4
- Fix RH #582959 - add dependency on man-pages-reader

* Tue Apr 27 2010 Pablo Martin-Gomez <pablo.martin-gomez AT laposte DOT net> 3.23-3
- Revert the fix for RH #582959; it's only for Rawhide

* Sat Apr 24 2010 Pablo Martin-Gomez <pablo.martin-gomez AT laposte DOT net> 3.23-2
- Fix RH #582959 and #569441
- Fix a bug that ignore all the man pages from the main tarball

* Sun Feb 07 2010 Pablo Martin-Gomez <pablo.martin-gomez AT laposte DOT net> 3.23-1
- Fix RH #560915
- Switch to the Debian's man-pages-fr fork (Source0), which is updated, correctly maintained and provide the patches from man-pages Fedora package

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 Pablo Martin-Gomez <pablo.martin-gomez AT laposte DOT net> 3.03.0-3
- Fix #495703

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 6 2008 Pablo Martin-Gomez <pablo.martin-gomez AT laposte DOT net> 3.03.0-1
- Updated to 3.03.0
- Little change to the sources

* Sat Sep 13 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.80.0-5
- I wanted to say rpm of course...

* Sat Sep 13 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.80.0-4
- Sitecopy french men page isn't yet provided by upstream

* Sat Sep  6 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.80.0-3
- Remove pages provided by their upstream tarball
  Fix #455277 and #457663

* Fri Jun  6 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.80.0-2
- Bump release because wrong sources file

* Fri Jun  6 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.80.0-1
- Update to 2.80.0
- New SOURCE1 tarball and url for download
- New SOURCE2 tarball
- groups.1, latex2rtf.1, linkchecker.1, rpc.statd.8 and vipw.8
  are no more presents in man-pages-sup-fr.

* Fri May  2 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.79.0-5
- Remove linkchecker.1. Fix #445987.

* Fri May  2 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.79.0-4
- Remove vipw.8 already in shadow-utils. Fix #444868.

* Tue Apr 29 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.79.0-3
- Synchronize spec file with upstream one: many cleanup
- Increase release number to supersede upstream repository

* Fri Apr 25 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.79.0-2
- New ${SOURCE2} tarball

* Thu Apr 24 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.79.0-1
- Update to 2.79.0

* Wed Apr 23 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.78.0-1
- Update to 2.78.0

* Wed Apr 23 2008 Alain Portal <aportal AT univ-montp2 DOT fr> 2.77.0-1
- Update to 2.77.0

* Tue Feb 19 2008 Marcela Maslanova <mmaslano@redhat.com> 2.76.0-1
- update on 2.76.0
- definitely remove second source, wasn't used

* Fri Jan 11 2008 Marcela Maslanova <mmaslano@redhat.com> 2.75.0-1
- update on 2.75.0

* Tue Dec 18 2007 Marcela Maslanova <mmaslano@redhat.com> 2.40.0-11
- fix #425051 exclude vipw

* Tue Sep 18 2007 Marcela Maslanova <mmaslano@redhat.com> 2.40.0-10
- rebuild with correct sources

* Mon Sep 10 2007 Marcela Maslanova <mmaslano@redhat.com> 2.40.0-9
- 273941 doesn't install linkchecker man page

* Wed Aug 22 2007 Marcela Maslanova <mmaslano@redhat.com> 2.40.0-1
- new version from upstream
- check license

* Mon Mar 05 2007 Marcela Maslanova <mmaslano@redhat.com> 2.39-8
- merge review
- rhbz#230061

* Fri Oct 13 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-7
- rebuilt

* Fri Oct 13 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-6
- rebuilt

* Mon Oct 2 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-5
- fix spec (#208826)

* Wed Sep 06 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-4
- fix spec (#205349)

* Mon Sep 04 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-3
- new version from second source
- removed patch

* Wed Aug 30 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-2
- new version of man-pages

* Wed Aug 09 2006 Marcela Maslanova <mmaslano@redhat.com> 2.33.0-1
- new version of man-pages from source0

* Mon Jul 24 2006 Marcela Maslanova <mmaslano@redhat.com> 2.22.0-4
- new spec file for better encoding

* Fri Jul 21 2006 Marcela Maslanova <mmaslano@redhat.com> 2.22.0-3
- deleting conflicts in man-pages

* Wed Jul 19 2006 Marcela Maslanova <mmaslano@redhat.com> 2.22.0-2
- make from sources from Alain Portal new version of French man-pages
- man-pages-fr-aumix_missTH.patch - missed header
- used Spec file for version 2.16 from Alain Portal

* Thu Jul 13 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.16.0-1
- Update to 2.16.0
- New extra tarball

* Wed Jul 12 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.15.0-1
- Update to 2.15.0

* Wed Jul 12 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.14.0-1
- Update to 2.14.0

* Tue Jul 11 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.13.0-1
- Update to 2.13.0

* Mon Jul 10 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.12.0-1
- Update to 2.12.0

* Mon Jul 10 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.11.0-1
- Update to 2.11.0

* Fri Jul  7 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.10.0-1
- Update to 2.10.0
- New extra tarball

* Thu Jul  6 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.09.0-1
- Update to 2.09.0

* Wed Jul  5 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.08.0-1
- Update to 2.08.0

* Mon Jul  3 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.07.0-1
- Update to 2.07.0
- New extra tarball

* Fri Jun 30 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.06.0-1
- Update to 2.06.0

* Wed Jun 28 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.05.0-1
- Update to 2.05.0

* Tue Jun 27 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.04.0-1
- Update to 2.04.0
- New extra tarball
- Set LANG to fr before creating Index.?

* Thu Jun 15 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.03.0-1
- Update to 2.03.0

* Wed Jun 14 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.02.0-1
- Update to 2.02.0

* Tue May 30 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.01.0-1
- Update to 2.01.0

* Tue May 30 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 2.00.0-1
- Update to 2.00.0
- Add the new man-pages-extras-fr tarball.

* Fri May 12 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 1.70.0-1
- Update to 1.70.0

* Thu May 11 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 1.69.1-1
- Update to 1.69.1

* Wed May 10 2006 Alain Portal <aportal AT univ-montp2 DOT fr> 1.69.0-1
- Update to 1.69.0
- Remove some others conflicting pages from ${SOURCE1}
- Add BR because ${SOURCE0} pages are utf8 encoded
  and ${SOURCE1} are ASCII, ISO-8859-1 or ISO-8859-15 encoded

* Wed Nov  2 2005 Alain Portal <aportal AT univ-montp2 DOT fr> 1.64.0-1
- Update to 1.64.0
- Remove latex2rtf.1: package isn't provided by Fedora
- Remove gputils pages that are provided by upstream

* Thu Jul  7 2005 Matthias Saou <http://freshrpms.net/> 1.62.0-1
- Update to 1.62.0, remove very old and now included original LDP man pages.
- Spec file cleanup : Add URL, simplify installation.
- Go through all know conflicting man pages and separate them by package.

* Wed Sep 29 2004 Leon Ho <llch@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Akira TAGOH <tagoh@redhat.com> 0.9.7-9
- removed apropos.1, man.1, whatis.1, and man.config.5, because the latest man contains those manpages.

* Wed Sep 17 2003 Paul Gampe <pgampe@redhat.com> 0.9.7-8
- Bump

* Fri Sep 12 2003 Paul Gampe <pgampe@redhat.com> 0.9.7-7
- Clean out core files included in upstream tarball [#101328]

* Wed May 28 2003 Phil Knirsch <pknirsch@redhat.com> 0.9.7-6.1
- Bumped release and rebuilt

* Wed May 28 2003 Phil Knirsch <pknirsch@redhat.com> 0.9.7-6
- Dropped ethers.5 and domainname.1 manpages as they are in net-tools now.

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 0.9.7-5
- Convert all manpages to utf-8.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.9.7-4
- rebuilt

* Thu Jan  9 2003 Tim Powers <timp@redhat.com> 0.9.7-3
- more pages to remove

* Thu Jan  9 2003 Tim Powers <timp@redhat.com> 0.9.7-2
- remove pages that conflict with other packages

* Thu Jan  9 2003 Paul Gampe <pgampe@redhat.com> 0.9.7-1
- incorporate the three sources of available french manual pages
  to increase coverage

* Thu Nov  7 2002 Tim Powers <timp@redhat.com> 0.9-10
- remove lpq.1, lpr.1, and lprm.1 since they conflict with the mas
  mages in the cups package

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.9-9
- automated rebuild

* Mon Jun 17 2002 Trond Eivind Glomsrd <teg@redhat.com> 0.9-8
- Update nm.1 (#66666 - I like bugs with attached fixes :)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Aug 13 2001 Trond Eivind Glomsrd <teg@redhat.com> 0.9-5
- Rebuild. This should fix #51685

* Thu Aug  2 2001 Trond Eivind Glomsrd <teg@redhat.com>
- Own %%{_mandir}/fr
- s/Copyright/License/

* Sun Apr  8 2001 Trond Eivind Glomsrd <teg@redhat.com>
- Remove dnsdomainname.1 and hostname.1, they're now part of net-tools

* Tue Apr  3 2001 Trond Eivind Glomsrd <teg@redhat.com>
- fixes to the roff sources

* Tue Dec 19 2000 Trond Eivind Glomsrd <teg@redhat.com>
- 0.9

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Mon Jun 19 2000 Matt Wilson <msw@redhat.com>
- defattr root

* Mon Jun 12 2000 Trond Eivind Glomsrd <teg@redhat.com>
- use %%{_mandir} and %%{_tmppath}

* Mon May 15 2000 Trond Eivind Glomsrd <teg@redhat.com>
- first build
