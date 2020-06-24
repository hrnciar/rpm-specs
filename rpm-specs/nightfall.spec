Name:		nightfall
Version:	1.92
Release:	4%{?dist}
Summary:	Nightfall is an astronomy application for emulation of eclipsing stars

License:	GPLv2+
URL:		http://www.hs.uni-hamburg.de/DE/Ins/Per/Wichmann/Nightfall.html
Source0:	http://www.la-samhna.de/%{name}/%{name}-%{version}.tar.gz
Patch0:		nightfall-1.62-fixmakefile.patch
Patch1:		nightfall-1.62-optflags.patch
Patch2:		nightfall-desktop.patch

BuildRequires:	gcc gtk2-devel desktop-file-utils
BuildRequires:	libjpeg-devel freeglut-devel
Requires:	gnuplot

%description
Nightfall is an astronomy application for fun, education, and science.
It can produce animated views of eclipsing binary stars,
calculate synthetic lightcurves and radial velocity curves,
and eventually determine the best-fit model for a given set of
observational data of an eclipsing binary star system.
It is, however, not able to fry your breakfast egg on your harddisk.

%prep
%setup -q
%patch0 -p2 -b .makefile
%patch1 -p1 -b .optflags
%patch2 -p1 -b .desktop

%build
%configure --with-gnuplot --enable-gnome --enable-debug
make %{_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
mv %{buildroot}%{_datadir}/nightfall/locale %{buildroot}%{_datadir}/locale
%find_lang %{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications nightfall.desktop

%files -f %{name}.lang
%doc UserManual.pdf UserManual.html README AUTHORS ChangeLog
%license COPYING
%{_bindir}/nightfall
%{_mandir}/man1/nightfall.*
%{_datadir}/nightfall/
%{_datadir}/applications/*nightfall.desktop

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 1.92-3
- Reinstante part of .optflags patch, specifically don't remove too much
  whitespace when removing options from CFLAGS

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 2019 Christian Dersch <lupinix@fedoraproject.org> - 1.92-1
- new version to fix broken package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 11 2015 Sérgio Basto <sergio@serjux.com> - 1.86-2
- Fix locale files and fix Icon path in .desktop
- Removed clean tag.

* Sat Jul 11 2015 Sérgio Basto <sergio@serjux.com> - 1.86-1
- Update to 1.86, enable openGL, improve nightfall.desktop

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 1.62-14
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.62-10
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May  9 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.62-7
- Patch for useful debuginfo package, better honor $RPM_OPT_FLAGS (#499917).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.62-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.62-5
- Include /usr/share/nightfall directory.

* Sat Mar 1  2008 Marek Mahut <mmahut@fedoraproject.org> - 1.62-4
- Rebuild for GCC 4.3 

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.62-3
- Autorebuild for GCC 4.3

* Sun Nov 25 2007 Marek Mahut <mmahut@fedoraproject.org> - 1.62-2
- Initial build.
