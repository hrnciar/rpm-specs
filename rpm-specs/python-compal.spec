%global pypi_name compal

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Compal CH7465LG/Ziggo Connect Box client

License:        MIT
URL:            https://github.com/ties/compal_CH7465LG_py
Source0:        %{pypi_source}
BuildArch:      noarch

%description
API wrapper for the web interface of the Ziggo Connect Box (i.e. the Compal
CH7465LG).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
API wrapper for the web interface of the Ziggo Connect Box (i.e. the Compal
CH7465LG).

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests/

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora
