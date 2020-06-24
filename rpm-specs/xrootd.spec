%if %{?fedora}%{!?fedora:0} >= 21 || %{?rhel}%{!?rhel:0} >= 7
%global use_systemd 1
%else
%global use_systemd 0
%endif

%if %{?fedora}%{!?fedora:0} >= 22 || %{?rhel}%{!?rhel:0} >= 7
%global use_libc_semaphore 1
%else
%global use_libc_semaphore 0
%endif

%if %{?fedora}%{!?fedora:0} >= 30 || %{?rhel}%{!?rhel:0} >= 8
%global py2 0
%else
%global py2 1
%endif

%if %{?fedora}%{!?fedora:0} >= 28 || %{?rhel}%{!?rhel:0} >= 7
%global macaroons 1
%else
%global macaroons 0
%endif

Name:		xrootd
Epoch:		1
Version:	4.12.2
Release:	3%{?dist}
Summary:	Extended ROOT file server

License:	LGPLv3+
URL:		http://xrootd.org/
Source0:	http://xrootd.org/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	fuse-devel
BuildRequires:	krb5-devel
BuildRequires:	libcurl-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-generators
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	selinux-policy-devel
%if %{use_systemd}
BuildRequires:	systemd-devel
%endif
%if %{py2}
BuildRequires:	python2-devel
%endif
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	python3-devel
BuildRequires:	python3-sphinx
%endif
%if %{?rhel}%{!?rhel:0} == 7
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_other_pkgversion}-devel
BuildRequires:	python2-sphinx
%endif
%if %{?rhel}%{!?rhel:0} == 6
BuildRequires:	python-sphinx10
%endif
%if %{macaroons}
BuildRequires:	json-c-devel
BuildRequires:	libmacaroons-devel
%endif
BuildRequires:	libuuid-devel
BuildRequires:	voms-devel >= 2.0.6

Requires:	%{name}-server%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-selinux = %{epoch}:%{version}-%{release}
Obsoletes:	%{name} < 1:4.0.0

%description
The Extended root file server consists of a file server called xrootd
and a cluster management server called cmsd.

The xrootd server was developed for the root analysis framework to
serve root files. However, the server is agnostic to file types and
provides POSIX-like access to any type of file.

The cmsd server is the next generation version of the olbd server,
originally developed to cluster and load balance Objectivity/DB AMS
database servers. It provides enhanced capability along with lower
latency and increased throughput.

%package server
Summary:	Xrootd server daemons
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	expect
Requires:	logrotate
Requires(pre):		shadow-utils
%if %{use_systemd}
%{?systemd_requires}
%else
Requires(pre):		chkconfig
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	initscripts
%endif

%description server
This package contains the xrootd servers without the SELinux support.
Unless you are installing on a system without SELinux also install the
xrootd-selinux package.

%package selinux
Summary:	SELinux policy module for the xrootd server
BuildArch:	noarch
Requires:	selinux-policy
Requires(post):		policycoreutils
Requires(postun):	policycoreutils

%description selinux
This package contains SELinux policy module for the xrootd server package.

%package libs
Summary:	Libraries used by xrootd servers and clients
#		Java admin client no longer supported
Obsoletes:	%{name}-client-admin-java < 1:3.3.0
#		Perl admin client no longer supported
Obsoletes:	%{name}-client-admin-perl < 1:4.0.0
%if ! %{py2}
#		Python 2 bindings not built for Fedora 30+
Obsoletes:	%{name}-python < 1:4.6.1-6
Obsoletes:	python2-%{name} < %{epoch}:%{version}-%{release}
%endif

%description libs
This package contains libraries used by the xrootd servers and clients.

%package devel
Summary:	Development files for xrootd
Provides:	%{name}-libs-devel = %{epoch}:%{version}-%{release}
Provides:	%{name}-libs-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-libs-devel < %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files and development libraries for xrootd
development.

%package client-libs
Summary:	Libraries used by xrootd clients
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client-libs
This package contains libraries used by xrootd clients.

