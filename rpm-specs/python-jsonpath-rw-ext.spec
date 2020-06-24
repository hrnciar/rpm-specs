# Created by pyp2rpm-2.0.0
%global pypi_name jsonpath-rw-ext
%global sname jsonpath_rw_ext

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        7%{?dist}
Summary:        Extensions for JSONPath RW

License:        ASL 2.0
URL:            https://github.com/sileht/python-jsonpath-rw-ext
Source0:        https://pypi.python.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Extensions for JSONPath RW

%package -n     python3-%{pypi_name}
Summary:        Extensions for JSONPath RW
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx

Requires:       python3-pbr >= 1.8
Requires:       python3-jsonpath-rw >= 1.2

%description -n python3-%{pypi_name}
Extensions for JSONPath RW

%package -n python-%{pypi_name}-doc
Summary:        jsonpath-rw-ext documentation
%description -n python-%{pypi_name}-doc
Documentation for jsonpath-rw-ext

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%{__python3} setup.py build
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python3} setup.py install --skip-build --root %{buildroot}


%files -n python3-%{pypi_name}
%license LICENSE
%doc doc/source/readme.rst README.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/*.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Subpackage python2-jsonpath-rw-ext has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Feb 26 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.2.0-1
- Bump to 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 05 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.0.0-1
- Rebase to 1.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 01 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.7-1
- Initial package.
