%global pypi_name sshtunnel

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        2%{?dist}
Summary:        Pure python SSH tunnels

License:        MIT
URL:            https://github.com/pahaz/sshtunnel
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(check-manifest)
BuildRequires:  python3dist(paramiko) >= 1.15.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tox) >= 1.8.1

%description
Pure python SSH tunnels

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(paramiko) >= 1.15.2
Requires:       python3dist(setuptools)
Requires:       python3dist(tox) >= 1.8.1

%description -n python3-%{pypi_name}
Pure python SSH tunnels


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/sshtunnel
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.1.5-1
- Initial package.
