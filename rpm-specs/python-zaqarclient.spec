%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname zaqarclient

%global common_desc \
Python client to Zaqar messaging service API v1

Name:           python-zaqarclient
Version:        1.13.1
Release:        1%{?dist}
Summary:        Client Library for OpenStack Zaqar Queueing API

License:        ASL 2.0
URL:            http://wiki.openstack.org/zaqar
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
BuildArch:      noarch


%description
%{common_desc}

%package -n python3-%{sname}
Summary:        Client Library for OpenStack Zaqar Queueing API
%{?python_provide:%python_provide python3-%{sname}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pbr
Requires:       python3-requests >= 2.14.2
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-jsonschema

%description -n python3-%{sname}
%{common_desc}

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{py3_build}

%install
%{py3_install}


%files -n python3-%{sname}
%doc README.rst ChangeLog examples
%license LICENSE
%{python3_sitelib}/zaqarclient
%{python3_sitelib}/python_zaqarclient-*-py%{python3_version}.egg-info

%changelog
* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 1.13.1-1
- Update to upstream version 1.13.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.12.0-1
- Update to upstream version 1.12.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 RDO <dev@lists.rdoproject.org> 1.11.0-1
- Update to 1.11.0

