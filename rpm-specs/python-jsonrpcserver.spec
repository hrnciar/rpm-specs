# Created by pyp2rpm-3.3.2
%global pypi_name jsonrpcserver

Name:           python-%{pypi_name}
Version:        4.0.5
Release:        3%{?dist}
Summary:        Process JSON-RPC requests

License:        MIT
URL:            https://github.com/bcb/jsonrpcserver
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A Python 2.7 and 3.4+ server implementation of the JSON RPC 2.0 protocol. 
This library has been pulled out of the Python Language Server project.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(aiohttp)
Requires:       python3dist(aiozmq)
Requires:       python3dist(apply-defaults) < 1
Requires:       python3dist(flask)
Requires:       python3dist(flask-socketio)
Requires:       python3dist(jsonschema) < 4
Requires:       python3dist(jsonschema) >= 2
Requires:       python3dist(pyzmq)
Requires:       python3dist(tornado)
Requires:       python3dist(tox)
Requires:       python3dist(websockets)
Requires:       python3dist(werkzeug)

%description -n python3-%{pypi_name}
A Python 2.7 and 3.4+ server implementation of the JSON RPC 2.0 protocol. 
This library has been pulled out of the Python Language Server project.


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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 4.0.5-1
- Initial package.
