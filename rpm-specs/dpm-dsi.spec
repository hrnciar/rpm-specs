%if %{?fedora}%{!?fedora:0} >= 25 || %{?rhel}%{!?rhel:0} >= 7
%global systemd 1
%else
%global systemd 0
%endif

Name:		dpm-dsi
Summary:	Disk Pool Manager (DPM) plugin for the Globus GridFTP server
Version:	1.9.14
Release:	7%{?dist}
License:	ASL 2.0
URL:		https://svnweb.cern.ch/trac/lcgdm/wiki/Dpm
# The source of this package was pulled from upstream's vcs. Use the
# following commands to generate the tarball:
# svn export http://svn.cern.ch/guest/lcgdm/dpm-dsi/tags/dpm-dsi_1_9_14 dpm-dsi-1.9.14
# tar -czvf dpm-dsi-1.9.14.tar.gz dpm-dsi-1.9.14
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-64.patch
#ExcludeArch:    ppc64le

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:		cmake
BuildRequires:		dmlite-devel
BuildRequires:		globus-gridftp-server-devel >= 11.8-4
BuildRequires:          globus-common-progs
BuildRequires:		voms-devel
BuildRequires:		yum-utils
%if %systemd
BuildRequires:          systemd
%endif

%if %systemd
Requires(post):         systemd
Requires(preun):        systemd
Requires(postun):       systemd
%else
Requires(post):         chkconfig
Requires(preun):        chkconfig
Requires(preun):        initscripts
Requires(postun):       initscripts
%endif
Requires:		dmlite-libs >= 1.11.0
Requires:               globus-gridftp-server-progs >= 11.8-4

Provides:		DPM-gridftp-server = %{version}-%{release} 
Obsoletes:		DPM-gridftp-server <= 1.8.1
Provides:		DPM-DSI = %{version}-%{release} 
Obsoletes:		DPM-DSI <= 1.8.1

%description
The dpm-dsi package provides a Disk Pool Manager (DPM) plugin for the 
Globus GridFTP server, following the Globus Data Storage Interface (DSI).

The Disk Pool Manager (DPM) is a lightweight storage solution for grid sites.
It offers a simple way to create a disk-based grid storage element and 
supports relevant protocols (SRM, gridFTP, RFIO) for file 
management and access.

Globus provides open source grid software, including a server implementation
of the GridFTP protocol. This plugin implements the DPM backend specifics 
required to expose the data using this protocol.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%if %systemd
        %cmake . -DCMAKE_INSTALL_PREFIX=/ -DSYSTEMD_INSTALL_DIR=%{_unitdir}
%else
        %cmake . -DCMAKE_INSTALL_PREFIX=/
%endif

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

install -p -d -m 755 %{buildroot}%{_localstatedir}/log/dpm-gsiftp

%files
%if %systemd
%attr(0644,root,root) %{_unitdir}/dpm-gsiftp.service
%else
%{_initrddir}/dpm-gsiftp
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/dpm-gsiftp
%config(noreplace) %{_sysconfdir}/sysconfig/dpm-gsiftp
%{_libdir}/libglobus_gridftp_server_dmlite*.so*
%{_localstatedir}/log/dpm-gsiftp
%doc LICENSE RELEASE-NOTES

%post
%if %systemd
        /bin/systemctl daemon-reload > /dev/null 2>&1 || :
%else
        /sbin/chkconfig --add dpm-gsiftp
%endif
/sbin/ldconfig

%preun
if [ $1 -eq 0 ] ; then
%if %systemd
        /bin/systemctl stop dpm-gsiftp.service > /dev/null 2>&1 || :
        /bin/systemctl --no-reload disable dpm-gsiftp.service > /dev/null 2>&1 || :
%else
        /sbin/service dpm-gsiftp stop > /dev/null 2>&1
        /sbin/chkconfig --del dpm-gsiftp
%endif
fi

%postun
/sbin/ldconfig
if [ $1 -ge 1 ]; then
%if %systemd
        /bin/systemctl try-restart dpm-gsiftp.service > /dev/null 2>&1 || :
%else
        /sbin/service dpm-gsiftp condrestart > /dev/null 2>&1 || :
%endif
fi

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.9.14-4
- Rebuilt for dmlite 1.11.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.9.14-2
- Enable systemd on EPEL7

* Tue Mar 27 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.9.14-1
- Upstream 1.9.14

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.13-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Andrey Kiryanov <Andrey.Kiryanov.@cern.ch> - 1.9.13-1
- New Globus API from https://github.com/globus/globus-toolkit/pull/98

