Name:		libtelnet
Version:	0.21
Release:	18%{?dist}
Summary:	TELNET protocol parsing framework

License:	Public Domain
URL:		http://github.com/elanthis/libtelnet
Source0:	http://cloud.github.com/downloads/seanmiddleditch/libtelnet/libtelnet-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: zlib-devel
BuildRequires: doxygen

%description
Small library for parsing the TELNET protocol, responding to TELNET
commands via an event interface, and generating valid TELNET commands.

libtelnet includes support for the non-official MCCP, MCCP2, ZMP, and
MSSP protocols used by MUD servers and clients.

%package devel
Summary: Header files for libtelnet
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Header files for developing applications making use of libtelnet.

%package utils
Summary: TELNET utility programs from libtelnet
Requires: %{name} = %{version}-%{release}

%description utils
Provides three utilities based on the libtelnet library.
  * telnet-proxy - a TELNET proxy and debugging daemon
  * telnet-client - simple TELNET client
  * telnet-chatd - no-features chat server for testing TELNET clients.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf "$RPM_BUILD_ROOT"
make install INSTALL="install -p" DESTDIR="$RPM_BUILD_ROOT"
rm "$RPM_BUILD_ROOT%{_libdir}"/*.la

%ldconfig_scriptlets

%files
%doc README COPYING NEWS
%{_libdir}/*.so.*

%files devel
%doc %{_datadir}/man/man1/*.1.gz
%doc %{_datadir}/man/man3/*.3.gz
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files utils 
%{_bindir}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Sean Middleditch <sean@seanmiddleditch.com> - 0.21-3
- Update source URL for new upstream source location.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Sean Middleditch <sean@middleditch.us> - 0.21-1
- Update to libtelnet 0.21.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.20-3
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Sean Middleditch <sean@middleditch.us> 0.20-2
- Added BuildRequires on doxygen.

* Tue Sep 14 2010 Sean Middleditch <sean@middleditch.us> 0.20-1
- Update to libtelnet 0.20.

* Wed Oct 24 2009 Sean Middleditch <sean@middleditch.us> 0.12-1
- Update to libtelnet 0.12.
- Include libtelnet.pc in -devel package.

* Wed Aug 31 2009 Sean Middleditch <sean@middleditch.us> 0.11-1
- Update to libtelnet 0.11.
- Add BuildRequires on zlib-devel.
- Added INSTALL='install -p' to install script.
- Renamed -bin subpackage to -utils.
- Added COPYING and NEWS to main package document list.
- Removed document files from subpackages.

* Wed Aug 29 2009 Sean Middleditch <sean@middleditch.us> 0.10-2
- Corrected URL.
- Removed unnecessary Build-Requires.
- Fixed up use of defattr macro.
- Removed use of makeinstall macro.
- Merged the individual utility packages into a single libtelnet-bin package.

* Wed Jul 29 2009 Sean Middleditch <sean@middleditch.us> 0.10-1
- Initial RPM release.
