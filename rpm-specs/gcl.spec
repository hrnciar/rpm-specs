# Address randomization breaks gcl's memory management scheme
%undefine _hardened_build

# Upstream prerelease number
%global prerel 90

Name:           gcl
Version:        2.6.13
Release:        0.%{prerel}%{?dist}
Summary:        GNU Common Lisp

License:        GPL+ and LGPLv2+
URL:            http://www.gnu.org/software/gcl/
Source0:        ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-2.6.12.tar.gz
Source1:        gcl.el
# This is some info files that are needed for the DESCRIBE function to do
# something useful.  These files are present in git HEAD (i.e., the upcoming
# 2.7.0 release), but are missing in the 2.6 branch.
Source2:        %{name}-2.6.8-info.tar.xz
# Because we must keep address randomization off, we include a script to
# ensure that happens.
Source3:        gcl-exec

# Upstream builds point releases for Debian, and uploads the patches directly
# to the Debian Patch Tracker, but does not spin new tarballs.  These are the
# upstream patches from https://sources.debian.org/patches/gcl/.
Patch0:         Version_2_6_13pre1.patch
Patch1:         Version_2_6_13pre1a.patch
Patch2:         Version_2_6_13pre1b.patch
Patch3:         Version_2_6_13pre2.patch
Patch4:         Version_2_6_13pre3.patch
Patch5:         Version_2_6_13pre3a.patch
Patch6:         Version_2_6_13pre4.patch
Patch7:         Version_2_6_13pre5.patch
Patch8:         Version_2_6_13pre6.patch
Patch9:         Version_2_6_13pre7.patch
Patch10:        Version_2_6_13pre8a.patch
Patch11:        Version_2_6_13pre8b.patch
Patch12:        Version_2_6_13pre12.patch
Patch13:        Version_2_6_13pre13.patch
Patch14:        Version_2_6_13pre16.patch
Patch15:        Version_2_6_13pre17.patch
Patch16:        Version_2_6_13pre18.patch
Patch17:        Version_2_6_13pre19.patch
Patch18:        Version_2_6_13pre20.patch
Patch19:        Version_2_6_13pre22.patch
Patch20:        Version_2_6_13pre25.patch
Patch21:        Version_2_6_13pre26.patch
Patch22:        Version_2_6_13pre27.patch
Patch23:        Version_2_6_13pre28.patch
Patch24:        Version_2_6_13pre29.patch
Patch25:        Version_2_6_13pre30.patch
Patch26:        Version_2_6_13pre31.patch
Patch27:        Version_2_6_13pre32.patch
Patch28:        Version_2_6_13pre33.patch
Patch29:        Version_2_6_13pre34.patch
Patch30:        Version_2_6_13pre35.patch
Patch31:        Version_2_6_13pre36.patch
Patch32:        Version_2_6_13pre38.patch
Patch33:        Version_2_6_13pre39.patch
Patch34:        data_bss_offset-in-unexec-sparc64-fix.patch
Patch35:        Version_2_6_13pre41.patch
Patch36:        Version_2_6_13pre45.patch
Patch37:        Version_2_6_13pre46.patch
Patch38:        Version_2_6_13pre47.patch
Patch39:        Version_2_6_13pre48.patch
Patch40:        Version_2_6_13pre49.patch
Patch41:        Version_2_6_13pre50.patch
Patch42:        pathnames1.1.patch
Patch43:        ansi-test-clean-target.patch
Patch44:        pathnames1.2.patch
Patch45:        pathnames1.3.patch
Patch46:        pathnames1.4.patch
Patch47:        pathnames1.5.patch
Patch48:        pathnames1.6.patch
Patch49:        pathnames1.7.patch
Patch50:        pathnames1.9.patch
Patch51:        pathnames1.11.patch
Patch52:        pathnames1.12.patch
Patch53:        pathnames1.13.patch
Patch54:        list_order.1.patch
Patch55:        list_order.5.patch
Patch56:        list_order.6.patch
Patch57:        defined_real_maxpage.patch
Patch58:        list_order.7.patch
Patch59:        list_order.8.patch
Patch60:        list_order.9.patch
Patch61:        list_order.11.patch
Patch62:        disable_gprof_aarch64.patch
Patch63:        list_order.12.patch
Patch64:        real_list_order.12.patch
Patch65:        list_order.13.patch
Patch66:        list_order.4.patch
Patch67:        list_order.16.patch
Patch68:        list_order.17.patch
Patch69:        list_order.18.patch
Patch70:        list_order.19.patch
Patch71:        list_order.20.patch
Patch72:        list_order.21.patch
Patch73:        list_order.22.patch
Patch74:        list_order.23.patch
Patch75:        list_order.24.patch
Patch76:        list_order.25.patch
Patch77:        Version_2_6_13pre52.patch
Patch78:        Version_2_6_13pre54.patch
Patch79:        Version_2_6_13pre55.patch
Patch80:        Version_2_6_13pre56.patch
Patch81:        Version_2_6_13pre57.patch
Patch82:        Version_2_6_13pre58.patch
Patch83:        Version_2_6_13pre59.patch
Patch84:        Version_2_6_13pre60.patch
Patch85:        Version_2_6_13pre61.patch
Patch86:        Version_2_6_13pre62.patch
Patch87:        Version_2_6_13pre63.patch
Patch88:        Version_2_6_13pre64.patch
Patch89:        Version_2_6_13pre65.patch
Patch90:        Version_2_6_13pre66.patch
Patch91:        Version_2_6_13pre67.patch
Patch92:        Version_2_6_13pre68.patch
Patch93:        Version_2_6_13pre69.patch
Patch94:        Version_2_6_13pre70.patch
Patch95:        Version_2_6_13pre71.patch
Patch96:        Version_2_6_13pre72.patch
Patch97:        Version_2_6_13pre73.patch
Patch98:        Version_2_6_13pre74.patch
Patch99:        Version_2_6_13pre76.patch
Patch100:       Version_2_6_13pre77.patch
Patch101:       Version_2_6_13pre78.patch
Patch102:       Version_2_6_13pre79.patch
Patch103:       Version_2_6_13pre80.patch
Patch104:       Version_2_6_13pre81.patch
Patch105:       Version_2_6_13pre82.patch
Patch106:       Version_2_6_13pre83.patch
Patch107:       Version_2_6_13pre84.patch
Patch108:       Version_2_6_13pre85.patch
Patch109:       Version_2_6_13pre86.patch
Patch110:       Version_2_6_13pre87.patch
Patch111:       Version_2_6_13pre88.patch
Patch112:       Version_2_6_13pre89.patch
Patch113:       Version_2_6_13pre90.patch

