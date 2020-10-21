%global srcname relval

Name:           relval
Version:        2.5.2
Release:        1%{?dist}
Summary:        Tool for interacting with Fedora QA wiki pages

License:        GPLv3+
URL:            https://pagure.io/fedora-qa/relval
Source0:        https://www.happyassassin.net/relval/releases/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-fedfind >= 2.8.0
Requires:       python3-markupsafe
Requires:       python3-mwclient
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-wikitcms >= 2.6.0
Requires:       python3-bugzilla

%description
Relval can perform various tasks related to Fedora QA by interacting with the
Fedora wiki. It lets you:

* Create wiki pages for Fedora release validation test events
* Generate statistics on release validation testing
* Report release validation test results using a console interface

See https://fedoraproject.org/wiki/QA/SOP_Release_Validation_Test_Event for
more information on the process relval helps with.

%prep
%autosetup -n %{srcname}-%{version}

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%doc README.md
%license COPYING
%{python3_sitelib}/%{srcname}*
%{_bindir}/relval

%changelog
* Tue Aug 25 2020 Adam Williamson <awilliam@redhat.com> - 2.5.2-1
- New release 2.5.2: bump Workstation live size limit to 2.1GB

* Mon Aug 17 2020 Adam Williamson <awilliam@redhat.com> - 2.5.1-1
- New release 2.5.1: size-check warn if blocker trackers not found

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Rebuilt for Python 3.9

* Fri May 15 2020 Adam Williamson <awilliam@redhat.com> - 2.5.0-1
- New release 2.5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Adam Williamson <awilliam@redhat.com> - 2.4.11-1
- New release 2.4.11: add max size for Comp_Neuro

* Mon Dec 30 2019 Adam Williamson <awilliam@redhat.com> - 2.4.10-1
- New release 2.4.10: update Games max size to 16GB

* Tue Nov 19 2019 Adam Williamson <awilliam@redhat.com> - 2.4.9-1
- New release 2.4.9: handle BZ not letting us change bug status

* Tue Oct 01 2019 Adam Williamson <awilliam@redhat.com> - 2.4.8-1
- New release 2.4.8: update MATE max size to 3GiB

* Mon Sep 30 2019 Adam Williamson <awilliam@redhat.com> - 2.4.7-1
- New release 2.4.7: add missing space to size-check bug description

* Mon Sep 30 2019 Adam Williamson <awilliam@redhat.com> - 2.4.6-1
- New release 2.4.6: limit bug alias length, update Cinnamon max size

* Thu Sep 19 2019 Adam Williamson <awilliam@redhat.com> - 2.4.5-1
- New release 2.4.5: correct python-bugzilla requirement

* Thu Sep 19 2019 Adam Williamson <awilliam@redhat.com> - 2.4.4-1
- New release 2.4.4: size-check can now file bugs for oversize images

* Thu Sep 12 2019 Adam Williamson <awilliam@redhat.com> - 2.4.3-1
- New release 2.4.3: avoid deprecation warnings with mwclient 0.10.0+

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Adam Williamson <awilliam@redhat.com> - 2.4.2-1
- New release 2.4.2: per-environment last_tested in testcase_stats json

