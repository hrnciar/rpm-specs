%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname ironicclient

%global common_desc A python and command line client library for Ironic

Name:           python-ironicclient
Version:        4.1.0
Release:        1%{?dist}
Summary:        Python client for Ironic

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-%{sname}
Source0:        https://tarballs.openstack.org/python-%{sname}/python-%{sname}-%{version}%{?milestone}.tar.gz
BuildArch:      noarch


%description
%{common_desc}


%package -n python3-%{sname}
Summary:        Python client for Ironic
%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools

Requires:       genisoimage
Requires:       python3-appdirs >= 1.3.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-osc-lib >= 1.10.0
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-requests
Requires:       python3-cliff >= 2.8.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-openstacksdk >= 0.18.0
Requires:       python3-dogpile-cache >= 0.6.2
Requires:       python3-jsonschema
Requires:       python3-PyYAML

%description -n python3-%{sname}
%{common_desc}

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/baremetal
%{python3_sitelib}/%{sname}*
%{python3_sitelib}/python_%{sname}*

%changelog
* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 4.1.0-1
- Update to upstream version 4.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Alfredo Moralejo <amoralej@redhat.com> 3.1.0-1
- Update to upstream version 3.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 2.7.0-1
- Update to 2.7.0

