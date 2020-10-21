%undefine __cmake_in_source_build

Name:		yubihsm-shell
Version:	2.0.2
Release:	7%{?dist}
Summary:	Tools to interact with YubiHSM 2

License:	ASL 2.0 
URL:		https://github.com/Yubico/%{name}/
Source0:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:	gpgkey-C4686BFE.gpg
Patch1:		yubihsm-shell-2.0.2-gcc.patch

BuildRequires:	cmake
BuildRequires:	cppcheck
BuildRequires:	gcc
BuildRequires:	lcov
BuildRequires:	gengetopt
BuildRequires:	help2man
BuildRequires:	openssl-devel
BuildRequires:	libcurl-devel
BuildRequires:	libedit-devel
BuildRequires:	pcsc-lite-devel
BuildRequires:	clang
BuildRequires:	pkg-config
BuildRequires:	libusb-devel
BuildRequires:	chrpath
BuildRequires:	gnupg2

%description
This package contains most of the components used to interact with
the YubiHSM 2 at both a user-facing and programmatic level.

%package devel
Summary: Development tools for interacting with YubiHSM 2
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for working with yubihsm 2.

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch1 -p1


%build
# https://bugzilla.redhat.com/show_bug.cgi?id=1865658#c6
# The generated code fails to build on s390x in Fedora 33
# For now, disable this particular check when building this arch
%ifarch s390x
export CFLAGS="$CFLAGS -Wno-error=format-overflow"
%endif
%cmake
%cmake_build


%install
%cmake_install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubihsm-shell
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubihsm-wrap
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/pkcs11/yubihsm_pkcs11.so


%files
%license LICENSE
%{_bindir}/yubihsm-shell
%{_bindir}/yubihsm-wrap
%{_libdir}/libyubihsm.so.2
%{_libdir}/libyubihsm.so.2.*
%{_libdir}/libyubihsm_http.so.2
%{_libdir}/libyubihsm_http.so.2.*
%{_libdir}/libyubihsm_usb.so.2
%{_libdir}/libyubihsm_usb.so.2.*
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/yubihsm_pkcs11.so
%doc 
%{_mandir}/man1/yubihsm-shell.1.*
%{_mandir}/man1/yubihsm-wrap.1.*

%files devel
%{_libdir}/libyubihsm.so
%{_libdir}/libyubihsm_http.so
%{_libdir}/libyubihsm_usb.so
%{_includedir}/yubihsm.h
%dir %{_includedir}/pkcs11
%{_includedir}/pkcs11/pkcs11.h
%{_includedir}/pkcs11/pkcs11y.h
%{_datadir}/pkgconfig/yubihsm.pc



%changelog
* Thu Aug 06 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.2-7
- Workaround FTBFS on s390x (#1865658)

* Thu Aug 06 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.2-6
- Rebuild after libz3 soname bump (#1865658)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 16 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.2-3
- Avoid warnings/errors with new gcc on s390x (#1800289)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Jakub Jelen <jjelen@redhat.com> - 2.0.2-1
- New upstream release (#1772013)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Jakub Jelen <jjelen@redhat.com> - 2.0.1-1
- New upstream release (#1692935)

* Wed Feb 13 2019 Jakub Jelen <jjelen@redhat.com> - 2.0.0-4
- Workaround unreasonagle error from GCC9 (#1676257)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Jakub Jelen <jjelen@redhat.com> - 2.0.0-2
- Pull the latest signed tarballs
- Address review comments (#1654689)

* Thu Nov 29 2018 Jakub Jelen <jjelen@redhat.com> - 2.0.0-1
- Initial release


