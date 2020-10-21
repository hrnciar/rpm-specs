%global commit 934450798654bcc819fb81ad66a2bf5e5b4d39d7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		xclip
Version:	0.13
Release:	11.git%{shortcommit}%{?dist}
License:	GPLv2+
Summary:	Command line clipboard grabber
URL:		http://sourceforge.net/projects/xclip
# Source0:	https://github.com/astrand/xclip/archive/%%{version}.tar.gz
Source0:	https://github.com/astrand/xclip/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:	libXmu-devel, libICE-devel, libX11-devel, libXext-devel
BuildRequires:	autoconf, automake, libtool

%description
xclip is a command line utility that is designed to run on any system with an
X11 implementation. It provides an interface to X selections ("the clipboard")
from the command line. It can read data from standard in or a file and place it
in an X selection for pasting into other X applications. xclip can also print
an X selection to standard out, which can then be redirected to a file or
another program.

%prep
%setup -q -n %{name}-%{commit}
autoreconf -ifv

%build
%configure
make CDEBUGFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%files
%license COPYING
%doc README
%{_bindir}/xclip
%{_bindir}/xclip-copyfile
%{_bindir}/xclip-cutfile
%{_bindir}/xclip-pastefile
%{_mandir}/man1/xclip*.1*

%changelog
* Mon Sep 21 2020 Tom Callaway <spot@fedoraproject.org> - 0.13-11.git9344507
- update to latest from git

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct  5 2016 Tom Callaway <spot@fedoraproject.org> - 0.13-1
- update to 0.13

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-11.20140209svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-10.20140209svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-9.20140209svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-8.20140209svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.12-7.20140209svn
- update to upstream subversion revision 85 (#1076798, #1076800)
- use autoreconf and add BR: autoconf automake

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.12-1
- update to 0.12

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-1
- update to 0.11

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.10-3
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.10-2
- enable utf8 support by default

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.10-1
- bump to 0.10
- new URL

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.08-4
- license tag fix
- rebuild for BuildID

* Wed Apr 25 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.08-3
- add extra BR for old FC versions

* Wed Apr 25 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.08-2
- smp_mflags

* Tue Apr 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.08-1
- initial package for Fedora Extras
