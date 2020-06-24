Name:           execdb
# NOTE: if you update version, *make sure* to also update `execdb/__init__.py`
Version:        0.1.0
Release:        6%{?dist}
Summary:        Execution status database for Taskotron

License:        GPLv2+
URL:            https://pagure.io/taskotron/execdb
Source0:        https://qa.fedoraproject.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3-alembic
Requires:       python3-flask
Requires:       python3-flask-sqlalchemy
Requires:       python3-flask-wtf
Requires:       python3-flask-login
Requires:       python3-flask-restful
Requires:       python3-psycopg2
Requires:       python3-wtforms
Requires:       python3-six

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
ExecDB is a database that stores the execution status of jobs running
inside the Taskotron framework. You can see which jobs were scheduled,
started and finished, and some of their properties.

%prep
%setup -q

%check
# This seems to be the only place where we can remove pyco files, see:
# https://fedoraproject.org/wiki/Packaging:Python#Byte_compiling
rm -f %{buildroot}%{_sysconfdir}/execdb/*.py{c,o}

%build
%py3_build

%install
%py3_install

# apache and wsgi settings
install -d %{buildroot}%{_datadir}/execdb/conf
install -p -m 0644 conf/execdb.conf %{buildroot}%{_datadir}/execdb/conf/
install -p -m 0644 conf/execdb.wsgi %{buildroot}%{_datadir}/execdb/

# alembic config and data
cp -r --preserve=timestamps alembic %{buildroot}%{_datadir}/execdb/
install -p -m 0644 alembic.ini %{buildroot}%{_datadir}/execdb/

# exedb config
install -d %{buildroot}%{_sysconfdir}/execdb
install -p -m 0644 conf/settings.py.example %{buildroot}%{_sysconfdir}/execdb/settings.py

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/execdb
%{python3_sitelib}/*.egg-info

%{_bindir}/execdb

%dir %{_sysconfdir}/execdb
%config(noreplace) %{_sysconfdir}/execdb/settings.py

%dir %{_datadir}/execdb
%{_datadir}/execdb/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.0-1
- Updating buildbot status info handling code to handle new buildbot
- Switch to Python 3
- Drop Fedora 27

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 27 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.0.10-1
- API
- Fix show_job template to use right path for api

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Kamil Páral <kparal@redhat.com> - 0.0.9-5
- synchronize fedora spec with project spec

* Wed Jan 10 2018 Kamil Páral <kparal@redhat.com> - 0.0.9-4
- fix condition for python deps

* Fri Jan 05 2018 Kamil Páral <kparal@redhat.com> - 0.0.9-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3 and
  https://src.fedoraproject.org/rpms/execdb/pull-request/1)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 28 2017 Tim Flink <tflink@fedoraproject.org> - 0.0.9-1
- Fix links in job overview

* Wed Mar 15 2017 Tim Flink <tflink@fedoraproject.org> - 0.0.8-1
- Change job.taskname from String(20) to Text (D1160)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Martin Krizek <mkrizek@redhat.com> - 0.0.7-5
- do not replace config file
- using python2-flask-sqlalchemy breaks depcheck on f23

* Wed Sep 21 2016 Martin Krizek <mkrizek@redhat.com> - 0.0.7-4
- use python2-* where possible
- fix rpmlint's description-line-too-long
- remove conf examples from doc

* Thu Aug 11 2016 Martin Krizek <mkrizek@redhat.com> - 0.0.7-3
- use python macros
- make description more verbose
- fix permissions

* Mon Jun 13 2016 Martin Krizek <mkrizek@redhat.com> - 0.0.7-2
- add license
- remove not needed custom macros

* Wed Jun 17 2015 Josef Skladanka <jskladan@fedoraproject.org> - 0.0.7-1
- added alembic config and data to package
- added requires python-alembic

* Mon Mar 30 2015 Tim Flink <tflink@fedoraproject.org> - 0.0.6-1
- bumped version for initial release

* Thu Feb 12 2015 Josef Skladanka <jskladan@redhat.com> - 0.0.1-1
- initial packaging
