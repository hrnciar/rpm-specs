Name: thc-ipv6
Version: 3.4
Release: 7%{?dist}
Summary: An toolkit for attacking the IPv6 protocol suite

License: AGPLv3 with exceptions
URL: https://www.thc.org/thc-ipv6/
Source0: http://www.thc.org/releases/thc-ipv6-%{version}.tar.gz

# PR #23 
Patch0: /tmp/0001-Include-stdint.h-in-dnsrevenum6.c-since-uintptr_t-is.patch

BuildRequires:  gcc
BuildRequires: libpcap-devel
BuildRequires: openssl-devel 
BuildRequires: libnetfilter_queue-devel
BuildRequires: perl-generators
# For patches
BuildRequires: git-core

%description
A complete tool set to attack the inherent protocol weaknesses of IPV6
and ICMP6, and includes an easy to use packet factory library.

%prep
%autosetup -S git -n thc-ipv6-%{version}


%build

sed -i "s|^PREFIX=/usr/local|PREFIX=/usr|" Makefile 
sed -i "s/^STRIP=strip/STRIP=echo/" Makefile 
sed -i "/^CFLAGS=-O2/d" Makefile 
make %{?_smp_mflags} CFLAGS="%{optflags} -D_HAVE_SSL"


%install
make install DESTDIR=%{buildroot}


%files
%doc CHANGES LICENSE LICENSE.OPENSSL README HOWTO-INJECT
%{_bindir}/*
%{_mandir}/man8/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 3.4-1
- Update to 3.4 (rhbz #1531027)
- Fix build and add SSL support

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 3.0-1
- Update to 3.0
- Add new deps
- Do not strip binaries 

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 2.7-1
- Update to 2.7

* Fri Jul 25 2014 Athmane Madjoudj <athmane@fedoraproject.org> 2.5-2
- Rename the package properly

* Wed Apr 16 2014 Athmane Madjoudj <athmane@fedoraproject.org> 2.5-1
- Initial specfile

