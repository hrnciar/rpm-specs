%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name taskflow

%global with_doc 1

%global common_desc \
A library to do [jobs, tasks, flows] in a HA manner using \
different backends to be used with OpenStack projects.

Name:           python-%{pypi_name}
Version:        4.1.0
Release:        2%{?dist}
Summary:        Taskflow structured state management library

License:        ASL 2.0
URL:            https://launchpad.net/taskflow
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}


%package -n python3-%{pypi_name}
Summary:        Taskflow structured state management library
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  git
BuildRequires:  python3-babel

Requires:       python3-cachetools >= 2.0.0
Requires:       python3-jsonschema
Requires:       python3-six
Requires:       python3-stevedore
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-automaton >= 1.9.0
Requires:       python3-futurist >= 1.2.0
Requires:       python3-fasteners >= 0.7.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-tenacity >= 4.4.0
Requires:       python3-pydot >= 1.2.4
Requires:       python3-networkx >= 2.1.0

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:          Documentation for Taskflow
BuildRequires:  python3-alembic
BuildRequires:  python3-cachetools
BuildRequires:  python3-jsonschema
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinx
BuildRequires:  graphviz
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-stevedore
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-futurist
BuildRequires:  python3-fasteners
BuildRequires:  python3-automaton
BuildRequires:  python3-kombu
BuildRequires:  python3-tenacity

BuildRequires:  python3-redis
BuildRequires:  python3-kazoo
BuildRequires:  python3-networkx
BuildRequires:  python3-sqlalchemy-utils

%description doc
%{common_desc}

This package contains the associated documentation.
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# TODO(apevec) remove once python-networking subpackaging is fixed
sed -i /networkx.drawing/d taskflow/types/graph.py

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf *requirements.txt


%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Mon Jun 15 2020 Eric Harney <eharney@redhat.com> - 4.1.0-2
- Remove dependency on python3-networkx-core

* Thu Jun 04 2020 Joel Capitao <jcapitao@redhat.com> 4.1.0-1
- Update to upstream version 4.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-4
- Rebuilt for Python 3.9

* Thu Feb 13 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.7.1-3
- Upgrade networkx dependency (it no longer provides networkx-core)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Alfredo Moralejo <amoralej@redhat.com> 3.7.1-1
- Update to upstream version 3.7.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Eric Harney <eharney@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Tue Mar 12 2019 Eric Harney - 3.4.0-1
- Update to 3.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Eric Harney - 2.6.0-8
- Remove Python 2 package for Fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-2
- Rebuild for Python 3.6

* Mon Sep 12 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.6.0-1
- Update to 2.6.0

