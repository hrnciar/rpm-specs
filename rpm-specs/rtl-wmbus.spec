Name:                  rtl-wmbus
Version:               0

%global forgeurl       https://github.com/xaelsouth/%{name}
%global date           20191213
%global commit         6a04c4548245c4f6adaad6348ee4d2deef825d63
%global the_binary     rtl_wmbus

%forgemeta

Release:               6%{?dist}
Summary:               Software defined receiver for wireless M-Bus with RTL-SDR
License:               BSD
Url:                   %{forgeurl}
Source0:               %{forgesource}
# Upstream reference: https://github.com/xaelsouth/rtl-wmbus/pull/8
Patch0:                %{name}-Allow-to-redefine-CFLAGS-LDFLAGS-and-OUTPUT-director.patch

BuildRequires:         /usr/bin/git
BuildRequires:         gcc
BuildRequires:         fixedptc-devel

Requires:              /usr/bin/rtl_sdr


%description
rtl-wmbus is a software defined receiver for Wireless-M-Bus.
It is written in plain C and uses RTL-SDR to interface with RTL2832-based
hardware.

Wireless-M-Bus is the wireless version of M-Bus
("Meter-Bus", http://www.m-bus.com), which is an European standard for
remote reading of smart meters.

The primary purpose of rtl-wmbus is experimenting with digital signal
processing and software radio.

rtl-wmbus can be used on resource constrained devices such as Raspberry Pi Zero
or Raspberry PI B+ overclocked to 1GHz. Any Android based tablet will do
the same too.

rtl-wmbus provides:
  - filtering
  - FSK demodulating
  - clock recovering
  - mode T1 and mode C1 packet decoding


%prep
%forgeautosetup -S git
# Remove bundled fixedptc library
rm -rf include

# Split the LICENSE from the README.md
awk '/^  License/ {dump=1; next} \
     /^  -------/ {next} \
     /.*/         {if (dump) {print}}' \
     README.md >LICENSE


%build
%set_build_flags
export LIB="%{__global_ldflags} -lm"
%{make_build}


%install
install -p -m 0755 -D build/%{the_binary} %{buildroot}%{_bindir}/%{the_binary}


%files
# The license is in the documentation file
%license LICENSE
%doc README.md
%{_bindir}/%{the_binary}


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-4.20191213git6a04c45
- Split the LICENSE from the README.md
- Remove -v from forgemeta

* Tue Mar 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-3.20191213git6a04c45
- Use %%set_build_flags

* Mon Mar 02 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-2.20191213git6a04c45
- Add upstream reference to patch.

* Fri Feb 28 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-1.20191213git6a04c45
- Initial RPM release.
