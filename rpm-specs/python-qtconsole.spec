%global pypi_name qtconsole

Name:		python-%{pypi_name}
Version:	4.7.5
Release:	1%{?dist}
Summary:	Jupyter Qt console

#license clarification issue opened with upstream
# https://github.com/jupyter/qtconsole/issues/142
License:	BSD

URL:		http://jupyter.org
Source0:	https://files.pythonhosted.org/packages/source/q/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-ipython-sphinx
BuildRequires:	python3-sphinx_rtd_theme

BuildRequires:	desktop-file-utils

%description
Qt-based console for Jupyter with support for rich media output

%package -n     python3-%{pypi_name}
Summary:	Jupyter Qt console
%{?python_provide:%python_provide python3-%{pypi_name}}

Provides:	python3-ipython-gui = %{version}-%{release}
%{?python_provide:%python_provide python3-ipython-gui}
Obsoletes:	python3-ipython-gui < 4
 
Requires:	python3-qt5
Requires:	python3-traitlets
Requires:	python3-jupyter-core
Requires:	python3-jupyter-client >= 4.1
Requires:	python3-pygments
Requires:	python3-ipykernel >= 4.1
Requires:	python3-setuptools

%description -n python3-%{pypi_name}
Qt-based console for Jupyter with support for rich media output

%package -n python-%{pypi_name}-doc
Summary:	Documentation subpackage for qtconsole

%description -n python-%{pypi_name}-doc
Documentation for qtconsole

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

# generate html docs 
sphinx-build docs/source html

# fix file encoding and utf-8
sed -i 's/\r$//' html/objects.inv


# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications examples/jupyter-qtconsole.desktop

%files -n python3-%{pypi_name} 
%license LICENSE
%doc README.md
%{_bindir}/jupyter-qtconsole
%{_datadir}/applications/jupyter-qtconsole.desktop
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/*
%dir %{python3_sitelib}/%{pypi_name}/

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Mon Jun 22 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.7.5-1
- Update to 4.7.5

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.4-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4

* Sat May 02 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0

* Thu Sep 26 2019 Miro Hrončok <mhroncok@redhat.com> - 4.5.5-3
- Correct the BR of python3-jupyter-core

* Wed Sep 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 4.5.5-2
- drop Requires: python3-sip (#1753069)

* Mon Sep 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.5.5-1
- Update to 4.5.5

* Thu Aug 22 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.5.3-1
- Update to 4.5.3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.4.4-1
- Update to 4.4.4
- Added python-sphinx_rtd_theme as buildrequires
- Fixed license installation (COPYING.md was renamed to license)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.3.1-7
- Add python3-sip as requires

* Tue Nov 06 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.3.1-6
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-4
- Rebuilt for Python 3.7

* Fri Mar 23 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.3.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1

* Fri Sep 01 2017 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-2
- Move executables from py2 to py3 (#1410332)

* Wed Aug 16 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0
- Added python{,3}-qt5 as requires (fixes #1482258 & #1478629)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-7
- Provide/Obsolete pythonX-ipython-gui

* Wed Feb 22 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.1-6
- Fix python dependencies (py2 sub-package does not req py3)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.1-4
- Removed scripts; F25+ only

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.1-3
- Added scripts for desktop database (fixes embarassing oversight!)

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.1-2
- Fix typos in description
- Fix typos in summary
- Add BR: desktop-file-utils
- Add desktop files

* Fri Aug 12 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 4.2.1-1
- Initial package.
