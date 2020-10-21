# Only these have llvm/clang >= 6.  x86_64 el7 has llvm7.0, but not
# clang7.0; it has llvm-toolset-7, but not available in koji.
%global dowrap 0%{?fedora}%{?el8}

# OMPI4 oshcc is now not on all arches (depending on UCX)
%global oshm 1
# Fixme: There's something odd here, since aarch64 has the oshm compilers
%if 0%{?fedora} > 30 || 0%{?el8}
%ifnarch ppc64le x86_64
%global oshm 0
%endif
%endif
%ifarch aarch64
%{?el7:%global oshm 0}
%endif

%global libuwcommit 5646a9b520c51bf6aaa86ae4c25289e30b7c3a41
%global libuwshort %(c=%{libuwcommit}; echo ${c:0:7})

# Needed to get scorep-score built (depending on use of cube C++ lib)
%{?el7:%global dts devtoolset-9}

Name:           scorep
Version:        6.0
Release:        12%{?dist}
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes
License:        BSD
URL:            http://www.vi-hps.org/projects/score-p/
Source0:        https://www.vi-hps.org/cms/upload/packages/%{name}/%{name}-%{version}.tar.gz
# Recommended by developers
Source1:        https://github.com/score-p/libunwind/archive/%{libuwcommit}/libunwind-%{libuwshort}.tar.gz
Patch1:         scorep-rpath.patch
# Fix plugin for GCC 10
Patch2:         scorep-plugin.patch
# Fix argument mismatch errors with gfortran 10
Patch3:         scorep-fortran.patch
# Upstream change for binutils-2.34 BFD
Patch4:         scorep-bfd.patch
Patch5:         scorep-gcc11.patch
BuildRequires:  gcc-gfortran
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  binutils-devel
BuildRequires:  chrpath
BuildRequires:  cube-libs-devel >= 4.4
BuildRequires:  ocl-icd-devel
BuildRequires:  opari2 >= 2.0
BuildRequires:  otf2-devel >= 2.0
BuildRequires:  papi-devel
BuildRequires:  gcc-plugin-devel
%{?dts:BuildRequires:  %dts-gcc-c++}
BuildRequires:  gcc-c++
%if 0%{?dowrap}
BuildRequires:  llvm-devel
BuildRequires:  clang
BuildRequires:  clang-devel
%endif
BuildRequires:  automake libtool
# Required for cubelib to build scorep-score against cubew 4.5
%{?dts:BuildRequires:  %dts-gcc-c++}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       binutils-devel%{?_isa}
Requires:       cube-libs-devel%{?_isa} >= 4.4
Requires:       otf2-devel%{?_isa} >= 2.2
Requires:       papi-devel%{?_isa}
Requires:       ocl-icd-devel%{?_isa}
Requires:       opari2%{?_isa} >= 2.0
# Missing papi and libunwind
ExcludeArch: s390 s390x
Provides:       bundled(libunwind) = 1.3

%global with_mpich 1
%global with_openmpi 1

# el7 has both 1.10 and 3.0, except on ppc64
%ifarch ppc64
%global with_openmpi3 0
%else
%global with_openmpi3 0%{?el7}
%endif

%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif
%if %{with_openmpi3}
%global mpi_list %{?mpi_list} openmpi3
%endif

# Avoid missing symbol link errors in test
%undefine _ld_as_needed
# Avoid in test
#   /usr/bin/ld: pomp_tpd_: TLS reference in ./.libs/libscorep_adapter_opari2_op nmp_event.so mismatches non-TLS reference in jacobi_omp_f90-jacobi.mod.o
%undefine _hardened_build

%global __requires_exclude_from ^%{_libdir}(/(openmpi|mpich)/lib)?/libscorep_.*|^%{_docdir}/.*$


%description
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}


%package libs
Summary:        Score-P runtime libraries
# This is useful at runtime.
Requires:       %{name}-config%{?_isa} = %{version}-%{release}

%description libs
Score-P runtime libraries.

