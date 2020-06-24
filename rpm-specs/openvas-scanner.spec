Name:		openvas-scanner
Version:	7.0.1
Release:	1%{?dist}
Summary:	Open Vulnerability Assessment (OpenVAS) Scanner

License:	GPLv2
URL:		http://www.openvas.org
#               https://github.com/greenbone/openvas/releases

Source0:	https://github.com/greenbone/openvas/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://github.com/greenbone/openvas/releases/download/v%{version}/openvas-%{version}.tar.gz.sig#/%{name}-%{version}.tar.gz.sig

# The authenticator public key obtained from release 7.0.0
# gpg2 -vv openvas-7.0.0.tar.gz.sig
# gpg2 --search-key 9823FAA60ED1E580
# wget https://www.greenbone.net/GBCommunitySigningKey.asc
# gpg2 --import GBCommunitySigningKey.asc
# gpg2 --list-public-keys 9823FAA60ED1E580
# gpg2 --export --export-options export-minimal 8AE4BE429B60A59B311C2E739823FAA60ED1E580 > gpgkey-8AE4BE429B60A59B311C2E739823FAA60ED1E580.gpg
Source2:	gpgkey-8AE4BE429B60A59B311C2E739823FAA60ED1E580.gpg

Source3:	openvas-scanner.logrotate
Source4:	openvas-scanner.sysconfig
Source5:	openvas-nvt-sync-cron
Source6:	openvas-nvt-sync-cronjob



BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:	cmake >= 2.6.0
BuildRequires:	openvas-libraries-devel >= 11.0.0
BuildRequires:	glib2-devel
BuildRequires:	libpcap-devel
BuildRequires:	gnutls-devel
BuildRequires:	gpgme-devel
BuildRequires:	libksba-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libssh-devel
BuildRequires:	pkgconfig
BuildRequires:	doxygen

# This is introduced to accomodate difference in RHEL5/CentOS5
%if %{defined rhel}
%if 0%{?rhel} <= 5
# RHEL5
BuildRequires:	e2fsprogs-libs-devel
%else
#RHEL6
BuildRequires:	libuuid-devel
%endif
%else
# Fedora 14 doesn't have "rhel" defined
BuildRequires:	libuuid-devel
%endif

%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
BuildRequires:	systemd
BuildRequires:	systemd-units
Requires(post):	systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):	chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
%endif


# Required by the openvas-nvt-sync and greenbone-nvt-sync
Requires:	/usr/bin/md5sum
Requires:	/usr/bin/rsync
Requires:	/usr/bin/wget
Requires:	/usr/bin/curl

%filter_provides_in %{_libdir}/openvas/plugins
%filter_setup

%description
Scanner module for the Open Vulnerability Assessment System (OpenVAS).

%package doc
Summary:        Development documentation for %{name}
BuildRequires:  graphviz

%description doc
You can find documentation for development of %{name} under file://%{_docdir}/%{name}-developerdocs.
It can be used with a Browser.



%prep
#check signature
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}

%autosetup -n openvas-%{version}

for i in CHANGELOG.md ; do
	iconv -f iso8859-1 -t utf-8 $i > $i.utf8 && \
	touch -r $i $i.utf8 && \
	mv -f $i.utf8 $i;
done



%build
# TODO change migrate to new pcap API from deprecated API
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations -Wno-error=stringop-truncation -Wno-error=format-truncation="
%cmake -DCMAKE_BUILD_TYPE=Release -DLOCALSTATEDIR:PATH=%{_var} -DOPENVASSD_RULES:PATH=%{_sysconfdir}/openvas/openvassd.rules
make %{?_smp_mflags} VERBOSE=1
make doc-full



%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Config directory
mkdir -p %{buildroot}/%{_sysconfdir}/openvas
chmod 755 %{buildroot}/%{_sysconfdir}/openvas

