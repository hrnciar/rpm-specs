Name:           xsecurelock
Version:        1.7.0
Release:        1%{?dist}
Summary:        X11 screen lock utility with security in mind
License:        ASL 2.0
URL:            https://github.com/google/xsecurelock

Source0:        https://github.com/google/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

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
 

%description
XSecureLock is an X11 screen lock utility designed with the primary goal of
security.

%prep
%autosetup

%build
%configure --with-pam-service-name=system-auth
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
* Fri Feb 21 2020 Sam P <survient@fedoraproject.org> - 1.7.0-1
- Initial Build
