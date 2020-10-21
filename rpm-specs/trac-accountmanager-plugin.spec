%global svnrev  17619
%global svndate 20191212

Name:           trac-accountmanager-plugin
Version:        0.6
Release:        0.2.r17619%{?dist}
Summary:        Trac plugin for account registration and management
License:        Copyright only
URL:            http://trac-hacks.org/wiki/AccountManagerPlugin
Source0:        TracAccountManager-%{version}dev-r%{svnrev}.tar.bz2
BuildArch:      noarch
BuildRequires:  python2-devel >= 2.7

# Source sometimes comes from SVN repository at trac-hacks.org
Source1:        pull-from-svn.sh
Patch0:         TracAccountManager-0.5dev-r16888-shellbang.patch

# Fix test failure with trac 1.4
Patch1:         TracAccountManager-0.6dev-r17619-test.patch

# Required for import of pkg_resources
BuildRequires:  python2-setuptools
Requires:       python2-setuptools

# Needed for translations
BuildRequires:  python2dist(babel) >= 0.9.5
Requires:       python2dist(babel) >= 0.9.5

# Needed for templates
BuildRequires:  python2dist(genshi) >= 0.6
Requires:       python2dist(genshi) >= 0.6

# This package is explicitly for trac ≥ 1.2
BuildRequires:  trac >= 1.2
Requires:       trac >= 1.2

%description
The AccountManagerPlugin offers several features for managing user accounts:

 * allow users to register new accounts
 * login via an HTML form instead of using HTTP authentication
 * allow existing users to change their passwords or delete their accounts
 * send a new password to users who've forgotten their password
 * administer user accounts using the trac web interface

%prep
%setup -n TracAccountManager-%{version}dev-r%{svnrev} -q

# Use /usr/bin/python2 rather than /usr/bin/env python
%patch0

# Fix test failure with trac 1.4
# https://trac-hacks.org/ticket/13747
%patch1

%build
%py2_build

%install
%py2_install

# Don't need to package this
rm %{buildroot}%{python2_sitelib}/acct_mgr/locale/.placeholder

%check
%{__python2} setup.py test

