%if 0%{?fedora} > 17 || 0%{?rhel} > 6
%global systemd_support 1
%else
%global systemd_support 0
%endif

Summary:        Nagios Service Check Acceptor
Name:           nsca
Version:        2.10.0
Release:        3%{?dist}
License:        GPLv2+
URL:            http://www.nagios.org/
Source0:        https://github.com/NagiosEnterprises/nsca/releases/download/nsca-%{version}/nsca-%{version}.tar.gz
Source1:        nsca-initscript
Source2:        nsca-sysconfig
Source3:        nsca.service

Patch0:         nsca-2.9-initscript.patch
Patch1:         nsca-2.10.0-confpath.patch
Patch100:       nsca-2.10.0-drop_hex_delimiter.patch

BuildRequires:  gcc
BuildRequires:  libmcrypt-devel
BuildRequires:  perl-interpreter
%if %{systemd_support}
BuildRequires: systemd-units
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(post): /sbin/chkconfig
Requires(postun): /sbin/service
%endif
Requires:       nagios


%description
The purpose of this addon is to allow you to execute Nagios/NetSaint
plugins on a remote host in as transparent a manner as possible.


%package client
Summary:        Client application for sending updates to a nsca server
Requires:       nagios-common


%description client
Client application for sending updates to a nsca server.


%prep
%setup -q
%patch0 -p0 -b .initscript
%patch1 -p1 -b .confpath
%patch100 -p1 -b .hex_delimiter
# Change defaults in the config file to match the nagios package
sed -i -e "s|^command_file=.*|command_file=%{_localstatedir}/spool/nagios/cmd/nagios.cmd|" \
       -e "s|^alternate_dump_file=.*|alternate_dump_file=%{_localstatedir}/spool/nagios/cmd/nsca.dump|" \
       sample-config/nsca.cfg.in
# Default to legacy 2.7 compat mode for EL6
%if 0%{?el6}
sed -i -e "s|^# legacy_2_7_mode=true$|legacy_2_7_mode=true|" sample-config/send_nsca.cfg.in
sed -i -e "s|^int legacy_2_7_mode=FALSE;$|int legacy_2_7_mode=TRUE;|" src/send_nsca.c
%endif


%build
%configure \
        --sysconfdir="%{_sysconfdir}/nagios" \
        --localstatedir="%{_localstatedir}/log/nagios" \
        --with-nsca-user="nagios" \
        --with-nsca-grp="nagios" \
        --with-nsca-port="5667"
make %{?_smp_mflags} all


%install
install -Dp -m 0755 src/nsca %{buildroot}%{_sbindir}/nsca
install -Dp -m 0755 src/send_nsca %{buildroot}%{_sbindir}/send_nsca
install -Dp -m 0644 sample-config/nsca.cfg %{buildroot}%{_sysconfdir}/nagios/nsca.cfg
install -Dp -m 0644 sample-config/send_nsca.cfg %{buildroot}%{_sysconfdir}/nagios/send_nsca.cfg
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/nsca
%if %{systemd_support}
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/nsca.service
%else
install -Dp -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/nsca
%endif

%if %{systemd_support}
%post
%systemd_post nsca.service

%preun
%systemd_preun nsca.service

%postun
%systemd_postun_with_restart nsca.service 
%else
%post
/sbin/chkconfig --add nsca || :

%preun
if [ $1 -eq 0 ]; then
        /sbin/service nsca stop &>/dev/null
        /sbin/chkconfig --del nsca || :
fi

%postun
if [ "$1" -ge "1" ]; then
        /sbin/service nsca condrestart &>/dev/null || :
fi
%endif


%files
%license LICENSE.md
%doc CHANGELOG.md CONTRIBUTORS.md README.md SECURITY.md
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/nagios/nsca.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/nsca
%{_sbindir}/nsca
%if %{systemd_support}
%{_unitdir}/nsca.service
%else
%{_initrddir}/nsca
%endif


%files client
%license LICENSE.md
%doc CHANGELOG.md CONTRIBUTORS.md README.md SECURITY.md
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/nagios/send_nsca.cfg
%{_sbindir}/send_nsca


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Xavier Bachelot <xavier@bachelot.org> - 2.10.0-2
- Add patch to drop broken hex delimiter handling (RHBZ#1830611)

* Thu Apr 16 2020 Xavier Bachelot <xavier@bachelot.org> - 2.10.0-1
- Update to 2.10.0
  https://github.com/NagiosEnterprises/nsca/blob/nsca-2.10.0/CHANGELOG.md

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Xavier Bachelot <xavier@bachelot.org> - 2.9.2-5
- Add BR: gcc.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Xavier Bachelot <xavier@bachelot.org> - 2.9.2-1
- Update to 2.9.2.
- Clean up specfile.
- Drop EL5 support.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Xavier Bachelot <xavier@bachelot.org> - 2.9.1-9
- Fix typo in systemd unit file.

* Thu Oct 10 2013 Xavier Bachelot <xavier@bachelot.org> - 2.9.1-8
- Fix systemd unit file (RHBZ#928248).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Xavier Bachelot <xavier@bachelot.org> - 2.9.1-6
- Let nsca-client require nagios-common rather than own /etc/nagios (RHBZ#977438).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 04 2012 Xavier Bachelot <xavier@bachelot.org> - 2.9.1-4
- Add systemd support.

* Mon Sep 03 2012 Xavier Bachelot <xavier@bachelot.org> - 2.9.1-3
- Add a sysconfig file.
- Rewrite initscript.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Xavier Bachelot <xavier@bachelot.org> - 2.9.1-1
- Update to 2.9.1.
- Drop MAX_INPUTPLUGIN_LENGHT revert patch, fixed upstream.

* Thu Jan 26 2012 Xavier Bachelot <xavier@bachelot.org> - 2.9-2
- Revert MAX_INPUTPLUGIN_LENGHT, it breaks backward compatibility.

* Mon Jan 16 2012 Xavier Bachelot <xavier@bachelot.org> - 2.9-1
- Update to 2.9.
- Fix initscript return code (RHBZ#620013).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 31 2008 Wart <wart@kobold.org> - 2.7.2-6
- Change license to match sources

* Tue Mar 11 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.2-5
- Fix and rename initscript patch.
- Let client sub-package own %%{_sysconfdir}/nagios.

* Sun Mar 09 2008 Wart <wart@kobold.org> - 2.7.2-4
- Merge sed script for init script into the init script patch

* Mon Mar 03 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.2-3
- Sync with Wart's package (rhbz#433547).

* Thu Feb 07 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.2-2
- Split daemon and client.

* Sat Feb 02 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.2-1
- Update to 2.7.2.
- Clean up spec.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 2.6-1
- Updated to release 2.6.

* Wed Feb 08 2006 Dag Wieers <dag@wieers.com> - 2.5-2
- Removed -s option in sysv script. (Rick Johnson)

* Wed Feb 08 2006 Dag Wieers <dag@wieers.com> - 2.5-1
- Updated to release 2.5.

* Tue Nov 11 2003 Dag Wieers <dag@wieers.com> - 2.4-2
- Fixed command_file and alternate_dump_file in nsca.cfg. (Johan Krisar)
- Removed the nagios dependency. (Johan Krisar)
- Added %%{_localstatedir}/spool/nagios/ as directoriy to filelist.

* Mon Oct 27 2003 Dag Wieers <dag@wieers.com> - 2.4-1
- Fixed default port and xinetd file. (Shad L. Lords)

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 2.4-0
- Initial package. (using DAR)
