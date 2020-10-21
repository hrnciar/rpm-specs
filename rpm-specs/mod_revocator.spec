%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}

Name: mod_revocator
Version: 1.0.3
Release: 35%{?dist}
Summary: CRL retrieval module for the Apache HTTP server
License: ASL 2.0
URL: http://directory.fedoraproject.org/wiki/Mod_revocator
Source: http://directory.fedoraproject.org/sources/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires: nspr-devel >= 4.6, nss-devel >= 3.11.9
BuildRequires: nss-pkcs11-devel >= 3.11
BuildRequires: nss-pkcs11-devel-static
BuildRequires: httpd-devel >= 0:2.0.52, apr-devel, apr-util-devel
BuildRequires: pkgconfig, autoconf, automake, libtool
BuildRequires: openldap-devel >= 2.2.29
Requires: mod_nss >= 1.0.8
Requires: httpd-mmn = %{_httpd_mmn}
Patch1: mod_revocator-libpath.patch
Patch2: mod_revocator-kill.patch
Patch3: mod_revocator-segfault-fix.patch
Patch4: mod_revocator-32-bit-semaphore-fix.patch
Patch5: mod_revocator-array-size.patch
Patch6: mod_revocator-waitpid.patch
Patch7: mod_revocator-man.patch

%description
The mod_revocator module retrieves and installs remote
Certificate Revocate Lists (CRLs) into an Apache web server. 

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
autoreconf -fvi

# Needed for ppc64, automake can't be run here
for file in %{_datadir}/automake-*/config.{guess,sub}
do
    cp -f $file .
done

CFLAGS="$RPM_OPT_FLAGS"
export CFLAGS

NSPR_INCLUDE_DIR=`/usr/bin/pkg-config --variable=includedir nspr`
NSPR_LIB_DIR=`/usr/bin/pkg-config --variable=libdir nspr`

NSS_INCLUDE_DIR=`/usr/bin/pkg-config --variable=includedir nss`
NSS_LIB_DIR=`/usr/bin/pkg-config --variable=libdir nss`

NSS_BIN=`/usr/bin/pkg-config --variable=exec_prefix nss`

%configure \
    --with-nss-lib=$NSS_LIB_DIR \
    --with-nss-inc=$NSS_INCLUDE_DIR \
    --with-nspr-lib=$NSPR_LIB_DIR \
    --with-nspr-inc=$NSPR_INCLUDE_DIR \
    --with-apr-config --enable-openldap \
    --with-apxs=%{_httpd_apxs}

make %{?_smp_flags} all

%install
# The install target of the Makefile isn't used because that uses apxs
# which tries to enable the module in the build host httpd instead of in
# the build root.
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_httpd_confdir} $RPM_BUILD_ROOT%{_httpd_modconfdir} \
       $RPM_BUILD_ROOT%{_libdir}/httpd/modules $RPM_BUILD_ROOT%{_bindir}      \
       $RPM_BUILD_ROOT%{_libexecdir} $RPM_BUILD_ROOT%{_sbindir}               \
       $RPM_BUILD_ROOT%{_mandir}/man8

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# httpd >= 2.4.x
sed -n /^LoadModule/p revocator.conf > 11-revocator.conf
sed -i /^LoadModule/d revocator.conf
install -m 644 11-revocator.conf $RPM_BUILD_ROOT%{_httpd_modconfdir}/11-revocator.conf
%endif
install -m 644 revocator.conf $RPM_BUILD_ROOT%{_httpd_confdir}/revocator.conf
install -m 755 .libs/libmodrev.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_rev.so
install -m 644 ldapget.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install -m 644 crlhelper.8 $RPM_BUILD_ROOT%{_mandir}/man8/
# Ugh, manually create the ldconfig symbolic links
version=`grep -v '^\#' ./libtool-version`
current=`echo $version | cut -d: -f1`
revision=`echo $version | cut -d: -f2`
age=`echo $version | cut -d: -f3`
install -m  755 .libs/librevocation.so.$current.$revision.$age $RPM_BUILD_ROOT%{_libdir}/
# install missing symlink (was giving no-ldconfig-symlink rpmlint errors)
ldconfig -n $RPM_BUILD_ROOT%{_libdir}
(cd $RPM_BUILD_ROOT%{_libdir} && ln -s librevocation.so.$current.$revision.$age librevocation.so.0)
(cd $RPM_BUILD_ROOT%{_libdir} && ln -s librevocation.so.$current.$revision.$age  librevocation.so)
install -m 755 ldapget $RPM_BUILD_ROOT%{_sbindir}/
install -m 755 crlhelper $RPM_BUILD_ROOT%{_libexecdir}/
# Provide compatibility links to prevent disruption of customized deployments.
#
#     NOTE:  These links may be deprecated in a future release
#            of 'mod_revocator'.
#
ln -s %{_sbindir}/ldapget $RPM_BUILD_ROOT%{_bindir}/ldapget
ln -s %{_libexecdir}/crlhelper $RPM_BUILD_ROOT%{_bindir}/crlhelper

%ldconfig_scriptlets

