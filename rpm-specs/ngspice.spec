# Features in Fedora/Free Electronic Lab
#	What else does this build do aside compiling ngspice ?
#	- Ensures interoperability with xcircuit via Tcl
#	- Ensures interoperability with mot-adms
#	- Provides tclspice capabilities
# Chitlesh Goorah

%global	userelease	0
%global	usegitbare	1

%if 0%{?usegitbare} < 1
# force
%global	userelease	1
%endif

%global	mainver	32.2
%global	docver		32
%undefine	prever
%global	prerpmver	%(echo "%{?prever}" | sed -e 's|-||g')

%global	mainrel	1

%if 0%{?usegitbare} >= 1
%global	gitcommit	5c3e2b6526b22015ddec692450f5c5077efa1d80
%global	gitdate	20200505
%global	shortcommit	%(c=%{gitcommit}; echo ${c:0:7})

%global	tarballdate	20200506
%global	tarballtime	0950
%endif

%if 0%{?userelease} >= 1
%global	fedorarel	%{?prever:0.}%{mainrel}%{?prever:.%{prerpmver}}
%endif
%if 0%{?usegitbare} >= 1
#%global	fedorarel	%{?prever:0.}%{mainrel}.D%{gitdate}git%{shortcommit}
%global	fedorarel	%{?prever:0.}%{mainrel}%{?prever:.%{prerpmver}}
%endif

%undefine       _changelog_trimtime

Name:			ngspice
Version:		%{mainver}
Release:		%{fedorarel}%{?dist}
Summary:		A mixed level/signal circuit simulator

License:		BSD
URL:			http://ngspice.sourceforge.net

%if 0%{?userelease} >= 1
Source0:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{version}/ngspice-%{version}.tar.gz
%endif
%if 0%{?usegitbare} >= 1
Source0:       	ngspice-%{tarballdate}T%{tarballtime}.tar.gz
%endif
Source1:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{version}/ngspice-%{docver}-manual.pdf
Source2:		https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{version}/ng_adms_va.tar.gz
Source10:		create-ngspice-git-bare-tarball.sh


# Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or
# not (bug 1047056, debian bug 737279)
Patch0:		ngspice-26-blt-linkage-workaround.patch

BuildRequires:	gcc

BuildRequires:	readline-devel
BuildRequires:	libXext-devel
BuildRequires:	libpng-devel
BuildRequires:	libICE-devel
BuildRequires:	libXaw-devel
BuildRequires:	libGL-devel
BuildRequires:	libXt-devel
# From ngspice 32
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libXft-devel
BuildRequires:	libXrender-devel

BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex

BuildRequires:	ImageMagick
BuildRequires:	mot-adms

BuildRequires:	git

Obsoletes:	ngspice-doc < 20-4.cvs20100619
Provides:	ngspice-doc = %{version}-%{release}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Ngspice is a general-purpose circuit simulator program.
It implements three classes of analysis:
- Nonlinear DC analyses
- Nonlinear Transient analyses
- Linear AC analyses

Ngspice implements the usual circuits elements, like resistors, capacitors,
inductors (single or mutual), transmission lines and a growing number of
semiconductor devices like diodes, bipolar transistors, mosfets (both bulk
and SOI), mesfets, jfet and HFET. Ngspice implements the EKV model but it
cannot be distributed with the package since its license does not allow to
redistribute EKV source code.

Ngspice integrates Xspice, a mixed-mode simulator built upon spice3c1 (and
then some tweak is necessary merge it with spice3f5). Xspice provides a
codemodel interface and an event-driven simulation algorithm. Users can
develop their own models for devices using the codemodel interface.

It can be used for VLSI simulations as well.


%package -n	tclspice
Summary:	Tcl/Tk interface for ngspice
BuildRequires:	tk-devel
BuildRequires:	blt-devel

%description -n	tclspice
TclSpice is an improved version of Berkeley Spice designed to be used with
the Tcl/Tk scripting language. The project is based upon the NG-Spice source
code base with many improvements.

%package	-n libngspice
Summary:	Shared library version of ngspice

%description	-n libngspice
This package contains shared library version of ngspice.

%package	-n libngspice-devel
Summary:	Development files for libngspice
Requires:	libngspice%{?isa} = %{version}-%{release}

%description	-n libngspice-devel
This package contains libraries and header files for
developing applications that use libngspice.


%prep
%if 0%{?userelease} >= 1
%setup -q
git init
git config user.name "%{name} maintainer"
git config user.email "%{name}-owner@fedoraproject.org"
git add .
git commit -m "base" -a
%endif

