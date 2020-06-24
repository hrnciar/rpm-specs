%global         srcname  acme

%if (0%{?fedora}) || (0%{?rhel} && 0%{?rhel} >= 8)
%bcond_without python3
%else
%bcond_with python3
%endif

%if (0%{?fedora} && 0%{?fedora} >= 30) || (0%{?rhel} && 0%{?rhel} >= 8)
%bcond_with python2
%global         SPHINXBUILD sphinx-build-3
%else
%bcond_without python2
%global         SPHINXBUILD sphinx-build
%endif

Name:           python-acme
Version:        1.5.0
Release:        1%{?dist}
Summary:        Python library for the ACME protocol
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/acme
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
# Key mentioned in https://certbot.eff.org/docs/install.html#certbot-auto
# Keyring generation steps as follows:
#   gpg2 --keyserver pool.sks-keyservers.net --recv-key A2CFB51FA275A7286234E7B24D17C995CD9775F2
#   gpg2 --export --export-options export-minimal A2CFB51FA275A7286234E7B24D17C995CD9775F2 > gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg
Source2:        gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg

# When running tests argparse is not recognised as provided by core

Patch0:         epel7-setup.patch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-sphinx
%if 0%{?fedora}
BuildRequires:  python2-sphinx_rtd_theme
%endif
BuildRequires:  python2-cryptography
BuildRequires:  python2-mock
BuildRequires:  python2-requests
BuildRequires:  python2-pyrfc3339
BuildRequires:  python2-josepy >= 1.1.0
%endif

%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-cryptography
BuildRequires:  python3-pyOpenSSL >= 0.13.1
BuildRequires:  python3-requests
BuildRequires:  python3-requests-toolbelt
BuildRequires:  python3-pyrfc3339
BuildRequires:  python3-josepy >= 1.1.0
%endif

%if %{with python2}
%if 0%{?fedora} >= 28
# Fedora 28 added versioned names for this package
BuildRequires:  python2-pytz
%else
BuildRequires:  pytz
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
BuildRequires:  pytest
BuildRequires:  python-ndg_httpsclient
BuildRequires:  python-requests-toolbelt
BuildRequires:  pyOpenSSL >= 0.13.1
%else
BuildRequires:  python2-ndg_httpsclient
BuildRequires:  python2-pytest
BuildRequires:  python2-requests-toolbelt
BuildRequires:  python2-pyOpenSSL >= 0.13.1
%endif
%endif

%if %{with python3}
BuildRequires:  python3-ndg_httpsclient
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz
%endif

# Used to verify OpenPGP signature
BuildRequires:  gnupg2
%if 0%{?rhel} && 0%{?rhel} == 8
# "gpgverify" macro, not in COPR buildroot by default
BuildRequires:  epel-rpm-macros >= 8-5
%endif

BuildArch:      noarch

%description
Python libraries implementing the Automatic Certificate Management Environment
(ACME) protocol. It is used by the Let's Encrypt project.

%if %{with python2}
%package -n python2-acme
Requires: python2-cryptography
Requires: python2-pyasn1
Requires: python2-pyrfc3339
Requires: python2-requests
Requires: python2-six
Requires: python2-josepy >= 1.1.0

%if 0%{?fedora} >= 28
# Fedora 28 added versioned names for this package
Requires:       python2-pytz
%else
Requires:       pytz
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
Requires:       python-ndg_httpsclient
Requires:       python-requests-toolbelt
Requires:       pyOpenSSL >= 0.13.1
%else
Requires:       python2-ndg_httpsclient
Requires:       python2-requests-toolbelt
Requires:       python2-pyOpenSSL >= 0.13.1
%endif

%if %{with python3}
# Recommends not supported by rpm on EL7
#Recommends: python-acme-doc
%endif
Summary:        %{summary}
%{?python_provide:%python_provide python2-acme}


%description -n python2-acme
Python 2 library for use of the Automatic Certificate Management Environment
protocol as defined by the IETF. It's used by the Let's Encrypt project.
%endif

%if %{with python3}
%package -n python3-acme
Requires: python3-cryptography
Requires: python3-ndg_httpsclient
Requires: python3-pyasn1
Requires: python3-pyOpenSSL
Requires: python3-pyrfc3339
Requires: python3-pytz
Requires: python3-requests
Requires: python3-requests-toolbelt
Requires: python3-six
Requires: python3-josepy >= 1.1.0
#Recommends: python-acme-doc
Summary:        %{summary}
%{?python_provide:%python_provide python3-acme}

%description -n python3-acme
Python 3 library for use of the Automatic Certificate Management Environment
protocol as defined by the IETF. It's used by the Let's Encrypt project.
%endif

%if 0%{?fedora}
%package doc
Requires: fontawesome-fonts fontawesome-fonts-web
Summary:  Documentation for python-acme libraries

%description doc
Documentation for the ACME python libraries
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -n %{srcname}-%{version}
%if 0%{?rhel} && 0%{?rhel} == 7
%patch0 -p1
%endif
# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

# Doc generation is currently broken on EL7, see bz#1492884
%if 0%{?fedora}
# man page is pretty useless but api pages are decent
# Issue opened upstream for improving man page
# Need to cd as parent makefile tries to build libraries
(  cd docs && make html SPHINXBUILD=%{SPHINXBUILD} )
# Clean up stuff we don't need for docs
rm -rf docs/_build/html/{.buildinfo,man,_sources}
# Unbundle fonts already on system
# Lato ttf is in texlive but that adds a lot of dependencies (30+MB) for just a font in documentation
# and lato is not in it's own -fonts package, only texlive
rm -f docs/_build/html/_static/fonts/fontawesome*
ln -sf /usr/share/fonts/fontawesome/fontawesome-webfont.eot docs/_build/html/_static/fonts/fontawesome-webfont.eot
ln -sf /usr/share/fonts/fontawesome/fontawesome-webfont.svg docs/_build/html/_static/fonts/fontawesome-webfont.svg
ln -sf /usr/share/fonts/fontawesome/fontawesome-webfont.ttf docs/_build/html/_static/fonts/fontawesome-webfont.ttf
ln -sf /usr/share/fonts/fontawesome/fontawesome-webfont.woff docs/_build/html/_static/fonts/fontawesome-webfont.woff
%endif