# This is relevant for Scalasca analysis, at least, without the libraries.
%package config
Summary:        Score-P configuration files

%description config
Score-P configuration files.

%if %{with_mpich}
%package mpich
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes for mpich
BuildRequires:  mpich-devel
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}
Requires:       cube-devel%{?_isa} >= 4.4
Requires:       otf2-devel%{?_isa} >= 2.0
Requires:       papi-devel%{?_isa}

%description mpich
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.

This package was compiled with mpich.


%package mpich-libs
Summary:        Score-P mpich runtime libraries
Requires:       %{name}-mpich-config%{?_isa} = %{version}-%{release}
#Provides:       bundled(libunwind) = 1.3

%description mpich-libs
Score-P mpich runtime libraries.

%package mpich-config
Summary:        Score-P mpich configuration files

%description mpich-config
Score-P mpich configuration files.
%endif


%if %{with_openmpi}
%package openmpi
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes for openmpi
BuildRequires:  openmpi-devel
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}
Requires:       cube-devel%{?_isa} >= 4.4
Requires:       otf2-devel%{?_isa} >= 2.0
Requires:       papi-devel%{?_isa}
#Provides:       bundled(libunwind) = 1.3

%description openmpi
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.

This package was compiled with openmpi.

%package openmpi-libs
Summary:        Score-P openmpi runtime libraries
Requires:       %{name}-openmpi-config%{?_isa} = %{version}-%{release}
#Provides:       bundled(libunwind) = 1.3

%description openmpi-libs
Score-P openmpi runtime libraries.

%package openmpi-config
Summary:        Score-P openmpi configuration files

%description openmpi-config
Score-P openmpi configuration files.
%endif

%if %{with_openmpi3}
%package openmpi3
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes for openmpi3
BuildRequires:  openmpi3-devel
Requires:       %{name}-openmpi3-libs%{?_isa} = %{version}-%{release}
Requires:       cube-devel%{?_isa}
Requires:       otf2-devel%{?_isa}
Requires:       papi-devel%{?_isa}

%description openmpi3
The Score-P (Scalable Performance Measurement Infrastructure for
Parallel Codes) measurement infrastructure is a highly scalable and
easy-to-use tool suite for profiling, event trace recording, and
online analysis of HPC applications.

This package was compiled with openmpi3.

%package openmpi3-libs
Summary:        Score-P openmpi3 runtime libraries
#Provides:       bundled(libunwind) = 1.3

%description openmpi3-libs
Score-P openmpi3 runtime libraries.
Requires:       %{name}-openmpi-config%{?_isa} = %{version}-%{release}

%package openmpi3-config
Summary:        Score-P openmpi3 configuration files

%description openmpi3-config
Score-P openmpi3 configuration files.
%endif


%prep
%setup -q
# Bundled libs in vendor/
rm -rf vendor/{opari2,otf2,cubew,cubelib}
mkdir bin
# configure expects llvm-config
ln -s %_bindir/llvm-config-%__isa_bits bin/llvm-config
%patch1 -p1 -b .rpath
%patch2 -p1 -b .plugin
%patch3 -p1 -b .fort
%patch4 -p1 -b .bfd
%patch5 -p1 -b .gcc11
tar fx %SOURCE1


%build
# This package uses -Wl,-wrap to wrap calls at link time.  This is incompatible
# with LTO.
# Disable LTO
%define _lto_cflags %{nil}

%{?dts:. /opt/rh/%dts/enable}
%global _configure ../configure
# It doesn't build on aarch64 due to missing ELF definitions
%ifarch x86_64
pushd libunwind*
# Per Fedora packaging
sed -i 's/= UNW_ARM_METHOD_ALL/= UNW_ARM_METHOD_EXIDX/' src/arm/Gglobal.c
./autogen.sh
CFLAGS="%build_cflags -fcommon" LDFLAGS="%build_ldflags" \
  ./configure --prefix=$(pwd)/unwind --enable-static --disable-dynamic
