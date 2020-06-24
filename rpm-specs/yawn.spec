%global htmldir /var/www/yawn
%global apacheconfdir /etc/httpd
%global svnrev 632
%global revdate 20140318

Name:           yawn
Version:        0
Release:        0.35.%{revdate}svn%{svnrev}%{?dist}
Summary:        Yet Another WBEM Navigator


License:        GPLv2
URL:            https://sourceforge.net/apps/mediawiki/pywbem/index.php?title=YAWN
# The source for this package was pulled from upstream svn repository.
# Use the following commands to get the archive:
#  svn export -r 632 https://svn.code.sf.net/p/pywbem/code/yawn/trunk/mod_wsgi yawn-20140318
#  tar -cJvf yawn-20140318.tar.xz yawn-20140318
Source0:        %{name}-%{revdate}.tar.xz

Patch0: fix-shebang-lines.patch
Patch1: python-3-support.patch
Patch2: fix-requires.patch

BuildRequires:  httpd, python3-devel
Requires:       python3-mod_wsgi, python3-pywbem, httpd, python3-werkzeug, python3-mako
BuildArch:      noarch

%description
Web-based CIM/WBEM browser

%package server
Summary: Standalone web server for yawn
Requires: %{name}

%description server
Script to run yawn without Apache web server.

%prep
%setup -q -n %{name}-%{revdate}
%patch0 -p1 -b .fix-shebang-lines
%patch1 -p1 -b .python-3-support
%patch2 -p1 -b .fix-requires

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root ${RPM_BUILD_ROOT}
mkdir -p $RPM_BUILD_ROOT%{htmldir}
install ./scripts/yawn.wsgi $RPM_BUILD_ROOT%{htmldir}/index.wsgi
install -d $RPM_BUILD_ROOT%{apacheconfdir}/conf.d/
install -m 0644 ./apache/yawn.conf ${RPM_BUILD_ROOT}/%{apacheconfdir}/conf.d/yawn.conf

%post
/bin/systemctl try-restart httpd.service >/dev/null 2>&1 || :

%files
%{htmldir}
%{python3_sitelib}/*
%config(noreplace) %{apacheconfdir}/conf.d/yawn.conf
%doc README Changelog

%files server
%{_bindir}/yawn.py

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.35.20140318svn632
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.34.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.33.20140318svn632
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0-0.32.20140318svn632
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.30.20140318svn632
- Various python2 -> python3 fixes
- Fix dependencies
  Resolves: #1701930

* Tue Feb 19 2019 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.29.20140318svn632
- Fix FTBFS
  Resolves: #1676255

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.27.20140318svn632
- Fix FTBFS
  Resolves: #1606766

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0-0.24.20140318svn632
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.21.20140318svn632
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.19.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.18.20140318svn632
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Michal Minar <miminar@redhat.com> 0-0.17.20140318svn632
- New upstream version with option to disable certificate verification.

* Thu Feb 27 2014 Michal Minar <miminar@redhat.com> 0-0.16.20140227svn630
- New upstream version fixing enumeration of instrumetned classes.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.20130426svn620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Michal Minar <miminar@redhat.com> 0-0.15.20130426svn620
- Updated to latest upstream version

* Wed Feb 13 2013 Michal Minar <miminar@redhat.com> 0-0.14.20130213svn617
- Updated to latest upstream version

* Fri Jan 18 2013 Michal Minar <miminar@redhat.com> 0-0.13.20130118svn610
- Updated to latest upstream version
- Added changelog file

* Thu Nov 15 2012 Michal Minar <miminar@redhat.com> - 0-0.12.20121115svn605
- Update to latest upstream version

* Tue Nov 06 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.11.20121106svn600
- Update to latest upstream version
- Fix tarball name

* Mon Sep 17 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.10.20120917svn593
- Update to latest upstream version

* Mon Sep 10 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.9.20120905svn588
- Fix issues found by fedora-review utility in the spec file

* Wed Sep 05 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.8.20120905svn588
- Update to latest upstream version

* Thu Aug 02 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.7.20120620svn578
- Add python-mako to Requires

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20120620svn578
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.5.20120620svn578
- Update to latest upstream version (switched from mod_python to mod_wsgi)

* Thu May 17 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.4.20120227svn561
- Fix URLs (patch by Radek Novacek, rnovacek@redhat.com)

* Tue Mar 13 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.3.20120227svn561
- Fix Pickle method sets Content-type: text/plain instead of text/html
  (patch by Jan Safranek, jsafrane@redhat.com)
  Resolves: #802683

* Tue Feb 28 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.2.20120227svn561
- Fix twice listed files

* Mon Feb 27 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 0-0.1.20120227svn561
- Remove obsolete BuildRoot tag, use systemctl instead of service, own htmldir,
  fix source and version

* Thu Feb 23 2012 Vitezslav Crhonek <vcrhonek@redhat.com>
- Change htmldir, fix license

* Wed Jan 25 2012 Vitezslav Crhonek <vcrhonek@redhat.com>
- Initial build for Fedora
