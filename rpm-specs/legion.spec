Name:           legion
Version:        20.03.0
Release:        1%{?dist}
Summary:        A data-centric parallel programming system
License:        ASL 2.0
Url:            http://legion.stanford.edu/
Source0:        https://github.com/StanfordLegion/legion/archive/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?fedora} >= 32
# https://github.com/StanfordLegion/legion/issues/575
# The first patch should be OK. The second one is an ugly workaround.
# But legion should fall back to reading directly from /sys, which should
# be OK as a stopgap measure.
Patch0001:      0001-hwloc-2.0-use-hwloc_linux_read_path_as_cpumask.patch
Patch0002:      0002-Disable-hwloc-use-with-online_cpuset.patch
# https://github.com/StanfordLegion/legion/issues/803
Patch0003:      https://gitlab.com/StanfordLegion/legion/-/commit/0741659dc1961b2cdfc7a6c33015670eec2942f3.patch
# https://github.com/StanfordLegion/legion/issues/804
Patch0004:      https://gitlab.com/StanfordLegion/legion/-/commit/3ea76cc5bd3f8afdced55c2d1659f53457c21320.patch
BuildRequires:  hwloc-devel >= 2.0
%else
BuildRequires:  hwloc-devel
%endif

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  gasnet-devel
BuildRequires:  gasnet-static
BuildRequires:  cmake3 >= 3.1

%description
Legion is a data-centric parallel programming system for writing portable
high performance programs targeted at distributed heterogeneous architectures.
Legion presents abstractions which allow programmers to describe properties of
program data (e.g. independence, locality). By making the Legion programming
system aware of the structure of program data, it can automate many of the
tedious tasks programmers currently face, including correctly extracting task-
and data-level parallelism and moving data around complex memory hierarchies.
A novel mapping interface provides explicit programmer controlled placement of
data in the memory hierarchy and assignment of tasks to processors in a way that
is orthogonal to correctness, thereby enabling easy porting and tuning of Legion
applications to new architectures.

%package openmpi
Summary:        Legion Open MPI binaries and libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openmpi
BuildRequires:  openmpi-devel

%description openmpi
Legion is a data-centric parallel programming system for writing portable
high performance programs targeted at distributed heterogeneous architectures.
Legion presents abstractions which allow programmers to describe properties of
program data (e.g. independence, locality). By making the Legion programming
system aware of the structure of program data, it can automate many of the
tedious tasks programmers currently face, including correctly extracting task-
and data-level parallelism and moving data around complex memory hierarchies.
A novel mapping interface provides explicit programmer controlled placement of
data in the memory hierarchy and assignment of tasks to processors in a way that
is orthogonal to correctness, thereby enabling easy porting and tuning of Legion
applications to new architectures.

Legion compiled with Open MPI, package incl. binaries and libraries

%package mpich
Summary:        Legion MPICH binaries and libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mpich
BuildRequires:  mpich-devel

%description mpich
Legion is a data-centric parallel programming system for writing portable
high performance programs targeted at distributed heterogeneous architectures.
Legion presents abstractions which allow programmers to describe properties of
program data (e.g. independence, locality). By making the Legion programming
system aware of the structure of program data, it can automate many of the
tedious tasks programmers currently face, including correctly extracting task-
and data-level parallelism and moving data around complex memory hierarchies.
A novel mapping interface provides explicit programmer controlled placement of
data in the memory hierarchy and assignment of tasks to processors in a way that
is orthogonal to correctness, thereby enabling easy porting and tuning of Legion
applications to new architectures.

Legion compiled with MPICH, package incl. binaries and libraries

%package devel
Summary:        Development headers and libraries for %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-openmpi%{?_isa} = %{version}
Requires:       %{name}-mpich%{?_isa} = %{version}
Requires:       mpich-devel
Requires:       openmpi-devel

%description devel
Legion is a data-centric parallel programming system for writing portable
high performance programs targeted at distributed heterogeneous architectures.
Legion presents abstractions which allow programmers to describe properties of
program data (e.g. independence, locality). By making the Legion programming
system aware of the structure of program data, it can automate many of the
tedious tasks programmers currently face, including correctly extracting task-
and data-level parallelism and moving data around complex memory hierarchies.
A novel mapping interface provides explicit programmer controlled placement of
data in the memory hierarchy and assignment of tasks to processors in a way that
is orthogonal to correctness, thereby enabling easy porting and tuning of Legion
applications to new architectures.

This package contains development headers and libraries for the legion library

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%build
mkdir serial openmpi mpich

%global defopts \\\
 -DLegion_USE_HWLOC=ON \\\
 -DLegion_BUILD_EXAMPLES=ON \\\
 -DCOMPILER_SUPPORTS_MARCH=OFF \\\
 -DCOMPILER_SUPPORTS_MCPU=OFF \\\
 -DLegion_BUILD_TESTS=ON \\\
 -DLegion_BUILD_TUTORIAL=ON \\\
 -DLegion_ENABLE_TESTING=ON \\\

export LDFLAGS="%{__global_ldflags} -Wl,--as-needed"

