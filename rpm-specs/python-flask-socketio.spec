# Created by pyp2rpm-3.3.2
%global pypi_name flask-socketio
%global egg_name Flask_SocketIO

%global _description %{expand:
Flask-SocketIO gives Flask applications access to low latency bi-directional 
communications between the clients and the server. The client-side application 
can use any of the SocketIO official clients libraries in Javascript, C++, 
Java and Swift, or any compatible client to establish a permanent connection 
to the server.}

Name:           python-%{pypi_name}
Version:        4.2.1
Release:        4%{?dist}
Summary:        Socket.IO integration for Flask applications

License:        MIT
URL:            http://github.com/miguelgrinberg/Flask-SocketIO/
# pypi source tarball does not contain tests
#Source0:        https://files.pythonhosted.org/packages/source/f/{pypi_name}/Flask-SocketIO-{version}.tar.gz
Source0:        https://github.com/miguelgrinberg/%{pypi_name}/archive/v%{version}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(flask) >= 0.9
BuildRequires:  python3dist(python-socketio) >= 4.3.0
BuildRequires:  python3dist(setuptools)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(flask) >= 0.9
Requires:       python3dist(python-socketio) >= 4.3.0

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n Flask-SocketIO-%{version}
# Remove bundled egg-info
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
%{python3_sitelib}/flask_socketio
%{python3_sitelib}/%{egg_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.1-2
- Use expand macro for description

* Sun Dec 22 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 4.2.1-1
- Initial package.
