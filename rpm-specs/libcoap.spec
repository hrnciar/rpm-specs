#global candidate rc4

Name:     libcoap
Version:  4.2.1
Release:  1%{?candidate:.%{candidate}}%{?dist}
Summary:  C library implementation of CoAP
URL:      https://libcoap.net/
# If build against gnutls the license is BSD + LGPL 2.1
License:  BSD

Source0:  https://github.com/obgm/libcoap/archive/v%{version}.tar.gz#/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: asciidoc
BuildRequires: ctags
BuildRequires: doxygen
BuildRequires: graphviz

%description
The Constrained Application Protocol (CoAP) is a specialized web transfer 
protocol for use with constrained nodes and constrained networks in the Internet 
of Things. The protocol is designed for machine-to-machine (M2M) applications 
such as smart energy and building automation.

libcoap implements a lightweight application-protocol for devices with 
constrained resources such as computing power, RF range, memory, bandwidth,
or network packet sizes. This protocol, CoAP, was standardized in the IETF
working group "CoRE" as RFC 7252.

%package  utils
Summary:  Client and server CoAP utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for working with %{name}.

%package  devel
Summary:  Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package  doc
Summary:  Documentation package for %{name}
BuildArch: noarch

%description doc
Documentation for development with %{name}.

%prep
%autosetup -n %{name}-%{version}%{?candidate:-%{candidate}}

%build
autoreconf -vif
%configure --without-debug CFLAGS="$RPM_OPT_FLAGS -D COAP_DEBUG_FD=stderr" \
           --enable-examples --enable-documentation --enable-doxygen --enable-manpages \
           --enable-dtls --with-openssl --disable-static

%make_build

%install
%make_install

#Remove libtool archives
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license LICENSE COPYING
%doc AUTHORS
%{_libdir}/libcoap-2-openssl.so.2*

%files utils
%{_bindir}/coap*
%{_mandir}/man5/coap*

%files doc
%{_mandir}/man7/coap*
%{_datadir}/doc/libcoap/

%files devel
%{_mandir}/man3/coap*
%{_includedir}/coap2/
%{_libdir}/pkgconfig/libcoap-2*.pc
%{_libdir}/libcoap-2-openssl.so

%changelog
* Mon Feb 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.2.0-1
- Update to 4.2.0 GA stable release

* Sat Feb  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 4.2.0-0.1.rc4
- Update to 4.2.0 rc4

* Sat Jul  1 2017 Peter Robinson <pbrobinson@fedoraproject.org> 4.1.2-2
- Minor package review updates

* Fri Apr 21 2017 Peter Robinson <pbrobinson@fedoraproject.org> 4.1.2-1
- Initial package