%package client-devel
Summary:	Development files for xrootd clients
Provides:	%{name}-cl-devel = %{epoch}:%{version}-%{release}
Provides:	%{name}-cl-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-cl-devel < %{epoch}:%{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client-devel
This package contains header files and development libraries for xrootd
client development.

%package server-libs
Summary:	Libraries used by xrootd servers
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description server-libs
This package contains libraries used by xrootd servers.

%package server-devel
Summary:	Development files for xrootd servers
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description server-devel
This package contains header files and development libraries for xrootd
server development.

%package private-devel
Summary:	Private xrootd headers
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description private-devel
This package contains some private xrootd headers. Backward and forward
compatibility between versions is not guaranteed for these headers.

%package client
Summary:	Xrootd command line client tools
Provides:	%{name}-cl = %{epoch}:%{version}-%{release}
Provides:	%{name}-cl%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-cl < %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client
This package contains the command line tools used to communicate with
xrootd servers.

%package fuse
Summary:	Xrootd FUSE tool
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	fuse

%description fuse
This package contains the FUSE (file system in user space) xrootd mount
tool.

%package voms
Summary:	VOMS attribute extractor plug-in for XRootD
Provides:	vomsxrd = %{epoch}:%{version}-%{release}
Provides:	%{name}-voms-plugin = %{epoch}:%{version}-%{release}
Obsoletes:	vomsxrd < 1:0.6.0-4
Obsoletes:	%{name}-voms-plugin < 1:0.6.0-3
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description voms
The VOMS attribute extractor plug-in for XRootD.

%if %{py2}
%package -n python2-%{name}
Summary:	Python 2 bindings for xrootd
%{?python_provide:%python_provide python2-%{name}}
Provides:	%{name}-python = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-python < 1:4.6.1-6
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description -n python2-%{name}
This package contains Python 2 bindings for xrootd.
%endif

%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 7
%package -n python%{python3_pkgversion}-%{name}
Summary:	Python 3 bindings for xrootd
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
This package contains Python 3 bindings for xrootd.
%endif

%if %{?rhel}%{!?rhel:0} == 7
%package -n python%{python3_other_pkgversion}-%{name}
Summary:	Python 3 bindings for xrootd
%{?python_provide:%python_provide python%{?python3_other_pkgversion}-%{name}}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description -n python%{python3_other_pkgversion}-%{name}
This package contains Python 3 bindings for xrootd.
%endif

%package doc
Summary:	Developer documentation for the xrootd libraries
BuildArch:	noarch

%description doc
This package contains the API documentation of the xrootd libraries.

%prep
%setup -q

%build
mkdir build

pushd build
%cmake -DUSE_LIBC_SEMAPHORE:BOOL=%{use_libc_semaphore} \
%if %{py2}
    -DPYTHON_EXECUTABLE=%{__python2} ..
%else
    -DPYTHON_EXECUTABLE=%{__python3} ..
%endif
make %{?_smp_mflags}
popd

%if %{py2}
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 7
pushd build/bindings/python
%py3_build
%if %{?rhel}%{!?rhel:0} == 7
%py3_other_build
%endif
popd
%endif
%endif

pushd packaging/common
make -f /usr/share/selinux/devel/Makefile
popd

doxygen Doxyfile

%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 8
export PYTHONPATH=$(cd build/bindings/python/build/lib.*-%{python3_version} ; pwd)
%else
export PYTHONPATH=$(cd build/bindings/python/build/lib.*-%{python2_version} ; pwd)
%endif
export LD_LIBRARY_PATH=${PWD}/build/src/XrdCl:${PWD}/build/src
pushd bindings/python/docs
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 8
make html SPHINXBUILD=sphinx-build-3
%endif
%if %{?rhel}%{!?rhel:0} == 7
make html
%endif
%if %{?rhel}%{!?rhel:0} == 6
make html SPHINXBUILD=sphinx-1.0-build
%endif
popd

%install
pushd build
make install DESTDIR=%{buildroot}
popd

# Workaround for EPEL 6
[ -h %{buildroot}%{_libdir}/libXrdSecgsiVOMS-4.so ] || \
    ln -s libXrdVoms-4.so %{buildroot}%{_libdir}/libXrdSecgsiVOMS-4.so

%if %{py2}
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 7
pushd build/bindings/python
%py3_install
%if %{?rhel}%{!?rhel:0} == 7
%py3_other_install
%endif
popd
%endif
%endif

# Service start-up scripts / unit files
%if %{use_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 packaging/common/xrootd@.service %{buildroot}%{_unitdir}
install -m 644 packaging/common/xrootd@.socket %{buildroot}%{_unitdir}
install -m 644 packaging/common/xrdhttp@.socket %{buildroot}%{_unitdir}
install -m 644 packaging/common/cmsd@.service %{buildroot}%{_unitdir}
install -m 644 packaging/common/frm_xfrd@.service %{buildroot}%{_unitdir}
install -m 644 packaging/common/frm_purged@.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 packaging/rhel/xrootd.tmpfiles %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
mkdir -p %{buildroot}%{_initddir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p packaging/rhel/xrootd.init %{buildroot}%{_initddir}/xrootd
install -p packaging/rhel/cmsd.init %{buildroot}%{_initddir}/cmsd
install -p packaging/rhel/frm_purged.init %{buildroot}%{_initddir}/frm_purged
install -p packaging/rhel/frm_xfrd.init %{buildroot}%{_initddir}/frm_xfrd
sed s/%{name}.functions/%{name}-functions/ -i %{buildroot}%{_initddir}/*
install -m 644 -p packaging/rhel/%{name}.functions \
    %{buildroot}%{_initddir}/%{name}-functions
install -m 644 -p packaging/rhel/%{name}.sysconfig \
    %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%endif

# Server config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 644 -p packaging/common/%{name}-clustered.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-clustered.cfg
install -m 644 -p packaging/common/%{name}-standalone.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-standalone.cfg
install -m 644 -p packaging/common/%{name}-filecache-clustered.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-filecache-clustered.cfg
install -m 644 -p packaging/common/%{name}-filecache-standalone.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-filecache-standalone.cfg
%if %{use_systemd}
install -m 644 -p packaging/common/%{name}-http.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-http.cfg
%endif

# Client config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d
install -m 644 -p packaging/common/client.conf \
    %{buildroot}%{_sysconfdir}/%{name}/client.conf
install -m 644 -p packaging/common/client-plugin.conf.example \
    %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d

chmod 644 %{buildroot}%{_datadir}/%{name}/utils/XrdCmsNotify.pm

sed 's!/usr/bin/env perl!/usr/bin/perl!' -i \
    %{buildroot}%{_datadir}/%{name}/utils/netchk \
    %{buildroot}%{_datadir}/%{name}/utils/XrdCmsNotify.pm \
    %{buildroot}%{_datadir}/%{name}/utils/XrdOlbMonPerf

sed 's!/usr/bin/env bash!/bin/bash!' -i %{buildroot}%{_bindir}/xrootd-config

mkdir -p %{buildroot}%{_sysconfdir}/%{name}/config.d

mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}

mkdir %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 -p packaging/common/%{name}.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{name}
install -m 644 -p packaging/common/%{name}.pp \
    %{buildroot}%{_datadir}/selinux/packages/%{name}

# Documentation
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr doxydoc/html %{buildroot}%{_pkgdocdir}

cp -pr bindings/python/docs/build/html %{buildroot}%{_pkgdocdir}/python
rm %{buildroot}%{_pkgdocdir}/python/.buildinfo

%ldconfig_scriptlets libs

%ldconfig_scriptlets client-libs

%ldconfig_scriptlets server-libs

%pre server
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -s /sbin/nologin \
  -d %{_localstatedir}/spool/%{name} -c "XRootD runtime user" %{name}

# Remove obsolete service
/sbin/service olbd stop >/dev/null 2>&1 || :
/sbin/chkconfig --del olbd >/dev/null 2>&1 || :

%if %{use_systemd}
# Remove old init config when systemd is used
/sbin/service xrootd stop >/dev/null 2>&1 || :
/sbin/service cmsd stop >/dev/null 2>&1 || :
/sbin/service frm_purged stop >/dev/null 2>&1 || :
/sbin/service frm_xfrd stop >/dev/null 2>&1 || :
/sbin/chkconfig --del xrootd >/dev/null 2>&1 || :
/sbin/chkconfig --del cmsd >/dev/null 2>&1 || :
/sbin/chkconfig --del frm_purged >/dev/null 2>&1 || :
/sbin/chkconfig --del frm_xfrd >/dev/null 2>&1 || :
%endif

%if %{use_systemd}

%post server
if [ $1 -eq 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun server
if [ $1 -eq 0 ] ; then
    for DAEMON in xrootd cmsd frm_purged frm xfrd; do
	for INSTANCE in `systemctl | grep $DAEMON@ | awk '{print $1;}'`; do
	    systemctl --no-reload disable $INSTANCE > /dev/null 2>&1 || :
	    systemctl stop $INSTANCE > /dev/null 2>&1 || :
	done
    done
fi

%postun server
if [ $1 -ge 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
    for DAEMON in xrootd cmsd frm_purged frm xfrd; do
	for INSTANCE in `systemctl | grep $DAEMON@ | awk '{print $1;}'`; do
	    systemctl try-restart $INSTANCE >/dev/null 2>&1 || :
	done
    done
fi

%else

%post server
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add xrootd
    /sbin/chkconfig --add cmsd
    /sbin/chkconfig --add frm_purged
    /sbin/chkconfig --add frm_xfrd
fi

%preun server
if [ $1 -eq 0 ]; then
    /sbin/service xrootd stop >/dev/null 2>&1 || :
    /sbin/service cmsd stop >/dev/null 2>&1 || :
    /sbin/service frm_purged stop >/dev/null 2>&1 || :
    /sbin/service frm_xfrd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del xrootd
    /sbin/chkconfig --del cmsd
    /sbin/chkconfig --del frm_purged
    /sbin/chkconfig --del frm_xfrd
fi

%postun server
if [ $1 -ge 1 ]; then
    /sbin/service xrootd condrestart >/dev/null 2>&1 || :
    /sbin/service cmsd condrestart >/dev/null 2>&1 || :
    /sbin/service frm_purged condrestart >/dev/null 2>&1 || :
    /sbin/service frm_xfrd condrestart >/dev/null 2>&1 || :
fi

%endif

%post selinux
/usr/sbin/semodule -i %{_datadir}/selinux/packages/%{name}/%{name}.pp >/dev/null 2>&1 || :

%postun selinux
if [ $1 -eq 0 ] ; then
    /usr/sbin/semodule -r %{name} >/dev/null 2>&1 || :
fi

%files
# Empty

%files server
%{_bindir}/cconfig
%{_bindir}/cmsd
%{_bindir}/frm_admin
%{_bindir}/frm_purged
%{_bindir}/frm_xfragent
%{_bindir}/frm_xfrd
%{_bindir}/mpxstats
%{_bindir}/wait41
%{_bindir}/xrdacctest
%{_bindir}/xrdpfc_print
%{_bindir}/xrdpwdadmin
%{_bindir}/xrdsssadmin
%{_bindir}/xrootd
%{_mandir}/man8/cmsd.8*
%{_mandir}/man8/frm_admin.8*
%{_mandir}/man8/frm_purged.8*
%{_mandir}/man8/frm_xfragent.8*
%{_mandir}/man8/frm_xfrd.8*
%{_mandir}/man8/mpxstats.8*
%{_mandir}/man8/xrdpfc_print.8*
%{_mandir}/man8/xrdpwdadmin.8*
%{_mandir}/man8/xrdsssadmin.8*
%{_mandir}/man8/xrootd.8*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/utils
%if %{use_systemd}
%{_unitdir}/*
%{_tmpfilesdir}/%{name}.conf
%else
%{_initddir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/%{name}/config.d
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%attr(-,xrootd,xrootd) %{_localstatedir}/log/%{name}
%attr(-,xrootd,xrootd) %{_localstatedir}/spool/%{name}

%files selinux
%{_datadir}/selinux/packages/%{name}/%{name}.pp

%files libs
%{_libdir}/libXrdAppUtils.so.*
%{_libdir}/libXrdCrypto.so.*
%{_libdir}/libXrdCryptoLite.so.*
%{_libdir}/libXrdUtils.so.*
%{_libdir}/libXrdXml.so.*
# Plugins
%{_libdir}/libXrdCksCalczcrc32-4.so
%{_libdir}/libXrdCryptossl-4.so
%{_libdir}/libXrdSec-4.so
%{_libdir}/libXrdSecProt-4.so
%{_libdir}/libXrdSecgsi-4.so
%{_libdir}/libXrdSecgsiAUTHZVO-4.so
%{_libdir}/libXrdSecgsiGMAPDN-4.so
%{_libdir}/libXrdSeckrb5-4.so
%{_libdir}/libXrdSecpwd-4.so
%{_libdir}/libXrdSecsss-4.so
%{_libdir}/libXrdSecunix-4.so
%license COPYING* LICENSE

%files devel
%{_bindir}/xrootd-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/XProtocol
%{_includedir}/%{name}/Xrd
%{_includedir}/%{name}/XrdCks
%{_includedir}/%{name}/XrdNet
%{_includedir}/%{name}/XrdOuc
%{_includedir}/%{name}/XrdSec
%{_includedir}/%{name}/XrdSys
%{_includedir}/%{name}/XrdXml
%{_includedir}/%{name}/XrdVersion.hh
%{_libdir}/libXrdAppUtils.so
%{_libdir}/libXrdCrypto.so
%{_libdir}/libXrdCryptoLite.so
%{_libdir}/libXrdUtils.so
%{_libdir}/libXrdXml.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/cmake

%files client-libs
%{_libdir}/libXrdCl.so.*
%{_libdir}/libXrdClient.so.*
%{_libdir}/libXrdFfs.so.*
%{_libdir}/libXrdPosix.so.*
%{_libdir}/libXrdPosixPreload.so.*
# This lib may be used for LD_PRELOAD so the .so link needs to be included
%{_libdir}/libXrdPosixPreload.so
%{_libdir}/libXrdSsiLib.so.*
%{_libdir}/libXrdSsiShMap.so.*
# Plugins
%{_libdir}/libXrdClProxyPlugin-4.so
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/client.conf
%dir %{_sysconfdir}/%{name}/client.plugins.d
%config(noreplace) %{_sysconfdir}/%{name}/client.plugins.d/client-plugin.conf.example

%files client-devel
%{_includedir}/%{name}/XrdCl
%{_includedir}/%{name}/XrdClient
%{_includedir}/%{name}/XrdPosix
%{_libdir}/libXrdCl.so
%{_libdir}/libXrdClient.so
%{_libdir}/libXrdFfs.so
%{_libdir}/libXrdPosix.so

%files server-libs
%{_libdir}/libXrdHttpUtils.so.*
%{_libdir}/libXrdServer.so.*
# Plugins
%{_libdir}/libXrdBlacklistDecision-4.so
%{_libdir}/libXrdBwm-4.so
%{_libdir}/libXrdCmsRedirectLocal-4.so
%{_libdir}/libXrdFileCache-4.so
%{_libdir}/libXrdHttp-4.so
%{_libdir}/libXrdHttpTPC-4.so
%if %{macaroons}
%{_libdir}/libXrdMacaroons-4.so
%endif
%{_libdir}/libXrdN2No2p-4.so
%{_libdir}/libXrdOssSIgpfsT-4.so
%{_libdir}/libXrdPss-4.so
%{_libdir}/libXrdSsi-4.so
%{_libdir}/libXrdSsiLog-4.so
%{_libdir}/libXrdThrottle-4.so
%{_libdir}/libXrdXrootd-4.so

%files server-devel
%{_includedir}/%{name}/XrdAcc
%{_includedir}/%{name}/XrdCms
%{_includedir}/%{name}/XrdFileCache
%{_includedir}/%{name}/XrdHttp
%{_includedir}/%{name}/XrdOfs
%{_includedir}/%{name}/XrdOss
%{_includedir}/%{name}/XrdSfs
%{_includedir}/%{name}/XrdXrootd
%{_libdir}/libXrdHttpUtils.so
%{_libdir}/libXrdServer.so

%files private-devel
%{_includedir}/%{name}/private
%{_libdir}/libXrdSsiLib.so
%{_libdir}/libXrdSsiShMap.so

%files client
%{_bindir}/xprep
%{_bindir}/xrd
%{_bindir}/xrdadler32
%{_bindir}/xrdcopy
%{_bindir}/xrdcp
%{_bindir}/xrdcp-old
%{_bindir}/xrdfs
%{_bindir}/xrdgsiproxy
%{_bindir}/xrdgsitest
%{_bindir}/xrdmapc
%{_bindir}/xrdstagetool
%{_mandir}/man1/xprep.1*
%{_mandir}/man1/xrd.1*
%{_mandir}/man1/xrdadler32.1*
%{_mandir}/man1/xrdcopy.1*
%{_mandir}/man1/xrdcp.1*
%{_mandir}/man1/xrdcp-old.1*
%{_mandir}/man1/xrdfs.1*
%{_mandir}/man1/xrdgsiproxy.1*
%{_mandir}/man1/xrdgsitest.1*
%{_mandir}/man1/xrdmapc.1*
%{_mandir}/man1/xrdstagetool.1*

%files fuse
%{_bindir}/xrootdfs
%{_mandir}/man1/xrootdfs.1*

%files voms
%{_libdir}/libXrdVoms-4.so
%{_libdir}/libXrdSecgsiVOMS-4.so
%doc %{_mandir}/man1/libXrdVoms.1*
%doc %{_mandir}/man1/libXrdSecgsiVOMS.1*

%if %{py2}
%files -n python2-%{name}
%{python2_sitearch}/xrootd-*.egg-info
%{python2_sitearch}/pyxrootd
%{python2_sitearch}/XRootD
%endif

%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 7
%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/xrootd-*.egg-info
%{python3_sitearch}/pyxrootd
%{python3_sitearch}/XRootD
%endif

%if %{?rhel}%{!?rhel:0} == 7
%files -n python%{python3_other_pkgversion}-%{name}
%{python3_other_sitearch}/xrootd-*.egg-info
%{python3_other_sitearch}/pyxrootd
%{python3_other_sitearch}/XRootD
%endif

%files doc
%doc %{_pkgdocdir}

%changelog
* Thu Jun 11 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.2-3
- Provide/Obsolete xrootd-voms-plugin and vomsxrd

* Tue Jun 09 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.2-2
- Remove libXrdSecgsiVOMS-4.so symlink from xrootd-libs

* Fri Jun 05 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.2-1
- Update to version 4.12.2
- Add voms attribute extractor plugin package
- Drop patches (accepted upstream)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:4.12.1-2
- Rebuilt for Python 3.9

* Thu May 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.1-1
- Update to version 4.12.1
- Fix broken man page

* Fri May 08 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.12.0-1
- Update to version 4.12.0
- Fix empty xrdmapc manpage

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1:4.11.3-2
- Rebuild (json-c)

* Sat Mar 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.3-1
- Update to version 4.11.3
- Use libc semaphores for EPEL 7 build
  POSIX compliant semaphores were backported to glibc in RHEL 7.2
- Drop glibc version requirement for semaphores (backported to older version)
- Move libXrdSsi{Lib,ShMap}.so.* to client-libs package (from server-libs)

* Wed Feb 05 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.2-1
- Update to version 4.11.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.1-1
- Update to version 4.11.1

* Fri Oct 18 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.11.0-1
- Update to version 4.11.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:4.10.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Oct 02 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.10.1-1
- Update to version 4.10.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:4.10.0-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.10.0-1
- Update to version 4.10.0
- Drop the xrootd-ceph package (now in a separate source RPM)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.9.1-1
- Update to version 4.9.1
- Drop patch xrootd-fix-compilation-errors.patch (accepted upstream)

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 1:4.9.0-2
- Rebuilt to change main python from 3.4 to 3.6

* Fri Feb 22 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.9.0-1
- Update to version 4.9.0
- Drop patches previously backported

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:4.8.5-7
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.5-5
- Fix Fedora Rawhide build (gcc 9)

* Thu Jan 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.5-4
- Drop ceph support for 32 bit arches in Fedore 30+

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1:4.8.5-3
- Rebuilt for libcrypt.so.2 (#1666033)

* Wed Nov 14 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.5-2
- XrdCl: Handle properly server disconnect

* Sat Nov 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.5-1
- Update to version 4.8.5
- Drop Python 2 bindings for Fedora 30+
- New subpackage for EPEL7: python36-xrootd

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.4-1
- Update to version 4.8.4

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:4.8.3-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.3-1
- Update to version 4.8.3
- Drop patch xrootd-fix-compiling-errors.patch (accepted upstream)

* Thu Apr 12 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.2-2
- Add missing ? in systemd_requires macro

* Thu Apr 12 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.2-1
- Update to version 4.8.2
- Drop patch xrootd-missing-header.patch (accepted upstream)

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:4.8.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.1-1
- Update to version 4.8.1

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1:4.8.0-2
- Rebuilt for switch to libxcrypt

* Fri Dec 15 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.8.0-1
- Update to version 4.8.0
- New subpackage for EPEL7: python34-xrootd

* Thu Nov 02 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.7.1-1
- Update to version 4.7.1
- Drop patch xrootd-signed-char.patch (accepted upstream)
- Drop patch xrootd-dcache-compat.patch (previously backported)

* Wed Oct 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.7.0-3
- Add two library symlinks to xrootd-private-devel

* Mon Oct 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.7.0-2
- Compatibility with older dcache servers

* Mon Aug 28 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.7.0-1
- Update to version 4.7.0
- Drop patch xrootd-ceph12.patch - accepted upstream
- Add python3 sub-package (Python 3 is supported in this release according
  to the release notes)
- Fix comparison always false error

* Thu Aug 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.1-6
- Rename python sub-package

* Sat Aug 05 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.1-5
- Adapt to ceph version 12

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed May 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.1-1
- Update to version 4.6.1
- Drop patches (accepted upstream or previously backported)
- EPEL 5 end-of-life specfile clean-up

* Fri Mar 31 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-9
- Rebuild for rpm build-id ownership bug (Fedora 27) (rhbz #1432372)

* Mon Mar 13 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-8
- Absent CRL should not trigger authentication error

* Fri Mar 03 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-7
- Make sure the effective CA is always defined

* Thu Mar 02 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-6
- Ignore parameter of discarded old configuration directive

* Wed Mar 01 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-5
- Fix backward compatibilities in XrdSecXtractor interface
- Allow old configuration directives for file cache
- Use upstream's fixes when different from previous patches
- Backport fixes to CRL handling

* Fri Feb 17 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-4
- A valid legacy proxy should not trigger an error msg

* Wed Feb 15 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-3
- Fix for CA chain verification segfault
- Absent CRL should not trigger authentication error

* Fri Feb 10 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-2
- Fix for CRL verification bug

* Wed Feb 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.6.0-1
- Update to version 4.6.0
- Drop patch xrootd-gcc7.patch

* Mon Feb 06 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.5.0-3
- Address compiler errors from GCC 7 (backported from git)

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:4.5.0-2
- Rebuild for readline 7.x

* Thu Nov 17 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.5.0-1
- Update to version 4.5.0
- Adapt to OpenSSL 1.1.0

* Wed Oct 05 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.4.1-1
- Update to version 4.4.1

* Fri Jul 29 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1:4.4.0-1
- Update to version 4.4.0
- Drop patch xrootd-deprecated.patch

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.3.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 21 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.3.0-3
- Backport upstream's fix for the deprecation of readdir_r

* Sat Feb 27 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.3.0-2
- Workaround deprecation of readdir_r in glibc 2.24

* Fri Feb 26 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.3.0-1
- Update to version 4.3.0
- Drop patches accected upstream or that were previously backported:
  xrootd-selinux.patch, xrootd-pth-cancel.patch, xrootd-link.patch,
  xrootd-c++11.patch, xrootd-doxygen.patch, xrootd-autoptr.patch,
  xrootd-indent.patch, xrootd-throw-dtor.patch and xrootd-sockaddr.patch

* Wed Feb 17 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-6
- Fix strict aliasing issues with struct sockaddr

* Fri Feb 12 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-5
- Use upstream's patch for the pthread segfault
- Backport fixes for gcc 6 from upstream

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-3
- Fix for c++11 usage in ceph (backport from upstream git)
- Doxygen fixes

* Wed Dec 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-2
- Fix segfault due to pthread clean-up functions

* Tue Sep 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.3-1
- Update to version 4.2.3

* Fri Jul 31 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.2-1
- Update to version 4.2.2
- Drop patch xrootd-narrowing.patch (accepted upstream)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.1-2
- Fix narrowing conversion error on ppc64 (EPEL 7)

* Tue Jun 02 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.2.1-1
- Update to version 4.2.1
- New subpackages ceph (F22+) and python

* Fri Apr 17 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.1.1-2
- Rebuilt for gcc C++ ABI change

* Mon Dec 08 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.1.1-1
- Update to version 4.1.1
- Drop patch xrootd-signed-char.patch (accepted upstream)

* Fri Nov 28 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.1.0-1
- Update to version 4.1.0
- Install systemd unit files (F21+, EPEL7+)

* Sat Nov 01 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.0.4-1
- Update to version 4.0.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.0.3-1
- Update to version 4.0.3

* Fri Jul 11 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.0.1-1
- Update to version 4.0.1
- Split main package into server and selinux
- New main package installs server and selinux
- Drop patches accepted upstream (-32bit, -range, -narrowing)

* Sun Jun 29 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:4.0.0-1
- Update to version 4.0.0
- Remove the perl package - no longer part of upstream sources

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.6-1
- Update to version 3.3.6

* Tue Dec 03 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.5-1
- Update to version 3.3.5

* Tue Nov 19 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.4-1
- Update to version 3.3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.3-1
- Update to version 3.3.3
- Change License tag to LGPLv3+ due to upstream license change

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1:3.3.2-2
- Perl 5.18 rebuild

* Sun Apr 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.2-1
- Update to version 3.3.2

* Wed Mar 06 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.3.1-1
- Update to version 3.3.1
- Remove the java package - no longer part of upstream sources
- Drop patches fixed upstream: xrootd-cryptoload.patch, xrootd-init.patch and
  xrootd-perl.patch
- Drop obsolete patch: xrootd-java.patch
- Add private-devel package for deprecated header files

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.2.7-1
- Update to version 3.2.7
- Split libs package into libs, client-libs and server-libs
- Split devel package into devel, client-devel and server-devel

* Fri Oct 12 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.2.5-1
- Update to version 3.2.5

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.2.2-1
- Update to version 3.2.2

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1:3.2.1-2
- Perl 5.16 rebuild

* Thu May 17 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.2.1-1
- Update to version 3.2.1

* Sat Mar 17 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.1.1-1
- Update to version 3.1.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.5-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.5-1
- Update to version 3.0.5

* Mon Jul 18 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.4-2.1
- Rebuild for new gridsite (EPEL 5 only)

* Tue Jun 28 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.4-2
- Add missing BuildRequires ncurses-devel

* Tue Jun 28 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.4-1.1
- Remove xrootdfs man page on EPEL 4

* Mon Jun 27 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.4-1
- Update to version 3.0.4
- Drop patches fixed upstream: xrootd-man.patch, xrootd-rhel5-no-atomic.patch
- Drop the remaining man-pages copied from root - now provided by upstream

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:3.0.3-3
- Perl mass rebuild

* Mon May 02 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.3-2
- Proper fix for the atomic detection on ppc - no bug in gcc after all

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.3-1.1
- Workaround for broken gcc on RHEL5 ppc (rhbz #699149)

* Fri Apr 22 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.3-1
- Update to version 3.0.3
- Use upstream's manpages where available (new in this release)
- Use upstream's start-up scripts (new in this release)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.2-1
- Update to version 3.0.2
- Patch XrdCms makefile to make the Xmi interface public

* Fri Dec 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.0-2
- Rebuilt for updated gridsite package

* Mon Dec 13 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1:3.0.0-1
- Update to version 3.0.0
- New subpackage - xrootd-fuse
- New version scheme inroduced by upstream - add epoch

* Wed Sep 01 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-5
- Disable threads in doxygen - causes memory corruption on ppc

* Wed Sep 01 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-4
- Add startup scripts for cmsd service that replaces the deprecated
  olbd service

* Fri Jul 09 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-3
- Fix broken jar

* Mon Jun 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-2
- Add LGPLv2+ to License tag due to man pages
- Better package description

* Wed Jun 09 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 20100315-1
- Initial packaging
