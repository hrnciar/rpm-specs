%global sname oslo.config
%global pypi_name oslo-config
%global with_doc 1
%global repo_bootstrap 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:       python-oslo-config
Epoch:      2
Version:    8.0.2
Release:    2%{?dist}
Summary:    OpenStack common configuration library

Group:      Development/Languages
License:    ASL 2.0
URL:        https://launchpad.net/%{sname}
Source0:    https://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz

Patch0001: 0001-add-usr-share-project-dist.conf-to-the-default-confi.patch

BuildArch:  noarch

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%package -n python3-%{pypi_name}
Summary:    OpenStack common configuration library
%{?python_provide:%python_provide python3-%{pypi_name}}
Obsoletes: python2-%{pypi_name} < %{version}-%{release}

Requires:   python3-oslo-i18n >= 3.15.3
Requires:   python3-rfc3986 >= 1.2.0
Requires:   python3-pbr
Requires:   python3-requests >= 2.18.0
Requires:   python3-stevedore >= 1.20.0
Requires:   python3-debtcollector >= 1.2.0
Requires:   python3-netaddr >= 0.7.18
Requires:   python3-PyYAML >= 3.10

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-oslo-i18n
BuildRequires: python3-rfc3986
BuildRequires: python3-pbr
BuildRequires: git
# Required for tests
BuildRequires: python3-testscenarios
BuildRequires: python3-stestr
BuildRequires: python3-testtools
BuildRequires: python3-oslotest
BuildRequires: python3-requests-mock
BuildRequires: python3-netaddr
BuildRequires: python3-stevedore
BuildRequires: python3-PyYAML

%if 0%{?repo_bootstrap} == 0
BuildRequires: python3-oslo-log
%endif

%description -n python3-%{pypi_name}
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:    Documentation for OpenStack common configuration library

BuildRequires: python3-sphinx
BuildRequires: python3-fixtures
BuildRequires: python3-openstackdocstheme
BuildRequires: python3-oslotest >= 1.10.0
BuildRequires: python3-debtcollector
BuildRequires: python3-stevedore
BuildRequires: python3-sphinxcontrib-apidoc

%description -n python-%{pypi_name}-doc
Documentation for the oslo-config library.
%endif

%prep
%autosetup -n %{sname}-%{upstream_version} -S git
# Remove shebang from non executable file, it's used by the oslo-config-validator binary.
sed -i '/\/usr\/bin\/env/d' oslo_config/validator.py
# let RPM handle deps
rm -rf {test-,}requirements.txt

# Remove tests requiring sphinx if sphinx is not available
%if 0%{?with_doc} == 0
rm oslo_config/tests/test_sphinxext.py
rm oslo_config/tests/test_sphinxconfiggen.py
%endif

%build
%{py3_build}

%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}
pushd %{buildroot}/%{_bindir}
for i in generator validator
do
ln -s oslo-config-$i oslo-config-$i-3
done
popd

%check
%if 0%{?repo_bootstrap} == 0
PYTHON=python3 stestr-3 run
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/oslo-config-generator
%{_bindir}/oslo-config-generator-3
%{_bindir}/oslo-config-validator
%{_bindir}/oslo-config-validator-3
%{python3_sitelib}/oslo_config
%{python3_sitelib}/*.egg-info

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 2:8.0.2-1
- Update to upstream version 8.0.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2:6.11.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:6.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 2:6.11.1-2
- Update to upstream version 6.11.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2:6.8.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2:6.8.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:6.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Miro Hrončok <mhroncok@redhat.com> - 2:6.8.1-2
- Rename the documentation package back to python-oslo-config-doc

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 2:6.8.1-1
- Update to 6.8.1

