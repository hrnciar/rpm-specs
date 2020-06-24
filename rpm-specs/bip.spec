#global prerel  rc3
%global commit      c9cc64f2e1932339ddd08d39261331f6b6ceee71
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20181225

Name:    bip
Version: 0.9.0
Release: 0.7.%{date}git%{shortcommit}%{?dist}
Summary: IRC Bouncer
License: GPLv2+
URL: http://bip.t1r.net

#Source0: https://projects.duckcorp.org/attachments/download/87/bip-%{version}-%{prerel}.tar.gz
# git clone https://vcs-git.duckcorp.org/projects/bip/bip.git
# git archive --prefix=bip/ (commit) | gzip > bip-(commit).tar.gz
Source0: bip-%{commit}.tar.gz
# Fedora 15+ - ensure that /var/run/bip is created on system start
# http://bugzilla.redhat.com/show_bug.cgi?id=707294
Source2: bip-tmpfs.conf
Source3: bip.service
Patch0: 0001-Setup-bip-for-Fedora-s-paths.patch
Patch1: 0002-Throttle-joins-to-prevent-flooding.patch
# Fix a build failure:
# https://bugzilla.redhat.com/show_bug.cgi?id=1799189
Patch2: 0001-Fix-stringop-truncation-error-thanks-DJ-Delorie.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: byacc
BuildRequires: flex
BuildRequires: gcc
BuildRequires: m4
BuildRequires: openssl-devel
BuildRequires: perl-generators
BuildRequires: systemd-units
BuildRequires: git
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
Bip is an IRC proxy, which means it keeps connected to your preferred IRC
servers, can store the logs for you, and even send them back to your IRC
client(s) upon connection.
You may want to use bip to keep your logfiles (in a unique format and on a
unique computer) whatever your client is, when you connect from multiple
workstations, or when you simply want to have a playback of what was said
while you were away.

%prep
%autosetup -n %{name} -p1

iconv -f iso-8859-1 -t utf-8 -o ChangeLog{.utf8,}
mv ChangeLog{.utf8,}


%build
# for git snapshots
autoreconf -i
%configure --with-openssl
make CFLAGS="$RPM_OPT_FLAGS -fPIE -Wno-unused-result -Wno-error=format-truncation"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# Remove misplaced files
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/bip
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
# Install bip.conf
install -m 0644 samples/bip.conf $RPM_BUILD_ROOT%{_sysconfdir}/bip.conf
# Install bipgenconfig
install -m 0755 scripts/bipgenconfig $RPM_BUILD_ROOT%{_bindir}/bipgenconfig
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/bip
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/bip

install -d -m 755 $RPM_BUILD_ROOT%{_tmpfilesdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_tmpfilesdir}/bip.conf

# Install systemd service file
install -d -m 755 $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/


%pre
/usr/sbin/useradd -c "Bip IRC Proxy" \
  -s /bin/sh -r -d / bip 2> /dev/null || :

%post
%systemd_post bip.service
/bin/systemd-tmpfiles --create %{_tmpfilesdir}/bip.conf

%preun
%systemd_preun bip.service

%postun
%systemd_postun_with_restart bip.service

%triggerun -- bip < 0.8.8-2
/usr/bin/systemd-sysv-convert --save bip >/dev/null 2>&1 ||:
/sbin/chkconfig --del bip >/dev/null 2>&1 || :
/bin/systemctl try-restart bip.service >/dev/null 2>&1 || :

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%doc samples/bip.vim
%{_bindir}/bip
%{_bindir}/bipgenconfig
%{_bindir}/bipmkpw
%{_mandir}/man1/bip.1.gz
%{_mandir}/man5/bip.conf.5.gz
%{_mandir}/man1/bipmkpw.1.gz
%attr(0640,root,bip) %config(noreplace) %{_sysconfdir}/bip.conf
%config %{_tmpfilesdir}/bip.conf
%attr(-,bip,bip) %ghost %{_localstatedir}/run/bip
%attr(-,bip,bip) %dir %{_localstatedir}/log/bip
%{_unitdir}/bip.service

%changelog
* Thu Apr 23 2020 Tom Hughes <tom@compton.nu> - 0.9.0-0.7.20181225gitc9cc64f
- Fix patch to correctly terminate strings

