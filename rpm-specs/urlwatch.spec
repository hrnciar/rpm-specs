Name:           urlwatch
Version:        2.17
Release:        7%{?dist}
Summary:        A tool for monitoring webpages for updates

License:        BSD
URL:            http://thpinfo.com/2008/urlwatch/
Source0:        https://github.com/thp/urlwatch/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-idle

Requires:       python3-requests
Requires:       python3-keyring
Requires:       python3-minidb
Requires:       python3-PyYAML

%description
This script is intended to help you watch URLs and get notified (via
email or in your terminal) of any changes. The change notification
will include the URL that has changed and a unified diff of what has
changed.

The script supports the use of a filtering hook function to strip
trivially-varying elements of a webpage.

Basic features

* Simple configuration (text file, one URL per line)
* Easily hackable (clean Python implementation)
* Can run as a cronjob and mail changes to you
* Always outputs only plaintext - no HTML mails :)
* Supports removing noise (always-changing website parts)
* Example hooks to filter content in Python

%prep
%autosetup

%build
%py3_build

%install
%py3_install
# Fix exec permission for rpmlint
chmod 0755 %{buildroot}%{python3_sitelib}/%{name}/*txt.py
chmod a+x %{buildroot}%{python3_sitelib}/%{name}/handler.py

%files
%doc CHANGELOG.md README.md
%license COPYING
%{_mandir}/man*/*.*
%{_bindir}/%{name}
%{_datadir}/%{name}/examples/
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.17-6
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.17-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.17-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.17-1
- Update to latest upstream release 2.17 (rhbz#1692110)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.6-4
- Fix rhbz#1445286

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.6-2
- Add new requirements

* Thu Dec 29 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.6-1
- Update to latest upstream release 2.6

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.18-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.18-1
- Update to latest upstream release 1.18

* Tue Jun 24 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.16-2
- Drop XMPP support

* Mon Jun 23 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.16-1
- Update to latest upstream release 1.16

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.15-4
- Import error fix with python2

* Wed Feb 20 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.15-3
- Updated convert script and fix BR

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 02 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.15-1
- Updated to new upstream version 1.15

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 11 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.14-3
- Update for py3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.14-1
- Update to new upstream version 1.14

* Fri Aug 26 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.13-1
- Update to new upstream version 1.13

* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.12-2
- Rebuild (python-xmpp)

* Sun Mar 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 1.12-1
- Update to new upstream version 1.12

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.11-2
- Remove compression of man page

* Sat Aug 07 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.11-1
- Update to new upstream version 1.11

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 10 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-1
- Fix #590638
- Update to new upstream version 1.10

* Sat Oct 10 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.9-1
- Add patch for xmpp functionality
- Update to new upstream version 1.9

* Thu Sep 17 2009 Fabian Affolter <mail@fabian-affolter.ch> - 1.8-1
- Minior spec file changes
- Update to new upstream version 1.8

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 18 2008 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-2
- Change license from MIT to BSD

* Fri Jan 18 2008 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-1
- Initial package for Fedora
