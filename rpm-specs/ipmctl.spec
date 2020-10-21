Name:		ipmctl
Version:	02.00.00.3825
Release:	2%{?dist}
Summary:	Utility for managing Intel Optane DC persistent memory modules
License:	BSD
URL:		https://github.com/intel/ipmctl
Source:		https://github.com/intel/ipmctl/archive/v%{version}/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1628752
ExclusiveArch:	x86_64

Requires:	libipmctl%{?_isa} = %{version}-%{release}
BuildRequires:	pkgconfig(libndctl)
BuildRequires:	cmake
BuildRequires:	python3
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	asciidoctor
BuildRequires:	systemd
Obsoletes:	ixpdimm-cli < 01.00.00.3000

Patch0: gcc-lto.patch
Patch1: ipmctl-gcc11.patch

%description
Utility for managing Intel Optane DC persistent memory modules
Supports functionality to:
Discover DCPMMs on the platform.
Provision the platform memory configuration.
View and update the firmware on DCPMMs.
Configure data-at-rest security on DCPMMs.
Track health and performance of DCPMMs.
Debug and troubleshoot DCPMMs.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%package -n libipmctl
Summary:	Library for Intel DCPMM management
Obsoletes:	ixpdimm_sw < 01.00.00.3000
Obsoletes:	libixpdimm-common < 01.00.00.3000
Obsoletes:	libixpdimm-core < 01.00.00.3000
Obsoletes:	libixpdimm-cli < 01.00.00.3000
Obsoletes:	libixpdimm-cim < 01.00.00.3000
Obsoletes:	libixpdimm < 01.00.00.3000
Obsoletes:	ixpdimm-data < 01.00.00.3000

%description -n libipmctl
An Application Programming Interface (API) library for managing Intel Optane DC
persistent memory modules.

%package -n libipmctl-devel
Summary:	Development packages for libipmctl
Requires:	libipmctl%{?_isa} = %{version}-%{release}
Obsoletes:	ixpdimm-devel < 01.00.00.3000
Obsoletes:	ixpdimm_sw-devel < 01.00.00.3000

%description -n libipmctl-devel
API for development of Intel Optane DC persistent memory management utilities.

%build
%cmake -DBUILDNUM=%{version} -DCMAKE_INSTALL_PREFIX=/ \
    -DLINUX_PRODUCT_NAME=%{name} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
    -DCMAKE_INSTALL_BINDIR=%{_bindir} \
    -DCMAKE_INSTALL_DATAROOTDIR=%{_datarootdir} \
    -DCMAKE_INSTALL_MANDIR=%{_mandir} \
    -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir} \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -DRELEASE=ON \
    -DRPM_BUILD=ON
%cmake_build

%install
%{!?_cmake_version: cd build}
%cmake_install

%post -n libipmctl -p /sbin/ldconfig

%postun -n libipmctl -p /sbin/ldconfig

%files -n ipmctl
%{_bindir}/ipmctl
%{_mandir}/man1/ipmctl*

%files -n libipmctl
%{_libdir}/libipmctl.so.4*
%dir %{_datadir}/doc/ipmctl
%doc %{_datadir}/doc/ipmctl/ipmctl_default.conf
%doc %{_datadir}/doc/ipmctl/LICENSE
%config(noreplace) %{_datadir}/ipmctl/ipmctl.conf
%dir %{_localstatedir}/log/ipmctl
%config(noreplace) %{_sysconfdir}/logrotate.d/ipmctl

%files -n libipmctl-devel
%{_libdir}/libipmctl.so
%{_includedir}/nvm_types.h
%{_includedir}/nvm_management.h
%{_includedir}/export_api.h
%{_includedir}/NvmSharedDefs.h
%{_libdir}/pkgconfig/libipmctl.pc

%changelog
* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 02.00.00.3825-2
- Fix mismatched array sizes for argument to os_mkdir caught by gcc-11

* Wed Sep 30 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3825-1
- Release 02.00.00.3825

* Sun Aug 30 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3809-2
- Change to use cmake macros

* Sun Aug 30 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3809-1
- Release 02.00.00.3809

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 02.00.00.3791-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 02.00.00.3791-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Juston Li <juston.li@intel.com> - 02.00.00.3791-1
- Release 02.00.00.3791

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 02.00.00.3764-2
- Fix latent type mismatch problem exposed by LTO

* Fri May 01 2020 Juston Li <juston.li@intel.com> - 02.00.00.3764-1
- Release 02.00.00.3764

* Fri Apr 24 2020 Juston Li <juston.li@intel.com> - 02.00.00.3759-1
- Inital 2.x Release 02.00.00.3759
- Removed ipmctl-monitor
- Removed libsafec dependency

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 01.00.00.3474-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed May 02 2018 Juston Li <juston.li@intel.com> - 01.00.00.3000-1
- initial spec