%make_build -k
%make_install
popd
# See above
PATH=$(pwd)/bin:$PATH
%endif
# Fixme: --disable-silent-rules or V=1 doesn't work in all parts of the build
%global configure_opts --enable-shared --disable-static --disable-silent-rules --with-unwind=$(pwd)/unwind

cp /usr/lib/rpm/redhat/config.{sub,guess} build-config/

# Build serial version
mkdir serial
cd serial
%configure %{configure_opts} --without-mpi --without-shmem
find -name Makefile -exec sed -r -i 's,-L%{_libdir}/?( |$),,g;s,-L/usr/lib/../%{_lib} ,,g' {} \;

# We need to build the plugin for the system compiler, which
# presumably is going to be used when scorep is run, although we're
# overall compiling with devtooset on el7.  I couldn't see a better
# way of doing it than re-configuring here.
%{?el7:(cd build-gcc-plugin; export PATH=%_bindir:$PATH; ./config.status --recheck CXX=%_bindir/g++)}

%make_build V=1
cd -

# Build MPI versions
for mpi in %{mpi_list}
do
  mkdir $mpi
  cd $mpi
  module load mpi/$mpi-%{_arch}
  %configure %{configure_opts} \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --datadir=%{_libdir}/$mpi/share \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --mandir=%{_libdir}/$mpi/share/man
  find -name Makefile -exec sed -r -i 's,-L%{_libdir}/?( |$),,g;s,-L/usr/lib/../%{_lib} ,,g' {} \;
  sed -i -e 's/HARDCODE_INTO_LIBS"]="1"/HARDCODE_INTO_LIBS"]="0"/' \
      -e "s/hardcode_into_libs='yes'/hardcode_into_libs='no'/" \
      build-backend/config.status
  # See serial version
  %{?el7:(cd build-gcc-plugin; export PATH=%_bindir:$PATH; ./config.status --recheck CXX=%_bindir/g++)}
  %make_build V=1
  module purge
  cd -
done