. /etc/profile.d/modules.sh
for mpi in '' mpich openmpi ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  mkdir -p ${mpi:-serial}
  pushd ${mpi:-serial}
  %{cmake3} %{defopts} \
    $(test -z "${mpi}" && echo -DLegion_USE_GASNet=OFF || echo -DLegion_USE_GASNet=ON -DCMAKE_INSTALL_LIBDIR=${MPI_LIB} -DCMAKE_INSTALL_INCLUDEDIR=${MPI_INCLUDE} -DGASNet_CONDUIT=mpi) \
  ..
  %make_build
  popd
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%install
. /etc/profile.d/modules.sh
for mpi in '' mpich openmpi ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %make_install -C ${mpi:-serial}
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%check
%if 0%{?rhel}
#currently MPI on rhel does not support MPI_THREAD_MULTIPLE
%global testargs ARGS='-E mpi_interop'
%endif

. /etc/profile.d/modules.sh
for mpi in '' mpich openmpi ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  make -C ${mpi:-serial} test CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}
  %make_install -C ${mpi:-serial}
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

#move cmake files in a place where cmake can find them
mkdir -p %{buildroot}%{_libdir}/cmake
mv %{buildroot}{%{_datadir}/Legion,%{_libdir}/cmake/%{name}}

# MPI subpackages don't need the ldconfig magic.  They are hidden by
# default, in MPI back-end-specific directory, and only show to the
# user after the relevant environment module has been loaded.
# rpmlint will report that as errors, but it is fine.
%ldconfig_scriptlets

%files
%doc README.md CHANGES.txt
%license LICENSE.txt
%{_libdir}/lib*.so.1

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/cmake/%{name}
%{_libdir}/openmpi*/lib/lib*.so
%{_libdir}/mpich*/lib/lib*.so

%files openmpi
%{_libdir}/openmpi*/lib/lib*.so.1

%files mpich
%{_libdir}/mpich*/lib/lib*.so.1

%changelog
* Wed Apr 01 2020 Christoph Junghans <junghans@votca.org> - 20.03.0-1
- Version bump to v20.03.0 (bug #1819522)

* Fri Mar 13 2020 Christoph Junghans <junghans@votca.org> - 19.12.0-1
- Version bump to v19.12.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.09.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 19.09.1-1
- Update to 19.09.1 (#1752178)

* Tue Sep 10 2019 Christoph Junghans <junghans@votca.org> - 19.09.0-1
- Version bump to 19.09.0 (bug #1750624)

* Sun Aug 25 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 19.06.0-3
- Rebuilt for hwloc-2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.06.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Christoph Junghans <junghans@votca.org> - 19.06.0-1
- Version bump tp 19.06.0 (bug #1725210)

* Wed May 29 2019 Christoph Junghans <junghans@votca.org> - 19.04.0-2
- Rebuild for gasnet-2019.3.2

* Wed May 01 2019 Christoph Junghans <junghans@votca.org> - 19.04.0-1
- Version bump to 19.04.0 (bug #1705033)

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 18.12.0-2
- Rebuild for openmpi 3.1.3

* Sun Feb 10 2019 Christoph Junghans <junghans@votca.org> - 18.12.0-1
- Version bump to 18.12.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.09.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Christoph Junghans <junghans@votca.org> - 18.09.0-1
- Version bump to 18.09.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.05.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Christoph Junghans <junghans@votca.org> - 18.05.0-1
- Version bump to 18.05.0 (#1585174)

* Mon Feb 12 2018 Christoph Junghans <junghans@votca.org> - 18.02.0-3
- Added gcc-8.patch to support gcc-8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.02.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Christoph Junghans <junghans@votca.org> - 18.02.0-1
- Version bump to 18.02.0 (#1541580)

* Sat Oct 28 2017 Christoph Junghans <junghans@votca.org> - 17.10.0-1
- Version bump to 17.10.0

* Tue Oct 03 2017 Christoph Junghans <junghans@votca.org> - 17.08.0-3
- Rebuilt for gasnet-1.30.0 for fc27

* Fri Sep 01 2017 Christoph Junghans <junghans@votca.org> - 17.08.0-2
- Rebuilt for gasnet-1.30.0

* Fri Aug 25 2017 Christoph Junghans <junghans@votca.org> - 17.08.0-1
- Update to 17.08.0 (#1485085)
- Re-enable tests on ppc and some on epel7

* Fri Aug 04 2017 Christoph Junghans <junghans@votca.org> - 17.05.0-4
- Added patch for s390x (bug #1477749), enable gasnet of s390x

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.05.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.05.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Christoph Junghans <junghans@votca.org> - 17.05.0-1
- Version bump to 17.05.0 (bug #1456066)
- Drop 229.patch and 232.patch - merged upstream

* Tue Mar 28 2017 Christoph Junghans <junghans@votca.org> - 17.02.0-5
- Rebuilt for gasnet-1.28.2

* Mon Mar 20 2017 Christoph Junghans <junghans@votca.org> - 17.02.0-4
- Final changes from review (bug #1382755)

* Sun Mar 19 2017 Christoph Junghans <junghans@votca.org> - 17.02.0-3
- Added 232.patch to fix segfault for test on 1 thread systems
- Disable some broken tests on ppc64

* Mon Mar 13 2017 Christoph Junghans <junghans@votca.org> - 17.02.0-2
- Added 229.patch to support "make check" in cmake
- Minor changes from review (bug #1382755)

* Fri Feb 24 2017 Christoph Junghans <junghans@votca.org> - 17.02.0-1
- initial import

