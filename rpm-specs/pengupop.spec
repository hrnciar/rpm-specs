Name:           pengupop
Version:        2.2.2
Release:        25%{?dist}
Summary:        Networked Game in the vein of Move/Puzzle Bobble

License:        GPLv2+
URL:            http://www.junoplay.com/pengupop
Source0:        http://www.junoplay.com/files/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  SDL-devel, zlib-devel, desktop-file-utils

%description
Finally a networked multiplayer game in the vein of the puzzle classic Bust a
Move/Puzzle Bobble. Beat your friends in this addictive game, or play against
a random opponent! The purpose of this game is to shoot colored orbs into your
playfield, so they form groups of three or more. You win if you manage to
remove all orbs. You lose if any orb attaches below the white line.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags} CFLAGS="$CFLAGS -D_FORTIFY_SOURCE=0" LIBS="-lm"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp pengupop.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
        pengupop.desktop


%files
%doc AUTHORS COPYING
%{_bindir}/pengupop
%{_datadir}/applications/pengupop.desktop
%{_datadir}/icons/hicolor/48x48/apps/pengupop.png


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.2-19
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 2.2.2-10
- Drop desktop vendor tag.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 25 2010 Jon Ciesla <limb@jcomserv.net> 2.2.2-6
- Fix for dsolink FTBFS, BZ 599890.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> 2.2.2-3
- GCC 4.3 rebuild.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> 2.2.2-2
- License tag correction.

* Thu Mar 01 2007 Jon Ciesla <limb@jcomserv.net> 2.2.2-1
- Bumped to upstream.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.1.4-3
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 13 2006 Hugo Cisneiros <hugo@devin.com.br> 2.1.4-2
- Rebuilt for FC6

* Mon Aug 14 2006 Hugo Cisneiros <hugo@devin.com.br> 2.1.4-1
- New upstream release

* Sun Aug  6 2006 Hugo Cisneiros <hugo@devin.com.br> 2.1.0-1
- New upstream release
- Removed extra png and desktop file due to inclusion into
  the upstream version

* Sun Jun 18 2006 Hugo Cisneiros <hugo@devin.com.br> 2.0.2-2
- Added desktop-file-utils BR
- Removed description inconsistency

* Sun Jun 18 2006 Hugo Cisneiros <hugo@devin.com.br> 2.0.2-1
- Initial RPM release
