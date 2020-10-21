%{!?dmlite_test: %global dmlite_tests 0}

# systemd definition, to do the right thing if we need to restart daemons
%if %{?fedora}%{!?fedora:0} >= 17 || %{?rhel}%{!?rhel:0} >= 7
%global systemd 1
%else
%global systemd 0
%endif

%if %{?fedora}%{!?fedora:0} >= 27
%global cpp11 ON
%else
%global cpp11 OFF
%endif

%if %{?fedora}%{!?fedora:0} >= 31 || %{?rhel}%{!?rhel:0} >= 8
%global withlcgdm 0
%else
%global withlcgdm 1
%endif


# By default, build with python 2 and 3
# These settings have to be compatible with the logic in 
# python/CMakeLists.txt
%global with_python2_libs 1
%global with_python3_libs 1
%global py_app_version 2
%global boost_py2_version 2
%global boost_py3_version 3

%if %{?fedora}%{!?fedora:0} >= 31
  %global py_app_version 3
  %global with_python2_libs 0
  %global with_python3_libs 1
%endif

%if %{?fedora}%{!?fedora:99} <= 30
  %global py_app_version 2
  %global with_python2_libs 1
  %global with_python3_libs 1
%endif

%if %{?rhel}%{!?rhel:0} == 6
  %global py_app_version 2
  %global with_python2_libs 1
  %global with_python3_libs 0
%endif

%if %{?rhel}%{!?rhel:0} == 7
  %global py_app_version 2
  %global with_python2_libs 1
  %global with_python3_libs 1
  %global boost_py3_version 36
%endif

%if %{?rhel}%{!?rhel:0} >= 8
  %global py_app_version 3
  %global with_python2_libs 0
  %global with_python3_libs 1
%endif

%if %{?rhel}%{!?rhel:99} <= 7
  # no number
  %undefine python2_pkgversion
%else
  %global python2_pkgversion 2
%endif

# Handle new cmake macros

%if %{?fedora}%{!?fedora:99} <= 32 || %{?rhel}%{!?rhel:0} >= 7
  %undefine __cmake_in_source_build
  %undefine __cmake3_in_source_build
%endif

%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}

Name:					dmlite
Version:				1.13.99
Release:				8%{?dist}
Summary:				Lcgdm grid data management and storage framework
License:				ASL 2.0
URL:					https://gitlab.cern.ch/lcgdm/dmlite
# The source of this package was pulled from upstream's vcs. Use the
# following commands to generate the tarball:
# git clone --branch shell_py3_04062020 http://gitlab.cern.ch/lcgdm/dmlite.git
# cd dmlite && git archive --prefix dmlite-1.13.99/ shell_py3_04062020 | gzip > dmlite-1.13.99.tar.gz

Source0:				%{name}-%{version}.tar.gz
%if %{?fedora}%{!?fedora:0} >= 31 || %{?rhel}%{!?rhel:0} >= 8
Patch0:         dmlite-python3.patch
%endif

%if %{?fedora}%{!?fedora:0} >= 17 || %{?rhel}%{!?rhel:0} >= 7
BuildRequires:      gcc-c++
BuildRequires:      boost-devel >= 1.48.0
%else
BuildRequires:      boost148-devel >= 1.48.0
%endif

%if %{?with_python2_libs}%{!?with_python2_libs:0}
BuildRequires:      python2-rpm-macros
BuildRequires:      python2-devel
%if %{?rhel}%{!?rhel:0} == 6
BuildRequires:      boost148-python
%else 
%if %{?rhel}%{!?rhel:0} == 7
BuildRequires:      boost-python
%else
BuildRequires:      boost-python2-devel
%endif
%endif
%endif

%if %{?with_python3_libs}%{!?with_python3_libs:0}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      boost-python%{boost_py3_version}-devel
BuildRequires:      python3-rpm-macros
%endif


BuildRequires:			cmake
BuildRequires:			cmake3
BuildRequires:			cppunit-devel
BuildRequires:			doxygen
BuildRequires:			graphviz
BuildRequires:			openssl-devel
BuildRequires:			zlib-devel

# Plugins require
BuildRequires:			libmemcached-devel
%if %{?fedora}%{!?fedora:0} >= 28
BuildRequires:                  mariadb-connector-c-devel
%else
BuildRequires:                   mysql-devel
%endif
BuildRequires:			protobuf-devel
BuildRequires:			davix-devel >= 0.6.7
BuildRequires:			globus-gridftp-server-devel >= 13.20
BuildRequires:			voms-devel
%if %systemd
BuildRequires:			systemd
%endif
BuildRequires:			gridsite-devel
BuildRequires:			gsoap-devel
BuildRequires:			httpd-devel
BuildRequires:			json-c-devel
BuildRequires:  		libbsd-devel
%if %{withlcgdm}
BuildRequires:			lcgdm-devel
BuildRequires:			dpm-devel
%endif

%description
This package provides the dmlite framework that implements common
logic for data management and storage for the Lcg grid.

