%global pypi_name claripy

Name:           python-%{pypi_name}
Version:        8.20.6.8
Release:        1%{?dist}
Summary:        Abstraction layer for constraint solvers

License:        BSD
URL:            https://github.com/angr/claripy
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Claripy is an abstracted constraint-solving wrapper.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-z3
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Claripy is an abstracted constraint-solving wrapper.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove installation requirement. Fedora is using a different name, see above
sed -i -e '/z3-solver/d' setup.py
# Remove shebangs
sed -i -e '/^#!\//, 1d' claripy/{*.py,frontend_mixins/*.py,frontends/*.py}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.8-1
- Update to latest upstream release 8.20.6.8

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.1-1
- Don't delete a specific line
- Update to latest upstream release 8.20.6.1

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-2
- Fix installation requirements (rhbz#1815670)

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-1
- Initial package for Fedora
