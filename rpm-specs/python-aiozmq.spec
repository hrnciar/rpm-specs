# Created by pyp2rpm-3.3.2

%global pypi_name aiozmq

%global commit 4e6703c7c56e07c58898228f5d4cf5cb56065a26
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

%global gitrev 20191223git%{shortcommit}

%global _description %{expand:
asyncio (PEP 3156) support for ZeroMQ, a messaging library.
Features:
 * Implements create_zmq_connection() coroutine for making 0MQ connections.
 * Provides ZmqTransport and ZmqProtocol
 * Provides RPC Request-Reply, Push-Pull and Publish-Subscribe patterns for
   remote calls.
}

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        5.20191223git%{shortcommit}%{?dist}
Summary:        ZeroMQ integration with asyncio

License:        BSD
URL:            https://aiozmq.readthedocs.org
#Source0:        https://files.pythonhosted.org/packages/source/a/{pypi_name}/{pypi_name}-{version}.tar.gz
#Source0:        https://github.com/aio-libs/{pypi_name}/archive/v{version}.tar.gz
Source0:        https://github.com/aio-libs/aiozmq/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(msgpack-python) >= 0.4.0
BuildRequires:  python3dist(pyzmq) >= 13.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-pytest

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(msgpack-python) >= 0.4.0
Requires:       python3dist(pyzmq) >= 13.1
Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name}
%_description

%prep
%autosetup -n %{pypi_name}-%{commit}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -r -i "s/(install_requires = \['pyzmq)>=13.1,<17.1.2('\])/\1\2/" setup.py

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v tests/ \
  --deselect tests/zmq_events_test.py::ZmqEventLoopTests::test_close_on_error

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{_bindir}/aiozmq-proxy
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-5.20191223git4e6703c
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4.20191223git4e6703c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.0-3.20191223git56065a26
- Download source directly from github
- Use macros for generating sources
- Enable tests (Thanks to zbyszek)

* Mon Dec 23 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.8.0-2.20191223git56065a26
- Build from master branch of repo
- contains fixes for python 3.7+

* Sun Dec 22 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.8.0-1
- Initial package.
