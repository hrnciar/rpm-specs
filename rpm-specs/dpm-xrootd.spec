Name:		dpm-xrootd
Summary:	XROOT interface to the Disk Pool Manager (DPM)
Version:	3.6.6
Release:	4%{?dist}
License:	GPLv3
URL:		http://svnweb.cern.ch/trac/lcgdm
# The source of this package was pulled from upstream's vcs. Use the 
# following commands to generate the tarball: 
# svn export http://svn.cern.ch/guest/lcgdm/dpm-xrootd/tags/dpm-xrootd_3_6_6 dpm-xrootd-3.6.6
# tar -czvf dpm-xrootd-3.6.6.tar.gz dpm-xrootd-3.6.6
Source0:	%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	dmlite-devel >= 0.8.1
BuildRequires:	dmlite-private-devel >= 0.8.1
BuildRequires:	openssl-devel
BuildRequires:	xrootd-server-devel >= 1:4.2
%if %{?fedora}%{!?fedora:0} >= 17 || %{?rhel}%{!?rhel:0} >= 7
BuildRequires:                  boost-devel >= 1.48.0
%else
BuildRequires:                  boost148-devel >= 1.48.0
%endif

Requires(preun):	chkconfig
Requires(post):		chkconfig
%if %{?fedora}%{!?fedora:0} < 29
Requires(preun):	initscripts
Requires(postun):	initscripts
%endif
Requires:		xrootd >= 1:4.2
Requires:		xrootd-client >= 1:4.2
Requires:		xrootd-selinux >= 1:4.2
Requires:		dmlite-libs >= 0.8.1
Provides:		DPM-xrootd = %{version}-%{release}
Obsoletes:		DPM-xrootd <= 2.2.0
Conflicts:		vomsxrd <= 1:0.2.0
Conflicts:		xrootd-server-atlas-n2n-plugin <= 2.1
Conflicts:		xrootd-alicetokenacc <= 1.2.2

%description
This package contains plugins for XROOTD to allow it to provide
access to DPM managed storage via the XROOT protocol.

%package devel 
Summary:	Development libraries and headers for the DPM XROOT interface 
Requires:	dpm-xrootd%{?isa} = %{version}-%{release} 
 
%description devel 
This package contains the development libraries and headers for the  
DPM XROOT interface. 

%prep
%setup -q -n %{name}-%{version}

%build
%cmake . -DCMAKE_INSTALL_PREFIX=/ -DOVERWRITE_CONFIGFILES=ON

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}
ln -s libXrdDPMFinder-4.so %{buildroot}%{_libdir}/libXrdDPMFinder.so-4.3
ln -s libXrdDPMDiskAcc-4.so %{buildroot}%{_libdir}/libXrdDPMDiskAcc.so-4.3
ln -s libXrdDPMOss-4.so %{buildroot}%{_libdir}/libXrdDPMOss.so-4.3
ln -s libXrdDPMRedirAcc-4.so %{buildroot}%{_libdir}/libXrdDPMRedirAcc.so-4.3
ln -s libXrdDPMStatInfo-4.so %{buildroot}%{_libdir}/libXrdDPMStatInfo.so-4.3

%post -p /sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
    /sbin/service xrootd stop >/dev/null 2>&1 || :
    /sbin/service cmsd stop >/dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
if [ "$1" -ge "1" ] ; then
    /sbin/service xrootd condrestart >/dev/null 2>&1 || :
    /sbin/service cmsd condrestart >/dev/null 2>&1 || :
fi

%files
%config(noreplace) %{_sysconfdir}/xrootd/xrootd-dpmdisk.cfg
%config(noreplace) %{_sysconfdir}/xrootd/xrootd-dpmfedredir_atlas.cfg
%config(noreplace) %{_sysconfdir}/xrootd/xrootd-dpmredir.cfg
%{_libdir}/libXrdDPMDiskAcc-4.so
%{_libdir}/libXrdDPMDiskAcc.so-4.3
%{_libdir}/libXrdDPMFinder-4.so
%{_libdir}/libXrdDPMFinder.so-4.3
%{_libdir}/libXrdDPMOss-4.so
%{_libdir}/libXrdDPMOss.so-4.3
%{_libdir}/libXrdDPMRedirAcc-4.so
%{_libdir}/libXrdDPMRedirAcc.so-4.3
%{_libdir}/libXrdDPMStatInfo-4.so
%{_libdir}/libXrdDPMStatInfo.so-4.3
%doc COPYING RELEASE-NOTES