# Make directories for the NVT feeds
mkdir -p  %{buildroot}/%{_var}/lib/openvas/plugins
chmod 755 %{buildroot}/%{_var}/lib/openvas/plugins

# Log directory
mkdir -p %{buildroot}/%{_var}/log/openvas

# Make plugin cache directory
mkdir -p %{buildroot}/%{_var}/cache/openvas

# Doc directory
mkdir -p %{buildroot}/{_datadir}/doc/%{name}

# Install initial configuration
sed -e "s:@@OPENVAS_PLUGINS@@:%{_var}/lib/openvas/plugins:g
	s:@@OPENVAS_CACHE@@:%{_var}/cache/openvas:g
	s:@@OPENVAS_LOGDIR@@:%{_var}/log/openvas:g
	s:@@OPENVAS_SYSCONF@@:%{_sysconfdir}/openvas:g
	s:@@OPENVAS_CERT@@:%{_sysconfdir}/pki/openvas:g" %{SOURCE2} > openvassd.conf

install -Dp -m 644 openvassd.conf %{buildroot}/%{_sysconfdir}/openvas/

# Install log rotation stuff
install -m 644 -Dp %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/openvas-scanner

# Install sysconfig configration
install -Dp -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/openvas-scanner

# Install cron script for update
install -Dp -m 755 %{SOURCE5} %{buildroot}/%{_sbindir}/

# Install cront jobs to periodically update plugins
install -Dp -m 644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/cron.d/openvas-sync-plugins

# Delete *.so files as there is no devel package for scanner
rm -f %{buildroot}/%{_libdir}/libopenvas_*.so


