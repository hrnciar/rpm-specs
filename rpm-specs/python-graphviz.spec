# Created by pyp2rpm-3.3.0
%global pypi_name graphviz

%global common_description %{expand:
This package facilitates the creation and rendering of graph descriptions in
the DOT language of the Graphviz graph drawing software (master repo) from
Python.

Create a graph object, assemble the graph by adding nodes and edges, and
retrieve its DOT source code string. Save the source code to a file and
render it with the Graphviz installation of your system.}

Name:           python-%{pypi_name}
Version:        0.14.1
Release:        2%{?dist}
# Set Epoch to avoid being obsoleted by graphviz-python
Epoch:          1
Summary:        Simple Python interface for Graphviz

License:        MIT
URL:            https://github.com/xflr6/graphviz
Source0:        %{pypi_source %{pypi_name} %{version} zip}

BuildArch:      noarch

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(mock) >= 2
BuildRequires:  python3dist(pytest) >= 3.3
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  graphviz
Requires:       graphviz

%description -n python3-%{pypi_name}
%{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

%description -n python-%{pypi_name}-doc
%{common_description}

This is the documentation package.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's/\r//' docs/*.rst
sed -i 's/\r//' README.rst

%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} -m pytest

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 18:16:51 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1:0.14.1-1
- Update to 0.14.1 (#1856318)

* Fri Jun 19 19:36:17 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1:0.14-1
- Update to 0.14 (#1826692)

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.13.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 00:44:09 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1:0.13.2-1
- Release 0.13.2 (#1771081)

* Mon Sep 23 21:56:51 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1:0.13-2
- Drop Python 2 support (#1754306)

* Wed Sep 11 23:42:39 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1:0.13-1
- Release 0.13 (#1744290)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.11.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 20:01:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1:0.11.1-1
- Release 0.11.1 (#1727363)

* Mon Jun 10 19:42:48 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1:0.11-1
- Release 0.11 (#1716623)

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1:0.10.1-1
- Release 0.10.1 (#1687519)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.3-4
- Drop unneeded build dependencies
- Run the tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.8.3-2
- Rebuilt for Python 3.7

* Thu May 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.3-1
- Upstream release 0.8.3

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.2-1
- Initial package.
