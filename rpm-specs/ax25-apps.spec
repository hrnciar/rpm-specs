# https://gcc.gnu.org/gcc-10/porting_to.html#common
%define _legacy_common_support 1

Name:		ax25-apps
Version:	2.0.0
Release:	1%{?dist}
Summary:	AX.25 ham radio applications

#ax25ipd is BSD licensed, rest is GPLv2+
License:	GPLv2+ and BSD
URL:		https://github.com/ve7fet/linuxax25

# git clone https://github.com/ve7fet/linuxax25.git
# cd linuxax25/ax25apps
# git archive --prefix=ax25apps-2.0.0/ -o ../ax25apps-2.0.0.tar.gz HEAD
Source0:	ax25apps-%{version}.tar.gz

Patch0:		ax25-apps-ax25rtd-config_c.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gcc
BuildRequires:	libax25-devel
BuildRequires:	ncurses-devel


%description

This package provides specific user applications for hamradio that use AX.25 
Net/ROM or ROSE network protocols:

 * axcall: a general purpose AX.25, NET/ROM and ROSE connection program.
 * axlisten: a network monitor of all AX.25 traffic heard by the system.
 * ax25ipd: an RFC1226 compliant daemon which provides encapsulation of
   AX.25 traffic over IP.
 * ax25mond: retransmits data received from sockets into an AX.25 monitor
   socket.


%prep
%autosetup -p1 -n ax25apps-%{version}


%build
./autogen.sh
%configure
%make_build


%install
%make_install

#don't include these twice
rm -rf $RPM_BUILD_ROOT%{_docdir}/ax25apps

# Fix the encoding on the doc files to be UTF-8
recode()
{
	iconv -f "$2" -t utf-8 < "$1" > "${1}_"
	mv -f "${1}_" "$1"
}
recode AUTHORS iso-8859-15


%files
%doc AUTHORS ChangeLog README
%doc doc/*
%license COPYING
%config(noreplace) %{_sysconfdir}/ax25/ax25ipd.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25mond.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25rtd.conf
%{_bindir}/*
%{_sbindir}/*
%{_localstatedir}/ax25/ax25rtd/
%{_mandir}/man?/*


%changelog
* Mon Mar 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.0.0-1
- Upgrade to 2.0.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Richard Shaw <hobbes1069@gmail.com> - 1.0.5-8
- Add patch for segfault when using Unix98 pty, (#1644317).

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Richard Shaw <hobbes1069@gmail.com> - 1.0.5-1
- Update to latest upstream release.

* Wed Sep 23 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.8-0.1.rc4
- Update to latest upstream release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Randall Berry, N3LRX <dp67@fedoraproject.org> - 0.0.6-17
- 3rd rebuild

* Sat Aug 03 2013 Randall Berry, N3LRX <dp67@fedoraproject.org> - 0.0.6-16
- 2nd rebuild

* Sat Aug 03 2013 Randall Berry, N3LRX <dp67@fedoraproject.org> - 0.0.6-15
- Rebuild for LICENSE inclusion problem (mass rebuild)
- Also corrects bug #888206

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Randall Berry, N3LRX <dp67@fedoraproject.org> - 0.0.6-12
- Add patch to relicense /listen/ripdump.c
- Author re-released source in question under BSD
- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=630893
- BZ: #888206 https://bugzilla.redhat.com/show_bug.cgi?id=888206
- Add BSD license text to package.

* Sun Aug 05 2012 Randall Berry, N3LRX <dp67@fedoraproject.org> - 0.0.6-11
- Cleanup build for F18/Rawhide
- Remove patch1 0 byte file

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Randall Berry, N3LRX <dp67@fedoraproject.org> - 0.0.6-8
- Rebuild for Rawhide
- Added Patch1 required for rawhide build.
- De-versioned autotools for rawhide build.
- Added Makefile.am patch per build log.

* Thu Jun 23 2011 Randall Berry, N3LRX <dp67@fedoraproject.org> - 0.0.6-7
- Rebuild for Rawhide
- Added Patch1 required for rawhide build.
- Deversioned autotools.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 21 2009 Robert Scheck <robert@fedoraproject.org> 0.0.6-4
- Rebuilt against libtool 2.2

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 16 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.0.6-2
- Submit for review

* Thu Dec 06 2007 Sindre Pedersen Bjørdal <foolish@guezz.net> 0.0.6-1
- Initial Build
