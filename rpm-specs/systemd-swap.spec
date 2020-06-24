Name: systemd-swap
Summary: Creating hybrid swap space from zram swaps, swap files and swap partitions
Version: 3.3.0
Release: 5%{?dist}
License: GPLv3+
URL: https://github.com/Nefelim4ag/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Not schred swapfc file on ext4
Patch0: %{url}/commit/9f843c41a185b8972470e8ce828cadffea936b59.patch

BuildArch: noarch

%if 0%{?fedora} >= 31
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd-units
%endif
%{?systemd_requires}

BuildRequires: help2man

# support for zram
Requires: util-linux
Requires: kmod

# need Linux kernel version 2.6.37.1 or better to use zram
#Requires: kernel >= 2.6.37.1
Requires: kmod(zram.ko)

%description
Manage swap on:
    zswap - Enable/Configure
    zram - Autoconfigurating
    files - (sparse files for saving space, support btrfs)
    block devices - auto find and do swapon
It is configurable in /etc/systemd/swap.conf


%prep
%autosetup -n%{name}-%{version}
# preserve timestamps
sed -i -r 's:install -:\0p -:' Makefile

%build
# nothing

%install
%make_install PREFIX=%{buildroot}
pushd %{buildroot}
install -d .%{_unitdir}
find . -name '*.service' -print -exec mv '{}' .%{_unitdir} \;
install -d .%{_mandir}/man1
help2man -o .%{_mandir}/man1/%{name}.1 .%{_bindir}/%{name}


%post
%systemd_post mkzram.service

%preun
%systemd_preun mkzram.service

%postun
%systemd_postun_with_restart mkzram.service


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/systemd/swap.conf
%{_unitdir}/*.service
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 14 2019 Raphael Groner <projects.rg@smart.ms> - 3.3.0-3
- fix some typos

* Wed Apr 10 2019 Raphael Groner <projects.rg@smart.ms> - 3.3.0-2
- fix hints from package review
- simplify dependencies
- use macros
- note real version in changelog
- generate manpage

* Tue Jul 11 2017 Raphael Groner <projects.rg@smart.ms> - 3.3.0-1
- initial
