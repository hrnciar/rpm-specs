%global srcname synapse

# Version suffix in URL when building release candidates
%global rcx %{nil}

%{?python_enable_dependency_generator}

Name:       matrix-%{srcname}
Version:    1.18.0
Release:    1%{?dist}
Summary:    A Matrix reference homeserver written in Python using Twisted
License:    ASL 2.0
URL:        https://github.com/matrix-org/%{srcname}
Source0:    %{url}/archive/v%{version}%{rcx}/%{srcname}-%{version}%{rcx}.tar.gz
Source1:    synapse.sysconfig
Source2:    synapse.service
# https://github.com/matrix-org/synapse/pull/8208
Patch1:     0001-Use-TLSv1.2-for-fake-servers-in-tests.patch
BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Test dependencies
BuildRequires:  python3-mock >= 2.0
BuildRequires:  python3-parameterized >= 0.7.0
BuildRequires:  /usr/bin/openssl

# Package dependencies
#BuildRequires:  python3-txacme >= 0.9.2
BuildRequires:  python3-attrs >= 19.1.0
BuildRequires:  python3-authlib
BuildRequires:  python3-bcrypt >= 3.1.0
BuildRequires:  python3-bleach >= 1.4.3
BuildRequires:  python3-canonicaljson >= 1.1.3
BuildRequires:  python3-daemonize >= 2.3.1
BuildRequires:  python3-frozendict >= 1.0
BuildRequires:  python3-idna >= 2.5
BuildRequires:  python3-jinja2 >= 2.9
BuildRequires:  python3-jsonschema >= 2.5.1
BuildRequires:  python3-jwt
BuildRequires:  python3-lxml >= 3.5.0
BuildRequires:  python3-matrix-synapse-ldap3 >= 0.1
BuildRequires:  python3-msgpack >= 0.5.2
BuildRequires:  python3-netaddr >= 0.7.18
BuildRequires:  python3-phonenumbers >= 8.2.0
BuildRequires:  python3-pillow >= 4.3.0
BuildRequires:  python3-prometheus_client < 0.9.0
BuildRequires:  python3-pyOpenSSL >= 16.0.0
BuildRequires:  python3-pyasn1 >= 0.1.9
BuildRequires:  python3-pyasn1-modules >= 0.0.7
BuildRequires:  python3-pymacaroons-pynacl >= 0.13.0
BuildRequires:  python3-pynacl >= 1.2.1
BuildRequires:  python3-pysaml2 >= 4.5.0
BuildRequires:  python3-pyyaml >= 3.11
BuildRequires:  python3-service-identity >= 18.1.0
BuildRequires:  python3-signedjson >= 1.1.0
BuildRequires:  python3-sortedcontainers >= 1.4.4
BuildRequires:  python3-systemd >= 231
BuildRequires:  python3-treq >= 15.1
BuildRequires:  python3-twisted >= 18.9.0
BuildRequires:  python3-typing-extensions >= 3.7.4
BuildRequires:  python3-unpaddedbase64 >= 1.1.0
BuildRequires:  systemd

Requires(pre):  shadow-utils
Requires:       systemd
%{?systemd_requires}

%description
Matrix is an ambitious new ecosystem for open federated Instant Messaging and
VoIP. Synapse is a reference "homeserver" implementation of Matrix from the
core development team at matrix.org, written in Python/Twisted. It is intended
to showcase the concept of Matrix and let folks see the spec in the context of
a coded base and let you run your own homeserver and generally help bootstrap
the ecosystem.


%prep
%autosetup -p1 -n %{srcname}-%{version}%{rcx}

# We don't support the built-in client so remove all the bundled JS.
rm -rf synapse/static


%build
%py3_build


%install
%py3_install

# Synapse includes some benchmarks in a separate Python package named "synmark"
# which is installed by default. Remove it to avoid shipping it in the Fedora
# package, since it is unlikely to be useful to end users.
rm -r %{buildroot}%{python3_sitelib}/synmark/

install -p -D -T -m 0644 contrib/systemd/log_config.yaml %{buildroot}%{_sysconfdir}/synapse/log_config.yaml
install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/synapse
install -p -D -T -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/synapse.service
install -p -d -m 755 %{buildroot}/%{_sharedstatedir}/synapse


%check
PYTHONPATH=. trial-3 tests


%pre
getent group synapse >/dev/null || groupadd -r synapse
getent passwd synapse >/dev/null || \
    useradd -r -g synapse -d %{_sharedstatedir}/synapse -s /sbin/nologin \
    -c "The user for the Synapse Matrix server" synapse
exit 0

%post
%systemd_post synapse.service

%preun
%systemd_preun synapse.service

%postun
%systemd_postun_with_restart synapse.service