### Fedora patches

# This patch was last sent upstream on 29 Dec 2008.  It fixes a file descriptor
# leak, as well as combining 4 system calls into only 2 on an exec().
Patch500:       %{name}-2.6.12-fd-leak.patch
# This patch was last sent upstream on 29 Dec 2008.  It updates one source file
# from LaTeX 2.09 to LaTeX 2e, thereby eliminating LaTeX warnings about running
# in compatibility mode.
Patch501:       %{name}-2.6.11-latex.patch
# This patch was last sent upstream on 29 Dec 2008.  It adapts to texinfo 5.0.
Patch502:       %{name}-2.6.11-texinfo.patch
# This patch was last sent upstream on 29 Dec 2008.  It fixes a large number of
# compile- and run-time problems with the Emacs interface code.
Patch503:       %{name}-2.6.11-elisp.patch
# This is a Fedora-specific patch.  Do not delete C files produced from D files
# so they can be pulled into the debuginfo package.
Patch504:       %{name}-2.6.11-debuginfo.patch
# This patch was last sent upstream on 13 Oct 2009.  It fixes two bugs in the
# reading of PLT information.
Patch505:       %{name}-2.6.11-plt.patch
# This patch was last sent upstream on 13 Oct 2009.  It fixes several malformed
# function prototypes involving an ellipsis.
Patch506:       %{name}-2.6.11-ellipsis.patch
# Fix a linker problem on ARM platforms.
Patch507:       %{name}-2.6.11-arm.patch
# This patch was last sent upstream on 29 Dec 2008.  It updates the autoconf
# and libtool files to newer versions.  By itself, this patch accomplishes
# little of interest.  However, some of the later patches change configure.in.
# Without this patch, autoconf appears to run successfully, but generates a
# configure script that contains invalid shell script syntax.
Patch508:       %{name}-2.6.11-infrastructure.patch
# This patch was last sent upstream on 29 Dec 2008.  It rationalizes the
# handling of system extensions.  For example, on glibc-based systems, some
# functionality is available only when _GNU_SOURCE is defined.
Patch509:       %{name}-2.6.11-extension.patch
# This patch was last sent upstream on 29 Dec 2008.  It fixes a compilation
# error on newer GCC systems due to an include inside a function.  This affects
# the "unrandomize" sbrk() functionality, hence the name of the patch.
Patch510:       %{name}-2.6.12-unrandomize.patch
# The need for this patch was last communicated to upstream on 21 May 2009.
# Without this patch, compilation fails due to conflicting type definitions
# between glibc and Linux kernel headers.  This patch prevents the kernel
# headers from being used.
Patch511:       %{name}-2.6.11-asm-signal-h.patch
# Turn address randomization off early.  GCL is linked with libtirpc, which is
# linked with libselinux, which has a static initializer that calls malloc()
# and free() on systems that do not have /sys/fs/selinux or /selinux mounted,
# or have them mounted read-only.
Patch512:       %{name}-2.6.12-libselinux.patch

