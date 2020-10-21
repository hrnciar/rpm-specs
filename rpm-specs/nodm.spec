Name:           nodm
Version:        0.13
Release:        9%{?dist}
Summary:        A display manager automatically starting an X session

# xsession-child.c is under BSD (3 clause) and GPLv2+, all other sources with GPLv2+,
# config/install-sh with MIT/X11
License:        BSD and GPLv2+
URL:            https://github.com/spanezz/nodm
Source0:        https://github.com/spanezz/nodm/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
# patch removes useless default configuration setting (/usr/bin/Xnest)
Patch1:         nodm-0.11-nested-nodefault.patch
Patch2:         nodm-0.13-AM_CFLAGS.patch

BuildRequires:  libX11-devel
BuildRequires:  pam-devel
BuildRequires:  cmake
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  systemd-units

# runtime
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires:         systemd
# rudimental start of some X session
Requires:         xorg-x11-xinit

%description
An automatic display manager which automatically starts an X session at
system boot. It is meant for devices like smartphones, but can be used
on a regular computer as well, if the security implications are acceptable.


%prep
%setup -q
%patch1 -p0
%patch2 -p1

# run autogen.sh since we patch configure.ac
# but don't run configure twice
NOCONFIGURE=true ./autogen.sh

%build
%configure
%make_build

%install
%make_install
install -m0644 %SOURCE1 -D %{buildroot}%{_unitdir}/%{name}.service
install -m0644 %SOURCE2 -D %{buildroot}%{_sysconfdir}/%{name}.conf


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license COPYING
%doc AUTHORS README.md
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 15 2017 Sérgio Basto <sergio@serjux.com> - 0.13-1
- Update nodm 0.13.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 13 2016 Sérgio Basto <sergio@serjux.com> - 0.12-1
- Update nodm to debian-0.12-1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Raphael Groner <projects.rg@smart.ms> - 0.11-3
- improve systemd unit, obsoleted launch script

* Fri Jan 08 2016 Raphael Groner <projects.rg@smart.ms> - 0.11-2
- fix typo

* Wed Jan 06 2016 Raphael Groner <projects.rg@smart.ms> - 0.11-1
- bump to version 0.11 as in Debian
- provide useful configuration
- remove %%check

* Thu Dec 17 2015 Raphael Groner <projects.rg@smart.ms> - 0.7-2
- add more systemd stuff
- adjust License tag

* Wed Dec 16 2015 Raphael Groner <projects.rg@smart.ms> - 0.7-1
- unretire, new upstream version

* Sun Feb 14 2010 Sebastian Dziallas <sebastian@when.com> - 0.6-2
- fix issue with DSO linking thanks to Mathieu Bridon

* Thu Jan 28 2010 Sebastian Dziallas <sebastian@when.com> - 0.6-1
- initial packaging
