Name:           xsecurelock
Version:        1.7.0
Release:        3%{?dist}
Summary:        X11 screen lock utility with security in mind
License:        ASL 2.0
URL:            https://github.com/google/xsecurelock

Source0:        https://github.com/google/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Requires: libXft
BuildRequires: gcc
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pam-devel
BuildRequires: pamtester
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xrandr)
BuildRequires: httpd-tools
BuildRequires: pandoc
BuildRequires: doxygen
BuildRequires: libXft-devel
 

%description
XSecureLock is an X11 screen lock utility designed with the primary goal of
security.

%prep
%autosetup

%build
%configure --with-pam-service-name=system-auth --with-xft
%make_build

%install
%make_install
rm %{buildroot}%{_pkgdocdir}/LICENSE

%files
%license LICENSE
%doc README.md
%doc CONTRIBUTING
%doc /usr/share/doc/xsecurelock/examples/saver_livestreams
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_libexecdir}/%{name}/auth_x11
%{_libexecdir}/%{name}/authproto_pam
%{_libexecdir}/%{name}/authproto_pamtester
%{_libexecdir}/%{name}/authproto_htpasswd
%{_libexecdir}/%{name}/dimmer
%{_libexecdir}/%{name}/pgrp_placeholder
%{_libexecdir}/%{name}/saver_blank
%{_libexecdir}/%{name}/saver_multiplex
%{_libexecdir}/%{name}/until_nonidle

%changelog
* Mon Sep 14 2020 Sam P <survient@fedoraproject.org> - 1.7.0-3
- Added --with-xft build flag

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 21 2020 Sam P <survient@fedoraproject.org> - 1.7.0-1
- Initial Build
