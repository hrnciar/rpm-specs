%global pypi_name serpent

Name:           python-%{pypi_name}
Version:        1.30.2
Release:        1%{?dist}
Summary:        Serialization based on ast.literal_eval

License:        MIT
URL:            https://github.com/irmen/Serpent
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Serpent is a simple serialization library based on ast.literal_eval. Because
it only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network
for instance) and de-serialize it there.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-attrs
BuildRequires:  python3-pytz
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Serpent is a simple serialization library based on ast.literal_eval. Because
it only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network
for instance) and de-serialize it there.
%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jul 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.30.2-1
- Initial package for Fedora
