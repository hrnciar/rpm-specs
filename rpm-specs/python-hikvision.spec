%global pypi_name hikvision

Name:           python-%{pypi_name}
Version:        2.0.3
Release:        1%{?dist}
Summary:        Python interface to interact with a Hikvision camera

License:        MIT
URL:            https://github.com/fbradyirl/hikvision
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This is a Python module providing a basic Python interface to interact
with a Hikvision IP Camera.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a Python module providing a basic Python interface to interact
with a Hikvision IP Camera.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-1
- Add docs and license (rhbz#1875808)
- UPdate to latest upstream release 2.0.3

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-1
- Initial package for Fedora
