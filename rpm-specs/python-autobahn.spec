# Cannot build doc as of this moment. Construction requires unpackaged python2
# only deps.
%global with_doc 0
%global pypi_name autobahn
%global project_owner crossbario
%global github_name autobahn-python
%global _docdir_fmt %{name}

Name:           python-%{pypi_name}
Version:        19.10.1
Release:        3%{?dist}
Summary:        Python networking library for WebSocket and WAMP

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
# pypi release doen't include README, nor doc, so using github instead
# See: https://github.com/tavendo/AutobahnPython/issues/429
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/v%{version}/%{github_name}-%{version}.tar.gz
# By default it requires version 2.7 but according to tests and the requirement on twilio, it works with 2.6.1 which is in fedora.
# Until https://bugzilla.redhat.com/show_bug.cgi?id=1715680 is done, this is required.
# Take tare before updating that it is still the case with the updated version.
Patch0:         lower-deps-cryptographie.patch

BuildArch:      noarch
%if 0%{with_doc}
BuildRequires:  python3-scour # No python 3, https://github.com/oberstet/scour/issues/4
BuildRequires:  python3-scons
BuildRequires:  python3-taschenmesser # No python 3, https://github.com/oberstet/taschenmesser/issues/3
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-bootstrap # Not packaged yet
BuildRequires:  python3-sphinxcontrib-spelling # Not packaged yet
BuildRequires:  python3-repoze-sphinx-autointerface
BuildRequires:  python3-pyenchant
%endif # End with_doc

%description
Autobahn a networking library that is part of the Autobahn project and provides
implementations of
* The WebSocket Protocol http://tools.ietf.org/html/rfc6455_
* The Web Application Messaging Protocol (WAMP) http://wamp.ws
for Twisted and asyncio on Python 2 & 3 and for writing servers and clients.


%package -n     python3-%{pypi_name}
Summary:        Python networking library for WebSocket and WAMP
BuildArch:      noarch
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-cffi
BuildRequires:  python3-mock >= 1.3.0
BuildRequires:  python3-pytest >= 2.8.6
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-six >= 1.11.0
BuildRequires:  python3-txaio >= 2.2.1
BuildRequires:  python3-pynacl
BuildRequires:  python3-cryptography
Requires:       python3-zope-interface >= 3.6
Requires:       python3-ujson >= 1.33
Requires:       python3-wsaccel >= 0.6.2
Requires:       python3-snappy >= 0.5
Requires:       python3-lz4 >= 0.2.1
Requires:       python3-msgpack >= 0.4.6
Requires:       python3-six >= 1.11.0
Requires:       python3-txaio >= 2.10.0
Requires:       python3-cffi
Requires:       python3-cryptography
Requires:       python3-pynacl
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Autobahn a networking library that is part of the Autobahn project and provides
implementations of
* The WebSocket Protocol http://tools.ietf.org/html/rfc6455_
* The Web Application Messaging Protocol (WAMP) http://wamp.ws
for Twisted and asyncio on Python 2 & 3 and for writing servers and clients.


%if 0%{with_doc}
%package doc
Summary:        Python networking library for WebSocket and WAMP

%description doc
Autobahn a networking library that is part of the Autobahn project and provides
implementations of
* The WebSocket Protocol http://tools.ietf.org/html/rfc6455_
* The Web Application Messaging Protocol (WAMP) http://wamp.ws
for Twisted and asyncio on Python 2 & 3 and for writing servers and clients.

HTML documentation
%endif # with doc


%prep
%setup -qn %{github_name}-%{version}
%patch0 -p1

# Remove upstream's egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

%if 0%{with_doc}
# Build doc
cd doc && make build_no_network
%endif


%install
%py3_install


%check
# Ignore tests that rely on optionnal and not packaged deps.
USE_ASYNCIO=1 PYTHONPATH=$(pwd) py.test-%{python3_version} --pyargs autobahn -k 'not test_unknown_arg and not test_no_memory_arg and not test_basic and not test_argon2id_static and not test_websocket_custom_loop and not TestSerializer and not test_rng'


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst DEVELOPERS.md
%{_bindir}/wamp
%{python3_sitelib}/%{pypi_name}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{pypi_name}/
%dir %{python3_sitelib}/twisted
%dir %{python3_sitelib}/twisted/plugins
%dir %{python3_sitelib}/twisted/plugins/__pycache__
%{python3_sitelib}/twisted/plugins/autobahn*.py
%{python3_sitelib}/twisted/plugins/__pycache__/autobahn*.py*

%if 0%{with_doc}
%files doc
%license LICENSE
%doc doc/_build
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 19.10.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Orion Poplawski <orion@nwra.com> - 19.10.1-1
- Update to 19.10.1
- Drop BR on pep8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.8.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Yatin Karel <ykarel@redhat.com> - 19.8.1-1
- Update to 19.8.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 19.7.2-3
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Julien Enselme <jujens@jujens.eu> - 19.7.2-2
- Lower requirement on python-cryptography.

