Name:       odcs
Version:    0.2.50
Release:    1%{?dist}
Summary:    The On Demand Compose Service


License:    MIT
URL:        https://pagure.io/odcs
Source0:    https://files.pythonhosted.org/packages/source/o/%{name}/%{name}-%{version}.tar.gz
Source1:    odcs-backend.service
# In Fedora, "pyldap" is only for python3, not for python2. Therefore we
# have to patch the requirements.txt to use python-ldap instead of pyldap.
# Both ldap bindings are compatible on Python code level.
Patch0:     odcs-pythonldap.patch
# Fedora related configuration for ODCS.
Patch1:     odcs-fedora-conf.patch

BuildArch:    noarch

BuildRequires:    help2man
BuildRequires:    python3-libmodulemd
BuildRequires:    gobject-introspection
BuildRequires:    systemd
BuildRequires:    python3-devel
BuildRequires:    python3-pdc-client
BuildRequires:    python3-fedora
BuildRequires:    python3-productmd
BuildRequires:    python3-funcsigs
BuildRequires:    python3-openidc-client
BuildRequires:    python3-setuptools
BuildRequires:    python3-flask-sqlalchemy
BuildRequires:    python3-flask-migrate
BuildRequires:    python3-nose
BuildRequires:    python3-mock
BuildRequires:    python3-tabulate
BuildRequires:    python3-six
BuildRequires:    python3-flask
BuildRequires:    python3-systemd
BuildRequires:    python3-defusedxml
BuildRequires:    python3-koji
BuildRequires:    python3-httplib2
BuildRequires:    python3-pyOpenSSL
BuildRequires:    python3-sqlalchemy
BuildRequires:    python3-ldap
BuildRequires:    python3-gobject-base
BuildRequires:    python3-flask-script
BuildRequires:    python3-flask-login
BuildRequires:    python3-munch
BuildRequires:    python3-moksha-hub
BuildRequires:    python3-psutil
BuildRequires:    python3-flufl-lock
BuildRequires:    python3-celery
BuildRequires:    python3-kobo
BuildRequires:    python3-prometheus_client

%{?systemd_requires}

Requires(pre): shadow-utils
Requires:    systemd
Requires:    pungi
Requires:    python3-pdc-client
Requires:    python3-fedora
Requires:    python3-funcsigs
Requires:    python3-openidc-client
Requires:    python3-productmd
Requires:    hardlink
Requires:    python3-libmodulemd
Requires:    gobject-introspection
Requires:    python3-moksha-hub
Requires:    python3-psutil
Requires:    python3-flufl-lock
Requires:    python3-celery
Requires:    python3-flask
Requires:    python3-flask-login
Requires:    python3-flask-sqlalchemy
Requires:    python3-systemd
Requires:    python3-ldap
Requires:    python3-defusedxml
Requires:    python3-flask-script
Requires:    python3-flask-migrate
Requires:    python3-fedora-messaging
Requires:    fedora-messaging
Requires:    python3-kobo
Requires:    python3-prometheus_client

Requires:    python3-odcs-common = %{version}-%{release}


%description
The On Demand Compose Service (ODCS) creates temporary composes using Pungi
tool and manages their lifetime. The composes can be requested by external
services or users using the REST API provided by Flask frontend.

%package -n python3-odcs-common
Summary:        ODCS subpackage providing code shared between server and client.
%{?python_provide:%python_provide python3-odcs-client}

Requires:       python3-six

%description -n python3-odcs-common
ODCS subpackage providing code shared between server and client.

%package -n python3-odcs-client
Summary:        ODCS client module
%{?python_provide:%python_provide python3-odcs-client}

Requires:       python3-six
Requires:       python3-requests
Requires:       python3-requests-kerberos
Requires:       python3-odcs-common = %{version}-%{release}

%description -n python3-odcs-client
Client library for sending requests to On Demand Compose Service (ODCS).

