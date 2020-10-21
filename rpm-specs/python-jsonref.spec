%global pypi_name jsonref

Name:           python-%{pypi_name}
Version:        0.2
Release:        1%{?dist}
Summary:        An implementation of JSON Reference for Python

License:        MIT
URL:            https://github.com/gazpachoking/jsonref
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-pytest

%description
jsonref is a library for automatic dereferencing of JSON Reference objects
for Python (supporting Python 2.6+ and Python 3.3+).

This library lets you use a data structure with JSON reference objects, as if
the references had been replaced with the referent data.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
jsonref is a library for automatic dereferencing of JSON Reference objects
for Python (supporting Python 2.6+ and Python 3.3+).

This library lets you use a data structure with JSON reference objects, as if
the references had been replaced with the referent data.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# DOS line ending
sed -i -e 's/\r$//' README.rst


%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest tests.py


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/proxytypes.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 08 2020 Aurelien Bompard <abompard@fedoraproject.org> - 0.2-1
- Initial package.
