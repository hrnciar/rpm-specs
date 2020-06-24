Name:		xrootd-ceph
Epoch:		1
Version:	4.11.3
Release:	1%{?dist}
Summary:	XRootD plug-in for interfacing with the Ceph storage platform

License:	LGPLv3+
URL:		https://github.com/xrootd/xrootd-ceph
Source0:	https://github.com/xrootd/xrootd-ceph/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	xrootd-server-devel
BuildRequires:	xrootd-private-devel
BuildRequires:	librados-devel
BuildRequires:	libradosstriper-devel

%if %{?fedora}%{!?fedora:0} >= 30
# Ceph is not available for 32 bit arches in Fedora 30+
ExcludeArch:	%{ix86} %{arm}
%endif

%description
The xrootd-ceph is an OSS layer plug-in for the XRootD server for interfacing
with the Ceph storage platform.

%prep
%setup -q

%build
mkdir build

pushd build
%cmake ..
%make_build
popd

%install
pushd build
%make_install
popd
rm %{buildroot}%{_libdir}/libXrdCephPosix.so

%ldconfig_scriptlets

%files
%{_libdir}/libXrdCeph-4.so
%{_libdir}/libXrdCephXattr-4.so
%{_libdir}/libXrdCephPosix.so.*
%license COPYING* LICENSE

%changelog
* Sat Mar 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.3-1
- Update to version 4.11.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.0-1
- Update to version 4.11.0

* Sun Jul 28 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.10.0-1
- xrootd-ceph split off to a separate source RPM
