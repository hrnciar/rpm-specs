Name:		fvwm
Version:	2.6.9
Release:	3%{?dist}
Summary:	Highly configurable multiple virtual desktop window manager

License:	GPLv2+
URL:		http://www.fvwm.org/
Source0:	https://github.com/fvwmorg/fvwm/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop

Patch1:		fvwm-0001-Change-html-viewer-to-xdg-open.patch
Patch2:		fvwm-0002-Use-mimeopen-instead-of-EDITOR.patch
# This patch will NEVER be included in the official FVWM and that's why:
#
# https://bugs.gentoo.org/show_bug.cgi?id=411811#c7
# https://github.com/ThomasAdam/fvwm/pull/4#issuecomment-5712410
#
# In short - X-servers other than X.org and Xfree86 doesn't support so many
# mouse buttons so this is a distro-specific patch.
Patch3:		fvwm-0003-Increase-number-of-mouse-buttons-supported.patch
# https://github.com/ThomasAdam/fvwm/issues/5
Patch4:		fvwm-0004-FvwmPager-be-more-careful-with-window-labels.patch

# Fedora-specific
Patch5:		fvwm-0005-Skip-install-data-hook-for-default-configs.patch

BuildRequires:  gcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext libX11-devel libXt-devel libXext-devel libXinerama-devel libXpm-devel
BuildRequires:	libXft-devel libXrender-devel
BuildRequires:	libstroke-devel perl-generators readline-devel libpng-devel fribidi-devel
BuildRequires:	librsvg2-devel
BuildRequires:	libxslt
BuildRequires:	libXcursor-devel
Requires:	xterm %{_bindir}/mimeopen

# for fvwm-bug
Requires:	%{_sbindir}/sendmail

# for fvwm-menu-headlines
Requires:	xdg-utils

# for fvwm-menu-xlock
Requires:	xlockmore

# for fvwm-menu-desktop
Requires: python3-pyxdg

%description
Fvwm is a window manager for X11. It is designed to
minimize memory consumption, provide a 3D look to window frames,
and implement a virtual desktop.


%prep
%autosetup -p1


%build
aclocal --force
autoreconf -ivf
%configure --enable-mandoc
%make_build


%install
%make_install
%find_lang %{name}
%find_lang FvwmScript
cat FvwmScript.lang >> %{name}.lang

# xsession
install -D -m0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/xsessions/%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md NEWS
%{_bindir}/*
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_datadir}/xsessions/%{name}.desktop


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.6.9-2
- Fix man-page generation (rhbz#1768223)

* Thu Sep 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.6.9-1
- Ver. 2.6.9

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.6.8-5
- Fix version string (drop unnecessary patch)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.8-4
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.6.8-1
- Ver. 2.6.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.6.7-4
- Added missing Requires - python3-pyxdg

* Tue Apr 11 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.6.7-3
- Fix issue with default python symlinking to py3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.6.7-1
- Ver. 2.6.7
- No longer supports menu auto-generation

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6.6-2
- Rebuild for readline 7.x

* Thu Jul 14 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.6.6-1
- Update to 2.6.6

* Thu Mar  3 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.6.5-12
- Apply patch no.7 which hopefully fixes rhbz#823499

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 2.6.5-9
- Fix FTBFS in Rawhide (rhbz #1106311)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.6.5-5
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.6.5-3
- Fix segfaults in FvwmPager

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.6.5-1
- Ver. 2.6.5

* Thu Apr 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 2.6.4-1
- Ver. 2.6.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.5.30-5
- Rebuild for new libpng

* Sat Mar 05 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.30-4
- Fixed FTBFS issue (rhbz #661049)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 12 2010 Adam Goode <adam@spicenitz.org> - 2.5.30-2
- Increase number of mouse buttons (#548534)

* Sun Jul 11 2010 Adam Goode <adam@spicenitz.org> - 2.5.30-1
- New upstream release, many changes, see http://www.fvwm.org/news/

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Adam Goode <adam@spicenitz.org> - 2.5.26-2
- RPM 4.6 fix for patch tag

* Wed Jun  4 2008 Adam Goode <adam@spicenitz.org> - 2.5.26-1
- Upgrade to new release
- Remove module_list patch, fixed in upstream

* Sat Feb  9 2008 Adam Goode <adam@spicenitz.org> - 2.5.24-2
- Really fix segfault (#382321)

* Sun Dec  2 2007 Adam Goode <adam@spicenitz.org> - 2.5.24-1
- New upstream release
- Fixes segfault (#382321)

* Tue Oct  2 2007 Adam Goode <adam@spicenitz.org> - 2.5.23-3
- Change htmlview to xdg-open (thanks, Ville Skyttä !)

* Mon Sep 10 2007 Adam Goode <adam@spicenitz.org> - 2.5.23-2
- Don't add gnome-libs-devel to BR (not on ppc64?)

* Mon Sep 10 2007 Adam Goode <adam@spicenitz.org> - 2.5.23-1
- New upstream release

* Tue Aug 21 2007 Adam Goode <adam@spicenitz.org> - 2.5.21-5
- Update license tag
- Rebuild for buildid

* Thu Mar 15 2007 Adam Goode <adam@spicenitz.org> - 2.5.21-4
- Don't patch configure, just patch a few files

* Thu Mar  8 2007 Adam Goode <adam@spicenitz.org> - 2.5.21-3
- Rebuild configure with autoconf >= 2.60 (for datarootdir)
- Filter out local Perl libraries from provides and requires

* Wed Feb 28 2007 Adam Goode <adam@spicenitz.org> - 2.5.21-2
- Shorten description
- Enable auto-generate menus in the Setup Form config generator
- Use htmlview instead of netscape
- Use mimeopen instead of EDITOR
- Add more Requires

* Sun Jan 21 2007 Adam Goode <adam@spicenitz.org> - 2.5.21-1
- New specfile for Fedora
