Summary:        Library with simple API for communication with LXI devices
Name:           liblxi
Version:        1.13
Release:        6%{?dist}
# src/vxi11core* and src/include/vxi11core* are EPICS, rest is BSD
License:        BSD and EPICS
URL:            https://lxi-tools.github.io/
Source0:        https://github.com/lxi/liblxi/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxi/liblxi/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1.gpg
BuildRequires:  gcc
BuildRequires:  %{_bindir}/rpcgen
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
BuildRequires:  libtirpc-devel
%endif
BuildRequires:  avahi-devel
BuildRequires:  libxml2-devel
BuildRequires:  gnupg2

%description
The LXI library (liblxi) is an open source software library for GNU/Linux
systems which offers a simple API for communicating with LXI enabled
instruments. The API allows applications to easily discover instruments on
networks and communicate SCPI commands.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/lxi.h
%{_mandir}/man3/lxi_*.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Robert Scheck <robert@fedoraproject.org> 1.13-1
- Upgrade to 1.13 (#1556050)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Robert Scheck <robert@fedoraproject.org> 1.7-1
- Upgrade to 1.7

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.3-1
- Upgrade to 1.3

* Sat Oct 28 2017 Robert Scheck <robert@fedoraproject.org> 1.2-1
- Upgrade to 1.2

* Sun Oct 08 2017 Robert Scheck <robert@fedoraproject.org> 1.0-2
- Run /sbin/ldconfig (#1499559, thanks to Robert-André Mauchin)

* Sun Oct 08 2017 Robert Scheck <robert@fedoraproject.org> 1.0-1
- Upgrade to 1.0
- Initial spec file for Fedora and Red Hat Enterprise Linux
