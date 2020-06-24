# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:		sugar-castle
Version:	23
Release:	16%{?dist}
Summary:	A game of discovery and strategy inspired by the Adventure games of the 70s

License:	GPLv3+
URL:		http://activities.sugarlabs.org/en-US/sugar/addon/4397
Source0:	http://mirror.aarnet.edu.au/pub/sugarlabs/activities/4397/castle-%{version}.xo

BuildRequires:	python2-devel sugar-toolkit gettext 
BuildArch:	noarch
Requires:	sugar 
Requires:	sugar-toolkit

%description
A game of discovery and strategy inspired by the Adventure games of the 70s. 

%prep
%setup -q -n Castle.activity

chmod -x *.py
chmod -x data/*.dat
chmod -x  activity/activity.svg
chmod +x setup.py Castle.py

sed -i "s|\r||g" Castle.py
sed -i "s|\r||g" activity/activity.svg
sed -i "s|python|python2|g" setup.py
sed -i "s|python|python2|g" Castle.py

%build
%{__python2} ./setup.py build

%install
%{__python2} ./setup.py install --prefix=%{buildroot}%{_prefix}

%files 
%doc MANIFEST
%{sugaractivitydir}/Castle.activity/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 23-14
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 23-6
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Danishka Navin <danishka@gmail.com> - 23-4
- removed "#sed -i 's/\r//' Castle.py" from the %%prep section

* Tue Aug 06 2013 Danishka Navin <danishka@gmail.com> - 23-3
- corrected spec as per suggestions of the review bug 843678

* Thu Jun 06 2013 Danishka Navin <danishka@gmail.com> - 23-2
- removed sed -i -e '1i#!%%{__python}' activity/activity.svg entry

* Sun Jul 15 2012 Danishka Navin <danishka@gmail.com> - 23-1
- initial packaging
