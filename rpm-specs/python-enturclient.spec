%global pypi_name enturclient

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        2%{?dist}
Summary:        Python API client for data from Entur.org

License:        MIT
URL:            https://github.com/hfurubotten/enturclient
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Python client for fetching estimated departures from stop places in
Norway from Entur.org's API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python client for fetching estimated departures from stop places in
Norway from Entur.org's API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# https://github.com/hfurubotten/enturclient/issues/13
#%%check
#%%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-2
- Prepare for running tests (#1882903)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Initial package for Fedora