%files devel 
%dir %{_includedir}/XrdDPM
%{_includedir}/XrdDPM/XrdCompileVersion.hh

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Oliver Keeble <oliver.keeble@cern.ch> - 3.6.6-1
- New upstream release 3.6.6

* Tue Aug 28 2018 Oliver Keeble <oliver.keeble@cern.ch> - 3.6.5-1
- New upstream release 3.6.5

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Oliver Keeble <oliver.keeble@cern.ch> - 3.6.4-5
- Upstream 3.6.4b

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Andrea Manzi <andrea.manzi@cern.ch> 3.6.4-1
- included patch for openssl 1.1.0 from Mattias

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Andrea Manzi <andrea.manzi@cern.ch> 3.6.3-1
- new upstream release

* Fri Oct 14 2016 Andrea Manzi <andrea.manzi@cern.ch> 3.6.2-1
- new upstream release

* Fri Sep 23 2016 Andrea Manzi <andrea.manzi@cern.ch> 3.6.1-1
- new upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 David Smith <david.smith@cern.ch> 3.6.0-1
- introduced the XrdDPMStatInfo plugin
- See the RELEASE-NOTES for a summary of other changes

* Thu Sep 17 2015 David Smith <david.smith@cern.ch> 3.5.5-1
- Update for new upstream release

* Wed Apr 29 2015 David Smith <david.smith@cern.ch> 3.5.4-1
- Update for new upstream release

* Wed Apr 29 2015 David Smith <david.smith@cern.ch> 3.5.3-1
- Update for new upstream release

* Tue Dec 16 2014 David Smith <david.smith@cern.ch> 3.5.2-1
- Update for new upstream release

* Fri Sep 26 2014 Alejandro Alvarez <aalvarez@cern.ch> - 3.4.0-1
- Update for new upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Feb 04 2014 David Smith <david.smith@cern.ch> 3.3.6-1
- Update for new upstream release

* Tue Feb 04 2014 David Smith <david.smith@cern.ch> 3.3.5-1
- Update for new upstream release

* Fri Jun 21 2013 David Smith <david.smith@cern.ch> 3.3.4-1
- Update for new upstream release

* Tue Apr  2 2013 David Smith <david.smith@cern.ch> 3.3.3-1
- Update for new upstream release

* Wed Mar 27 2013 David Smith <david.smith@cern.ch> 3.3.2-1
- Update for new upstream release
- See RELEASE-NOTES for summary of changes

* Wed Feb 20 2013 David Smith <david.smith@cern.ch> 3.3.1-1
- Update version number for trunk

* Thu Jan 17 2013 David Smith <david.smith@cern.ch> 3.3.0-1
- Update version number for trunk

* Wed Dec 19 2012 David Smith <david.smith@cern.ch> 3.2.0-1
- Update for new upstream release

* Mon Oct 08 2012 David Smith <david.smith@cern.ch> 3.1.2-1
- Update for new upstream release

* Tue Jul 24 2012 David Smith <david.smith@cern.ch> 3.1.1-1
- Update for new upstream release

* Fri Jun 15 2012 Ricardo Rocha <ricardo.rocha@cern.ch> 3.1.0-1
- Update for new upstream release

* Thu May 24 2012 Ricardo Rocha <ricardo.rocha@cern.ch> 3.0.0-2
- Added devel package

* Wed Feb 29 2012 David Smith <david.smith@cern.ch> 3.0.0-1
- New packaging for 3.0.0-1

* Mon Dec 05 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 2.2.5-1
- Added dpmmgr user creation (required for service), only if non-existing
- Put init scripts in appropriate directory (initrddir)
- Moved include dir to -devel package
- Update to new upstream patch release

* Mon Nov 21 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 2.2.4-1
- Fixed license to match upstream (GPLv3)
- Update to new upstream version

* Sat Nov 19 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 2.2.3-2
- Added provides/obsoletes entry for DPM-xrootd <= 2.2.0

* Wed Nov 16 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 2.2.3-1
- Fixed spelling issues (detected by rpmlint)
- Added dependency on dpm-xrootd from devel package
- Removed ldconfig from -devel scriptlets
- Dropped useless doc files from -devel package
- Updated to build 2.2.3 upstream release (move to cmake and several fixes)

* Tue Nov 08 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 2.2.2-1
- Updated to build 2.2.2 upstream release (fixes for build in >=RHEL5)

* Mon Oct 17 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 2.2.1-1
- Initial build