%install
%make_install -C serial
# Strip rpath
chrpath -d %{buildroot}%{_libdir}/*.so.*

for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %make_install -C $mpi
  module purge
done
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -delete

# Fixme: I haven't figured out how to get this re-built with the final
# build-gcc-plugin result; kludge it for now.
find %{buildroot} -name scorep.summary | xargs sed -i -e "s|\
no, missing plug-in headers, please install|\
yes, using the C++ compiler and -I$(%_bindir/gcc -print-file-name=plugin/include)|"

%ldconfig_scriptlets libs

%check
%{?dts:. /opt/rh/%dts/enable}
%if %{with_openmpi}
%_openmpi_load
OMPI_MCA_rmaps_base_oversubscribe=1 \
make -C openmpi check V=1
%else
make -C serial check V=1
%endif


%files
%license COPYING
%doc AUTHORS ChangeLog README THANKS OPEN_ISSUES
%{_bindir}/scorep
%{_bindir}/scorep-backend-info
%{_bindir}/scorep-g++
%{_bindir}/scorep-gcc
%{_bindir}/scorep-gfortran
%{_bindir}/scorep-info
%{_bindir}/scorep-score
%{_bindir}/scorep-wrapper
%{_bindir}/scorep-online-access-registry
%{_bindir}/scorep-preload-init
%if %{dowrap}
%{_bindir}/scorep-libwrap-init
%endif
%{_libdir}/scorep/
%{_includedir}/scorep/
# Are the libtools in here necessary (different from vanilla)?
%{_libexecdir}/scorep

%files doc
%{_defaultdocdir}/scorep/

%files libs
%license COPYING
%{_libdir}/libscorep_*.so*

%files config
%license COPYING
%{_bindir}/scorep-config
%{_datadir}/scorep/

%if %{with_mpich}
%files mpich
%license COPYING
%doc AUTHORS ChangeLog README THANKS OPEN_ISSUES
%{_libdir}/mpich/bin/scorep
%{_libdir}/mpich/bin/scorep-backend-info
%{_libdir}/mpich/bin/scorep-g++
%{_libdir}/mpich/bin/scorep-gcc
%{_libdir}/mpich/bin/scorep-gfortran
%{_libdir}/mpich/bin/scorep-info
%{_libdir}/mpich/bin/scorep-mpicc
%{_libdir}/mpich/bin/scorep-mpicxx
%{_libdir}/mpich/bin/scorep-mpif77
%{_libdir}/mpich/bin/scorep-mpif90
%{_libdir}/mpich/bin/scorep-score
%{_libdir}/mpich/bin/scorep-wrapper
%{_libdir}/mpich/bin/scorep-online-access-registry
%{_libdir}/mpich/bin/scorep-preload-init
%if %{dowrap}
%{_libdir}/mpich/bin/scorep-libwrap-init
%endif
%{_libdir}/mpich/lib/scorep/
%{_includedir}/mpich-%{_arch}/scorep/

%files mpich-libs
%license COPYING
%{_libdir}/mpich/lib/*.so*

%files mpich-config
%license COPYING
%{_libdir}/mpich/bin/scorep-config
%{_libdir}/mpich/share/scorep
%endif

%if %{with_openmpi}
%files openmpi
%license COPYING
%doc AUTHORS ChangeLog README THANKS OPEN_ISSUES
%{_libdir}/openmpi/bin/scorep
%{_libdir}/openmpi/bin/scorep-backend-info
%{_libdir}/openmpi/bin/scorep-g++
%{_libdir}/openmpi/bin/scorep-gcc
%{_libdir}/openmpi/bin/scorep-gfortran
%{_libdir}/openmpi/bin/scorep-info
%{_libdir}/openmpi/bin/scorep-mpicc
%{_libdir}/openmpi/bin/scorep-mpicxx
%{_libdir}/openmpi/bin/scorep-mpif77
%{_libdir}/openmpi/bin/scorep-mpif90
%if %oshm
%{_libdir}/openmpi/bin/scorep-oshcc
%{!?el7:%{_libdir}/openmpi/bin/scorep-oshcxx}
%{_libdir}/openmpi/bin/scorep-oshfort
%endif
%{_libdir}/openmpi/bin/scorep-score
%{_libdir}/openmpi/bin/scorep-wrapper
%{_libdir}/openmpi/bin/scorep-online-access-registry
%{_libdir}/openmpi/bin/scorep-preload-init
%if %{dowrap}
%{_libdir}/openmpi/bin/scorep-libwrap-init
%endif
%{_libdir}/openmpi/lib/scorep/
%{_includedir}/openmpi-%{_arch}/scorep/

%files openmpi-libs
%license COPYING
%{_libdir}/openmpi/lib/*.so*

%files openmpi-config
%license COPYING
%{_libdir}/openmpi/bin/scorep-config
%{_libdir}/openmpi/share/scorep
%endif

%if %{with_openmpi3}
%files openmpi3
%license COPYING
%doc AUTHORS ChangeLog README THANKS OPEN_ISSUES
%{_libdir}/openmpi3/bin/scorep
%{_libdir}/openmpi3/bin/scorep-backend-info
%{_libdir}/openmpi3/bin/scorep-g++
%{_libdir}/openmpi3/bin/scorep-gcc
%{_libdir}/openmpi3/bin/scorep-gfortran
%{_libdir}/openmpi3/bin/scorep-info
%{_libdir}/openmpi3/bin/scorep-mpicc
%{_libdir}/openmpi3/bin/scorep-mpicxx
%{_libdir}/openmpi3/bin/scorep-mpif77
%{_libdir}/openmpi3/bin/scorep-mpif90
%if %oshm
%{_libdir}/openmpi3/bin/scorep-oshcc
%{_libdir}/openmpi3/bin/scorep-oshcxx
%{_libdir}/openmpi3/bin/scorep-oshfort
%endif
%{_libdir}/openmpi3/bin/scorep-score
%{_libdir}/openmpi3/bin/scorep-wrapper
%{_libdir}/openmpi3/bin/scorep-online-access-registry
%{_libdir}/openmpi3/bin/scorep-preload-init
%{_libdir}/openmpi3/lib/scorep/
%{_includedir}/openmpi3-%{_arch}/scorep/

%files openmpi3-libs
%{_libdir}/openmpi3/lib/*.so*

%files openmpi3-config
%license COPYING
%{_libdir}/openmpi3/bin/scorep-config
%{_libdir}/openmpi3/share/scorep
%endif


%changelog
* Fri Oct 16 2020 Jeff Law <law@redhat.com> - 6.0-12
- Add missing includes for gcc-11
- Fix diagnostics triggered by gcc-11

* Wed Aug 19 2020 Dave Love <loveshack@fedoraproject.org> - 6.0-11
- Don't (build)require external libunwind

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Dave Love <loveshack@fedoraproject.org> - 6.0-9
- Fix building gcc plugin, and reporting its use, on el7
- Drop el6 conditionals
- Don't try to install osh on aarch64

* Wed Jul  1 2020 Jeff Law <law@redhat.com> - 6.0-8
- Disable LTO

* Thu Jun 11 2020 Dave Love <loveshack@fedoraproject.org> - 6.0-8
- BR devtoolset-9 on el7

* Wed Feb 26 2020 Dave love <loveshack@fedoraproject.org> - 6.0-7
- Bundle the recommended modified libunwind
- Fix FTBFS with binutils 2.34
- Avoid oshm on el8/fedora aarch64

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 29 2020 Dave Love <loveshack@fedoraproject.org> - 6.0-5
- Add patches for GCC 10

* Fri Aug 30 2019 Dave love <loveshack@fedoraproject.org> - 6.0-4
- Add openmpi3 variant on el7
- Fix logic for mpi running in %%check
- Specify cube and opari version requirements

* Wed Aug 28 2019 Dave love <loveshack@fedoraproject.org> - 6.0-3
- BR libunwind on el8 again (now in EPEL)

* Mon Aug 19 2019 Dave love <loveshack@fedoraproject.org> - 6.0-2
- Don't BR libunwind on el8

* Thu Aug  1 2019 Dave Love <loveshack@fedoraproject.org> - 6.0-1
- New version
- BR otf2 >= 2.2

* Mon Jul 29 2019 Dave Love <loveshack@fedoraproject.org> - 5.0-4
- Bump release to try to trigger rebuild

* Sat Jul 27 2019 Dave Love <loveshack@fedoraproject.org> - 5.0-3
- armv7hl: build libwrap-init again
- Conditionalize osh... wrappers

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Dave Love <loveshack@fedoraproject.org> - 5.0-1
- New version
- Update source URL

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 4.1-6
- Rebuild for openmpi 3.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec  3 2018 Dave Love <loveshack@fedoraproject.org> - 1.4.2-7
- Add openmpi3 variant on el7

* Fri Nov 30 2018 Dave Love <loveshack@fedoraproject.org> - 4.1-4
- BR cube-libs-devel, not cube-devel

* Mon Oct 29 2018 Dave Love <loveshack@fedoraproject.org> - 4.1-3
- Replace rpath hard-coding with patch, not configure fiddle
- Filter requires

* Tue Oct 23 2018 Dave Love <loveshack@fedoraproject.org> - 4.1-2
- Avoid rpath in scorep-config output
- Fix requires for MPI packages
- Move files required for Scalasca to -config packages
- Add license to libs packages

* Fri Oct 12 2018 Dave Love <loveshack@fedoraproject.org> - 4.1-1
- New version
- Remove 64-bit install fixup

* Fri Oct 12 2018 Dave Love <loveshack@fedoraproject.org> - 4.0-3
- Exclude libwrap stuff on ppc64le fedora < 29

* Tue Oct 9 2018 Dave Love <loveshack@fedoraproject.org> - 4.0-2
- Use ldconfig_scriptlets and remove some EPEL-ism in build
- Patch to correct cube configuration
- Build libwrap
- Undefine _ld_as_needed, _hardened_build to make %%check work
- Require libunwind-devel, ocl-icd-devel, opari2 [#1610849]

* Wed Jul 25 2018 Dave Love <loveshack@fedoraproject.org> - 4.0-1
- New version (#1606317, #1574496); soname bump affects old binaries
- Remove bundled cubew, cubelib
- Account for _libdir being partially ignored
- Maybe BR gcc-plugin-devel

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Dave Love <loveshack@fedoraproject.org> - 3.1-6
- Fix check for getaddrinfo; install scorep-online-access-registry

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun  4 2017 Dave Love <loveshack@fedoraproject.org> - 3.1-2
- Remove useless s390 conditional

* Wed May 31 2017 Dave Love <loveshack@fedoraproject.org> - 3.1-1
- Update to 3.1 (#1457285)
- Exclude s390, s390x

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 3 2017 Orion Poplawski <orion@cora.nwra.com> - 3.0-4
- Enable libunwind and OpenCL support

* Tue Jan 31 2017 Orion Poplawski <orion@cora.nwra.com> - 3.0-3
- Rebuild for gcc 7

* Mon Oct 31 2016 Dave Love <loveshack@fedoraproject.org> - 1.4.2-7
- Work around install failure on RHEL 7.2 (bz#1365792)

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0-2
- Rebuild for openmpi 2.0

* Tue Sep 20 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0-1
- Update to 3.0

* Thu Sep 15 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-2
- Rebuild for papi 5.5.0
- Force scorep_platform to be "linux"

* Tue May 24 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-1
- Update to 2.0.2

* Fri Apr 15 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.1-1
- Update to 2.0.1

* Fri Feb 19 2016 Dave Love <loveshack@fedoraproject.org> - 1.4.2-6
- Link against papi-5.1.1 on el6
- Link --as-needed (see previous rpmlint warnings)
- Install OPEN_ISSUES as doc
- Use -std=gnu++98 for gcc6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Orion Poplawski <orion@cora.nwra.com> - 1.4.2-4
- Rebuild for papi 5.4.3

* Wed Sep 16 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4.2-3
- Rebuild for openmpi 1.10.0

* Mon Aug 10 2015 Dave Love <d.love@liverpool.ac.uk> - 1.4.2-2
- Rebuild for updated cube

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 1.4.2-2
- Rebuild for RPM MPI Requires Provides Change

* Fri Jun 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4.2-1
- Update to 1.4.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4.1-2
- Require papi-devel, add requires to mpi packages

* Fri May 8 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4.1-1
- Update to 1.4.1

* Tue May 5 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4-1
- Update to 1.4

* Sun May  3 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-7
- Rebuild for changed mpich

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3-6
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 13 2015 Orion Poplawski <orion@cora.nwra.com> - 1.3-5
- Rebuild for mpich 3.1.4 soname change

* Wed Mar 04 2015 Orion Poplawski <orion@cora.nwra.com> - 1.3-4
- Rebuild for papi

* Mon Jan 19 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.3-3
- update gnu-config files to build on aarch64

* Sat Dec 13 2014 Orion Poplawski <orion@cora.nwra.com> - 1.3-2
- Use %%license

* Fri Oct 3 2014 Orion Poplawski <orion@cora.nwra.com> - 1.3-1
- Update to 1.3

* Tue Mar 4 2014 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-2
- Split out runtime libraries in libs sub-packages
- Fix doc duplication
- Use chrpath to remove rpaths

* Wed Feb 26 2014 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-1
- Update to 1.2.3

* Tue Dec 17 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-1
- Update to 1.2.2
- Drop path patch fixed upstream
- Drop rpath issue fixes, fixed upstream

* Wed Sep 25 2013 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-1
- Initial package