%files
%doc README LICENSE docs/mod_revocator.html
%{_mandir}/man8/*
%config(noreplace) %{_httpd_confdir}/*.conf
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/*.conf
%endif
%{_libdir}/httpd/modules/mod_rev.so
# rpmlint will complain that librevocation.so is a shared library but this
# must be ignored because this file is loaded directly by name by the Apache
# module.
%{_libdir}/librevocation.*so*
%{_sbindir}/ldapget
%{_libexecdir}/crlhelper
%{_bindir}/ldapget
%{_bindir}/crlhelper

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-30
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 08 2016 Matthew Harmsen <mharmsen@redhat.com> - 1.0.3-25
Bumped release number to force rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.3-22
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 1.0.3-19
- fix _httpd_mmn expansion in absence of httpd-devel

* Tue Jul 30 2013 Joe Orton <jorton@redhat.com> - 1.0.3-18
- add dependency on httpd-mmn

* Tue Jul  9 2013 Matthew Harmsen <mharmsen@redhat.com> - 1.0.3-17
- rpmlint mod_revocator.spec
  0 packages and 1 specfiles checked; 0 errors, 0 warnings.
- rpmlint mod_revocator-1.0.3-16 (SRPM)
  W: spelling-error %%description -l en_US revocator -> equivocator
  1 packages and 0 specfiles checked; 0 errors, 1 warnings.
- rpmlint mod_revocator-1.0.3-16 (RPM)
  W: spelling-error %%description -l en_US revocator -> equivocator
  W: devel-file-in-non-devel-package /usr/lib64/librevocation.so
  1 packages and 0 specfiles checked; 0 errors, 2 warnings.
- rpmlint mod_revocator-debuginfo-1.0.3-16 (RPM)
  W: spelling-error Summary(en_US) revocator -> equivocator
  W: spelling-error %%description -l en_US revocator -> equivocator
  1 packages and 0 specfiles checked; 0 errors, 2 warnings.

* Wed Jul  3 2013 Matthew Harmsen <mharmsen@redhat.com> - 1.0.3-16
- Bugzilla Bug #948875 - Man page scan results for mod_revocator
- Moved 'ldapget' from %%bindir to %%sbindir (provided compatibility link)
- Moved 'crlhelper' from %%bindir to %%libexecdir (provided compatibility link)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct  8 2012 Matthew Harmsen <mharmsen@redhat.com> - 1.0.3-14
- Bugzilla Bug #861999 - mod_revocator exec CLR URIs fail to load: unable to
  load Revocation module, NSS error -8187 - stephen.capstick64@gmail.com
  (mod_revocator-waitpid.patch)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Joe Orton <jorton@redhat.com> - 1.0.3-12
- use 11- prefix for config file w/2.4

* Wed Apr 18 2012 Joe Orton <jorton@redhat.com> - 1.0.3-11
- fix deps, packaging for 2.4 (#803074)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Matthew Harmsen <mharmsen@redhat.com> - 1.0.3-9
- Bugzilla Bug #716874 - httpd (32 bit) failed to start if mod_revocator
  (32 bit) is installed on ppc64

* Fri Oct 21 2011 Matthew Harmsen <mharmsen@redhat.com> - 1.0.3-7
- Bugzilla Bug #716355 - mod_revocator does not shut down httpd server if
  expired CRL is fetched
- Bugzilla Bug #716361 - mod_revocator does not bring down httpd server if
  CRLUpdate fails

* Tue Oct 11 2011 Matthew Harmsen <mharmsen@redhat.com> - 1.0.3-6
- Bugzilla Bug #737556 - CRLS are not downloaded when mod_revocator module
  is loaded successfully. And no error was thrown in httpd error_log -
  mharmsen
- Add 'autoreconf -fvi' to build section - mharmsen
- Fix shutting down Apache if CRLUpdateCritical is on and a CRL
  is not available at startup (#654378) - rcritten@redhat.com
- Updated mod_revocator-kill patch. The ownership of the semaphore used to
  control access to crlhelper was not always changed to the Apache user
  (#648546) - rcritten@redhat.com
- Actually apply the patch (#648546) - rcritten@redhat.com
- Fix killing the web server if updatecritical is set (#648546) -
  rcritten@redhat.com

* Mon Mar  7 2011 Rob Crittenden <rcritten@redhat.com> - 1.0.3-4
- Use correct package name, nss-pkcs11-devel-static (#640293)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct  5 2010 Rob Crittenden <rcritten@redhat.com> - 1.0.3-2
- Add BuildRequires: nss-pkcs11-static (#640293)

* Wed Apr 14 2010 Rob Crittenden <rcritten@redhat.com> - 1.0.3-1
- Update to upstream 1.0.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 04 2009 Robert Scheck <robert@fedoraproject.org> - 1.0.2-7
- Solve the ppc64-redhat-linux-gnu configure target error

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-5
- fix license tag

* Mon Feb 25 2008 Rob Crittenden <rcritten@redhat.com> 1.0.2-4
- The nss package changed the location of the NSS shared libraries to /lib from
  /usr/lib. Static libraries remained in /usr/lib. They then updated their
  devel package to put symlinks back from /lib to /usr. Respin to pick that up.
  BZ 434395.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2-3
- Autorebuild for GCC 4.3

* Wed Dec  5 2007 Rob Crittenden <rcritten@redhat.com> 1.0.2-2
- Respin to pick up new openldap

* Mon Oct 16 2006 Rob Crittenden <rcritten@redhat.com> 1.0.2-1
- Initial build
