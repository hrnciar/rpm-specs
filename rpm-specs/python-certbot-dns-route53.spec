%global pypi_name certbot-dns-route53

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
Version:        1.9.0
Release:        1%{?dist}
Summary:        Route53 DNS Authenticator plugin for Certbot

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/certbot-dns-route53
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
# Key mentioned in https://certbot.eff.org/docs/install.html#certbot-auto
# Keyring generation steps as follows:
#   gpg2 --keyserver pool.sks-keyservers.net --recv-key A2CFB51FA275A7286234E7B24D17C995CD9775F2
#   gpg2 --export --export-options export-minimal A2CFB51FA275A7286234E7B24D17C995CD9775F2 > gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg
Source2:        gpg-A2CFB51FA275A7286234E7B24D17C995CD9775F2.gpg

BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-acme >= 0.29.0
# python-certbot-dns-route53 contains "from botocore.exceptions import …" but
# does not declare this in setup.py
BuildRequires:  python-botocore
BuildRequires:  python2-certbot >= 1.1.0
BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-zope-interface

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has unversioned names for these packages
BuildRequires:  pytest
BuildRequires:  python-boto3
%else
BuildRequires:  python2-boto3
BuildRequires:  python2-pytest
%endif
%endif

%if %{with python3}
BuildRequires:  python3-acme >= 0.29.0
BuildRequires:  python3-boto3
# python-certbot-dns-route53 contains "from botocore.exceptions import …" but
# does not declare this in setup.py
BuildRequires:  python3-botocore
BuildRequires:  python3-certbot >= 1.1.0
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-zope-interface
%endif

# Used to verify OpenPGP signature
BuildRequires:  gnupg2

%description
This certbot plugin automates the process of completing an ACME
dns-01 challenge by creating, and subsequently removing, TXT
records using AWS Route53.

%if %{with python2}
%package -n python2-%{pypi_name}
# Provide the name users expect as a certbot plugin
%if 0%{?rhel} && 0%{?rhel} <= 7
Provides:       %{pypi_name} = %{version}-%{release}
%endif
# Although a plugin for the certbot command it's technically
# an extension to the certbot python libraries
Requires:       python2-acme >= 0.29.0
Requires:       python2-certbot >= 1.1.0
Requires:       python2-mock
# python-certbot-dns-route53 contains "from botocore.exceptions import …" but
# does not declare this in setup.py
Requires:       python2-botocore
Requires:       python2-zope-interface

%if 0%{?rhel} && 0%{?rhel} <= 7
# EL7 has an unversioned name for this package
Requires:       python-boto3
%else
Requires:       python2-boto3
%endif

%if 0%{?fedora}
#Recommend the CLI as that will be the interface most use
Recommends:     certbot >= 0.39.0
%else
Requires:       certbot >= 0.39.0
%endif
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This certbot plugin automates the process of completing an ACME
dns-01 challenge by creating, and subsequently removing, TXT
records using AWS Route53.

This is the Python 2 version of the package.
%endif

%if %{with python3}
%package -n python3-%{pypi_name}
# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:       %{pypi_name} = %{version}-%{release}
%endif
# Although a plugin for the certbot command it's technically
# an extension to the certbot python libraries
Requires:       python3-acme >= 0.29.0
Requires:       python3-boto3
# python-certbot-dns-route53 contains "from botocore.exceptions import …" but
# does not declare this in setup.py
Requires:       python3-botocore
Requires:       python3-certbot >= 1.1.0
Requires:       python3-zope-interface

%if 0%{?fedora}
#Recommend the CLI as that will be the interface most use
Recommends:     certbot >= 0.39.0
%else
Requires:       certbot >= 0.39.0
%endif
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This certbot plugin automates the process of completing an ACME
dns-01 challenge by creating, and subsequently removing, TXT
records using AWS Route53.

This is the Python 3 version of the package.
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%check
%if %{with python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test
%endif

%if %{with python3}
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version}
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python2_sitelib}/certbot_dns_route53
%{python2_sitelib}/certbot_dns_route53-%{version}*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/certbot_dns_route53
%{python3_sitelib}/certbot_dns_route53-%{version}*.egg-info
%endif

%changelog
* Thu Oct 08 2020 Nick Bebout <nb@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Tue Oct 06 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Aug 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#1866093)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1854586)

* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843216)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.9

* Tue May 12 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-2
- run tests with pytest to fix tests on EPEL 7 (workaround for rhbz #1834529)

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831928)

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809786)

* Sat Feb 29 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.0-1
- Update to 1.2.0 (#1791076)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769119)

* Wed Dec 04 2019 Eli Young <elyscape@gmail.com> - 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757589)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748626)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742592)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717691)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686198)

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673760)

* Thu Jan 31 2019 Eli Young <elyscape@gmail.com> - 0.30.2-2
- Fix boto3 dependency

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669327)

* Thu Dec 27 2018 Eli Young <elyscape@gmail.com> - 0.29.1-2
- Fix dependency issues in EPEL7

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1627583)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600303)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591042)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588230)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574149)

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563910)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 0.21.1-2
- Simplify deps, add python2- prefix where available

* Wed Feb 14 2018 Eli Young <elyscape@gmail.com> - 0.21.1-1
- Initial package (#1544562)
