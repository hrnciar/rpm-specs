%global pypi_name omnilogic

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        1%{?dist}
Summary:        Integration for the Hayward OmniLogic pool control system

License:        ASL 2.0
URL:            https://github.com/djtimca/omnilogic-api
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Integration library for Hayward Omnilogic pool controllers to allow easy
integration through their API to your home automation system.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Integration library for Hayward Omnilogic pool controllers to allow easy
integration through their API to your home automation system.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/djtimca/omnilogic-api/pull/8
#%%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Update to latest upstream release 0.4.2

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora