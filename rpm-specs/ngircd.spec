#
# Needed until upstream gcc10 porting is doen
# https://github.com/ngircd/ngircd/issues/266
#
%define _legacy_common_support 1

Name:           ngircd
Version:        25
Release:        7%{?dist}
Summary:        Next Generation IRC Daemon
License:        GPLv2+
URL:            http://ngircd.barton.de/
Source0:        http://ngircd.barton.de/pub/ngircd/ngircd-%{version}.tar.gz
Source1:        ngircd.init
Source2:        ngircd.service
# Listen only on localhost by default, set user/group
Patch0:         ngircd-fedora.patch
# Use system cipher list
Patch1:         ngircd-cipher.patch
# Patch for service file - no forking, no user/group for SSL key access, add doc,
# add CAP_KILL to allow reload
Patch2:         ngircd-service.patch

BuildRequires:  gcc
BuildRequires:  zlib-devel, avahi-compat-howl-devel
BuildRequires:  gnutls-devel
BuildRequires:  pam-devel
# Needed for tests
BuildRequires:  expect procps-ng telnet
%if 0%{?rhel} > 6 || 0%{?fedora}
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
%endif

Requires(pre): shadow-utils

%description
ngIRCd is a free open source daemon for Internet Relay Chat (IRC), 
developed under the GNU General Public License (GPL). It's written from 
scratch and is not based upon the original IRCd like many others.

%prep
%setup -q
%patch0 -p1 -b .fedora
# SYSTEM Cipher support in fedora and rhel > 7
%if 0%{?fedora} || 0%{?rhel} > 7
%patch1 -p1 -b .cipher
%endif
%patch2 -p1 -b .service

%build
%configure \
	--with-syslog \
	--with-zlib \
	--with-epoll \
	--with-zeroconf \
	--with-gnutls \
	--with-pam \
	--enable-ipv6

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%if 0%{?rhel} > 6 || 0%{?fedora}
# Upstream service file uses options only in newer systemd
%if 0%{?fedora}
install -D -m 644 contrib/ngircd.service %{buildroot}%{_unitdir}/ngircd.service
%else
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/ngircd.service
%endif
%else
install -D -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/ngircd
%endif

install -D -m 660 doc/sample-ngircd.conf %{buildroot}%{_sysconfdir}/ngircd.conf

mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -D -m 660 ./contrib/Debian/ngircd.pam %{buildroot}%{_sysconfdir}/pam.d/ngircd

touch  %{buildroot}%{_sysconfdir}/ngircd.motd
rm %{buildroot}%{_docdir}/ngircd/INSTALL
%if 0%{?rhel} > 6 || 0%{?fedora}
mkdir -p %{buildroot}%{_tmpfilesdir}
echo d /run/ngircd 0750 ngircd ngircd - > %{buildroot}%{_tmpfilesdir}/ngircd.conf
%else
mkdir -p %{buildroot}%{_localstatedir}/run/ngircd
%endif

%check
make check

%pre
getent group ngircd >/dev/null || groupadd -r ngircd
getent passwd ngircd >/dev/null || \
    useradd -r -g ngircd -d /tmp/ -s /sbin/nologin \
    -c "Next Generation IRC Daemon" ngircd
exit 0

%post
%if 0%{?rhel} > 6 || 0%{?fedora}
%systemd_post ngircd.service
%else
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add ngircd
%endif

%preun
%if 0%{?rhel} > 6 || 0%{?fedora}
%systemd_preun ngircd.service
%else
if [ $1 = 0 ]; then
        /sbin/service ngircd stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del ngircd
fi
%endif

%postun
%if 0%{?rhel} > 6 || 0%{?fedora}
%systemd_postun_with_restart ngircd.service
%else
if [ "$1" -ge "1" ]; then
        /sbin/service ngircd condrestart >/dev/null 2>&1 || :
fi
%endif

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%config(noreplace) %attr(660, root, ngircd) %{_sysconfdir}/ngircd.conf
%config(noreplace) %attr(660, root, ngircd) %{_sysconfdir}/pam.d/ngircd
%ghost %config(noreplace) %attr(660, root, ngircd) %{_sysconfdir}/ngircd.motd
%if 0%{?rhel} > 6 || 0%{?fedora}
%{_unitdir}/ngircd.service
%else
%{_initrddir}/ngircd
%endif
%{_sbindir}/ngircd
%{_docdir}/ngircd/
%{_mandir}/man5/ngircd.conf*
%{_mandir}/man8/ngircd.8*
%if 0%{?rhel} > 6 || 0%{?fedora}
%{_tmpfilesdir}/ngircd.conf
%else
%dir %attr(750, ngircd, ngircd) %{_localstatedir}/run/ngircd/
%endif

%changelog
* Sat May 16 2020 Kevin Fenzi <kevin@scrye.com> - 25-7
- rhel8 also has system cypher support, so add that before initial epel8 package.

* Sun Mar 29 2020 Kevin Fenzi <kevin@scrye.com> - 25-6
- Build with -fcommon for now until upstream gcc10 fixes land. Fixes FTBFS bug #1799688

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Orion Poplawski <orion@nwra.com> - 25-4
- Build without libident (bz#1790478)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Kevin Fenzi <kevin@scrye.com> - 25-1
- Update to 25. Fixes bug #1668960

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Kevin Fenzi <kevin@scrye.com> - 24-5
- Drop tcpwrappers support. Fixes bug #1518770

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Kevin Fenzi <kevin@scrye.com> - 24-1
- Update to 24. Fixes bug #1415350

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Orion Poplawski <orion@cora.nwra.com> 23-1
- Update to 23
- Update service file from upstream
- Base config file on upstream
- Use %%license, upstream doc install

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 06 2015 Kevin Fenzi <kevin@scrye.com> 22.1-1
- Update to 22.1

* Mon Jan 19 2015 Kevin Fenzi <kevin@scrye.com> 22-2
- Set default gnutls ciphers to "@SYSTEM". Fixes bug #1179328

* Mon Oct 13 2014 Kevin Fenzi <kevin@scrye.com> 22-1
- Update to 22. Fixes bug #1152080

* Fri Oct 03 2014 Kevin Fenzi <kevin@scrye.com> 21.1-6
- Sync ngircd.conf with sample template version. Fixes bug #1149012

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Kevin Fenzi <kevin@scrye.com> 21.1-4
- Set pam config to allow connections by default. 

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Kevin Fenzi <kevin@scrye.com> 21.1-2
- Enable pam support. Fixes bug #1092706

* Wed Mar 26 2014 Kevin Fenzi <kevin@scrye.com> 21.1-1
- Update to 21.1

* Fri Nov 01 2013 Kevin Fenzi <kevin@scrye.com> 21-1
- Update to 21

* Wed Sep 04 2013 Kevin Fenzi <kevin@scrye.com> 20.3-2
- Fix docs to not include Makefiles. Fixes bug #1004557

* Sat Aug 24 2013 Kevin Fenzi <kevin@scrye.com> 20.3-1
- Update to 20.3. Fixes bug #1000690
- Fix for CVE-2013-5580

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Kevin Fenzi <kevin@scrye.com> 20.2-1
- Update to 20.2.
- Fix for CVE-2013-1747

* Thu Mar  7 2013 Tomáš Mráz <tmraz@redhat.com> 20.1-2
- Rebuilt with new GnuTLS

* Sat Feb  2 2013 Kevin Fenzi <kevin@scrye.com> 20.1-1
- Update to 20.1
- Convert to systemd units for f19+

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Kevin Fenzi <kevin@scrye.com> - 18-2
- Fix config file typo. 

* Mon Aug 22 2011 Kevin Fenzi <kevin@scrye.com> - 18-1
- Update to 18

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Kevin Fenzi <kevin@tummy.com> - 17.1-2
- Fix up for tmpfs /var/run
- Remove fedora-usermgmt stuff
- Fix username in config file to match up. 

* Tue Dec 21 2010 Kevin Fenzi <kevin@tummy.com> - 17.1-1
- Update to 17.1

* Sun Nov 21 2010 Kevin Fenzi <kevin@tummy.com> - 17-1
- Update to 17

* Sun Jul 04 2010 Kevin Fenzi <kevin@tummy.com> - 16-1
- Update to 16
- Add ssl support with gnutls
- Add zeroconf support

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 Andreas Thienemann <andreas@bawue.net> 0.12.1-1
- Updated to 0.12.1
- Updated configuration sample

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.11.0-2
- fix license tag

* Mon Feb 11 2008 Andreas Thienemann <andreas@bawue.net> 0.11.0-1
- Updated to 0.11.0

* Tue Nov 20 2007 Andreas Thienemann <andreas@bawue.net> 0.10.3-1
- Rebased to 0.10.3
- Incorporated patches from fw@strlen.de

* Thu Apr 26 2007 Andreas Thienemann <andreas@bawue.net> 0.10.1-3
- Removed libident requirement
- Added patch from fw fixing server connections

* Mon Apr 02 2007 Andreas Thienemann <andreas@bawue.net> 0.10.1-2
- Added ngirc user

* Sat Mar 31 2007 Andreas Thienemann <andreas@bawue.net> 0.10.1-1
- Initial package

