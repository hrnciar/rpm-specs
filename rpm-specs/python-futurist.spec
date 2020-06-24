
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name futurist

%global common_desc \
Code from the future, delivered to you in the now.

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        1%{?dist}
Summary:        Useful additions to futures, from the future

License:        ASL 2.0
URL:            http://docs.openstack.org/developer/futurist
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%package -n python3-%{pypi_name}
Summary:        Useful additions to futures, from the future
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  git
BuildRequires:  python3-prettytable
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-contextlib2

Requires:       python3-six >= 1.10.0
Requires:       python3-prettytable

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Useful additions to futures, from the future - documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-%{pypi_name}-doc
%{common_desc}
%endif

%description
========
Futurist
========

%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -W -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py?.?.egg-info

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 2.1.1-1
- Update to upstream version 2.1.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.9.0-2
- Update to upstream version 1.9.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 1.8.1-1
- Update to 1.8.1
