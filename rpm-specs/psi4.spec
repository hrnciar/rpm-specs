Name:           psi4
Epoch:          1
Version:        1.3.2
Release:        3%{?dist}
Summary:        An ab initio quantum chemistry package
License:        LGPLv3 and MIT
URL:            http://www.psicode.org/
Source0:        https://github.com/psi4/psi4/archive/v%{version}/psi4-%{version}.tar.gz

# Use system packages
Patch0:         psi4-1.3.2-fedora.patch
# Use python3 not python in test runner
Patch1:         psi4-1.3.2-python3.patch
# Patch for libxc5 support
Patch2:         psi4-1.3.2-libxc5.patch

BuildRequires:  cmake
BuildRequires:  bison-devel
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  perl-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  zlib-devel

BuildRequires:  openblas-devel
BuildRequires:  CheMPS2-devel
BuildRequires:  libint-devel >= 1.1.5-3
BuildRequires:  libxc-devel
BuildRequires:  pybind11-static
BuildRequires:  gau2grid-devel
BuildRequires:  libefp-devel

BuildRequires:  python3-devel >= 2.7
BuildRequires:  python3-numpy
BuildRequires:  python3-deepdiff
BuildRequires:  python3-sphinx >= 1.1
BuildRequires:  python3-pydantic
BuildRequires:  python3-qcelemental
# These are required also at runtime
Requires:       python3-numpy
Requires:       python3-pydantic
Requires:       python3-qcelemental
Requires:       python3-deepdiff

# For the documentation
BuildRequires:  tex(latex)
BuildRequires:  tex-preview
BuildRequires:  dvipng
BuildRequires:  graphviz

%if %{with tests}
# Needed for running tests
BuildRequires:  perl(Env)
%endif

Requires:  %{name}-data = %{epoch}:%{version}-%{release}
# Libint can break the api between releases
Requires:  libint(api)%{?_isa} = %{_libint_apiversion}

# Don't have documentation in the cmake version yet.. 
Obsoletes: psi4-doc < 1:0.3-1

%description
PSI4 is an open-source suite of ab initio quantum chemistry programs
designed for efficient, high-accuracy simulations of a variety of
molecular properties. We can routinely perform computations with more
than 2500 basis functions running serially or in parallel.


%package data
Summary:   Data files necessary for operation of PSI4
BuildArch: noarch

%description data
This package contains necessary data files for PSI4, e.g., basis sets
and the quadrature grids.


%package devel
Summary:   Static libraries and development headers for psi
Requires:  %{name}%{?_isa} = %{epoch}:%{version}-%{release}
# For dir ownership
Requires:  cmake

%description devel
This package contains static libraries and development headers for psi.

%prep
%setup -q
%patch0 -p1 -b .fedora
%patch1 -p1 -b .python3
%if 0%{?fedora} > 32
%patch2 -p1 -b .libxc5
%endif

%build
export F77=gfortran
export FC=gfortran

mkdir objdir-%{_target_platform}
cd objdir-%{_target_platform}
%cmake .. \
       -DENABLE_OPENMP=ON -DENABLE_MPI=OFF -DENABLE_XHOST=OFF \
       -DBLAS_LIBRARIES='-lopenblaso' -DLAPACK_LIBRARIES='-lopenblaso' -DENABLE_AUTO_LAPACK=OFF \
       -DCMAKE_Fortran_COMPILER=gfortran -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ \
       -DCUSTOM_C_FLAGS='%{optflags} -std=c11 -DNDEBUG' -DCUSTOM_CXX_FLAGS='%{optflags} -std=c++11 -DNDEBUG' \
       -DCUSTOM_Fortran_FLAGS='-I%{_libdir}/gfortran/modules %{optflags} -DNDEBUG' \
       -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR="%{_lib}" \
       -DENABLE_CheMPS2=ON -DENABLE_libefp=OFF
#libefp turned off since it needs a separate Python wrapper

# Build program
make %{?_smp_mflags} VERBOSE=1

%install
make -C objdir-%{_target_platform} install DESTDIR=%{buildroot}

# Get rid of spurious files
rm -rf %{buildroot}%{_builddir}
rm -rf %{buildroot}%{_datadir}/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/TargetLAPACK/
rm -rf %{buildroot}%{_datadir}/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/cmake/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/cmake/TargetLAPACK/