%files
%doc CHANGELOG.md COPYING COPYING.GPLv2 README.md
%dir %{_sysconfdir}/openvas/
%dir %{_var}/lib/openvas/
%dir %{_var}/lib/openvas/plugins/
#Separation of feeds not possible because nasl script_dependencies doesn't search in all include_folders
#_dir _{_var}/lib/openvas/plugins/nvt/
#_dir _{_var}/lib/openvas/plugins/gsf/
%dir %{_var}/log/openvas/
%dir %{_var}/cache/openvas/
%config(noreplace) %{_sysconfdir}/openvas/openvassd.conf
%config(noreplace) %{_sysconfdir}/openvas/openvas_log.conf
%config(noreplace) %{_sysconfdir}/sysconfig/openvas-scanner
%config(noreplace) %{_sysconfdir}/cron.d/openvas-sync-plugins
%config(noreplace) %{_sysconfdir}/logrotate.d/openvas-scanner
%{_sbindir}/openvas-nvt-sync-cron
%{_sbindir}/openvas
%{_bindir}/openvas-nasl
%{_bindir}/openvas-nasl-lint
%{_bindir}/greenbone-nvt-sync
%{_mandir}/man1/*.1.*
%{_mandir}/man8/*.8.*
%{_libdir}/libopenvas*.so.*


%files doc
%doc doc/generated/html/*


%changelog
* Sat May 23 2020 josef radinger <cheese@nosuchhost.net> - 7.0.1-1
- bump version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Michal Ambroz <rebus at, seznam.cz> - 7.0.0-1
- update to 7.0.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 josef radinger <cheese@nosuchhost.net> - 5.1.3-6
- rebuild against correct openvas-libraries

* Tue Feb 05 2019 josef radinger <cheese@nosuchhost.net> - 5.1.3-5
- add openvas-scanner-coverty_#274950.patch to fix -Werror=stringop-truncation

* Sun Feb 03 2019 josef radinger <cheese@nosuchhost.net> - 5.1.3-4
- rename (unreleased) subpackage developerdocs to doc

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 josef radinger <cheese@nosuchhost.net> - 5.1.3-2
- add Buildrequires on graphviz
- add subpackage developerdocs
- small cleanup in spec-file

* Thu Jan 10 2019 josef radinger <cheese@nosuchhost.net> - 5.1.3-1
- bump version
- remove patch5
- add patch6 to fix compile errors because of cast-warnings
- add patch7 to fix compile errors because of format-truncation-warnings
- new openvas-libraries 9.0.3-1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 5.1.1-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon Apr 17 2017 Michal Ambroz <rebus at, seznam.cz> - 5.1.1-1
- Update to OpenVAS-9 openvas-scanner release 5.1.1
- tag fallthrough case to fix gcc7 build

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Michal Ambroz <rebus at, seznam.cz> - 5.0.7-1
- bump to 5.0.7

* Mon Sep 05 2016 Michal Ambroz <rebus at, seznam.cz> - 5.0.6-1
- bump to 5.0.6

* Fri Apr 29 2016 Michal Ambroz <rebus at, seznam.cz> - 5.0.5-3
- sync spec-files across fedora versions

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 josef radinger <cheese@nosuchhost.net> - 5.0.5-1
- bump version
- small cleanup specfile
- remove patch2

* Sat Aug 22 2015 Michal Ambroz <rebus at, seznam.cz> - 5.0.4-6
- 1254459 - fixing the logrotate script

* Wed Jul 15 2015 Michal Ambroz <rebus at, seznam.cz> - 5.0.4-1
- Update to OpenVAS-8 openvas-scanner release 5.0.4

* Thu Jun 25 2015 Michal Ambroz <rebus at, seznam.cz> - 5.0.3-5
- fix for epel

* Thu Jun 25 2015 Michal Ambroz <rebus at, seznam.cz> - 5.0.3-4
- add example redis configs

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Michal Ambroz <rebus at, seznam.cz> - 5.0.3-2
- fixing build error with gcrypt when RPM_OPT_FLAGS not used

* Tue May 26 2015 Michal Ambroz <rebus at, seznam.cz> - 5.0.3-1
- Update to OpenVAS-8 openvas-scanner release 5.0.3

* Sat Apr 04 2015 Michal Ambroz <rebus at, seznam.cz> - 4.0.6-1
- Update to OpenVAS-7 openvas-scanner release 4.0.6

* Sat Dec 06 2014 Michal Ambroz <rebus at, seznam.cz> - 4.0.5-1
- Update to OpenVAS-7 openvas-scanner release 4.0.5

* Fri Nov 07 2014 Michal Ambroz <rebus at, seznam.cz> - 4.0.4-2
- removed sysvinit subpackage - not needed anymore

* Wed Nov 05 2014 Michal Ambroz <rebus at, seznam.cz> - 4.0.4-1
- Update to OpenVAS-7 openvas-scanner release 4.0.4

* Fri Sep 12 2014 Michal Ambroz <rebus at, seznam.cz> - 4.0.3-1
- Update to OpenVAS-7 openvas-scanner release 4.0.3

* Tue Sep 02 2014 Michal Ambroz <rebus at, seznam.cz> - 4.0.2-1
- Update to OpenVAS-7 openvas-scanner release 4.0.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Michal Ambroz <rebus at, seznam.cz> - 4.0.1-2
- fix startscripts due to -q (quiet) option removed

* Mon May 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.1-1
- Spec file update
- Update to lastest upstream release 4.0.1

* Thu Apr 24 2014 Tomáš Mráz <tmraz@redhat.com> - 3.4-4.beta2
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Michal Ambroz <rebus at, seznam.cz> - 3.4-2.beta2
- bump to OpenVas-6 version 3.4+beta2

* Thu Mar 07 2013 Tomáš Mráz <tmraz@redhat.com> - 3.4-1.beta1
- rebuilt with new GnuTLS

* Wed Feb 06 2013 Michal Ambroz <rebus at, seznam.cz> - 3.4-0.beta1
- bump to OpenVas-6 version 3.4+beta1

* Thu Nov 15 2012 Michal Ambroz <rebus at, seznam.cz> - 3.3.1-1
- bump to OpenVas-5 version 3.3.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 10 2012 Michal Ambroz <rebus at, seznam.cz> - 3.2.5-5
- migrate the init scripts to systemd unit
- not containing the scripts for trigrerun as the whole suite is not functional
  anyway because of the incompatibility of gnutls

* Mon Jan 23 2012 Michal Ambroz <rebus at, seznam.cz> - 3.2.5-4
- fixed reporting of missing key file

* Mon Jan 23 2012 Michal Ambroz <rebus at, seznam.cz> - 3.2.5-3
- changed init.d script to display hints about openvas-mkcert in syslog

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Michal Ambroz <rebus at, seznam.cz> - 3.2.5-1
- bump to bugfix release 3.2.5

* Tue Oct 04 2011 Michal Ambroz <rebus at, seznam.cz> - 3.2.4-1
- bump to bugfix release 3.2.4

* Mon Apr 11 2011 Michal Ambroz <rebus at, seznam.cz> - 3.2.3-1
- bump to bugfix release 3.2.3

* Mon Mar 28 2011 Michal Ambroz <rebus at, seznam.cz> - 3.2.2-4
- more strict dependencies to new openvas-libraries for OpenVAS 4

* Mon Mar 28 2011 Michal Ambroz <rebus at, seznam.cz> - 3.2.2-3
- rename intrd and logrotate to allow same naming convention for openvas-manager

* Sat Mar 26 2011 Michal Ambroz <rebus at, seznam.cz> - 3.2.2-2
- patch to fix compile time errors about set but not used variables

* Fri Mar 18 2011 Michal Ambroz <rebus at, seznam.cz> - 3.2.2-1
- Bump to latest stable release 4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  9 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.1.2-2
- Changed BR so that it works for both RHEL5/CentOS5 and Fedora
- Changed startup script so that it works for both RHEL5/CentOS5 and Fedora

* Tue Nov 23 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.1.1-1
- synced with upstream version

* Fri Apr 16 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.0.2-3
- Reverted plugin permissions to 644
- Removed non-existing provides

* Wed Apr 14 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.0.2-2
- Changes based on the comments in the following review
  https://bugzilla.redhat.com/show_bug.cgi?id=562469#c24
- Included missed modifications to openvassd.conf by Michal Ambroz

* Tue Apr 13 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.0.2-1
- bump to a new upstream release

* Thu Mar 25 2010 Michal Ambroz <rebus at, seznam.cz> - 3.0.1-6
- fix config on 32bit architecture, double includes in specfile, permissions
- usage of macros/shell variables

* Fri Mar 12 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.0.1-5
- cron job shouldn't be replaced upon upgrade
- better alignment with Fedora's SysVInitScript guidelines
- Moved cronjob to cron.d directory
- Changed init.d name from openvassd into openvas-scanner
- Don't strip binary plugins in install phase to properly generate debuginfo

* Tue Mar  9 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.0.1-4
- Added cron job to periodically update plugins
- Added new option to init.d script to reload plugins

* Wed Mar  3 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.0.1-3
- Changes based on the comments in
  https://bugzilla.redhat.com/show_bug.cgi?id=562469#c5
- Fixed a small bug in postun scriptlet
- Ownership of /etc/openvas directory moved to libraries
- Modified init.d script to change openvassd into openvas-scanner

* Fri Feb 26 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.0.1-2
- Added cmake BR
- Changes based on the comments in
  https://bugzilla.redhat.com/show_bug.cgi?id=562469#c3

* Sat Feb  6 2010 Stjepan Gros <stjepan.gros@gmail.com> - 3.0.1-1
- Upgraded spec file for scanner version 3

* Tue Nov 17 2009 Stjepan Gros <stjepan.gros@gmail.com> - 2.0.3-1
- Minor changes from taken from Xavier Bachelot <xavier@bachelot.org>
- Initial spec file
