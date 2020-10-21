%global pypi_name smbprotocol

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Interact with a server using the SMB 2/3 Protocol

License:        MIT
URL:            https://github.com/jborean93/smbprotocol
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
SMB is a network file sharing protocol and has numerous iterations
over the years. This library implements the SMBv2 and SMBv3 protocol
based on the MS-SMB2 document.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pyspnego)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
SMB is a network file sharing protocol and has numerous iterations
over the years. This library implements the SMBv2 and SMBv3 protocol
based on the MS-SMB2 document.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/smbclient/
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Initial package for Fedora
