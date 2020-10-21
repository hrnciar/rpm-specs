Name:           lpcnetfreedv
Version:        0.2
Release:        4%{?dist}
Summary:        LPCNet for FreeDV

License:        BSD
URL:            https://github.com/drowe67/LPCNet
Source0:        https://github.com/drowe67/LPCNet/archive/v%{version}/LPCNet-%{version}.tar.gz
Source1:        http://rowetel.com/downloads/deep/lpcnet_191005_v1.0.tgz

# Fixes for aarch64 which has NEON instructions natively
Patch0:         lpcnetfreedv-vector-updates.patch
# Make library private for FreeDV
Patch1:         lpcnetfreedv-private_libs.patch

BuildRequires:  cmake gcc
BuildRequires:  codec2-devel

%description
Experimental version of LPCNet that has been used to develop FreeDV 2020 - a HF
radio Digial Voice mode for over the air experimentation with Neural Net speech
coding. Possibly the first use of Neural Net speech coding in real world
operation.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Development files and tools for LPCNet

%description devel
%{summary}.


%prep
%autosetup -p1 -n LPCNet-%{version}


%build
# Add model data archive to the build directory so CMake finds it.
mkdir -p %{_vpath_builddir}
cp %{SOURCE1} %{_vpath_builddir}/

# We need to force optimizations to specific values since the build system and
# host system will likely be different.
%ifarch i686 x86_64
    %global _cpuopt "-DAVX=TRUE"
%endif
%ifarch armv7hl
    %global _cpuopt "-DNEON=TRUE"
%endif
%ifarch aarch64 ppc64le s390x
    # NEON instructions are native in arm64.
    %global _cpuopt ""
%endif

%cmake -DDISABLE_CPU_OPTIMIZATION=TRUE %{_cpuopt}
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc README.md
%{_libdir}/%{name}/lib%{name}.so

%files devel
%{_bindir}/*
%{_includedir}/lpcnet/
%{_libdir}/cmake/lpcnetfreedv/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Richard Shaw <hobbes1069@gmail.com> - 0.2-2
- Update per reviewer comments.
- Renamed package to lpcnetfreedv (same as library), repo will be renamed in
  the near future.
- Made library private as it is essentially a plugin for freedv.

* Mon Apr 20 2020 Richard Shaw <hobbes1069@gmail.com> - 0.2-1
- Initial packaging.