BuildRequires:  binutils-devel
BuildRequires:  bzip2
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  tex(latex)
BuildRequires:  tex-ec
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  emacs
BuildRequires:  xemacs
BuildRequires:  xemacs-packages-extra

Requires:       gcc
Requires:       util-linux%{?_isa}

# This can be removed when Fedora 30 reaches EOL
Obsoletes:      gcl-selinux < 2.6.13-0.84.1%{?dist}
Provides:       gcl-selinux = %{version}-%{release}


%description
GCL is a Common Lisp currently compliant with the ANSI standard.  Lisp
compilation produces native code through the intermediary of the
system's C compiler, from which GCL derives efficient performance and
facile portability. Currently uses TCL/Tk as GUI.


%package emacs
Summary:        Emacs mode for interacting with GCL
Requires:       %{name} = %{version}-%{release}
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description emacs
Emacs mode for interacting with GCL

%package xemacs
Summary:        XEmacs mode for interacting with GCL
Requires:       %{name} = %{version}-%{release}
Requires:       xemacs(bin) >= %{_xemacs_version}, xemacs-packages-extra
BuildArch:      noarch

%description xemacs
XEmacs mode for interacting with GCL


%prep
%setup -q -n %{name}
%setup -q -n %{name} -T -D -a 2
%autopatch -p1

# Don't insert line numbers into cmpinclude.h; the compiler gets confused
sed -i 's,\($(CC) -E\) -I,\1 -P -I,' makefile

# Ensure the frame pointer doesn't get added back
sed -i 's/"-fomit-frame-pointer"/""/' configure

# Fix a path in the launch script
sed -i 's|/usr/lib/tk|%{_datadir}/tk|' debian/gcl.sh

# Get a version of texinfo.tex that works with the installed version of texinfo
cp -p %{_texmf_main}/tex/texinfo/texinfo.tex info

# The archive is so full of spurious executable bits that we just remove them
# all here, then add back the ones that should exist
find . -type f -perm /0111 | xargs chmod a-x
chmod a+x add-defs add-defs1 config.guess config.sub configure install.sh
chmod a+x bin/info bin/info1 gcl-tk/gcltksrv.in gcl-tk/ngcltksrv mp/gcclab
chmod a+x o/egrep-def utils/replace xbin/*

%build
# SGC requires the frame pointer
export CFLAGS="%{optflags} -fno-omit-frame-pointer -fwrapv"
%configure --enable-readline --enable-ansi --enable-dynsysgmp --enable-xgcl \
  --enable-tclconfig=%{_libdir} --enable-tkconfig=%{_libdir}
# FIXME: %%{?_smp_mflags} breaks the build
make

# Build gcl.info, which is needed for DESCRIBE to work properly
make -C info gcl.info

# dwdoc needs one extra LaTeX run to resolve references
cd xgcl-2
pdflatex dwdoc.tex


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Get rid of the parts that we don't want
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/emacs
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/gcl-*/info

