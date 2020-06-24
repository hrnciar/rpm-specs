Name:    libcircle
Version: 0.3
Release: 3%{?dist}

Source: https://github.com/hpc/libcircle/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: http://hpc.github.io/libcircle/
Summary: A library used to distribute workloads
License: BSD

BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
A simple interface for processing workloads using an automatically
distributed global queue.

%package openmpi
Summary:        Libcircle Open MPI libraries
BuildRequires:  openmpi-devel

%description openmpi
A simple interface for processing workloads using an automatically
distributed global queue.

libcircle compiled with Open MPI

%package mpich
Summary:        Libcircle MPICH libraries
BuildRequires:  mpich-devel

%description mpich
A simple interface for processing workloads using an automatically
distributed global queue.

libcircle compiled with MPICH

%package doc
Summary:        Documuation for libcircle
BuildArch:      noarch

%description doc
A simple interface for processing workloads using an automatically
distributed global queue.

This package contain documenation for libcircle

%package openmpi-devel
Summary:    Development headers and libraries for Open MPI libcircle
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
A simple interface for processing workloads using an automatically
distributed global queue.

This package contains development headers and libraries for Open 
MPI ibcircle

%package mpich-devel
Summary:    Development headers and libraries for MPICH libcircle
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
A simple interface for processing workloads using an automatically
distributed global queue.

This package contains development headers and libraries for
MPICH ibcircle

%prep
%setup -q
./autogen.sh

%build
mkdir openmpi mpich
%global _configure ../configure


pushd openmpi
%{_openmpi_load}
%configure --enable-doxygen --enable-tests --disable-static --libdir="${MPI_LIB}" --includedir="${MPI_INCLUDE}"
%make_build
%{_openmpi_unload}
popd

pushd mpich
%{_mpich_load}
%configure --enable-tests --disable-static --libdir="${MPI_LIB}" --includedir="${MPI_INCLUDE}"
%make_build
%{_mpich_unload}
popd

%install
%make_install -C openmpi
%make_install -C mpich
rm %{buildroot}%{_libdir}/*mpi*/lib/*.la

cd openmpi
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r doc/html/* %{buildroot}%{_docdir}/%{name}

%check
%{_openmpi_load}
make -C openmpi check || { cat openmpi/tests/test-suite.log && exit 1; }
%{_openmpi_unload}
%{_mpich_load}
make -C mpich check || { cat mpich/tests/test-suite.log && exit 1; }
%{_mpich_unload}

%files openmpi
%license COPYING AUTHORS
%{_libdir}/openmpi*/lib/%{name}.so.*

%files mpich
%license COPYING AUTHORS
%{_libdir}/mpich*/lib/%{name}.so.*

%files openmpi-devel
%{_libdir}/openmpi*/lib/%{name}.so
%{_libdir}/openmpi*/lib/pkgconfig/%{name}.pc
%{_includedir}/openmpi*/%{name}.h

%files mpich-devel
%{_libdir}/mpich*/lib/%{name}.so
%{_libdir}/mpich*/lib/pkgconfig/%{name}.pc
%{_includedir}/mpich*/%{name}.h

%doc
%{_docdir}/%{name}

%changelog
* Sat Feb 01 2020 Christoph Junghans <junghans@votca.org> - 0.3-3
- Remove s390x workaround

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Christoph Junghans <junghans@votca.org> - 0.3-1
- Version bump to 0.3 (bug #1794592)

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 0.2.1-0.9rc1
- Redefine _configure and use standard #configure macro

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-0.8rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 0.2.1-0.7rc1
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-0.6rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-0.5rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-0.4rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 05 2017 Christoph Junghans <junghans@votca.org> - 0.2.1-0.3rc1
- Comments from #1513733

* Wed Nov 15 2017 Christoph Junghans <junghans@votca.org> - 0.2.1-0.2rc1
- Split devel pacakge

* Wed Nov 15 2017 Christoph Junghans <junghans@votca.org> - 0.2.1-0.1rc1
- First release.
