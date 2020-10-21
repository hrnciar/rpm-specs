%global ver_maj 1
%global ver_min 4
%global ver_patch 2

Name:		pixiewps	
Version:	%{ver_maj}.%{ver_min}.%{ver_patch}
Release:	7%{?dist}
Summary:	An offline Wi-Fi Protected Setup brute-force utility 

License:	GPLv3
URL:		https://github.com/wiire-a/pixiewps
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		0001-unbundle_tc.patch
Patch1:		0002-unbundle_tfm.patch

BuildRequires:	libtomcrypt-devel
BuildRequires:	tomsfastmath-devel
BuildRequires:	openssl-devel
BuildRequires:	glibc-devel
BuildRequires:	gcc

%description
Pixiewps is a tool written in C used to bruteforce offline the WPS PIN
exploiting the low or non-existing entropy of some software implementations,
the so-called "pixie-dust attack" discovered by Dominique Bongard in summer
2014.

%prep
%autosetup -p1
sed -i "s|^\tinstall -|\t\$(INSTALL) -|" Makefile
rm -rf src/crypto/tfm
rm -f src/tc/*.h
rm -f src/tc/aes.c
rm -f src/tc/aes_tab.c
rm -f src/tc/sha256.c

%build
%make_build CFLAGS="%{build_cflags}" OPENSSL=1

%install
%make_install PREFIX="%{_prefix}"

%files
%doc README.md
%license LICENSE.md
%{_bindir}/pixiewps
%{_mandir}/man1/pixiewps.1.*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tomas Korbar <tomas.korb@seznam.cz> - 1.4.2-3
- Add gcc to build requires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018 Tomas Korbar <tomas.korb@seznam.cz> - 1.4.2-1
- Initial import (#1573778)
