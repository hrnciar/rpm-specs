Name:           resolv_wrapper
Version:        1.1.6
Release:        1%{?dist}

Summary:        A wrapper for dns name resolving or dns faking
License:        BSD
Url:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        resolv_wrapper.keyring

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  libcmocka-devel
BuildRequires:  socket_wrapper

Recommends:     cmake
Recommends:     pkgconfig

%description
It is likely that if you have a server/client architecture, you need to do DNS
queries or a third party library, like Kerberos needs to be able to do queries.
In the case of Kerberos the client needs to look the address of the KDC up via a
SRV record. resolv_wrapper is able to either redirect all DNS queries to your
DNS server implementation, or fake DNS replies!

To use it set the following environment variables:

LD_PRELOAD=libresolv_wrapper.so
RESOLV_WRAPPER_CONF=./my_resolv.conf

This package doesn't have a devel package because this project is for
development/testing.

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p1

%build
if test ! -e "obj"; then
  mkdir obj
fi
pushd obj
%cmake \
  -DUNIT_TESTING=ON \
  %{_builddir}/%{name}-%{version}

make %{?_smp_mflags} VERBOSE=1
popd

%install
pushd obj
make DESTDIR=%{buildroot} install
popd

%ldconfig_scriptlets

%check
pushd obj
ctest --output-on-failure

LD_PRELOAD=src/libpam_wrapper.so bash -c '>/dev/null'
popd

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libresolv_wrapper.so*
%dir %{_libdir}/cmake/resolv_wrapper
%{_libdir}/cmake/resolv_wrapper/resolv_wrapper-config-version.cmake
%{_libdir}/cmake/resolv_wrapper/resolv_wrapper-config.cmake
%{_libdir}/pkgconfig/resolv_wrapper.pc
%{_mandir}/man1/resolv_wrapper.1*

%changelog
* Tue Mar 24 2020 Andreas Schneider <asn@redhat.com> - 1.1.6-8
- Update to version 1.1.6
  * https://gitlab.com/cwrap/resolv_wrapper/-/blob/master/CHANGELOG

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Jakub Hrozek <jhrozek@redhat.com> - 1.1.5-1
- Update to version 1.1.5
  * Support URI DNS records
  * Support PTR DNS records

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Andreas Schneider <asn@redhat.com> - 1.1.4-1
- Update to version 1.1.4
  * Added support for faking NS entries
  * Fixed some platform compatibility bugs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Andreas Schneider <asn@redhat.com> - 1.1.3-1
- Update to version 1.1.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 16 2014 Andreas Schneider <asn@redhat.com> - 1.1.0-2
- Add Requires for pkgconfig and cmake.

* Wed Dec 10 2014 Andreas Schneider <asn@redhat.com> - 1.1.0-1
- resolves: #1172534 - Initial package.
