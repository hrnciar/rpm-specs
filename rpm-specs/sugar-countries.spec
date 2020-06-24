# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-countries
Version:        33
Release:        18%{?dist}
Summary:        A game to play with identifying countries

License:        GPLv3+
URL:            http://activities.sugarlabs.org/en-US/sugar/addon/4528
Source0:        http://activities.sugarlabs.org/downloads/file/27834/countries-%{version}.xo

BuildRequires:  python2-devel sugar-toolkit gettext
BuildArch:      noarch
Requires:       sugar
Requires:       sugar-toolkit

%description
Countries is a game where players have to type in a country for
each letter of the alphabet. Successes are rewarded with the
display of the country's flag. The activity consists of the
English names of 212 countries.

%prep
%setup -q -n Countries.activity
chmod +x Countries.py
sed -i 's/\r//' Countries.py

sed -i 's/python/python2/' *.py

%build
%{__python2} ./setup.py build

%install
%{__python2} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%files 
%{sugaractivitydir}/Countries.activity/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 33-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 33-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 33-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 33-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 33-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-11
- Build for f25

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 33-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 33-7
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-2
- changed url
- removed chmod +x for setup.py in prep

* Sun Feb 19 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-1
- initial packaging
