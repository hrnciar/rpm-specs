%global pypi_name shodan
# The tests require a working API key and the possibility to connect to Shodan.io
%bcond_with api_key
# Add your Shodan.io API key
%global api_key ABCDEFGH

Name:           python-%{pypi_name}
Version:        1.23.0
Release:        1%{?dist}
Summary:        Python library and command-line utility for Shodan.io

License:        MIT
URL:            https://github.com/achillean/shodan-python
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  dos2unix

%description
The official Python library and CLI for Shodan Shodan is a search engine for 
Internet-connected devices. Google lets you search for websites, Shodan lets
you search for devices. This library provides developers easy access to all
of the data stored in Shodan in order to automate tasks and integrate into
existing tools.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-click
BuildRequires:  python3-click-plugins
BuildRequires:  python3-colorama
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-xlsxwriter
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The official Python library and CLI for Shodan Shodan is a search engine for 
Internet-connected devices. Google lets you search for websites, Shodan lets
you search for devices. This library provides developers easy access to all
of the data stored in Shodan in order to automate tasks and integrate into
existing tools.

%package -n python-%{pypi_name}-doc
Summary:        %{name} documentation

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%package -n     %{pypi_name}
Summary:        CLI tool to access Shodan.io

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{pypi_name}
Command-line tool to to access Shodan.io.

%prep
%autosetup -n %{pypi_name}-python-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' shodan/cli/worldmap.py
dos2unix docs/{api.rst,tutorial.rst}
dos2unix docs/examples/{basic-search.rst,cert-stream.rst,query-summary.rst}
%if %{with api_key}
echo %{api_key} > SHODAN-API-KEY
%endif

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%if %{with api_key}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.23.0-1
- Update to latest upstream release 1.23.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.22.0-2
- Rebuilt for Python 3.9

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.22.0-1
- Update to latest upstream release 1.22.0

* Thu Jan 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.3-3
- Fix line endings

* Tue Jan 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.3-2
- Fix ownership
- Improve the check workflow (rhbz#1795077)

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.3-1
- Initial package for Fedora
