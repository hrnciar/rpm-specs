%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           trac-navadd-plugin
Version:        0.9.0.1
Release:        20111238svn11020%{?dist}
Summary:        Allows the addition of custom items

License:        BSD
URL:            http://trac-hacks.org/wiki/NavAddPlugin
# Produce via 'svn export -r11020 http://trac-hacks.org/svn/navaddplugin/0.9 navaddplugin'
# tar -czvf trac-navadd-plugin-0.9.svn11020.tar.gz navaddplugin
Source0:        trac-navadd-plugin-0.9.svn11020.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel, python2-setuptools
Requires:       trac >= 0.10

%description
A trac plugin that should allow you to add custom items ("buttons") 
to both the main and the meta navigation bar.

%prep
%setup -q -n navaddplugin

%build
%py2_build

%install
rm -rf $RPM_BUILD_ROOT
%py2_install

%files
%{python2_sitelib}/*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.1-20111238svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.1-20111237svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.1-20111236svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.1-20111235svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.1-20111234svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.0.1-20111233svn11020
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.1-20111232svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.1-20111231svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0.1-20111230svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.1-20111229svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.1-20111228svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.1-20111227svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.1-20111226svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.1-20111225svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0.1-20111224svn11020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Andrea Veri <averi@fedoraproject.org> - 0.9.0.1-20111223svn11020
- First package release.