* Thu Nov 22 2018 Adam Williamson <awilliam@redhat.com> - 2.4.1-1
- New release 2.4.1: fix broken `compose --cid` from 2.4.0 (#5)

* Fri Oct 05 2018 Adam Williamson <awilliam@redhat.com> - 2.4.0-1
- New release 2.4.0:
  + compose: clarify --cid vs. release/milestone/compose
  + Revise code and docs for new-style wiki auth
  + Stop allowing 'Alpha' milestone for most purposes

* Fri Oct 05 2018 Adam Williamson <awilliam@redhat.com> - 2.3.0-1
- New release 2.3.0: output testcase_stats data as JSON also (jskladan)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Adam Williamson <awilliam@redhat.com> - 2.2.1-1
- New release 2.2.1: avoid unneeded Modular questions in report-results

* Fri Nov 10 2017 Adam Williamson <awilliam@redhat.com> - 2.2.0-1
- New release 2.2.0: support Modular events

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Adam Williamson <awilliam@redhat.com> - 2.1.8-1
- new release 2.1.8: adjust KDE target size to 2GB (per KDE sig)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.7-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Adam Williamson <awilliam@redhat.com> - 2.1.7-1
- new release 2.1.7:
- + Adjust to 'Final' milestone becoming 'RC' from Fedora 24 on
- + size-check: really catch when we don't find any images
- + size-check: include arch of over-size images in comment

* Sat Oct 08 2016 Adam Williamson <awilliam@redhat.com> - 2.1.5-1
- new release 2.1.5 (add `--since` and `--until` for `user-stats`)

* Wed Oct 05 2016 Adam Williamson <awilliam@redhat.com> - 2.1.4-1
- new release 2.1.4 (update size-check for ostree installer metadata mess)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 28 2016 Adam Williamson <awilliam@redhat.com> - 2.1.3-1
- new release 2.1.3 (fix compose --download-only, it was totally busted)

* Thu Mar 17 2016 Adam Williamson <awilliam@redhat.com> - 2.1.2-1
- new release 2.1.2 (adjust to fedfind changes)

* Thu Mar 17 2016 Adam Williamson <awilliam@redhat.com> - 2.1.1-1
- new release 2.1.1 (fix testcase-stats bitmap sorting)

* Wed Mar 16 2016 Adam Williamson <awilliam@redhat.com> - 2.1.0-1
- new release 2.1.0 (adjust to wikitcms Pungi 4 changes)

* Fri Mar 04 2016 Adam Williamson <awilliam@redhat.com> - 2.0.3-1
- new release 2.0.3 (add system-wide credentials file)

* Thu Mar 03 2016 Adam Williamson <awilliam@redhat.com> - 2.0.2-1
- new release 2.0.2 (major changes, now Python 3)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Adam Williamson <awilliam@redhat.com> - 1.11.7-1
- new release 1.11.7: add --wait argument for nightly subcommand

* Thu Nov 05 2015 Adam Williamson <awilliam@redhat.com> - 1.11.6-2
- use license macro
- use py2_build and py2_install macros

* Tue Oct 20 2015 Adam Williamson <awilliam@redhat.com> - 1.11.6-1
- new release 1.11.6: improve testcase_stats page sorting

* Mon May 04 2015 Adam Williamson <awilliam@redhat.com> - 1.11.5-1
- new release 1.11.5: small fixes and cleanups

* Tue Apr 21 2015 Adam Williamson <awilliam@redhat.com> - 1.11.4-1
- new release 1.11.4: various changes for 'bot' results

* Fri Apr 17 2015 Adam Williamson <awilliam@redhat.com> - 1.11.3-1
- new release 1.11.3: comments in size-check, env in shebangs

* Wed Mar 25 2015 Adam Williamson <awilliam@redhat.com> - 1.11.1-1
- new release 1.11.1: size-check: display compose being checked

* Wed Mar 25 2015 Adam Williamson <awilliam@redhat.com> - 1.11-1
- new release 1.11: new size-check subcommand, under-the-hood changes

* Mon Mar 16 2015 Adam Williamson <awilliam@redhat.com> - 1.10.2-1
- new release 1.10.2: report-auto test case searching now case-insensitive

* Wed Feb 18 2015 Adam Williamson <awilliam@redhat.com> - 1.10.1-1
- fix some leftover version bugs in report-results

* Wed Feb 18 2015 Adam Williamson <awilliam@redhat.com> - 1.10-1
- update for wikitcms versioning changes, fix some bugs

* Thu Feb 12 2015 Adam Williamson <awilliam@redhat.com> - 1.9.4-1
- new release 1.9.4: add Download page generation, bugfixes

* Mon Feb 02 2015 Adam Williamson <awilliam@redhat.com> - 1.9.3-1
- new release 1.9.3: add report-auto and comment support for report-results

* Wed Jan 07 2015 Adam Williamson <awilliam@redhat.com> - 1.8.8-1
- new release 1.8.8: one more mistake, honest, this one really works

* Wed Jan 07 2015 Adam Williamson <awilliam@redhat.com> - 1.8.7-1
- new release 1.8.7: complete fix from 1.8.6

* Wed Jan 07 2015 Adam Williamson <awilliam@redhat.com> - 1.8.6-1
- new release 1.8.6: bugfix (no wiki login with Python < 2.7.9)

* Fri Jan 02 2015 Adam Williamson <awilliam@redhat.com> - 1.8.5-1
- new release 1.8.5: SECURITY: input sanitization for stats subcommands

* Tue Dec 23 2014 Adam Williamson <awilliam@redhat.com> - 1.8.3-1
- new release 1.8.3: multiple fixes and enhancements

* Fri Dec 19 2014 Adam Williamson <awilliam@redhat.com> - 1.7-1
- new release 1.7: handle wikitcms changes, bugfixes

* Tue Dec 16 2014 Adam Williamson <awilliam@redhat.com> - 1.6-1
- new release 1.6: handle wikitcms changes, bugfixes

* Fri Dec 12 2014 Adam Williamson <awilliam@redhat.com> - 1.5.2-1
- new release: re-fix bugzilla URL links (lost between 1.4.1 and 1.5)

* Tue Dec 09 2014 Adam Williamson <awilliam@redhat.com> - 1.5-1
- new release: nightly compose support

* Fri Oct 31 2014 Adam Williamson <awilliam@redhat.com> - 1.4.1-1
- new release 1.4.1: fix URL of bugzilla links on detail pages (tcs)

* Sat Oct 25 2014 Adam Williamson <awilliam@redhat.com> - 1.4-1
- new release (some refinements to result reporting and testcase-stats)

* Thu Oct 23 2014 Adam Williamson <awilliam@redhat.com> - 1.3.2-1
- new release (misc. bugfixes in result reporting)

* Wed Oct 22 2014 Adam Williamson <awilliam@redhat.com> - 1.3.1-1
- new release 1.3.1 (fix crasher in result reporting)

* Tue Oct 21 2014 Adam Williamson <awilliam@redhat.com> - 1.3-1
- new release 1.3

* Fri Oct 17 2014 Adam Williamson <awilliam@redhat.com> - 1.2.1-1
- brown paper bag release 1.2.1

* Thu Oct 16 2014 Adam Williamson <awilliam@redhat.com> - 1.2-1
- new release 1.2

* Mon Oct 13 2014 Adam Williamson <awilliam@redhat.com> - 1.1-1
- first build of relval as separate package from wikitcms
