# Upstream stopped making release tarballs in 2015.  Pull from git until
# upstream starts making them again.
%global gittag   12652a071bd43802eaf234b6489eeb9d395e284c
%global shorttag %(cut -b -7 <<< %{gittag})
%global gitdate  20200527

%ifarch %{ix86}
%global pvsarch ix86
%else
%ifarch x86_64
%global pvsarch ix86_64
%else
%global pvsarch %{_arch}
%endif
%endif

Name:           pvs-sbcl
Version:        7.0
Release:        2.%{gitdate}.%{shorttag}%{?dist}
Summary:        Interactive theorem prover from SRI

License:        GPLv2+ and BSD and Public Domain
URL:            http://pvs.csl.sri.com/
# We would like to use this URL:
# Source0:        https://github.com/SRI-CSL/PVS/archive/%%{gittag}/PVS-%%{shorttag}.tar.gz
# but we can't, because the PVS code is full of invocations of git, to find
# hashes on files, compute the number of commits since a tag, etc., and that
# URL yields a file with no .git directory.  I tried to patch out the git
# invocations but kept breaking things, so in despair, I have resorted to this:
# 1. git clone https://github.com/SRI-CSL/PVS
# 2. cd PVS
# 3. git reset --hard %%{gittag}
# 4. cd ..
# 5. tar cJf PVS-%%{version}-%%{shorttag}.tar PVS
Source0:        PVS-%{version}-%{shorttag}.tar.xz
Source1:        http://pvs.csl.sri.com/doc/pvs-prelude.pdf
Source2:        http://pvs.csl.sri.com/doc/interpretations.pdf
Source3:        http://pvs.csl.sri.com/papers/csl-97-2/csl-97-2.ps.gz
Source4:        http://pvs.csl.sri.com/papers/csl-93-9/csl-93-9.ps.gz
Source5:        pvs-sbcl.desktop
# This patch will not be sent upstream.  It adapts the SBCL support to the
# needs of SELinux-enabled Fedora systems, links against the system mona
# library instead of building the included sources, and enables building on
# architectures that the original sources do not support.
Patch0:         pvs-fedora.patch
# This patch was sent upstream 22 Feb 2013.  It removes an obsolete workaround
# for a missing glibc function; the workaround now fails the build.
# https://github.com/SRI-CSL/PVS/pull/78
Patch1:         pvs-siglongjmp.patch
# Fix FTBFS with gcc 10 due to -fno-common becoming the default.
# https://github.com/SRI-CSL/PVS/pull/75
Patch2:         pvs-fno-common.patch
# Fix texinfo errors that cause makeinfo to exit with nonzero status
# https://github.com/SRI-CSL/PVS/pull/72
# https://github.com/SRI-CSL/PVS/pull/74
Patch3:         pvs-texi.patch
# Fix Emacs Lisp error that caused building the language manual to abort
# https://github.com/SRI-CSL/PVS/pull/76
Patch4:         pvs-language-manual.patch
# Fix build problems with the user guide
# https://github.com/SRI-CSL/PVS/pull/77
Patch5:         pvs-user-guide.patch
# Fix LaTeX sources in the language manual
Patch6:         pvs-language-manual-latex.patch

BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  emacs
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-core
BuildRequires:  git-core
BuildRequires:  latexmk
BuildRequires:  mona-devel
BuildRequires:  perl-generators
BuildRequires:  sbcl
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)
BuildRequires:  tex(boxedminipage.sty)
BuildRequires:  tex(libertine.sty)
BuildRequires:  tex(relsize.sty)
BuildRequires:  tex(stmaryrd.sty)
BuildRequires:  tex(tocbibind.sty)
BuildRequires:  tex(xtab.sty)
BuildRequires:  tex-xits
BuildRequires:  yices-tools

Requires:       tex(latex)
Requires:       tk
Requires:       yices-tools
Provides:       pvs = %{version}-%{release}, pvsio = %{version}-%{release}

# This should (generally) match the corresponding tag in the sbcl spec
ExclusiveArch: %{ix86} x86_64 ppc sparcv9

# requires the same sbcl it was built against
%global sbcl_vr %(sbcl --version 2>/dev/null | cut -d' ' -f2)
%if "x%{?sbcl_vr}" != "x%{nil}"
Requires: sbcl = %{sbcl_vr}
%else
Requires: sbcl
%endif

