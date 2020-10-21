%global pypi_name productivity

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Python driver for AutomationDirect Productivity Series PLCs

License:        GPLv2
URL:            http://github.com/numat/productivity/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Python driver and command-line tool for AutomationDirect Productivity
Series PLCs.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python driver and command-line tool for AutomationDirect Productivity
Series PLCs.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# https://github.com/numat/productivity/pull/26
#%%license LICENSE
%{_bindir}/productivity
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Initial package for Fedora