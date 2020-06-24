%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           trac-tocmacro-plugin
Version:        0.11.0.0.3
Release:        20111241svn11062%{?dist}
Summary:        Trac plugin table of content macro

License:        BSD
URL:            http://trac-hacks.org/wiki/TocMacro
# Produce via 'svn export -r11062 http://trac-hacks.org/svn/tocmacro/0.11 tocmacro'
# tar -czvf trac-tocmacro-plugin-0.11.svn11062.tar.gz tocmacro
Source0:        trac-tocmacro-plugin-0.11.svn11062.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel, python2-setuptools
Requires:       trac >= 0.10

%description
The TocMacro's Trac plugin generates a table of contents for
the current page or a set of pages.

%prep
%setup -q -n tocmacro

%build
%py2_build

%install
rm -rf $RPM_BUILD_ROOT
%py2_install

%files
%{python2_sitelib}/*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.0.3-20111241svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.0.3-20111240svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.0.3-20111239svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.0.3-20111238svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.0.3-20111237svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11.0.0.3-20111236svn11062
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.0.3-20111235svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.0.3-20111234svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.0.3-20111233svn11062
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.0.3-20111232svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.0.3-20111231svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.0.3-20111230svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.0.3-20111229svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.0.3-20111228svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.0.3-20111227svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.0.3-20111226svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 25 2011 Andrea Veri <averi@fedoraproject.org> - 0.11.0.0.3-20111225svn11062
- First package release.
