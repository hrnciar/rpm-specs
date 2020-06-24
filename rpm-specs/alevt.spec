Name: alevt
Version: 1.6.2
Release: 34%{?dist}
Summary: Teletext decoder/browser
License: GPLv2
URL: http://goron.de/~froese
Source: http://goron.de/~froese/%{name}/%{name}-%{version}.tar.gz
Source1: alevt.desktop
Patch0: alevt-1.6.2-pixmap.patch
Patch1: alevt-1.6.2-manpath.patch
Patch2: alevt-1.6.2-rus-greek.patch
Patch3: alevt-1.6.2-doublefont.patch
Patch4: alevt-1.6.2-zlib.patch
BuildRequires:  gcc
BuildRequires: libX11-devel
BuildRequires: libpng-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick

%description
AleVT is a teletext/videotext decoder and browser for the
vbi (/dev/vbi) device and X11.  It features multiple windows,
a page cache, regexp searching, built-in manual, and more.
There's also a program to get the time from teletext and
one to capture teletext pages from scripts.


%prep
%setup -q
%patch0 -p1 -b .pixmap
%patch1 -p1 -b .manpath
%patch2 -p1 -b .rusgreek
%patch3 -p1 -b .double
%patch4 -p1 -b .zlib

%build
# alevt does not have standard build system, so we populate OPT, 
# which is internal build variable to accommodate Fedora opt flags
# This will produce lot of garbage on output.
make %{?_smp_mflags} -e OPT="%{optflags}"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

make USR_X11R6=%{_prefix} MAN=%{_mandir} rpm-install
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%files
%{_bindir}/alevt
%{_bindir}/alevt-date
%{_bindir}/alevt-cap
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}*
%{_datadir}/pixmaps/mini-alevt.xpm
%doc README CHANGELOG COPYRIGHT

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-20
- add patch to build against newer zlib (fixes #843204)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.6.2-17
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.6.2-15
- Update desktop file according to F-12 FedoraStudio feature

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 30 2009 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-13
- update patch0 fix bug #498775 - direct teletext page access

* Mon Apr 13 2009 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-12
- new patches from Alexey

* Mon Apr 13 2009 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-11
- rebuild with corrected patch2

* Fri Apr 10 2009 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-10
- new patch for chrilic fonts from Alexey Loukianov (mooroon2@mail.ru)
- updated doublefont patch

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 05 2008 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-8
- update build requires

* Fri Dec 05 2008 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-7
- add doublefont patch; fixes #459294

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-6
- fix for #458818

* Tue Jul 28 2008 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-5
- Misc cleanups
- Patch for man install

* Tue Jul 22 2008 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-4
- misc cleanups

* Mon Jun 30 2008 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-3
- better debuginfo handling, drop configure (Michal Nowak)

* Sun Jun 29 2008 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-2
- Misc cleanups
- Use fedora's CFLAGS

* Wed Jun 11 2008 Lucian Langa <cooly@gnome.eu.org> - 1.6.2-1
- Update to fedora specs
- Patched against wrong pixmaps directory
- Force to build with debuginfo
- Added .desktop file

* Mon Jun 14 1999 Karsten Hopp <karsten@delix.de>
- removed old patch from specfile
- removed LibC-Macro
- added '-oldbttv' to the package description.

* Sun May 23 1999 Karsten Hopp <karsten@delix.de>
- several minor patches of Marios spec-file:
- german descriptions
- buildroot (patched Makefile)
- some changed install-paths
