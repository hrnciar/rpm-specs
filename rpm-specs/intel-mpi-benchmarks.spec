Summary: Intel MPI benchmarks
Name:    intel-mpi-benchmarks
Version: 2018.0
Release: 8%{?dist}
License: CPL
URL:     https://software.intel.com/en-us/articles/intel-mpi-benchmarks
Source0: https://github.com/intel/mpi-benchmarks/archive/v%{version}.tar.gz
BuildRequires: gcc

%global desc The Intel MPI Benchmarks perform a set of MPI performance measurements for\
point-to-point and global communication operations for a range of message\
sizes. The generated benchmark data fully characterizes:\
 - Performance of a cluster system, including node performance, network\
   latency, and throughput\
 - Efficiency of the MPI implementation used

%description
%{desc}

%package license
Summary: License of Intel MPI benchmarks
BuildArch: noarch
%description license
This package contains the license of Intel MPI benchmarks.

%package openmpi
Summary: Intel MPI benchmarks compiled against openmpi
BuildRequires: openmpi-devel
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: openmpi
Requires: %{name}-license = %{version}-%{release}
%description openmpi
%{desc}

This package was built against the Open MPI implementation of MPI.

%package mpich
Summary: Intel MPI benchmarks compiled against mpich
BuildRequires: mpich-devel
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: mpich
Requires: %{name}-license = %{version}-%{release}
%description mpich
%{desc}

This package was built against the MPICH implementation of MPI.

%prep
%setup -q -n mpi-benchmarks-%{version}

%build
do_build() {
  mkdir .$MPI_COMPILER
  cp -al * .$MPI_COMPILER
  mv .$MPI_COMPILER build-$MPI_COMPILER
  cd build-$MPI_COMPILER/src
  make -f make_mpich OPTFLAGS="%{optflags}" MPI_HOME="$MPI_HOME" all
  cd ../..
}

# do N builds, one for each mpi stack
%{_openmpi_load}
do_build
%{_openmpi_unload}

%{_mpich_load}
do_build
%{_mpich_unload}

%install
do_install() {
  mkdir -p %{buildroot}$MPI_BIN
  cd build-$MPI_COMPILER/src
  for f in IMB-*; do
    cp "$f" "%{buildroot}$MPI_BIN/${f}$MPI_SUFFIX"
  done
  cd ../..
}

# do N installs, one for each mpi stack
%{_openmpi_load}
do_install
%{_openmpi_unload}

%{_mpich_load}
do_install
%{_mpich_unload}

%files license
%license license/{,use-of-trademark-}license.txt

%files openmpi
%{_libdir}/openmpi/bin/IMB-{MPI1,EXT,IO,NBC,RMA}_openmpi

%files mpich
%{_libdir}/mpich/bin/IMB-{MPI1,EXT,IO,NBC,RMA}_mpich

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2018.0-5
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Michal Schmidt <mschmidt@redhat.com> - 2018.0-1
- Update to upstream release v2018.0.
- The doc/ directory has been removed by upstream. The -doc subpackage is gone.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Michal Schmidt <mschmidt@redhat.com> - 2017-2
- Remove HTML docs from the tarball due to non-free JavaScript files.

* Wed Feb 22 2017 Michal Schmidt <mschmidt@redhat.com> - 2017-1
- Initial package for Fedora.
- Parts copied from the mpitests package from RHEL.
