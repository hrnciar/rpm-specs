%global upstream_version 1.1.6

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without server
%else
# For EPEL7 we build only the CLI, not the server bits,
# because Flask and other dependencies are too old.
%bcond_with server
%endif

Name:           waiverdb
Version:        1.1.6
Release:        2%{?dist}
Summary:        Service for waiving results in ResultsDB
License:        GPLv2+
URL:            https://pagure.io/waiverdb
Source0:        https://files.pythonhosted.org/packages/source/w/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%else # EPEL7 uses Python 2 and python- package naming convention
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%endif

%if %{with server}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-httpdomain
BuildRequires:  python3-flask
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-flask-cors
BuildRequires:  python3-flask-restful
BuildRequires:  python3-flask-sqlalchemy
BuildRequires:  python3-psycopg2
BuildRequires:  python3-gssapi
BuildRequires:  python3-requests-gssapi
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-flask-oidc
BuildRequires:  python3-click
BuildRequires:  python3-flask-migrate
BuildRequires:  python3-stomppy
BuildRequires:  python3-fedora-messaging
BuildRequires:  python3-prometheus_client
BuildRequires:  python3-six
Requires:       python3-flask
Requires:       python3-sqlalchemy
Requires:       python3-flask-cors
Requires:       python3-flask-restful
Requires:       python3-flask-sqlalchemy
Requires:       python3-psycopg2
Requires:       python3-gssapi
Requires:       python3-requests-gssapi
Requires:       python3-mock
Requires:       python3-flask-oidc
Requires:       python3-click
Requires:       python3-flask-migrate
Requires:       python3-stomppy
Requires:       python3-fedora-messaging
Requires:       python3-prometheus_client
Requires:       waiverdb-common = %{version}-%{release}
%endif

%description
WaiverDB is a companion service to ResultsDB, for recording waivers
against test results.

%package common
Summary: Common resources for WaiverDB subpackages.

%description common
This package is not useful on its own.  It contains common filesystem resources
for other WaiverDB subpackages.

%package cli
Summary: A CLI tool for interacting with waiverdb
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  python3-click
BuildRequires:  python3-requests-gssapi
Requires:       python3-click
Requires:       python3-requests-gssapi
%else
BuildRequires:  python-click
BuildRequires:  python-requests-gssapi
Requires:       python-click
Requires:       python-requests-gssapi
Requires:       python-configparser
# For xmlrpc.client
Requires:       python2-future
%endif

Requires:       waiverdb-common = %{version}-%{release}

%description cli
This package contains a CLI tool for interacting with waiverdb.

Primarily, submitting new waiverdbs.

%prep
%setup -q -n %{name}-%{upstream_version}

# We guard against version flask-restful=0.3.6 in requirements.txt,
# but the version in Fedora is patched to work.
sed -i '/Flask-RESTful/d' requirements.txt

# Replace any staging urls with prod ones
sed -i 's/\.stg\.fedoraproject\.org/.fedoraproject.org/g' conf/client.conf.example

%build
%if 0%{?fedora} || 0%{?rhel} > 7
%py3_build
make -C docs html man text
%else
%py2_build
%endif

%install
%if 0%{?fedora} || 0%{?rhel} > 7
%py3_install
%else
PYTHONDONTWRITEBYTECODE=1 %py2_install
%endif

