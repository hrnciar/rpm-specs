%global pypi_name ciso8601

Name:           python-%{pypi_name}
Version:        2.1.3
Release:        2%{?dist}
Summary:        Fast ISO8601 date time parser

License:        MIT
URL:            https://github.com/closeio/ciso8601
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%description
ciso8601 converts ISO 8601 or RFC 3339 date time strings into Python
datetime objects. Since it's written as a C module, it is much faster
than other Python libraries.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
ciso8601 converts ISO 8601 or RFC 3339 date time strings into Python
datetime objects. Since it's written as a C module, it is much faster
than other Python libraries.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc CHANGELOG.md README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}.*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-2
- Enable debug output (rhbz#1875860)

* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Initial package for Fedora
