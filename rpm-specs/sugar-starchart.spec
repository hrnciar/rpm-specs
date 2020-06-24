# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:		sugar-starchart
Version:	16
Release:	13%{?dist}
Summary:	Display a map of the sky showing the position of the visible stars	

License:	GPLv2+
URL:		http://wiki.laptop.org/go/StarChart 
Source0:	http://download.sugarlabs.org/sources/honey/StarChart/StarChart-%{version}.tar.bz2

BuildRequires:	sugar-toolkit gettext python2-devel
BuildArch:	noarch
Requires:	sugar
Requires:	sugar-toolkit

%description
This activity will display a map of the sky showing the position 
of the visible stars, some of the larger and brighter deep-sky 
objects (DSOs), the "classical" planets, the sun and the moon. 

%prep
%setup -q -n StarChart-%{version}
sed -i "s|\r||g" NEWS
sed -i 's/python/python2/g' setup.py
chmod 644 activity/*

%build
%{__python2} ./setup.py build

%install
%{__python2} ./setup.py install --prefix=%{buildroot}%{_prefix}
%find_lang org.laptop.StarChart

%files -f org.laptop.StarChart.lang
%license COPYING
%doc NEWS 
%{sugaractivitydir}/StarChart.activity/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 16-11
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 16-3
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Danishka Navin <danishka@gmail.com> - 16-1
- removed sugar-toolkit-gtk3 and added sugar-toolkit to BuildRequires

* Tue Nov 19 2013 Danishka Navin <danishka@gmail.com> - 16-0
- updated to version 16

* Mon Jun 10 2013 Danishka Navin <danishka@gmail.com> - 15-2
- removed backslash between %%{buildroot} and %%{_prefix}
- fixed script-without-shebang rpmlint error

* Mon Jun 10 2013 Danishka Navin <danishka@gmail.com> - 15-1
- initial packaging

