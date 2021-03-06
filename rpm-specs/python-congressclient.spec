%global pypi_name congressclient
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Client for OpenStack Congress (Open Policy Framework)

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        2%{?dist}
Summary:        Client for OpenStack Congress (Open Policy Framework)

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  git

%description
%{common_desc}

%package -n     python3-%{pypi_name}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-mock
BuildRequires:  python3-oslo-log
BuildRequires:  python3-cliff
BuildRequires:  python3-fixtures

Requires:       python3-babel >= 2.3.4
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-six >= 1.10.0
Requires:       python3-cliff >= 2.8.0

Summary:        Client for OpenStack Congress (Open Policy Framework)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
# Documentation package
%package -n python3-%{pypi_name}-doc
Summary:        Documentation for OpenStack Congress Client
%{?python_provide:%python_provide python3-%{pypi_name}-doc}

BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-apidoc
BuildRequires: python3-openstackdocstheme

%description -n python3-%{pypi_name}-doc
Documentation for the client library for interacting with Openstack
Congress API.
%endif

# Tests package
%package -n python3-%{pypi_name}-tests

Summary:  congressclient test subpackage

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       python3-fixtures >= 1.3.1
Requires:       python3-mock
Requires:       python3-testtools
Requires:       python3-subunit >= 0.0.18
Requires:       python3-testrepository >= 0.0.18
Requires:       python3-testscenarios >= 0.4
Requires:       python3-webob >= 1.2.3

%description -n python3-%{pypi_name}-tests
Test suite for OpenStack Congress (Open Policy Framework) client.

%prep
%autosetup -n %{name}-%{upstream_version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -rf *requirements.txt


%build
%{py3_build}

%install
%{py3_install}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/python_%{pypi_name}-*-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files -n python3-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/%{pypi_name}/tests

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 2.0.1-1
- Update to upstream version 2.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.13.0-1
- Update to upstream version 1.13.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 RDO <dev@lists.rdoproject.org> 1.12.0-1
- Update to 1.12.0
- Add fixtures as BuildRequries

