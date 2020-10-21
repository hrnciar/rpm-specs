%global pypi_name soco

Name:           python-%{pypi_name}
Version:        0.19
Release:        1%{?dist}
Summary:        Python library to control Sonos speakers

License:        MIT
URL:            https://github.com/SoCo/SoCo
Source0:        %{pypi_source}
BuildArch:      noarch

%description
SoCo (Sonos Controller) is a Python project that allows you to programmatically
control Sonos speakers.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(graphviz)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(xmltodict)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
SoCo (Sonos Controller) is a Python project that allows you to programmatically
control Sonos speakers.

%package -n python-%{pypi_name}-doc
Summary:        soco documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
rm -rf examples/webapp/.gitignore
sed -i -e '/^#!\//, 1d' {examples/plugins/socoplugins.py,examples/commandline/tunein.py}
chmod -x {examples/plugins/socoplugins.py,examples/commandline/tunein.py}

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc examples/ README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.rst

%changelog
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.19-1
- Initial package for Fedora