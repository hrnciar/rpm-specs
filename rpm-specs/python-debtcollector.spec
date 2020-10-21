
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name debtcollector
%global with_doc 1
%global common_desc \
It is a collection of functions/decorators which is used to signal a user when \
*  a method (static method, class method, or regular instance method) or a class \
    or function is going to be removed at some point in the future. \
* to move a instance method/property/class from an existing one to a new one \
* a keyword is renamed \
* further customizing the emitted messages

Name:        python-%{pypi_name}
Version:     2.0.1
Release:     2%{?dist}
Summary:     A collection of Python deprecation patterns and strategies

License:     ASL 2.0
URL:         https://pypi.python.org/pypi/%{pypi_name}
Source0:     https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz

BuildArch:   noarch

BuildRequires: git

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:     A collection of Python deprecation patterns and strategies
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires:    python3-funcsigs
Requires:    python3-pbr
Requires:    python3-six
Requires:    python3-wrapt

%description -n python3-%{pypi_name}
%{common_desc}


%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for the debtcollector module

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-fixtures
BuildRequires:  python3-six
BuildRequires:  python3-wrapt

%description -n python-%{pypi_name}-doc
Documentation for the debtcollector module
%endif


%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
rm -rf *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# doc
sphinx-build-3 -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-%{pypi_name}
%doc README.rst CONTRIBUTING.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 2.0.1-1
- Update to upstream version 2.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.22.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 1.22.0-2
- Update to upstream version 1.22.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.21.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.21.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 1.21.0-1
- Update to 1.21.0

