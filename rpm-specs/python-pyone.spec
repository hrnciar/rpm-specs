%global pypi_name pyone

Name:           python-%{pypi_name}
Version:        5.10.4
Release:        2%{?dist}
Summary:        Python Bindings for OpenNebula XML-RPC API

License:        ASL 2.0
URL:            http://opennebula.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://github.com/OpenNebula/addon-pyone/blob/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-aenum
BuildRequires:  python3-check-manifest
BuildRequires:  python3-coverage
BuildRequires:  python3-dicttoxml
BuildRequires:  python3-lxml
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-tblib
BuildRequires:  python3-xmltodict
%description
OpenNebula Python Bindings Description --PyOne is an implementation of Open
Nebula XML-RPC bindings in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-aenum
Requires:       python3-coverage
Requires:       python3-dicttoxml
Requires:       python3-lxml
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-tblib
Requires:       python3-xmltodict

%description -n python3-%{pypi_name}
OpenNebula Python Bindings Description --PyOne is an implementation of Open
Nebula XML-RPC bindings in Python. It has been integrated into upstream
OpenNebula release cycles from here <

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
install -pm 0644 %{SOURCE1} LICENSE
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.10.4-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 siddharthvipul <siddharthvipul1@gmail.com> - 5.10.4-1
- Initial package.
