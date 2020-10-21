%global pypi_name pyShelly
%global pkg_name shelly

Name:           python-%{pkg_name}
Version:        0.2.6
Release:        1%{?dist}
Summary:        Library for Shelly smart home devices

License:        MIT
URL:            https://github.com/StyraHem/pyShelly
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pyShellyLibrary for Shelly smart home devices. Using CoAP for auto discovery
and status updates.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
pyShellyLibrary for Shelly smart home devices. Using CoAP for auto discovery
and status updates.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# https://github.com/StyraHem/pyShelly/pull/39
sed -i 's/\r$//' README.md
chmod -x README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README.md
# https://github.com/StyraHem/pyShelly/pull/38
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.6-1
- Initial package for Fedora