%if 0%{?usegitbare} >= 1
%setup -q -c -T -a 0
git clone ./%{name}.git/
cd %{name}
git config user.name "%{name} maintainer"
git config user.email "%{name}-owner@fedoraproject.org"

git checkout -b %{name}-%{version}-fedora %{gitcommit}
%endif

cat %{SOURCE2} | gzip -dc  | tar xof -

%patch0 -p2 -b .link
git commit -m "Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or not" -a

# make sure the examples are UTF-8...
for nonUTF8 in \
	examples/tclspice/tcl-testbench4/selectfromlist.tcl \
	examples/tclspice/tcl-testbench1/testCapa.cir \
	examples/tclspice/tcl-testbench1/capa.cir \
	ChangeLog \
	%{nil}
do
	%{_bindir}/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
	%{__mv} -f $nonUTF8.conv $nonUTF8
done
git commit -m "Change files to UTF8" -a

# rpmlint warnings
find examples/ -type f -name ".cvsignore" -exec rm -rf {} ';'
find src/ -type f -name "*.c" -exec chmod -x {} ';'
find src/ -type f -name "*.h" -exec chmod -x {} ';'
find src/ -type f -name "*.l" -exec chmod -x {} ';'
find src/ -type f -name "*.y" -exec chmod -x {} ';'
git commit -m "Fix permission" -a || :

# Fix Tclspice's examples
sed -i \
	's|load "../../../src/.libs/libspice.so"|lappend auto_path "%{_libdir}/tclspice"\npackage require spice|' \
	examples/tclspice/*/*.{tcl,sh}
sed -i \
	's|load ../../../src/.libs/libspice.so|lappend auto_path "%{_libdir}/tclspice"\npackage require spice|' \
	examples/tclspice/*/*.{tcl,sh}
sed -i \
	's|spice::codemodel ../../src/xspice/icm/spice2poly|spice::codemodel %{_libdir}/tclspice/spice2poly|' \
	examples/tclspice/tcl-testbench*/tcl-testbench*.sh
git commit -m "Fix Tclspice's examples" -a

# Fixed minor CVS build
sed -i \
	"s|AM_CPPFLAGS =|AM_CPPFLAGS = -I\$(top_srcdir)/src/maths/ni |" \
	src/spicelib/analysis/Makefile.am
git commit -m "Fix include path" -a

export ACLOCAL_FLAGS=-Im4
./autogen.sh --adms
git commit -m "Execute autogen" -a || :

chmod +x configure

%build
%if 0%{?usegitbare} >= 1
cd %{name}
%endif

# ---- Tclspice ----------------------------------------------------------------
# Adding BLT support
export CFLAGS="%{optflags} -I%{_includedir}/blt"

# Make builddir for tclspice
%{__mkdir} -p tclspice
%{__cp} -Rl `ls . | grep -v tclspice` tclspice

# Configure tclspice
cd tclspice
sed -i \
	's|\#define NGSPICEDATADIR "\`echo \$dprefix/share/ngspice\`"|\#define NGSPICEDATADIR "\`echo %{_libdir}/tclspice\`"|' \
	configure*

# direct access to Tcl_Interp->result deprecated in tcl8.6,
# remaining usage cannot be replaced by Tcl_SetResult
export CPPFLAGS=-DUSE_INTERP_RESULT

# comment by Mamoru TASAKA (20170330)
# Looking at the actually source code, --enable-newpred does not seem to
# make sense, and it seems to cause calculation error (bug 844100, bug 1429130)
#
# (20190120) Remove some obsolete or dangerous configure option
# by the request from the upstream
%configure \
	--disable-silent-rules \
	--enable-adms \
	--enable-xspice \
	--enable-maintainer-mode \
	--enable-dependency-tracking \
	--enable-cider \
%if 0
	--enable-newpred \
%endif
	--enable-openmp \
	--enable-predictor \
	--enable-shared \
	--with-readline=yes \
	--with-tcl=%{_libdir}/ \
	--libdir=%{_libdir}/tclspice \
	--enable-oldapps \
	%{nil}

%{__make} -k
# Once install to the temp dir
rm -rf $(pwd)/../INST-TCLSPICE
%{__make} INSTALL="install -p" install DESTDIR=$(pwd)/../INST-TCLSPICE
cd ..
# ------------------------------------------------------------------------------

for opt in with-ngshared without-ngshared
do
%configure \
	--disable-silent-rules \
	--${opt} \
	--enable-adms \
	--enable-xspice \
	--enable-maintainer-mode \
	--enable-dependency-tracking \
	--enable-cider \
