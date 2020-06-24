Summary:        Open Programmable Acceleration Engine (OPAE) SDK
Name:           opae
Version:        1.4.1
Release:        5%{?dist}
License:        BSD and MIT
ExclusiveArch:  x86_64
URL:            https://github.com/OPAE/%{name}-sdk
Source0:        https://github.com/OPAE/opae-sdk/releases/download/%{version}-1/%{name}-%{version}-1.tar.gz
Patch01:        0001-Do-not-install-static-libraries.patch
Patch02:        improve-library-link.patch

BuildRequires:  gcc, gcc-c++
BuildRequires:  cmake, make
BuildRequires:  python3-devel
BuildRequires:  json-c-devel
BuildRequires:  libuuid-devel
BuildRequires:  rpm-build
BuildRequires:  hwloc-devel
BuildRequires:  doxygen

%description
Open Programmable Acceleration Engine (OPAE) is a software framework
for managing and accessing programmable accelerators (FPGAs).
Its main parts are:

* OPAE Software Development Kit (OPAE SDK) (this package)
* OPAE Linux driver for Intel(R) Xeon(R) CPU with
  Integrated FPGAs and Intel(R) PAC with Arria(R) 10 GX FPGA
* Basic Building Block (BBB) library for accelerating AFU

OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.
It provides a library implementing the OPAE C API for presenting a
streamlined and easy-to-use interface for software applications to
discover, access, and manage FPGA devices and accelerators using
the OPAE software stack.

%package devel
Summary:    OPAE headers, sample source, and documentation
Requires:   libuuid-devel, %{name}%{?_isa} = %{version}-%{release}

%description devel
OPAE headers, tools, sample source, and documentation

%prep
%setup -q -n %{name}-%{version}-1
%patch01 -p1
%patch02 -p1

# Remove hidden .clang-format
rm opae-libs/tests/xfpga/.clang-format
rm tests/.clang-format
rm tools/argsfilter/.clang-format

%build
mkdir -p _build
cd _build
%cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DOPAE_PRESERVE_REPOS=ON
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/opae
cp ./RELEASE_NOTES.md %{buildroot}%{_datadir}/opae/RELEASE_NOTES.md
cp ./LICENSE %{buildroot}%{_datadir}/opae/LICENSE
cp ./COPYING %{buildroot}%{_datadir}/opae/COPYING

# cmake modules
mkdir -p %{buildroot}%{_usr}/src/opae/cmake/modules
for s in FindSphinx.cmake
do
  cp "cmake/${s}" %{buildroot}%{_usr}/src/opae/cmake/
done
mkdir -p %{buildroot}%{_usr}/src/opae/opae-libs/cmake/modules
for s in FindHwloc.cmake \
         OPAE.cmake \
         FindUUID.cmake \
         Findjson-c.cmake \
         OPAECompiler.cmake \
         OPAEGit.cmake \
         OPAEPackaging.cmake 
do
  cp "opae-libs/cmake/modules/${s}" %{buildroot}%{_usr}/src/opae/opae-libs/cmake/modules
done

# Samples
mkdir -p %{buildroot}%{_usr}/src/opae/samples
mkdir -p %{buildroot}%{_usr}/src/opae/samples/hello_fpga/
cp samples/hello_fpga/hello_fpga.c %{buildroot}%{_usr}/src/opae/samples/hello_fpga/

%make_install -C _build

%files
%dir %{_datadir}/opae
%doc %{_datadir}/opae/RELEASE_NOTES.md
%license %{_datadir}/opae/LICENSE
%license %{_datadir}/opae/COPYING
%{_libdir}/libbitstream.so.%{version}
%{_libdir}/libbitstream.so.1
%{_libdir}/libopae-c.so.%{version}
%{_libdir}/libopae-c.so.1
%{_libdir}/libopae-c-ase.so.%{version}
%{_libdir}/libopae-c-ase.so.1
%{_libdir}/libopae-cxx-core.so.%{version}
%{_libdir}/libopae-cxx-core.so.1

