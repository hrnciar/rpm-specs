Name:		ipmctl
Version:	02.00.00.3764
Release:	1%{?dist}
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
Obsoletes:	ixpdimm-cli < 01.00.00.3000

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
%make_build

%install
%{!?_cmake_version: cd build}
%make_install -f Makefile

%post -n libipmctl -p /sbin/ldconfig

%postun -n libipmctl -p /sbin/ldconfig

%files -n ipmctl
%{_bindir}/ipmctl
%{_mandir}/man1/ipmctl*

%files -n libipmctl
%{_libdir}/libipmctl.so.4*
%dir %{_datadir}/doc/ipmctl
%doc %{_datadir}/doc/ipmctl/ipmctl_default.conf
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
* Fri May 01 2020 Juston Li <juston.li@intel.com> - 02.00.00.3764-1
- Release 02.00.00.3764

* Fri Apr 24 2020 Juston Li <juston.li@intel.com> - 02.00.00.3759-1
- Inital 2.x Release 02.00.00.3759
- Removed ipmctl-monitor
- Removed libsafec dependency

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 01.00.00.3474-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Juston Li <juston.li@intel.com> - 01.00.00.3474-1
- Release 01.00.00.3474

* Wed May 02 2018 Juston Li <juston.li@intel.com> - 01.00.00.3000-1
- initial spec
