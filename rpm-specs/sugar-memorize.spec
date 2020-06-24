# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:          sugar-memorize
Version:       57
Release:       1%{?dist}
Summary:       Memorize for Sugar
License:       GPLv2+
URL:           http://wiki.sugarlabs.org/go/Activities/Memorize
Source0:       https://download.sugarlabs.org/sources/honey/Memorize/Memorize-%{version}.tar.bz2
BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: gstreamer-plugins-espeak
Requires: sugar

%description
The game memorize is about finding matching pairs. A pair can consist of any
multimedia object. At the moment these are images, sounds and text but this
could be extended to animations or movie snippets as well. Which pairs do 
match is up to the creator of the game. Memorize is actually more than just
a predefined game you can play, it allows you to create new games yourself
as well.

%prep
%autosetup -n Memorize-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build


%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
%find_lang org.laptop.Memorize


%files -f org.laptop.Memorize.lang
%license COPYING
%doc AUTHORS NEWS
%{sugaractivitydir}/Memorize.activity/
%{_datadir}/metainfo/org.laptop.Memorize.appdata.xml


%changelog
* Mon Feb 10 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 57-1
- Update to 57
- Add file for package data

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 55-1
- Update to 55

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 54-1
- Update to 54

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 52-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 52-1
- Update to 52

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 51-4
- Fix FTBFS issue

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 51-1
- Update to 51

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 49-1
- Update to 49

* Sun Jul 27 2014 Peter Robinson <pbrobinson@fedoraproject.org> 48-1
- Update to 48

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 47-1
- Update to 47

* Sun Jan 12 2014 Peter Robinson <pbrobinson@fedoraproject.org> 46-1
- Update to v46, build using sugar gtk3 support

* Thu Oct 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 45-3
- Add gstreamer-python runtime dependency

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  2 2013 Peter Robinson <pbrobinson@fedoraproject.org> 45-1
- Update to 45

* Sat Jun 29 2013 Peter Robinson <pbrobinson@fedoraproject.org> 44-1
- Update to 44

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 43-1
- Update to 43

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 41-1
- Update to 41

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 39-1
- Update to 39

* Tue Sep 20 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 37-1
- Update to 37

* Wed Sep  7 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 36-4
- add missing libxml2-python dependency

* Sun May 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 36-3
- Fix Requires

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Fabian Affolter <fabian@bernewireless.net> - 35-1
- Updated to new upstream version 35

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 33-4
- recompiling .py files against Python 2.7 (rhbz#623380)

* Mon Dec 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 33-3
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 539053

* Sat Aug 08 2009 Fabian Affolter <fabian@bernewireless.net> - 33-2
- Bump release

* Tue Aug 04 2009 Fabian Affolter <fabian@bernewireless.net> - 33-1
- Changed source url, now hosted on Sugarlabs
- Updated to new upstream version 33

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 29-2
- Rebuild for Python 2.6

* Wed Nov 19 2008 Fabian Affolter <fabian@bernewireless.net> - 29-1
- updated to version 29
- changed source0 to release tarball
- removed permission hacks, end-lind-encoding, hidden files

* Thu Oct 16 2008 Fabian Affolter <fabian@bernewireless.net> - 28-1
- Initial package for Fedora
