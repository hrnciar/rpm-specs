%global driver asekey
%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null)
%global rulesdir %(pkg-config udev --variable udevdir 2>/dev/null)/rules.d

Name:           pcsc-lite-%{driver}
Version:        3.7
Release:        14%{dist}
Summary:        ASEKey USB token driver
# 92_pcscd_asekey.rules:    LGPLv2+
# other files:              BSD
License:        BSD and LGPLv2+
# The address does not exist anymore.
URL:            http://www.athena-scs.com/
Source0:        %{url}docs/reader-drivers/%{driver}-%(echo %{version}|tr '.' '-')-tar.bz2
# Fix PCSC bundle
Patch0:         %{driver}-3.7-bundle.patch
# Fix GCC-8 warnings
Patch1:         %{driver}-3.7-Fix-compiler-warnings.patch
BuildRequires:  gcc
BuildRequires:  libusb-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libpcsclite) >= 1.8.0
BuildRequires:  pkgconfig(udev)
BuildRequires:  sed
Requires:       pcsc-lite >= 1.8.0
Requires(post):     systemd
Requires(postun):   systemd
Provides:       pcsc-ifd-handler

%global __provides_exclude_from %{?__provides_exclude_from:%{__provides_exclude_from}|}^%{dropdir}

%description
This is a driver for the ASEKey USB cryptographic token in form of a PCSC
plug-in.

%prep
%setup -q -n %{driver}-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure --with-udev-rules-dir="%{rulesdir}"
# Work around bug #893432:
# All platforms calls the compiler without "-gnu" suffix, except armv7hl which
# uses "-gnueabi" suffix.
%ifarch armv7hl
sed -i -e '/^BUILD=/ s/-gnu$/-gnueabi/' Makefile.inc
%else
sed -i -e '/^BUILD=/ s/-gnu$//' Makefile.inc
%endif
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%post
/bin/systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%postun
/bin/systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%files
%license LICENSE
%doc ChangeLog README
%{dropdir}/ifd-ASEKey.bundle
%{rulesdir}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Petr Pisar <ppisar@redhat.com> - 3.7-10
- Reflow package description text

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Petr Pisar <ppisar@redhat.com> - 3.7-8
- Fix compiler warnings

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Petr Pisar <ppisar@redhat.com> - 3.7-6
- Fix 92_pcscd_asekey.rules file location (bug #1476619)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Petr Pisar <ppisar@redhat.com> - 3.7-1
- Initial package
