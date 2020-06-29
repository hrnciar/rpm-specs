%global pypi_name ldeep

Name:           %{pypi_name}
Version:        1.0.8
Release:        1%{?dist}
Summary:        LDAP enumeration utility

License:        MIT
URL:            https://github.com/franc-pentest/ldeep
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Tool to interact and enumerate LDAP instances.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Tool to interact and enumerate LDAP instances.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.8-1
- Initial package for Fedora