%if ! %{with server}
# Need to properly split out the client one day...
rm %{buildroot}%{_bindir}/waiverdb
ls -d %{buildroot}%{python2_sitelib}/waiverdb/* | grep -E -v '(__init__.py|cli.py)$' | xargs rm -r
%endif

install -d %{buildroot}%{_sysconfdir}/waiverdb/
install -m0644 \
    conf/client.conf.example \
    %{buildroot}%{_sysconfdir}/waiverdb/client.conf

%if 0%{?fedora} || 0%{?rhel} > 7
install -D -m0644 \
    docs/_build/man/waiverdb-cli.1 \
    %{buildroot}%{_mandir}/man1/waiverdb-cli.1

install -D -m0644 \
    docs/_build/man/client.conf.5 \
    %{buildroot}%{_mandir}/man5/waiverdb-client.conf.5

install -D -m0644 \
    docs/_build/man/waiverdb.7 \
    %{buildroot}%{_mandir}/man7/waiverdb.7
%endif

# Tests don't make sense here now that we require postgres to run them.
#%%check
#export PYTHONPATH=%%{buildroot}/%%{python3_sitelib}
#py.test-3 tests/

%if %{with server}
%files
%{python3_sitelib}/%{name}
%exclude %{python3_sitelib}/%{name}/__init__.py
%exclude %{python3_sitelib}/%{name}/__pycache__/__init__.*pyc
%exclude %{python3_sitelib}/%{name}/cli.py
%exclude %{python3_sitelib}/%{name}/__pycache__/cli.*.pyc
%attr(755,root,root) %{_bindir}/waiverdb
%endif

%files common
%license COPYING
%doc README.md conf
%if 0%{?fedora} || 0%{?rhel} > 7
%doc docs/_build/html docs/_build/text
%dir %{python3_sitelib}/%{name}
%dir %{python3_sitelib}/%{name}/__pycache__
%{python3_sitelib}/%{name}/__init__.py
%{python3_sitelib}/%{name}/__pycache__/__init__.*pyc
%{python3_sitelib}/%{name}*.egg-info
%else
%dir %{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}/__init__.py*
%{python2_sitelib}/%{name}*.egg-info
%endif

%files cli
%license COPYING
%if 0%{?fedora} || 0%{?rhel} > 7
%{python3_sitelib}/%{name}/cli.py
%{python3_sitelib}/%{name}/__pycache__/cli.*.pyc
%else
%{python2_sitelib}/%{name}/cli.py*
%endif
%attr(755,root,root) %{_bindir}/waiverdb-cli
%config(noreplace) %{_sysconfdir}/waiverdb/client.conf

%if 0%{?fedora} || 0%{?rhel} > 7
%{_mandir}/man1/waiverdb-cli.1*
%{_mandir}/man5/waiverdb-client.conf.5*
%{_mandir}/man7/waiverdb.7*
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-2
- Rebuilt for Python 3.9

* Tue Mar 10 2020 Valerij Maljulin <vmaljuli@redhat.com> - 1.1.6-1
- Version 1.1.5 was bumped due to error during the release

* Mon Mar 9 2020 Valerij Maljulin <vmaljuli@redhat.com> - 1.1.5-1
- STOMP connection will always disconnect regardless of errors
- Added ``docker-compose`` support

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Luiz Carvalho <lui@redhat.com> - 1.1.4-1
- New ``/config`` API endpoint to expose the application configuration
- Retry sending STOMP message after a delay
- Revert allow overriding krb_principal option for waiverdb-cli

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Lukas Holecek <lholecek@redhat.com> - 1.1.3-1
- Allow overriding krb_principal option for waiverdb-cli
- Code optimizations and improvements

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Lukas Holecek <lholecek@redhat.com> - 1.1.1-1
-  Move CORS header support to flask-cors library

* Wed May 15 2019 Lukas Holecek <lholecek@redhat.com> - 1.1.0-1
- Allow optional trailing slash for about endpoint
- Add ``proxied_by`` in the CLI
- Update dependencies for Jenkins slave
- Test proxied_by with access control
- Restrict waiver creation based on users/groups and testcase

* Mon Feb 11 2019 Giulia Naponiello <gnaponie@redhat.com> - 0.14.0-1
- Fix incorrect splitting of Python files into subpackages.
- Improve authentication error response.
- Introduce a /metrics endpoint to the API for monitoring reasons.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13.0-2
- Fix incorrect splitting of Python files into subpackages

* Mon Jan 14 2019 Matt Prahl <mprahl@redhat.com> - 0.13.0-1
- Stop validating subject types against a hard-coded list. Since Greenwave
  now supports arbitrary subject types, this list of valid subject types
  no longer needs to be maintained.

* Mon Dec 03 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-4
- Remove ambiguous python buildrequires and stop dragging in Python 2

* Wed Aug 15 2018 Ralph Bean - 0.11.0-3
- Fixed requires lines for epel7.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Dan Callaghan <dcallagh@redhat.com> - 0.11.0-1
- new upstream release 0.11.0:
  https://docs.pagure.org/waiverdb/release-notes.html#waiverdb-0-11

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.7

* Thu May 10 2018 Lukas Holecek <lholecek@redhat.com> - 0.10.0-1
- Comment is now explicitly required when creating waivers (both in API and
  CLI).
- Multiple waivers can now be created with single POST request (#98). To create
  multiple waivers, POST list to "waivers/" instead of single waiver.
- When creating a waiver by referring to a result ID, WaiverDB now accepts
  results with ``'type': 'brew-build'`` as an alias for ``'koji_build'``.
- Messaging can be disabled is settings with ``MESSAGE_PUBLISHER = None``.
- The ``KERBEROS_HTTP_HOST`` setting in the server configuration is now
  ignored. This setting is no longer needed because GSSAPI will automatically
  find a key in the Kerberos keytab matching the service principal in the
  client request.
- New man pages are available for ``waiverdb-cli(1)`` and ``waiverdb(7)`` (REST
  API).
- Changed error message for bad ``since`` value. E.g.
  ``api/v1.0/waivers/?since=123`` results in HTTP 400 with message
  ``{"message": {"since": "time data '123' does not match format
  '%%Y-%%m-%%dT%%H:%%M:%%S.%%f'"}}``.
- CORS headers are now supported for every request (#160).
- Wrong ``subject`` filter produces more user-friendly error (#162).
- Setting a keytab file is no longer required: if one is not explicitly set,
  ``/etc/krb5.keytab`` will be used (#55).
- Unused option ``resultsdb_api_url`` was removed from client.conf.
- Containers on Quay (`<https://quay.io/repository/factory2/waiverdb>`__).

* Mon Mar 12 2018 Ralph Bean <rbean@redhat.com - 0.9.1-1
- Include new resultsdb_api_url config for the client.
- Port to python3.

* Thu Mar 01 2018 Dan Callaghan <dcallagh@redhat.com> - 0.9.0-1
- new upstream release 0.9.0:
  https://docs.pagure.org/waiverdb/release-notes.html#waiverdb-0-9

* Fri Feb 23 2018 Giulia Naponiello <gnaponie@redhat.com> - 0.8.0-1
- Removed support to SQLite in favor of PostgreSQL.
- Fixed and improved interaction with PostgreSQL.
- Added information on the README file on how to configure the db.

* Fri Feb 16 2018 Giulia Naponiello <gnaponie@redhat.com> - 0.7.0-2
- Bump the version to fix a minor issue.

* Fri Feb 16 2018 Giulia Naponiello <gnaponie@redhat.com> - 0.7.0-1
- Backward compatibility for submitting a waiver using the result_id.
  This feature will be removed in the near future.
- You can now waive the absence of a result. Now it is possible to
  submit waivers using a subject/testcase.
- Added logo in the README page.
- Dummy authentication for CLI for developing and debugging reasons.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Dan Callaghan <dcallagh@redhat.com> - 0.5.0-2
- waiverdb-cli requires python-configparser (RHBZ#1538463)

* Thu Jan 11 2018 Giulia Naponiello <gnaponie@redhat.com> - 0.5.0-1
- Return error messages in JSON
- Support SSL cert auth
- Allow proxyuser
  https://docs.pagure.org/waiverdb/release-notes.html#waiverdb-0-5

* Thu Dec 07 2017 Ralph Bean <rbean@redhat.com> - 0.4.0-2
- Synchronize specfile with upstream.
- Docs are back.

* Tue Nov 07 2017 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- Latest upstream.
- Include new waiverdb-cli subpackage.
- Temporarilly disable building the docs,
  https://pagure.io/waiverdb/issue/90

* Thu Oct 05 2017 Ralph Bean <rbean@redhat.com> - 0.3.1-2
- Require only python-fedmsg-core.

* Wed Sep 27 2017 Matt Jia <mjia@redhat.com> - 0.3.1-1
- Bump the version to fix some minor issues.

* Tue Sep 26 2017 Matt Jia <mjia@redhat.com> - 0.3.1
- new upstream release 0.3.1:
  https://docs.pagure.org/waiverdb/release-notes.html#waiverdb-0-3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Dan Callaghan <dcallagh@redhat.com> - 0.2.1-1
- new upstream release 0.2.1:
  https://docs.pagure.org/waiverdb/release-notes.html#waiverdb-0-2

* Wed May 03 2017 Matt Jia <mjia@redhat.com> - 0.1.1-2
- Fix the long line error in the spec file reported by rpmlint

* Wed Apr 26 2017 Matt Jia <mjia@redhat.com> - 0.1.1-1
- Updated to release 0.1.1

