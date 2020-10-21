Name:           i3status
Version:        2.13
Release:        3%{?dist}
Summary:        Status bar generator for i3bar, dzen2, xmobar or similar programs
License:        BSD
URL:            https://i3wm.org/i3status/
Source0:        %{url}/%{name}-%{version}.tar.bz2
Source1:        %{url}/%{name}-%{version}.tar.bz2.asc
# Michael Stapelberg's GPG key:
Source2:        gpgkey-424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D.gpg

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(yajl)
# man pages
BuildRequires:  asciidoc
BuildRequires:  xmlto
# gpg verification
BuildRequires:  gnupg2
# tests
BuildRequires:  perl

%description
i3status is a program for generating a status bar for i3bar, dzen2,
xmobar or similar programs. It issues a small number of system
calls, as one generally wants to update such status lines every
second so that the bar is updated even under load. It saves a bit of
energy by being more efficient than shell commands.

%prep
gpg2 --keyring %{SOURCE2} --verify %{SOURCE1}
%autosetup

%build
autoreconf -fi
# out of source builds are mandatory
mkdir build && pushd build
ln -s ../configure configure
%configure --disable-sanitizers
%make_build
popd

%install
%make_install -C build

%check
# this need the testcases/ dir from upstream git repository
# unfortunately this fails on koji
# make check -C build || (cat test-suite.log; false)

%files
%doc CHANGELOG
%license LICENSE
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man*/%{name}.1*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 2.13-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.12-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Christian Dersch <lupinix@mailbox.org> - 2.11-6
- rebuilt for libconfuse

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Jon Ciesla <limburgher@gmail.com> - 2.11-3
- libconfuse rebuild.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Christian Dersch <lupinix@mailbox.org> - 2.11-1
- new version

* Wed Jun 15 2016 Jon Ciesla <limburgher@gmail.com> - 2.10-3
- libconfuse rebuild.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Martin Preisler <mpreisle@redhat.com> - 2.10-1
- Update to 2.10
- Added new deps - libnl3 and pulseaudio

* Thu Sep 17 2015 Christopher Meng <rpm@cicku.me> - 2.9-1
- Update to 2.9

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Martin Preisler <mpreisle@redhat.com> - 2.8-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 09 2013 Simon Wesp <cassmodiah@fedoraproject.org> - 2.7-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Martin Preisler <mpreisle@redhat.com> - 2.6-1
- Updated to 2.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Martin Preisler <mpreisle@redhat.com> - 2.5.1-1
- Updated to 2.5.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 11 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 2.1-1
- New upstream release

* Sat Mar 20 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 2.0-4.20100320git
- Update to current git

* Fri Feb 05 2010 Simon Wesp <cassmodiah@fedoraproject.org> - 2.0-2
- Some bugfixes (sync with upstream)

* Wed Dec 02 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 2.0-1
- Package build for Fedora