* Tue Jul 30 2019 Julien Enselme <jujens@jujens.eu> - 19.7.2-1
- Update to 19.7.2
- Skip test about random generator which can make build hang.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 19.7.1-1
- Update to 19.7.1

* Sat Mar 23 2019 Julien Enselme <jujens@jujens.eu> - 19.3.2-1
- Update to 19.3.2

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-2
- Subpackage python2-autobahn has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Julien Enselme <jujens@jujens.eu> - 18.7.1-1
- Update to 18.7.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 18.6.1-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Julien Enselme <jujens@jujens.eu> - 18.6.1-1
- Update to 18.6.1

* Sat May 12 2018 Julien Enselme <jujens@jujens.eu> - 18.5.1-1
- Update to 18.5.1

* Sun Apr 15 2018 Julien Enselme <jujens@jujens.eu> - 18.4.1-2
- Correct requires

* Sun Apr 15 2018 Julien Enselme <jujens@jujens.eu> - 18.4.1-1
- Update to 18.4.1

* Tue Mar 06 2018 Julien Enselme <jujens@jujens.eu> - 18.3.1-1
- Update to 18.3.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17.10.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Nov 06 2017 Julien Enselme <jujens@jujens.eu> - 17.10.1-1
- Update to 17.10.1
- Use %%version to get the sources

* Tue Sep 26 2017 Julien Enselme <jujens@jujens.eu> - 17.9.3-1.gitd398c4d
- Update to 17.9.3

* Thu Sep 14 2017 Julien Enselme <jujens@jujens.eu> - 17.9.2-1.git164106a
- Update to 17.9.2

* Wed Sep 06 2017 Julien Enselme <jujens@jujens.eu> - 17.9.1-1.gitb813019
- Update to 17.9.1

* Sat Aug 19 2017 Julien Enselme <jujens@jujens.eu> - 17.8.1-1.git96543dd
- Update to 17.8.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.7.1-2.git9ad7878
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Julien Enselme <jujens@jujens.eu> - 17.7.1-1.git9ad7878
- Update to 17.7.1

* Sat Jul 01 2017 Julien Enselme <jujens@jujens.eu> - 17.6.2-1.gitbc2a1b3
- Update to 17.6.2

* Sat Jun 10 2017 Julien Enselme <jujens@jujens.eu> - 17.6.1-1.gite69b314
- Update to 17.6.1

* Sun May 07 2017 Julien Enselme <jujens@jujens.eu> - 17.5.1-1.git73bcac2
- Update to 17.5.1

* Tue Apr 18 2017 Julien Enselme <jujens@jujens.eu> - 0.18.2-1.git731228a
- Update to 0.18.2

* Wed Apr 05 2017 Julien Enselme <jujens@jujens.eu> - 0.18.1-1.gitfd7ec41
- Update to 0.18.1

* Tue Feb 28 2017 Julien Enselme <jujens@jujens.eu> - 0.17.2-1.git0eef8c7
- Update to 0.17.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2.git81d9276
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

*  Mon Dec 26 2016 Julien Enselme <jujens@jujens.eu> - 0.17.0-1.git81d9276
- Update to 0.17.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-3.gitade9eb5
- Rebuild for Python 3.6

* Sat Oct 01 2016 Julien Enselme <jujens@jujens.eu> - 0.16.0-2.gitade9eb5
- Fix tests for pytest3

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 0.16.0-1.gitade9eb5
- Update to 0.16.0

* Mon Jul 25 2016 Julien Enselme <jujens@jujens.eu> - 0.15.0-1.git43b57f8
- Update to 0.15.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2.git81f693d
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Julien Enselme <jujens@jujens.eu> - 0.14.0-1.git81f693d
- Update to 0.14.0

* Sat Feb 27 2016 Julien Enselme <jujens@jujens.eu> - 0.12.1-1.git22b1183
- Update to 0.12.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-3.gita69e704
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.7-2.gita69e704
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 6 2015 Julien Enselme <jujens@jujens.eu> - 0.10.7-1.gita69e7048
- Update to 0.10.7

* Sun Sep 6 2015 Julien Enselme <jujens@jujens.eu> - 0.10.6-1.gitb35d99f1
- Update to 0.10.6

* Sat Aug 15 2015 Julien Enselme <jujens@jujens.eu> - 0.10.5-1.git3fce8ac
- Update to 0.10.5.post-2

* Wed Aug 5 2015 Julien Enselme <jujens@jujens.eu> - 0.10.4-3.git29f8acc
- Build python2 and python3 in the same dir
- Update dependencies
- Put python2 package in a subpackage
- Add provides
- Correct %%files section

* Fri Jul 24 2015 Julien Enselme <jujens@jujens.eu> - 0.10.4-2.git29f8acc
- Surround doc package with if
- Remove %%py3dir macro
- Add CFLAGS in %%build

* Sat Jul 18 2015 Julien Enselme <jujens@jujens.eu> - 0.10.4-1.git29f8acc
- Initial packaging
