%global pypi_name pyblackbird
%global pkg_name blackbird

Name:           python-%{pkg_name}
Version:        0.5
Release:        1%{?dist}
Summary:        Python API for talking to Monoprice Blackbird devices

License:        MIT
URL:            https://github.com/koolsb/pyblackbird
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python interface implementation for Monoprice Blackbird 4k 8x8
HDBaseT Matrix.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(pyserial-asyncio)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python interface implementation for Monoprice Blackbird 4k 8x8
HDBaseT Matrix.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# https://github.com/koolsb/pyblackbird/issues/6
%pytest -v tests -k "not TestAsyncBlackbird"

%files -n python3-%{pkg_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5-1
- Initial package for Fedora