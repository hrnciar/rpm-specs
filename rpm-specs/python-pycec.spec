%global pypi_name pyCEC
%global mod_name pycec

Name:           python-%{mod_name}
Version:        0.4.14
Release:        1%{?dist}
Summary:        Provide HDMI CEC devices as objects

License:        MIT
URL:            https://github.com/konikvranik/pycec/
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  libcec-devel

%description
TCP <=> HDMI bridge to control HDMI devices over TCP network.

%package -n     python3-%{mod_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{mod_name}}

%description -n python3-%{mod_name}
TCP <=> HDMI bridge to control HDMI devices over TCP network.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{mod_name}
%license LICENSE
%doc README.rst
%{_bindir}/pycec
%{python3_sitelib}/pycec/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Oct 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.14-1
- Initial package for Fedora