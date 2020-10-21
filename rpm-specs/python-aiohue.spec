%global pypi_name aiohue

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        3%{?dist}
Summary:        Python module to talk to Philips Hue

License:        ASL 2.0
URL:            https://github.com/home-assistant-libs/aiohue
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Asynchronous library to control Philips Hue.

%package -n     python3-%{pypi_name}
Summary:        %{summary}


BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Asynchronous library to control Philips Hue.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

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
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-2
- Use upstream tarball and add license file (rhbz#1849457)

* Sun Jun 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Initial package.
