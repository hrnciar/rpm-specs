%global svnrev 17127

Name:           trac-spamfilter-plugin
Version:        1.4.0
Release:        0.2.20190829svn%{svnrev}%{?dist}
Summary:        Spam-Filter plugin for Trac
License:        BSD
URL:            http://trac.edgewall.org/wiki/SpamFilter
Source0:        TracSpamFilter-%{version}dev-r%{svnrev}.tar.bz2
Source1:        pull-from-svn.sh
BuildArch:      noarch
BuildRequires:  python2-devel >= 2.6
BuildRequires:  python2-pillow
BuildRequires:  python2-setuptools
BuildRequires:  python2dist(babel)
BuildRequires:  python2dist(dnspython) >= 1.3.5
BuildRequires:  python2dist(httplib2)
BuildRequires:  python2dist(oauth2)
BuildRequires:  trac >= 1.4
Requires:       python2-pillow
Requires:       python2-setuptools
Requires:       python2dist(dnspython) >= 1.3.5
Requires:       python2dist(httplib2)
Requires:       python2dist(oauth2)
Requires:       trac >= 1.4

%description
TracSpamFilter is a plugin for Trac (http://trac.edgewall.com/) that provides
an infrastructure for detecting and rejecting spam (or other forms of
illegitimate/unwanted content) in submitted content.

%prep
%setup -n TracSpamFilter-%{version}dev-r%{svnrev} -q

%build
%py2_build

%install
%py2_install
 
%check
%{__python2} setup.py test

%files
%license COPYING
%doc README.txt
%{python2_sitelib}/TracSpamFilter-%{version}*-py*.egg-info/
%dir %{python2_sitelib}/tracspamfilter/
%{python2_sitelib}/tracspamfilter/*.py*
%{python2_sitelib}/tracspamfilter/captcha/
%{python2_sitelib}/tracspamfilter/filters/
%{python2_sitelib}/tracspamfilter/fonts/
%{python2_sitelib}/tracspamfilter/htdocs/
%{python2_sitelib}/tracspamfilter/templates/
%{python2_sitelib}/tracspamfilter/upgrades/
%dir %{python2_sitelib}/tracspamfilter/locale/
%dir %{python2_sitelib}/tracspamfilter/locale/cs/
%dir %{python2_sitelib}/tracspamfilter/locale/cs/LC_MESSAGES/
%lang(de) %{python2_sitelib}/tracspamfilter/locale/cs/LC_MESSAGES/tracspamfilter.mo
%dir %{python2_sitelib}/tracspamfilter/locale/de/
%dir %{python2_sitelib}/tracspamfilter/locale/de/LC_MESSAGES/
%lang(de) %{python2_sitelib}/tracspamfilter/locale/de/LC_MESSAGES/tracspamfilter.mo
%dir %{python2_sitelib}/tracspamfilter/locale/fr/
%dir %{python2_sitelib}/tracspamfilter/locale/fr/LC_MESSAGES/
%lang(fr) %{python2_sitelib}/tracspamfilter/locale/fr/LC_MESSAGES/tracspamfilter.mo
%dir %{python2_sitelib}/tracspamfilter/locale/ko/
%dir %{python2_sitelib}/tracspamfilter/locale/ko/LC_MESSAGES/
%lang(ko) %{python2_sitelib}/tracspamfilter/locale/ko/LC_MESSAGES/tracspamfilter.mo

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-0.2.20190829svn17127
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Paul Howarth <paul@city-fan.org> - 1.4.0-0.1.20190829svn17127
- Update to current svn snapshot

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-0.3.20180627svn16684
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-0.2.20180627svn16684
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Paul Howarth <paul@city-fan.org> - 1.2.7-0.1.20180627svn16684
- Update to current svn snapshot
- Drop legacy Group: tag
- Unversioned %%{python_sitelib} macro replaced by %%{python2_sitelib}

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.28.20170215svn15536
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.27.20170215svn15536
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.26.20170215svn15536
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Paul Howarth <paul@city-fan.org> - 1.2.0-0.25.20170215svn15536
- Update to current svn snapshot
- Modernize spec somewhat
- Add %%check section

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-0.24.20150929svn14342
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-0.23.20150929svn14342
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct  8 2015 Paul Howarth <paul@city-fan.org> - 1.0.6-0.22.20150929svn14342
- Update to current svn snapshot
- Add dependenies on python-httplib2 and python-oauth2 for Mollom support

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-0.21.20150328svn13942
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Paul Howarth <paul@city-fan.org> - 1.0.6-0.20.20150328svn13942
- Update to current svn snapshot
- Drop dependency on orphaned (apparently dead upstream) spambayes

* Mon Feb 16 2015 Paul Howarth <paul@city-fan.org> - 1.0.6-0.19.20150216svn13735
- Update to current svn snapshot
- BuildRequire everything that we Require to avoid unpleasant dependency
  surprises with the built package
- Go to great trouble to set %%lang on translations

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-0.18.20130913svn11796
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 13 2013 Paul Howarth <paul@city-fan.org> - 0.8.0-0.17.20130913svn11796
- Update to current svn snapshot
- Drop PIL import patch, issue fixed upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-0.16.20130228svn11702
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar  8 2013 Paul Howarth <paul@city-fan.org> - 0.7.3-0.15.20130228svn11702
- Update to trac 1.0 branch
- Fix PIL imports to work with pillow (#896262)
- Require python-pillow rather than python-imaging

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-0.14.20110716svn10756
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-0.13.20110716svn10756
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Paul Howarth <paul@city-fan.org> - 0.4.7-0.12.20110716svn10756
- Fedora 17 mass rebuild

* Sun Jul 17 2011 Paul Howarth <paul@city-fan.org> - 0.4.7-0.11.20110716svn10756
- Update to current svn snapshot
  - Various Blogspam timeout fixes
  - Add links to kill spammy users (Upstream #10093)
  - Add proper check for Defensio and python < 2.6 (Upstream #10195)
  - Add cleanup code to remove obsolete captcha db entries
  - Fix issues with different SQL engines (Upstream #10227)
  - Fix wrong argument count in log message (Upstream #10264)
  - Fix possibly uninitialized value (Upstream #10261)
- No need for %%defattr

* Mon Mar 21 2011 Paul Howarth <paul@city-fan.org> - 0.4.7-0.10.20110305svn10633
- Update to current svn snapshot
  - Add BlogSpam service
  - Add Defensio service
- Update pull-from-svn script to set time of tarball to that of last commit
- Drop BuildRoot tag and explicit buildroot cleaning
- No need to define %%{python_sitelib}

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-0.9.20101210svn10366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Paul Howarth <paul@city-fan.org> - 0.4.3-0.8.20101210svn10366
- Update to current svn snapshot
- Plugin requires trac >= 0.12, so drop EL4 support
- Add dependency on python-dns for DNS blacklist support
- Add dependency on python-imaging for captcha support
- Add pull-from-svn script for creation of tarball

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.1-0.7.20090714svn8330
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.6.20090714svn8330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Paul Howarth <paul@city-fan.org> - 0.2.1-0.5.20090714svn8330
- Update to rev8330, addresses upstream tickets #6130, #7627, #8032, #8121, #8257

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.4.20080603svn6990
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.1-0.3.20080603svn6990
- Rebuild for Python 2.6

* Fri Jul 04 2008 Jesse Keating <jkeating@redhat.com> - 0.2.1-0.2.20080603svn6990
- R spambayes

* Tue Jun 03 2008 Jesse Keating <jkeating@redhat.com> - 0.2.1-0.1.20080603svn6990
- Initial packaging

