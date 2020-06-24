# Created by pyp2rpm-3.3.2
%global pypi_name qdarkstyle
%global mod_name QDarkStyle

Name:           python-%{pypi_name}
Version:        2.8
Release:        2%{?dist}
Summary:        A dark stylesheet for Python and Qt applications

License:        MIT
URL:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
Source0:        https://files.pythonhosted.org/packages/source/q/%{pypi_name}/QDarkStyle-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(helpdev) >= 0.6.2
BuildRequires:  python3dist(m2r)
BuildRequires:  python3dist(pyqt5)
BuildRequires:  python3dist(pyside2)
BuildRequires:  python3dist(qtpy) >= 1.7
BuildRequires:  python3dist(qtsass)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-watchdog

# required for tests
BuildRequires:  python3-PyQt4
BuildRequires:  python3dist(pyqtgraph)
BuildRequires:  python3dist(tox)

%description
A dark stylesheet for Qt applications (Qt4, Qt5, PySide, PySide2, PyQt4, 
PyQt5, QtPy, PyQtGraph).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(helpdev) >= 0.6.2
Requires:       python3dist(m2r)
Requires:       python3dist(pyqt5)
Requires:       python3dist(pyside2)
Requires:       python3dist(qtpy) >= 1.7
Requires:       python3dist(qtsass)
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)
Requires:       python3dist(sphinx-rtd-theme)
Requires:       python3dist(watchdog)
Requires:       python3dist(tox)

%description -n python3-%{pypi_name}
A dark stylesheet for Qt applications (Qt4, Qt5, PySide, PySide2, PyQt4, 
PyQt5, QtPy, PyQtGraph).


%prep
%autosetup -n QDarkStyle-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc AUTHORS.rst CHANGES.rst CONTRIBUTING.rst
%{_bindir}/qdarkstyle
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{mod_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8-2
- Rebuilt for Python 3.9

* Mon Mar 16 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.8-1
- Update to 2.8 
- uses pyside2

* Sat Dec 21 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 2.7-1
- Initial package.
