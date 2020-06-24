Name:           gasnet
Version:        2020.3.0
Release:        2%{?dist}
Summary:        A Portable High-Performance Communication Layer for GAS Languages
License:        PostgreSQL
Url:            https://gasnet.lbl.gov
Source0:        https://gasnet.lbl.gov/EX/GASNet-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  perl-generators
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description
GASNet is a language-independent, low-level networking layer that provides
network-independent, high-performance communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

%package common
Summary:        GASNet shared binaries and libraries
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description common
GASNet is a language-independent, low-level networking layer that provides
network-independent, high-performance communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

GASNet files shared between serial and parallel versions

%package openmpi
Summary:        GASNet Open MPI binaries and libraries
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires:  openmpi-devel

%description openmpi
GASNet is a language-independent, low-level networking layer that provides
network-independent, high-performance communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

GASNet compiled with Open MPI, package incl. binaries and libraries

%package mpich
Summary:        GASNet MPICH binaries and libraries
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires:  mpich-devel

%description mpich
GASNet is a language-independent, low-level networking layer that provides
network-independent, high-performance communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

GASNet compiled with MPICH, package incl. binaries and libraries

%package devel
Summary:        Development package for GASNet
Requires:       %{name}%{?_isa} = %{version}
Requires:       %{name}-openmpi%{?_isa} = %{version}
Requires:       %{name}-mpich%{?_isa} = %{version}
Requires:       mpich-devel
Requires:       openmpi-devel
Provides:       gasnet-static = %{version}-%{release}

%description devel
GASNet is a language-independent, low-level networking layer that provides
network-independent, high-performance communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

Development package for GASNet. Including header files and libraries.

%package doc
Summary:        Documentation package for GASNet
BuildArch:      noarch

%description doc
GASNet is a language-independent, low-level networking layer that provides
network-independent, high-performance communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

Documentation package for GASNet.

%prep
%setup -q -n GASNet-%{version}

%build
mkdir serial openmpi mpich
%global _configure ../configure

pushd serial
%configure --enable-udp --disable-mpi --enable-par --disable-aligned-segments --disable-ibv --enable-segment-fast --with-segment-mmap-max=4GB CC="gcc -fPIC" CXX="g++ -fPIC"
%make_build MANUAL_CFLAGS="%optflags -fPIC" MANUAL_MPICFLAGS="%optflags -fPIC" MANUAL_CXXFLAGS="%optflags -fPIC" -j1
popd

pushd openmpi
%{_openmpi_load}
%configure --enable-udp --enable-mpi --enable-par --disable-aligned-segments  --disable-ibv --enable-segment-fast --with-segment-mmap-max=4GB --bindir="${MPI_BIN}"  --includedir="${MPI_INCLUDE}" --libdir="${MPI_LIB}" CC="gcc -fPIC" CXX="g++ -fPIC"
%make_build MANUAL_CFLAGS="%optflags -fPIC" MANUAL_MPICFLAGS="%optflags -fPIC" MANUAL_CXXFLAGS="%optflags -fPIC" -j1
%{_openmpi_unload}
popd

pushd mpich
%{_mpich_load}
%configure --enable-udp --enable-mpi --enable-par --disable-aligned-segments  --disable-ibv --enable-segment-fast --with-segment-mmap-max=4GB --bindir="${MPI_BIN}"  --includedir="${MPI_INCLUDE}" --libdir="${MPI_LIB}" CC="gcc -fPIC" CXX="g++ -fPIC"
%make_build MANUAL_CFLAGS="%optflags -fPIC" MANUAL_MPICFLAGS="%optflags -fPIC" MANUAL_CXXFLAGS="%optflags -fPIC" -j1
%{_mpich_unload}
popd

%check
make -C serial check MANUAL_CFLAGS="%optflags -fPIC" MANUAL_MPICFLAGS="%optflags -fPIC" MANUAL_CXXFLAGS="%optflags -fPIC"
%{_openmpi_load}
make -C openmpi check MANUAL_CFLAGS="%optflags -fPIC" MANUAL_MPICFLAGS="%optflags -fPIC" MANUAL_CXXFLAGS="%optflags -fPIC"
%{_openmpi_unload}
%{_mpich_load}
make -C mpich check MANUAL_CFLAGS="%optflags -fPIC" MANUAL_MPICFLAGS="%optflags -fPIC" MANUAL_CXXFLAGS="%optflags -fPIC"
%{_mpich_unload}

%install
%make_install -C serial
%make_install -C openmpi
%make_install -C mpich

#shared between serial and parallel
rm -f %{buildroot}/%{_libdir}/*mpi*/bin/gasnet_trace

