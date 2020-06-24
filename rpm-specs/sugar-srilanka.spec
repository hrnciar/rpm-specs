# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:		sugar-srilanka
Version:	3 
Release:	12%{?dist}
Summary:	Game about the geography of Sri Lanka

License:	GPLv3+
URL:		http://activities.sugarlabs.org//en-US/sugar/addon/4600
Source0:	http://activities.sugarlabs.org/en-US/sugar/downloads/file/28223/i_know_sri_lanka-%{version}.xo

BuildRequires:	python2-devel sugar-toolkit gettext 
BuildArch:	noarch
Requires:	sugar
Requires:	sugar-toolkit

%description
Game about the geography of Sri Lanka.

%prep
%setup -q -n IknowSriLanka.activity
sed -i -e '1i#!/usr/bin/python' recursos/comun/datos/commons.py
sed -i 's/python/python2/g' *.py
sed -i 's/python/python2/g' recursos/comun/datos/commons.py

%build
%{__python2} ./setup.py build

%install
%{__python2} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.ceibaljam.conozcosrilanka

%files -f org.ceibaljam.conozcosrilanka.lang
%doc COPYING README
%{sugaractivitydir}/IknowSriLanka.activity/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 3-10
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3-2
- Add Requires sugar-toolkit

* Fri Jun 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3-1
- Update to Release 3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Danishka Navin <danishka@gmail.com> - 1-3
- fixed BuildRequires
 
* Wed Jun 05 2013 Danishka Navin <danishka@gmail.com> - 1-2
- fixed one standard directory permission error

* Tue Jun 04 2013 Danishka Navin <danishka@gmail.com> - 1-1
- added python2-devel and sugar-toolkit-gtk3 to the BuildRequires

* Wed Sep 19 2012 Danishka Navin <danishka@gmail.com> - 1-0
- initial packaging