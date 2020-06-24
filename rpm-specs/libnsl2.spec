%global commit0 4a062cf4180d99371198951e4ea5b4550efd58a3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


Name:       libnsl2
Version:    1.2.0
Release:    6.20180605git%{shortcommit0}%{?dist}
Summary:    Public client interface library for NIS(YP) and NIS+

License:    BSD and LGPLv2+
URL:        https://github.com/thkukuk/libnsl


Source0:    https://github.com/thkukuk/libnsl/archive/%{commit0}.tar.gz#/libnsl-%{commit0}.tar.gz

Patch0: libnsl2-1.0.5-include_stdint.patch

BuildRequires: autoconf, automake, gettext-devel, libtool, libtirpc-devel

%description
This package contains the libnsl library. This library contains
the public client interface for NIS(YP) and NIS+.
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.

%package devel
Summary: Development files for libnsl
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: glibc-devel < 2.26.9000-40

%description devel
Development files for libnsl2


%prep
%setup -q -n libnsl-%{commit0}

%patch0 -p1 -b .include_stdint

%build

export CFLAGS="%{optflags}"

autoreconf -fiv

%configure\
    --libdir=%{_libdir}\
    --includedir=%{_includedir}

%make_build


%install

%make_install

rm %{buildroot}/%{_libdir}/libnsl.a
rm %{buildroot}/%{_libdir}/libnsl.la

%files
%{_libdir}/libnsl.so.2
%{_libdir}/libnsl.so.2.0.0

%license COPYING

%files devel
%{_libdir}/libnsl.so
%{_includedir}/*
%{_libdir}/pkgconfig/libnsl.pc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 James Antill <james.antill@redhat.com>
- Remove ldconfig scriptlet, now done via. transfiletrigger in glibc (#1644073).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Matej Mužila <mmuzila@redhat.com> - 1.2.0-2.20181605git4a062cf
- Update to 1.2.0-2.20181605git4a062cf
  Resolves: rhbz#1573895

* Fri Feb 09 2018 Matej Mužila <mmuzila@reedhat.com> - 1.2.0-1
- Update to version 1.2.0
- Change libdir and includedir

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Matej Mužila <mmuzila@redhat.com> 1.1.0-1
- Update to version 1.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Matej Mužila <mmuzila@redhat.com> 1.0.5-1
- Update to version 1.0.5
- Fix missing stdint.h

* Mon Apr 10 2017 Matej Mužila <mmuzila@redhat.com> 1.0.4-4
- Initial version for 1.0.4