# Minor fixes
chmod +x %{buildroot}/%{_bindir}/*.pl
sed -i '1s@env @@' %{buildroot}/%{_bindir}/*.pl
chmod +x %{buildroot}/%{_libdir}/*mpi*/bin/*.pl
sed -i '1s@env @@' %{buildroot}/%{_libdir}/*mpi*/bin/*.pl

#Upstream doesn't want to support shared libs: https://bitbucket.org/berkeleylab/gasnet/pull-requests/36
# but making shared libs is hard as: "libgasnet_tools-seq.a, libgasnet_tools-par.a, and libgasnet-mpi-par.a
# are all mutually exclusive - each of the GASNet conduit libraries implement the GASNet comm API for that
# backend and and the GASNet-tools API. The gasnet_tools-{seq,par}.a libraries are for clients who want to
# use the GASNet tools API without a conduit. So any given link/executable should include at most ONE library
# matching *gasnet*. The undocumented symbols in these libraries used to implement the macro API may not even
# match in size or type. (Ref: https://github.com/StanfordLegion/legion/issues/445#issuecomment-433159867)

%ldconfig_scriptlets

%files
%{_bindir}/amudprun
%doc ChangeLog README README-tools
%license license.txt

%files common
%{_bindir}/gasnet_trace*

%files openmpi
%{_libdir}/openmpi*/bin/*

%files mpich
%{_libdir}/mpich*/bin/*

%files doc
%{_datadir}/doc/GASNet

%files devel
%doc ChangeLog
%{_includedir}/*.h
%{_includedir}/*.mak
%{_includedir}/*-conduit
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*.pc
%{_libdir}/valgrind
%{_includedir}/openmpi-*/*
%{_libdir}/openmpi*/lib/lib*.a
%{_libdir}/openmpi*/lib/pkgconfig/*.pc
%{_libdir}/openmpi*/lib/valgrind
%{_includedir}/mpich-*/*
%{_libdir}/mpich*/lib/lib*.a
%{_libdir}/mpich*/lib/pkgconfig/*.pc
%{_libdir}/mpich*/lib/valgrind

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2020.3.0-2
- Perl 5.32 rebuild

* Thu Mar 12 2020 Christoph Junghans <junghans@votca.org> - 2020.3.0-1
- Version bump to v2020.3.0 (bug #1813092)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 2019.9.0-2
- Just redefine the configure source file and use the standard
  %configure.  This works better with the redhat-rpm-config
  changes which fix configure files in place for LTO

* Fri Sep 13 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2019.9.0-1
- Update to 2019.9.0 (#1720764)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2019.3.2-2
- Perl 5.30 rebuild

* Tue May 28 2019 Christoph Junghans <junghans@votca.org> - 2019.3.2-1
- Version bump to 2019.3.2 (bug #1714346)
- Build-require perl-generators (bug #1714249)

* Wed May 01 2019 Christoph Junghans <junghans@votca.org> - 2019.3.0-1
- Version bump to 2019.3.0

* Wed May 01 2019 Christoph Junghans <junghans@votca.org> - 1.32.0-5
- Rebuild for legion-19.04.0

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 1.32.0-4
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Christoph Junghans <junghans@votca.org> - 1.32.0-2
- move to static libs

* Thu Oct 25 2018 Christoph Junghans <junghans@votca.org> - 1.32.0-1
- Version bump to 1.32.0 (bug #1606929)
- drop gasnet-s390-support.patch, merged upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.30.0-6
- Perl 5.28 rebuild

* Sat Jun 02 2018 Christoph Junghans <junghans@votca.org> - 1.30.0-5
- Rebuilt for legion-18.05.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Christoph Junghans <junghans@votca.org> - 1.30.0-3
- Rebuilt for legion-18.02.0

* Tue Oct 03 2017 Christoph Junghans <junghans@votca.org> - 1.30.0-2
- Rebuilt for legion-17.08.0-3 on fc27

* Fri Sep 01 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.30.0-1
- Update to 1.30.0 (#1487618)

* Thu Aug 03 2017 Christoph Junghans <junghans@votca.org> - 1.28.2-7
- Added patch from OpenSuse to support s390x (bug #1453092)
- limit to -j1 due to parallel make error

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.28.2-4
- Perl 5.26 rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.28.2-3
- Perl 5.26 rebuild

* Mon May 22 2017 Christoph Junghans <junghans@votca.org> - 1.28.2-2
- Exclude s390x (not supported by upstream) - #1453092

* Sat Mar 18 2017 Christoph Junghans <junghans@votca.org> - 1.28.2-1
- Update to 1.28.2 (#1433545)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Christoph Junghans <junghans@votca.org> - 1.28.0-1
- Version bump (bug #1388084)

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.26.4-7
- Rebuild for openmpi 2.0

* Tue Oct 18 2016 Christoph Junghans <junghans@votca.org> - 1.26.4-6
- Link libamudp against gasnet_tools-seq as suggested by Paul
  Hargrove (upstream), fix broken links in devel package

* Mon Oct 03 2016 Christoph Junghans <junghans@votca.org> - 1.26.4-5
- Added -z,-relro to link flags

* Wed Sep 28 2016 Christoph Junghans <junghans@votca.org> - 1.26.4-4
- Drop --disable-pshm as recommended by Dan Bonachea (upstream) on
  https://bitbucket.org/berkeleylab/gasnet/pull-requests/36

* Mon Sep 26 2016 Christoph Junghans <junghans@votca.org> - 1.26.4-3
- More changes from review (bug #1375744)

* Thu Sep 22 2016 Christoph Junghans <junghans@votca.org> - 1.26.4-2
- Minor changes from review (bug #1375744)

* Mon Sep 12 2016 Christoph Junghans <junghans@votca.org> - 1.26.4-1
- First release.
