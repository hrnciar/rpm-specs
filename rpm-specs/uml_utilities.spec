Name: uml_utilities
Version: 20070815
Release: 27%{?dist}
License: GPL+
URL: http://user-mode-linux.sourceforge.net/index.html
Source0: http://user-mode-linux.sourceforge.net/%{name}_%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires: fuse-devel, perl-generators, readline-devel
Requires(pre): shadow-utils
Summary: Utilities for user-mode linux kernel
# installation problem was reported upstream:
# http://sourceforge.net/mailarchive/message.php?msg_name=47E16C87.8080705%40plauener.de
Patch0: uml_utilities_20070815-install.patch
# Fix building with glibc 2.28, bug #1676173,
# <https://sourceforge.net/p/user-mode-linux/bugs/69/>
Patch1: tools-20070815-Inlude-sys-sysmacros.h-for-makedev.patch

%description 
This package contains the utilities for user-mode linux for networking, 
COW, etc.

%prep
%setup -q -n tools-%{version}
%patch0 -p1 -b .install
%patch1 -p1

%build
%{__make} CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
# Makefiles do hardcoded stripping, breaking debug package
for mfile in */Makefile; do sed -i "s/install -s/install /" $mfile; done

make install LIB_DIR=%{_libdir}/uml DESTDIR=$RPM_BUILD_ROOT
# we need port-helper in the path
mylib=`echo %{_libdir} | sed "s/\/usr//"`
ln -s ..$mylib/uml/port-helper $RPM_BUILD_ROOT%{_bindir}/port-helper

%files
%doc COPYING Changelog
%attr(755,root,root) %dir %{_libdir}/uml
%attr(4750,root,uml-net) %{_bindir}/uml_net
%{_bindir}/jailtest
%{_bindir}/tunctl
%{_bindir}/uml_mconsole
%{_bindir}/uml_moo
%{_bindir}/uml_switch
%{_bindir}/uml_mkcow
%{_bindir}/uml_watchdog
%{_bindir}/port-helper
%{_libdir}/uml/port-helper
#%%attr(755,root,root) %%{_libdir}/uml/functions
#%%attr(755,root,root) %%{_bindir}/mkrootfs
#paul these were missing
%{_bindir}/uml_mount
%{_sbindir}/jail_uml
%{_bindir}/humfsify

%pre
getent group uml-net >/dev/null || groupadd -r uml-net
exit 0

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Petr Pisar <ppisar@redhat.com> - 20070815-25
- Fix building with glibc 2.28 (bug #1676173)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20070815-24
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 20070815-17
- Rebuild for readline 7.x

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20070815-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 20070815-11
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070815-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Paul Wouters <paul@xelerance.com> - 20070815-5
- Limited setuid binary to only members of the uml-net group

* Fri Feb 27 2009 Christian Krause <chkr@plauener.de> - 20070815-4
- use regular version tag
- fixed license tag
- updated Source0 URL
- removed unneeded BuildRequirement

* Sun Feb 15 2009 Christian Krause <chkr@plauener.de> - 20070815-3
- fix install parameter
- set LIB_DIR to fix installation on ppc64
- set CFLAGS to honor RPM_OPT_FLAGS

* Sun Nov  2 2008 Paul Wouters <paul@xelerance.com> - 20070815-2
- Added -q to setup

* Sat Nov  1 2008 Paul Wouters <paul@xelerance.com> - 20070815-1
- Was pointed to newer version of source at obscured location
- Hack out hardcoded stripping of binaries
- -D_FILE_OFFSET_BITS=64 no longer needed

* Tue Oct 28 2008 Paul Wouters <paul@xelerance.com> - 20060622-2
- Added a link to port-helper, so it is in the path

* Fri Oct 24 2008 Paul Wouters <paul@xelerance.com> - 20060622-1
- Initial package based on spec file in the sourcecode