%check
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python3}
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
%endif

%if %{with python2}
%files -n python2-acme
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}*.egg-info
%endif

%if %{with python3}
%files -n python3-acme
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}*.egg-info
%endif

%if 0%{?fedora}
%files doc
%license LICENSE.txt
%doc README.rst
%doc docs/_build/html
%endif

%changelog
* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843199)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9
- EPEL 8: disable failing test case (rhbz #1834530)

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831912)

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809794)

* Fri Feb 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (#1791073)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Felix Schwarz <fschwarz@fedoraproject.org> 1.1.0-1
- Update to 1.1.0

* Thu Dec 05 2019 Felix Schwarz <fschwarz@fedoraproject.org> 1.0.0-2
- adapt conditions for EPEL8
- remove runtime dependency on mock

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769084)

* Thu Nov 21 2019 Felix Schwarz <fschwarz@fedoraproject.org> 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757606)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748611)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742576)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Sun Jun 30 2019 Miro Hrončok <mhroncok@redhat.com> - 0.35.1-2
- Rebuilt to update automatic Python dependencies

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717675)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686201)

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673768)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669312)

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1625793)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600290)

* Thu Jul 12 2018 Eli Young <elyscape@gmail.com> - 0.26.0-1
- Update to 0.26.0 (#1600290)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591030)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588214)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574138)
- Remove unnecessary build dependencies and patches

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563878)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2 (#1558275)

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0 (#1552951)

* Thu Mar 08 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.21.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.1-3
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Eli Young <elyscape@gmail.com> - 0.21.1-1
- Update to 0.21.1 (#1535990)

* Wed Dec 20 2017 Eli Young <elyscape@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Fri Oct 06 2017 Eli Young <elyscape@gmail.com> - 0.19.0-1
- Update to 0.19.0 (bz#1499366)

* Fri Sep 22 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2

* Mon Sep 18 2017 Eli Young <elyscape@gmail.com> - 0.18.1-2
- Disable doc package entirely for EPEL7

* Mon Sep 18 2017 Eli Young <elyscape@gmail.com> - 0.18.1-1
- Disable doc generation for EPEL7

* Sun Sep 10 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Fri May 12 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.0-1
- Update to 0.14.0

* Wed Apr 19 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-1
- Update to 0.13.0

* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-3
- upstream request not to use py3 yet so switch jws to py2
- include a py3 option for testing

* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-2
- Build for python rpm macro change

* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-1
- Update to 0.12.0
- Change %%{_bindir}/jws to be python3 on Fedora

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-1
- Upgrade to 0.11.1

* Thu Jan 05 2017 Adam Williamson <awilliam@redhat.com> - 0.9.3-2
- Backport upstream fix for tests with OpenSSL 1.1
- Backport upstream removal of sphinxcontrib-programoutput usage
- Re-enable doc generation

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6
- Removing the docs subpackage for now until the dependency works in rawhide

* Fri Oct 14 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.3-1
- Upgrade to 0.9.3
* Thu Oct 13 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.2-1
- Upgrade to 0.9.2
* Fri Oct 07 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.1-1
- Upgrade to 0.9.1
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Wed Jun 15 2016 Nick Bebout <nb@fedoraproject.org> - 0.8.1-1
- Upgrade to 0.8.1
* Fri Jun 03 2016 James Hogarth <james.hogarth@gmail.com> - 0.8.0-1
- update to 0.8.0 release
* Mon May 30 2016 Nick Bebout <nb@fedoraproject.org> - 0.7.0-1
- Upgrade to 0.7.0
* Thu May 12 2016 Nick Bebout <nb@fedoraproject.org> - 0.6.0-1
- Upgrade to 0.6.0
* Wed Apr 06 2016 Nick Bebout <nb@fedoraproject.org> - 0.5.0-1
- Upgrade to 0.5.0
* Sat Mar 05 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-3
- Package does not require python-werkzeug anymore, upstream #2453
* Fri Mar 04 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-2
- Fix build on EL7 where no newer setuptools is available
* Fri Mar 04 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.4.2-1
- Upgrade to 0.4.2
* Tue Mar 1 2016 Nick Le Mouton <nick@noodles.net.nz> - 0.4.1-1
- Upgrade to 0.4.1
* Thu Feb 11 2016 Nick Bebout <nb@fedoraproject.org> - 0.4.0-1
- Upgrade to 0.4.0
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Nick Bebout <nb@fedoraproject.org> - 0.3.0-1
- Upgrade to 0.3.0
* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-1
- Upgrade to 0.2.0
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- Upgrade to 0.1.1
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-3
- Restore missing dependencies causing a FTBFS with py3 tests
- Add the man pages
* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.1.0-4
- Specify more of the EPEL dependencies
* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.1.0-3
- epel7: Only build python2 package
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Fix up the removal of the dev release snapshot
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Mon Nov 30 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3-dev20151123
- Update spec with comments from review
* Sat Nov 28 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec with comments from review
- Add python3 library
* Fri Nov 27 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-1.dev20151123
- initial packaging
