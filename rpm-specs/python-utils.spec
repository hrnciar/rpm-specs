Name:           python-utils
Version:        2.4.0
Release:        2%{?dist}
Summary:        Python Utils is a module with some convenient utilities

License:        BSD
URL:            https://github.com/WoLpH/python-utils
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-sphinx

%?python_enable_dependency_generator

%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. This module makes it easy to
execute common tasks in Python scripts such as converting text to numbers
and making sure a string is in unicode or bytes format.

%package -n     python3-utils
Summary:        %{summary}
%{?python_provide:%python_provide python3-utils}

%description -n python3-utils
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. This module makes it easy to
execute common tasks in Python scripts such as converting text to numbers
and making sure a string is in unicode or bytes format.


%prep
%autosetup -p1 -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

# Stop linting code in %%check and measuring coverage, this is upstream's business
sed -Ei '/--(cov|pep8|flakes)/d' pytest.ini

%build
%py3_build
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/{.doctrees,.buildinfo,*.inv}


%install
%py3_install


%check
%{__python3} setup.py pytest --addopts --ignore=build


%files -n python3-utils
%doc README.rst html
%license LICENSE
%{python3_sitelib}/python_utils
%{python3_sitelib}/python_utils-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 2.4.0-1
- Update to 2.4.0 (#1809705)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Orion Poplawski <orion@nwra.com> - 2.3.0-5
- Add patch to build docs with python 3 (bugz#1709063)
- Drop unneeded BR on pytest-cache

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Rebuilt for Python 3.7

* Sat May 05 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-1
- New version 2.3.0 (#1474328)
- Use automatic dependency generator

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-1
- New version 2.1.0 (#1438625)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-1
- Updated, added LICENSE file

* Sun Dec 04 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-1
- Initial package
