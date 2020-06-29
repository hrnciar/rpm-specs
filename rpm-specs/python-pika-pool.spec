%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name pika-pool
%global old_name  pika_pool
%global _description Pika connection pooling inspired by:\
\
    flask-pika\
    sqlalchemy.pool.Pool

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        20%{?dist}
Summary:        Connection pooling for the Pika Python AMQP Client Library

License:        BSD
URL:            https://github.com/bninja/pika-pool
Source0:        https://pypi.io/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        LICENSE
BuildArch:      noarch

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Connection pooling for the Pika Python AMQP Client Library
%{?python_provide:%python_provide python2-%{pypi_name}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Provides:       python-%{old_name} = %{version}-%{release}
Provides:       python2-%{old_name} = %{version}-%{release}
Obsoletes:      python-%{old_name} < 0.1.3-6
Obsoletes:      python2-%{old_name} < 0.1.3-6

Requires:       python2-pika >= 0.9
%description -n python2-%{pypi_name}
%{_description}
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        Connection pooling for the Pika Python AMQP Client Library
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3-%{old_name} = %{version}-%{release}
Obsoletes:      python3-%{old_name} < 0.1.3-6

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-pika >= 0.9
%description -n python3-%{pypi_name}
%{_description}

%endif

%description
%{_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# No license file in source, https://github.com/bninja/pika-pool/issues/7
cp %{SOURCE1} .

# Remove upper cap on pika version, https://github.com/bninja/pika-pool/issues/17
sed -i 's/pika >=0.9,<0.11/pika >=0.9/' setup.py

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if %{with python3}
%py3_install
%endif
%if %{with python2}
%py2_install
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/pika_pool.py*
%{python2_sitelib}/pika_pool-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pika_pool.py
%{python3_sitelib}/pika_pool-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Javier Peña <jpena@redhat.com> - 0.1.3-15
- Remove upper cap for pika version in setup.py

* Mon Feb 04 2019 Javier Peña <jpena@redhat.com> - 0.1.3-14
- Remove Python2 subpackage in Fedora 30+ (bz#1671981)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.3-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Javier Peña <jpena@redhat.com> - 0.1.3-6
- Renamed package to python-pika-pool

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 24 2016 Javier Peña <jpena@redhat.com> - 0.1.3-3
- Switch name to python-pika_pool

* Wed Feb 24 2016 Javier Peña <jpena@redhat.com> - 0.1.3-2
- Updated to enable py3 subpackage

* Wed Jan 20 2016 jpena <jpena@redhat.com> - 0.1.3-1
- Initial package.
