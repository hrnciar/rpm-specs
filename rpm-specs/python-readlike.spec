%global pypi_name readlike

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        1%{?dist}
Summary:        Readline-like line editing module

License:        MIT
URL:            https://github.com/jangler/readlike
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A Python module that provides GNU Readline-like line editing functions (the
default Emacs-style ones).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python module that provides GNU Readline-like line editing functions (the
default Emacs-style ones).

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
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Sep 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- Initial package for Fedora