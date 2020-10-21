%global package_name pyfakefs

Name:           python-%{package_name}
Version:        3.5.8
Release:        7%{?dist}
Summary:        pyfakefs implements a fake file system that mocks the Python file system modules.
License:        ASL 2.0
URL:            http://pyfakefs.org
Source0:        https://pypi.io/packages/source/p/%{package_name}/%{package_name}-%{version}.tar.gz
BuildArch:      noarch


%description
pyfakefs implements a fake file system that mocks the Python file system
modules.
Using pyfakefs, your tests operate on a fake file system in memory without
touching the real disk. The software under test requires no modification to
work with pyfakefs.

%package -n python3-%{package_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{package_name}}

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-pytest >= 2.8.6

%description -n python3-%{package_name}
pyfakefs implements a fake file system that mocks the Python file system
modules.
Using pyfakefs, your tests operate on a fake file system in memory without
touching the real disk. The software under test requires no modification to
work with pyfakefs.

%prep
%autosetup -n %{package_name}-%{version} -S git

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%py3_build

%install
%py3_install

%files -n python3-%{package_name}
%license COPYING
%doc README.md
%{python3_sitelib}/%{package_name}
%{python3_sitelib}/*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5.8-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Orion Poplawski <orion@nwra.com> - 3.5.8-1
- Update to 3.5.8

* Sat Apr 27 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1-7
- Subpackage python2-pyfakefs has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 1 2017 David Moreau Simard <dmsimard@redhat.com> - 3.1-1
- First packaged version of pyfakefs
