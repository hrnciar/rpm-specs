Name:           ez-ipupdate
Version:        3.0.11
Release:        0.42.b8%{?dist}
Summary:        Client for Dynamic DNS Services

## Note: Upstream is no longer reachable. Thanks to openSUSE and
## Debian for maintaning the code, patches have been gathered from
## there.

License:        GPLv2+
URL:            http://www.gusnet.cx/proj/ez-ipupdate/
Source0:        http://www.gusnet.cx/proj/ez-ipupdate/dist/ez-ipupdate-3.0.11b8.tar.gz

## Fedora specific patches ##
## systemd unit
Source1:        %{name}.service
# Make code and man page match.
Patch1:         %{name}-pidfile.patch
# Hopefully improve error handling.
Patch3:         %{name}-returnvalues.patch
# Remove options which conflict with the way the service is started.
Patch4:         %{name}-shortexamples.patch

## Patches from openSUSE ##
# Build fix.
Patch11:         ez-ipupdate-3.0.11b8-include.diff
# Security.
Patch12:         ez-ipupdate-format-string-vuln.patch
# Build fix.
Patch13:         ez-ipupdate-includes.patch
# Feature patch, add support for dnsexit dyndns service.
Patch14:         ez-ipupdate-dnsexit.patch
# Various fixes for configure.ac and Makefile.am
Patch15:         ez-ipupdate-fix_autofoo.patch
# Feature patch, add support for joker.com dyndns service
Patch16:         ez-ipupdate-joker_com.patch
# Do type punning via memcpy
Patch17:         ez-ipupdate-type-punning.patch
# Reduce compiler warnings.
Patch18:         ez-ipupdate-code_cleanup.patch

## Patches from Debian ##
Patch30:         http://ftp.de.debian.org/debian/pool/main/e/ez-ipupdate/ez-ipupdate_3.0.11b8-13.4.diff.gz

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires:  gcc
BuildRequires: systemd autoconf automake
Requires(pre):    /usr/sbin/useradd /usr/sbin/groupadd

%description
ez-ipupdate is a utility for updating DNS records at a number of
different dynamic DNS services.


%prep
%setup -q -n %{name}-%{version}b8

%patch11 -p1
%patch12 -p1
%patch13
%patch14
mv configure.in configure.ac
%patch15
%patch16
%patch17
%patch18
rm acconfig.h

%patch30 -p1

