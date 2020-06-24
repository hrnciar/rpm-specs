%global	modname	fpylll

Name:		python-%{modname}
Version:	0.5.1dev
Release:	3%{?dist}
Summary:	A Python wrapper for fplll
License:	GPLv2+
URL:		https://github.com/fplll/%{modname}
Source0:	https://github.com/fplll/%{modname}/releases/download/%{version}/%{modname}-%{version}.tar.gz
# Adapt to mpfr 4
Patch0:		%{name}-mpfr4.patch

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gmp-devel
BuildRequires:	pari-devel
BuildRequires:	pkgconfig(fplll)
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	pkgconfig(qd)

%description
A Python wrapper for fplll.

%package	-n python3-%{modname}
Summary:	A Python 3 wrapper for fplll
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:	python3-cysignals-devel
BuildRequires:	python3-devel
BuildRequires:	python3dist(cython)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(pytest)

Requires:	python3dist(cysignals)

Recommends:	python3dist(ipython)
Recommends:	python3dist(matplotlib)
Recommends:	python3dist(numpy)

%description	-n python3-%{modname}
A Python 3 wrapper for fplll.

%prep
%autosetup -p0 -n %{modname}-%{version}

# Tell Cython to generate python 3 code
sed -i "s/\('language_level': \)2/\13/" setup.py

%build
# Do not pass -pthread to the compiler or linker
export CC=gcc
export LDSHARED="gcc -shared"
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_docdir}/%{name}

%check
pushd tests
    # Note that some tests may fail if sagemath installed and not run
    # under "sage -sh" (to have environment variables defined)
    PYTHONPATH=%{buildroot}%{python3_sitearch} pytest
popd

%files -n python3-%{modname}
%license LICENSE
%doc PKG-INFO README.rst
%{python3_sitearch}/%{modname}
%{python3_sitearch}/%{modname}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1dev-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1dev-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 0.5.1dev-1
- Version 0.5.1dev
- Reenable test_lll

* Fri Nov 29 2019 Jerry James <loganjerry@gmail.com> - 0.5.0dev-1
- Version 0.5.0dev
- Drop upstreamed -time-clock patch
- Add -mpfr4 patch to adapt to mpfr 4

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 0.4.1dev-10
- Rebuild for mpfr 4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1dev-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1dev-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1dev-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Jerry James <loganjerry@gmail.com> - 0.4.1dev-6
- Add -time-clock patch to fix FTBFS with python 3.8 (bz 1718334)
- Pass language_level: 3 to cython

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1dev-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1dev-4
- Subpackage python2-fpylll has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1dev-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1dev-2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 0.4.1dev-1
- Update to 0.4.1dev for libfplll 5.2.1
- BR python-flake8
- R python-cysignals and numpy

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4dev-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 0.2.4dev-1
- Update to 0.2.4dev for libfplll 5.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3dev-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3dev-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 27 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.2.3dev-2
- Add missing changelog
- Add missing URL
- Add python provides to python3 subpackage
- Correct mixed tabs and spaces in the spec
- Implement %%check using pytest
- Add numpy Build Requires
- Add LICENSE as extra source

* Thu Apr 27 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.2.3dev-1
- Initial python-fpylll spec
