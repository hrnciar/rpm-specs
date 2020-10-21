Name:           libcacard
Version:        2.8.0
Release:        1%{?dist}
Summary:        CAC (Common Access Card) library
License:        LGPLv2+
URL:            https://gitlab.freedesktop.org/spice/libcacard
Source0:        http://www.spice-space.org/download/libcacard/%{name}-%{version}.tar.xz
Source1:        http://www.spice-space.org/download/libcacard/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-E37A484F.gpg
# https://gitlab.freedesktop.org/spice/libcacard/-/merge_requests/24
Patch0:         libcacard-2.8.0-32bit.patch
Epoch:          3

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  nss-devel
BuildRequires:  softhsm
BuildRequires:  opensc
BuildRequires:  gnutls-utils
BuildRequires:  nss-tools
BuildRequires:  openssl
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pcsc-lite-devel
Conflicts:      qemu-common < 2:2.5.0

%description
This library provides emulation of smart cards to a virtual card
reader running in a guest virtual machine.

It implements DoD CAC standard with separate pki containers
(compatible coolkey), using certificates read from NSS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch0 -p1

%build
%meson
%meson_build

%check
# Do not run the tests on s390x, which fails
%ifnarch s390x
%meson_test
%endif

%install
%meson_install
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/libcacard.so.*

%files devel
%{_includedir}/cacard
%{_libdir}/libcacard.so
%{_libdir}/pkgconfig/libcacard.pc

%changelog
* Tue Oct 06 2020 Jakub Jelen <jjelen@redhat.com> - 2.8.0-1
- New upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Jakub Jelen <jjelen@redhat.com> - 2.7.0-3
- Backport an upstream patch to unbreak testing

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Christophe Fergeau <cfergeau@redhat.com> - 2.6.1-1
- Update to new upstream release

* Wed Aug  8 2018 Marc-André Lureau <marcandre.lureau@redhat.com> - 3:2.6.0-1
- Update to release v2.6.0
- remove vscclient, drop libcacard-tools

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Marc-André Lureau <marcandre.lureau@redhat.com> - 3:2.5.3-1
- new upstream release 2.5.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3:2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  8 2015 Marc-André Lureau <marcandre.lureau@redhat.com> - 3:2.5.2-1
- Update to latest libcacard's release (2.5.2)

* Wed Nov 25 2015 Fabiano Fidêncio <fidencio@redhat.com> - 3:2.5.1-1
- Update to latest libcacard's release (2.5.1)

* Wed Sep 23 2015 Marc-André Lureau <marcandre.lureau@redhat.com> - 3:2.5.0-1
- Initial standalone libcacard package.
