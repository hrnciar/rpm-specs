%global pypi_name argon2-cffi

Name:           python-%{pypi_name}
Version:        20.1.0
Release:        2%{?dist}
Summary:        The secure Argon2 password hashing algorithm

License:        MIT
URL:            https://argon2-cffi.readthedocs.io/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel >= 3.5
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(wheel)
BuildRequires:  pkgconfig(libargon2)

%description
CFFI-based Argon2 Bindings for Python.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cffi) >= 1.0.0
Requires:       python3dist(hypothesis)
Requires:       python3dist(pytest)
Requires:       python3dist(six)

%description -n python3-%{pypi_name}
CFFI-based Argon2 Bindings for Python.


%package     -n python-%{pypi_name}-doc
Summary:        Documentation for argon2-cffi

%description -n python-%{pypi_name}-doc
Documentation for argon2-cffi.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# using system libargon
rm -r   extras/libargon2/LICENSE \
        extras/libargon2/README.md \
        docs/license.rst


%build
export ARGON2_CFFI_USE_SYSTEM=1
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
export k='not test_argument_ranges'
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/argon2/
%{python3_sitearch}/argon2_cffi-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.1.0-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.1.0-1
- Update to 20.1.0
- Disable LTO

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 19.2.0-1
- Update to 19.2.0
- Switch to {pypi_source}
- Enable LTO
- Cosmetic spec file fix
- Minimum Python version is >= 3.5 now

* Fri Jun 14 2019 Pavlo Rudyi <paulcarroty@fedoraproject.org> - 19.1.0-1
- initial build
