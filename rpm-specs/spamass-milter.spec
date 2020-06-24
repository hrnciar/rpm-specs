# This package uses systemd init from Fedora 16, but can use it for
# Fedora 15 if built using --with systemd
%if !((0%{?rhel} && 0%{?rhel} <= 6) || (0%{?fedora} && 0%{?fedora} <= 15))
%global _with_systemd --with-systemd
%endif
%global use_systemd %{!?_with_systemd:0}%{?_with_systemd:1}

# The runtime directory is on tmpfs from Fedora 15 regardless of whether or not we're using systemd init
%if (0%{?rhel} && 0%{?rhel} <= 6) || (0%{?fedora} && 0%{?fedora} <= 14)
%global rundir %{_localstatedir}/run
%global rundir_tmpfs 0
%else
%global rundir /run
%global rundir_tmpfs 1
%endif

# systemd-units merged into systemd at Fedora 17
%if (0%{?fedora} && 0%{?fedora} <= 16)
%global systemd_units systemd-units
%else
%global systemd_units systemd
%endif

# Support systemd presets and drop support for SysV migration from Fedora 18, RHEL 7
%if (0%{?rhel} && 0%{?rhel} <= 6) || (0%{?fedora} && 0%{?fedora} <= 17)
%global preset_support 0
%global sysv_to_systemd %{use_systemd}
# Flag file for SysV-to-systemd migration
%global migrfile /run/%{name}-%{version}-%{release}-%{_arch}.systemd-migration
# This macro not defined until Fedora 18
%global _tmpfilesdir %{_prefix}/lib/tmpfiles.d
%else
%global preset_support 1
%global sysv_to_systemd 0
%endif

# Milter header files package name
%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 25)
%global milter_devel_package sendmail-devel
%else
%global milter_devel_package sendmail-milter-devel
%endif

# Do a hardened build where possible
%global _hardened_build 1

Summary:	Milter (mail filter) for spamassassin
Name:		spamass-milter
Version:	0.4.0
Release:	17%{?dist}
License:	GPLv2+
URL:		http://savannah.nongnu.org/projects/spamass-milt/
Source0:	http://savannah.nongnu.org/download/spamass-milt/spamass-milter-%{version}.tar.gz
Source1:	spamass-milter.README.Postfix
Source2:	spamass-milter-tmpfs.conf
Source3:	spamass-milter-postfix-tmpfs.conf
# SysV init
Source10:	spamass-milter.sysv
Source11:	spamass-milter-sysconfig.sysv
# systemd
Source20:	spamass-milter.service
Source21:	spamass-milter-root.service
Source22:	spamass-milter-sysconfig.systemd
Source23:	spamass-milter-postfix-sysconfig.systemd
# Patches submitted upstream:
# http://savannah.nongnu.org/bugs/?29326
Patch2:		spamass-milter-0.4.0-authuser.patch
Patch3:		spamass-milter-0.4.0-rcvd.patch
Patch4:		spamass-milter-0.4.0-bits.patch
Patch5:		spamass-milter-0.4.0-group.patch
# Patches not yet submitted upstream
Patch8:		spamass-milter-0.4.0-auth-no-ssf.patch
# Fedora-specific patches
Patch10:	spamass-milter-0.4.0-pathnames.patch
Patch11:	spamass-milter-0.4.0-rundir.patch
BuildRequires:	coreutils
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	%milter_devel_package
BuildRequires:	spamassassin
Requires:	spamassassin, /usr/sbin/sendmail
%if %{rundir_tmpfs}
# Needed for ownership of %%{_tmpfilesdir}
Requires:	%{systemd_units}
%endif

Requires(pre): glibc-common, shadow-utils
%if %{sysv_to_systemd}
Requires(pre): chkconfig, coreutils, systemd-sysv
%endif
%if %{use_systemd}
BuildRequires: %{systemd_units}
Requires(post): coreutils, %{systemd_units}
Requires(preun): %{systemd_units}
Requires(postun): %{systemd_units}
%else
Requires(post): chkconfig
Requires(preun): chkconfig, initscripts
Requires(postun): initscripts
%endif

%description
A milter (Mail Filter) application that pipes incoming mail (including things
received by rmail/UUCP) through SpamAssassin, a highly customizable spam
filter. A milter-compatible MTA such as Sendmail or Postfix is required.

%package postfix
Summary:	Postfix support for spamass-milter
Requires:	%{name} = %{version}-%{release}
Requires(pre):	postfix
Requires(post):	shadow-utils, %{name} = %{version}-%{release}
BuildArch:	noarch

