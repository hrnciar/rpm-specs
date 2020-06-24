%global srcname pep8-naming
%global srcname_ pep8_naming
%global _description \
Check the PEP-8 naming conventions. \
This module provides a plugin for flake8, the Python code checker. \
(It replaces the plugin flint-naming for the flint checker.)


Name:           python-%{srcname}
Version:        0.11.1
Release:        1%{?dist}
Summary:        Check PEP-8 naming conventions, a plugin for flake8

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-flake8
BuildRequires:  (python3dist(flake8-polyfill) >= 1.0.2 with python3dist(flake8-polyfill) < 2)


%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-flake8


%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} run_tests.py


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/pep8ext_naming.py
%{python3_sitelib}/__pycache__/pep8ext_naming.*.py*
%{python3_sitelib}/%{srcname_}-%{version}-py*.egg-info


%changelog
* Sun Jun 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.11.1-1
- Update to latest version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.9

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10.0-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.1-1
- Update to latest version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-9
- Subpackage python2-pep8-naming has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 27 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.4.1-4
- Use python2- BuildRequires/Requires.
- Add license file to package.

* Wed Oct 25 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.4.1-3
- Enable tests during build.
- Simplify spec for Fedora.

* Thu Jun 08 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.4.1-2
- Don't build python3-pep8-naming on EL7

* Tue Jun 6 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.4.1-1
- New upstream release

* Tue Feb 16 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.3.3-1
- Initial RPM release
