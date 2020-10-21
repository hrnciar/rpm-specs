# SPEC file for AdPlug, primary target is the Fedora Extras
# RPM repository.

%define adplugdbver 2006-07-07
Name:		adplug
Version:	2.2.1
Release:	13%{?dist}
Summary:	A software library for AdLib (OPL2) emulation
URL:		http://adplug.github.io/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	http://download.sourceforge.net/%{name}/adplugdb-%{adplugdbver}.tar.gz
Patch0:		adplug-2.2.1-signed-char.patch
Patch1:		adplug-2.3.1-cve-2018-17825.patch
Patch2:		adplug-2.2.1-inline.patch
License:	LGPLv2+
BuildRequires:  gcc-c++
BuildRequires:	libbinio-devel >= 1.4
BuildRequires:	pkgconfig
BuildRequires:	texinfo
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
# This is to resolve the endless disputes of the shared data for this
# package. Whenever _sharedstatedir contains something acceptable to
# Fedora that can be used instead.
%define shareddata %{_localstatedir}/lib

%description
AdPlug is a free software, cross-platform, hardware independent AdLib
sound player library, mainly written in C++ and released under the
LGPL. AdPlug plays sound data, originally created for the AdLib (OPL2)
audio board, directly from its original format on top of an OPL2
emulator or by using the real hardware. No OPL chip is required for
playback. It supports various audio formats from MS-DOS AdLib trackers.

%package devel
Summary:        Development files for AdPlug
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:	libbinio-devel

%description devel
This package contains development files for the AdPlug AdLib
(OPL2) emulator.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
tar xvfz %{SOURCE1}
# Include these by different name
mv %{adplugdbver}/README README.adplugdb
mv %{adplugdbver}/NEWS NEWS.adplugdb

%build
rm -f ltmain.sh config.guess config.sub
libtoolize --copy --force || fail
rm -f aclocal.m4
aclocal $ACLOCAL_FLAGS || fail
rm -f depcomp install-sh missing
touch config.rpath
automake --add-missing --gnu || fail
rm -f configure
autoconf
%configure --disable-static --sharedstatedir=%{shareddata} --disable-rpath
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
mkdir -p $RPM_BUILD_ROOT%{shareddata}/%{name}
install -p -m 644 %{adplugdbver}/adplug.db $RPM_BUILD_ROOT%{shareddata}/%{name}

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%dir %{shareddata}/%{name}/
%config(noreplace) %{shareddata}/%{name}/adplug.db
%{_bindir}/adplugdb
%{_mandir}/man1/adplugdb.1*
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO
%doc NEWS.adplugdb README.adplugdb

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_infodir}/*.gz

%changelog
* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 2.2.1-9
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Robert Scheck <robert@fedoraproject.org> - 2.2.1-7
- Fix double-free in CEmuopl::~CEmuopl() (#1635881, CVE-2018-17825)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 12 2016 Linus Walleij <triad@df.lth.se> - 2.2.1-1
- New upstream version
- Run libtoolize, aclocal, automake and autoconf on build to avoid
  rpath problems
- Builds without patches

* Tue Mar 08 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.1-21
- Fix FTBFS with GCC 6 (#1307307)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1-18
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 2.1-17
- Drop buildroot tag, %%defattr, %%clean.
- Fix -devel group tag.
- Add %%_isa to -devel base package dep.
- Rebuild for libbinio (GCC 5 C++ ABI change), so deps can compile/link with this.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-11
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Linus Walleij <triad@df.lth.se> 2.1-6
- Nailed the GCC build problems to numerous include <cstring>.

* Mon Feb 11 2008 Linus Walleij <triad@df.lth.se> 2.1-5
- Patch include directives with a patch derived from Debian.

* Mon Feb 11 2008 Linus Walleij <triad@df.lth.se> 2.1-4
- Rebuild for GCC 4.3.

* Fri Jan 18 2008 Linus Walleij <triad@df.lth.se> 2.1-3
- New glibc ABI needs rebuild.

* Fri Aug 17 2007 Linus Walleij <triad@df.lth.se> 2.1-2
- License field update LGPL to LGPLv2+

* Wed Apr 11 2007 Linus Walleij <triad@df.lth.se> 2.1-1
- New upstream version.

* Tue Aug 29 2006 Linus Walleij <triad@df.lth.se> 2.0.1-2
- Rebuild for Fedora Extras 6.

* Tue Jul 25 2006 Linus Walleij <triad@df.lth.se> 2.0.1-1
- New upstream version, including several security fixes.

* Mon May 15 2006 Linus Walleij <triad@df.lth.se> 2.0-2
- Tell package to avoid rpath, import to FE after review by John Mahowald.

* Sat May 6 2006 Linus Walleij <triad@df.lth.se> 2.0-1
- Upstream release the stuff they've been working on for some time now!

* Thu Apr 6 2006 Linus Walleij <triad@df.lth.se> 1.5.1-8.20060323cvs
- Realize that /var/adplug/adplug.db is a real nice place to keep
  the database actually. And it is obviously OK to create and own
  directories under /var/lib as opposed to /var.

* Thu Mar 30 2006 Linus Walleij <triad@df.lth.se> 1.5.1-7.20060323cvs
- Patching to move database from /var/adplug to just /var since
  FHS does not like creation of directories under /var.

* Thu Mar 23 2006 Linus Walleij <triad@df.lth.se> 1.5.1-6.20060323cvs
- Hardcoding the place to store adplugdb since the dispute regarding
  its location never seem to resolve. /var/adplug should be acceptable
  for this package atleast. Also getting a bugfix from CVS.

* Sat Mar 4 2006 Linus Walleij <triad@df.lth.se> 1.5.1-5.20060228cvs
- Include adplug.db too, everyone will want it anyway

* Tue Feb 28 2006 Linus Walleij <triad@df.lth.se> 1.5.1-4.20060228cvs
- Pushed upstream to move adplugdb to sharedstatedir /usr/com

* Sun Jan 15 2006 Linus Walleij <triad@df.lth.se> 1.5.1-3.20060101cvs
- Fixed scriptlet problems under non-shell environments.
- Make adplug-devel require libbinio-devel.

* Sun Jan 08 2006 Linus Walleij <triad@df.lth.se> 1.5.1-2.20060101cvs
- Did a clean-up rollercoaster ride.

* Sun Jan 01 2006 Linus Walleij <triad@df.lth.se> 1.5.1-1.20060101cvs
- We need the CVS version to get going (fixes were initialized in
  upstream by ourselves so we should eat our own dogfood).

* Tue Oct 11 2005 Linus Walleij <triad@df.lth.se> 1.5.1-1
- First try at an AdPlug RPM.
