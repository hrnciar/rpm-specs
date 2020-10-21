Name:           direwolf
Version:        1.5
Release:        8%{?dist}
Summary:        Sound Card-based AX.25 TNC

License:        GPLv2+
URL:            https://github.com/wb2osz/direwolf/
Source0:        https://github.com/wb2osz/direwolf/archive/%{version}/%{name}-%{version}.tar.gz
# Fix make install to put udev rule into DESTDIR
Patch0:         direwolf-1.5-makefile.patch
Patch1:         direwolf-1.5-gpsd-api-7.patch
Patch2:         direwolf-1.5-gpsd-api-8.patch
Patch3:         direwolf-1.5-gpsd-api-9.patch

BuildRequires:  alsa-lib-devel libax25-devel gpsd-devel hamlib-devel glibc-devel gcc systemd-devel perl-generators
Requires:       ax25-tools ax25-apps

%description
Dire Wolf is a modern software replacement for the old 1980's style
TNC built with special hardware.  Without any additional software, it
can perform as an APRS GPS Tracker, Digipeater, Internet Gateway
(IGate), APRStt gateway. It can also be used as a virtual TNC for
other applications such as APRSIS32, UI-View32, Xastir, APRS-TW, YAAC,
UISS, Linux AX25, SARTrack, RMS Express, BPQ32, Outpost PM, and many
others.

%prep
%autosetup -n %{name}-%{version}


%build
%make_build

%install
%make_install DESTDIR=${RPM_BUILD_ROOT}/usr

# Copy doc pngs
cp direwolf-block-diagram.png ${RPM_BUILD_ROOT}%{_pkgdocdir}/direwolf-block-diagram.png
cp tnc-test-cd-results.png    ${RPM_BUILD_ROOT}%{_pkgdocdir}/tnc-test-cd-results.png

# remove extraneous files
# This is not a desktop application, per the guidelines.  Running it in a terminal
# does not make it a desktop application.
rm ${RPM_BUILD_ROOT}/usr/share/direwolf/pixmaps/dw-icon.png
rm ${RPM_BUILD_ROOT}/usr/share/applications/direwolf.desktop
rm ${RPM_BUILD_ROOT}/usr/share/doc/direwolf/CHANGES.md
rm ${RPM_BUILD_ROOT}/usr/share/doc/direwolf/LICENSE-dire-wolf.txt
rm ${RPM_BUILD_ROOT}/usr/share/doc/direwolf/LICENSE-other.txt

# Move Telemetry Toolkit sample scripts into docs
mv ${RPM_BUILD_ROOT}%{_bindir}/telem* ${RPM_BUILD_ROOT}%{_pkgdocdir}/examples/
chmod 0644 ${RPM_BUILD_ROOT}%{_pkgdocdir}/examples/*


%package -n %{name}-doc
Summary:        Documentation for Dire Wolf
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description -n %{name}-doc
Dire Wolf is a modern software replacement for the old 1980's style
TNC built with special hardware.  Without any additional software, it
can perform as an APRS GPS Tracker, Digipeater, Internet Gateway
(IGate), APRStt gateway. It can also be used as a virtual TNC for
other applications such as APRSIS32, UI-View32, Xastir, APRS-TW, YAAC,
UISS, Linux AX25, SARTrack, RMS Express, BPQ32, Outpost PM, and many
others.


%files
%license LICENSE-dire-wolf.txt
%{_udevrulesdir}/99-direwolf-cmedia.rules
%{_bindir}/* 
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/symbols-new.txt
%{_datadir}/%{name}/symbolsX.txt
%{_datadir}/%{name}/tocalls.txt
%dir %{_pkgdocdir}
%{_pkgdocdir}/README.md
%{_pkgdocdir}/direwolf-block-diagram.png
%{_pkgdocdir}/tnc-test-cd-results.png

%dir %{_pkgdocdir}/examples
%{_pkgdocdir}/examples/*


%files -n %{name}-doc
%{_pkgdocdir}/*.pdf


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Björn Esser <besser82@fedoraproject.org> - 1.5-7
- Rebuild (gpsd)

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 1.5-6
- Rebuild for hamlib 4.

* Thu Feb 20 2020 Matt Domsch <matt@domcsh.com> - 1.5-5
- Remove unneeded dependency on python2-devel (#1805225)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.5-2
- Rebuild (gpsd)

* Sun Feb 17 2019 Matt Domsch <matt@domsch.com> - 1.5-1
- Upgrade to released version 1.5
- Apply upstream patch for newer gpsd API

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-0.2.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Matt Domsch <matt@domsch.com> - 1.5-0.1.beta4
- Fedora Packaging Guidelines, based on spec by David Ranch
  Moved Telemetry Toolkit examples into examples/ docs.
