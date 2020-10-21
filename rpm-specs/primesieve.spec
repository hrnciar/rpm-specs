Name:     primesieve
Version:  7.5
Release:  6%{?dist}
Summary:  Fast prime number generator
License:  BSD
URL:      https://github.com/kimwalisch/primesieve
Source0:  https://github.com/kimwalisch/primesieve/archive/v%{version}.tar.gz
Requires: primesieve-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.7
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  asciidoc

%description
primesieve is a program that generates primes using a highly optimized
sieve of Eratosthenes implementation. primesieve can generate primes
and prime k-tuplets up to 2^64.

%package -n primesieve-libs
Summary: C/C++ library for generating prime numbers

%description -n primesieve-libs
This package contains the shared runtime library for primesieve.

%package -n primesieve-devel
Summary: Development files for the primesieve library
Requires: primesieve-libs%{?_isa} = %{version}-%{release}

%description -n primesieve-devel
This package contains the C/C++ header files and the configuration
files for developing applications that use the primesieve library.
It also contains the API documentation of the library.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake . -DBUILD_STATIC_LIBS=OFF -DBUILD_TESTS=ON -DBUILD_MANPAGE=ON -DBUILD_DOC=ON
%cmake_build
%cmake_build --target doc
find %{_vpath_builddir}/doc/html -name '*.md5' -exec rm {} +

%install
%cmake_install

%ldconfig_scriptlets -n primesieve-libs

%check
make test

%files -n primesieve
%doc README.md ChangeLog
%{_bindir}/primesieve
%{_mandir}/man1/primesieve.1*

%files -n primesieve-libs
%license COPYING
%{_libdir}/libprimesieve.so.*

%files -n primesieve-devel
%doc examples %{_vpath_builddir}/doc/html
%{_libdir}/libprimesieve.so
%{_includedir}/primesieve.h
%{_includedir}/primesieve.hpp
%dir %{_includedir}/primesieve
%{_includedir}/primesieve/StorePrimes.hpp
%{_includedir}/primesieve/iterator.h
%{_includedir}/primesieve/iterator.hpp
%{_includedir}/primesieve/primesieve_error.hpp
%dir %{_libdir}/cmake/primesieve
%{_libdir}/cmake/primesieve/*.cmake
%{_libdir}/pkgconfig/primesieve.pc

%changelog
* Tue Aug 04 2020 Kim Walisch <walki@fedoraproject.org> - 7.5-6
- Fix CMake doc target issue, indicate path

* Tue Aug 04 2020 Kim Walisch <walki@fedoraproject.org> - 7.5-5
- Fix CMake issue, CMake build directory changed in Fedora 33

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Kim Walisch <walki@fedoraproject.org> - 7.5-1
- Update to primesieve-7.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Kim Walisch <walki@fedoraproject.org> - 7.4-2
- Rename libprimesieve to primesieve-libs
- Rename libprimesieve-devel to primesieve-devel
- Increase CMake version to >= 3.7

* Mon Apr 08 2019 Kim Walisch <walki@fedoraproject.org> - 7.4-1
- Update to primesieve-7.4
- Move Requires before description
- Drop libprimesieve-static package

* Sun Jul 08 2018 Kim Walisch <walki@fedoraproject.org> - 7.0-1
- Update to primesieve-7.0
- Fix erroneous date in changelog

* Sat Mar 24 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-5
- Update to primesieve-6.4

* Fri Feb 16 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-4
- Add libprimesieve package
- Improve summaries and descriptions
- Update to primesieve-6.4-rc2

* Tue Feb 06 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-3
- Fix new issues from package review

* Wed Jan 31 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-2
- Fix issues from package review

* Tue Jan 30 2018 Kim Walisch <walki@fedoraproject.org> - 6.4-1
- Initial package
