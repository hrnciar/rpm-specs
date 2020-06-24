Name:           mktorrent
Version:        1.1
Release:        5%{?dist}
Summary:        Command line utility to create BitTorrent metainfo files

License:        GPLv2+
URL:            https://github.com/Rudde/mktorrent
Source0:        https://github.com/Rudde/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  openssl-devel

%description
Command line utility to create BitTorrent metainfo files.
See --help option for mktorrent command for details on usage.

%prep
%setup -q
# Use openssl sha1 routine rather than included one.
rm sha1.c sha1.h

%build
%ifarch alpha ia64 ppc64 s390x sparc64 x86_64
%global largefiles 0
%else
%global largefiles 1
%endif

make %{?_smp_mflags} USE_LARGE_FILES=%{largefiles}  USE_PTHREADS=1 \
       USE_OPENSSL=1 USE_LONG_OPTIONS=1  CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
make install USE_LARGE_FILES=%{largefiles}  USE_PTHREADS=1 \
       USE_OPENSSL=1 USE_LONG_OPTIONS=1 CFLAGS="%{optflags}" \
       PREFIX=%{buildroot}%{_prefix} INSTALL="install -p"

%files
%{_bindir}/mktorrent
%doc COPYING README

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Steve Traylen <steve.traylen@cern.ch> 1.1-1
- New 1.1 release. Project now hosted on github.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Apr 24 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0-4
- First official release for Fedora/EPEL

* Tue Apr 20 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0-3
- Enable large file support on 32bit.

* Tue Mar 23 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0-2
- Preserve timestamps.

* Tue Mar 23 2010 Steve Traylen <steve.traylen@cern.ch> - 1.0-1
- Initial spec file.

