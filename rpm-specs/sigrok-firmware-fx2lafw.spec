Name:           sigrok-firmware-fx2lafw
Version:        0.1.7
Release:        3%{?dist}
Summary:        Firmware for logic analyzers based on the Cypress EZ-USB FX2(LP) chip
# Combined and LGPLv2+ and GPLv2+
License:        GPLv2+
URL:            http://www.sigrok.org
Source0:        %{url}/download/source/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  sdcc

Requires:       sigrok-firmware-filesystem

%description
fx2lafw is a free/libre/open-source firmware for logic analyzers based on
the Cypress EZ-USB FX2(LP) chip.

This firmware package is needed to use libsigrok with Cypress EZ-USB FX2(LP)
based logic analyzers (the fx2lafw driver in libsigrok).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc README NEWS COPYING COPYING.LESSER
%{_datadir}/sigrok-firmware/fx2lafw-*.fw

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.7-1
- Update to fx2lafw 0.1.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.5-1
- Update to fx2lafw 0.1.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.3-0
- Update to fx2lafw 0.1.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 05 2013 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.1-1
- Update to fx2lafw 0.1.1

* Fri Mar 15 2013 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.0-1
- Initial RPM release