%package -n odcs-client
Summary:        ODCS command line client
Requires:       python3-openidc-client
Requires:       python3-odcs-client = %{version}-%{release}

%description -n odcs-client
Command line client for sending requests to ODCS.


%prep
%setup -q

sed -i '/futures/d' common/requirements.txt
sed -i '/futures/d' client/requirements.txt
sed -i '/futures/d' server/requirements.txt

%patch0 -p1 -b .pyldap
%patch1 -p1

%build
%py3_build


%install
%py3_install

export PYTHONPATH=%{buildroot}%{python3_sitelib}
mkdir -p %{buildroot}%{_mandir}/man1
for command in odcs-manager odcs-frontend odcs-gencert odcs-upgradedb ; do
export ODCS_CONFIG_FILE=server/conf/config.py
help2man -N \
    --version-string=%{version} %{buildroot}%{_bindir}/$command  > \
    %{buildroot}%{_mandir}/man1/$command.1 || \
    %{buildroot}%{_bindir}/$command --help

done

install -d -m 0755 %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/

install -d -m 0755 %{buildroot}%{_datadir}/odcs
install -p -m 0644 server/contrib/odcs.wsgi %{buildroot}%{_datadir}/odcs


%pre
getent group odcs >/dev/null || groupadd -r odcs
getent passwd odcs >/dev/null || \
    useradd -r -g odcs -s /sbin/nologin \
    -c "On Demand Compose Service user" odcs
exit 0

%post
%systemd_post odcs-backend.service

%preun
%systemd_preun odcs-backend.service

%postun
%systemd_postun_with_restart odcs-backend.service

%check
nosetests-%{python3_version} -v

%files -n odcs-client
%doc README.md
%license LICENSE
%{_bindir}/odcs

%files -n python3-odcs-common
%doc README.md
%license LICENSE
%dir %{python3_sitelib}/odcs/
%{python3_sitelib}/odcs/__init__.py*
%{python3_sitelib}/odcs/common/
%{python3_sitelib}/odcs-%{version}-py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/odcs/__pycache__

%files -n python3-odcs-client
%doc README.md
%license LICENSE
%dir %{python3_sitelib}/odcs/
%{python3_sitelib}/odcs/client/
%exclude %{python3_sitelib}/odcs/__pycache__

