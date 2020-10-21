%global pypi_name python-snappy

Name:           python-snappy
Version:        0.5.4
Release:        8%{?dist}
Summary:        Python library for the snappy compression library from Google
License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/45/35/65d9f8cc537129894b4b32647d80212d1fa342877581c5b8a69872cea8be/python-snappy-0.5.4.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  snappy-devel

%description
Python bindings for the snappy compression library from Google.


%package -n     python3-snappy
Summary:        Python library for the snappy compression library from Google
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-cffi
BuildRequires:  snappy-devel
Requires:       python3-cffi
Requires:       snappy
# Don't use %%pypi_name here to avoid a python-python-snappy provide
%{?python_provide:%python_provide python3-snappy}

%description -n python3-snappy
Python bindings for the snappy compression library from Google.


%prep
%setup -qn %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install

# Remove shebang
sed -i '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitearch}/snappy/snappy.py


%files -n python3-snappy
%doc README.rst AUTHORS
%license LICENSE
%{python3_sitearch}/python_snappy-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/snappy/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-2
- Subpackage python2-snappy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Mar 23 2019 Julien Enselme <jujens@jujens.eu> - 0.5.4-1
- Update to 0.5.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Julien Enselme <jujens@jujens.eu> - 0.5.3-1
- Update to 0.5.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Julien Enselme <jujens@jujens.eu> - 0.5.2-1
- Update to 0.5.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 07 2017 Julien Enselme <jujens@jujens.eu> - 0.5.1-1
- Update to 0.5.1 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 6 2015 Julien Enselme <jujens@jujens.eu> - 0.5-6
- Correct provides for python2 package

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.5-5
- Rebuilt for python 3.5

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.5-4
- Update package for new python guidelines

* Thu Jul 30 2015 Julien Enselme <jujens@jujens.eu> - 0.5-3
- Add provides for python2-snappy
- Remove usage of python2 and python3 dirs

* Fri Jul 24 2015 Julien Enselme <jujens@jujens.eu> - 0.5-2
- Remove usage of %%py3dir
- Add CFLAGS in %%build

* Sat Jul 18 2015 Julien Enselme <jujens@jujens.eu> - 0.5-1
- Initial packaging
