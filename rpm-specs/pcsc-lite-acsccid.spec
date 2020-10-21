%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null)

Name:		pcsc-lite-acsccid
Version:	1.1.8
Release:	3%{?dist}
Summary:	ACS CCID PC/SC Driver for Linux/Mac OS X

License:	LGPLv2+
URL:		http://acsccid.sourceforge.net/
Source0:	https://downloads.sourceforge.net/acsccid/acsccid-%{version}.tar.bz2

BuildRequires:	gcc
BuildRequires:	pcsc-lite-devel
BuildRequires:	libusb-devel
BuildRequires:	flex
BuildRequires:	perl
BuildRequires:	pkg-config
BuildRequires:	systemd-rpm-macros

Requires:	pcsc-lite

# This is bundled from pcsc-lite-ccid and pcsc-lite upstreams
Provides: bundled(simclist) = 1.6
# There are parts of openct project, last import to CCID on 2004
Provides: bundled(openct) = 0.6.0

%description
acsccid is a PC/SC driver for Linux/Mac OS X and it supports ACS CCID smart card
readers. This library provides a PC/SC IFD handler implementation and
communicates with the readers through the PC/SC Lite resource manager (pcscd).

acsccid is based on ccid. See CCID free software driver [1] for more
information.


%prep
%setup -q -n acsccid-%{version}


%build
%configure --disable-silent-rules
%make_build


%install
%make_install
install -p -m 644 src/openct/LICENSE LICENSE.openct
install -p -m 644 src/towitoko/README README.towitoko


%post
%systemd_postun_with_restart pcscd.service


%preun
%systemd_preun pcscsd.service


%postun
%systemd_postun_with_restart pcscd.service


%files
%doc AUTHORS ChangeLog README README.towitoko
%license COPYING LICENSE.openct
%dir %{dropdir}/ifd-acsccid.bundle/
%dir %{dropdir}/ifd-acsccid.bundle/Contents/
%{dropdir}/ifd-acsccid.bundle/Contents/Info.plist
%dir %{dropdir}/ifd-acsccid.bundle/Contents/Linux/
%{dropdir}/ifd-acsccid.bundle/Contents/Linux/libacsccid.so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Jakub Jelen <jjelen@redhat.com> - 1.1.8-1
- New upstream release (#1788719)

* Mon Aug 19 2019 Jakub Jelen <jjelen@redhat.com> - 1.1.7-1
- New upstream release (#1742307)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Jakub Jelen <jjelen@redhat.com> - 1.1.6-1
- Initial release in Fedora
