%global srcname pplpy

Name:           python-%{srcname}
Version:        0.8.4
Release:        8%{?dist}
Summary:        Python PPL wrapper

License:        GPLv3+
URL:            https://pypi.org/project/pplpy/
Source0:        %pypi_source
# Fix the Cython include path and set the language level to 3
Patch0:         %{name}-cython.patch

BuildRequires:  gcc-c++
BuildRequires:  libmpc-devel
BuildRequires:  pari-devel
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  ppl-devel
BuildRequires:  python3-cysignals-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(gmpy2)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
This package provides a Python wrapper to the C++ Parma Polyhedra
Library (PPL).

%package     -n python3-%{srcname}
Summary:        Python 3 PPL wrapper

%description -n python3-%{srcname}
This package provides a Python 3 wrapper to the C++ Parma Polyhedra
Library (PPL).

%package     -n python3-%{srcname}-devel
Summary:        Development files for the python 3 PPL wrapper
Requires:       python3-%{srcname}%{?_isa} = %{version}-%{release}

%description -n python3-%{srcname}-devel
Development files for the python 3 PPL wrapper.

%prep
%autosetup -p0 -n %{srcname}-%{version}

%build
# Do not pass -pthread to the compiler or linker
export CC=gcc
export LDSHARED="gcc -shared"
%py3_build

# Build the documentation
PYTHONPATH=$(ls -1d $PWD/build/lib.*) make -C docs html
rst2html --no-datestamp README.rst README.html

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc CHANGES.txt README.html docs/build/html/*
%license LICENSE.txt
%{python3_sitearch}/pplpy*
%{python3_sitearch}/ppl/
%exclude %{python3_sitearch}/ppl/*.hh
%exclude %{python3_sitearch}/ppl/*.pxd

%files -n python3-%{srcname}-devel
%{python3_sitearch}/ppl/*.hh
%{python3_sitearch}/ppl/*.pxd

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-5
- Invoke cython at language level 3
- Do not link with libpthread unnecessarily

* Tue Sep 10 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-4
- Install the documentation where sagemath wants it

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-1
- Initial RPM
