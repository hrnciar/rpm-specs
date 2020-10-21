%global pypi_name aioiotprov

Name:           python-%{pypi_name}
Version:        0.0.7
Release:        1%{?dist}
Summary:        Library/utility to help provision various IoT devices

License:        MIT
URL:            http://github.com/frawau/aioiotprov
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A library/utility to provision IoT devices. It can provision TP-Link
smartplugs, Broadlink IR blasters, Sonoff switches running the Tasmota
firmware, Shelly devices and E-Trix power monitors.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A library/utility to provision IoT devices. It can provision TP-Link
smartplugs, Broadlink IR blasters, Sonoff switches running the Tasmota
firmware, Shelly devices and E-Trix power monitors.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' {aioiotprov/plugins/*.py,aioiotprov/*.py}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/aioiotprov
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.7-1
- Initial package for Fedora