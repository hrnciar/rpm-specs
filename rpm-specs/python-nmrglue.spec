%global pkgname nmrglue
%global pkgsum Python module for processing NMR data

Name:		python-%{pkgname}
Version:	0.7
Release:	8%{?dist}
Summary:	%{pkgsum}

License:	BSD
URL:		https://github.com/jjhelmus/%{pkgname}
Source0:	https://github.com/jjhelmus/%{pkgname}/archive/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
# these are required for tests
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy

%description
nmrglue is a module for working with NMR data in Python. When used with the 
numpy, scipy, and matplotlib packages nmrglue provides a robust interpreted 
environment for processing, analyzing, and inspecting NMR data.

%package -n python3-%{pkgname}
Summary:	%{pkgsum}
%{?python_provide:%python_provide python3-%{pkgname}}
Requires:	python3-numpy
Requires:	python3-scipy

%description -n python3-%{pkgname}
nmrglue is a module for working with NMR data in Python. When used with the 
numpy, scipy, and matplotlib packages nmrglue provides a robust interpreted 
environment for processing, analyzing, and inspecting NMR data.

%prep
%autosetup -n %{pkgname}-%{version}

# disable tests bundling
sed -i '/nmrglue.fileio.tests/d' setup.py
sed -i '/package_data/d' setup.py
sed -i '/fileio\/tests\/data\//d' setup.py


%build
%py3_build

%install
%py3_install

%check

pushd nmrglue/fileio/tests

#python3 tests
PYTHONPATH="%{buildroot}%{python3_sitelib}" %{__python3} test_pipe.py

popd

%files -n python3-%{pkgname}
%license LICENSE.txt
%doc README.rst TODO.txt
%{python3_sitelib}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7-7
- Add BR:python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.7-1
- Update to 0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-7
- Drop unused python2 build dependencies

* Sat Oct 20 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6-6
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6-1
- Update to version 0.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar 07 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.5-3
- Enable tests
- Fix source URL
- Remove tests from the package

* Sun Mar 06 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.5-2
- Fix requires - move to subpackages
- Shorten description

* Sat Mar  5 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.5-1
- Initial package
