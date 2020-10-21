
%global _hardened_build		1

Name:		nfdump
Version:	1.6.21
Release:	1%{?dist}
Summary:	NetFlow collecting and processing tools

License:	BSD and GPLv2+
URL:		https://github.com/phaag/nfdump
Source0:	https://github.com/phaag/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	bzip2-devel
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	rrdtool-devel
BuildRequires:	sed

Requires:	nfdump-libs = %{version}-%{release}


%description
Nfdump is a set of tools to collect and process NetFlow data. It's fast and has
a powerful filter pcap like syntax. It supports NetFlow versions v1, v5, v7, v9
and IPFIX as well as a limited set of sflow. It includes support for CISCO ASA
(NSEL) and CISCO NAT (NEL) devices which export event logging records as v9
flows. Nfdump is fully IPv6 compatible.

%package libs
Summary:	Libraries used by NFDUMP packages

%description libs
Contains libraries used by NFDUMP utilities


%prep
%setup -q

%build
# prepare build script
./bootstrap

export LDFLAGS="${LDFLAGS} -fPIC"

%configure \
    --enable-nsel \
    --enable-nfprofile \
    --enable-nftrack \
    --enable-sflow \
    --enable-readpcap \
    --enable-nfpcapd \
    --enable-shared \
    --disable-static

# removing rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# disable parallel build to get proper linking order
make

%install
make install DESTDIR=%{buildroot}
chmod 0644 AUTHORS ChangeLog README.md
rm -f %{buildroot}%{_libdir}/*.la


%ldconfig_scriptlets libs


%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_bindir}/*
%{_mandir}/man1/*.1*

%files libs
%{_libdir}/libnfdump-%{version}.so
%{_libdir}/libnfdump.so


%changelog
* Tue Aug 11 2020 Denis Fateyev <denis@fateyev.com> - 1.6.21-1
- Update to version 1.6.21

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Denis Fateyev <denis@fateyev.com> - 1.6.20-1
- Update to version 1.6.20

* Fri Feb 28 2020 Denis Fateyev <denis@fateyev.com> - 1.6.19-1
- Update to version 1.6.19

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Denis Fateyev <denis@fateyev.com> - 1.6.18-1
- Update to version 1.6.18

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Denis Fateyev <denis@fateyev.com> - 1.6.17-1
- Update to version 1.6.17

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 29 2016 Denis Fateyev <denis@fateyev.com> - 1.6.15-2
- Remove extra debug output option

* Sat Jun 11 2016 Denis Fateyev <denis@fateyev.com> - 1.6.15-1
- Update to version 1.6.15

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Denis Fateyev <denis@fateyev.com> - 1.6.13-1
- Update to version 1.6.13

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 Denis Fateyev <denis@fateyev.com> - 1.6.12-1
- Update to version 1.6.12

* Wed Feb 05 2014 Denis Fateyev <denis@fateyev.com> - 1.6.11-1
- Initial Fedora RPM release
