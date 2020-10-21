Name:           libusb
Epoch:          1
Version:        0.1.7
Release:        2%{?dist}
Summary:        Compatibility shim around libusb-1.0 offering the old 0.1 API
License:        LGPLv2+
URL:            https://github.com/libusb/libusb-compat-0.1
Source0:        https://github.com/libusb/libusb-compat-0.1/releases/download/v%{version}/libusb-compat-%{version}.tar.bz2
Patch0:         libusb-config-multilib.patch
BuildRequires:  gcc libtool
BuildRequires:  libusb1-devel

%description
This package provides a shim / compatibility layer on top of libusb-1.0
offering the old 0.1 API for applications which do not have been ported
to the new 1.0 API yet. Where ever possible applications really should
use and / or be ported to the new 1.0 API instead of relying on this
compatibility library.


%package devel
Summary:        Development files for libusb
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files, libraries and documentation needed to
develop applications that use libusb-0.1. However new applications should use
libusb-1.0 library instead of this one.


%package        tests-examples
Summary:        Tests and examples for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description tests-examples
This package contains tests and examples for %{name}.


%prep
%autosetup -n libusb-compat-%{version}
autoreconf -ivf


%build
%configure --disable-static --enable-examples-build
%make_build


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/libusb.la
for i in lsusb testlibusb; do
    install -m 755 examples/.libs/$i \
        $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-$i
done


%check
LD_LIBRARY_PATH=libusb/.libs ldd -r $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-lsusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-lsusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-compat-0.1-testlibusb


%ldconfig_scriptlets


%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/libusb-0.1.so.*

%files devel
%{_includedir}/usb.h
%{_libdir}/libusb.so
%{_libdir}/pkgconfig/libusb.pc
%{_bindir}/libusb-config

