%global pypi_name pytapo

Name:           python-%{pypi_name}
Version:        0.11
Release:        1%{?dist}
Summary:        Python library for communication with Tapo Cameras

License:        MIT
URL:            https://github.com/JurajNyiri/pytapo
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python library for communication with Tapo Cameras.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python library for communication with Tapo Cameras.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.11-1
- License file is now part of the source
- Update to latest upstream release 0.11 (#1885060)

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- Initial package for Fedora