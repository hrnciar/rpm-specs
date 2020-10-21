%define svnver .20090722svn
Summary:	Language for developing expert systems
Name:		clips
Version:	6.30.0
Release:	0.23%{?svnver}%{?dist}
Url:		http://clipsrules.sourceforge.net
License:	GPLv2
Source0:	http://downloads.sourceforge.net/clipsmm/%{name}-%{version}%{?svnver}.tar.bz2
Source1:	http://downloads.sourceforge.net/clipsmm/%{name}-%{version}%{?svnver}-doc.tar.bz2
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildRequires:  gcc-c++
BuildRequires:	ncurses-devel 
%else
BuildRequires:	libtermcap-devel
%endif
BuildRequires:	libXt-devel libXext-devel libXmu-devel libXaw-devel 
BuildRequires:	xorg-x11-proto-devel xorg-x11-xbitmaps 
BuildRequires:	desktop-file-utils
BuildRequires:	automake autoconf libtool
BuildRequires:	pkgconfig
BuildRequires:	ImageMagick

%define _legacy_common_support 1

%description
CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

This package provides the CLIPS command line environment and the clips
library.

%package	libs
Summary:	Run-time C libraries for CLIPS applications

%description	libs
This package contains the run-time libraries needed for CLIPS applications.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

%package	devel
Summary:	C headers for developing programs that will embed CLIPS
Requires:	clips-libs = %{version}-%{release}
Requires:	ncurses-devel pkgconfig

%description	devel
This package contains the libraries and header files needed for
developing embedded CLIPS applications.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

%package	xclips
Summary:	X interface to the CLIPS expert system
Requires:	%{name} = %{version}-%{release}
Requires:	hicolor-icon-theme

%description	xclips
X interface to CLIPS.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

%package	doc
Summary:	Documentation and examples for the CLIPS expert system
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:	noarch
%endif

%description	doc
This package contains documentation for the CLIPS library as well as numerous 
examples.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

The following are some of the documents in this package:
- Proceedings of the Third Conference on CLIPS, 1994 (3CCP.pdf)
- Application abstracts (abstract.pdf)
- CLIPS Reference Manual, Volume I, Basic Programming Guide (bpg.pdf,bpg.htm)
- CLIPS Reference Manual, Volume II, Adv. Programming Guide (apg.pdf, apg.htm)
- CLIPS Reference Manual, Volume III, Interfaces Guide (ig.pdf,ig.htm)
- CLIPS Architecture Manual (arch5-1.pdf)
- CLIPS Users Guide (ug.pdf,ug.htm)

%package	emacs
Summary:	EMACS add-ons for the CLIPS expert system
Requires:	emacs-common
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildArch:	noarch
%endif

%description	emacs
This package contains CLIPS emacs scripts.

CLIPS (C Language Integrated Production System) is an expert system
development tool which provides a complete environment for the 
construction of rule and/or object based expert systems. 

Created in 1985 by NASA at the Johnson Space Center, CLIPS is now 
widely used throughout the government, industry, and academia.

