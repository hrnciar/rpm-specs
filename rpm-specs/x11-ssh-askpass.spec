%global __alternatives	/usr/sbin/alternatives
%global appdefaultsdir	/usr/share/X11/app-defaults

%{!?release_func:%global release_func() %1%{?dist}}

Name:		x11-ssh-askpass
Version:	1.2.4.1
Release:	%release_func 31
Summary:	A passphrase dialog for X and not only for OpenSSH


License:	Public Domain
URL:		http://www.jmknoble.net/software/x11-ssh-askpass/
Source0:	http://www.jmknoble.net/software/x11-ssh-askpass/%name-%version.tar.gz
Source10:	x11-ssh-askpass.csh
Source11:	x11-ssh-askpass.sh
Patch0:		x11-ssh-askpass-1.2.4-random.patch

Provides:		openssh-askpass-x11

BuildRequires:  gcc
BuildRequires:		imake libXt-devel

%description
x11-ssh-askpass is a lightweight passphrase dialog for OpenSSH or
other open variants of SSH. In particular, x11-ssh-askpass is useful
with the Unix port of OpenSSH by Damien Miller and others, and Damien
includes it in his RPM packages of OpenSSH.

x11-ssh-askpass uses only the stock X11 libraries (libX11, libXt) for
its user interface. This reduces its dependencies on external libraries
(such as GNOME or Perl/Tk). See the README for further information.

%prep
%setup -q
%patch0 -p1 -b .random

%global makeflags	XAPPLOADDIR='%appdefaultsdir'
%build
export LDFLAGS='-Wl,--as-needed'
%configure --libexecdir=%_libexecdir/openssh
xmkmf
make includes  %makeflags
make %{?_smp_mflags} %makeflags

%install
make install install.man DESTDIR=$RPM_BUILD_ROOT %makeflags

mkdir -p                              $RPM_BUILD_ROOT%_sysconfdir/profile.d
install -p -m0644 %SOURCE10 %SOURCE11 $RPM_BUILD_ROOT%_sysconfdir/profile.d/

rm -f $RPM_BUILD_ROOT{%_libexecdir/openssh,%_mandir/man1}/ssh-askpass*

%files
%doc ChangeLog README TODO *.ad
%config(noreplace) %_sysconfdir/profile.d/*
%appdefaultsdir/*
%_libexecdir/openssh
%_mandir/*/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.2.4.1-29
- install profile scriptlets as non-executable to avoid explicit csh/sh dep

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.2.4.1-27
- Remove obsolete requirements for %%postun/%%pre scriptlets

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.2.4.1-25
- Rebuild with fixed binutils

* Fri Jul 27 2018 David Cantrell <dcantrell@redhat.com> - 1.2.4.1-24
- Make nothing but cosmetic changes to the spec file and other source
  files to appease the build system and fix what I suspect is a bogus
  FTBFS (#1606816)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.2.4.1-22
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 09 2009 Adam Jackson <ajax@redhat.com> 1.2.4.1-8
- Requires: libXt for pre and postun, not the file path, since libXt will
  always provide it.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 30 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-6
- use lower-cased name for profile files and simplified them

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4.1-4
- Autorebuild for GCC 4.3

* Sun Feb  4 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-3
- rebuilt with -Wl,--as-needed

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-2
- rebuilt

* Tue Jul 25 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-1
- initial Fedora Extras package (review #176580)

* Sat May 20 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-0.2
- removed '%%config' from the app-defaultsdir
- do not own the app-defaultsdir anymore
- added some tricks to the -random patch to avoid removal of the
  clear-the-passphrase-memset() during optimization

* Sun Mar 26 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-0.1
- fixed path of app-defaults dir

* Wed Dec 21 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.2.4.1-0
- initial build