%files
%doc README.md
%license LICENSE
%{_unitdir}/odcs-backend.service
%{python3_sitelib}/odcs/server
%{_bindir}/odcs-*
%{_mandir}/man1/odcs-*.1*
%{_datadir}/odcs
%dir %{_sysconfdir}/odcs
%config(noreplace) %{_sysconfdir}/odcs/config.py
%config(noreplace) %{_sysconfdir}/odcs/pungi.conf
%config(noreplace) %{_sysconfdir}/odcs/raw_config_wrapper.conf
%exclude %{_sysconfdir}/odcs/*.py[co]
%exclude %{_sysconfdir}/odcs/__pycache__
%exclude %{python3_sitelib}/odcs/__pycache__


%changelog
* Tue Sep 08 2020 Lubomír Sedlář <lsedlar@redhat.com> - 0.2.50-1
- New upstream release

* Wed Aug 19 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.49-1
- new version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.48-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 31 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.48-1
- new version

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.46-2
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.46-1
- new version

* Tue Apr 21 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.45-1
- new version

* Mon Apr 20 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.44-1
- new version

* Wed Apr 01 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.42-1
- new version

* Fri Mar 20 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.41-1
- new version

* Mon Mar 16 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.40-1
- new version

* Wed Mar 04 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.39-1
- new version

* Tue Feb 25 2020 Jan Kaluza <jkaluza@redhat.com> - 0.2.38-1
- new version

* Thu Oct 24 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.36-4
- add fedora-messaging requirement.

* Wed Oct 23 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.36-3
- backport patch to support fedora-messaging.

* Tue Oct 22 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.36-2
- Add missing requires, backport patch to disable SNI when not needed.

* Thu Oct 17 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.36-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.23-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.23-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.23-2
- require python3-fedmsg instead of fedmsg-hub

* Fri Feb 15 2019 Jan Kaluza <jkaluza@redhat.com> - 0.2.23-1
- new version

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.2.7-5
- Update requires for python-gobject -> python2-gobject rename

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Ralph Bean <rbean@redhat.com> - 0.2.7-1
- new version

* Wed Jun 20 2018 Ralph Bean <rbean@redhat.com> - 0.2.6.2-1
- new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6.1-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6.1-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Ralph Bean <rbean@redhat.com> - 0.2.6.1-1
- new version

* Thu Jun 14 2018 Ralph Bean <rbean@redhat.com> - 0.2.6-1
- new version

* Wed Jun 06 2018 Ralph Bean <rbean@redhat.com> - 0.2.4-2
- Add dep on python-requests-kerberos
  https://pagure.io/odcs/issue/203

* Mon Jun 04 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.4-1
- updated to new version 0.2.4

* Mon May 07 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.3-1
- updated to new version 0.2.3.

* Thu Apr 19 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.2-1
- updated to new version 0.2.2.

* Mon Mar 12 2018 Ralph Bean <rbean@redhat.com> - 0.2.1-2
- Python3 subpackages.

* Mon Mar 12 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.1-1
- updated to new version 0.2.1.

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 26 2018 Jan Kaluza <jkaluza@redhat.com> - 0.2.0-1
- updated to new version 0.2.0.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Jan Kaluza <jkaluza@redhat.com> - 0.1.7-2
- restart odcs-backend.service on failure.

* Mon Feb 05 2018 Jan Kaluza <jkaluza@redhat.com> - 0.1.7-1
- updated to new version 0.1.7.

* Thu Jan 11 2018 Jan Kaluza <jkaluza@redhat.com> - 0.1.6-1
- updated to new version 0.1.6.

* Tue Dec 12 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-5
- do not remove pungi ODCS composes

* Mon Dec 11 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-4
- fix Koji kerberos login with keytab

* Mon Dec 11 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-3
- fix Koji kerberos login with keytab

* Mon Dec 11 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-2
- fix traceback in unique_path.

* Fri Dec 08 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.5-1
- updated to new version 0.1.5

* Fri Nov 24 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.4-1
- updated to new version 0.1.4.

* Fri Nov 24 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.3-1
- updated to new version 0.1.3.

* Wed Nov 01 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.2-1
- updated to new version 0.1.2.

* Mon Oct 30 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.1-3
- Require:hardlink

* Mon Oct 30 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.1-1
- updated to new version 0.1.1.

* Thu Oct 12 2017 Jan Kaluza <jkaluza@redhat.com> - 0.1.0-2
- use http instead of https for pulp .repo file

* Fri Oct 06 2017 Ralph Bean <rbean@redhat.com> - 0.1.0-1
- new version

* Thu Oct 05 2017 Ralph Bean <rbean@redhat.com> - 0.0.8-1
- new version

* Fri Sep 29 2017 Ralph Bean <rbean@redhat.com> - 0.0.7-1
- new version

* Tue Sep 26 2017 Ralph Bean <rbean@redhat.com> - 0.0.6-1
- new version

* Thu Sep 21 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.5-1
- new version

* Thu Aug 10 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.4-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.3-4
- fix reversed condition for python2-* dependencies

* Mon Jul 17 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.3-3
- Add python2- prefix to requirements when it makes sense
- Add -p to install command to preserve timestamp
- Fix macros formatting, use _datadir instead of /usr/share

* Tue Jul 11 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.3-2
- fix dependencies

* Thu Jun 29 2017 Jan Kaluza <jkaluza@redhat.com> - 0.0.3-1
- Initial version of spec file