%prep
%setup -q -n %{name}-%{version}%{?svnver} -a 1
%{__mv} %{name}-%{version}%{?svnver}-doc/* documentation/ 

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%{__install} -p --mode=0644 -D documentation/clips-init.el %{buildroot}%{_datadir}/emacs/site-lisp/site-start.d/clips-init.el
%{__install} -p --mode=0644 -D documentation/clips-mode.el %{buildroot}%{_datadir}/emacs/site-lisp/clips-mode.el
%{__install} -p --mode=0644 -D documentation/inf-clips.el %{buildroot}%{_datadir}/emacs/site-lisp/inf-clips.el

# create icons
# create 16x16, 32x32, 64x64, 128x128 icons
for s in 16 32 64 128 ; do
  %{__mkdir_p} %{buildroot}/%{_datadir}/icons/hicolor/${s}x${s}/apps/
  convert -scale ${s}x${s} \
    x_window_system/xinterface/xclips.png \
    %{buildroot}/%{_datadir}/icons/hicolor/${s}x${s}/apps/xclips.png
done

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	x_window_system/xinterface/xclips.desktop

%ldconfig_scriptlets libs


%files
%{_bindir}/clips

%files libs
%{_libdir}/*.so.*
%{_datadir}/%{name}/
%doc COPYING_CLIPS_LINUX
%doc README_CLIPS_LINUX

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}/

%files xclips
%{_bindir}/xclips
%{_bindir}/xclips-color
%{_datadir}/icons/hicolor/*x*/apps/xclips.png
%{_datadir}/applications/*xclips.desktop

%files doc
%doc examples/
%doc documentation/3CCP.pdf
%doc documentation/abstract.pdf 
%doc documentation/apg.pdf
%doc documentation/architecture5-1.pdf 
%doc documentation/bpg.pdf 
%doc documentation/ig.pdf
%doc documentation/ug.pdf 
%doc documentation/html/

%files emacs
%{_datadir}/emacs/site-lisp/site-start.d/clips-init.el
%{_datadir}/emacs/site-lisp/clips-mode.el
%{_datadir}/emacs/site-lisp/inf-clips.el
 
%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.23.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Till Hofmann <thofmann@fedoraproject.org> - 6.30.0-0.22.20090722svn
- Allow linking with `-fcommon`

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.21.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.20.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.19.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.18.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.17.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.30.0-0.16.20090722svn
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.15.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.14.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.13.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.30.0-0.12.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.30.0-0.11.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.30.0-0.10.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.30.0-0.9.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.30.0-0.8.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 6.30.0-0.7.20090722svn
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.30.0-0.6.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.30.0-0.5.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.30.0-0.4.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.30.0-0.3.20090722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Dan Horák <dan[at]danny.cz> 6.30.0-0.2.20090722svn
- remove xorg-x11-server-Xorg from BRs, it doesn't exist on s390(x) and builds fine without it

* Mon Jul 27 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.30.0-0.1.20090722svn
- New release
- Removed multiple sources and patches that are in new release
- Improved summaries and descriptions
- Added clips-emacs subpackage

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.24-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-27
- Updated desktop entry file to add categories and remove deprecated items
- Added hicolor-icon-theme requires to xclips
- Install xclips icons to hicolor directory
- Added validation to desktop file
- Added icon cache rebuild to pre and post sections for xclips
- Added preserve to file installs
- Made install modes explicit
- Added pkgconfig and ImageMagick to build requires
- Updated URL
- Updated source URL's
- Added html docs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.24-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 6.24-25
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-24
- Added automake, autoconf and libtool to build requires

* Sat Aug 25 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-23
- Added patch to fix time function; closes bug 249995
- Fixed the version in the xclips.desktop file and removed it from the linux patch
- Added the linux patch and xclips.desktop files to cvs
- Changed the linux patch from a bzip file to a normal patch file
- Removed the pre-generated autotools files from the linux patch
- Added running of autogen.sh prior to running configure to build autotools files
- Added timestamp preservation to install
- Updated (not changed) license to new tag GPLv2

* Fri Feb 02 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-22
- Bump release to build FC-5 and devel against new patch

* Fri Feb 02 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-21
- New clips patch builds against ncurses instead of libtermcap
- Changed all requires of libtermcap-devel to ncurses-devel

* Sun Aug 27 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-20
- Bump release for mass rebuild

* Mon Jul 31 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-19
- Remove autoconf config.h from linux patch
- Added clips-config.h with CLIPS_HELPFILE define to linux patch

* Sat Jul 08 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-18
- Added FunctionContext.zip patch
- Removed objrtmch.c from linux patch and changed to download patch
- Added bug fix report num 0873 to docs

* Fri Jul 07 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-17
- Changed UNIX_V define to UNIX_7 for upstream optimizations

* Fri Jul 07 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-16
- Bumped release for make sources error

* Fri Jul 07 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-15
- Added objrtmch.c upstream patch to general patch fixing pattern match bug

* Fri Jun 30 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-14
- Bumped release to satisfy make tag

* Fri Jun 30 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-13
- Bumped release number to fix broken upgrade path

* Thu Jun 22 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-8
- Fixed pkgconfig .pc from -L libdir to -Llibdir

* Thu Jun 22 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-7
- Renamed docs subpackage to doc
- Changed pkgconfig .pc to use -L libdir -lclips in patch
- Added extern "C" and ifdef __cplusplus to clips.h in patch

* Wed Jun 21 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-6
- Created docs subpackage
- Moved all pdf docs and examples into docs subpackage
- Removed Requires clips from xclips
- Added emacs mode to clips package

* Sun Jun 18 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-5
- Created libs subpackage
- Renamed x11 subpackage to xclips
- Changed install location of clips.hlp in autotools patch
- Renamed clips.png to xclips.png
- Moved xclips.desktop and xclips.png to xclips subpackage
- Modified autotools patch to build xclips.desktop to keep version tag current
- Changed xclips Requires from %%{name} to clips to be more explicit

* Sat Jun 17 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-4
- Moved ig.pdf to x11 subpackage

* Sat Jun 17 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-3
- Autotools patch now treats clips.hlp as data rather than doc

* Sat Jun 17 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-2
- Fixed pkgconfig include directory to /usr/include/clips
- Fixed help define

* Fri Jun 16 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.24-1
- New release
- Changed desktop entry name from xclips to XCLIPS
- New autotools struture builds clips and xclips in separate directories
- Moved bpg.pdf to clips main package
- Added examples from AllExamples.tar.Z
- Moved clips.hlp to clips main package
- Remove xclips.desktop source and moved it into autotools patch
- Added build for xclips color utility as xclips-color

* Thu Jun 15 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.23-2
- Added libXt-devel, libXaw-devel, libXext-devel, libXmu-devel to BuildRequires

* Tue Jun 13 2006 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 6.23-1
- Initial release
 