* Wed Mar 15 2017 Andrea Manzi <andrea.manzi@cern.ch> - 1.9.12-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Andrea Manzi <andrea.manzi@cern.ch> - 1.9.11-1
- New upstream release

* Mon Nov 07 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.9.10-2
- Rebuilt for globus-gridftp-server 11.8

* Fri Oct 14 2016 Andrea Manzi <andrea.manzi@cern.ch> - 1.9.10-1
- New upstream release

* Tue Oct 04 2016 Andrea Manzi <andrea.manzi@cern.ch> - 1.9.9-1
- New upstream release

* Mon Sep 05 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.9.8-3
- Rebuilt for globus-gridftp-server 11.3

* Thu Aug 18 2016 Andrea Manzi <andrea.manzi@cern.ch> - 1.9.8-2
- Build with the new gridftp server

* Mon Aug 01 2016 Andrea Manzi <andrea.manzi@cern.ch> - 1.9.8-1
- Systemd support
- support for gridftp 11.1

* Wed Jul 27 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.9.7-7
- Rebuilt for globus-gridftp-server 11.1

* Thu May 19 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.7-6
- Rebuilt for globus-gridftp-server 10.4

* Fri May 06 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.7-5
- Rebuilt for globus-gridftp-server 10.2

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.7-4
- Rebuilt for globus-gridftp-server 9.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.7-2
- Rebuilt for globus-gridftp-server 9.4

* Thu Jan 07 2016 Andrey Kiryanov <andrey.Kiryanov.@cern.ch> - 1.9.7-1
- fix for Gridftp Redirection: transfers with checksums fail when delayed passive is enabled
- fix for Gridftp Redirection: transfer overwrite  fails
- fix for Gridftp logs not compressed
- Implemented checksum calculation on the disknodes with Gridftp Redirection enabled

* Thu Nov 26 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.5-13
- Rebuilt for globus-gridftp-server 9.3

* Fri Nov 06 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.5-12
- Rebuilt for globus-gridftp-server 9.1

* Tue Nov 03 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.5-11
- Adapt properly to globus-gridftp-server 9.0

* Tue Oct 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.5-10
- Rebuilt for globus-gridftp-server 9.0

* Sun Oct 25 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.9.5-9
- Rebuilt for globus-gridftp-server 8.9

* Mon Aug 31 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.9.5-8
- Rebuilt for globus-gridftp-server 8.7

* Tue Aug 11 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.9.5-7
- Rebuilt for globus-gridftp-server 8.1

* Tue Jul 28 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.9.5-6
- Rebuilt for globus-gridftp-server 8.0

* Tue Jun 23 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.9.5-5
- Avoid hardcoded dependency on Globus

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Laurence Field <laurence.field@cern.ch> - 1.9.5-3
- Strict dependency towards Globus and minor fixes for compatibility

* Fri Apr 17 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.9.5-2
- Missing fix by upstream

* Thu Apr 16 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.9.5-1
- Update for new upstream release

* Wed Apr 08 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.9.4-1
- Update for new upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Michal Simon <michal.simon@cern.ch> - 1.9.3-3
- Patch for the FTS2 issue 

* Thu May 15 2014 Alejandro Alvarez <aalvarez@cern.ch> - 1.9.3-2
- Patch for proper EOF handling

* Wed Mar 12 2014 Alejandro Alvarez <aalvarez@cern.ch> - 1.9.3-1
- Update for new upstream release
- Fixed bogus date

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 Alejandro Alvarez <aalvarez@cern.ch> - 1.9.0-3
- Removed devel package
- Removed %%{?_isa} suffix from globus-gridftp-server-progs

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.9.0-1
- Update for new upstream release

* Fri Dec 14 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.8.3-1
- Update to new upstream release
- Removed previously required patches (integrated upstream)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Dan Horák <dan[at]danny.cz> - 1.8.2-6
- fix build on 64-bit arches (s390x, sparc64 and possibly others)

* Tue Nov 15 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.8.2-5
- Removed architecture from globus-gridftp-server-progs requires

* Wed Nov 09 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.8.2-4
- Added patch for proper libdir usage in ppc64

* Wed Nov 09 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.8.2-3
- Added patch for LD_LIBRARY_PATH setting in init script

* Fri Nov 04 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.8.2-2
- Removed README and LICENSE from devel package
- Added parallel flags to make command

* Mon Oct 17 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.8.2-1
- Initial build