%description
PVS is a verification system: that is, a specification language
integrated with support tools and a theorem prover.  It is intended to
capture the state-of-the-art in mechanized formal methods and to be
sufficiently rugged that it can be used for significant applications.

This build of PVS must be invoked as "pvs-sbcl", both to distinguish it
from builds with other Common Lisp engines, and to distinguish it from
/usr/sbin/pvs in the lvm2 package.

%prep
%autosetup -n PVS -p1

# Upstream didn't give us a configure script
autoreconf -ivf

# Fix building the language documentation
ln -s ../makebnf.sty doc/language

# We know where perl lives
sed -i 's,/usr/bin/env perl,/usr/bin/perl,' provethem.in

# Adapt the release notes to texi2any
sed -i 's/\$(TEXI2HTML).*-nav/texi2any --html --no-number-sections/' \
    doc/release-notes/Makefile

# Insert our build flags
sed -i "/XCFLAGS/s|-O|%{optflags}|" src/{BDD,WS1S}/%{pvsarch}-Linux/Makefile
sed -i "/WFLAGS/s|-Wall|%{optflags}|" src/utils/%{pvsarch}-Linux/Makefile
sed -i "s|^LDFLAGS =.*|& $RPM_LD_FLAGS|" \
    src/{BDD,utils,WS1S}/%{pvsarch}-Linux/Makefile

# Make yices available where the build system expects it
mkdir -p yices/%{pvsarch}-Linux/yices-2.6/bin
cp -p %{_bindir}/yices yices/%{pvsarch}-Linux/yices-2.6/bin/yices

# Remove obsolete version control files
find . -name .cvsignore -delete

%build
# SBCL defaults to an external format of ASCII in mock builds, which breaks
# the build when PVS tries to read Unicode-encoded files.
export LC_ALL=C.UTF-8
%configure

# The runtime image is built from the sbcl executable.  Most ELF sections are
# simply copied.  This includes the .note.gnu.build-id section, which holds
# the executable build-id, leading to a conflict with the sbcl package.  We
# cannot alter the build-id after PVS is built, because PVS computes a checksum
# over its ELF image, which then fails to match.  So we copy the sbcl binary
# here, alter its build-id, then build PVS with the altered binary.
cp -p %{_bindir}/sbcl .

# The section header is 16 bytes, so change at least one byte after that.
objcopy --dump-section .note.gnu.build-id=/tmp/build_id ./sbcl
byte=$(od -N 1 -t u -j 16 /tmp/build_id | \
       sed -n 's/^[[:alnum:]]*[[:blank:]]*\([[:digit:]]*\)/\1/p')
if [ $byte -eq 255 ]; then
  byte=0
else
  byte=$(( $byte + 1 ))
fi
printf $(printf '\\x%x' $byte) | \
  dd of=/tmp/build_id bs=1 seek=16 count=1 conv=notrunc
objcopy --update-section .note.gnu.build-id=/tmp/build_id ./sbcl
rm /tmp/build_id

# Build with the altered binary
make SBCLISP_HOME=$PWD
make SBCLISP_HOME=$PWD make-release-notes

# Mimic the effects of the relocate script for the build location
sed -i -e "s,^PVSPATH=.*$,PVSPATH=$PWD," pvs
sed -i -e "s,^PVSPATH=.*$,PVSPATH=$PWD," pvsio
sed -i -e "s,^PVSPATH=.*$,PVSPATH=$PWD," proveit
sed -i -e "s,^\$PVSPATH=.*$,\$PVSPATH=$PWD," provethem

# Run it once to force Lisp compilation of the native interfaces
./pvs -raw <<<'(sb-ext:exit :code 0 :abort t)'

# Get rid of some temporary files we no longer need
rm -f doc/release-notes/pvs-release-notes.{pg,ky,tp,fn,cp,vr}

# Build the documentation
make -C doc/api pvs-api.pdf
make -C doc/language language.pdf
make -C doc/prover prover.pdf
touch doc/user-guide/user-guide.ind
make -C doc/user-guide user-guide.pdf

# No sources for the prelude docs
cp -p %{SOURCE1} .

# Cannot be built: needs cslreport.cls
# pushd doc/interpretations
# pdflatex interpretations
# popd
cp -p %{SOURCE2} .

