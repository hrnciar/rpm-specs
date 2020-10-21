%global pypi_name adb-shell

Name:           python-%{pypi_name}
Version:        0.2.3
Release:        1%{?dist}
Summary:        Python implementation for ADB shell and file sync

License:        ASL 2.0
URL:            https://github.com/JeffLIrion/adb_shell
Source0:        %{pypi_source adb_shell}
BuildArch:      noarch

%description
Python package implements ADB shell and FileSync functionality.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python package implements ADB shell and FileSync functionality.

%prep
%autosetup -n adb_shell-%{version}
rm -rf %{pypi_name}.egg-info
# Conflict with crypto
sed -i -e 's/pycryptodome/pycryptodomex/g' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/adb_shell/
%{python3_sitelib}/adb_shell-%{version}-py*.egg-info/

%changelog
* Mon Aug 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.3-1
- Update to new upstream release 0.2.3 (#1883034)

* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.2-1
- Update to new upstream release 0.2.2 (#1871369)

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Update to new upstream release 0.2.1 (#1858210)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Update to latest upstream release 0.2.0 (#1858210)

* Wed Jun 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.7-1
- Add license file
- Update to latest upstream release 0.1.7

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.4-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-1
- Update to latest upstream release 0.1.4

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- Initial package for Fedora
