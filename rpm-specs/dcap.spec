Name:		dcap
Version:	2.47.12
Release:	10%{?dist}
Summary:	Client Tools for dCache

#		plugins/gssapi/{base64.[ch],gssIoTunnel.c,util.c} - BSD license
#		the rest - LGPLv2+ license
License:	LGPLv2+ and BSD
URL:		http://www.dcache.org/manuals/libdcap.shtml
Source0:	https://github.com/dCache/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#		Fix autoconf for EPEL 6
#		https://github.com/dCache/dcap/pull/17
Patch0:		%{name}-am-prog-ar.patch
#		Missing function declaration
#		https://github.com/dCache/dcap/pull/18
Patch1:		%{name}-missing-declaration.patch

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:	globus-gssapi-gsi-devel
BuildRequires:	krb5-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	CUnit-devel

%description
dCache is a distributed mass storage system.
This package contains the client tools.

%package libs
Summary:	Client Libraries for dCache
License:	LGPLv2+

%description libs
dCache is a distributed mass storage system.
This package contains the client libraries.

%package devel
Summary:	Client Development Files for dCache
License:	LGPLv2+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
dCache is a distributed mass storage system.
This package contains the client development files.

%package tunnel-gsi
Summary:	GSI tunnel for dCache
License:	LGPLv2+ and BSD
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-gsi
This package contains the gsi tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-krb
Summary:	Kerberos tunnel for dCache
License:	LGPLv2+ and BSD
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-krb
This package contains the kerberos tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-ssl
Summary:	SSL tunnel for dCache
License:	LGPLv2+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-ssl
This package contains the ssl tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-telnet
Summary:	Telnet tunnel for dCache
License:	LGPLv2+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-telnet
This package contains the telnet tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./bootstrap.sh

%configure \
    --disable-static \
    --with-tunneldir=%{_libdir}/%{name} \
    --with-globus-include=%{_includedir}/globus \
    --with-globus-lib=/dummy
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove libtool archive files
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/%{name}/*.la

# We are installing the docs in the files sections
rm -rf %{buildroot}/%{_docdir}

%check
make %{?_smp_mflags} check

%ldconfig_scriptlets libs

%files
%{_bindir}/dccp
%{_mandir}/man1/dccp.1*

%files libs
%{_libdir}/libdcap.so.*
%{_libdir}/libpdcap.so.*
%dir %{_libdir}/%{name}
%license LICENSE COPYING.LIB AUTHORS

%files devel
%{_libdir}/libdcap.so
%{_libdir}/libpdcap.so
%{_includedir}/dc_hack.h
%{_includedir}/dcap.h
%{_includedir}/dcap_errno.h

%files tunnel-gsi
%{_libdir}/%{name}/libgsiTunnel.so
%license plugins/gssapi/Copyright

%files tunnel-krb
%{_libdir}/%{name}/libgssTunnel.so
%license plugins/gssapi/Copyright

%files tunnel-ssl
%{_libdir}/%{name}/libsslTunnel.so

%files tunnel-telnet
%{_libdir}/%{name}/libtelnetTunnel.so

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.47.12-6
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.12-4
- Fix an implicit declaration warning

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.47.12-2
- Rebuilt for switch to libxcrypt

* Sat Nov 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.12-1
- New upstream release

* Wed Oct 25 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.11-1
- New upstream release
- Drop patches (previously backported)
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Sat Aug 12 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.10-9
- Don't use deprecated TLSv1_client_method

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 15 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.10-5
- Rebuild for OpenSSL 1.1.0 (Fedora 26)
- Fix more compiler warnings

* Wed Sep 14 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.10-4
- Backport fixes from upstream

* Thu Mar 10 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.10-3
- Fix broken postun scriptlet in dcap-libs

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.10-1
- New upstream release
- Drop patch dcap-dlopen.patch - merged upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.9-1
- New upstream release
- Enable tests and add BR CUnit-devel (except EPEL 5)
- Adapt to new license packaging guidelines

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.8-1
- New upstream release
- Drop patch dcap-segfault.patch - merged upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.7-3
- Fix segfault

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.7-1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.6-2
- Remove encoding fixes

* Thu May 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.6-1
- New upstream release (EMI 2 release)
- Drop patches dcap-aliasing.patch and dcap-libs.patch implemented upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 11 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 06 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.5-1
- New upstream release
- Drop dcap-docs.patch - implemented upstream
- Put CFLAGS back to default - the issue causing problem is fixed upstream

* Thu Jun 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.2-2
- Adjust CFLAGS so that the compiled program works correctly

* Wed Apr 07 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.2-1
- New upstream release
- Drop dcap-adler32.patch - implemented upstream

* Thu Mar 11 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.44.0-3
- Add missing build requires on autotools
- Fix configure to look for functions in the right libraries

* Wed Mar 10 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.44.0-2
- Use the adler32 function from zlib and drop the bundled source file
- Drop the zlib license tag again

* Wed Mar 10 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.44.0-1
- Major revision of spec file - upstream has started using autotools
- Add zlib license tag due to the adler32 source

* Sun Jan  3 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.44-2
- Porting to additional architectures
- Add BSD license tags for the tunnel-gsi and tunnel-krb sub packages

* Thu Dec 17 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.44-1
- Update to version 1.2.44 (svn tag 1.9.3-7)

* Thu Sep 17 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.42-2
- Update to new svn tag 1.9.3-3

* Thu Aug 13 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.42-1
- Initial Fedora package based on svn tag 1.9.3-1
