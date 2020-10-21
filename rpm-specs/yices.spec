Name:           yices
Version:        2.6.2
Release:        5%{?dist}
Summary:        SMT solver

# The yices code is GPLv3+.  The cudd code is BSD.
License:        GPLv3+ and BSD
URL:            http://yices.csl.sri.com/
Source0:        https://github.com/SRI-CSL/yices2/archive/Yices-%{version}.tar.gz
# The CUDD web site disappeared in 2018.  The Fedora package was retired in 2019
# when there were no more Fedora users.  Instead of resurrecting the package for
# the sole use of yices, we bundle a snapshot of the last released version.
Source1:        https://github.com/ivmai/cudd/archive/cudd-3.0.0.tar.gz
# Fix the build on big endian machines
# https://github.com/SRI-CSL/yices2/pull/185
Patch0:         %{name}-big-endian.patch
# Adapt to newer versions of cryptominisat
Patch1:         %{name}-cryptominisat.patch
# Adapt to sphinx 3.x
# https://github.com/SRI-CSL/yices2/commit/52d025a6b0ae2af55bf8f537ddeb9cd8f2519237
Patch2:         %{name}-sphinx3.patch

BuildRequires:  cadical-devel
BuildRequires:  cryptominisat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  latexmk
BuildRequires:  libpoly-devel
BuildRequires:  libtool
BuildRequires:  python3dist(sphinx)
BuildRequires:  tex(latex)

# See Source1 comment
Provides:       bundled(cudd) = 3.0.0

%description
Yices 2 is an efficient SMT solver that decides the satisfiability of
formulas containing uninterpreted function symbols with equality, linear
real and integer arithmetic, bitvectors, scalar types, and tuples.

Yices 2 can process input written in the SMT-LIB notation (both versions
2.0 and 1.2 are supported).

Alternatively, you can write specifications using the Yices 2
specification language, which includes tuples and scalar types.

Yices 2 can also be used as a library in other software.

%package devel
Summary:        Development files for yices
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
This package contains the header files necessary for developing programs
which use yices.

%package tools
Summary:        Command line tools that use the yices library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Command line tools that use the yices library.

%package doc
Summary:        Documentation for yices
BuildArch:      noarch

%description doc
This package contains yices documentation.

%prep
%autosetup -n yices2-Yices-%{version} -p1
%setup -q -n yices2-Yices-%{version} -T -D -a 1

# Do not try to avoid -fstack-protector
sed -i 's/@NO_STACK_PROTECTOR@//' make.include.in

# Do not override our build flags
sed -i 's/ -O3//;s/ -fomit-frame-pointer//' src/Makefile tests/unit/Makefile

# Generate the configure script
autoreconf -fi

# Fix end of line encodings
sed -i 's/\r//' examples/{jinpeng,problem_with_input}.ys

# Fix permissions
sed -i 's/cp/install -m 0644/' utils/make_source_version

%build
# Build cudd
cd cudd-cudd-3.0.0
%configure CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"
%make_build
cd -

#bv64_interval_abstraction depends on wrapping for signed overflow
%global optflags %{optflags} -fwrapv

export CPPFLAGS="-I$PWD/cudd-cudd-3.0.0/cudd -DHAVE_CADICAL -DHAVE_CRYPTOMINISAT"
export LDFLAGS="$RPM_LD_FLAGS -L$PWD/cudd-cudd-3.0.0/cudd/.libs"
export LIBS="-lcadical -lcryptominisat5"
%configure --enable-mcsat

guess=$(./config.guess)
if [ "%{_host}" != "$guess" ]; then
  mv configs/make.include.%{_host} configs/make.include.${guess}
fi
%make_build MODE=debug

# Build the manual
make doc

# Build the interface documentation
make -C doc/sphinx html
rm doc/sphinx/build/html/.buildinfo

%install
make install prefix=%{buildroot}%{_prefix} exec_prefix=%{buildroot}%{_prefix} \
     bindir=%{buildroot}%{_bindir} libdir=%{buildroot}%{_libdir} \
     includedir=%{buildroot}%{_includedir}/%{name} MODE=debug
rm -f %{buildroot}%{_libdir}/libyices.a
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1

%ifnarch %{ix86} %{arm}
%check
make check MODE=debug
%endif

%files
%doc doc/SMT-LIB-LANGUAGE doc/YICES-LANGUAGE
%license copyright.txt LICENSE.txt
%{_libdir}/*.so.2*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so

%files tools
%{_bindir}/yices
%{_bindir}/yices-sat
%{_bindir}/yices-smt
%{_bindir}/yices-smt2
%{_mandir}/man1/*

%files doc
%doc doc/manual/manual.pdf doc/sphinx/build/html examples
%license copyright.txt LICENSE.txt

%changelog
* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-5
- Rebuild for cadical 1.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-3
- Rebuild for cryptominisat 5.7.0
- Switch to upstream's solution for sphinx 3 support

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-2
- Use native sphinx 3 support for enum instead of cenum extension (bz 1823515)

* Thu Mar 26 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-1
- Version 2.6.2
- Drop upstreamed -missing-typedef patch
- Add -big-endian patch to fix s390x build
- Add -cryptominisat5 patch to fix build with recent cryptominisat releases
- Skip tests on 32-bit platforms; some tests fail due to the limited size of a
  C integer

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Jerry James <loganjerry@gmail.com> - 2.6.1-5
- Add -missing-typedef patch to fix FTBFS with gcc 10
- Set -doc subpackage to noarch

* Fri Nov 22 2019 Jerry James <loganjerry@gmail.com> - 2.6.1-4
- Add -fwrapv to build flags; thanks to Jeff Law for the diagnosis

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 2.6.1-1
- New upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul  4 2018 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Jerry James <loganjerry@gmail.com> - 2.5.4-2
- Add a -doc subpackage
- Fix end of line encodings
- Fix permissions on yices_debug_version.c

* Mon Jan  1 2018 Jerry James <loganjerry@gmail.com> - 2.5.4-1
- Initial RPM
