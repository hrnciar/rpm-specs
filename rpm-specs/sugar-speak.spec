# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-speak
Version:        58
Release:        2%{?dist}
Summary:        Speak for Sugar

License:        GPLv2+ and GPLv3+
URL:            http://wiki.laptop.org/go/Speak
Source0:        https://download.sugarlabs.org/sources/honey/Speak/Speak-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3
BuildRequires:  sugar-toolkit-gtk3
Requires:       espeak-ng
Requires:       gstreamer-plugins-espeak
Requires:       python3-numpy
Requires:       sugar
Requires:       sugar-toolkit-gtk3

%description
Speak is a talking face for the XO laptop. Anything you type will be spoken
aloud using the XO's speech synthesizer, espeak. You can adjust the accent,
rate and pitch of the voice as well as the shape of the eyes and mouth. This
is a great way to experiment with the speech synthesizer, learn to type or 
just have fun making a funny face for your XO.  

%prep
%autosetup -n Speak-%{version}

sed -i 's/python/python3/' bot/*.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
find  %{buildroot}%{sugaractivitydir}Speak.activity/activity.py  -type f -name \* -exec chmod 644 {} \;
%find_lang vu.lux.olpc.Speak

%files -f vu.lux.olpc.Speak.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Speak.activity/

%changelog
* Thu Jan 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> 58-2
- Python3 fixes

* Thu Jan 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> 58-1
- New 58 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 57-1
- New 57 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 54-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 54-3
- Various Requires fixes and spec cleanups

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 54-1
- New 54 release

* Sat Apr 22 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 52-1
- New 52 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 51-1
- New 51 release

* Wed Apr 15 2015 Peter Robinson <pbrobinson@fedoraproject.org> 50-1
- New 50 release

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 49-2
- Add Requires sugar-toolkit

* Wed Dec 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 49-1
- New 49 release

* Tue Nov 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 48-2
- Fix replying to questions

* Wed Jul 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 48-1
- New 48 release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Peter Robinson <pbrobinson@fedoraproject.org>
- Add gstreamer-python runtime dependency

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 47-1
- New 47 release

* Mon May 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 46-1
- New 46 release

* Tue Mar  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 45-1
- New 45 release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> 44-1
- New 44 release