%description postfix
This package adds support for running spamass-milter using a Unix-domain
socket to communicate with the Postfix MTA.

%prep
%setup -q

# Copy in general support files
cp -p %{SOURCE1} README.Postfix
cp -p %{SOURCE2} spamass-milter-tmpfs.conf
cp -p %{SOURCE3} spamass-milter-postfix-tmpfs.conf

# Fix Received-header generation (#496763)
%patch3 -b .rcvd

# Add authentication info to dummy Received-header (#496769)
%patch4 -b .bits

# Add -g option for group-writable socket for Postfix support (#452248)
%patch5 -b .group

# Help for users authenticating to Postfix (#730308)
%patch8 -b .postfix-auth

# Local patch for initscript and socket paths
%patch10 -b .pathnames

# Add -I option to ignore (don't check) mail from authenticated users
# (#437506, #496767) http://savannah.nongnu.org/bugs/?21046
# Note: upstream introduced a similar -a option in version 0.4.0, so this
# option is retained only in builds prior to Fedora 22 for compatibility
%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 21)
%patch2 -b .authuser
%endif

# With systemd, the runtime directory is /run rather than /var/run
%if %{rundir_tmpfs}
%patch11 -b .rundir
%endif

# Copy in SysV init files
%if !%{use_systemd}
cp -p %{SOURCE10} %{SOURCE11} .
%endif

# Copy in systemd files
%if %{use_systemd}
cp -p %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} .
%endif

%build
export SENDMAIL=/usr/sbin/sendmail
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

install -m 755 -d %{buildroot}%{_localstatedir}/lib/spamass-milter
install -m 711 -d %{buildroot}%{rundir}/spamass-milter
install -m 750 -d %{buildroot}%{rundir}/spamass-milter/postfix
%if %{use_systemd}
install -m 644 -D spamass-milter.service \
	%{buildroot}%{_unitdir}/spamass-milter.service
install -m 644 -D spamass-milter-root.service \
	%{buildroot}%{_unitdir}/spamass-milter-root.service
install -m 644 -D spamass-milter-sysconfig.systemd \
	%{buildroot}%{_sysconfdir}/sysconfig/spamass-milter
install -m 644 -D spamass-milter-postfix-sysconfig.systemd \
	%{buildroot}%{_sysconfdir}/sysconfig/spamass-milter-postfix
%else
install -m 755 -D spamass-milter.sysv \
	%{buildroot}%{_initddir}/spamass-milter
install -m 644 -D spamass-milter-sysconfig.sysv \
	%{buildroot}%{_sysconfdir}/sysconfig/spamass-milter
%endif

# Make sure %%{rundir}/spamass-milter{,/postfix} exist at boot time for systems
# with %%{rundir} on tmpfs (#656692)
%if %{rundir_tmpfs}
install -m 755 -d %{buildroot}%{_tmpfilesdir}
install -m 644 spamass-milter-tmpfs.conf \
	%{buildroot}%{_tmpfilesdir}/spamass-milter.conf
install -m 644 spamass-milter-postfix-tmpfs.conf \
	%{buildroot}%{_tmpfilesdir}/spamass-milter-postfix.conf
%endif

# Create dummy sockets for %%ghost-ing
: > %{buildroot}%{rundir}/spamass-milter/spamass-milter.sock
: > %{buildroot}%{rundir}/spamass-milter/postfix/sock

%pre
getent group sa-milt >/dev/null || groupadd -r sa-milt
getent passwd sa-milt >/dev/null || \
	useradd -r -g sa-milt -d %{_localstatedir}/lib/spamass-milter \
		-s /sbin/nologin -c "SpamAssassin Milter" sa-milt
# Fix homedir for upgrades
usermod --home %{_localstatedir}/lib/spamass-milter sa-milt &>/dev/null
%if %{sysv_to_systemd}
# Start SysV-to-systemd migration
rm -f %{migrfile} &>/dev/null
if [ $1 -gt 1 -a ! -e %{_unitdir}/spamass-milter.service -a -e %{_initddir}/spamass-milter ]; then
	systemd-sysv-convert --save spamass-milter &>/dev/null
	chkconfig --del spamass-milter &>/dev/null
	touch %{migrfile} &>/dev/null
fi
%endif
exit 0

%post
if [ $1 -eq 1 ]; then
	# Initial installation
%if %{use_systemd}
	systemctl daemon-reload &>/dev/null || :
%else
	chkconfig --add spamass-milter || :
