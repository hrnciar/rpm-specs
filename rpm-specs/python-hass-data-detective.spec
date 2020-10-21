%global pypi_name HASS-data-detective
%global pkg_name hass-data-detective

Name:           python-%{pkg_name}
Version:        2.3
Release:        4%{?dist}
Summary:        Tools for studying Home Assistant data

License:        MIT
URL:            https://github.com/robmarkcole/HASS-data-detective
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides a set of convenience functions and classes to analyze the
data in your Home Assistant database.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pandas
BuildRequires:  python3-pytz
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-setuptools
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
This package provides a set of convenience functions and classes to analyze the
data in your Home Assistant database.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e 's/2.1/2.3/g' setup.py

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests \
  -k "not test_load_hass_config"

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/detective/
%{python3_sitelib}/HASS_data_detective-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Aug 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-4
- Fix FTBFS (rhbz#1865291)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-1
- Update to new upstream release 2.3

* Tue Jun 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1-1
- Initial package for Fedora
