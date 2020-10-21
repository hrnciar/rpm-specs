%global commit 0d9635ae238b52b977b259aa5f5cddc26e8a2a91

Name:           OpenMolcas
Version:        19.11
Release:        7%{?dist}
Summary:        A multiconfigurational quantum chemistry software package
License:        LGPLv2
URL:            https://gitlab.com/Molcas/OpenMolcas
Source0:        https://gitlab.com/Molcas/OpenMolcas/-/archive/v%{version}/%{name}-%{version}.tar.gz 

# Fedora patches
Patch0:         OpenMolcas-19.11-fedora.patch
# Read python modules from system directory
Patch1:         OpenMolcas-19.11-pymodule.patch
# Proper integer type
Patch2:         OpenMolcas-19.11-int8.patch

BuildRequires:  cmake
BuildRequires:  gcc-gfortran
%if 0%{?fedora} >= 33
BuildRequires:  pkgconfig(flexiblas)
%else
BuildRequires:  openblas-devel
%endif

# Required by runtime
%if 0%{?rhel} == 7
BuildRequires:  python2-devel
Requires:       pyparsing
%else
BuildRequires:  python3-devel
Requires:       python3-pyparsing
Requires:       python3-setuptools
%endif

%description
OpenMolcas is a quantum chemistry software package developed by
scientists and intended to be used by scientists. It includes programs
to apply many different electronic structure methods to chemical
systems, but its key feature is the multiconfigurational approach,
with methods like CASSCF and CASPT2.

OpenMolcas is not a fork or reimplementation of Molcas, it is a large
part of the Molcas codebase that has been released as free and
open-source software (FOSS) under the Lesser GNU Public License
(LGPL). Some parts of Molcas remain under a different license by
decision of their authors (or impossibility to reach them), and are
therefore not included in OpenMolcas.

%prep
%setup -q -n %{name}-v%{version}-%{commit}
%patch0 -p1 -b .fedora
%patch1 -p1 -b .pymodule
%patch2 -p1 -b .int8

# Name of OpenBLAS library to use is
%if 0%{?fedora} >= 33
%if 0%{?__isa_bits} == 64
sed -i 's|@OPENBLAS_LIBRARY@|flexiblas64|g' CMakeLists.txt
%else
sed -i 's|@OPENBLAS_LIBRARY@|flexiblas|g' CMakeLists.txt
%endif
%else
%if 0%{?__isa_bits} == 64
sed -i 's|@OPENBLAS_LIBRARY@|openblaso64|g' CMakeLists.txt
%else
sed -i 's|@OPENBLAS_LIBRARY@|openblaso|g' CMakeLists.txt
%endif
%endif

# Location python modules are installed
sed -i 's|@MOLCAS_PYTHON@|%{_libdir}/%{name}/python|g' Tools/pymolcas/pymolcas.py
# Fix shebang
%if 0%{?rhel} == 7
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python2|g' Tools/pymolcas/pymolcas.py
%else
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|g' Tools/pymolcas/pymolcas.py
%endif

%build
export CC=gcc
export FC=gfortran

export CFLAGS="%{optflags} -fopenmp -std=gnu99 -fPIC"
export FFLAGS="%{optflags} -cpp -fopenmp -fdefault-integer-8 -fPIC"

# GCC10 compatibility
%if 0%{?fedora} > 31
export FFLAGS="$FFLAGS -fallow-argument-mismatch"
%endif

%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_libdir}/%{name}/ \
    -DLINALG=OpenBLAS -DOPENMP=ON -DHDF5=OFF -DCHEMPS2=OFF
%{cmake_build}

%install
%{cmake_install}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<EOF
# OpenMolcas root is
export MOLCAS=%{_libdir}/%{name}
export PATH=\${PATH}:\${MOLCAS}/bin:\${MOLCAS}/sbin
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<EOF
# OpenMolcas root is
setenv MOLCAS %{_libdir}/%{name}
export PATH \${PATH}:\${MOLCAS}/bin:\${MOLCAS}/sbin
EOF

# Install the wrapper and its requirements
mkdir -p %{buildroot}%{_libdir}/%{name}/python
for f in tee molcas_aux emil_grammar simpleeval abstract_flow emil_parse python_parse check_test molcas_wrapper; do
    cp -p Tools/pymolcas/${f}.py %{buildroot}%{_libdir}/%{name}/python
done
mkdir -p %{buildroot}%{_bindir}
cp -p Tools/pymolcas/pymolcas.py %{buildroot}%{_bindir}/pymolcas

%files
%license LICENSE
%doc CONTRIBUTORS.md
%{_sysconfdir}/profile.d/%{name}.*
%{_libdir}/%{name}
%{_bindir}/pymolcas

%changelog
* Fri Aug 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 19.11-7
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 19.11-6
- Adapt to new CMake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.11-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 19.11-3
- Explicit buildrequire python3-setuptools.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 19.11-1
- Update to 19.11.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.09-2
- Fix python shebang.

* Wed Jan 02 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.09-1
- Update to 18.09 stable release.

* Tue Sep 25 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-7.o180813.1752
- Remove HDF5 support because upstream code is non-portable and too hard to fix.

* Tue Sep 18 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-6.o180813.1752
- Fix pyparsing requirement on EPEL7.

* Wed Sep 12 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-5.o180813.1752
- Add missing python modules and wrapper.

* Fri Aug 31 2018 Dave Love <loveshack@fedoraproject.org> - 18.0-4.o180813.1752
- Fix build on EPEL

* Fri Aug 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-3.o180813.1752
- Fix build on non-64-bit architectures.

* Fri Aug 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-2.o180813.1752
- Review fixes.

* Thu Aug 16 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.0-1.o180813.1752
- Initial release.