%endif
%if %{preset_support}
	systemctl preset spamass-milter.service &>/dev/null || :
	systemctl preset spamass-milter-root.service &>/dev/null || :
%endif
fi

%preun
if [ $1 -eq 0 ]; then
	# Package removal, not upgrade
%if %{use_systemd}
	systemctl --no-reload disable spamass-milter.service &>/dev/null || :
	systemctl stop spamass-milter.service &>/dev/null || :
	systemctl --no-reload disable spamass-milter-root.service &>/dev/null || :
	systemctl stop spamass-milter-root.service &>/dev/null || :
%else
	%{_initddir}/spamass-milter stop &>/dev/null || :
	chkconfig --del spamass-milter || :
%endif
fi

%postun
%if %{use_systemd}
systemctl daemon-reload &>/dev/null || :
%endif
if [ $1 -ge 1 ]; then
	# Package upgrade, not uninstall
%if %{use_systemd}
	systemctl try-restart spamass-milter.service &>/dev/null || :
	systemctl try-restart spamass-milter-root.service &>/dev/null || :
%else
	%{_initddir}/spamass-milter condrestart &>/dev/null || :
%endif
fi

%if %{sysv_to_systemd}
%triggerpostun -- spamass-milter
# Complete the SysV-to-system migration started in %%pre
if [ $1 -gt 0 -a -e %{migrfile} ]; then
	systemctl daemon-reload &>/dev/null || :
	systemctl try-restart spamass-milter.service &>/dev/null
fi
rm -f %{migrfile} &>/dev/null || :
%endif

%post postfix
# This is needed because the milter needs to "give away" the MTA communication
# socket to the postfix group, and it needs to be a member of the group to do
# that.
usermod -a -G postfix sa-milt || :

%files
%doc AUTHORS ChangeLog NEWS README
%{_mandir}/man1/spamass-milter.1*
%config(noreplace) %{_sysconfdir}/sysconfig/spamass-milter
%if %{rundir_tmpfs}
%{_tmpfilesdir}/spamass-milter.conf
%endif
%if %{use_systemd}
%{_unitdir}/spamass-milter.service
%{_unitdir}/spamass-milter-root.service
%else
%{_initddir}/spamass-milter
%endif
%{_sbindir}/spamass-milter
%dir %attr(-,sa-milt,sa-milt) %{_localstatedir}/lib/spamass-milter/
%dir %attr(-,sa-milt,sa-milt) %{rundir}/spamass-milter/
%ghost %{rundir}/spamass-milter/spamass-milter.sock

%files postfix
%doc README.Postfix
%if %{rundir_tmpfs}
%{_tmpfilesdir}/spamass-milter-postfix.conf
%endif
%if %{use_systemd}
%config(noreplace) %{_sysconfdir}/sysconfig/spamass-milter-postfix
%endif
%dir %attr(-,sa-milt,postfix) %{rundir}/spamass-milter/postfix/
%ghost %{rundir}/spamass-milter/postfix/sock

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Paul Howarth <paul@city-fan.org> - 0.4.0-12
- Account for systemd-units being merged into systemd at Fedora 17
- Drop support for SysV-to-systemd migration from Fedora 18, RHEL 7
- Use forward-looking conditionals
- One build requirement per line

