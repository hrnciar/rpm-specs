%global pypi_name cppheaderparser

Name:           python-%{pypi_name}
Version:        2.7.4
Release:        1%{?dist}
Summary:        Parse C++ header files and generate a data structure

License:        BSD
URL:            http://senexcanis.com/open-source/cppheaderparser/
Source0:        %{pypi_source CppHeaderParser}
BuildArch:      noarch

%description
Parse C++ header files and generate a data structure representing the
class.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Parse C++ header files and generate a data structure representing the
class.

%prep
%autosetup -n CppHeaderParser-%{version}
rm -rf %{pypi_name}.egg-info
# Remove outdated parts (Python 2.x)
rm -rf CppHeaderParser/{examples,docs}
sed -i -e '/^#!\//, 1d' CppHeaderParser/CppHeaderParser.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.txt README.html
%{python3_sitelib}/CppHeaderParser/
%{python3_sitelib}/CppHeaderParser-%{version}-py%{python3_version}.egg-info/

%changelog
* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.4-1
- Initial package for Fedora