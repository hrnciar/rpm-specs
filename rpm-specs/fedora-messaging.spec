%global pkgname fedora-messaging
%global srcname fedora_messaging
%global desc \
Tools and APIs to make working with AMQP in Fedora easier.

%{?python_enable_dependency_generator}

Name:           %{pkgname}
Version:        2.0.1
Release:        3%{?dist}
Summary:        Set of tools for using Fedora's messaging infrastructure

License:        GPLv2+
URL:            https://github.com/fedora-infra/fedora-messaging
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-blinker
BuildRequires:  python3-click
BuildRequires:  python3-crochet
BuildRequires:  python3-jsonschema
BuildRequires:  python3-mock
BuildRequires:  python3-pika
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-pytest
#BuildRequires:  python3-pytest-twisted
BuildRequires:  python3-toml
BuildRequires:  python3-service-identity
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
BuildRequires:  python3-twisted
Requires:       python3-%{pkgname} = %{version}-%{release}

BuildRequires: systemd-rpm-macros

%description %{desc}

%package     -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}
# Drop when https://github.com/fedora-infra/fedora-messaging/pull/51 is released
Requires: python3-service-identity

%description -n python3-%{pkgname} %{desc}


%package doc
Summary:        Documentation for %{pkgname}
%description doc
Documentation for %{pkgname}.


%prep
%autosetup -n %{pkgname}-%{version}


%build
%py3_build
# generate docs
PYTHONPATH=${PWD} sphinx-build-3 -M html -d docs/_build/doctrees docs docs/_build/html
PYTHONPATH=${PWD} sphinx-build-3 -M man -d docs/_build/doctrees docs docs/_build/man
# remove the sphinx-build leftovers
rm -rf docs/_build/*/.buildinfo


%install
%py3_install
install -D -m 644 config.toml.example $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/config.toml
install -D -m 644 configs/fedora.toml $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora.toml
install -D -m 644 configs/fedora.stg.toml $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora.stg.toml
install -D -m 644 configs/cacert.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/cacert.pem
# Yes, this is supposed to be a world-readable private key. It's for public Fedora broker access.
install -D -m 644 configs/fedora-key.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora-key.pem
install -D -m 644 configs/fedora-cert.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora-cert.pem
install -D -m 644 configs/stg-cacert.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/stg-cacert.pem
install -D -m 644 configs/fedora.stg-key.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora.stg-key.pem
install -D -m 644 configs/fedora.stg-cert.pem $RPM_BUILD_ROOT%{_sysconfdir}/fedora-messaging/fedora.stg-cert.pem
install -D -m 644 docs/_build/man/fedora-messaging.1 $RPM_BUILD_ROOT%{_mandir}/man1/fedora-messaging.1
install -D -m 644 fm-consumer@.service $RPM_BUILD_ROOT%{_unitdir}/fm-consumer@.service


%check
#export PYTHONPATH=.
#pytest-3 -vv


%files
%license LICENSE
%doc README.rst
%dir %{_sysconfdir}/fedora-messaging/
%config(noreplace) %{_sysconfdir}/fedora-messaging/config.toml
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora.toml
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora.stg.toml
%config(noreplace) %{_sysconfdir}/fedora-messaging/cacert.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora-key.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora-cert.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/stg-cacert.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora.stg-key.pem
%config(noreplace) %{_sysconfdir}/fedora-messaging/fedora.stg-cert.pem
%{_mandir}/man1/%{name}.*
%{_bindir}/%{name}
%{_unitdir}/fm-consumer@.service

%files -n python3-%{pkgname}
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE
%doc README.rst docs/*.rst docs/_build/html docs/sample_schema_package


%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Tue Dec 03 2019 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0
- Until pytest-twisted is packaged, disable the tests in %%check.

* Tue Sep 03 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.2-1
- Update to 1.7.2. Fixes bug #1742459

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jeremy Cline <jcline@redhat.com> - 1.7.1-1
- Update to v1.7.1

* Wed Jun 19 2019 Pavel Raiskup <praiskup@redhat.com> - 1.7.0-3
- install sample schema documentation cited by
  https://fedora-messaging.readthedocs.io/en/latest/tutorial/schemas.html

* Mon Jun 10 2019 Jeremy Cline <jcline@redhat.com> - 1.7.0-2
- Include the stage config and credentials

* Tue May 21 2019 Jeremy Cline <jcline@redhat.com> - 1.7.0-1
- Update to v1.7.0

* Wed Apr 17 2019 Jeremy Cline <jcline@redhat.com> - 1.6.1-1
- Update to v1.6.1

* Thu Apr 04 2019 Jeremy Cline <jcline@redhat.com> - 1.6.0-1
- Update to v1.6.0

* Thu Mar 07 2019 Aurelien Bompard <abompard@fedoraproject.org> - 1.5.0-2
- Add the Systemd service template file.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jeremy Cline <jeremy@jcline.org> - 1.3.0-1
- Update to v1.3.0

* Mon Jan 21 2019 Jeremy Cline <jeremy@jcline.org> - 1.2.0-1
- Update to v1.2.0

* Thu Nov 15 2018 Jeremy Cline <jeremy@jcline.org> - 1.1.0-1
- Update to v1.1.0

* Wed Oct 10 2018 Jeremy Cline <jeremy@jcline.org> - 1.0.1-1
- Update to v1.0.1

* Wed Oct 10 2018 Jeremy Cline <jeremy@jcline.org> - 1.0.0-1
- Update to v1.0.0

* Fri Sep 07 2018 Jeremy Cline <jeremy@jcline.org> - 1.0.0-0.2b1
- Move dependency generator macro to top of file
- Depend on version + release for the library
- Add python_provide macro

* Wed Aug 29 2018 Jeremy Cline <jeremy@jcline.org> - 1.0.0-0.1b1
- Update to 1.0.0b1
- Drop Python 2 package for Rawhide

* Wed Aug 15 2018 Aurelien Bompard <abompard@fedoraproject.org> - 1.0.0-0.1.a1
- Initial package
