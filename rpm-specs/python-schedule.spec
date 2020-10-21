%global pypi_name schedule

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        2%{?dist}
Summary:        Job scheduling for humans

License:        MIT
URL:            https://github.com/dbader/schedule
Source0:        %{pypi_source}
BuildArch:      noarch

%description
An in-process scheduler for periodic jobs that uses the builder pattern for
configuration. Schedule lets you run Python functions (or any other callable)
periodically at pre-determined intervals using a simple, human-friendly syntax.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(mock)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
An in-process scheduler for periodic jobs that uses the builder pattern for
configuration. Schedule lets you run Python functions (or any other callable)
periodically at pre-determined intervals using a simple, human-friendly syntax.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc HISTORY.rst README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-2
- Add HISTORY.rst to docs (rhbz#1875744)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Initial package for Fedora
