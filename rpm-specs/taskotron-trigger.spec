Name:           taskotron-trigger
# NOTE: if you update version, *make sure* to also update `setup.py`
Version:        0.7.0
Release:        7%{?dist}
Summary:        Triggering Taskotron jobs via fedmsg

License:        GPLv2+
URL:            https://pagure.io/taskotron/taskotron-trigger
Source0:        https://qa.fedoraproject.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3-fedmsg
Requires:       git
Requires:       python3-koji
Requires:       python3-future
Requires:       python3-pyyaml
Requires:       python3-mongoquery
Requires:       python3-requests
Requires:       python3-twisted

BuildRequires:  python3-fedmsg
BuildRequires:  python3-future
BuildRequires:  python3-munch
BuildRequires:  python3-pyyaml
BuildRequires:  python3-koji
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-mongoquery
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools

%description
Triggering Taskotron jobs via fedmsg.

%prep
%setup -q

%check
%{__python3} setup.py test
rm -f %{buildroot}%{_sysconfdir}/fedmsg.d/*.py{c,o}

%build
%py3_build

%install
%py3_install

install -d %{buildroot}%{_sysconfdir}/taskotron/
install -p -m 644 conf/trigger.cfg.example %{buildroot}%{_sysconfdir}/taskotron/trigger.cfg
install -p -m 644 conf/trigger_rules.yml.example %{buildroot}%{_sysconfdir}/taskotron/trigger_rules.yml

install -d %{buildroot}%{_sysconfdir}/fedmsg.d/
install -p -m 0644 fedmsg.d/taskotron-trigger.py %{buildroot}%{_sysconfdir}/fedmsg.d/taskotron-trigger.py

install -d %{buildroot}%{_sysconfdir}/logrotate.d/
install -p -m 0644 conf/logrotate.d/taskotron-trigger %{buildroot}%{_sysconfdir}/logrotate.d/taskotron-trigger

install -d %{buildroot}%{_localstatedir}/log/taskotron-trigger/
install -d %{buildroot}%{_sharedstatedir}/taskotron-trigger/

%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/jobtriggers/
%{python3_sitelib}/jobtriggers-*.egg-info

%{_bindir}/jobrunner

%dir %attr(755,fedmsg,fedmsg) %{_localstatedir}/log/taskotron-trigger
%dir %attr(755,fedmsg,fedmsg) %{_sharedstatedir}/taskotron-trigger

%dir %{_sysconfdir}/taskotron
%{_sysconfdir}/fedmsg.d/taskotron-trigger.py*
%config(noreplace) %{_sysconfdir}/taskotron/trigger.cfg
%config(noreplace) %{_sysconfdir}/taskotron/trigger_rules.yml
%config(noreplace) %{_sysconfdir}/logrotate.d/taskotron-trigger

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.7.0-1
- Use Python 3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.6.1-1
- critpath: make config value optional

* Wed Jul 04 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.6.0-2
- SPEC: Explicitly use python2

* Wed Jul 04 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.6.0-1
- make critpath file optional
- Fix jobrunner for pagure git commits

* Thu May 03 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.5.1-1
- Make fixed-architecture job scheduling possible
- Ondemand task scheduling

* Mon Mar 05 2018 Kamil Páral <kparal@redhat.com> - 0.5.0-1
- support Standard Test Interface tasks instead of custom libtaskotron formulae

* Fri Feb 02 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.4.9-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Nov 23 2017 Kamil Páral <kparal@redhat.com> - 0.4.9-1
- Added consumer for Github's Pull Requests

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 4 2017 Martin Krizek <mkrizek@redhat.com> - 0.4.8-1
- Add MBS (Module Build Service) consumer (D1180)
- Change name of 'branch' parameter so it isn't squashed in buildbot (D1183)

* Wed Mar 15 2017 Tim Flink <tflink@fedoraproject.org> 0.4.7-1
- Fix hardcoded paths in cloud_compose_completed (D1170)

* Fri Mar 10 2017 Martin Krizek <mkrizek@redhat.com> - 0.4.6-1
- Add support for cloud and atomic composes (D1157)
- support multiple builders for tasks stored in distgit (D1159)

* Thu Mar 2 2017 Tim Flink <tflink@fedoraproject.org> - 0.4.5-1
- add configuration option to listen for stg fedmsgs

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 10 2017 Kamil Páral <kparal@redhat.com> - 0.4.4-2
- add python-pytest-cov dependency
- use the same test approach we use in development (just run py.test and
  inherit everything from tox.ini)

* Mon Jan 23 2017 Martin Krizek <mkrizek@redhat.com> - 0.4.4-1
- Fix CLI to work with the trigger rules (D1081)

* Mon Oct 31 2016 Tim Flink <tflink@fedoraproject.org> - 0.4.3-1
- Improve task discovery for dist-git (D1031)
- Add support for triggering on dist-git commit events (D1064)
- Use proper dist-git namespaces (D1062)
- Require mongoquery (D1068)

* Mon Oct 31 2016 Tim FLink <tflink@fedoraproject.org> - 0.4.2-1
- Adding more restrictions on the koji tags that can trigger tasks (D1042)

* Mon Oct 17 2016 Martin Krizek <mkrizek@redhat.com> - 0.4.1-2
- install trigger_rules.yml

* Thu Oct 13 2016 Martin Krizek <mkrizek@redhat.com> - 0.4.1-1
- remove mongoquery bundle

* Tue Oct 11 2016 Tim FLink <tflink@fedoraproject.org> - 0.4.0-1
- bumping version properly for a major release

* Tue Oct 11 2016 Tim FLink <tflink@fedoraproject.org> - 0.3.17-1
- rework trigger to be more easily configurable (D963)

* Fri Jul 22 2016 Martin Krizek <mkrizek@redhat.com> - 0.3.16-4
- remove rm -rf buildroot as it's not neccessary
- preserve timestamps of installed files

* Mon Jun 13 2016 Martin Krizek <mkrizek@redhat.com> - 0.3.16-3
- fix Source0 url
- fix conf files permissions

* Mon May 30 2016 Martin Krizek <mkrizek@redhat.com> - 0.3.16-2
- add license file
- add check
- fix url and source
- fix requires and buildrequires

* Wed May 25 2016 Martin Krizek <mkrizek@redhat.com> - 0.3.16-1
- Allow enabling distgit style tasks in config
- libabigail has been renamed to abicheck

* Fri May 6 2016 Martin Krizek <mkrizek@redhat.com> - 0.3.15-1
- Removing daemon as a dependency from requirements.txt (T768)
- dist-git support
- libabigail triggering

* Wed Mar 30 2016 Martin Krizek <mkrizek@redhat.com> - 0.3.14-1
- Add triggering for dockerautotest check

* Tue Jan 5 2016 Martin Krizek <mkrizek@redhat.com> - 0.3.13-2
- fix logrotate config file permissions

* Wed Dec 9 2015 Martin Krizek <mkrizek@redhat.com> - 0.3.13-1
- Use datagrepper to fetch jobs (D667)

* Mon May 25 2015 Martin Krizek <mkrizek@redhat.com> - 0.3.12-1
- fix blacklisting releases

* Wed Apr 8 2015 Martin Krizek <mkrizek@redhat.com> - 0.3.11-1
- fix triggering jobs when no task is configured

* Tue Mar 31 2015 Martin Krizek <mkrizek@redhat.com> - 0.3.10-1
- Add support for execdb

* Tue Sep 30 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.9-1
- remove koji build queries to fix scheduling issues in T341

* Tue Sep 23 2014 Martin Krizek <mkrizek@redhat.com> - 0.3.8-1
- listen on primary koji instance only
- fix blacklisting releases of the form: '1.el7.1'

* Tue Sep 2 2014 Martin Krizek <mkrizek@redhat.com> - 0.3.7-1
- fix blacklisting releases in koji_tag consumer

* Thu Aug 21 2014 Martin Krizek <mkrizek@redhat.com> - 0.3.6-1
- list trigger.cfg as config file
- fix upgradepath scheduling

* Thu Aug 14 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.5-1
- change to not schedule upgradepath on *-testing-pending

* Mon Jun 30 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.3-1
- switching trigger over to use change_source instead of hacking at force build
- supporting x86_64-only checks

* Tue Jun 24 2014 Martin Krizek <mkrizek@redhat.com> - 0.3.2-1
- change koji tag triggering to use *-pending tags

* Mon Jun 23 2014 Martin Krizek <mkrizek@redhat.com> - 0.3.1-1
- add python-twisted as dep

* Mon Jun 16 2014 Tim Flink <tflink@fedoraproject.org> - 0.3.0-1
- releasing 0.3.0

* Fri Jun 13 2014 Tim Flink <tflink@fedoraproject.org> - 0.2.1-1
- support triggering with koji_tag on bodhi update change

* Thu May 29 2014 Tim Flink <tflink@fedoraproject.org> - 0.1.2-1
- Fixing typo that broke the jobrunner executable

* Fri May 23 2014 Martin Krizek <mkrizek@redhat.com> - 0.1.1-1
- Add jobrunner script
- Add logrotate conf file

* Fri May 16 2014 Tim Flink <tflink@fedoraproject.org> - 0.1.0-1
- Adding missing deps
- Releasing taskotron-trigger 0.1.0

* Tue Apr 15 2014 Tim Flink <tflink@fedoraproject.org> - 0.0.10-1
- Updating to latest upstream. Triggers buildbot builds based on item arch
- adding koji to requires

* Mon Mar 10 2014 Martin Krizek <mkrizek@fedoraproject.org> - 0.0.9-1
- Initial packaging