# The binary MUST be run with address randomization off.  The main() function
# has code to accomplish that, but it does not run early enough.  Ensure that
# randomization is off before GCL even starts.
mv $RPM_BUILD_ROOT%{_bindir}/gcl $RPM_BUILD_ROOT%{_bindir}/gcl-binary
install -p -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/gcl

# Install the man page
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -pf man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

# Install the HTML documentation
mkdir -p html
cp -pfr info/gcl-si info/gcl-tk html

# Install and compile the Emacs code
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
cp -pfr elisp/* $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
rm -f $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl/makefile
rm -f $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl/readme
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
sed -e "s|%LISP_DIR%|%{_emacs_sitelispdir}|" %{SOURCE1} > $RPM_BUILD_ROOT%{_emacs_sitestartdir}/gcl.el
pushd $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
%{_emacs_bytecompile} *.el
popd

# Install and compile the XEmacs code
mkdir -p $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/gcl
cp -fr elisp/* $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/gcl
rm -f $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/gcl/makefile
rm -f $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/gcl/readme
mkdir -p $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
sed -e "s|%LISP_DIR%|%{_xemacs_sitelispdir}|" %{SOURCE1} > $RPM_BUILD_ROOT%{_xemacs_sitestartdir}/gcl.el
pushd $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/gcl
%{_xemacs_bytecompile} *.el
popd

# Help the debuginfo generator
ln -s ../h/cmpinclude.h cmpnew/cmpinclude.h
ln -s ../h/cmpinclude.h lsp/cmpinclude.h
ln -s ../h/cmpinclude.h xgcl-2/cmpinclude.h

# The image has garbage strings containing RPM_BUILD_ROOT
export QA_SKIP_BUILD_ROOT=1


%clean
rm -f /tmp/gazonk_* /tmp/gcl_*


%files
%{_bindir}/gcl
%{_bindir}/gcl-binary
%{_prefix}/lib/gcl*
%{_infodir}/*
%{_mandir}/man*/*
%doc readme readme.xgcl RELEASE* ChangeLog* faq doc
%doc gcl*.jpg gcl.ico gcl.png
%doc html/gcl-si html/gcl-tk
%license COPYING*

