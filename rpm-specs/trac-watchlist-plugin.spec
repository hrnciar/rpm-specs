%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define         svn_rev 11062

Name:           trac-watchlist-plugin
Version:        0.5
Release:        0.19.svn%{svn_rev}%{?dist}
Summary:        Watchlist plugin for Trac for watching tickets or wiki pages

# GPLv3 license from setup.py
License:        GPLv3
URL:            http://trac-hacks.org/wiki/WatchlistPlugin
# Generate via 'svn export -r%{svn_rev} http://trac-hacks.org/svn/watchlistplugin/0.11 trac-watchlist-plugin-0.5 && tar -czvf trac-watchlist-plugin-0.5.%{svn_rev}.tar.gz trac-watchlist-plugin-0.5
Source0:        trac-watchlist-plugin-0.5.svn%{svn_rev}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel, python2-setuptools

Requires:       trac >= 0.11

%description
This plug-in adds a watchlist for wikis and tickets. Every logged-in user can
watch any wikis and ticket and later unwatch it. The watchlist is provided
under [/projectname]/watchlist which is added to the main navigation bar as
soon the user watches something.

This plug-in is still under development. The basic functions are implemented
but the watchlist layout might change in the future. ATM there seems to be
some issues when PostgresSQL is used as DB backend. Therefore the DB table
layout might change in the future. Feel free to test it out and provide
feedback.

%prep
%setup -q


%build
%py2_build

%install
rm -rf $RPM_BUILD_ROOT
%py2_install



%files
%doc
# For noarch packages: sitelib
%{python2_sitelib}/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.19.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.18.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.17.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.16.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.15.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5-0.14.svn11062
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.13.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.12.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.11.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.10.svn11062
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.9.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.8.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.7.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.6.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.5.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.4.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.3.svn11062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 25 2011 Jon Stanley <jonstanley@gmail.com> - 0.5-0.2.svn11062
- Correct license tag from intiial time spec was written

* Sun Dec 25 2011 Jon Stanley <jonstanley@gmail.com> - 0.5-0.1.svn11062
- New upstream release, initial import

* Fri Apr 3 2009 Jon Stanley <jonstanley@gmail.com> - 0.1-0.2.svn5357
- Update release to follow pre-release guidelines per review

* Wed Mar 25 2008 Jon Stanley <jonstanley@gmail.com> - 0.1-1.svn5357
- Initial package
