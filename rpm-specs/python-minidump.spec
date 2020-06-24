%global pypi_name minidump

Name:           python-%{pypi_name}
Version:        0.0.13
Release:        2%{?dist}
Summary:        A Python library to parse and read Microsoft minidump file format

License:        MIT
URL:            https://github.com/skelsec/minidump
Source0:        %pypi_source
BuildArch:      noarch

%description
A Python library to parse and read Microsoft minidump file format. Can create
minidumps on Windows machines using the windows API (implemented with ctypes).

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python library to parse and read Microsoft minidump file format. Can create
minidumps on Windows machines using the windows API (implemented with ctypes).

%package -n %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}
Command line tools for the Microsoft minidump file format.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs
sed -i -e '/^#!\//, 1d' %{pypi_name}/{*.py,*/*.py}
# Fix line endings
sed -i "s|\r||g" README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%files -n %{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/%{pypi_name}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.13-2
- Rebuilt for Python 3.9

* Mon Mar 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.13-1
- Use LICENSE file shipped in source tarball
- Update to latest upstream release 0.0.4 (rhbz#1818642)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.12-1
- Update to new upstream version 0.0.12

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 15 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.6-1
- Initial package for Fedora