* Fri Feb 07 2020 Adam Williamson <awilliam@redhat.com> - 0.9.0-0.6.20181225gitc9cc64f
- Fix a build failure on Rawhide (thanks DJ Delorie)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.5.20181225gitc9cc64f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.4.20181225gitc9cc64f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Adam Williamson <awilliam@redhat.com> - 0.9.0-0.3.20181225gitc9cc64f
- Bump to latest git (with fixes for GCC 9 compile errors)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.2.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Adam Williamson <awilliam@redhat.com> - 0.9.0-0.1.rc3
- Bump to new release 0.9.0rc3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.9-16
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Adam Williamson <awilliam@redhat.com> - 0.8.9-12
- Specify HOME in bip.service, seems to be needed on F26+ (#1468379)
- Backport some upstream patches for OpenSSL 1.1 compatibility
- Fix some bad 'const const' declarations (upstream #580)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 31 2016 Brian C. Lane <bcl@redhat.com> 0.8.9-10
- Use %%{_tmpfilesdir} macro instead of /etc/tmpfiles.d

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Brian C. Lane <bcl@redhat.com> 0.8.9-7
- Send logs to the journal instead of a logfile (#1185131)

* Wed Dec 10 2014 Adam Williamson <awilliam@redhat.com> - 0.8.9-6
- backport a couple of patches that make CA mode TLS validation work OOTB

* Mon Oct 06 2014 Brian C. Lane <bcl@redhat.com> 0.8.9-5
- Use network-online.target (#862610)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 18 2013 Brian C. Lane <bcl@redhat.com> 0.8.9-2
- Scriptlets replaced with new systemd macros (#850046)

* Sat Nov 09 2013 Brian C. Lane <bcl@redhat.com> 0.8.9-1
- Upstream v0.8.9
- CVE-2013-4550 - failed SSL handshake resource leak
- Removed 2 patches included in new version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.8.8-9
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Brian C. Lane <bcl@redhat.com> 0.8.8-6
- Change /etc/bip.conf to 0640,root,bip (#815935)

* Fri Apr 13 2012 Adam Williamson <awilliam@redhat.com> - 0.8.8-5
- upstream patch to fix privmsg logs being split up (upstream #252)

* Tue Jan 24 2012 Brian C. Lane <bcl@redhat.com> - 0.8.8-4
- Upstream patch to fix buffer overflow with too many open fd's (#784301)
  https://projects.duckcorp.org/issues/269
- Switched spec to use git to apply patches

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Brian C. Lane <bcl@redhat.com> - 0.8.8-2
- Adding systemd unit file and removing sysvinit file

* Fri Jul 29 2011 Brian C. Lane <bcl@redhat.com> - 0.8.8-1
- Upstream v0.8.8

* Thu Jun  2 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.8.7-2
- Create file: /etc/tmpfiles.d/bip.conf
- Fixes #707294 - /var/run/bip on tmpfs

* Sat Feb 12 2011 Brian C. Lane <bcl@redhat.com> - 0.8.7-1
- Upstream v0.8.7
- New source tarball location
- Update spec with %%ghost for /var/run/bip/

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 06 2010 Brian C. Lane <bcl@redhat.com> - 0.8.6-1
- Upstream v0.8.6

* Sat Mar 27 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 0.8.4-3
- Install bipgenconfig as requested in bz #566879

* Mon Feb 1 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 0.8.4-2
- Import patch reported by Kevin Fenzi (bz #560476)
- + Add a join delay to work around ircd7 flood protection
- + Add support for the "quiet" list

* Fri Jan  8 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 0.8.4-1
- 0.8.4

* Thu Sep 03 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 0.8.2-1
- 0.8.2

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.8.0-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 0.8.0-1
- 0.8.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 0.7.5-3
- rebuild with new openssl

* Sat Nov 29 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.5-2
- rebuilt

* Sat Nov 29 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.5-1
- 0.7.5
- Added support for running bip as system daemon
  (patches from Tom Hughes, thanks! - BugID: 471791)

* Tue Jun 08 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.4-1
- New version

* Tue May 06 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.2-6
- Removed _smp_mflags to avoid compilation errors with parallel jobs

* Wed Apr 30 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.2-5
- Corrected License field
- Removed openssl from Requires

* Wed Apr 30 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.2-4
- Convert ChangeLog to utf-8 in prep
- Ensure that package is compiled using RPM_OPT_FLAGS
- Make usage of RPM_BUILD_ROOT consistent
- Removed macros from ChangeLog (bad mistake)

* Mon Apr 14 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.2-3
- Removed INSTALL from doc

* Sun Apr 13 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.2-2
- Added AUTHORS, ChangeLog, COPYING, INSTALL, README, TODO to docdir
- added --enable-ssl to configure, just to make sure that bip is built
  with SSL support using OpenSSL

* Sat Apr 12 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.2-1
- Version bump

* Sun Mar 16 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 0.7.0-1
- Initial release
