%global pypi_name socialscan
%bcond_with network

Name:           %{pypi_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        CLI and library for usage checking of user names and email addresses

License:        MPLv2.0
URL:            https://github.com/iojw/socialscan
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with network}
BuildRequires:  python3-pytest
BuildRequires:  python3-aiohttp
%endif

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
socialscan offers accurate and fast checks for email address and user name
usage on online platforms. Given an email address or user name, socialscan
returns whether it is available, taken or invalid on online platforms.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
socialscan offers accurate and fast checks for email address and user name
usage on online platforms. Given an email address or user name, socialscan
returns whether it is available, taken or invalid on online platforms.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with network}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests \
  -k "not Instagram"
%endif

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Update to latest upstream release 1.3.0 (#1882611)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.6-1
- Initial package
