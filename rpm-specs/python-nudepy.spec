%global pypi_name nudepy

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Python module for nudity detection

License:        MIT
URL:            https://github.com/hhatto/nude.py
Source0:        %{url}/archive/ver%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%description
Nudity detection in images with Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Nudity detection in images with Python.

%package -n %{pypi_name}
Summary:        %{summary}
Requires:       python3-%{pypi_name}

%description -n %{pypi_name}
Command line tools for nudity detection in images.

%prep
%autosetup -n nude.py-ver%{version}
sed -i -e '/^#!\//, 1d' nude.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitearch}/nude.py
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/skin_classifier*
%{python3_sitearch}/%{pypi_name}*.egg-info

%files -n %{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Add upstream license file
- Fix build issue with Python 3.9 (rhbz#1792967)
- Update to latest upstream release 0.5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-1
- Initial package for Fedora
