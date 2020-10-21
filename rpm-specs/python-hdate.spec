%global pypi_name hdate

Name:           python-%{pypi_name}
Version:        0.9.11
Release:        1%{?dist}
Summary:        Hebrew date and Zmanim

License:        GPLv3+
URL:            https://github.com/py-libhdate/py-libhdate
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Jewish/Hebrew date and Zmanim in native Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pytz)
%description -n python3-%{pypi_name}
Jewish/Hebrew date and Zmanim in native Python.

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
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.11-1
- Initial package for Fedora