%files tests-examples
%{_bindir}/libusb-compat-0.1-lsusb
%{_bindir}/libusb-compat-0.1-testlibusb


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 14 2020 Hans de Goede <hdegoede@redhat.com> - 1:0.1.7-1
- New upstream release 0.1.7 (rhbz#1805154)
- Add tests-examples sub-package and %%check

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.1.5-11
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Hans de Goede <hdegoede@redhat.com> - 0.1.5-3
- Revert atexit patch (rhbz#1003193)

* Wed Aug 14 2013 Hans de Goede <hdegoede@redhat.com> - 0.1.5-2
- Link with -znodelete to fix crash on unload of dl-opened code (rhbz#996760)

* Sun Aug 04 2013 Hans de Goede <hdegoede@redhat.com> - 0.1.5-1
- Update to 0.1.5 (#965414)
- Drop unused -static subpackage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jan 28 2013 Jindrich Novy <jnovy@redhat.com> 0.1.4-1
- update to 0.1.4 (#904748)
- drop upstreamed patches
- fix changelog dates

* Mon Nov 19 2012 Nils Philippsen <nils@redhat.com> - 1:0.1.3-12
- update sourceforge download URL

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Jan Vcelak <jvcelak@redhat.com> 0.1.3-9
- resolve multilib conflict in 'libusb-config' script

* Tue Jun 21 2011 Jan Vcelak <jvcelak@redhat.com> 0.1.3-8
- add libusb-config into -devel subpackage (#713483)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Jan Vcelak <jvcelak@redhat.com> 1:0.1.3-6
- pkg-config file has to be in /usr/lib/pkgconfig

* Tue Jan 25 2011 Jan Vcelak <jvcelak@redhat.com> 1:0.1.3-5
- move libraries from /usr/lib to /lib (#519716)

* Wed Sep 29 2010 jkeating - 1:0.1.3-4
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Jan Vcelak <jvcelak@redhat.com> 0.1.3-3
- add USB access error logging (#628356)
- update README

* Sat Aug 28 2010 Rex Dieter <rdieter@fedoraproject.org> 1:0.1.3-2
- fix epoch-related bustage

* Fri Aug 27 2010 Jan Vcelak <jvcelak@redhat.com> 0.1.3-1
- legacy libusb-0.1 replaced with libusb-compat

* Wed Jun 23 2010 Jan Vcelak <jvcelak@redhat.com> 0.1.12-23
- fixes invalid read causing segfault (#565904)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 21 2008 Jindrich Novy <jnovy@redhat.com> 0.1.12-20
- remove ExcludeArch: s390 s390x, libusb works fine there (#467768)

* Tue Oct 14 2008 Jindrich Novy <jnovy@redhat.com> 0.1.12-19
- don't apply the concurrency timeout handling patch, it breaks
  pilot-link (#456811)

* Mon Oct  6 2008 Jindrich Novy <jnovy@redhat.com> 0.1.12-18
- fix multiarch conflict in libusb-devel (#465209)

* Sat Aug  2 2008 Jindrich Novy <jnovy@redhat.com> 0.1.12-17
- apply patch from Graeme Gill to fix concurrency timeout
  handling (#456811)

* Fri Apr 18 2008 Jindrich Novy <jnovy@redhat.com> 0.1.12-16
- rebuild to fix broken ppc build

* Tue Feb 26 2008 Jindrich Novy <jnovy@redhat.com> 0.1.12-15
- don't apply wakeups patch until it's fixed, it causes problems
  with Eye-One Pro (#434950)

* Mon Feb 25 2008 Jindrich Novy <jnovy@redhat.com> 0.1.12-14
- manual rebuild because of gcc-4.3 (#434189)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.12-13
- Autorebuild for GCC 4.3

* Tue Dec  4 2007 Jindrich Novy <jnovy@redhat.com> 0.1.12-12
- remove unnecessary 1ms wakeups while USB transfers are in progress,
  thanks to Scott Lamb (#408131)

* Tue Nov  6 2007 Jindrich Novy <jnovy@redhat.com> 0.1.12-11
- fix multilib conflict in manual.ps (#342461)
- drop useless BR: gawk

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 0.1.12-10
- optimize usb_find_devices() and use openat() instead of open()
 (#273901), thanks to Ulrich Drepper
- BR gawk

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 0.1.12-9
- update License
- rebuild for BuildID

* Wed Aug  1 2007 Jindrich Novy <jnovy@redhat.com> 0.1.12-8
- don't use uninitialized buffers on stack (#250274)

* Thu Feb 08 2007 Jindrich Novy <jnovy@redhat.com> 0.1.12-7
- merge review spec fixes (#226053)
- create -static subpackage to ship static libs separately
- don't use auto* stuff, drop automake, libtool deps
- BuildRequire openjade, fix Requires

* Tue Dec 12 2006 Jindrich Novy <jnovy@redhat.com> 0.1.12-6
- fix BuildRoot, add dist tag, rpmlint warnfixes

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1.12-5.1
- rebuild

* Thu Jun 08 2006 Jesse Keating <jkeating@redhat.com> 0.1.12-5
- Add missing BR automake, libtool.
- Add missing Requires in -devel on pkgconfig

* Thu Jun  1 2006 Jindrich Novy <jnovy@redhat.com> 0.1.12-4
- remove .la files from libusb-devel (#172643)

* Tue May 30 2006 Jindrich Novy <jnovy@redhat.com> 0.1.12-3
- use pkg-config calls in libusb-config instead of hardcoded
  defaults to avoid multiarch conflicts (#192714)

* Fri May  5 2006 Jindrich Novy <jnovy@redhat.com> 0.1.12-2
- add docbook-utils-pdf BuildRequires (#191744)

* Mon Mar  6 2006 Jindrich Novy <jnovy@redhat.com> 0.1.12-1
- update to 0.1.12
- drop .format, .searchorder patches, applied upstream

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.1.11-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.1.11-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 27 2006 Jindrich Novy <jnovy@redhat.com> 0.1.11-2
- change device search order, /dev/bus/usb is tried first,
  then /proc/bus/usb, and never try /sys/bus/usb (#178994)

* Fri Jan 20 2006 Jindrich Novy <jnovy@redhat.com> 0.1.11-1
- 0.1.11
- require pkgconfig, package libusb.pc
- fix printf format in linux.c so that libusb can be built with -Werror (default)

* Mon Dec 19 2005 Tim Waugh <twaugh@redhat.com> 0.1.10a-3
- Rebuild.

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Mon Nov 21 2005 Tim Waugh <twaugh@redhat.com> 0.1.10a-2
- Build does not require xorg-x11-devel.  Fixes rebuild problem (no more
  xorg-x11-devel package).

* Wed Mar  9 2005 Tim Waugh <twaugh@redhat.com> 0.1.10a-1
- 0.1.10a.

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 0.1.10-2
- Rebuild for new GCC.

* Fri Feb 11 2005 Tim Waugh <twaugh@redhat.com> 0.1.10-1
- 0.1.10.

* Tue Feb  1 2005 Tim Waugh <twaugh@redhat.com> 0.1.9-1
- Build requires xorg-x11-devel.
- 0.1.9.

* Sat Jan 08 2005 Florian La Roche <laroche@redhat.com>
- rebuilt to get rid of legacy selinux filecontexts

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 25 2004 Tim Waugh <twaugh@redhat.com> 0.1.8-3
- Run aclocal/autoconf to make shared libraries work again.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 11 2004 Tim Waugh <twaugh@redhat.com> 0.1.8-1
- 0.1.8.

* Tue Jun 17 2003 Tim Waugh <twaugh@redhat.com> 0.1.7-3
- Fixed spec file.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Mar 19 2003 Tim Waugh <twaugh@redhat.com>
- Use the CFLAGS from the environment.

* Wed Mar 19 2003 Tim Waugh <twaugh@redhat.com> 0.1.7-1
- 0.1.7.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- exclude mainframe

* Tue Jun 25 2002 Tim Waugh <twaugh@redhat.com> 0.1.6-1
- 0.1.6.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.1.5-6
- automated rebuild

* Fri Jun 21 2002 Tim Waugh <twaugh@redhat.com> 0.1.5-5
- Rebuild to fix broken deps.

* Thu May 23 2002 Tim Powers <timp@redhat.com> 0.1.5-4
- automated rebuild

* Thu Apr 11 2002 Tim Waugh <twaugh@redhat.com> 0.1.5-3
- Rebuild (fixes bug #63196).

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 0.1.5-2
- Rebuild in new environment.

* Thu Feb  7 2002 Tim Waugh <twaugh@redhat.com> 0.1.5-1
- 0.1.5.

* Fri Jan 25 2002 Tim Waugh <twaugh@redhat.com> 0.1.4-2
- Rebuild in new environment.
- Work around tarball brokenness (doc directory was not automade).

* Mon Oct 29 2001 Tim Waugh <twaugh@redhat.com> 0.1.4-1
- Adapted for Red Hat Linux.
- 0.1.4.

* Thu Mar  1 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1.3b-1mdk
- Initial Mandrake release
