%global pypi_name habitipy

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Python library for Habitica RESTful API

License:        MIT
URL:            https://github.com/ASMfreaK/habitipy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python wrapper for the RESTful Habitica API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(plumbum)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(responses)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python wrapper for the RESTful Habitica API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
# Ignore the L10n parts (wrong location)
rm -rf %{buildroot}%{python3_sitelib}/%{pypi_name}/i18n

%check
%pytest -v tests -k "not test_data"

%files -n python3-%{pypi_name}
%doc CHANGES.txt CONTRIBUTORS.md README.md
%{_bindir}/habitipy
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora