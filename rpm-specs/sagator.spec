%define CHROOTDIR %{_var}/spool/vscan
%define BASE_LIBS glibc,libgcc,expat,libstdc++,zlib,bzip2-libs,cracklib,cracklib-dicts
%define ARCHIVERS tar,arc,unace,unrar,rar,zoo,unarj,arj,unzip,zip,gzip,bzip2
%define ANTIVIRS clamav,clamav-libs,avglinux,nod32ls,nod32lfs,kav4mailservers-linux
%define ANTISPAMS bogofilter,qsf
%define CLAMAV_VERSION 0.92

# SElinux policy for Fedoras and RHEL>=5
%if 0%{?fedora} || 0%{?rhel} >= 5
# SElinux temporarily disabled for all systems
%define install_sepolicy 0
%define sepolicy %{_datadir}/%{name}/selinux/%{name}.pp
%endif

%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
%define python_version python3
%else
%define python_version python2
%endif

Summary:   Antivirus/anti-spam gateway for smtp server
Name:      sagator
Version:   2.0.0
Release:   0.beta38%{?dist}
Source:    http://www.salstar.sk/pub/antivir/snapshots/sagator-%{version}-0.beta38.tar.bz2
URL:       http://www.salstar.sk/sagator/
License:   GPLv2+
BuildArch: noarch
BuildRequires: %{python_version}-devel, ed, gettext
Requires:  %{name}-core = %{version}-%{release}
Requires:  sed
Requires:  spamassassin
%if 0%{?suse_version}
Requires:  clamav >= %{CLAMAV_VERSION}
%else
Requires:  clamav-lib >= %{CLAMAV_VERSION}, clamav-update
%endif

%description
This program is an email antivirus/anti-spam gateway. It is an interface to
the postfix, sendmail, or any other smtpd, which runs antivirus and/or
spam checker. Its modular architecture can use any combination of
antivirus/spam checker according to configuration.

It has some internal checkers (string_scanner and regexp_scanner). Sagator
can parse MIME mails and decompress archives, if it is configured so.

Features:
    * simple chroot support
    * modular antivirus/spam checker support
          o attach an intrascanner to another intrascanner or realscanner
          o combine intrascanners
          o combine realscanners
          o virus/spam level based scanners
    * database support
          o SQL logging
          o dynamic scanner (antivirus/anti-spam) configuration
    * daily reports for users
    * web quarantine accessible for all users
    * you don't need any perl modules or any other modules, only python
    * you can return any quarantined mail to mailq/user mailbox
    * mailbox/maildir scanning and cleaning
    * smtp policy service (greylist)
    * nice statistics via WWW or MRTG
    * easy installation and configuration

%package core
Summary:        Antivirus/anti-spam gateway for smtp server, core files
Requires:       sed
%if 0%{?suse_version}
BuildRequires: aaa_base, python-xml, clamav >= %{CLAMAV_VERSION}
Requires:       aaa_base, smtp_daemon
%else
Requires:       server(smtp), shadow-utils
BuildRequires:  clamav-devel >= %{CLAMAV_VERSION}
Requires:       clamav-lib >= %{CLAMAV_VERSION}
%endif
%if 0%{?rhel} == 6
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires:       initscripts
BuildRequires:  initscripts
%else
BuildRequires:  systemd
%{?systemd_requires}
%endif
Requires:       spamassassin
BuildRequires:  logwatch
Obsoletes:      sagator-libclamav <= 1.2.3
Obsoletes:      sagator-pydspam <= 0.9.1

%description core
SAGATOR's core files. You can use this package separatelly, if you do
not to depend on other software, required by sagator.

%package webq
Summary:        SAGATOR's web quarantine access
Requires:       sagator-core = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       %{python_version}-jinja2
%else
Requires:       python-jinja2
%endif

%description webq
SAGATOR's web quarantine access can be used to allow users (or admin)
to access their emails in sagator's quarantine.

%if 0%{?install_sepolicy}>0
%package        selinux
Summary:        SELinux support for SAGATOR
Requires:       %{name}-core = %{version}-%{release}
Requires(postun): policycoreutils, selinux-policy
BuildRequires: selinux-policy-devel

%description selinux
This package helps moving to the upstream SELinux module.
%endif

%prep
%setup -q

%build
sh configure --prefix=%{_prefix} --filelist --python=%{python_version}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
rm -f %{buildroot}%{_datadir}/sagator/etc/sgconf.py* \
  scripts/mkchroot.sh scripts/graphs/*.in
touch %{buildroot}%{_datadir}/%{name}/etc/sgconf.py_
ln -s ../../../..%{_sysconfdir}/sagator.conf \
  %{buildroot}%{_datadir}/%{name}/etc/sgconf.py
mkdir -p %{buildroot}%{CHROOTDIR}/tmp/quarantine
cp -arf scripts/db %{buildroot}%{_datadir}/%{name}/
%find_lang %{name}

%pre core
getent group vscan >/dev/null || groupadd -r vscan
getent passwd vscan >/dev/null || \
useradd -r -g vscan -d %{CHROOTDIR} -s /sbin/nologin -c "SAGATOR" vscan
exit 0

%post core
touch %{_var}/lib/sagator-mkchroot
if [ $1 = 2 ]; then # upgrade
  [ -f %{_sysconfdir}/sysconfig/sagator ] && . %{_sysconfdir}/sysconfig/sagator || true
  # update configuration
  %{_datadir}/sagator/updatecfg.py || true
fi
%if 0%{?rhel} == 6
%{_initrddir}/sagator try-restart >/dev/null 2>&1 || true
%else
%systemd_post %{name}.service
%endif

%preun core
%if 0%{?rhel} == 6
if [ $1 = 0 ]; then # uninstall
  # stop service and remove init script symlinks
  %{_initrddir}/sagator stop >/dev/null 2>&1
  chkconfig --del sagator
fi
%else
%systemd_preun %{name}.service
%endif

%if 0%{?rhel} == 6
%else
%postun core
%systemd_postun_with_restart %{name}.service
%endif

%if 0%{?install_sepolicy}>0
%post selinux
if selinuxenabled; then
    # Replace the module by the upstream one
    #. /etc/selinux/config 2>/dev/null || :
    semodule -i %{sepolicy} 2>/dev/null || :
    # relabel files
    fixfiles -R %{name} restore || :
    # relabel chroot
    restorecon -R %{CHROOTDIR} || :
fi
%endif

%triggerin core -- sagator-webq,%{BASE_LIBS},%{ARCHIVERS},%{ANTIVIRS},%{ANTISPAMS}
touch %{_var}/lib/sagator-mkchroot

%triggerpostun core -- sagator-webq,%{BASE_LIBS},%{ARCHIVERS},%{ANTIVIRS},%{ANTISPAMS}
touch %{_var}/lib/sagator-mkchroot

%files
# no files, this package just requires others
# exclude sepolicy for builds without selinux module
%if 0%{?sepolicy:1}
%exclude %{sepolicy}
%endif

%files core -f filelist
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,vscan) %{_sysconfdir}/%{name}.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/*/conf.d/%{name}.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/mrtg/%{name}.cfg
%if 0%{?fedora} || 0%{?rhel} >= 7 || 0%{?suse_version} >= 01310
%{_unitdir}/%{name}.service
%exclude %{_initrddir}/%{name}
%else
%{_initrddir}/%{name}
%endif
%config(noreplace) %verify(not md5 size mtime) %attr(644,root,root) %{_sysconfdir}/cron.d/%{name}
%doc doc/README doc/FAQ doc/*.txt doc/*.html TODO COPYING ChangeLog test
%doc scripts/graphs scripts/*.sh scripts/log/analyzer.py
%{_bindir}/*
%{_sbindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py*
%dir %attr(750,root,vscan) %{_datadir}/%{name}/etc
%{_datadir}/%{name}/etc/*.py*
%exclude %{_datadir}/%{name}/etc/sgconf.py?
%{_datadir}/%{name}/avir
%{_datadir}/%{name}/aspam
%{_datadir}/%{name}/interscan
%{_datadir}/%{name}/srv
%exclude %{_datadir}/%{name}/srv/web
%exclude %{_datadir}/%{name}/srv/templates
%{_datadir}/%{name}/db
%{_mandir}/man*/*
%dir %{CHROOTDIR}
%attr(1777,vscan,vscan) %dir %{CHROOTDIR}/tmp
%attr(0770,vscan,vscan) %dir %{CHROOTDIR}/tmp/quarantine

%files webq -f sagator.lang
%{_datadir}/%{name}/srv/web
%{_datadir}/%{name}/srv/templates

%if 0%{?install_sepolicy}>0
%files selinux
%dir %{_datadir}/%{name}/selinux
%{sepolicy}
%endif

%changelog
* Sun Apr 19 2020 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.0.0-0.beta38
- update to upstream

* Thu Apr 02 2020 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.0.0-0.beta37
- Fix string quoting for rpm >= 4.16, suse_version used

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.1-1
- update to upstream

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul  9 2014 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.0-1
- update to upstream

* Sat May 14 2011 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3.0-1
- added Sanesecurity.Spam an Sanesecurity.Junk to default DROP pattern

* Thu Dec  9 2010 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.2.2-1
- database creation scripts moved to /usr/share/sagator

* Tue Jul 28 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.2.1-2
- updated english summary and description (fixed spelling errors suggested
  by rpmlint)

* Tue Jul 28 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.2.1-1
- Requires: smtpdaemon again for EPEL

* Wed Sep 17 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.1.1-1
- core files moved to core packages, sagator package now requires clamav
  and spamassassin
- added selinux policy dir

* Sun Feb 17 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.1.0-2
- changed dependency from smtpdaemon to server(smtp)
- reverted back previous change

* Sun Feb 17 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.1.0-1
- added libclamav module
- added pydspam module
- selinux module moved to separate subpackage

* Thu Jan 3 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.0-2
- /var/spool/vscan replaced by CHROOTDIR macro
- posttrans section moved to init script (start section)
- more macros used

* Thu Jan 3 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.0-1
- clean buildroot before install
- sagator.conf symlink is now relative

* Fri Sep 7 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.0.0-1
- sagator moved from /usr/lib to /usr/share

* Fri Apr 13 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- added sagator.pp selinux policy file and post-install script

* Wed Dec 27 2006 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- added GPG public key

* Tue Sep 05 2006 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- added gcc build-require for suse package
- better build for unstable releases
- postfix autoconfigure messages
- crontab modification moved to /etc/cron.d/ directory
- mrtg triggers removed
- removed clamav a dspam stuff
- fixed permissions for sagator.conf
- postfix autoconfiguration moved into documentation

* Sun Nov 20 2005 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- suse support
- proper pathes for logwatch 0.7 scripts

* Sun Aug 28 2005 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- configuration moved into config directory

* Fri Aug 05 2005 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- script documentation added

* Mon Jul 18 2005 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- new description
- changed dependecy from postfix to smtpdaemon

* Sun Jun 26 2005 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- changes recommended by Fedora Extras Packaging Guidelines

* Mon May 30 2005 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- web directory added

* Mon Apr 11 2005 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- postinstall script fix to update master.cf properly

* Mon Dec 20 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- Documentation moved into doc directory.
- man pages added
- dspam module

* Sun Nov  7 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- chkconfig is started only on install (not upgrade)
- sagator is restarted only when RESTART=auto is configured in sysconfig
- You will be able ... message will show only on install
- Fedora Core 3 yum.repos.d autodetect

* Thu Aug 26 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- logrotate script added

* Fri Aug  6 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- srv/* added
- updatecfg.py in postinstall script

* Tue Jul  6 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- mrtg script added

* Mon May 31 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- cron script is now as configuration script (not replaced)

* Thu Apr 29 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- added triggers

* Tue Apr 13 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- /var/spool/vscam/tmp permission fix

* Wed Feb  4 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- postfix requirement added
- fixed scriptlet fail when postfix is not started
- testing programs added to documentation

* Wed Jan 28 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- configs are not replaced

* Mon Jan 19 2004 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- added sysconfig file
- added logrotate files
- config moved into /etc and symlink into /usr/lib/sagator

* Fri Oct 31 2003 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- added mrtg.cfg and index.html
- making of chroot removed on upgrading

* Thu Sep 18 2003 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- postfix is not reloaded, when sagator is upgrading

* Tue Jun 10 2003 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk>
- first release