%files
%license LICENSE
%doc *.rst
%config(noreplace) %{_sysconfdir}/sysconfig/synapse
%{python3_sitelib}/synapse/
%{python3_sitelib}/matrix_synapse*.egg-info/
%{_bindir}/*
%{_unitdir}/synapse.service
%attr(755,synapse,synapse) %dir %{_sharedstatedir}/synapse
%attr(755,synapse,synapse) %dir %{_sysconfdir}/synapse
%attr(644,synapse,synapse) %config(noreplace) %{_sysconfdir}/synapse/*


%changelog
* Sat Aug 29 2020 Kai A. Hiller <V02460@gmail.com> - 1.18.0-1
- Update to v1.18.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13.0-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Dan Callaghan <djc@djc.id.au> - 1.13.0-1
- Update to v1.13.0

* Sun May 17 2020 Dan Callaghan <djc@djc.id.au> - 1.12.4-1
- Update to v1.12.4

* Wed Apr 22 2020 Kai A. Hiller <V02460@gmail.com> - 1.12.3-1
- Update to v1.12.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Arjen Heidinga <dexter@beetjevreeemd.nl> - 1.8.0-1
- Update to v1.8.0

* Tue Dec 31 2019 Dan Callaghan <djc@djc.id.au> - 1.7.2-1
- Update to v1.7.2

* Tue Dec 03 2019 Dan Callaghan <djc@djc.id.au> - 1.6.1-1
- Update to v1.6.1

* Fri Nov 08 2019 Kai A. Hiller <V02460@gmail.com> - 1.5.1-1
- Update to v1.5.1
- Add Python 3.8 compatibility

* Fri Oct 11 2019 Kai A. Hiller <V02460@gmail.com> - 1.4.0-1
- Update to v1.4.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Kai A. Hiller <V02460@gmail.com> - 1.2.1-1
- Update to v1.2.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Dan Callaghan <djc@djc.id.au> - 1.0.0-1
- Update to v1.0.0 release, including new protocol-mandated TLS
  certificate verification logic. See:
  https://github.com/matrix-org/synapse/blob/master/docs/MSC1711_certificates_FAQ.md

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jeremy Cline <jeremy@jcline.org> - 0.34.0.1-2
- synapse user should own its configuration directory (rhbz 1662672)

* Fri Jan 11 2019 Jeremy Cline <jeremy@jcline.org> - 0.34.0.1-1
- Update to v0.34.0.1, fixes CVE-2019-5885

* Fri Dec 28 2018 Jeremy Cline <jeremy@jcline.org> - 0.34.0-1
- Update to v0.34.0
- Switch to Python 3

* Thu Sep 06 2018 Jeremy Cline <jeremy@jcline.org> - 0.33.3.1-1
- Update to v0.33.3.1
- Use the Python dependency generator.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Jeremy Cline <jeremy@jcline.org> - 0.31.2-1
- Update to v0.31.2
- https://github.com/matrix-org/synapse/releases/tag/v0.31.2

* Wed Jun 13 2018 Jeremy Cline <jeremy@jcline.org> - 0.31.1-2
- Stop using Python dependency generator

* Wed Jun 13 2018 Jeremy Cline <jeremy@jcline.org> - 0.31.1-1
- Update to v0.31.1
- Fix CVE-2018-12291

* Thu May 24 2018 Jeremy Cline <jeremy@jcline.org> - 0.29.1-1
- Update to the latest upstream release.
- Use the Python dependency generator.

* Tue May 01 2018 Jeremy Cline <jeremy@jcline.org> - 0.28.1-1
- Update to the latest upstream release.

* Wed Apr 11 2018 Jeremy Cline <jeremy@jcline.org> - 0.27.3-1
- Update to the latest upstream release.

* Mon Mar 26 2018 Jeremy Cline <jeremy@jcline.org> - 0.27.2-1
- Update to the latest upstream release.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Jeremy Cline <jeremy@jcline.org> - 0.26.0-1
- Update to latest upstream

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.23.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Oct 03 2017 Jeremy Cline <jeremy@jcline.org> - 0.23.1-1
- Update to latest upstream
- Include patch to work with ujson-2.0+

* Fri Sep 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.1-4
- Use python2 prefix for packages whenever possible
- Add missing %%{?systemd_requires}

* Wed Aug 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.22.1-3
- Switch to python-bcrypt, BZ 1473018.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Jeremy Cline <jeremy@jcline.org> - 0.22.1-1
- Update to the latest upstream release

* Thu Jul 06 2017 Jeremy Cline <jeremy@jcline.org> - 0.22.0-1
- Update to the latest upstream release (#1462045)

* Fri Jun 23 2017 Jeremy Cline <jeremy@jcline.org> - 0.21.1-1
- Update to latest upstream release

* Tue May 30 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.3-4
- use _sharedstatedir  rather than _localstatedir

* Wed May 17 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.3-3
- Remove bundled JS
- Fix some typos in the summary and description

* Tue Apr 04 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.3-2
- Remove the duplicate requirement on pysaml

* Tue Mar 28 2017 Jeremy Cline <jeremy@jcline.org> - 0.19.3-1
- Initial package
