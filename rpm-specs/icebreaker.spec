Name:       icebreaker
Version:    2.1.0
Release:    1%{?dist}
Summary:    An addictive action-puzzle game involving bouncing penguins
License:    GPLv2+

Source:     https://mattdm.org/icebreaker/2.x/icebreaker-%{version}.tar.xz
URL:        http://www.mattdm.org/icebreaker/

BuildRequires:  gcc, make
BuildRequires:  SDL-devel, SDL_mixer-devel
BuildRequires:  gawk, sed, grep
BuildRequires:  desktop-file-utils

%description
IceBreaker is an action-puzzle game in which you must capture penguins from
an Antarctic iceberg so they can be shipped to Finland, where they are
essential to a secret plot for world domination. To earn the highest Geek
Cred, trap them in the smallest space in the shortest time while losing the
fewest lives. IceBreaker was inspired by (but is far from an exact clone of)
Jezzball by Dima Pavlovsky.


%prep
%setup -q

%build
make OPTIMIZE="$RPM_OPT_FLAGS" prefix=%{_prefix}

%install
make install prefix=${RPM_BUILD_ROOT}%{_prefix}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications icebreaker.desktop


%files
%license LICENSE
%doc README README.themes TODO ChangeLog
%{_bindir}/icebreaker
%{_datadir}/applications/icebreaker.desktop
%{_datadir}/icebreaker
%{_mandir}/man6/*


%changelog
* Mon Aug 31 2020 Matthew Miller <mattdm@mattdm.org> - 2.1.0-1
- update rawhide to 2.1.0 devel release with code cleanups

* Sun Aug 30 2020 Matthew Miller <mattdm@mattdm.org> - 2.0.0-2
- license is gpl v2 or later

* Sun Aug 30 2020 Matthew Miller <mattdm@mattdm.org> - 2.0.0-1
- high scores are going to be local to each home directory; no more setgid
- update to 2.0.0

* Thu Nov 16 2006 Matthew Miller <mattdm@mattdm.org>
- working towards 1.9.9 :)

* Fri May 31 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.6

* Mon May 27 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.5

* Thu May 23 2002 Matthew Miller <mattdm@mattdm.org>
- more complex makefile allows simpler specfile

* Tue May 21 2002 Matthew Miller <mattdm@mattdm.org>
- added themes docs

* Sun May 19 2002 Matthew Miller <mattdm@mattdm.org>
- inserted some convenience stuff to enable "make rpm" magic to work
- added "isprerelease" check. No one but me should care about this.

* Sun May 19 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.2

* Fri May 17 2002 Matthew Miller <mattdm@mattdm.org>
- REALLY add .ibt files for themes

* Mon May 13 2002 Matthew Miller <mattdm@mattdm.org>
- add .ibt files for themes

* Wed May 08 2002 Matthew Miller <mattdm@mattdm.org>
- 1.9.1

* Wed Aug 01 2001 Matthew Miller <mattdm@mattdm.org>
- 1.9.0

* Mon Jul 30 2001 Matthew Miller <mattdm@mattdm.org>
- 1.2.1

* Sat Jul 28 2001 Matthew Miller <mattdm@mattdm.org>
- 1.2

* Tue Jul 24 2001 Matthew Miller <mattdm@mattdm.org>
- move man page section 6

* Sun Jul 22 2001 Matthew Miller <mattdm@mattdm.org>
- 1.1

* Fri Jul 20 2001 Matthew Miller <mattdm@mattdm.org>
- borrowed idea of using post-script to create high score file
  from Mandrake RPM. That way, it doesn't have to be marked as a config
  file, and yet won't get zapped on upgrade.
- also, modified Makefile to cope with RPM_OPT_FLAGS, again as per
  Mandrake.

* Thu Jul 19 2001 Matthew Miller <mattdm@mattdm.org>
- added man page

* Tue Jul 18 2001 Matthew Miller <mattdm@mattdm.org>
- updated to 1.09

* Thu Oct 5 2000 Matthew Miller <mattdm@mattdm.org>
- looks good to me. one-point-oh

* Tue Oct 3 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.995 
- better make process

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.99 :)

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.98

* Fri Sep 15 2000 Matthew Miller <mattdm@mattdm.org>
- first package
