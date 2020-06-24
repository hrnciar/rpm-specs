%bcond_without mpich
%bcond_without openmpi

Name:           OpenCoarrays
Version:        2.8.0
Release:        2%{?dist}
Summary:        An open-source Fortran Coarrays implementation for gfortran
License:        BSD
URL:            http://www.opencoarrays.org/
Source0:        https://github.com/sourceryinstitute/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  cmake

# Tests fail on s390x and upstream is unwilling to support the architecture
ExcludeArch:    s390x

%description
OpenCoarrays is an open-source software project that produces an
application binary interface (ABI) used by the GNU Compiler Collection
(GCC) Fortran front-end to build executable programs that leverage the
parallel programming features of the Fortran 2018 Draft International
Standard.

%package devel
Summary:       Development headers for OpenCoarrays
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description devel
This package contains the development headers for OpenCoarrays.

%if %{with openmpi}
%package openmpi
Summary:       OpenMPI interface for OpenCoarrays
Requires:      %{name} = %{version}-%{release}
BuildRequires:  openmpi-devel

%description openmpi
This package contains the OpenCoarrays library compiled against OpenMPI.

%package openmpi-devel
Summary:       OpenMPI development libraries for OpenCoarrays
Requires:      %{name}-devel = %{version}-%{release}
Requires:      %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
This package contains the OpenCoarrays development library compiled
against OpenMPI.
%endif

%if %{with mpich}
%package mpich
Summary:       MPICH interface for OpenCoarrays
Requires:      %{name} = %{version}-%{release}
BuildRequires:  mpich-devel

%description mpich
This package contains the OpenCoarrays library compiled against MPICH.

%package mpich-devel
Summary:       MPICH development libraries for OpenCoarrays
Requires:      %{name}-devel = %{version}-%{release}
Requires:      %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
This package contains the OpenCoarrays development library compiled
against MPICH.
%endif

%prep
%autosetup

%build
%if %{with mpich}
%{_mpich_load}
mkdir mpich
cd mpich
# Failed image support appears to be buggy
%cmake .. -DCAF_ENABLE_FAILED_IMAGES=FALSE
make
cd ..
%{_mpich_unload}
%endif

%if %{with openmpi}
%{_openmpi_load}
mkdir openmpi
cd openmpi
# Failed image support appears to be buggy
%cmake .. -DCAF_ENABLE_FAILED_IMAGES=FALSE
make
cd ..
%{_openmpi_unload}
%endif

%install
%if %{with openmpi}
%{_openmpi_load}
make -C openmpi install DESTDIR=%{buildroot}
# Move files to the right place
mkdir -p %{buildroot}${MPI_BIN}
mv %{buildroot}%{_bindir}/caf* %{buildroot}${MPI_BIN}/
mkdir -p %{buildroot}${MPI_LIB}
mv %{buildroot}%{_libdir}/libcaf* %{buildroot}${MPI_LIB}/
mkdir -p %{buildroot}${MPI_FORTRAN_MOD_DIR}
mv %{buildroot}%{_includedir}/%{name}-*/opencoarrays.mod %{buildroot}${MPI_FORTRAN_MOD_DIR}/
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
make -C mpich install DESTDIR=%{buildroot}
# Move files to the right place
mkdir -p %{buildroot}${MPI_BIN}
mv %{buildroot}%{_bindir}/caf* %{buildroot}${MPI_BIN}/
mkdir -p %{buildroot}${MPI_LIB}
mv %{buildroot}%{_libdir}/libcaf* %{buildroot}${MPI_LIB}/
mkdir -p %{buildroot}${MPI_FORTRAN_MOD_DIR}
mv %{buildroot}%{_includedir}/%{name}-*/opencoarrays.mod %{buildroot}${MPI_FORTRAN_MOD_DIR}/
%{_mpich_unload}
%endif

# Remove symlink
\rm %{buildroot}%{_includedir}/opencoarrays.mod
# Remove cmake files
rm -rf %{buildroot}%{_libdir}/cmake/opencoarrays

# Remove static libraries
%if %{with openmpi}
\rm %{buildroot}%{_libdir}/openmpi/lib/*.a
%endif
%if %{with mpich}
\rm %{buildroot}%{_libdir}/mpich/lib/*.a
%endif

%check
%if %{with openmpi}
%{_openmpi_load}
make -C openmpi check
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
make -C mpich check
%{_mpich_unload}
%endif

%files
%license LICENSE
%doc AUTHORS.md README.md
%doc %{_mandir}/man1/caf*.1*

%files devel
%{_includedir}/libcaf*.h

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/caf*
%{_libdir}/openmpi/lib/libcaf*.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/libcaf*.so
%{_libdir}/gfortran/modules/openmpi/opencoarrays.mod
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/caf*
%{_libdir}/mpich/lib/libcaf*.so.*

%files mpich-devel
%{_libdir}/mpich/lib/libcaf*.so
%{_libdir}/gfortran/modules/mpich/opencoarrays.mod
%endif

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0.

* Thu Jul 25 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2.3.1-3
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1.

* Fri Aug 31 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-3
- Exclude s390x architecture since tests fail and upstream does not want it.

* Thu Aug 23 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-2
- Drop ISO_Fortran_bindings build requirement.

* Thu Aug 16 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.2.0-1
- Split off ISO_Fortran_bindings as it is now a separate project.
- Update to 2.2.0.

* Sun Jul 01 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0.

* Wed Mar 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.0-2
- Disable support for failed images.

* Tue Mar 27 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.0.0-1
- Initial release.