%if 0
	# bug 844100, bug 1429130
	--enable-newpred \
%endif
	--enable-openmp \
	--enable-predictor \
	--enable-shared \
	--with-readline=yes \
	--libdir=%{_libdir} \
	--enable-oldapps \
	%{nil}

%{__make} clean
# No parallel make
%{__make} -k
# Once install to the temp dir
rm -rf $(pwd)/INST-NGSPICE-${opt}
%{__make} INSTALL="install -p" install DESTDIR=$(pwd)/INST-NGSPICE-${opt}
find $(pwd)/INST-NGSPICE-${opt} -type f | sort

done

%install
%if 0%{?usegitbare} >= 1
cp -p %{name}/COPYING .
cd %{name}
%endif

# ---- Tclspice ----------------------------------------------------------------

# Clean up unneeded / duplicate files also installed from ngspice
pushd INST-TCLSPICE
rm -rf ./%{_datadir}/ngspice/include/
# see bug 1311869
rm -f ./%{_datadir}/ngspice/scripts/spinit
# binary differ
# for --short-circuit
if [ -f .%{_bindir}/cmpp ] ; then
  mv .%{_bindir}/cmpp{,-tclspice}
fi
popd

# Install
# ref: https://sourceforge.net/p/ngspice/support-requests/34/
# For codemodel files, install non-shared version
# so, first, install ngshared version, then non-shared version
cp -a INST-NGSPICE-with-ngshared/* %{buildroot}
cp -a INST-NGSPICE-without-ngshared/* %{buildroot}
cp -a INST-TCLSPICE/* %{buildroot}

%{__rm} -rf \
	%{buildroot}%{_libdir}/tclspice/libspice.la \
	%{buildroot}%{_libdir}/tclspice/libspicelite.la \
	%{buildroot}%{_libdir}/libngspice.la \
	%{nil}
# ------------------------------------------------------------------------------

# ADMS support
# It seems that the below is not needed, compiled into binary already
# (mtasaka, 20160628)
%if 0
cp -pr ./src/spicelib/devices/adms/ %{buildroot}%{_datadir}/%{name}
%endif

# Ensuring that all docs are under %%{_pkgdocdir}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr examples/ %{buildroot}%{_pkgdocdir}
install -cpm 0644 %{SOURCE1} %{buildroot}%{_pkgdocdir}/%{name}-%{version}.pdf

cp -a \
	Stuarts_Poly_Notes \
	FAQ \
	DEVICES \
	ANALYSES \
	%{buildroot}%{_pkgdocdir}
cp -a \
	AUTHORS \
	README* \
	BUGS \
	ChangeLog \
	NEWS \
	%{buildroot}%{_pkgdocdir}

# pull as debuginfo
chmod +x %{buildroot}%{_libdir}/ngspice/*.cm
chmod +x %{buildroot}%{_libdir}/tclspice/ngspice/*.cm

%check
%if 0%{?usegitbare} >= 1
cd %{name}
%endif
cd tests
#make check

%files
%{_bindir}/*
%exclude	%{_bindir}/cmpp-tclspice
%{_datadir}/%{name}/
%exclude	%{_datadir}/%{name}/scripts/tclspinit
%{_libdir}/ngspice/

%{_mandir}/man1/*
%exclude %{_pkgdocdir}/examples/tclspice
%doc	%{_pkgdocdir}
%license COPYING

%files	-n tclspice
%{_bindir}/cmpp-tclspice
%doc	%{_pkgdocdir}/examples/tclspice
%{_libdir}/tclspice/
%dir	%{_datadir}/ngspice
%dir	%{_datadir}/%{name}/scripts/
%{_datadir}/%{name}/scripts/tclspinit

%files	-n libngspice
%{_libdir}/libngspice.so.0*

%files	-n libngspice-devel
%{_libdir}/pkgconfig/ngspice.pc
%{_libdir}/libngspice.so
%{_includedir}/ngspice/

%changelog
* Wed May  6 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 32.2-1
- 32.2 tagged

* Tue May  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 32-1.D20200505gitbbe81ca
- Update to 32
- Use upstream git to use some upstream fixes since release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 31-4.respin2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct  7 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 31-3.respin2
- 31 tarball again respun

* Sun Sep 29 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 31-2.respin1
- 31 tarball respun

* Wed Sep 25 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 31-1
- Update to 31

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 30-4
- Rebuild for readline 8.0

* Tue Feb 05 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 30-3
- F-30: mass rebuild

* Sun Jan 20 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 30-2
- Remove some obsolete or dangerous configure options by
  the request from the upstream (and ref: bug 1666505)

* Tue Jan  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 30-1
- Update to 30

* Mon Dec 31 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 29-2
- Build shared library (bug 1440904 and so on)

* Sun Dec 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 29-1
- Update to 29

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 28-1
- Update to 28 (bug 1591460)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 27-1
- Update to 27

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 26-8
- Disable newpred mode (bug 844100, bug 1429130)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 26-6
- Rebuild for readline 7.x

* Sun Jul  3 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 26-5
- Link libspice.so with -lBLT or -lBLTlite, depending on whether in tk mode or
  not (bug 1047056, debian bug 737279)

* Tue Jun 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 26-4
- Don't get ngspice files overwritten by files from tclspice side
  (bug 1311869)
- rearrange files entries between ngspice / tclspice
  - move tclspinit into tclspice
  - rename tclspice side cmpp
  - also don't overwrite ngspice header files by tclspice side

* Mon Jun 27 2016 Mamoru TASAKA <mtasaka@fedoraproject.org>
- spec file clean up
- Don't install adms source and compiled .o objects, they are
  already linked into ngspice and tclspice shared library

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Eduardo Mayorga <mayorga@fedoraproject.org> - 26-2
- Use %%global instead of %%define

* Thu Oct 08 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 26-1
- Update to 26 release.
- use licence tag
- use configure macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 23-8
- Fix FTBFS with tcl-8.6 (#1106295)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 23-6
- Introduce %%_pkgdocdir (RHBZ #994004).
- Fix bogus changelog date.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 23-1
- New upstream sources with various bug fixes
- Upstream added #include <ftedev.h> to src/include/tclspice.h

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-6.cvs20101113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-5.cvs20101113
- new upstream sources with various bug fixes

* Sat Aug 21 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-4.cvs20100821
- enabling adms support

* Sun Aug 01 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-3.cvs20100719
- new fixes from development trunk

* Sun Jul 11 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-2.cvs20100620
- added bison and byacc as BR

* Thu Jul 01 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 21-1.cvs20100620
- release -21 with BSIMSOI support for < 130nm designs

* Sat Jun 19 2010  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 20-4.cvs20100619
- prerelease -21 with BSIMSOI support for < 130nm designs

* Tue Dec 8 2009  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 20-3
- Fixed build on CentOS-5

* Tue Dec 8 2009  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 20-2
- Improved interoperobability with xcircuit

* Mon Nov 16 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 20-1
- new upstream release

* Sun Aug 02 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 19-1
- new upstream release
- RHBZ #514484 A Long Warning Message (patched)
- RHBZ #511695 FTBFS ngspice-18-2.fc11

* Sat Feb 21 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 18-2
- x11 windows (help and plot) fixes #RHBZ 481525

* Sat Jan 10 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 18-1
- new upstream release

* Sun Jun 15 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-16
- Bugfix: #449409: FTBFS ngspice-17-14.fc9

* Fri Apr 18 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-15
- rebuild

* Fri Aug 24 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-13
- mass rebuild for fedora 8 - BuildID

* Mon Aug 06 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-12
- fixed ScriptletSnippets for Texinfo #246780
- moved documentations to -doc package

* Sat Mar 17 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-11
- droped patch: ngspice-bjt.patch, upstream will provide a better patch soon

* Sat Mar 17 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-10
- fixed bug #227519 in spec file - Ville Skyttä
- patch: ngspice-bjt.patch fixes the problem with bjt devices that have less than five nodes

* Tue Jan 09 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-9
- dropped --enable-cider since it requires non-opensource software
- dropped --enable-predictor from %%configure

* Tue Dec 19 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-8
- patch0 for xcircuit pipemode
- XCircuit can work as an ng-spice front-end
- fixed infodir to mean FE guidelines

* Sun Oct 15 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-7
- Fixed src/spinit.in for 64 bit

* Thu Oct 12 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-6
- Testing on 64 bit arch

* Mon Sep 04 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-5
- Added libXt-devel to include X headers

* Wed Aug 30 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 17-4
- Fix to pass compiler flags in xgraph.

* Tue Aug 29 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-3
- Fixed BR and script-without-shellbang for debug file

* Mon Aug 28 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-2
- Fixed BRs and excluded libbsim4.a
- Removed duplicates and useless ldconfig from %%post

* Sun Aug 27 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 17-1
- Initial Package for Fedora Extras
