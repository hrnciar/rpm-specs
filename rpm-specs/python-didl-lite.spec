%global pypi_name python-didl-lite
%global srcname didl-lite

Name:           python-%{srcname}
Version:        1.2.5
Release:        2%{?dist}
Summary:        DIDL-Lite (Digital Item Declaration Language) tools

License:        ASL 2.0
URL:            https://github.com/StevenLooman/python-didl-lite
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

%description
DIDL-Lite (Digital Item Declaration Language) tools for Python DIDL-Lite tools
for Python to read and write DIDL-Lite-xml.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Tests are only in the GitHub source tarball present which was not released as of today
#BuildRequires:  python3dist(defusedxml)
#BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
DIDL-Lite (Digital Item Declaration Language) tools for Python DIDL-Lite tools
for Python to read and write DIDL-Lite-xml.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

#%%check
#%%pytest -v tests

%files -n python3-%{srcname}
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/didl_lite/
%{python3_sitelib}/python_didl_lite-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.5-2
- Move comment (#1882470)

* Thu Sep 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.5-1
- Initial package for Fedora
