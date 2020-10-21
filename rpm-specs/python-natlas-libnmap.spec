%global pypi_name natlas-libnmap

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        2%{?dist}
Summary:        Python library for nmap tasks, parse and compare/diff scan results

License:        CC-BY
URL:            http://pypi.python.org/pypi/natlas-libnmap/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
libnmap is a Python toolkit for manipulating nmap. It allows you to process
namp scans and process the output in various ways.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
libnmap is a Python toolkit for manipulating nmap. It allows you to process
namp scans and process the output in various ways.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' libnmap/reportjson.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/libnmap
%{python3_sitelib}/natlas_libnmap-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Initial package for Fedora
