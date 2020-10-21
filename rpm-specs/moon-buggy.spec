# Enable oldstyle to have a nearly nothing requiring package after rebuilding
%global oldstyle 0

Summary:         Drive and jump with some kind of car across the moon
Name:            moon-buggy
Version:         1.0.51
Release:         27%{?dist}
License:         GPL+
URL:             http://seehuhn.de/pages/%{name}
Source0:         http://seehuhn.de/media/programs/%{name}-%{version}.tar.gz
Source1:         http://seehuhn.de/media/programs/%{name}-sound-%{version}.tar.gz
Source2:         %{name}.desktop
Source3:         %{name}-sound.desktop
Patch0:          moon-buggy-1.0.51-pause.patch
Patch1:          moon-buggy-1.0.51-sound.patch
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires(post):  /sbin/install-info
Requires(preun): /sbin/install-info
%endif
BuildRequires:   gcc, ncurses-devel, texinfo
%if !%{oldstyle}
BuildRequires:   esound-devel, desktop-file-utils, autoconf, automake
%endif

%description
Moon-buggy is a simple character graphics game where you drive some kind
of car across the moon's surface. Unfortunately there are dangerous craters
there. Fortunately your car can jump over them! 

The game has some resemblance of the classic arcade game moon-patrol which
was released in 1982. A clone of this game was relased for the Commodore
C64 in 1983. The present, ASCII art version of moon-buggy was written many
years later by Jochen Voss.

%prep
%setup -q -a 1
%patch0 -p1 -b .pause
%if !%{oldstyle}
%patch1 -p1 -b .sound
mv -f %{name}-%{version}/* .
autoreconf -f -i
%endif

%build
%configure --sharedstatedir=%{_localstatedir}/games
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

# Create zero-sized highscore file
touch $RPM_BUILD_ROOT%{_localstatedir}/games/%{name}/mbscore

# Install working *.desktop files and an icon
%if !%{oldstyle}
desktop-file-install --vendor "" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
desktop-file-install --vendor "" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}

install -D -p -m 644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%endif

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o ChangeLog.utf8 ChangeLog
sed -i 's|\r$||g' ChangeLog.utf8
touch -c -r ChangeLog ChangeLog.utf8
mv -f ChangeLog.utf8 ChangeLog

iconv -f iso-8859-1 -t utf-8 -o TODO.utf8 TODO
sed -i 's|\r$||g' TODO.utf8
touch -c -r TODO TODO.utf8
mv -f TODO.utf8 TODO

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi
%endif

%files 
%license COPYING
%doc ANNOUNCE AUTHORS ChangeLog README THANKS
%if !%{oldstyle}
%doc README.sound
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-sound.desktop
%endif
%attr(2755,root,games) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_infodir}/%{name}.info.*
%attr(0775,root,games) %{_localstatedir}/games/%{name}
%verify(not md5 size mtime) %config(noreplace) %attr(664,root,games) %{_localstatedir}/games/%{name}/mbscore

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.0.51-24
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Robert Scheck <robert@fedoraproject.org> 1.0.51-16
- Rebuild with sound support (#1251697)

* Sun Oct 11 2015 Robert Scheck <robert@fedoraproject.org> 1.0.51-15
- Rebuild (temporarily) without sound support (#1251697)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Robert Scheck <robert@fedoraproject.org> 1.0.51-12
- Let autoreconf add missing compile file/script (#1106238)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Robert Scheck <robert@fedoraproject.org> 1.0.51-9
- Added missing build requirement to texinfo (#914193)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.0.51-3
- Rebuilt against gcc 4.4 and rpm 4.6

* Sun Jan 04 2009 Robert Scheck <robert@fedoraproject.org> 1.0.51-2
- Avoid arbitrary modification of highscore file (#469585 #c25)

* Sat Jan 03 2009 Robert Scheck <robert@fedoraproject.org> 1.0.51-1
- Upgrade to 1.0.51
- Initial spec file for Fedora and Red Hat Enterprise Linux (based
  on a spec file of Simon Wesp <cassmodiah@fedoraproject.org>)
