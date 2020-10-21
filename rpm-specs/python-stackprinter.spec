%global pypi_name stackprinter

Name:           python-%{pypi_name}
Version:        0.2.4
Release:        1%{?dist}
Summary:        Debug-friendly stack traces

License:        MIT
URL:            https://github.com/cknd/stackprinter
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a more helpful version of Python's built-in exception message: It shows
more code context and the current values of nearby variables.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a more helpful version of Python's built-in exception message: It shows
more code context and the current values of nearby variables.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.4-1
- Initial package for Fedora