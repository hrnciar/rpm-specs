Name:           worminator-data
Version:        3.0R2.1
Release:        22%{?dist}
Summary:        Data for worminator the game
License:        GPLv2+
URL:            http://sourceforge.net/projects/worminator/
Source0:        http://download.sourceforge.net/worminator/%{name}-%{version}.tar.gz
Source1:	license.txt
Source2:        license-change.txt
BuildArch:      noarch
Requires:       worminator

%description
Data for worminator the game where you play as The Worminator and fight your
way through many levels of madness and mayhem. Worminator features nine unique
weapons, visible character damage, full screen scrolling, sound and music, and
much more!


%prep
#put the docs where %doc wants them
install -p -m 0644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_DIR


%build
#empty / notthing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/worminator
tar xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/worminator
rm $RPM_BUILD_ROOT%{_datadir}/worminator/ICON.ICO



%files
%doc license.txt license-change.txt
%{_datadir}/worminator


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-4
- Update License tag for new Licensing Guidelines compliance

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-3
- Add Requires on main package
- FE6 Rebuild

* Tue Mar 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-2
- move worminator data dir from /usr/share/games to just /usr/share to match
  the games-SIG guidelines. Sorry about the somewhat large download for
  effectivly no changes, but I wanted to make this change before FC5 release.

* Sat Mar  4 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-1
- initial Fedora Extras package
- loosely based on the SRPM from Cru:
  http://naturidentisch.de/packages/fc4/worminator/
