Name:           rudesocket
Version:        1.3.0
Release:        26%{?dist}
Summary:        Library (C++ API) for creating client sockets

License:        GPLv2+
URL:            http://www.rudeserver.com/socket
Source0:        http://homeless.fedorapeople.org/rudesocket/rudesocket-%{version}.tar.bz2
Patch0:         rudesocket-1.3.0-leak-connection.patch
Patch1:         rudesocket-1.3.0-timeout.patch

# autoreconf
BuildRequires:  gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

BuildRequires:  openssl-devel
Requires:       openssl

%description
rudesocket is a library provides client socket services to an application.
In addition to normal and SSL TCP connections, it supports 
proxies, SOCK4 and SOCKS5 servers. Furthermore, it allows you 
to chain proxies together.

%package        devel
Summary:        Development files for rudesocket
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
rudesocket is a library provides client socket services to an application.
In addition to normal and SSL TCP connections, it supports 
proxies, SOCK4 and SOCKS5 servers. Furthermore, it allows you 
to chain proxies together. The rudesocket-devel package 
contains libraries, header files, and documentation needed 
to develop C++ applications using rudesocket. 

%prep
%setup -q
%patch0 -p1 -b .leak
%patch1 -p1 -b .timeout

%build
autoreconf --verbose --force --install
%configure --disable-static --with-openssl
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README NEWS ChangeLog
%{_libdir}/*.so.*

%files devel
%doc 
%dir %{_includedir}/rude
%{_includedir}/rude/socket.h
%{_libdir}/*.so
%{_mandir}/man3/*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-16
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Jiri Popelka <jpopelka@redhat.com> - 1.3.0-12
- Run autoreconf prior to running configure (#926464)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Jiri Popelka <jpopelka@redhat.com> - 1.3.0-9
- fix hardcoded timeout and connection leaking (#665658)
- clean up spec file

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.3.0-6
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com>
- 1.3.0-3
- rebuild with new openssl

* Wed Feb 06 2008 Matt Flood <matt@rudeserver.com>
- 1.3.0-2
- Added missing include statement

* Wed Feb 06 2008 Matt Flood <matt@rudeserver.com>
- 1.3.0-1
- Replaced std c includes with c++ style includes

* Tue Jan 29 2008 Matt Flood <matt@rudeserver.com>
- 1.2.0-1
- Modified source code to facilitate windows builds
- Instead of configuring build to use openssl by default, 
  it now requires ./configure --with-openssl to include 
  openssl functionality

* Tue Jan 08 2008 Matt Flood <matt@rudeserver.com>
- 1.1.0-3
- Minor changes to build scripts

* Tue May 29 2007 Matt Flood <matt@rudeserver.com>
- 1.1.0-2
- Added Man Page
- Minor changes to build scripts

* Thu Apr 10 2006 Matt Flood <matt@rudeserver.com>
- 1.1.0-1
- First RPM Release

