# Created by pyp2rpm-3.3.2
%global pypi_name py3nvml

Name:           python-%{pypi_name}
Version:        0.2.6
Release:        2%{?dist}
Summary:        Python 3 Bindings for the NVIDIA Management Library

License:        BSD
URL:            https://github.com/fbcotter/py3nvml
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description \
Python 3 compatible bindings to the NVIDIA Management Library. Can be used to \
query the state of the GPUs on your system.

%description %{_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(xmltodict)
%description -n python3-%{pypi_name} %{_description}


%package -n     python3-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description -n python3-%{pypi_name}-doc %{_description}

This package contains the documentation for %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/py3smi
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitelib}/%{pypi_name}/

%files -n python3-%{pypi_name}-doc
%doc html
%license LICENSE


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-2
- Rebuilt for Python 3.9

* Tue Apr 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.6-1
- Update to 0.2.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.5-1
- Update to 0.2.5

* Fri Oct 11 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.4-1
- Update to 0.2.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.3-2
- Added docs and spec file fixes.

* Wed Mar 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.3-1
- Initial package.
