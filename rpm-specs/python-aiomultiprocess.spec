%global pypi_name aiomultiprocess

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        1%{?dist}
Summary:        Asyncio version of the standard multiprocessing module

License:        MIT
URL:            https://github.com/jreese/aiomultiprocess
Source0:        %{pypi_source}
BuildArch:      noarch

%description
aiomultiprocess presents a simple interface, while running a full AsyncIO
event loop on each child process, enabling levels of concurrency never
before seen in a Python application. Each child process can execute multiple
coroutines at once, limited only by the workload and number of cores available.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiomultiprocess presents a simple interface, while running a full AsyncIO
event loop on each child process, enabling levels of concurrency never
before seen in a Python application. Each child process can execute multiple
coroutines at once, limited only by the workload and number of cores available.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Update to latest upstream release 0.8.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Initial package for Fedora
