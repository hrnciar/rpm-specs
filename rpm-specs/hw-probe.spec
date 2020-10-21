Summary:    Check operability of computer hardware and find drivers
Name:       hw-probe
Version:    1.5
Release:    4%{?dist}
BuildArch:  noarch
License:    LGPLv2+
URL:        https://github.com/linuxhw/hw-probe
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:   perl-libwww-perl
Requires:   curl
Requires:   hwinfo
Requires:   pciutils
Requires:   usbutils
Requires:   smartmontools
Requires:   hdparm
Requires:   sysstat
Requires:   util-linux
Requires:   lm_sensors
%if 0%{?fedora} >= 24
Recommends: dmidecode
Recommends: mcelog
Recommends: acpica-tools
Recommends: edid-decode xdpyinfo xinput xrandr xvinfo
Recommends: glx-utils
%endif
%if 0%{?el6}%{?el7}
Requires:   dmidecode
%endif
%if 0%{?el8}
Recommends: dmidecode
Recommends: mcelog
%endif
BuildRequires: perl(Getopt::Long)
BuildRequires: perl-generators

%description
A tool to check operability of computer hardware and upload result
to the Linux hardware database.

Probe is a snapshot of your computer hardware state and system
logs. The tool checks operability of devices by analysis of logs
and returns a permanent url to view the probe of the computer.

The tool is intended to simplify collecting of logs necessary for
investigating hardware related problems. Just run one simple
command in the console to check your hardware and collect all the
system logs at once:

    sudo -E hw-probe -all -upload

By creating probes you contribute to the HDD/SSD Real-Life
Reliability Test study: https://github.com/linuxhw/SMART

%prep
%autosetup

%build
# Nothing to build yet

%install
mkdir -p %{buildroot}%{_prefix}
%make_install prefix=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 1.5-4
- Recommend edid-decode xdpyinfo xinput xrandr xvinfo, not xorg-x11-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.5-1
- Update to 1.5

* Mon Oct  7 2019 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-15
- Support for EL-8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  9 2019 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-12
- Do not require mesa-demos and redhat-lsb-core.

* Wed Dec 19 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-11
- Recommends acpica-tools.
- Fix dmidecode dependency.

* Wed Dec 19 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-10
- Recommends glx-utils for glxinfo.

* Wed Dec 19 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-9
- Recommends xorg-x11-utils for edid-decode and mesa-demos for glxgears.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-8
- Recommends dmidecode.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-7
- Exclude arm.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-6
- Fix ifdef for armhfp.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-5
- No dmidecode for armhfp.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-4
- Fix bogus date in changelog.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-3
- Recommends mcelog only for Fedora 24 or newer.

* Tue Dec 11 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-2
- Require perl(Getopt::Long) at build time.

* Mon Dec  3 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-1
- Initial Fedora package.