%check
# Run quick tests to see the program works.
# quicktests are too long, whole test suite way too long.
cd objdir-%{_target_platform}/tests
ctest -L smoketests

%files
%license COPYING COPYING.LESSER
%doc README.md
%{_libdir}/psi4/
%{_bindir}/psi4

%files data
%license COPYING COPYING.LESSER
%{_datadir}/psi4/

%files devel
%license COPYING COPYING.LESSER
%{_datadir}/cmake/psi4/
%{_includedir}/psi4/
%{_libdir}/psi4/

%changelog
* Tue May 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.2-3
- Rebuild against libxc 5 in rawhide.
- Add missing deepdiff requires.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.2-1
- Update to 1.3.2.

* Mon Mar 04 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.0-1
- Update to 1.3.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-5.b167f47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.2.1-4.b167f473git
- Add deepdiff requires.

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 1:1.2.1-3.b167f47
- Require python3-numpy instead of python2-numpy

* Wed Sep 26 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.2.1-2.b167f473git
- Update to git snapshot to make code run with -D_GLIBCXX_ASSERTIONS.

* Sat Sep 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.2.1-1
- Update to 1.2.1.

* Fri Aug 10 2018 Marcel Plch <mplch@redhat.com> - 1:1.1-8.add49b9git
- Patch for pybind 2.2.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-7.add49b9git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:1.1-6.add49b9git
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-5.add49b9git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-4.add49b9git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-3.add49b9git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 19 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.1-2.add49b95git
- Epoch was missing from a requires.

* Wed May 17 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.1-1.add49b95git
- Update to version 1.1. License changes from GPLv2+ to LGPLv3.
- Make sure binary is linked to right atlas library.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-3.2118f2fgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Mar 02 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.0-2.2118f2f5git
- Update to get patch that fixes build on rawhide.

* Mon Feb 27 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.0-1.926879e2git
- Update to newest git snapshot.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-0.3.rc.15fc63cgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1:1.0-0.2.rc.15fc63cgit
- Rebuilt for Boost 1.63

* Thu Jun 02 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.0-0.1.rc.15fc64cgit
- Update to 1.0 release candidate.

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1:0.3-7.1881450git
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-6.1881450git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1:0.3-5.1881450git
- Rebuilt for Boost 1.60

* Wed Sep 09 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3-4.1881450fgit
- Use narrowing patch from upstream instead of -Wno-narrowing.

* Tue Sep 08 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3-3.1881450fgit
- Add epoch to explicit requires.

* Tue Sep 08 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3-2.1881450fgit
- Patch to fix broken linkage.

* Sun Sep 06 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3-1.1881450fgit
- Update to newest release, switched to using github release tags.

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.21.c7deee9git.1
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.0-0.20.c7deee9git.1
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.19.c7deee9git.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0-0.18.c7deee9git.1
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 4.0-0.17.c7deee9git.1
- Rebuild for boost 1.57.0

* Thu Sep 11 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.16.c7deee99.1
- Forgot to tag buildroot override in previous build.

* Wed Sep 10 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.16.c7deee99
- Update to newest snapshot.
- Requires libint(api).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.15.0c7ea92git.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.14.0c7ea92git.1
- Rebuild due to rebuilt libint.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.14.0c7ea92git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 4.0-0.13.0c7ea92git
- Rebuild for boost 1.55.0

* Tue May 13 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.12.0c7ea928git
- Add BR: perl(Env) for tests.

* Tue May 13 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.11.0c7ea928git
- Update to newest git snapshot.
- Remove BR: ruby-devel.

* Mon Mar 10 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.10.b5
- Rebuild against updated libint.

* Sat Jan 04 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.9.b5
- Drop %%?_isa from virtual provide of -static package (BZ #951582).

* Fri Dec 27 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.8.b5
- Versioned libint build dependency.

* Tue Dec 24 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.7.b5
- Added LICENSE and COPYING to -data as well.
- Versioned libint dependency.

* Sat Dec 21 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.6.b5
- Get rid of bundled madness.

* Thu Dec 19 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.5.b5
- Added BR and R on numpy.
- Use ATLAS after all.

* Fri Aug 16 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.4.b5
- Use openblas on supported architectures.
- Update to beta5.

* Thu May 02 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.3.b4
- Added BR on graphviz and enabled dot in configure for documentation.

* Tue Apr 30 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.2.b4
- Review fixes.

* Thu Apr 11 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.1.b4
- First release.
