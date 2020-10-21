# Obsolete autotools m4 used
# https://github.com/INCF/libneurosim/issues/11

%global commit 03646747c8fe64fa3439ac2d282623b659f60c22
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global _description \
libneurosim is a general library that provides interfaces and common utility \
code for neuronal simulators. \
\
Currently it provides the ConnectionGenerator interface. \
\
The ConnectionGenerator API is a standard interface supporting efficient \
generation of network connectivity during model setup in neuronal network \
simulators. It is intended as an abstraction isolating both sides of the API: \
any simulator can use a given connection generator and a given simulator can \
use any library providing the ConnectionGenerator interface. It was initially \
developed to support the use of libcsa from NEST.

%bcond_without mpich
%bcond_without openmpi

Name:           libneurosim
Version:        0
Release:        11.20181124.git%{shortcommit}%{?dist}
Summary:        Common interfaces for neuronal simulators

License:        GPLv3+
URL:            https://github.com/INCF/%{name}
Source0:        https://github.com/INCF/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

# Pull in the common package
Requires:       %{name}-common = %{version}-%{release}

%description
%{_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        common
Summary:        Common files for %{name}
BuildArch:      noarch

%description    common
The %{name}-common package contains files required by all sub packages.

%if %{with openmpi}
%package openmpi
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
Requires:       openmpi
Requires:       %{name}-common = %{version}-%{release}
%description openmpi
%{_description}

%package openmpi-devel
Summary:        %{name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
Requires:       openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel
%{_description}

%endif


%if %{with mpich}
%package mpich
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
Requires:       mpich
Requires:       %{name}-common = %{version}-%{release}

%description mpich
%{_description}

%package mpich-devel
Summary:        %{name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
Requires:       mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel
%{_description}

%endif

%prep
%autosetup -c -n %{name}-%{commit}

# Make these accessible here
cp -v %{name}-%{commit}/COPYING .
cp -v %{name}-%{commit}/README.md .

# Default is py3
%if %{with mpich}
    cp -a %{name}-%{commit} %{name}-%{commit}-mpich
%endif

%if %{with openmpi}
    cp -a %{name}-%{commit} %{name}-%{commit}-openmpi
%endif

%build

%global do_build \
pushd %{name}-%{commit}$MPI_COMPILE_TYPE && \
./autogen.sh && \
%{set_build_flags} \
./configure CC=$MPICC CXX=$MPICXX --disable-static \\\
--disable-silent-rules \\\
--with-python=$PYTHON_VERSION \\\
--with-mpi=$MPI_YES \\\
--prefix=$MPI_HOME \\\
--libdir=$MPI_LIB \\\
--includedir=$MPI_INCLUDE \\\
--bindir=$MPI_BIN \\\
--mandir=$MPI_MAN && \
%make_build STRIP=/bin/true && \
popd || exit -1


# Python 3
MPI_COMPILE_TYPE=""
PYTHON_VERSION=3
MPI_YES="no"
MPI_HOME=%{_prefix}
MPI_LIB=%{_libdir}
MPI_INCLUDE=%{_includedir}
MPI_BIN=%{_bindir}
MPI_MAN=%{_mandir}
MPICC=%{__cc}
MPICXX=%{__cxx}
%{do_build}

# Mpich
%if %{with mpich}
%{_mpich_load}
# Python 3
MPI_COMPILE_TYPE="-mpich"
PYTHON_VERSION=3
MPI_YES="yes"
MPICC=mpicc
MPICXX=mpicxx
%{do_build}
%{_mpich_unload}
%endif

# Openmpi
%if %{with openmpi}
%{_openmpi_load}
# Python 3
MPI_COMPILE_TYPE="-openmpi"
PYTHON_VERSION=3
MPI_YES="yes"
MPICC=mpicc
MPICXX=mpicxx
%{do_build}

%{_openmpi_unload}
%endif

%install
%global do_install \
%make_install -C %{name}-%{commit}$MPI_COMPILE_TYPE STRIP=/bin/true || exit -1


# Python 3
MPI_COMPILE_TYPE=""
PYTHON_VERSION=3
%{do_install}

# Mpich
%if %{with mpich}
%{_mpich_load}
# Python 3
MPI_TYPE="mpich"
MPI_COMPILE_TYPE="-mpich"
PYTHON_VERSION=3
PY_VERSION=%{python3_version}
%{do_install}

%{_mpich_unload}
%endif

# Openmpi
%if %{with openmpi}
%{_openmpi_load}
MPI_TYPE="openmpi"
# Python3
MPI_COMPILE_TYPE="-openmpi"
PYTHON_VERSION=3
PY_VERSION=%{python3_version}
%{do_install}

%{_openmpi_unload}
%endif

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.0.0
%{_libdir}/libpy3neurosim.so.0
%{_libdir}/libpy3neurosim.so.0.0.0

%files devel
%{_includedir}/neurosim
%{_libdir}/%{name}.so
%{_libdir}/libpy3neurosim.so

%files common
%license COPYING
%doc README.md

%if %{with mpich}
%files mpich
%{_libdir}/mpich/lib/%{name}.so.0
%{_libdir}/mpich/lib/%{name}.so.0.0.0
%{_libdir}/mpich/lib/libpy3neurosim.so.0
%{_libdir}/mpich/lib/libpy3neurosim.so.0.0.0

%files mpich-devel
%{_includedir}/mpich*/neurosim
%{_libdir}/mpich/lib/%{name}.so
%{_libdir}/mpich/lib/libpy3neurosim.so
%endif

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/lib/%{name}.so.0
%{_libdir}/openmpi/lib/%{name}.so.0.0.0
%{_libdir}/openmpi/lib/libpy3neurosim.so.0
%{_libdir}/openmpi/lib/libpy3neurosim.so.0.0.0

%files openmpi-devel
%{_includedir}/openmpi*/neurosim
%{_libdir}/openmpi/lib/%{name}.so
%{_libdir}/openmpi/lib/libpy3neurosim.so
%endif


%changelog
* Tue Oct 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-11.20181124.git0364674
- Fix build
- https://lists.fedoraproject.org/archives/list/scitech@lists.fedoraproject.org/thread/BNKLXKY4O7BOTZ7LH7XDUTQO6FG2UWUT/
- remove py2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20181124.git0364674
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20181124.git0364674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20181124.git0364674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20181124.git0364674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 0-6.20181124.git0364674
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20181124.git0364674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-4.20181124.git0364674
- Use bcond conditionals

* Sat Nov 24 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-3.20181124.git0364674
- Update to latest upstream commit
- Put libraries in correct locations. libpyneurosim is NOT a python extension module
- Remove python sub packages: other software must link against both libneurosim and libpyneurosim
- All explained in: https://github.com/INCF/libneurosim/issues/12

* Sun Oct 28 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-2.20181028.git7d074da
- Rebuild using conditional

* Thu Oct 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-1.20181025.git7d074da
- Place python so in correct location
- Correct devel file list

* Fri Oct 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-1.20181019.git57b76e2
- Correct release field
- Correct autosetup usage
- Move common files to -common sub package
- Explicitly version sonames
- Use tweaks suggested in review
- Make python3 default
- Enable debuginfo
- Update to latest upstream commit
- Initial build
