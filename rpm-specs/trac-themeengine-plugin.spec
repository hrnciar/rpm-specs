%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           trac-themeengine-plugin
Version:        2.0.1
Release:        20120328svn11382%{?dist}
Summary:        Simple API and GUI for packaging and configuring Trac themes

License:        BSD
URL:            http://trac-hacks.org/wiki/ThemeEnginePlugin
# Produce via 'svn export -r11382 http://trac-hacks.org/svn/themeengineplugin/0.11 themeengineplugin'
# tar -czvf trac-themeengine-plugin-2.0.1.svn11382.tar.gz themeengineplugin
Source0:        %{name}-2.0.1.svn11382.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel, python2-setuptools
Requires:       trac >= 0.11

%description
A trac plugin that adds a simple API and GUI for
packaging and configuring Trac themes.

%prep
%setup -q -n themeengineplugin

%build
%py2_build

%install
rm -rf $RPM_BUILD_ROOT
%py2_install

%files
%doc README
%{python2_sitelib}/*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20120328svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20120327svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20120326svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20120325svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20120324svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.1-20120323svn11382
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20120322svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20120321svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20120320svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-20120319svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-20120318svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-20120317svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-20120316svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-20120315svn11382
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Andrea Veri <averi@fedoraproject.org> - 2.0.1-20120314svn11382
- First package release.
