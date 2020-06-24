Name:          intelhex
Version:       2.2.1
Release:       4%{?dist}
Summary:       Utilities for manipulating Intel HEX file format
License:       BSD
URL:           https://github.com/python-intelhex/intelhex
Source0:       https://github.com/python-intelhex/intelhex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: dos2unix
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx

%description
The Intel HEX file format is widely used in microprocessors and microcontrollers
area (embedded systems etc) as the de facto standard for representation of code
to be programmed into microelectronic devices.

This work implements an intelhex Python library and a number of utilities to 
read, write, create from scratch and manipulate data from Intel HEX file format.

The distribution package also includes several convenience Python scripts,
including "classic" hex2bin and bin2hex converters and more, those based on the
library itself. Check the docs to know more.

%package -n python3-intelhex
Summary:  A python3 library for manipulating Intel HEX file format
%{?python_provide:%python_provide python3-intelhex}

%description -n python3-intelhex
The Intel HEX file format is widely used in microprocessors and microcontrollers
area (embedded systems etc) as the de facto standard for representation of code
to be programmed into microelectronic devices.

This work implements an intelhex Python library and a number of utilities to 
read, write, create from scratch and manipulate data from Intel HEX file format.

The distribution package also includes several convenience Python scripts,
including "classic" hex2bin and bin2hex converters and more, those based on the
library itself. Check the docs to know more.

%package docs
Summary:  Manuak for the IntelHex python library

%description docs
User manual for IntelHex

%prep
%autosetup
dos2unix Readme.rst
dos2unix NEWS.rst
sed -i '1d' intelhex/bench.py

%build
%py3_build
pushd docs/manual/
make html
popd 

%install
%py3_install

%files
%doc NEWS.rst Readme.rst
%{_bindir}/*.py

%files -n python3-intelhex
%license LICENSE.txt
%{python3_sitelib}/intelhex*

%files docs
%doc docs/intelhex.pdf docs/manual.txt
%doc docs/manual/.build/html/*.html
%doc docs/manual/.build/html/searchindex.js

%changelog
* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.2.1-4
- Review updates, URL update

* Sat Jul 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.1-3
- Split python bindings and utilities

* Thu Nov  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.1-2
- Minor package updates

* Sun Oct 28 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.1-1
- Initial package