%files emacs
%doc elisp/readme
%{_emacs_sitelispdir}/gcl/
%{_emacs_sitestartdir}/*

%files xemacs
%doc elisp/readme
%{_xemacs_sitelispdir}/gcl/
%{_xemacs_sitestartdir}/*


%changelog
* Mon Feb 24 2020 Jerry James <loganjerry@gmail.com> - 2.6.13-0.90%{?dist}
- Update to 2.6.13pre90
- Drop -tail-recursion-check patch, obsoleted by this update
- Drop -fcommon from build flags, fixed upstream

* Fri Jan 31 2020 Jerry James <loganjerry@gmail.com> - 2.6.13-0.89
- Update to 2.6.13pre89
- Add -tail-recursion-check patch to work around a segfaulting test
- Add -fcommon to build flags to work around FTBFS with GCC 10
- Drop -mno-pltseq on ppc64le, fixed upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.84.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  2 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.84.3
- Update the path to texinfo.tex

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.84.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.84.2
- Make gcl a wrapper script for gcl-binary to fix address randomization issues

* Sat Jun 29 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.84.1
- Update to 2.6.13pre84 (bz 1674924)
- Drop the -selinux patch and subpackage, no longer needed
- Build with -fwrapv
- Add the -libselinux patch to fix FTBFS if selinuxfs is mounted read-only
- Build with -mno-pltseq on ppc64le to handle relocation issues

* Sat Mar 23 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.79.2
- Merge -(x)emacs-el subpackages into -(x)emacs

* Sun Feb 17 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.79.2
- Drop the -largefile patch, causing crashes

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.13-0.79.1.1
- Rebuild for readline 8.0

* Fri Feb 15 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.79.1
- Update to 2.6.13pre79, fixes FTBFS (bz 1674924)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 2.6.12-11
- The SELinux package is noarch, so drop isa from dependencies

* Wed Feb 21 2018 Jerry James <loganjerry@gmail.com> - 2.6.12-10
- Comply with the draft SELinux packaging policy
- A new method of modifying the CFLAGS is needed
- Add ppc64le patch to fix a link problem

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6.12-6
- Rebuild for readline 7.x

* Sat Mar  5 2016 Jerry James <loganjerry@gmail.com> - 2.6.12-5
- Add -sincos patch to fix maxima build failure

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Jerry James <loganjerry@gmail.com> - 2.6.12-3
- Fix gcl-selinux post script (bz 1246002)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 2.6.12-1
- New upstream release
- Drop upstreamed reloc patches

* Fri Oct 10 2014 Jerry James <loganjerry@gmail.com> - 2.6.11-3
- Add -aarch64 patch to fix build on aarch64
- Update -ppc64 patch to match upstream's version

* Tue Sep 23 2014 Jerry James <loganjerry@gmail.com> - 2.6.11-2
- Add -ppc64 patch to fix build on ppc64/ppc64le (bz 1145521)

* Mon Sep  8 2014 Jerry James <loganjerry@gmail.com> - 2.6.11-1
- New upstream release (bz 1138998)
- Drop upstreamed patches
- Drop -fstack-protector workaround; fixed upstream
- GCL now builds on ppc64 (bz 480519)
- GCL now builds on aarch64 (bz 1099534)
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Tue May 20 2014 Jerry James <loganjerry@gmail.com> - 2.6.10-4
- ExcludeArch aarch64 (bz 1099534)

* Mon May 19 2014 Jerry James <loganjerry@gmail.com> - 2.6.10-3
- Add temporary fix for FTBFS with gmp 6

* Wed Feb  5 2014 Jerry James <loganjerry@gmail.com> - 2.6.10-2
- Add -tcl8 patch to prepare for TCL 8.6

* Fri Nov 15 2013 Jerry James <loganjerry@gmail.com> - 2.6.10-1
- New upstream release
- Drop upstreamed patches
- Help the debuginfo generator find more sources

* Wed Nov 13 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-3
- Rebuild to fix SELinux policy breakage

* Tue Oct  8 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-2
- Add -print-double patch from upstream to fix maxima 5.31.2 or later build.

* Mon Aug 26 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-1
- Final 2.6.8 release
- Build with -fno-omit-frame-pointer on all arches; SGC needs it
- Fix bug in selinux post script
- Add -tcl patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.18.20130521cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.17.20130521cvs
- Update to 20130521 snapshot for bug fixes
- Rebase patches

* Mon May 13 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.16.20130511cvs
- Update to 20130511 snapshot for bug fixes
- Add -largefile patch

* Fri Mar 22 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.15.20130126cvs
- Really fix FTBFS on i386 with -fno-omit-frame-pointer
- Update the -texinfo patch for texinfo 5.x
- Update texinfo.tex so we have a version that works with texinfo 5.x

* Thu Feb 14 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.15.20130126cvs
- Update to 20130126 snapshot to fix FTBFS
- Drop upstreamed -s390-reloc patch

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.15.20130121cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Dan Horák <dan[at]danny.cz> - 2.6.8-0.14.20130121cvs
- fix build on s390
- successful build requires kernel newer than what's in RHEL-6

* Mon Jan 21 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.13.20130121cvs
- Update to 20130121 snapshot, fixes bz 838068
- Rebuild for bz 886934
- Add tex-ec BR for TeXLive 2012
- Fix texinfo sources
- Workaround error from passing --parent to %%doc

* Tue Oct 30 2012 Jerry James <loganjerry@gmail.com> - 2.6.8-0.12.20121008cvs
- Update to 20121008 snapshot
- Add patch to identify unknown relocs instead of just exiting

* Thu Jul 26 2012 Jerry James <loganjerry@gmail.com> - 2.6.8-0.11.20120705cvs
- Update to 20120705 snapshot
- Change SELinux BR to match recent changes in Rawhide

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.11.20120323cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Jerry James <loganjerry@gmail.com> - 2.6.8-0.10.20120323cvs
- Update to 20120323 snapshot

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 2.6.8-0.10.20120109cvs
- Update to 20120109 snapshot

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.8-0.9.20110516cvs.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 2.6.8-0.9.20110516cvs.1
- rebuild with new gmp

* Thu Jun 16 2011 Jerry James <loganjerry@gmail.com> - 2.6.8-0.9.20110516cvs
- Rebuild due to bz 712251
- Use explicitly versioned Requires on gcl-selinux
- Drop defattr

* Wed Jun  1 2011 Jerry James <loganjerry@gmail.com> - 2.6.8-0.8.20110516cvs
- Update to 20110516 CVS snapshot for more bug fixes
- Fix SELinux policy for maxima (bz 650279)
- Drop upstreamed volatile patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.8.20101115cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Jerry James <loganjerry@gmail.com> - 2.6.8-0.7.20101115cvs
- Update to 20101115 CVS snapshot for more bug fixes
- Drop upstreamed loginname patch
- Add man page patch
- Add license file to -selinux package
- Don't force dynamic BFD so we can use custreloc instead

* Tue Mar 23 2010 Jerry James <loganjerry@gmail.com> - 2.6.8-0.7.20100201cvs
- Update to 20100201 CVS snapshot for multiple bug fixes including, I hope,
  bz 573534
- Drop upstreamed sigprocmask-linux patch
- Work around binutils-devel/binutils-static brokenness in F-13+.

* Mon Nov 30 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.7.20090701cvs
- Fix scripts to reflect actual installation order (bz 541050)
- Update PLT patch for GNU ld >= 2.19 (bz 542004)
- Use (X)Emacs macros to simplify the spec file

* Tue Oct 20 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.6.20090701cvs
- Update SELinux policy for confined users (bz 529757)

* Tue Oct  6 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.5.20090701cvs
- Update SELinux files to give compiled maxima files the right context
- Drop SELinux compatibility kludge for early F-11 selinux-policy packages

* Tue Aug 11 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.4.20090701cvs
- Update to 20090701 CVS snapshot, fixes bz 511483
- Break fix for <asm/signal.h> out into a separate patch and do it right
- Add -plt patch to fix reading of PLT info
- Add -ellipsis patch to eliminate nondeterministic behavior
- Use xz payloads instead of bz2
- Minor spec file cleanups

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.4.20090303cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.3.20090303cvs
- Update to 20090303 CVS snapshot
- Drop upstreamed BFD patch
- Make separate -selinux subpackage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.3.20080902cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.2.20080902cvs
- Add -fno-strict-aliasing to fix build problems in Rawhide.
- Fix the broken version number scheme I used on the last two releases.

* Mon Jan 26 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.1.20080902cvs.2
- Add missing files required to build gcl.info, which is needed for the
  DESCRIBE function to work properly.
- Specify the info entries explicitly, else a mangled version is written.

* Sat Jan 17 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.1.20080902cvs.1
- ExcludeArch ppc64 for now until I can figure out why it doesn't build

* Fri Jan  9 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.1.20080902cvs
- Update from CVS to fix many build problems
- Fix SELinux and BFD problems that blocked the build
- Add patches to address various build and runtime problems
- Drop old patches that are obsoleted by the update from CVS
- Split out emacs and xemacs subpackages

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6.7-19
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.6.7-18
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-17
- exclude arch x86_64 for now

* Thu Jan 03 2008 Alex Lancaster <alexlan at fedoraproject.org> - 2.6.7-16
- Rebuild for new Tcl (8.5)

* Tue Aug 14 2007 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-15
- Fix post-install script path on x64_64

* Wed Dec 27 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-14
- added req ncurses-devel

* Thu Dec 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-13
- Fix for compiling with readline library

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-12
- Rebuild for FE6

* Sat May  6 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-11
- fixed summary text (CLtL1 -> ANSI)
- configure: readine -> readline

* Fri Apr 14 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-10
- added changes to SELinux policy

* Wed Mar  8 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-7
- Patch gcl-bash.patch for configure

* Sat Feb 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-6
- Rebuild for Fedora Extras 5

* Fri Sep  9 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-1
- New Version 2.6.7

* Sun Apr 17 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.6.6-2
- Added buildreq tetex and texinfo

* Wed Apr  6 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.6.6-1
- New Version 2.6.6

* Fri Feb 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.6.5-1
- First Fedora release
