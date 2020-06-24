# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:		sugar-deducto
Version:	9
Release:	16%{?dist}
Summary:	A learning activity aimed towards improving children’s skills to deducing logic

# sprites.py is in MIT and all other files in GPLv3+
License:	GPLv3+ and MIT
URL:		http://activities.sugarlabs.org/en-US/sugar/addon/4220
Source0:	http://download.sugarlabs.org/sources/honey/Deducto/Deducto-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	python2-devel
BuildRequires:	sugar-toolkit
Requires:	sugar
Requires:	sugar-toolkit
BuildArch:	noarch

%description
A learning activity aimed towards improving children's skills 
to deducing logic through pattern recognition.

%prep
%setup -q -n Deducto-%{version}
rm po/aym.po
sed -i "s|\r||g" README.txt
sed -i "s|python|python2|g" setup.py

%build
%{__python2} ./setup.py build

%install
%{__python2} ./setup.py install --prefix=%{buildroot}%{_prefix}
%find_lang  in.seeta.Deducto


%files -f in.seeta.Deducto.lang
%license COPYING
%doc README.txt NEWS
%{sugaractivitydir}/Deducto.activity/


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 9-15
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 9-7
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Danishka Navin  <snavin@lists.fedoraproject.org> - 9-5
- Fixed %%BuildRequires 

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-3
- Updated the license tag with GPLv3+ and MIT

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-2
- add a comment above the license tag
- removed backslash between %%{buildroot} and %%{_prefix}

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 9-1
- initial packaging