mv debian/*.8 .

# autotools stuff
patch <debian/patches/010_rebootstrap.diff -p1
# code fixes
patch <debian/patches/102_misc_crashes.diff -p1
# code fixes
patch <debian/patches/103_protocol.diff -p1
# code fixes
patch <debian/patches/104_misc_crashes.diff -p0
# text fixes
patch <debian/patches/150_cosmetic.diff -p1

%patch1 -p0

touch *.in aclocal.m4 configure
chmod +x missing
chmod a-x example*.conf

%patch3 -p0
find -name "example*" | xargs -n 1 sed -i "s@/usr/local/bin/@/usr/bin/@"
%patch4 -p0

%build
export CFLAGS="-D_FILE_OFFSET_BITS=64 $RPM_OPT_FLAGS"
autoreconf -fiv
%configure
make %{?_smp_mflags}
echo >tmpfiles.conf 'd %{_localstatedir}/run/%{name} 0755 ez-ipupd ez-ipupd -'


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT bindir=%{_sbindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
cp -p ez-ipupdate.8 $RPM_BUILD_ROOT%{_mandir}/man8

install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}@.service

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/%{name}
> $RPM_BUILD_ROOT%{_localstatedir}/cache/%{name}/default.cache

# Make a directory for config files
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
> $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/default.conf

# Create a dedicated dir for the pid file so we can run as non-root.
mkdir -p $RPM_BUILD_ROOT/run
install -d -m 0755 $RPM_BUILD_ROOT/run/%{name}/

# Also recreate the directory if needed.
mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
install -m 0644 tmpfiles.conf $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf




%pre
/usr/sbin/groupadd -r ez-ipupd >/dev/null 2>&1 || :
/usr/sbin/useradd -r -M -d %{_localstatedir}/cache/%{name} -g ez-ipupd \
  -s /sbin/nologin -c "Dynamic DNS Client" ez-ipupd >/dev/null 2>&1 || :

%post
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}@.service

%postun
%systemd_postun %{name}@.service


%files
%doc COPYING README example.conf example-*.conf
%attr(0644,root,root) %{_mandir}/man8/ez-ipupdate.*
%attr(0755,root,root) %{_sbindir}/ez-ipupdate
%attr(0644,root,root) %{_unitdir}/%{name}@.service
%attr(0644,root,root) %{_tmpfilesdir}/%{name}.conf
%attr(0750,root,ez-ipupd) %dir %{_sysconfdir}/%{name}
%ghost %attr(0640,root,ez-ipupd) %config(noreplace,missingok) %{_sysconfdir}/%{name}/default.conf
%attr(0755,ez-ipupd,ez-ipupd) %dir /run/%{name}/
%attr(0750,ez-ipupd,ez-ipupd) %dir %{_localstatedir}/cache/%{name}/
%ghost %attr(0640,ez-ipupd,ez-ipupd) %{_localstatedir}/cache/%{name}/default.cache


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.42.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.41.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.40.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.39.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.38.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.37.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.36.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.35.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.34.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-0.33.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.32.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.31.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.30.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Alexander Boström <abo@root.snowtree.se> - 3.0.11-0.29.b8
- Improve systemd unit file and fix broken tmpfiles handling.
- Pull patches from openSUSE and Debian and fix error handling.
- General tidying up.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.28.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.27.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.26.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Jon Ciesla <limburgher@gmail.com> - 3.0.11-0.25.b8
- Migrate to systemd, BZ 767801.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.24.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.23.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.22.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.11-0.21.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.0.11-0.20.b8
- fix license tag

* Mon Jun 16 2008 Jeff Layton <jlayton@redhat.com> - 3.0.11-0.19.b8
- compile with -D_FILE_OFFSET_BITS=64 so we can handle 64-bit inode numbers
  in stat() calls

* Sun Jun  8 2008 Jeff Layton <jlayton@redhat.com> - 3.0.11-0.18.b8
- default server for zoneedit has changed to dynamic.zoneedit.com (BZ#449375)

* Tue Mar 11 2008 Jeff Layton <jlayton@redhat.com> - 3.0.11-0.17.b8
- ez-ipupdate would be started a second time on runlevel changes (BZ#436616)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0.11-0.16.b8
- Autorebuild for GCC 4.3

* Sun Jul 15 2007 Jeff Layton <jlayton@redhat.com> - 3.0.11-0.15.b8
- initscript: add LSB header and fix return values
- initscript: remove /var/lock/subsys references

* Fri Jun 15 2007 J. Randall Owens <jrowens@ghiapet.homeip.net> - 3.0.11-0.14.b8
- fix doc directory permissions

* Thu Mar  8 2007 Jeff Layton <jlayton@redhat.com> - 3.0.11-0.13.b8
- remove Requires(postun) for user/groupdel since they're no longer needed

* Tue Sep 12 2006 Jeff Layton <jlayton@redhat.com> - 3.0.11-0.12.b8
- clean up changelog for specfile

* Tue Sep 12 2006 Jeff Layton <jlayton@redhat.com> - 3.0.11-0.11.b8
- rebuild for FC6

* Sat Jul 1 2006 Jeff Layton <jlayton@redhat.com> - 3.0.11-0.10.b8
- new init script that can handle more than one config file
- move config files into directory under sysconfdir
- don't remove user and group on exit
- don't set permissions explicitly except where needed

* Wed Feb 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.0.11-0.9.b8
- Sync with Debian's 3.0.11b8-10.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 3.0.11-0.8.b8
- rebuilt

* Sun Nov 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.11-0.7.b8
- Update patch from Debian to 3.0.11b8-8, fixes CAN-2004-0980.
- Try harder to avoid (re-)running aclocal and friends during build.
- Cosmetic specfile improvements.

* Wed Nov 10 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:3.0.11-0.6.b8
- Fix build on FC3 (add "chmod +x missing" in %%prep).

* Sat Jul 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.11-0.fdr.0.5.b8
- Update patch from Debian to 3.0.11b8-6 (bug 337).
- Revert default-cache to %%ghost (it's not a %%config file).

* Sat Jul 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.11-0.fdr.0.4.b8
- Own (ghost/config) %%{_sysconfdir}/ez-ipupdate.conf (bug 337).
- Change default-cache to ghost/config.

* Tue Jun 17 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.11-0.fdr.0.3.b8
- Fix "service ez-update status" hang if no cache-file is specified,
  thanks to Michael Schwendt for the catch (#337).
- Try to show last IP update from "service ez-ipupdate status" only if the
  config file is readable.

* Thu Jun  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.11-0.fdr.0.2.b8
- Fix bad in files section (#337).

* Tue May 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.11-0.fdr.0.1.b8
- First build, based on Debian's 3.0.11b8_2 and Rudolf Kastl's work.
