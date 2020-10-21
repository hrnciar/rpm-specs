Summary:        Performs a verified launch using Intel TXT
Name:           tboot
Version:        1.9.11
Release:        3%{?dist}
Epoch:          1

License:        BSD
URL:            http://sourceforge.net/projects/tboot/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Patch0:         disable-address-of-packed-member-warning.patch
Patch1:         tboot-gcc11.patch

BuildRequires:  gcc
BuildRequires:  trousers-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
ExclusiveArch:  %{ix86} x86_64

%description
Trusted Boot (tboot) is an open source, pre-kernel/VMM module that uses
Intel Trusted Execution Technology (Intel TXT) to perform a measured
and verified launch of an OS kernel/VMM.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
make debug=y %{?_smp_mflags}

%install
make debug=y DISTDIR=$RPM_BUILD_ROOT install


%files
%doc README COPYING docs/* lcptools/Linux_LCP_Tools_User_Manual.pdf
%config %{_sysconfdir}/grub.d/20_linux_tboot
%config %{_sysconfdir}/grub.d/20_linux_xen_tboot
%{_sbindir}/acminfo
%{_sbindir}/lcp_readpol
%{_sbindir}/lcp_writepol
%{_sbindir}/lcp2_crtpol
%{_sbindir}/lcp2_crtpolelt
%{_sbindir}/lcp2_crtpollist
%{_sbindir}/lcp2_mlehash
%{_sbindir}/parse_err
%{_sbindir}/tb_polgen
%{_sbindir}/tpmnv_defindex
%{_sbindir}/tpmnv_getcap
%{_sbindir}/tpmnv_lock
%{_sbindir}/tpmnv_relindex
%{_sbindir}/txt-stat
%{_mandir}/man8/acminfo.8.gz
%{_mandir}/man8/lcp_crtpconf.8.gz
%{_mandir}/man8/lcp_crtpol.8.gz
%{_mandir}/man8/lcp_crtpol2.8.gz
%{_mandir}/man8/lcp_crtpolelt.8.gz
%{_mandir}/man8/lcp_crtpollist.8.gz
%{_mandir}/man8/lcp_mlehash.8.gz
%{_mandir}/man8/lcp_readpol.8.gz
%{_mandir}/man8/lcp_writepol.8.gz
%{_mandir}/man8/tb_polgen.8.gz
%{_mandir}/man8/txt-stat.8.gz
/boot/tboot.gz
/boot/tboot-syms

%changelog
* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 1:1.9.11-3
- Explicitly allow uninitialized variables in a few places that do it
- on purpose

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 19 2020 Filipe Rosset <rosset.filipe@gmail.com> - 1:1.9.11-1
- Update to 1.9.11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Yunying Sun <yunying.sun@intel.com> - 1:1.9.10-1
- Add patch to fix package build error
- Add build dependency to zlib-devel
- Update to latest release 1.9.10

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Yunying Sun <yunying.sun@intel.com> - 1:1.9.8-1
- Updated to upstream 1.9.8 release

* Tue Sep 4 2018 Yunying Sun <yunying.sun@intel.com> - 1:1.9.7-1
- Updated to upstream 1.9.7 release
- Removed the patch for openssl 1.1 as it is included in 1.9.7 already

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Tomáš Mráz <tmraz@redhat.com> - 1:1.9.6-2
- Patch to build with OpenSSL-1.1.x

* Sun Feb 04 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1:1.9.6-1
- Upgrade to latest upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Gang Wei <gang.wei@intel.com> - 1:1.8.2-1
- Upgrade to latest upstream version which provided security fix for:
  tboot:argument measurement vulnerablity for GRUB2+ELF kernels

* Wed Jun 18 2014 Gang Wei <gang.wei@intel.com> - 1:1.8.1-1
- Upgrade to latest upstream version

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Gang Wei <gang.wei@intel.com> - 1:1.7.3-3
- Fix for breaking grub2-mkconfig operation in 32bit case(#929384)

* Wed Feb 20 2013 Gang Wei <gang.wei@intel.com> - 1:1.7.3-2
- Fix version string in log

* Wed Jan 30 2013 David Cantrell <dcantrell@redhat.com> - 1:1.7.3-1
- Upgrade to latest upstream version (#902653)

* Wed Aug 22 2012 Gang Wei <gang.wei@intel.com> - 1:1.7.0-2
- Fix build error with zlib 1.2.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 15 2012 Gang Wei <gang.wei@intel.com> - 1:1.7.0
- 1.7.0 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110429-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 29 2011 Gang Wei <gang.wei@intel.com> - 20110429-1
- Pull upstream changeset 255, rebuilt in F15

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 1 2010 Joseph Cihula <joseph.cihula@intel.com> - 20101005-1.fc13
- Initial import