%package apache-httpd
Summary:	Apache HTTPD frontend for dmlite
Requires:	httpd%{?_isa}
Requires:	httpd-mmn = %{_httpd_mmn}
Requires:	dmlite-libs = %{version}-%{release}

Provides:	lcgdm-dav-server = %{version}-%{release}
Provides:	lcgdm-dav-libs = %{version}-%{release}
Provides:	mod-lcgdm-dav = %{version}-%{release}
Provides:	lcgdm-dav = %{version}-%{release}

Obsoletes:	lcgdm-dav-server < %{version}-%{release}
Obsoletes:	lcgdm-dav-libs < %{version}-%{release}
Obsoletes:	mod_lcgdm_dav < %{version}-%{release}
Obsoletes:	lcgdm-dav < %{version}-%{release}
Obsoletes:	lcgdm-dav-debuginfo < %{version}-%{release}

Requires:	gridsite%{?_isa} >= 1.7
Requires:	httpd%{?_isa}
Requires:	mod_ssl%{?_isa}

%description apache-httpd
This package provides the HTTP/WebDAV frontend to DMLite. It's used for DPM and Dynafed



%files apache-httpd
%defattr(-,root,root,-)
%{_bindir}/htcopy
%{_mandir}/man1/htcopy.1*
%doc src/plugins/apache-httpd/src/client/README LICENSE
%{_libdir}/liblcgdmhtext.so.*
%{_libdir}/libdmlitemacaroons.so*
%doc README LICENSE
%{_libdir}/httpd/modules/mod_lcgdm_ns.so
%{_libdir}/httpd/modules/mod_lcgdm_disk.so
%{_libdir}/httpd/modules/mod_lcgdm_dav.so
%{_datadir}/lcgdm-dav/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%config(noreplace) %{_sysconfdir}/cron.d/*


%if %{withlcgdm}
%package dpmhead
Summary:  EMI DPM Head Node (MySQL)
Requires: bdii
Requires: dpm%{?_isa} >= 1.10
Requires: dmlite-dpm-dsi = %{version}
Requires: dpm-name-server-mysql%{?_isa} >= 1.10
Requires: dpm-perl%{?_isa} >= 1.10
Requires: dpm-python%{?_isa} >= 1.10
Requires: dpm-rfio-server%{?_isa} >= 1.10
Requires: dpm-server-mysql%{?_isa} >= 1.10
Requires: dpm-srm-server-mysql%{?_isa} >= 1.10
Requires: dmlite-plugins-domeadapter = %{version}
Requires: dmlite-dome = %{version}
Requires: dmlite-shell = %{version}
Requires: dmlite-plugins-mysql = %{version}
Requires: edg-mkgridmap
Requires: fetch-crl
Requires: finger
Requires: dmlite-apache-httpd = %{version}
Requires: davix >= 0.6.7
Requires: dmlite-plugins-adapter = %{version}
Requires: dpm-devel%{?_isa} >= 1.10
Obsoletes: emi-dpm_mysql

%description dpmhead
The LCG Disk Pool Manager (DPM) creates a storage element from a set
of disks. It provides several interfaces for storing and retrieving
data such as HTTP, Xrootd, GridFTP

%files dpmhead
%{_prefix}/share/dmlite/dbscripts
%{_prefix}/share/dmlite/filepull
%{_prefix}/share/dmlite/StAR-accounting
%endif

%if %{withlcgdm}
%package dpmdisk
Summary:  EMI DPM Disk Node
Requires: dpm%{?_isa} >= 1.10
Requires: dpm-perl%{?_isa} >= 1.10
Requires: dpm-python%{?_isa} >= 1.10
Requires: dpm-rfio-server%{?_isa} >= 1.10
Requires: dmlite-dpm-dsi = %{version}
Requires: dmlite-plugins-domeadapter = %{version}
Requires: dmlite-dome = %{version}
Requires: dmlite-shell = %{version}
Requires: edg-mkgridmap
Requires: fetch-crl
Requires: finger
Requires: dmlite-apache-httpd = %{version}
Requires: davix >= 0.6.7
Requires: dmlite-plugins-adapter = %{version}
Requires: dpm-devel%{?_isa} >= 1.10

Obsoletes: emi-dpm_disk

%description dpmdisk
The LCG Disk Pool Manager (DPM) creates a storage element from a set
of disks. It provides several interfaces for storing and retrieving
data such as RFIO and SRM version 1, version 2 and version 2.2.
This is a virtual package providing all required daemons for a DPM
Disk Node.

%files dpmdisk
%{_prefix}/share/dmlite/filepull

%endif


%package dpmhead-domeonly
Summary:  DPM Head Node (MySQL)
Requires: bdii

Requires: dmlite-dpm-dsi = %{version}
Requires: dmlite-plugins-domeadapter = %{version}
Requires: dmlite-dome = %{version}
Requires: dmlite-shell = %{version}
Requires: dmlite-plugins-mysql = %{version}
Requires: edg-mkgridmap
Requires: fetch-crl
Requires: finger
Requires: dmlite-apache-httpd = %{version}
Requires: davix >= 0.6.7
Requires: xrootd >= 1:4.8.2

Obsoletes: emi-dpm_mysql
Obsoletes: dpmhead
Conflicts: dpm%{?_isa}
Conflicts: dpm-devel%{?_isa}
Conflicts: dpm-name-server-mysql%{?_isa}
Conflicts: dpm-perl%{?_isa}
Conflicts: dpm-rfio-server%{?_isa}
Conflicts: dpm-server-mysql%{?_isa}
Conflicts: dpm-srm-server-mysql%{?_isa}
Conflicts: dmlite-plugins-adapter

%description dpmhead-domeonly
The Disk Pool Manager (DPM) creates a Grid storage element from a set
of disk servers. It provides several interfaces for storing and retrieving
data such as HTTP, Xrootd, GridFTP
This is a metapackage providing all required daemons for a DPM Head Node.

%files dpmhead-domeonly
%{_prefix}/share/dmlite/dbscripts
%{_prefix}/share/dmlite/filepull
%{_prefix}/share/dmlite/StAR-accounting

%package dpmdisk-domeonly
Summary:  DPM Disk Node

Requires: dmlite-dpm-dsi = %{version}

Requires: dmlite-plugins-domeadapter = %{version}
Requires: dmlite-dome = %{version}
Requires: edg-mkgridmap
Requires: fetch-crl
Requires: finger
Requires: dmlite-apache-httpd = %{version}

Requires: davix >= 0.6.7

Obsoletes: emi-dpm_disk
Obsoletes: dpmdisk
Conflicts: dpm%{?_isa}
Conflicts: dpm-devel%{?_isa}
Conflicts: dpm-perl%{?_isa}
Conflicts: dpm-rfio-server%{?_isa}
Conflicts: dmlite-plugins-adapter = %{version}

%description dpmdisk-domeonly
The Disk Pool Manager (DPM) creates a Grid storage element from a set
of disk servers. It provides several interfaces for storing and retrieving
data such as HTTP, Xrootd, GridFTP
This is a metapackage providing all required daemons for a DPM
Disk Node.

%files dpmdisk-domeonly
%{_prefix}/share/dmlite/filepull


%package libs
Summary:			Libraries for dmlite packages

# transition fix for package merge dmlite-*.src.rpm to dmlite.src.rpm
Obsoletes:			dmlite-plugins-adapter-debuginfo < 0.7.0-1
Obsoletes:			dmlite-plugins-mysql-debuginfo < 0.7.0-1
Obsoletes:			dmlite-plugins-memcache-debuginfo < 0.7.0-1
Obsoletes:			dmlite-plugins-profiler-debuginfo < 0.7.0-1
Obsoletes:			dmlite-plugins-librarian-debuginfo < 0.7.0-1
Obsoletes:			dmlite-shell-debuginfo < 0.7.0-1

# dpm-xrootd was the standalone project/package. Now dmlite-dpm-xrootd is part of dmlite
Conflicts:      dpm-xrootd

# # dpm-dsi was the standalone project/package. Now it's one of the dmlite plugins
Conflicts:      dpm-dsi < %{version}

# lcgdm-dav was the standalone project/package. Now it's built with the dmlite plugins, and we don't want 
Conflicts:      lcgdm-dav-server < %{version}
Conflicts:      lcgdm-dav < %{version}
Conflicts:      lcgdm-dav-libs < %{version}
Conflicts:      mod_lcgdm_dav < %{version}

# This was due to the switch to boost 1.48, linked to the bugs in propertytree
Conflicts:      dpm-xrootd <= 3.6.0

# Versions prior to this one do not properly do accounting on directories
Conflicts:      lcgdm-libs <= 1.10

# Versions prior to this one do not have the PoolManager::fileCopyPush/Pull and
# the C calls dmlite_copypush/pull
Conflicts:      dynafed < 1.5.0

# Not really necessary, just better to limit the space for mistakes
Conflicts:      dpm-dsi < 1.9.10

%description libs
This package provides the core libraries of dmlite.

%package dome
Summary:			The dome daemon
Requires:     httpd
Requires:     xrootd >= 1:4.8.2
BuildRequires:     xrootd-devel >= 1:4.8.2
BuildRequires:     xrootd-server-devel >= 1:4.8.2
BuildRequires:     xrootd-private-devel >= 1:4.8.2

%description dome
This package provides the binaries necessary to run the dome daemon.

%package devel
Summary:			Development libraries and headers for dmlite
Requires:			%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package provides C headers and development libraries for dmlite.

%package docs
Summary:			Documentation files for dmlite


%description docs
This package contains the man pages and HTML documentation for dmlite.


%package private-devel
Summary:			Private development libraries and headers for dmlite
Requires:			%{name}-devel%{?_isa} = %{version}-%{release}
%if %{?fedora}%{!?fedora:0} >= 17 || %{?rhel}%{!?rhel:0} >= 7
BuildRequires:                  boost-devel >= 1.48.0
%else
BuildRequires:                  boost148-devel >= 1.48.0
%endif
Obsoletes:			dpm-xrootd-devel


%description private-devel
Private development headers for dmlite. Provided for the development of
dmlite plugins only, no API compatibility is guaranteed on these headers.



%package dpm-tester
Summary:      The dpm tester tool
Requires:     gfal2-plugin-http
Requires:     gfal2-plugin-xrootd
Requires:     gfal2-plugin-srm
Requires:     gfal2-plugin-gridftp
Requires:     gfal2-plugin-file
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 8
Requires:     python%{py_app_version}-gfal2
%else
Requires:     gfal2-python
%endif

%if %{?rhel}%{!?rhel:0} == 6
Requires:     python-argparse
Requires:     python2
%else 
Requires:     python%{py_app_version}-libs
Requires:     python%{py_app_version}
%endif

%description dpm-tester
Tool that is useful to test the main features of a DPM setup

%files dpm-tester
%{_bindir}/dpm-tester.py


%package dpm-dsi
Summary:	Disk Pool Manager (DPM) plugin for the Globus GridFTP server
Group:		Applications/Internet
Requires:	globus-gridftp-server-progs >= 13.20
Requires:	dmlite-libs = %{version}-%{release}

%if %systemd
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%else
Requires(post):     	chkconfig
Requires(preun):    	chkconfig
Requires(preun):    	initscripts
Requires(postun):   	initscripts
%endif

Provides:			DPM-gridftp-server = %{version}-%{release}
Obsoletes:		DPM-gridftp-server < %{version}-%{release}
Provides:			DPM-DSI = %{version}-%{release}
Obsoletes:		DPM-DSI < %{version}-%{release}
Obsoletes:		dpm-dsi < %{version}-%{release}

%description dpm-dsi
The dpm-dsi package provides a Disk Pool Manager (DPM) plugin for the 
Globus GridFTP server, following the Globus Data Storage Interface (DSI).

The Disk Pool Manager (DPM) is a lightweight storage solution for grid sites.
It offers a simple way to create a disk-based grid storage element and 
supports relevant protocols (SRM, gridFTP, RFIO) for file 
management and access.

Globus provides open source grid software, including a server implementation
of the GridFTP protocol. This plugin implements the DPM backend specifics 
required to expose the data using this protocol.



%files dpm-dsi
%defattr(-,root,root)
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

%post dpm-dsi
%if %systemd
	/bin/systemctl daemon-reload > /dev/null 2>&1 || :
%else
	/sbin/chkconfig --add dpm-gsiftp
%endif
/sbin/ldconfig

%preun dpm-dsi
if [ $1 -eq 0 ] ; then
%if %systemd
	/bin/systemctl stop dpm-gsiftp.service > /dev/null 2>&1 || :
	/bin/systemctl --no-reload disable dpm-gsiftp.service > /dev/null 2>&1 || :
%else
	/sbin/service dpm-gsiftp stop > /dev/null 2>&1
	/sbin/chkconfig --del dpm-gsiftp
%endif
fi

%postun dpm-dsi
/sbin/ldconfig 
if [ $1 -ge 1 ]; then
%if %systemd
        /bin/systemctl try-restart dpm-gsiftp.service > /dev/null 2>&1 || :
%else
	/sbin/service dpm-gsiftp condrestart > /dev/null 2>&1 || :
%endif
fi


%if %{?with_python2_libs}%{!?with_python2_libs:0}
%package -n python%{?python2_pkgversion}-dmlite
%{?python_provide:%python_provide python2-dmlite}
Summary:			Python wrapper for dmlite

%description -n python%{?python2_pkgversion}-dmlite
This package provides a python wrapper for dmlite.

%files -n python%{?python2_pkgversion}-dmlite
%defattr(-,root,root,-)
%{python2_sitearch}/pydmlite.so
%endif


%if %{?with_python3_libs}%{!?with_python3_libs:0}
%package -n python%{python3_pkgversion}-dmlite
Summary:                        Python wrapper for dmlite
Group:                          Development/Libraries
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-dmlite
This package provides a python wrapper for dmlite.

%files -n python%{python3_pkgversion}-dmlite
%defattr(-,root,root,-)
%{python3_sitearch}/pydmlite.so
%endif

%package test
Summary:			All sorts of tests for dmlite interfaces

%description test
Set of C,CPP and Python tests for dmlite interfaces and plug-ins.

%package plugins-memcache
Summary:			Memcached plugin for dmlite
Requires:			%{name}-libs%{?_isa} = %{version}-%{release}

# Merge migration
Obsoletes:			dmlite-plugins-memcache < 0.7.0-1

%description plugins-memcache
This package provides the memcached plug-in for dmlite. It provides a
memcached based layer for the Lcgdm nameserver.

%package plugins-profiler
Summary:			Monitoring plugin for dmlite
Requires:			%{name}-libs%{?_isa} = %{version}-%{release}

# Merge migration
Obsoletes:			dmlite-plugins-profiler < 0.7.0-1

%description plugins-profiler
This package provides the profiler plug-in for dmlite. This plug-in
provides multiple performance measurement tools for dmlite.


%package plugins-librarian
Summary:                        Librarian plugin for dmlite
Requires:                       %{name}-libs%{?_isa} = %{version}-%{release}

# Merge migration
Obsoletes:                      dmlite-plugins-librarian < 0.7.0-1

%description plugins-librarian
This package provides the librarian plug-in for dmlite.



%package shell
Summary:			Shell environment for dmlite

Requires:     davix >= 0.6.7

%if %{py_app_version} == 2
Requires:     python%{?python2_pkgversion}-dmlite = %{version}
Requires:     python%{?python2_pkgversion}-ldap
Requires:     python%{?python2_pkgversion}-libs
Requires:     python%{?python2_pkgversion}-dateutil
Requires:     python%{?python2_pkgversion}-mysql
Requires:     python%{?python2_pkgversion}-pycurl
Requires:     python%{?python2_pkgversion}-rpm
Requires:     m2crypto
%endif

%if %{py_app_version} == 3
Requires:     python%{python3_pkgversion}-dmlite = %{version}
Requires:     python%{python3_pkgversion}-ldap
Requires:     python%{python3_pkgversion}-libs
Requires:     python%{python3_pkgversion}-dateutil
Requires:     python%{python3_pkgversion}-mysql
Requires:     python%{python3_pkgversion}-pycurl
Requires:     python%{python3_pkgversion}-rpm
Requires:     python%{python3_pkgversion}-m2crypto
%endif

Obsoletes:			dmlite-shell < %{version}-%{release}

%description shell
This package provides a shell environment for dmlite. It includes useful
commands for system administration, testers and power users.

%files shell
%{_bindir}/dmlite-shell
%{_bindir}/dpm-storage-summary.py
%{_bindir}/dpm-storage-summary.cgi
%{_bindir}/dmlite-mysql-dirspaces.py
%{_bindir}/dome-info-provider.py
%{_sharedstatedir}/bdii/gip/provider/dome-info-exec
%config(noreplace) %{_sysconfdir}/sysconfig/dpminfo
%if %{py_app_version} == 2
%{python2_sitelib}/dmliteshell
%else
%{python3_sitelib}/dmliteshell
%endif
%doc LICENSE README RELEASE-NOTES


%package dpm-xrootd
Summary:			XROOT interface to the Disk Pool Manager (DPM)
Requires:			%{name}-libs%{?_isa} = %{version}-%{release}
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(post):		chkconfig
Requires(postun):	initscripts
Requires:		xrootd >= 1:4.2
Requires:		xrootd-client >= 1:4.2
Requires:		xrootd-selinux >= 1:4.2
Conflicts:		vomsxrd <= 1:0.2.0
Conflicts:		xrootd-server-atlas-n2n-plugin <= 2.1
Conflicts:		xrootd-alicetokenacc <= 1.2.2
BuildRequires:	openssl-devel
BuildRequires:	xrootd-server-devel >= 1:4.2
%if %{?fedora}%{!?fedora:0} >= 17 || %{?rhel}%{!?rhel:0} >= 7
BuildRequires:                  boost-devel >= 1.48.0
%else
BuildRequires:                  boost148-devel >= 1.48.0
%endif
Obsoletes:              dpm-xrootd

%description dpm-xrootd
This package contains plugins for XROOTD to allow it to provide
access to DPM managed storage via the XROOT protocol.


%preun dpm-xrootd
if [ "$1" = "0" ]; then
    /sbin/service xrootd stop >/dev/null 2>&1 || :
    /sbin/service cmsd stop >/dev/null 2>&1 || :
fi

%postun dpm-xrootd
/sbin/ldconfig
if [ "$1" -ge "1" ] ; then
    /sbin/service xrootd condrestart >/dev/null 2>&1 || :
    /sbin/service cmsd condrestart >/dev/null 2>&1 || :
fi

%files dpm-xrootd
%defattr(-,root,root)
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
%{_libdir}/libXrdDPMCks-4.so
%{_libdir}/libXrdDPMCks.so-4.3


%package plugins-mysql
Summary:			MySQL plugin for dmlite
Requires:			%{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes:			dmlite-plugins-mysql < 0.7.0-1

%description plugins-mysql
This package provides the MySQL plug-in for dmlite.

%if %{withlcgdm}
%package plugins-adapter
Summary:			Adapter plugin for dmlite
Requires:			%{name}-libs%{?_isa} = %{version}-%{release}
Requires:			dpm-libs >= 1.8.8
Requires:			lcgdm-libs >= 1.8.8
Obsoletes:			dmlite-plugins-adapter < 0.7.0-1

%description plugins-adapter
This package provides the adapter plug-in for dmlite. This plug-in provides both
a name-space and pool management implementation which fallback to forwarding
calls to the old LcgDM DPNS and DPM daemons.

%files plugins-adapter
%{_libdir}/dmlite/plugin_adapter.so
%doc LICENSE README RELEASE-NOTES
%config(noreplace) %{_sysconfdir}/dmlite.conf.d/adapter.conf
%endif

%package plugins-domeadapter
Summary:      Adapter plugin for dmlite
Requires:     %{name}-libs%{?_isa} = %{version}-%{release}

%description plugins-domeadapter
This package provides the next-generation adapter plug-in for dmlite, which uses
dome and does not depend on the old LcgDM DPNS and DPM daemons.

%package puppet-dpm
Summary:                        Puppet modules for DPM configuration
BuildArch:                      noarch
Obsoletes:                      dmlite-puppet-dpm < %{version}-%{release}


%description puppet-dpm
This package provides the modules for the DPM configuration via puppet

%prep
%setup -q -n %{name}-%{version}
%if %{?fedora}%{!?fedora:0} >= 31 || %{?rhel}%{!?rhel:0} >= 8
%patch0 -p1
%endif

%build
./src/plugins/apache-httpd/buildcurl.sh
%if %systemd
%if %{?fedora}%{!?fedora:0} >= 28
    %cmake3 . -DCMAKE_INSTALL_PREFIX=/ -DRUN_ONLY_STANDALONE_TESTS=ON -DOVERWRITE_CONFIGFILES=ON -DSYSTEMD_INSTALL_DIR=%{_unitdir} -DBUILD_MEMCACHE=OFF
%else
    %cmake3 . -DCMAKE_INSTALL_PREFIX=/ -DRUN_ONLY_STANDALONE_TESTS=ON -DOVERWRITE_CONFIGFILES=ON -DSYSTEMD_INSTALL_DIR=%{_unitdir} 
%endif
%else
	%cmake3 . -DCMAKE_INSTALL_PREFIX=/ -DRUN_ONLY_STANDALONE_TESTS=ON -DOVERWRITE_CONFIGFILES=ON
%endif

%{cmake_build} %{?_smp_mflags}
make -C %{_vpath_builddir} doc

%check
pushd %{_vpath_builddir}/tests
LD_LIBRARY_PATH=~+/../src/ ctest -V
if [ $? -ne 0 ]; then
    exit 1
fi
popd

%install
pushd %{_vpath_builddir}

rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}

make install DESTDIR=%{buildroot}
# clean up the startup scripts we don't need - otherwise rpmbuild will fail
# due to unpackaged files
%if %systemd
  rm -rf %{buildroot}/%{_sysconfdir}/rc.d
%else
  rm -rf %{buildroot}/usr/lib/systemd
%endif

## remote tests if not needed
%if %{?dmlite_tests} == 0
rm -rf %{buildroot}/%{_libdir}/dmlite/test
%endif

popd

%define basefolder %{buildroot}/%{_prefix}/share/dmlite/puppet/modules
mkdir -p %{basefolder}
cp -R src/puppet/dmlite %{basefolder}
cp -R src/puppet/dpm %{basefolder}
cp -R src/puppet/gridftp %{basefolder}
cp -R src/puppet/lcgdm %{basefolder}
cp -R src/puppet/voms  %{basefolder}
cp -R src/puppet/xrootd %{basefolder}
mkdir -p %{basefolder}/bdii
tar zxvf src/puppet/CERNOps-bdii-*.tar.gz -C %{basefolder}/bdii/ --strip-components 1
mkdir -p %{basefolder}/fetchcrl
tar zxvf src/puppet/puppet-fetchcrl-*.tar.gz -C %{basefolder}/fetchcrl/ --strip-components 1
mkdir -p %{basefolder}/firewall
tar zxvf src/puppet/puppetlabs-firewall-*.tar.gz -C %{basefolder}/firewall/ --strip-components 1
mkdir -p %{basefolder}/memcached
tar zxvf src/puppet/saz-memcached-*.tar.gz -C %{basefolder}/memcached/ --strip-components 1
mkdir -p %{basefolder}/mysql
tar zxvf src/puppet/puppetlabs-mysql-*.tar.gz -C %{basefolder}/mysql/ --strip-components 1
mkdir -p %{basefolder}/staging
tar zxvf src/puppet/nanliu-staging-*.tar.gz -C %{basefolder}/staging/ --strip-components 1
mkdir -p %{basefolder}/stdlib
tar zxvf src/puppet/puppetlabs-stdlib-*.tar.gz -C %{basefolder}/stdlib --strip-components 1
mkdir -p %{basefolder}/concat
tar zxvf src/puppet/puppetlabs-concat-*.tar.gz  -C %{basefolder}/concat/ --strip-components 1


## for dpm-xrootd
ln -s libXrdDPMFinder-4.so %{buildroot}%{_libdir}/libXrdDPMFinder.so-4.3
ln -s libXrdDPMDiskAcc-4.so %{buildroot}%{_libdir}/libXrdDPMDiskAcc.so-4.3
ln -s libXrdDPMOss-4.so %{buildroot}%{_libdir}/libXrdDPMOss.so-4.3
ln -s libXrdDPMRedirAcc-4.so %{buildroot}%{_libdir}/libXrdDPMRedirAcc.so-4.3
ln -s libXrdDPMStatInfo-4.so %{buildroot}%{_libdir}/libXrdDPMStatInfo.so-4.3
ln -s libXrdDPMCks-4.so %{buildroot}%{_libdir}/libXrdDPMCks.so-4.3

## for dpm-dsi
install -p -d -m 755 %{buildroot}%{_localstatedir}/log/dpm-gsiftp

%post libs
/sbin/ldconfig
/sbin/service rsyslog condrestart || true
%if %systemd
        /bin/systemctl try-restart dpm.service || true
        /bin/systemctl try-restart dpnsdaemon.service || true
        /bin/systemctl try-restart httpd.service || true
        /bin/systemctl try-restart dpm-gsiftp.service || true
%else
        /sbin/service dpm condrestart  || true
        /sbin/service dpnsdaemon condrestart ||true
        /sbin/service httpd condrestart || true
        /sbin/service dpm-gsiftp condrestart || true
%endif


%postun libs 
/sbin/ldconfig
/sbin/service rsyslog condrestart || true

%files libs
%dir %{_sysconfdir}/dmlite.conf.d
%dir %{_libdir}/dmlite
%config(noreplace) %{_sysconfdir}/dmlite.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/dmlite
%config(noreplace) %{_sysconfdir}/rsyslog.d/20-log-dmlite.conf
%{_libdir}/libdmlite.so.*
%{_libdir}/dmlite/plugin_config.so
%doc README LICENSE RELEASE-NOTES

%files dome
%{_bindir}/dome-checksum
%{_libdir}/libdome*.so
%{_sysconfdir}/domehead.conf.example
%{_sysconfdir}/domedisk.conf.example

%files devel
%{_includedir}/dmlite/c
%{_includedir}/dmlite/common
%{_libdir}/libdmlite.so
%{_includedir}/lcgdm-dav
%{_libdir}/liblcgdmhtext.so

%files private-devel
%{_includedir}/dmlite/cpp
## for dpm-xrootd
%defattr(-,root,root) 
%dir %{_includedir}/XrdDPM
%{_includedir}/XrdDPM/XrdCompileVersion.hh



%files docs
%{_mandir}/man3/*
%{_defaultdocdir}/%{name}-%{version}

%if %{?dmlite_tests}

%files test
%{_libdir}/dmlite/test

%endif

%files plugins-memcache
%if %{?fedora}%{!?fedora:0} < 28
%{_libdir}/dmlite/plugin_memcache.so
%doc LICENSE README RELEASE-NOTES
%config(noreplace) %{_sysconfdir}/dmlite.conf.d/zmemcache.conf
%endif

%files plugins-profiler
%{_libdir}/dmlite/plugin_profiler.so
%doc LICENSE README RELEASE-NOTES
%config(noreplace) %{_sysconfdir}/dmlite.conf.d/profiler.conf

%files plugins-librarian
%{_libdir}/dmlite/plugin_librarian.so
%doc LICENSE README RELEASE-NOTES



%files plugins-mysql
%{_libdir}/dmlite/plugin_mysql.so
%doc LICENSE README RELEASE-NOTES
%config(noreplace) %{_sysconfdir}/dmlite.conf.d/mysql.conf

%files plugins-domeadapter
%{_libdir}/dmlite/plugin_domeadapter.so
%doc LICENSE README RELEASE-NOTES
%config(noreplace) %{_sysconfdir}/dmlite.conf.d/domeadapter.conf

%files puppet-dpm
%{_prefix}/share/dmlite/puppet/modules

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.99-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.13.99-7
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13.99-6
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.13.99-5
- Rebuild (json-c)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.99-2
- Require correct version of python-ldap and m2crypto

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Andrea Manzi <amanzi@cern.ch> - 1.13.1-1
- new upstream release

* Wed Jul 10 2019 Oliver Keeble <oliver.keeble@cern.ch> - 1.13.0-1
- New upstream release 1.13.0

* Fri Mar 15 2019 Oliver Keeble <oliver.keeble@cern.ch> - 1.12.1-1
- New upstream release 1.12.1

* Fri Mar 08 2019 Oliver Keeble <oliver.keeble@cern.ch> - 1.12.0-1
- New upstream release 1.12.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.11.1-2
- Rebuilt for Boost 1.69

* Fri Jan 11 2019 Oliver Keeble <oliver.keeble@cern.ch> - 1.11.1-1
- New upstream release 1.11.1

* Thu Aug 30 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.10.4-2
- Update dmlite-shell deps

* Mon Aug 27 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.10.4-1
- New upstream release 1.10.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.10.3-1
- New upstream release

* Thu Apr 19 2018 Andrea Manzi <amanzi@cern.ch> - 1.10.2-1
- new upstream release

* Thu Apr 05 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.10.1-4
- Fix dependency on epel7/el6

* Fri Mar 23 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.10.1-3
- New upstream 1.10.1l

* Mon Mar 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.10.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 16 2018 Andrea Manzi <amanzi@cern.ch> - 1.10.0-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8.8-5
- Rebuild for protobuf 3.5

* Tue Nov 14 2017 Andrea Manzi <amanzi@cern.ch> - 0.8.8-4
- new version to fix build with rawhide

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.8-3
- Rebuild for protobuf 3.4

* Thu Sep 21 2017 Andrea Manzi <amanzi@cern.ch> - 0.8.8-2
- change mysql-devel to mariadb-connector-c-devel

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.7-6
- Python 2 binary package renamed to python2-dmlite
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 0.8.7-3
- Rebuilt for Boost 1.64

* Wed Jun 28 2017 Andrea Manzi <amanzi@cern.ch> - 0.8.7-1
- New upstream release

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 0.8.6-3
- Rebuild for protobuf 3.3.1

* Fri Apr 07 2017 Andrea Manzi <amanzi@cern.ch> - 0.8.6-2
- New upstream release

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 0.8.5-3
- Rebuilt for Boost 1.63

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 0.8.5-2
- Rebuild for protobuf 3.2.0

* Wed Nov 30 2016  Andrea Manzi <amanzi@cern.ch> - 0.8.4-1
* bug fixes

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 0.8.3-2
- Rebuild for protobuf 3.1.0

* Wed Nov 09 2016  Andrea Manzi <amanzi@cern.ch> - 0.8.3-1
* bug fixes

* Fri Oct 28 2016  Andrea Manzi <amanzi@cern.ch> - 0.8.2-1
* bug fixes

* Thu Oct 13 2016  Andrea Manzi <amanzi@cern.ch> - 0.8.1-1
* bug fixes

* Thu Sep 22 2016  Andrea Manzi <amanzi@cern.ch> - 0.8.0-1
* new upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 04 2016  Andrea Manzi <amanzi@cern.ch> - 0.7.6-3
- moved to boost 1.4.8 on SL5/SL6

* Mon Feb 15 2016  Andrea Manzi <amanzi@cern.ch> - 0.7.6-1
- Added move replicat to dmlite-shell
- fix crash in dmlite-plugins-mysql
- some fixes in dmlite-shell drain


* Mon Nov 02 2015  Andrea Manzi <amanzi@cern.ch> - 0.7.5-1
- added xattr to Memcache plugin
- fix for checksums store

* Wed Jul 08 2015  Fabrizio Furano <furano@cern.ch> - 0.7.3-1
- Add librarian to the core plugins

* Mon Nov 17 2014  Fabrizio Furano <furano@cern.ch> - 0.7.2-1
- Fix logname on RFIO.cpp
- Fix logging issue in adapter

* Fri Oct 03 2014 Andrea Manzi <amanzi@cern.ch> - 0.7.1-1
- Fix for wrong file size stored in Memcache
- Fix for xroot third party copy when Memcache enabled

* Mon Jun 16 2014 Fabrizio Furano <furano@cern.ch> - 0.7.0-2
- Push on Fedora/EPEL for 0.7.0
- Fix ppc EPEL5 compilation issue

* Mon Jun 16 2014 Fabrizio Furano <furano@cern.ch> - 0.7.0-1
- Introduced the private devel headers
- Merged shell, profiler, memcache, mysql, adapter

* Fri Nov 29 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.6.1-2
- Enabled Python bindings

* Wed Jul 10 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.6.1-1
- Update for new upstream release

* Wed Dec 19 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.6.0-1
- Update for new upstream release

* Thu Oct 25 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.5.0-1
- Update for new upstream release

* Wed Oct 24 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.4.2-2
- Fedora #869568 - dmlite-libs should own /usr/lib(64)/dmlite

* Mon Sep 24 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.4.2-1
- update for new upstream release
- dropped plugin packages (moved to separate individual packages)

* Sat Sep 22 2012  Remi Collet <remi@fedoraproject.org> - 0.3.0-2
- rebuild against libmemcached.so.11 without SASL

* Thu Jul 19 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.3.0-1
- Update for new upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.2.0-3
- Removed subversion build dep
- Added patches for proper tests compilation (missing include, wrong cmake dep)

* Tue Feb 28 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.2.0-2
- Split plugins into multiple packages, added dependencies
- Updated package descriptions

* Tue Jan 31 2012 Alejandro Alvarez <alejandro.alvarez.ayllon@cern.ch> - 0.2.0-1
- Added documentation to the build process

* Mon Jan 23 2012 Alejandro Alvarez <alejandro.alvarez.ayllon@cern.ch> - 0.1.0-1
- Added cppunit-devel as a build dependency

* Fri Jan 20 2012 Alejandro Alvarez <alejandro.alvarez.ayllon@cern.ch> - 0.1.0-1
- Created spec file
