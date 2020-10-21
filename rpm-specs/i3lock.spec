Name:           i3lock
Version:        2.12
Release:        4%{?dist}
Summary:        Simple X display locker like slock
License:        MIT
URL:            https://i3wm.org/%{name}/
Source0:        %{URL}/%{name}-%{version}.tar.bz2
Source1:        %{URL}/%{name}-%{version}.tar.bz2.asc
# Michael Stapelberg's GPG key:
Source2:        gpgkey-424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D.gpg
# FIXME: drop on next upstream release after 2.12
# cherry picked from https://github.com/i3/i3lock/pull/259
Patch0:         0001-unlock_indicator.c-fix-build-failure-against-gcc-10.patch

BuildRequires:  gcc
# from configure.ac
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(xkbcommon-x11) >= 0.5.0
BuildRequires:  pkgconfig(cairo)
# these don't provide pkg-config files
BuildRequires:  libev-devel
BuildRequires:  pam-devel

# gpg verification
BuildRequires:  gnupg2

%description
i3lock is a simple screen locker like slock. After starting it, you will see a
white screen (you can configure the color/an image). You can return to your
screen by entering your password.

Many little improvements have been made to i3lock over time:

- i3lock forks, so you can combine it with an alias to suspend to RAM (run
  "i3lock && echo mem > /sys/power/state" to get a locked screen after waking up
  your computer from suspend to RAM)

- You can specify either a background color or a PNG image which will be
  displayed while your screen is locked.

- You can specify whether i3lock should bell upon a wrong password.

- i3lock uses PAM and therefore is compatible with LDAP etc. On OpenBSD i3lock
  uses the bsd_auth(3) framework.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure
%make_build

%install
%make_install INSTALL="install -p"
install -Dpm0644 i3lock.1 %{buildroot}%{_mandir}/man1/i3lock.1

%files
%doc CHANGELOG README*
%license LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/pam.d/%{name}
%{_mandir}/man1/i3lock.1*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 2.12-3
- Add upstream patch to fix compilation failure with gcc 10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 anadahz <andz@torproject.org> - 2.12-1
- new version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 anadahz <andz@torproject.org> - 2.11.1
- new version

* Sat Jul 14 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.10-1
- new version

* Sat Jul 14 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.9.1-4
- BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 05 2017 Christian Dersch <lupinix@mailbox.org> - 2.9.1-1
- new version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Christian Dersch <lupinix@mailbox.org> - 2.8-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Christopher Meng <rpm@cicku.me> - 2.7-1
- Update to 2.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Christopher Meng <rpm@cicku.me> - 2.6-1
- Update to 2.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Felix Wiedemann <felix.wiedemann@online.de> - 2.5-1
- New upstream release
- Removed custom i3lock.pam file
- Added new BuildRequires

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Martin Preisler <mpreisle@redhat.com> - 2.4.1-6
- Bumped release for clear upgrade path

* Fri Jul 13 2012 Martin Preisler <mpreisle@redhat.com> - 2.4.1-4
- Make sure we install README, LICENSE, CHANGELOG and the manpage

* Fri Jun 15 2012 Martin Preisler <mpreisle@redhat.com> - 2.4.1-3
- rebuilt with a bumped release number to make sure the package updates from f17

* Wed Jun 06 2012 Martin Preisler <mpreisle@redhat.com - 2.4.1-1
- Updated to upstream stable 2.4.1 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6.20100320git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5.20100320git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Mar 20 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 1.0-4.20100320git
- Update to current git

* Sat Feb 06 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 1.0-3
- Some bugfixes (sync with upstream)

* Sat Jan 09 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 1.0-2
- Add a PAM configfile as SOURCE1

* Wed Dec 02 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 1.0-1
- Package build for Fedora
