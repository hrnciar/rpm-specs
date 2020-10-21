%global pypi_name vsure

Name:           python-%{pypi_name}
Version:        1.6.0
Release:        1%{?dist}
Summary:        Read and change status of verisure devices

License:        MIT
URL:            http://github.com/persandstrom/python-verisure
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python module for reading and changing status of verisure devices
through mypages.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python module for reading and changing status of verisure devices
through mypages.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/persandstrom/python-verisure/pull/122
#%%license LICENSE
%{_bindir}/vsure
%{python3_sitelib}/verisure/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.0-1
- Initial package for Fedora
