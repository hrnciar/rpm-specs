# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-pukllanapac
Version:        13
Release:        8%{?dist}
Summary:        A sliding puzzle game

License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/Pukllanapac
Source0:        https://github.com/sugarlabs/pukllanapac/archive/v%{version}.tar.gz

BuildRequires:  python2 python2-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.97.0

%description
Pukllanapac is a sliding puzzle game; the objective is to rearrange 
tiles so that all of the circles (and semicircles) are composed 
of sectors of the same color. There are three different patterns: 
circles, triangles and hexagons. Drag tiles to swap their position; 
click on tiles to rotate them.

%prep
%autosetup -n pukllanapac-%{version}

sed -i 's/python/python2/' *.py

%build
python2 ./setup.py build

%install
python2 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

%find_lang org.sugarlabs.PukllanapacActivity

%files -f org.sugarlabs.PukllanapacActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Pukllanapac.activity/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 13-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 13-3
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 13-1
- Release version 13

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-3
- Release version 11 for gtk3

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 27 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-1
- Release version 11
- gtk 3 port

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Kalpa Welivitigofa <callkalpa@gmail.com> - 9-1
- Release version 9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild


* Tue Dec 20 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 8-2
- removed %%{__python} macro

* Thu Dec 15 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 8-1
- initial packaging
