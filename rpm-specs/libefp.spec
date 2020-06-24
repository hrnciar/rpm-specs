Name:    libefp
Version: 1.5.0
Release: 7%{?dist}
Summary: A full implementation of the Effective Fragment Potential (EFP) method
License: BSD 
URL:     https://libefp.github.io/
Source0: https://github.com/ilyak/libefp/archive/%{version}/%{name}-%{version}.tar.gz

# Add DESTDIR support
Patch0: libefp-1.5.0-destdir.patch
# Build shared library
Patch1: libefp-1.5.0-shared.patch

# For testing
BuildRequires: gcc-gfortran
BuildRequires: openblas-devel

Requires: %{name}-data = %{version}-%{release}

%description
The Effective Fragment Potential (EFP) method allows one to describe
large molecular systems by replacing chemically inert part of a system
by a set of Effective Fragments while performing regular ab initio
calculation on the chemically active part. The LIBEFP library is a
full implementation of the EFP method. It allows users to easily
incorporate EFP support into their favourite quantum chemistry
package.

%package data
Summary:  Data files for libefp
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description data
This package provides the data files needed by libefp.

%package devel
Summary:  Development headers for libefp
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the development headers for libefp.

%package -n efpmd
Summary: A molecular simulation program based on LIBEFP

%description -n efpmd
EFPMD is a molecular simulation program based on LIBEFP. It supports
single point energy and gradient calculations, semi-numerical Hessian
and normal mode analysis, geometry optimization, molecular dynamics
simulations in microcanonical (NVE), canonical (NVT), and
isobaric-isothermal (NPT) ensembles.


%prep
%setup -q
%patch0 -p1 -b .destdir
%patch1 -p1 -b .sharedlib
cat > config.inc <<EOF
# C compiler
CC= gcc
# Fortran compiler
FC= gfortran
# install prefix
PREFIX=%{_prefix}
# fragment library path
FRAGLIB=%{_prefix}/share/libefp/fraglib
# additional link libraries
MYLIBS=-lopenblaso -lgfortran
# additional linker flags
MYLDFLAGS=
# additional C flags
MYCFLAGS=%{optflags} -std=c99 -fopenmp -fPIC
# additional Fortran flags
MYFFLAGS=%{optflags} -fPIC
EOF

%build
make %{?_smp_mflags}

%install
%make_install LIBDIR=%{_libdir}

# Get rid of scripts with too common names
\rm %{buildroot}%{_bindir}/cubegen.pl
\rm %{buildroot}%{_bindir}/trajectory.pl

# Replace copy with symlink
\rm %{buildroot}%{_libdir}/libefp.so
libname=$(ls %{buildroot}%{_libdir}/libefp.so.*)
ln -s $(basename $libname) %{buildroot}%{_libdir}/libefp.so

%check
export LD_LIBRARY_PATH=$(pwd)/src
make check

%files
%license LICENSE
%doc README.md
%{_libdir}/libefp.so.*

%files data
%{_datadir}/libefp/

%files devel
%{_includedir}/efp.h
%{_libdir}/libefp.so

%files -n efpmd
%{_bindir}/efpmd

%ldconfig_post
%ldconfig_postun

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Susi Lehtola <jussilehtola@fedorapeople.org> - 1.5.0-4
- Add soname to shared library.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Susi Lehtola <jussilehtola@fedorapeople.org> - 1.5.0-2
- Review fixes. Switch to using makefile to get tests to run.

* Mon Mar 26 2018 Susi Lehtola <jussilehtola@fedorapeople.org> - 1.5.0-1
- Update to 1.5.0

* Wed Oct 04 2017 Susi Lehtola <jussilehtola@fedorapeople.org> - 1.4.2-1
- Update to 1.4.2, and review fixes.

* Sun Feb 05 2017 Susi Lehtola <jussilehtola@fedorapeople.org> - 1.4.1-1
- First release.
