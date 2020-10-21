Summary: Game data files for Fish Fillets Next Generation
Name: fillets-ng-data
Version: 1.0.1
Release: 13%{?dist}
# The GPLv2 is included and nothing indicates "any later version". Exceptions :
# - images/menu/flags/ is Public Domain
# - font/ is GPLv2+ (taken from "freefont")
License: GPLv2
URL: http://fillets.sourceforge.net/
Source: http://downloads.sf.net/fillets/fillets-ng-data-%{version}.tar.gz
# http://sourceforge.net/p/fillets/bugs/7/
Patch0: fillets-ng-data-1.0.1-lua-5.2.patch
# For the TTF file used, instead of duplicating it 3 times here
Requires: gnu-free-sans-fonts
Requires: fillets-ng >= 1.0.1-10
Obsoletes: fillets-ng-data-cs <= 0.6.0
BuildArch: noarch

%description
Fish Fillets is strictly a puzzle game. The goal in every of the
seventy levels is always the same: find a safe way out. The fish utter
witty remarks about their surroundings, the various inhabitants of
their underwater realm quarrel among themselves or comment on the
efforts of your fish. The whole game is accompanied by quiet,
comforting music.

This package contains the data files required to run the game.


%prep
%setup -q
%patch0 -p0


%build
# Move along, nothing to see here! :-)


%install
%{__mkdir_p} %{buildroot}%{_datadir}/fillets-ng
%{__cp} -a * %{buildroot}%{_datadir}/fillets-ng/
%{__rm} %{buildroot}%{_datadir}/fillets-ng/COPYING

# Replace bundled copy of the fonts with symlinks to the original one
%{__rm} -f %{buildroot}%{_datadir}/fillets-ng/font/copyright
for FONTFILE in %{buildroot}%{_datadir}/fillets-ng/font/*.ttf; do
    %{__rm} -f ${FONTFILE}
    %{__ln_s} %{_datadir}/fonts/gnu-free/FreeSansBold.ttf ${FONTFILE}
done


%files
%dir %{_datadir}/fillets-ng/
%license COPYING
%{_datadir}/fillets-ng/font/
%{_datadir}/fillets-ng/images/
%{_datadir}/fillets-ng/music/
%{_datadir}/fillets-ng/script/
%{_datadir}/fillets-ng/sound/
%doc %{_datadir}/fillets-ng/doc/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 David King <amigadave@amigadave.com> - 1.0.1-4
- Add lua 5.2 patch from upstream bugtracker
- Remove some obsolete tags
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 09 2015 Bruno Wolff III <bruno@wolff.to> - 1.0.1-2
- Fix files being listed twice by the spec file
- Use proper fonts

* Fri May 08 2015 Bruno Wolff III <bruno@wolff.to> - 1.0.1-1
- Update to latest release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 15 2009 Matthias Saou <http://freshrpms.net/> 0.9.0-2
- Rebuild for devel/F-12 to have the new package payload.

* Sat Sep 12 2009 Matthias Saou <http://freshrpms.net/> 0.9.0-1
- Update to 0.9.0.
- Don't replace fonts with symlinks, as it's fragile (see #505192) and the files
  have changed names now.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8.1-3
- fix broken font requires

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Matthias Saou <http://freshrpms.net/> 0.8.1-1
- Update to 0.8.1.

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 0.8.0-2
- Replace the 3 identical bundled copies of the FreeSansBold font with symlinks
  to the original and require the freefont package (#477385).

* Sun Feb 24 2008 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Update to 0.8.0.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 0.7.4-2
- Update License field.

* Wed Jun 20 2007 Matthias Saou <http://freshrpms.net/> 0.7.4-1
- Update to 0.7.4.
- Move all files from datadir/games/ to datadir/.
- Switch to use downloads.sf.net source URL.

* Fri Nov 10 2006 Matthias Saou <http://freshrpms.net/> 0.7.1-2
- Add pairs patch for lua 5.1 compatilibity (#212920, Ivo Danihelka).

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Minor spec file changes.

* Tue Aug 23 2005 Richard Henderson <rth@redhat.com> 0.7.1-1
- Update to 0.7.1. Obsolete the separate fillet-ng-data-cs package.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.6.1-2
- rebuilt

* Tue Feb  1 2005 Matthias Saou <http://freshrpms.net/> 0.6.1-1
- Split sources into separate source rpms (for data to be noarch).

