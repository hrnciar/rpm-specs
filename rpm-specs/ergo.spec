Name:		ergo
Version:	3.8
Release:	1%{?dist}
Summary:	A program for large-scale self-consistent field calculations
License:	GPLv3+
URL:		http://www.ergoscf.org
Source0:	http://ergoscf.org/source/tarfiles/ergo-%{version}.tar.gz

# OpenBLAS causes tests to fail on multiple architectures...
BuildRequires:	atlas-devel
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	gcc-gfortran
BuildRequires:	doxygen
# For tests
BuildRequires:	bc

%description
Ergo is a quantum chemistry program for large-scale self-consistent
field calculations.

Key features of the Ergo program:
* Performs electronic structure calculations using Hartree-Fock and
  Kohn-Sham density functional theory.
* Uses Gaussian basis sets.
* Both core and valence electrons are included in the calculations.
* Both restricted and unrestricted models are implemented for energy
  calculations.
* Implements a broad range of both pure and hybrid Kohn-Sham density
  functionals.
* Employs modern linear scaling techniques like fast multipole
  methods, hierarchic sparse matrix algebra, density matrix
  purification, and efficient integral screening.
* Linear scaling is achieved not only in terms of CPU usage but also
  memory utilization.
* The time consuming parts of the code are currently parallelized
  using the shared-memory paradigm.

Linear response calculations of polarizabilities and excitation energies are
possible for the restricted reference density, although complete linear scaling
is in the current implementation not achieved since full dense matrices are
still used in parts of the linear response implementation.

%package doc
Summary: Documentation for ergo
%if 0%{?rhel} > 5 || 0%{?fedora} > 12
BuildArch: noarch
%endif

%description doc
This package contains the documentation for ergo.

%prep
%setup -q -n ergo-%{version}

%build
# Compilers to use
export CXX=g++
export CC=gcc
export F77=gfortran

# Use OpenMP parallellization
export CFLAGS="%{optflags} -fopenmp"
export CXXFLAGS="${CFLAGS}"
export FFLAGS="${CFLAGS}"

# Linker flags
export LDFLAGS="-L%{_libdir}/atlas"
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
export LIBS="-lsatlas"
%else
export LIBS="-llapack -lf77blas -latlas"
%endif

# Build program
%configure --disable-linalgebra-templates
make %{?_smp_mflags} V=1

# Build documentation
doxygen

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Install basis sets
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a basis %{buildroot}%{_datadir}/%{name}
chmod 644 %{buildroot}%{_datadir}/%{name}/basis/*
rm %{buildroot}%{_datadir}/%{name}/basis/Makefile*

%check
# The check phase runs calculations, so it can be quite slow.
make check VERBOSE=1

%files
%license COPYING ergo_license_long.txt
%doc README ergo_release_notes*
%{_bindir}/ergo
%{_datadir}/%{name}

%files doc
%doc COPYING documentation/html/*

%changelog
* Tue Feb 04 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.8-1
- Update to 3.8.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.7-1
- Update to 3.7, trying to fix issues.

* Sat Jun 23 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.6-2
- Fix FTBFS.

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.6-1
- Added gcc-c++ buildrequires.
- Update to 3.6.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.4-1
- Update to 3.4.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.3.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 25 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1.

* Sun Sep 22 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3-1
- Update to 3.3.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1, fixing operation with global basis set library.

* Mon Sep 17 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.2-2
- Fix tests on i686.

* Thu Jul 05 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.2-1
- Update to 3.2.

* Thu Aug 11 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.1-1
- Update to 3.1.

* Wed Apr 27 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 3.0-1
- Initial release.
