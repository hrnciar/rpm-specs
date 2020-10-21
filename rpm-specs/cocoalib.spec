# NOTE on SAT implementations.
# Upstream wants MathSat, which is nonfree and closed source.  We can do
# without the solving capability, or we can look for an alternative:
# - glpk: either solves for floating point numbers or integers, but we need to
#   solve for rational solutions.  Looks infeasible.
# - CVC4: has a rational solver, unknown whether it accepts constraints
# - linbox: has a rational solver, unknown whether it accepts constraints
# - one of the coin-or-* packages might provide a suitable solver

Name:           cocoalib
Version:        0.99710
Release:        3%{?dist}
Summary:        C++ library for computations in commutative algebra

License:        GPLv3+
URL:            http://cocoa.dima.unige.it/%{name}/
Source0:        http://cocoa.dima.unige.it/%{name}/tgz/CoCoALib-%{version}.tgz
# Build a shared library instead of a static library
Patch0:         %{name}-shared.patch
# Fix the definition of FFelem values
Patch1:         %{name}-ffelem.patch
# Add a noreturn attribute to silence several warnings
Patch2:         %{name}-noreturn.patch
# Fix out of bounds vector accesses
Patch3:         %{name}-vec.patch
# Initialize cdd for gfanlib
Patch4:         %{name}-gfanlib.patch

BuildRequires:  boost-devel
BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  java-headless
BuildRequires:  libfrobby-devel
BuildRequires:  libgfan-devel
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  tex(latex)
BuildRequires:  tex(ulem.sty)

%description
The CoCoA C++ library offers functions to perform calculations in
Computational Commutative Algebra, and some other related areas.  The
library is designed to be pleasant to use while offering good run-time
performance.

%package devel
Summary:        Headers and library links for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       gsl-devel%{?_isa}
Requires:       libgfan-devel%{?_isa}

%description devel
Headers and library links for developing applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
License:        GFDL
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -p0 -n CoCoALib-%{version}

# Use FlexiBLAS instead of the reference lapack/blas implementation.
# Do not throw away our choice of compiler flags.
# Fix the location of the cddlib headers.
sed -e 's,-lblas -llapack,-lflexiblas,' \
    -e 's/ -Wall -pedantic/ $CXXFLAGS/' \
    -e 's,\(CDD_INC_DIR=\)".*",\1"%{_includedir}/cddlib",' \
    -i configure

# Do not suppress compiler command lines
sed -i 's/\$(MAKE) -s/\$(MAKE)/' Makefile doc/Makefile src/Makefile \
    src/AlgebraicCore/Makefile src/AlgebraicCore/TmpFactorDir/Makefile

# Use Fedora's linker flags
sed -i "s|@RPM_LD_FLAGS@|$RPM_LD_FLAGS|" src/AlgebraicCore/Makefile

%build
# This is NOT an autoconf-generated configure script!
./configure --prefix=%{_prefix} --threadsafe-hack \
  --with-cxxflags="%{optflags} -fPIC -I%{_includedir}/frobby -I%{_includedir}/gfanlib $RPM_LD_FLAGS" \
  --with-libcddgmp=%{_libdir}/libcddgmp.so \
  --with-libfrobby=%{_libdir}/libfrobby.so \
  --with-libgfan=%{_libdir}/libgfan.so \
  --with-libgsl=%{_libdir}/libgsl.so

# Defeat upstream's attempt to force us to use static libraries
pushd configuration/ExternalLibs/lib
for fil in cddgmp frobby gsl; do
  mv lib${fil}-symlink.so lib${fil}-symlink.a
done
popd

%make_build library
%make_build doc

%install
# The Makefile ignores DESTDIR.  Install by hand.

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p src/AlgebraicCore/libcocoa.so.0.0.0 %{buildroot}%{_libdir}
ln -s libcocoa.so.0.0.0 %{buildroot}%{_libdir}/libcocoa.so.0
ln -s libcocoa.so.0 %{buildroot}%{_libdir}/libcocoa.so

# Install the headers
mkdir -p %{buildroot}%{_includedir}
cp -a include/CoCoA %{buildroot}%{_includedir}
rm -f %{buildroot}%{_includedir}/{MakeUnifiedHeader.sh,PREPROCESSOR_DEFNS.H-old}

# Remove files from the doc directories that we want to include in %%files
rm -f doc/CoCoALib-tasks/{HTMLTasks,HTMLTasks.C,Makefile,tasks.xml}
rm -f examples/CopyInfo
chmod a-x examples/*.sh

%check
# 32-bit systems are unable to pass some of the tests due to the limited range
# of the FFelem type.  Disable those tests.
%if 0%{?__isa_bits} == 32
sed -e '/test-factor1\.C/d' \
    -e 's/test-SparsePolyRing1\.C //' \
    -e 's/test-SparsePolyRing5\.C //' \
    -e '/test-SqFreeFactor1\.C/d' \
    -i src/tests/Makefile
%endif

export LD_LIBRARY_PATH=$PWD/lib
make check

%files
%license COPYING-GPLv3
%doc README
%{_libdir}/libcocoa.so.*

%files devel
%{_includedir}/CoCoA
%{_libdir}/libcocoa.so

%files doc
%license doc/COPYING
%doc doc/*.html
%doc doc/*.pdf
%doc doc/CoCoALib-tasks
%doc doc/html
%doc examples

%changelog
* Fri Aug 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.99710-3
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99710-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.99710-1
- Version 0.99710

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 0.99700-1
- Version 0.99700

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99650-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Jerry James <loganjerry@gmail.com> - 0.99650-1
- Version 0.99650
- Drop upstreamed -include and -bigrat patches

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.99601-3
- Rebuilt for GSL 2.6.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99601-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Jerry James <loganjerry@gmail.com> - 0.99601-1
- New upstream version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99600-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 0.99600-2
- Build with openblas instead of atlas (bz 1618942)

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 0.99600-1
- New upstream version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99564-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Jerry James <loganjerry@gmail.com> - 0.99564-1
- New upstream version
- Drop upstreamed -return patch
- Add -include and -bigrat patches to fix FTBFS

* Mon Jun 11 2018 Jerry James <loganjerry@gmail.com> - 0.99563-2
- Make -doc subpackage noarch

* Sat Jun  9 2018 Jerry James <loganjerry@gmail.com> - 0.99563-1
- Initial RPM
