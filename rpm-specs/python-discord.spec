%global pypi_name discord.py
%global pkg_name discord

Name:           python-%{pkg_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Python wrapper for the Discord API

License:        MIT
URL:            https://github.com/Rapptz/discord.py
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A modern, easy to use, feature-rich, and async ready API wrapper for
Discord written in Python.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
A modern, easy to use, feature-rich, and async ready API wrapper for
Discord written in Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pkg_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Oct 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-1
- Update to latest upstream release 1.5.1 (#1889553)

* Sat Oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update to latest upstream release 1.5.0 (#1887054)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Initial package for Fedora
