Name:           primecount
Version:        6.0
Release:        1%{?dist}
Summary:        Fast prime counting function implementation

License:        BSD
URL:            https://github.com/kimwalisch/%{name}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdivide-static
%ifarch %{ix86} x86_64 ia64 ppc64le
BuildRequires:  libquadmath-devel
%endif
BuildRequires:  primesieve-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Primecount is a command-line program and C++ library that counts the
primes below an integer x<=10**31 using highly optimized implementations
of the combinatorial prime counting algorithms.

Primecount includes implementations of all important combinatorial prime
counting algorithms known up to this date all of which have been
parallelized using OpenMP.  Primecount contains the first ever open
source implementations of the Deleglise-Rivat algorithm and Xavier
Gourdon's algorithm (that works).  Primecount also features a novel load
balancer that is shared amongst all implementations and that scales up
to hundreds of CPU cores.  Primecount has already been used to compute
several world records e.g. pi(10**27)
(http://www.mersenneforum.org/showthread.php?t=20473) and
nth_prime(10**24) (https://oeis.org/A006988).

%package        libs
Summary:        C++ library for fast prime counting

%description    libs
This package contains a C++ library for counting primes below an
integer.  See the primecount package for a command line interface.

%package        devel
Summary:        Headers and library links for libprimecount
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem%{?_isa}

%description    devel
This package contains files necessary to develop applications that use
libprimecount.

%prep
%autosetup -p1

# Unbundle libdivide
rm -f include/libdivide.h
ln -s %{_includedir}/libdivide.h include/libdivide.h

# Do not add flags that change the architecture
sed -i '/if(mpopcnt)/,/endif()/d' CMakeLists.txt

%build
%ifarch %{ix86} x86_64
export CFLAGS="%{optflags} -DLIBDIVIDE_SSE2"
export CXXFLAGS="$CFLAGS"
%endif
mkdir build
cd build
%cmake -DBUILD_LIBPRIMESIEVE=OFF \
       -DBUILD_MANPAGE=ON \
       -DBUILD_SHARED_LIBS=ON \
       -DBUILD_STATIC_LIBS=OFF \
       -DBUILD_TESTS=ON \
       -DWITH_POPCNT=OFF \
%ifarch %{ix86} x86_64 ia64 ppc64le
       -DWITH_FLOAT128=ON \
%endif
       ..
%make_build
cd -

%install
cd build
%make_install
cd -

%check
make test

%files
%doc README.md
%{_bindir}/primecount
%{_mandir}/man1/primecount.1*

%files          libs
%license COPYING
%{_libdir}/libprimecount.so.6*

%files          devel
%doc ChangeLog doc/*.pdf doc/*.md
%{_includedir}/primecount.h
%{_includedir}/primecount.hpp
%{_libdir}/libprimecount.so

%changelog
* Sun Mar 22 2020 Jerry James <loganjerry@gmail.com> - 6.0-1
- Version 6.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Jerry James <loganjerry@gmail.com> - 5.3-1
- Version 5.3

* Mon Nov 18 2019 Jerry James <loganjerry@gmail.com> - 5.2-1
- Version 5.2
- Drop all patches
- Building man page now needs asciidoc instead of help2man

* Fri Sep 20 2019 Jerry James <loganjerry@gmail.com> - 5.1-2
- Add justifications in the patch files
- Generate a man page with help2man

* Thu Sep 19 2019 Jerry James <loganjerry@gmail.com> - 5.1-1
- Initial RPM
