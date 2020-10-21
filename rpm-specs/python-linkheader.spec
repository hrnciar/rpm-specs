%global pypi_name linkheader

Name:           python-%{pypi_name}
Version:        0.4.3
Release:        2%{?dist}
Summary:        Parse and format link headers according to RFC 5988

License:        BSD
URL:            https://github.com/asplake/link_header
Source0:        %{pypi_source LinkHeader}
BuildArch:      noarch

%description
Parse and format link headers according to RFC 5988 "Web Linking".

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Parse and format link headers according to RFC 5988 "Web Linking".

%prep
%autosetup -n LinkHeader-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/link_header.py
%{python3_sitelib}/LinkHeader-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.3-2
- Update URL (rhbz#1871414)

* Sun Aug 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.3-1
- Initial package for Fedora