%files devel
%dir %{_includedir}/opae
%dir %{_libdir}/opae
%dir %{_usr}/src/opae
%dir %{_usr}/src/opae/cmake/
%dir %{_usr}/src/opae/opae-libs/cmake/modules/
%dir %{_usr}/src/opae/samples
%{_bindir}/fpgaconf
%{_bindir}/fpgainfo
%{_bindir}/mmlink
%{_bindir}/userclk
%{_bindir}/hello_fpga
%{_bindir}/hello_cxxcore
%{_bindir}/afu_json_mgr
%{_bindir}/packager
%{_includedir}/opae/*
%{_libdir}/libbitstream.so
%{_libdir}/libopae-c.so
%{_libdir}/libopae-c-ase.so
%{_libdir}/libopae-cxx-core.so
%{_libdir}/opae/libxfpga.so
%{_libdir}/opae/libmodbmc.so
%{_libdir}/opae/libboard_rc.so
%{_libdir}/opae/libboard_vc.so
%{_usr}/share/opae/*
%{_usr}/src/opae/samples/hello_fpga/hello_fpga.c
%{_usr}/src/opae/cmake/*
%{_usr}/src/opae/opae-libs/cmake/modules/*

%changelog
* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.4.1-5
- Rebuild (json-c)

* Tue Apr 21 2020 Tom Rix <trix@redhat.com> 1.4.1-4
- Update the sources file

* Tue Apr 21 2020 Tom Rix <trix@redhat.com> 1.4.1-3
- Update the sources file

* Mon Apr 20 2020 Tom Rix <trix@redhat.com> 1.4.1-2
- Disable broken documents
- Do not install static libs
- Improve linking of libopae-cxx-core

* Fri Apr 17 2020 Korde Nakul <nakul.korde@intel.com> 1.4.1-1
- OPAE git repository layout changes.
- Removed Safe String module dependency.
- Various bug fixes.
- Ported python tools to python3.6.
- Various Static code scan bug fixes.
- Removed pybind11 3rd component from OPAE source repository.

* Tue Mar 10 2020 Tom Rix <trix@redhat.com> 1.4.0-6
- Add make as a dependency

* Fri Mar 6 2020 Tom Rix <trix@redhat.com> 1.4.0-5
- Use make_install macro
- Use license tag correctly

* Tue Mar 3 2020 Tom Rix <trix@redhat.com> 1.4.0-4
- Add libraries to link of libopae-cxx-core libopae-c++-utils
- Remove unneeded build flag _smp_mflags

* Thu Feb 27 2020 Tom Rix <trix@redhat.com> 1.4.0-3
- Remove ldconfig from post and postun
- Append dist tag to release tag
- Change libsafestr to shared library
- Set license tag to location of license files
- Remove phython3-sphnix build dependency.
- Consolidate samples,tools,tools-extra pkgs into devel
- Improve pkg created dir specification
- Set x86_64 as ExclusiveArch
- Change to runtime to implicit dependency on build *-devel
- Remove preun rm of opae-c.conf
- Use systemd rpm macros
- Add _smp_mflags to build
- Use unitdir for fpgad.service path
- Distribute the license and copying files

* Mon Feb 24 2020 Tom Rix <trix@redhat.com> 1.4.0-2
- Change to python3
- Remove release tag from upstream Source0 definition.
- Improve requires tag for subpackages
- Remove explicit root owner
- Remove vendor tag
- Remove group tag
- Remove clean section

* Tue Dec 17 2019 Korde Nakul <nakul.korde@intel.com> 1.4.0-1
- Added support to FPGA Linux kernel Device Feature List (DFL) driver patch set2.
- Increased test cases and test coverage
- Various bug fixes
- Various compiler warning fixes
- Various memory leak fixes
- Various Static code scan bug fixes
- Added new FPGA MMIO API to write 512 bits
