%global pypi_name certbot-dns-nsone

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} >= 8)
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pypi_name}
Version:        1.5.0
Release:        1%{?dist}
Summary:        NS1 DNS Authenticator plugin for Certbot

License:        ASL 2.0
URL:            https://github.com/certbot/certbot
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
# Key mentioned in https://certbot.eff.org/docs/install.html#certbot-auto
# Keyring generation steps as follows:
#   gpg2 --keyserver pool.sks-keyservers.net --recv-key A2CFB51FA275A7286234E7B24D17C995CD9775F2
#   gpg2 --export --export-options export-minimal A2CFB51FA275A7286234E7B24D17C995CD9775F2 > gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg
Source2:        gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg

BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-acme >= 0.31.0
BuildRequires:  python2-certbot >= 1.1.0
BuildRequires:  python2-devel
BuildRequires:  python2-dns-lexicon >= 2.2.1
BuildRequires:  python2-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-zope-interface

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
BuildRequires:  pytest
%else
BuildRequires:  python2-pytest
%endif
%endif

%if %{with python3}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-acme >= 0.31.0
BuildRequires:  python3-certbot >= 1.1.0
BuildRequires:  python3-devel
BuildRequires:  python3-dns-lexicon >= 2.2.1
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-zope-interface
%endif

# Used to verify OpenPGP signature
BuildRequires:  gnupg2

%description
NS1 DNS Authenticator plugin for Certbot

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-acme >= 0.31.0
Requires:       python2-certbot >= 1.1.0
Requires:       python2-dns-lexicon >= 2.2.1
Requires:       python2-mock
Requires:       python2-setuptools
Requires:       python2-zope-interface

# Provide the name users expect as a certbot plugin
%if 0%{?rhel} && 0%{?rhel} <= 7
Provides:      %{pypi_name} = %{version}-%{release}
%endif

%description -n python2-%{pypi_name}
NS1 DNS Authenticator plugin for Certbot
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-acme >= 0.31.0
Requires:       python3-certbot >= 1.1.0
Requires:       python3-dns-lexicon >= 2.2.1
Requires:       python3-setuptools
Requires:       python3-zope-interface

# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:      %{pypi_name} = %{version}-%{release}
%endif

%description -n python3-%{pypi_name}
NS1 DNS Authenticator plugin for Certbot

%package -n python-%{pypi_name}-doc
Summary:        certbot-dns-nsone documentation
%description -n python-%{pypi_name}-doc
Documentation for certbot-dns-nsone
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif


%check
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python3}
%{__python3} setup.py test
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/certbot_dns_nsone
%{python2_sitelib}/certbot_dns_nsone-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/certbot_dns_nsone
%{python3_sitelib}/certbot_dns_nsone-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%endif

%changelog
* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843214)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831926)

* Sat Mar 21 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-3
- bump version to fix damaged package.cfg

* Thu Mar 05 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.3.0-2
- bump release to retry koji build

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809787)

* Fri Feb 28 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.0-1
- Update to 1.2.0 (#1791077)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769116)

* Wed Dec 04 2019 Eli Young <elyscape@gmail.com> - 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757587)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748622)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742589)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717688)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686195)

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673757)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669324)

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1627580)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600301)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591040)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588228)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574147)

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563908)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 0.21.1-4
- Actually fix the setuptools dep

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 0.21.1-3
- Simplify deps, add python2- prefix where available

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 0.21.1-2
- Add patch to remove no longer needed versioned dep in epel7

* Tue Feb 20 2018 Nick Bebout <nb@usi.edu> - 0.21.1-1
- Initial package.