%files
%license COPYING
%doc changelog README README.update
%doc contrib/fix-session_attribute-failed_logins.py contrib/sessionstore_convert.py
%dir %{python2_sitelib}/acct_mgr/
%{python2_sitelib}/acct_mgr/*.py*
%{python2_sitelib}/acct_mgr/htdocs/
%{python2_sitelib}/acct_mgr/opt/
%{python2_sitelib}/acct_mgr/templates/
%dir %{python2_sitelib}/acct_mgr/locale/
%dir %{python2_sitelib}/acct_mgr/locale/cs/
%dir %{python2_sitelib}/acct_mgr/locale/cs/LC_MESSAGES/
%lang(cs) %{python2_sitelib}/acct_mgr/locale/cs/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/de/
%dir %{python2_sitelib}/acct_mgr/locale/de/LC_MESSAGES/
%lang(de) %{python2_sitelib}/acct_mgr/locale/de/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/es/
%dir %{python2_sitelib}/acct_mgr/locale/es/LC_MESSAGES/
%lang(es) %{python2_sitelib}/acct_mgr/locale/es/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/et/
%dir %{python2_sitelib}/acct_mgr/locale/et/LC_MESSAGES/
%lang(et) %{python2_sitelib}/acct_mgr/locale/et/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/fi/
%dir %{python2_sitelib}/acct_mgr/locale/fi/LC_MESSAGES/
%lang(fi) %{python2_sitelib}/acct_mgr/locale/fi/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/fr/
%dir %{python2_sitelib}/acct_mgr/locale/fr/LC_MESSAGES/
%lang(fr) %{python2_sitelib}/acct_mgr/locale/fr/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/he/
%dir %{python2_sitelib}/acct_mgr/locale/he/LC_MESSAGES/
%lang(he) %{python2_sitelib}/acct_mgr/locale/he/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/id_ID/
%dir %{python2_sitelib}/acct_mgr/locale/id_ID/LC_MESSAGES/
%lang(id_ID) %{python2_sitelib}/acct_mgr/locale/id_ID/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/it/
%dir %{python2_sitelib}/acct_mgr/locale/it/LC_MESSAGES/
%lang(it) %{python2_sitelib}/acct_mgr/locale/it/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/ja/
%dir %{python2_sitelib}/acct_mgr/locale/ja/LC_MESSAGES/
%lang(ja) %{python2_sitelib}/acct_mgr/locale/ja/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/nl/
%dir %{python2_sitelib}/acct_mgr/locale/nl/LC_MESSAGES/
%lang(nl) %{python2_sitelib}/acct_mgr/locale/nl/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/pl/
%dir %{python2_sitelib}/acct_mgr/locale/pl/LC_MESSAGES/
%lang(pl) %{python2_sitelib}/acct_mgr/locale/pl/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/pt_BR/
%dir %{python2_sitelib}/acct_mgr/locale/pt_BR/LC_MESSAGES/
%lang(pt_BR) %{python2_sitelib}/acct_mgr/locale/pt_BR/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/ru/
%dir %{python2_sitelib}/acct_mgr/locale/ru/LC_MESSAGES/
%lang(ru) %{python2_sitelib}/acct_mgr/locale/ru/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/sv/
%dir %{python2_sitelib}/acct_mgr/locale/sv/LC_MESSAGES/
%lang(sv) %{python2_sitelib}/acct_mgr/locale/sv/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/te/
%dir %{python2_sitelib}/acct_mgr/locale/te/LC_MESSAGES/
%lang(te) %{python2_sitelib}/acct_mgr/locale/te/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/tr/
%dir %{python2_sitelib}/acct_mgr/locale/tr/LC_MESSAGES/
%lang(tr) %{python2_sitelib}/acct_mgr/locale/tr/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/uk/
%dir %{python2_sitelib}/acct_mgr/locale/uk/LC_MESSAGES/
%lang(uk) %{python2_sitelib}/acct_mgr/locale/uk/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/zh_CN/
%dir %{python2_sitelib}/acct_mgr/locale/zh_CN/LC_MESSAGES/
%lang(zh_CN) %{python2_sitelib}/acct_mgr/locale/zh_CN/LC_MESSAGES/acct_mgr.mo
%dir %{python2_sitelib}/acct_mgr/locale/zh_TW/
%dir %{python2_sitelib}/acct_mgr/locale/zh_TW/LC_MESSAGES/
%lang(zh_TW) %{python2_sitelib}/acct_mgr/locale/zh_TW/LC_MESSAGES/acct_mgr.mo
%{python2_sitelib}/TracAccountManager-%{version}*-py2.7.egg-info/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-0.2.r17619
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Paul Howarth <paul@city-fan.org> - 0.6-0.1.r17619
- Update to svn revision 17619
- Add patch to fix test suite for compatibility with trac 1.4
  (https://trac-hacks.org/ticket/13747)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Paul Howarth <paul@city-fan.org> - 0.5.0-1
- Update to release version 0.5.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.4.r16888
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Paul Howarth <paul@city-fan.org> - 0.5-0.3.r16888
- Update to svn revision 16888
- Use %%{python2_sitelib} rather than %%{python_sitelib}
- Fix shellbangs not to use /usr/bin/env python

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.2.r16056
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Paul Howarth <paul@city-fan.org> - 0.5-0.1.r16056
- Update to current svn snapshot for trac 1.2 compatibility

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 Paul Howarth <paul@city-fan.org> - 0.4.4-2
- Allow a question as alternative BotTrapCheck field description
- Fix the test suite so that it works with trac 1.0.2
- Use %%license where possible

* Mon Jun  9 2014 Paul Howarth <paul@city-fan.org> - 0.4.4-1
- Update to current stable release version
  - Lots of password-related fixes
  - Lots of extra translations
- NOTE: existing users should read README.update for important change details
- Package upstream's COPYING file
- Drop %%defattr, redundant since rpm 4.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.5.20120108svn11131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.4.20120108svn11131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.3.20120108svn11131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.2.20120108svn11131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Paul Howarth <paul@city-fan.org> - 0.4-0.1.20120108svn11131
- Update to current svn snapshot (from trunk for trac 0.12)
- Set timestamp on tarball to timestamp of latest change in svn
- Add new translations to %%files list
- Drop test suite patch, no longer needed
- Package changelog and README.update
- NOTE: existing users should read README.update for important change details

* Wed Feb  9 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.3.20101206svn9591
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 Paul Howarth <paul@city-fan.org> - 0.3-0.2.20101206svn9591
- Require python-genshi >= 0.6 or python-genshi06 as per trac itself
- Go to great trouble to set %%lang on translations
- Help setup.py find Genshi 0.6, which is in an egg for EPEL-6
- Add %%check section and run test suite
- Patch out errors in test suite
- BR: trac for trac.test, needed for test suite

* Tue Dec 14 2010 Paul Howarth <paul@city-fan.org> - 0.3-0.1.20101206svn9591
- Update to current svn snapshot (from trunk for trac 0.12)
- Require trac >= 0.12
- Require python-genshi >= 0.5 as per setup.py

* Fri Dec 10 2010 Ben Boeckel <mathstuf@gmail.com> - 0.2.1-0.5.20090522svn5836
- Rebuild for new trac

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.1-0.4.20090522svn5836
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Aug 28 2009 Ben Boeckel <MathStuf@gmail.com> - 0.2.1-0.3.20090522svn5836
- Remove comments
- Fix tarball

* Thu Aug 27 2009 Ben Boeckel <MathStuf@gmail.com> - 0.2.1-0.2.20090522svn5836
- Merge spec with Paul Howarth's

* Thu Aug 06 2009 Ben Boeckel <MathStuf@gmail.com> - 0.2.1-0.1.20090522svn5836
- Initial package
