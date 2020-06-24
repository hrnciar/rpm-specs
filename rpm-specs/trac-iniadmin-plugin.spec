# Fill these in with the latest info:
%global svnrev 17525
%global svndate 20190925

Name:           trac-iniadmin-plugin
Version:        0.5.1
Release:        1.%{svndate}svn%{svnrev}%{?dist}
Summary:        Expose all TracIni options using the Trac 0.11 config option API

License:        BSD
URL:            http://trac-hacks.org/wiki/IniAdminPlugin
# Source comes from Trac right now: http://trac-hacks.org/changeset/{svnrev}/iniadminplugin/0.11?old_path=/&filename=iniadminplugin/0.11&format=zip
Source0:        iniadminplugin_0.11-r%{svnrev}.zip

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       trac >= 0.11, python2-setuptools

%description
This plugin uses the new configuration option API in Trac 0.11+ to allow
modification of any field exposed through this mechanism.

This currently includes all core Trac settings, and although no plugins are
taking advantage of this yet, I'm sure it will only be a matter of time :)

Note: Many Trac options require a restart of the server process, so your 
changes may not take effect until that is done.

%prep
%setup -n iniadminplugin/0.11 -q
# Confirm version number matches since 0.11 is the API version, not the package version
grep -q "version='%{version}'" setup.py


%build
%py2_build


%install
rm -rf $RPM_BUILD_ROOT
# skip-build doesn't work on el4
%py2_install

 

%files
# For noarch packages: sitelib
%{python2_sitelib}/*


%changelog
* Tue May 05 2020 Aaron D. Marasco <fedora-rpm-trac@marascos.net> - 0.5.1-1.20190925svn17525
- Bump to upstream 0.5.1 (svn 17525)
- Add build-time check for version numbering

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10.20151226svn13607
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9.20151226svn13607
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8.20151226svn13607
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7.20151226svn13607
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Iryna Shcherbina <ishcherb@redhat.com>
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2.20151226svn13607
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Kevin Fenzi <kevin@scrye.com> - 0.3-1.20151226svn13607
- Update to 0.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8.20120808svn11914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7.20120808svn11914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6.20120808svn11914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.2-5.20120808svn11914
- Bumped the spec version to fix F18 -> F19 upgrade path

* Fri Feb 22 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.2-3.20120808svn11914
- rebuilt

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2.20120808svn11914
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 08 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.2-1.20120808svn11914
- Updated version for 0.11 from SVN

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4.20101209svn9652
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3.20101209svn9652
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2.20101209svn9652
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Jesse Keating <jkeating@redhat.com> - 0.2-1.20101209svn9652
- New upstream version

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-8.20091026svn6877
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Oct 26 2009 Jesse Keating <jkeating@redhat.com> - 0.1-7.20091026svn3915
- Update for 0.11

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5.20071126svn2824
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.20071126svn2824
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1-3.20071126svn2824
- Rebuild for Python 2.6

* Wed Dec 05 2007 Jesse Keating <jkeating@redhat.com> - 0.1-2.20071126svn2824
- Change the url to point to the exact svn rev we're packaging.

* Mon Nov 26 2007 Jesse Keating <jkeating@redhat.com> - 0.1-1.20071126svn2824
- Initial package for Fedora
