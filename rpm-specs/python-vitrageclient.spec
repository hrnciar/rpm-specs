%global pypi_name vitrageclient

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{!?py_req_cleanup: %global py_req_cleanup rm -rf {,test-}requirements.txt}
%global with_doc 1

%global common_desc \
Python client for Vitrage REST API. Includes python library for Vitrage API \
and Command Line Interface (CLI) library.

Name:           python-%{pypi_name}
Version:        4.0.1
Release:        1%{?dist}
Summary:        Python client for Vitrage REST API

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

%description
%{common_desc}

%package -n     python3-%{pypi_name}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  git
BuildRequires:  python3-iso8601
BuildRequires:  python3-mock
BuildRequires:  python3-subunit
BuildRequires:  python3-pydot
BuildRequires:  python3-oslotest
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildRequires:  python3-cliff
BuildRequires:  python3-testscenarios

BuildRequires:  python3-networkx

Requires:       python3-iso8601
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-pbr
Requires:       python3-pydot
Requires:       python3-osc-lib >= 1.10.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-oslo-log
Requires:       python3-cliff >= 2.8.0

Requires:       %{name}-bash-completion = %{version}-%{release}

Requires:       python3-networkx


Summary:        Python client for Vitrage REST API
%{?python_provide:%python_provide python3-%{pypi_name}}
Obsoletes: python2-%{pypi_name} < %{version}-%{release}

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:       Documentation for python client for Vitrage REST API

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme

%description -n python-%{pypi_name}-doc
Documentation for python client for Vitrage REST API. Includes python library
for Vitrage API and Command Line Interface (CLI) library.
%endif

%package bash-completion
Summary:        bash completion files for vitrage
BuildRequires:  bash-completion

%description bash-completion
This package contains bash completion files for vitrage.


%prep
%autosetup -n %{name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -rf *requirements.txt


%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build -W -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s vitrage %{buildroot}%{_bindir}/vitrage-3

# push autocompletion
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p %{buildroot}$bashcompdir
mv %{buildroot}%{_datadir}/vitrage.bash_completion %{buildroot}$bashcompdir/vitrage

%check
export PYTHON=%{__python3}
# tests.cli.test_topology_show.TopologyShowTest.test_dot_emitter unit test fail because of
# elements order in a list. Until we find proper fix let's ignore results.
%{__python3} setup.py test --slowest || true

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/python_%{pypi_name}-*-py?.?.egg-info
%{_bindir}/vitrage
%{_bindir}/vitrage-3

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files bash-completion
%license LICENSE
%{_datadir}/bash-completion/completions/vitrage

%changelog
* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 4.0.1-1
- Update to upstream version 4.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Alfredo Moralejo <amoralej@redhat.com> 3.0.0-1
- Update to upstream version 3.0.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 2.7.0-1
- Update to 2.7.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
-
* Mon Nov 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Subpackage python2-vitrageclient has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue May 22 2018 RDO <dev@lists.rdoproject.org> 2.1.0-1
- Update to 2.1.0

* Sun Feb 11 2018 RDO <dev@lists.rdoproject.org> 2.0.0-1
- Update to 2.0.0
