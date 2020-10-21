Name:           resultsdb
# NOTE: if you update version, *make sure* to also update `resultsdb/__init__.py`
Version:        2.2.0
Release:        7%{?dist}
Summary:        Results store for automated tasks

License:        GPLv2+
URL:            https://pagure.io/taskotron/resultsdb
Source0:        https://qa.fedoraproject.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3-fedora-messaging >= 1.5.0
Requires:       python3-alembic
Requires:       python3-flask
Requires:       python3-flask-restful
Requires:       python3-flask-sqlalchemy
Requires:       python3-iso8601
Requires:       python3-six
Requires:       python3-sqlalchemy

BuildRequires:  python3-fedora-messaging >= 1.5.0
BuildRequires:  python3-alembic
BuildRequires:  python3-flask
BuildRequires:  python3-flask-restful
BuildRequires:  python3-flask-sqlalchemy
BuildRequires:  python3-iso8601
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
ResultsDB is a results store engine for, but not limited to, Fedora QA tools.

%prep
%setup -q

%check
NO_CAN_HAS_POSTGRES='sadly' PYTHONPATH=%{buildroot}%{python3_sitelib}/ pytest-3

# This seems to be the only place where we can remove pyco files, see:
# https://fedoraproject.org/wiki/Packaging:Python#Byte_compiling
rm -f %{buildroot}%{_sysconfdir}/resultsdb/*.py{c,o}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

# apache and wsgi settings
install -d %{buildroot}%{_datadir}/resultsdb/conf
install -p -m 0644 conf/resultsdb.conf %{buildroot}%{_datadir}/resultsdb/conf/
install -p -m 0644 conf/resultsdb.wsgi %{buildroot}%{_datadir}/resultsdb/

# resultsdb config
install -d %{buildroot}%{_sysconfdir}/resultsdb
install -p -m 0644 conf/settings.py.example %{buildroot}%{_sysconfdir}/resultsdb/settings.py

%files
%doc README.md conf/*
%license LICENSE

%{python3_sitelib}/resultsdb
%{python3_sitelib}/*.egg-info

%attr(755,root,root) %{_bindir}/resultsdb
%dir %{_sysconfdir}/resultsdb
%config(noreplace) %{_sysconfdir}/resultsdb/settings.py

%dir %{_datadir}/resultsdb
%{_datadir}/resultsdb/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.2.0-1
- Latest endpoint: group by additional fields
- specfile: Drop python 2 support
- Drop support for fedmsg and replace by fedora-messaging
- settings.py: use lists instead of tuples

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.2-1
- Support Python 3, use it on Fedora
- Fix ImmutableMultiDict handling for python 3.7
- Use tuples instead of list in RESULT_OUTCOME
- Define resource limits for the database container
- Makefile: Use generic Makefile provided by qa-make
- Add config for task-dockerbuild

* Sun Jul 01 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.1-2
- Fix building on EPEL 7

* Wed Jun 20 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.1-1
- Fix deprecated flask imports
- Make the list of allowed outcomes configurable

* Thu Mar 29 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.0-1
- Add OpenID Connect auth module for POST requests
- Allow GET requests to just pass without auth
- Publish more metadata in bus messages
- Update Python 2 dependency declarations
- generic message format which matches the HTTP API v2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.5-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Martin Krizek <mkrizek@redhat.com> - 2.0.5-1
- Sorting by key plugin for browse results collection (D1213)
- A stomp messaging plugin (D1191)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 10 2017 Kamil Páral <kparal@redhat.com> - 2.0.4-2
- add python-pytest-cov builddep since it's needed for running the test suite
  with our new tox.ini

* Thu Feb 02 2017 Kamil Páral <kparal@redhat.com> - 2.0.4-1
- setup.py: add missing modules

* Thu Feb 02 2017 Kamil Páral <kparal@redhat.com> - 2.0.3-1
- Fix pagination issue
- Add config options to resultsdb for requiring fields

* Fri Jan 20 2017 Matt Prahl <mprahl@redhat.com> - 2.0.2-2
- Add the ability to build on RHEL without EPEL by setting the "without_epel" variable to 1

* Wed Dec 14 2016 Martin Krizek <mkrizek@fedoraproject.org> - 2.0.2-1
- Make the migration less memory consuming (D1059)
- Flexible messaging (D1061)

* Tue Nov 22 2016 Martin Krizek <mkrizek@fedoraproject.org> - 2.0.1-1
- do not replace config file
- loosen pin on sqlalchemy in requirements.txt
- fix the migration, so it deals with duplicate job uuids

* Thu Nov 3 2016 Tim Flink <tflink@fedoraproject.org> - 2.0.0-1
- releasing v2.0 with new API

* Thu Jul 21 2016 Martin Krizek <mkrizek@fedoraproject.org> - 1.1.16-3
- preserve timestamps of original installed files
- fix installing the config file
- remove .py compiled files from config and datadir

* Wed Jun 1 2016 Martin Krizek <mkrizek@fedoraproject.org> - 1.1.16-2
- add license

* Mon Apr 18 2016 Martin Krizek <mkrizek@fedoraproject.org> - 1.1.16-1
- support for testcase namespaces

* Mon Jan 25 2016 Tim Flink <tflink@fedoraproject.org> - 1.1.15-1
- Add previous_outcome field to fedmsgs (D728)

* Mon Jan 18 2016 Tim Flink <tflink@fedoraproject.org> - 1.1.14-1
- Removed unnecessary count, added index on submit_time (D635)
- Don't ignore arch for fedmsg deduplication (D698)

* Wed Nov 4 2015 Josef Skladanka <jskladan@redhat.com> - 1.1.13-2
- synchronize package versions between spec file and requirements.txt

* Wed Oct 7 2015 Martin Krizek <mkrizek@redhat.com> - 1.1.13-1
- Emit fedmsg with whatever result is being stored

* Tue Aug 18 2015 Tim Flink <tflink@fedoraproject.org> - 1.1.12-1
- Use HTTP_X_FORWARDED_SCHEME (D264)
- Improve pagination metadata for JSON queries (D264)
- Add fedmenu to resultsdb (D364)
- Several dev and backend fixes

* Wed May 6 2015 Tim Flink <tflink@fedoraproject.org> - 1.1.11-1
- Added ABORTED outcome (T458)

* Mon Apr 20 2015 Tim Flink <tflink@fedoraproject.org> - 1.1.10-1
- Added indexes for foreign keys (T452)

* Thu Apr 9 2015 Tim Flink <tflink@fedoraproject.org> - 1.1.9-1
- fixed TB with file logging (T454)
- changed complete data returning on update_job to be optional (T466)

* Wed Apr 1 2015 Tim Flink <tflink@fedoraproject.org> - 1.1.8-2
- added alembic config and data to package
- added requires python-alembic

* Wed Apr 1 2015 Tim Flink <tflink@fedoraproject.org> - 1.1.8-1
- initial alembic support
- UUID support for integration with execdb

* Thu Oct 9 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.7-1
- fix jsonp interface and various associated bugs

* Fri Jul 4 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.4-1
- fix compatibility with flask-wtf 0.9

* Mon Jun 23 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.3-1
- add SHOW_DB_URI configuration value to stop DB URI leaking

* Wed Jun 18 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.2-2
- fixing botched build and bad changelog dates

* Wed Jun 18 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.2-1
- Fixing typo in date parsing code
- Working around limitations in how time data is stored without timezones

* Fri Jun 13 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.1-1
- adding jsonp suport

* Fri May 16 2014 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Releasing resultsdb 1.1.0

* Fri Apr 25 2014 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- bugfixes for api and using postgres as a backend

* Mon Apr 14 2014 Tim Flink <tflink@fedoraproject.org> - 1.0.1-1
- updating package for new upstream location, not using bitbucket downloads
- removing dep on mysql

* Thu Feb 6 2014 Jan Sedlak <jsedlak@redhat.com> - 1.0.0-1
- initial packaging