# Cannot be built: missing cslreport.cls
# make -C doc/semantics semantics.pdf
cp -p %{SOURCE3} .

# Cannot be built: missing /homes/rushby/tex/prelude
# make -C doc/datatypes datatypes.pdf
cp -p %{SOURCE4} .

# Mimic the effects of the relocate script for the installed location
sed -i -e "s,^PVSPATH=.*$,PVSPATH=%{_libdir}/pvs," pvs
sed -i -e "s,^PVSPATH=.*$,PVSPATH=%{_libdir}/pvs," pvsio
sed -i -e "s,^PVSPATH=.*$,PVSPATH=%{_libdir}/pvs," proveit
sed -i -e "s,^\$PVSPATH=.*$,\$PVSPATH=%{_libdir}/pvs," provethem

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/pvs/doc/release-notes
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_texmf}/tex/latex/pvs
cp -a bin emacs lib pvs-tex.sub wish %{buildroot}%{_libdir}/pvs
cp -a doc/release-notes/pvs-release-notes.info %{buildroot}%{_libdir}/pvs/doc/release-notes
cp -a pvs.sty %{buildroot}%{_texmf}/tex/latex/pvs
cp -a pvs %{buildroot}%{_bindir}/pvs-sbcl
cp -a pvsio proveit provethem %{buildroot}%{_bindir}

# Install the desktop file
desktop-file-install --mode=644 --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE5}

# Adjust the sbcl and yices symlinks
rm %{buildroot}%{_libdir}/pvs/bin/%{pvsarch}-Linux/{runtime/sbcl,yices2}
ln -s %{_bindir}/yices %{buildroot}%{_libdir}/pvs/bin/%{pvsarch}-Linux/yices2
ln -s %{_bindir}/sbcl %{buildroot}%{_libdir}/pvs/bin/%{pvsarch}-Linux/runtime/sbcl

# Remove a hidden make marker
rm %{buildroot}%{_libdir}/pvs/emacs/.readme

