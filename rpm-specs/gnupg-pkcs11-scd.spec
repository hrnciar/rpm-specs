Name:           gnupg-pkcs11-scd
Version:        0.9.2
Release:        2%{?dist}
Summary:        GnuPG-compatible smart-card daemon with PKCS#11 support

License:        BSD
URL:            http://gnupg-pkcs11.sourceforge.net
Source0:        https://github.com/alonbl/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  pkgconfig(openssl) >= 0.9.7a
BuildRequires:  pkgconfig(libpkcs11-helper-1)
BuildRequires:  libassuan-devel
BuildRequires:  libgcrypt-devel
Requires:       openssl >= 0.9.7a
Requires:       pkcs11-helper >= 1.03

%description
gnupg-pkcs11-scd is a drop-in replacement for the smart-card daemon (scd)
shipped with the next-generation GnuPG (gnupg2). The daemon interfaces
with smart-cards by using RSA Security Inc.'s PKCS#11 Cryptographic Token
Interface.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_ROOT}%{_docdir}

%files
%{_bindir}/*
%{_mandir}/*/*
%doc AUTHORS README THANKS gnupg-pkcs11-scd/gnupg-pkcs11-scd.conf.example
%license COPYING

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 W. Michael Petullo <mike@flyn.org> - 0.9.2-1
- New upstream version
- Remove upstreamed patch for OpenSSL 1.1.0+

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 W. Michael Petullo <mike[@]flyn.org> - 0.9.1-2
- Markup COPYING as license
- Use pkgconfig function with BuildRequires

* Thu Oct 05 2017 W. Michael Petullo <mike[@]flyn.org> - 0.9.1-1
- New upstream version
- Add patch for OpenSSL 1.1.0+
- BuildRequire pkgconfig
- Do not remove build root in install section
- Do not use defattr

* Wed Mar 18 2015 W. Michael Petullo <mike[@]flyn.org> - 0.7.3-1
- New upstream version

* Mon Jun 16 2014 W. Michael Petullo <mike[@]flyn.org> - 0.7.2-2
- Remove some explicit library dependencies

* Thu May 19 2011 W. Michael Petullo <mike[@]flyn.org> - 0.7.2-1
- Initial package