* Wed Nov 15 2017 Paul Howarth <paul@city-fan.org> - 0.4.0-11
- Replace /bin/* dependencies with coreutils etc. (#1512898)
- Drop explicit paths for commands to aid spec readability
- Drop EL-5 support
  - Drop legacy Group: and BuildRoot: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section
  - Noarch sub-packages are always available now

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 Paul Howarth <paul@city-fan.org> - 0.4.0-7
- Document expected warning message when used with Postfix (#1368645)

* Fri Aug  5 2016 Paul Howarth <paul@city-fan.org> - 0.4.0-6
- sendmail-devel renamed to sendmail-milter-devel from Fedora 26
- Specify all build requirements

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Paul Howarth <paul@city-fan.org> - 0.4.0-4
- Document macro requirements for Postfix (#1294245)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Paul Howarth <paul@city-fan.org> - 0.4.0-1
- Update to 0.4.0
  - New options:
    -C option to change the default reject code
    -S option to specify a path to sendmail (for the -x option)
    -R option to specify the rejection message
    -a option to skip messages that were authenticated
  - IPv6 address support
  - Syntax clean-ups
- Drop upstreamed syntax, rejection text and IPv6 patches
- Update authuser patch: note that upstream has introduced a -a option that
  does pretty much the same as the -I option added by this patch, so this
  patch is deprecated and will not be included in builds for Fedora 22 onwards
- Clean up other patches to apply cleanly

* Tue Feb 24 2015 Paul Howarth <paul@city-fan.org> - 0.3.2-15
- Add -R option to specify SMTP rejection text (#1131667)
- Drop %%defattr, redundant since rpm 4.4

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 0.3.2-14
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep  5 2012 Paul Howarth <paul@city-fan.org> - 0.3.2-9
- Add systemd preset support (#850321)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Paul Howarth <paul@city-fan.org> - 0.3.2-7
- Move the tmpfiles.d config from %%{_sysconfdir} to %%{_prefix}/lib

* Mon Apr 16 2012 Paul Howarth <paul@city-fan.org> - 0.3.2-6
- Do a hardened (PIE) build where possible

* Wed Jan 11 2012 Paul Howarth <paul@city-fan.org> - 0.3.2-5
- Rebuild for gcc 4.7 in Rawhide

* Wed Aug 24 2011 Paul Howarth <paul@city-fan.org> - 0.3.2-4
- Add systemd init support, on by default from Fedora 16
- %%ghost the sockets for clean uninstalls

* Thu Aug 18 2011 Paul Howarth <paul@city-fan.org> - 0.3.2-3
- Help for users authenticating to Postfix (#730308)

* Mon Jul 18 2011 Paul Howarth <paul@city-fan.org> - 0.3.2-2
- Drop the wrapper, which hasn't been needed since 0.3.1 was released
- Nobody else likes macros for commands

* Tue Feb 15 2011 Paul Howarth <paul@city-fan.org> - 0.3.2-1
- Update to 0.3.2 (upstream fix for popen unsanitized input vulnerability:
  CVE-2010-1132, #572117, #572119, http://savannah.nongnu.org/bugs/?29136)
- Drop popen patch, now upstream
- Rework syntax, rcvd and bits patches to apply against new codebase

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Paul Howarth <paul@city-fan.org> - 0.3.1-24
- Require systemd-units for ownership of /etc/tmpfiles.d directory
- Add Default-Stop LSB keyword in initscript

* Fri Nov 26 2010 Paul Howarth <paul@city-fan.org> - 0.3.1-23
- Make sure /var/run/spamass-milter and /var/run/spamass-milter/postfix exist
  at boot time for systems with /var/run on tmpfs (#656692)

* Wed Sep 29 2010 jkeating - 0.3.1-22
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Paul Howarth <paul@city-fan.org> - 0.3.1-21
- Add IPv6 whitelisting support (#630263)

* Tue Jun  8 2010 Paul Howarth <paul@city-fan.org> - 0.3.1-20
- RHEL-6 onwards have noarch subpackages, so make spamass-milter-postfix one

* Mon Apr 19 2010 Paul Howarth <paul@city-fan.org> - 0.3.1-19
- Fix patch for CVE-2010-1132 to not create a zombie process per email when
  the -x or -b options are used (#583523)

* Tue Mar 23 2010 Paul Howarth <paul@city-fan.org> - 0.3.1-18
- Add patch to get rid of compiler warnings
- Reorder and re-base patches to optimize chances of upstream accepting them
- Improve Received-header patch (#496763) incorporating additional fix from
  upstream update (http://savannah.nongnu.org/bugs/?17178)

* Fri Mar 12 2010 Paul Howarth <paul@city-fan.org> - 0.3.1-17
- Update initscript to support running the milter as root, which is needed
  for the -x (expand aliases) option; note that the milter does not run as
  root by default
- Add patch for popen unsanitized input vulnerability
  (CVE-2010-1132, #572117, #572119, http://savannah.nongnu.org/bugs/?29136)
- Rebase authuser patch
- Update patch adding auth info to dummy Received-header so that it doesn't
  generate spurious warnings about missing macros (#532266), and update and
  merge the macro documentation patch into this patch
- Document patch usage in spec file

* Tue Aug 11 2009 Paul Howarth <paul@city-fan.org> - 0.3.1-16
- Switch to bzipped source tarball

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 24 2009 Paul Howarth <paul@city-fan.org> - 0.3.1-14
- Fix Received-header generation (#496763)
- Add authentication info to dummy Received-header (#496769)
- Add option to skip checks for authenticated senders (#437506, #496767)
  (thanks to Habeeb J. Dihu for the reports and patches)

* Wed Mar 18 2009 Paul Howarth <paul@city-fan.org> - 0.3.1-13
- Call initscripts directly instead of via /sbin/service and fine-tune scriptlet
  dependencies
- Change sa-milt user's home directory from
  %%{_localstatedir}/run/spamass-milter to %%{_localstatedir}/lib/spamass-milter
  so as to retain directory contents across a reboot (#489995), and fix the home
  directory of any existing sa-milt account on upgrades

* Fri Feb 27 2009 Paul Howarth <paul@city-fan.org> - 0.3.1-12
- Subpackage for postfix is now noarch for Fedora 10 onwards
- Fix scriptlet deps to ensure that sa-milt user exists before we attempt to
  add it to the postfix group

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Paul Howarth <paul@city-fan.org> - 0.3.1-10
- Rebuild for shared libmilter in Fedora 11 development

* Thu Jul  3 2008 Paul Howarth <paul@city-fan.org> - 0.3.1-9
- Require /usr/sbin/sendmail (for -b/-B/-x options) rather than sendmail pkg
- Make summary and description less Sendmail-specific
- Add patch to support group-writable socket for MTA communication, needed
  to be able to use a Unix-domain socket with Postfix (#452248)
- Add subpackage with group-writable directory for Postfix support
- Tweak initscript to change default options when Postfix socket directory is
  present
- Document additional ENVRCPT macros to provide

* Tue May 20 2008 Paul Howarth <paul@city-fan.org> - 0.3.1-8
- Fix initscript failure to start with SELinux in enforcing mode (#447247)
  (needs selinux-policy >= 3.3.1-55 on F9)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.1-7
- Autorebuild for GCC 4.3

* Mon Feb 18 2008 Paul Howarth <paul@city-fan.org> - 0.3.1-6
- Rebuild with gcc 4.3.0 for Fedora 9

* Fri Oct 12 2007 Paul Howarth <paul@city-fan.org> - 0.3.1-5
- Split initscript and config out from being here documents in the spec and
  have them as separate source files instead
- Unexpand tabs
- Clarify license as GPL v2 or later (GPLv2+)
- Use the standard scriptlet for user/group creation in %%pre

* Wed Aug 30 2006 Paul Howarth <paul@city-fan.org> - 0.3.1-4
- Use make/DESTDIR instead of deprecated %%makeinstall macro
- Expand tabs and clean up changelog entries

* Mon May 15 2006 Paul Howarth <paul@city-fan.org> - 0.3.1-3
- Use upstream default settings (#191602)
  This change re-enables by default Subject/Content-Type header modification
  (which may have a performance impact for large messages) and disables by
  default the rejection of emails with a spam score of 15 or more. To re-enable
  these options, uncomment the line:
  EXTRA_FLAGS="-m -r 15"
  in %%{_sysconfdir}/sysconfig/spamass-milter
  
* Sun May  7 2006 Paul Howarth <paul@city-fan.org> - 0.3.1-2
- Fix race condition in "stop" clause of initscript (#190894)

* Thu Apr  6 2006 Paul Howarth <paul@city-fan.org> - 0.3.1-1
- Update to 0.3.1

* Wed Feb 15 2006 Paul Howarth <paul@city-fan.org> - 0.3.0-9
- Don't use macros in command paths, hardcode them instead

* Mon Aug  1 2005 Paul Howarth <paul@city-fan.org> - 0.3.0-8
- Run the milter in a wrapper script that restarts it if it crashes

* Thu Jun 16 2005 Paul Howarth <paul@city-fan.org> - 0.3.0-7
- Bump and rebuild due to transient build system failure

* Wed Jun 15 2005 Paul Howarth <paul@city-fan.org> - 0.3.0-6
- Adjust initscript chkconfig values so it starts before sendmail

* Mon Jun 13 2005 Paul Howarth <paul@city-fan.org> - 0.3.0-5
- Help the configure script find sendmail

* Mon Jun 13 2005 Paul Howarth <paul@city-fan.org> - 0.3.0-4
- Bump and rebuild

* Mon Jun 06 2005 Paul Howarth <paul@city-fan.org> - 0.3.0-3
- Use Extras standard buildroot
- Unpack tarball quietly
- Create account sa-milt and run the milter using that instead of root
- Fix socket name in README
- Initscript not %%config

* Sun Jun 05 2005 Warren Togami <wtogami@redhat.com> - 0.3.0-2
- Extras

* Tue Feb 08 2005 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Updated to release 0.3.0

* Wed Sep 01 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Fixed variables in sysconfig file (mator)

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Initial package (using DAR)
