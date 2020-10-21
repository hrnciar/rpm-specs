%global pypi_name reparser

Name:           python-%{pypi_name}
Version:        1.4.3
Release:        1%{?dist}
Summary:        Simple regex-based lexer/parser for inline markup

License:        MIT
URL:            https://github.com/xmikos/reparser
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Simple regex-based Python lexer/parser for inline markup.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Simple regex-based Python lexer/parser for inline markup.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/ReParser-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Sep 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.3-1
- Initial package for Fedora