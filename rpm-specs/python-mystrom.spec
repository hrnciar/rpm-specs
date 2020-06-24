%global pypi_name mystrom

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        1%{?dist}
Summary:        Asynchronous Python API client for interacting with myStrom devices

License:        MIT
URL:            https://github.com/fabaff/python-mystrom
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Asynchronous Python API client for interacting with myStrom devices like bulbs
and plugs. The buttons can be programmed easily with the command-line tool.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Asynchronous Python API client for interacting with myStrom devices like bulbs
and plugs. The buttons can be programmed easily with the command-line tool.

%package -n %{pypi_name}
Summary:        CLI tool to interact with myStrom devices

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n %{pypi_name}
CLI tool to interact with myStrom devices (bulbs, buttons and plugs).

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/py%{pypi_name}/
%{python3_sitelib}/python_mystrom*.egg-info

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}

%changelog
* Mon Jun 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.3-1
- Update to latest upstream release 1.1.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-2
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.2-1
- Update to latest upstream release 1.1.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Initial package for Fedora
