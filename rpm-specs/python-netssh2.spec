%global pypi_name netssh2

Name:		python-%{pypi_name}
Version:	0.1.7
Release:	9%{?dist}
Summary:	Library for communicating with network devices using ssh2-python

License:	GPLv3
URL:		https://gitlab.com/jkrysl/netssh2
Source0:	https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

%?python_enable_dependency_generator

BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(ssh2-python)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	python3dist(future)
BuildRequires:	python3dist(pytest-cov)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(tox)
BuildRequires:	python3dist(flake8)
BuildRequires:	python3dist(wheel)
BuildRequires:	python3dist(sphinx-autodoc-typehints)

%description
Library for communicating with network devices using ssh2-python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(ssh2-python)
%description -n python3-%{pypi_name}
Library for communicating with network devices using ssh2-python.

%package -n python-%{pypi_name}-doc
Summary:        netssh2 documentation
%description -n python-%{pypi_name}-doc
Documentation for netssh2

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

for lib in $(find . -type f -name "*.py"); do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%py3_build

#PYTHONPATH=${PWD} sphinx-build-3 docs html
#rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

#%check
#export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
#pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/docs
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/tests
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
#%doc html
%license LICENSE

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.7-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.1.7-3
- Rebuild

* Tue Jun 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.1.7-2
- Fix dependencie typo

* Wed Jun 05 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.1.7-1
- Initial package.
