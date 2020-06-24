%global pypi_name check-manifest

Name:           python-%{pypi_name}
Version:        0.42
Release:        2%{?dist}
Summary:        Check MANIFEST.in in a Python source package

License:        MIT
URL:            https://github.com/mgedmin/check-manifest
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  gpg

%description
Check MANIFEST.in in a Python source package for completeness to avoid the
upload of broken packages.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-toml
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-pep517
BuildRequires:  python3-wheel
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
Check MANIFEST.in in a Python source package for completeness to avoid the
upload of broken packages.

%package -n     %{pypi_name}
Summary:        CLI tool to check MANIFEST.in files

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{pypi_name}
Command-line tool to check MANIFEST.in files.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' check_manifest.py

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} \
  -v tests.py -k "not vcs and not git and not sdist"

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst CHANGES.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/check_manifest.py
%{python3_sitelib}/check_manifest-%{version}-py*.egg-info

%files -n %{pypi_name}
%{_bindir}/check-manifest

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.42-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.42-1
- Update to latest upstream release 0.42 (rhbz#1830740)

* Sat Apr 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.41-1
- Fix build issue (rhbz#1818596)
- Update to latest upstream release 0.41

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.40-2
- Adjust BR (rhbz#1790080)

* Wed Jan 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.40-1
- Initial package for Fedora