%files
%doc *.ps.gz *.pdf README.md Examples doc/*.pdf
%doc doc/api/pvs-api.pdf doc/language/language.pdf
%doc doc/prover/prover.pdf doc/release-notes/pvs-release-notes.pdf
%doc doc/user-guide/user-guide.pdf
%license LICENSE NOTICES
%{_bindir}/proveit
%{_bindir}/provethem
%{_bindir}/pvsio
%{_bindir}/pvs-sbcl
%{_libdir}/pvs/
%{_datadir}/applications/*.desktop
%{_texmf}/tex/latex/pvs/

%changelog
* Thu May 28 2020 Jerry James <loganjerry@gmail.com> - 7.0-2.20200218.12652a0
- Update to latest git snapshot for bug fixes
- Adapt to TexLive 2020; add -language-manual-latex patch

* Fri Feb 28 2020 Jerry James <loganjerry@gmail.com> - 7.0-1.20200218.a1f7148
- Rebuild for sbcl 2.0.1 (bz 1807476)
- Update to latest git snapshot for bug fixes

* Tue Feb  4 2020 Jerry James <loganjerry@gmail.com> - 7.0-1.20200129.b517ae2
- Update to latest git snapshot
- Drop upstream patches: -chmod, -emacs26, -hashfn, -makeindex,
  -remove-backslashes, -unicode
- Add patches to fix documentation: -language-manual, -texi, -user-guide
- Add -fno-common patch to fix FTBFS with GCC 10
- Drop XEmacs support

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug  2 2019 Jerry James <loganjerry@gmail.com> - 6.0-64
- rebuild (sbcl)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Jerry James <loganjerry@gmail.com> - 6.0-62
- rebuild (sbcl)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Rex Dieter <rdieter@fedoraproject.org> - 6.0-60
- rebuild (sbcl)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 6.0-58
- rebuild (sbcl)

* Tue Feb 13 2018 Jerry James <loganjerry@gmail.com> - 6.0-57
- Bump and rebuild for sbcl dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-55
- rebuild (sbcl)

* Fri Oct 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-54
- rebuild (sbcl)

* Wed Oct 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-53
- rebuild (sbcl)

* Fri Sep 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-52
- rebuild (sbcl)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-49
- rebuild (sbcl)

* Sun Jun 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-48
- rebuild (sbcl)

* Thu Jun 01 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-47
- rebuild (sbcl)

* Thu Mar 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-46
- rebuild (sbcl)

* Mon Mar 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 6.0-45
- rebuild (sbcl)

* Wed Feb 22 2017 Jerry James <loganjerry@gmail.com> - 6.0-44
- rebuild (sbcl)
- Drop workaround for bz 1268054, now fixed

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 6.0-42
- rebuild (sbcl)

* Wed Nov 30 2016 Jerry James <loganjerry@gmail.com> - 6.0-41
- rebuild (sbcl)
- Drop obsolete scriptlets

* Tue Aug 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 6.0-40
- rebuild (sbcl)

* Fri Apr 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 6.0-39
- rebuild (sbcl)

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 6.0-38
- rebuild (sbcl)

* Mon Mar 28 2016 Jerry James <loganjerry@gmail.com> - 6.0-37
- rebuild (mona)

* Mon Mar 07 2016 Rex Dieter <rdieter@fedoraproject.org> 6.0-36
- rebuild (sbcl)

* Sat Mar 05 2016 Rex Dieter <rdieter@fedoraproject.org> 6.0-35
- rebuild (sbcl)

* Wed Feb 10 2016 Jerry James <loganjerry@gmail.com> - 6.0-34
- rebuild (sbcl)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 6.0-32
- rebuild (sbcl)

* Wed Nov 11 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0-31
- rebuild (sbcl)

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0-30
- rebuild (sbcl)
- workaround botched texlive.macros (#1268054)

* Mon Sep 14 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0-29
- rebuild (sbcl)

* Mon Jun 22 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0-28
- rebuild (sbcl)

* Mon Jun 22 2015 Jerry James <loganjerry@gmail.com> - 6.0-27
- Use license macro
- Build an index for the user guide

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0-25
- rebuild (sbcl)

* Fri Feb 13 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0-24
- rebuild (sbcl)

* Sat Jan 03 2015 Rex Dieter <rdieter@fedoraproject.org> 6.0-23
- rebuild (sbcl)

* Wed Dec 17 2014 Rex Dieter <rdieter@fedoraproject.org> 6.0-22
- rebuild (sbcl)

* Thu Oct  9 2014 Jerry James <loganjerry@gmail.com> - 6.0-21
- Build documentation with texi2any instead of texi2html (bz 1151213)

* Thu Oct 09 2014 Rex Dieter <rdieter@fedoraproject.org> 6.0-21
- rebuild (sbcl)

* Thu Aug 21 2014 Rex Dieter <rdieter@fedoraproject.org> 6.0-20
- rebuild (sbcl)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Rex Dieter <rdieter@fedoraproject.org> 6.0-18
- rebuild (sbcl)

* Thu Jun 12 2014 Rex Dieter <rdieter@fedoraproject.org> 6.0-17
- rebuild (sbcl)

* Tue Jun 10 2014 Jerry James <loganjerry@gmail.com> - 6.0-16
- rebuild (sbcl)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 6.0-14
- rebuild (sbcl)

* Mon Mar 10 2014 Jerry James <loganjerry@gmail.com> - 6.0-13
- Add pvs-remove-backslashes.patch to fix the build with SBCL 1.1.16

* Fri Mar 07 2014 Rex Dieter <rdieter@fedoraproject.org> 6.0-13
- rebuild (sbcl)

* Wed Jan 29 2014 Rex Dieter <rdieter@fedoraproject.org> 6.0-12
- rebuild (sbcl)

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> 6.0-11
- rebuild (sbcl)

* Mon Nov 04 2013 Jerry James <loganjerry@gmail.com> - 6.0-10
- Update -fedora patch to fix ASDF failure (bz 1026454)

* Mon Nov 04 2013 Rex Dieter <rdieter@fedoraproject.org> 6.0-10
- rebuild (sbcl)

* Mon Sep 30 2013 Rex Dieter <rdieter@fedoraproject.org> 6.0-9
- rebuild (sbcl)

* Sun Sep 08 2013 Rex Dieter <rdieter@fedoraproject.org> 6.0-8
- rebuild (sbcl)

* Mon Aug 05 2013 Rex Dieter <rdieter@fedoraproject.org> 6.0-7
- rebuild (sbcl)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 6.0-5
- Perl 5.18 rebuild

* Sun Jun 02 2013 Rex Dieter <rdieter@fedoraproject.org> 6.0-4
- rebuild (sbcl)

* Mon Apr 29 2013 Rex Dieter <rdieter@fedoraproject.org> 6.0-3
- rebuild (sbcl)

* Tue Feb 26 2013 Rex Dieter <rdieter@fedoraproject.org> 6.0-2
- rebuild (sbcl)

* Thu Feb 21 2013 Jerry James <loganjerry@gmail.com> - 6.0-1
- New upstream release
- Drop unnecessary emacs patch
- Define LANG while building and add -unicode patch to get Unicode support
- Add the -siglongjmp patch to fix a build failure

* Wed Feb 20 2013 Rex Dieter <rdieter@fedoraproject.org> 5.0-20
- rebuild (sbcl)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 5.0-18
- rebuild (sbcl)

* Tue Dec 11 2012 Jerry James <loganjerry@gmail.com> - 5.0-17
- Alternate fix for the index problem
- Distribute the user guide

* Sat Dec 08 2012 Rex Dieter <rdieter@fedoraproject.org> 5.0-16
- rebuild (sbcl)

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 5.0-15
- rebuild (sbcl)

* Sat Oct 27 2012 Rex Dieter <rdieter@fedoraproject.org> 5.0-14
- rebuild (sbcl)

* Tue Aug 07 2012 Rex Dieter <rdieter@fedoraproject.org> 5.0-13
- rebuild (sbcl)

* Mon Jul 23 2012 Rex Dieter <rdieter@fedoraproject.org> 5.0-12
- rebuild (sbcl)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Rex Dieter <rdieter@fedoraproject.org> 5.0-10
- rebuild (sbcl)

* Thu Apr 12 2012 Rex Dieter <rdieter@fedoraproject.org> 5.0-9
- rebuild (sbcl)

* Thu Apr 05 2012 Rex Dieter <rdieter@fedoraproject.org> 5.0-8
- rebuild (sbcl)

* Wed Jan 18 2012 Jerry James <loganjerry@gmail.com> - 5.0-7
- rebuild (sbcl)
- Adapt to new fixnum size
- Fix the (chmod) function
- Adapt to Emacs 24
- Minor spec file cleanups

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec  6 2011 Jerry James <loganjerry@gmail.com> - 5.0-5
- Fix building on non-Intel architectures

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 5.0-4
- rebuild (sbcl)

* Sat Oct 15 2011 Rex Dieter <rdieter@fedoraproject.org> 5.0-3
- rebuild (sbcl)

* Mon Aug 22 2011 Rex Dieter <rdieter@fedoraproject.org> 5.0-2
- fix %%sbcl_vr macro usage

* Sat Apr 16 2011 Jerry James <loganjerry@gmail.com> - 5.0-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-12.20100126svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Jerry James <loganjerry@gmail.com> - 4.2-11.20100126svn
- Update patches for new SBCL

* Thu Sep 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2-10.20100126svn
- rebuild (sbcl)

* Wed Sep 29 2010 jkeating - 4.2-9.20100126svn
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2-8.20100126svn
- rebuild (sbcl)

* Mon Aug 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2-7.20100126svn
- rebuild (sbcl)

* Sat Jul 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2-6.20100126svn
- rebuild (sbcl)

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2-5.20100126svn
- rebuild (sbcl)

* Sat Apr 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2-4.20100126svn
- rebuild (sbcl)

* Mon Feb 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.2-3.20100126svn
- rebuild (sbcl)
- drop Requires(post): desktop-file-utils (not needed)

* Fri Jan 29 2010 Jerry James <loganjerry@gmail.com> - 4.2-2.20100126svn
- Update to 20100126 snapshot
- Fix several Emacs bugs, including bz 553023

* Mon Jan  4 2010 Jerry James <loganjerry@gmail.com> - 4.2-2.20100104svn
- Update to 20100104 snapshot.
- Fix mona patch.
- Dump a non-executable SBCL image to avoid prelink and strip issues.
- Solve the build-time hang in (X)Emacs.

* Tue Dec 22 2009 Jerry James <loganjerry@gmail.com> - 4.2-2.20091008svn
- Attempt to solve build-time hang in (X)Emacs.
- Don't fail if sbcl has not been prelinked.

* Mon Dec 21 2009 Jerry James <loganjerry@gmail.com> - 4.2-1.20091008svn
- Initial RPM
