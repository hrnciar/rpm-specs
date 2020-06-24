
%global pkgname   dirsrv
%global srcname   389-ds-base

# Exclude i686 bit arches
ExcludeArch: i686 

# for a pre-release, define the prerel field e.g. .a1 .rc2 - comment out for official release
# also remove the space between % and global - this space is needed because
# fedpkg verrel stupidly ignores comment lines
#% global prerel .rc3
# also need the relprefix field for a pre-release e.g. .0 - also comment out for official release
#% global relprefix 0.

# If perl-Socket-2.000 or newer is available, set 0 to use_Socket6.
%global use_Socket6 0

%global use_asan 0
%global use_rust 0
%global use_legacy 1
%global bundle_jemalloc 1
%if %{use_asan}
%global bundle_jemalloc 0
%endif

%if %{bundle_jemalloc}
%global jemalloc_name jemalloc
%global jemalloc_ver 5.2.1
%global __provides_exclude ^libjemalloc\\.so.*$
%endif

# Use Clang instead of GCC
%global use_clang 0

# fedora 15 and later uses tmpfiles.d
# otherwise, comment this out
%{!?with_tmpfiles_d: %global with_tmpfiles_d %{_sysconfdir}/tmpfiles.d}

# systemd support
%global groupname %{pkgname}.target

# set PIE flag
%global _hardened_build 1

Summary:          389 Directory Server (base)
Name:             389-ds-base
Version:          1.4.4.3
Release:          %{?relprefix}1%{?prerel}%{?dist}.1
License:          GPLv3+
URL:              https://www.port389.org
Conflicts:        selinux-policy-base < 3.9.8
Conflicts:        freeipa-server < 4.0.3
Obsoletes:        %{name} <= 1.4.0.9
Provides:         ldif2ldbm >= 0

BuildRequires:    nspr-devel
BuildRequires:    nss-devel >= 3.34
BuildRequires:    openldap-devel
BuildRequires:    libdb-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    icu
BuildRequires:    libicu-devel
BuildRequires:    pcre-devel
BuildRequires:    cracklib-devel
%if %{use_clang}
BuildRequires:    libatomic
BuildRequires:    clang
%else
BuildRequires:    gcc
BuildRequires:    gcc-c++
%endif
# The following are needed to build the snmp ldap-agent
BuildRequires:    net-snmp-devel
BuildRequires:    lm_sensors-devel
BuildRequires:    bzip2-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
# the following is for the pam passthru auth plug-in
BuildRequires:    pam-devel
BuildRequires:    systemd-units
BuildRequires:    systemd-devel
%if %{use_asan}
BuildRequires:    libasan
%endif
# If rust is enabled
%if %{use_rust}
BuildRequires: cargo
BuildRequires: rust
%endif
BuildRequires:    pkgconfig
BuildRequires:    pkgconfig(systemd)
BuildRequires:    pkgconfig(krb5)

# Needed to support regeneration of the autotool artifacts.
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
# For our documentation
BuildRequires:    doxygen
# For tests!
BuildRequires:    libcmocka-devel
BuildRequires:    libevent-devel
# For lib389 and related components
BuildRequires:    python%{python3_pkgversion}-devel
BuildRequires:    python%{python3_pkgversion}-setuptools
BuildRequires:    python%{python3_pkgversion}-ldap
BuildRequires:    python%{python3_pkgversion}-six
BuildRequires:    python%{python3_pkgversion}-pyasn1
BuildRequires:    python%{python3_pkgversion}-pyasn1-modules
BuildRequires:    python%{python3_pkgversion}-dateutil
BuildRequires:    python%{python3_pkgversion}-argcomplete
BuildRequires:    python%{python3_pkgversion}-argparse-manpage
BuildRequires:    python%{python3_pkgversion}-libselinux
BuildRequires:    python%{python3_pkgversion}-policycoreutils

# For cockpit
BuildRequires:    rsync
BuildRequires:    npm
BuildRequires:    nodejs

Requires:         %{name}-libs = %{version}-%{release}
Requires:         python%{python3_pkgversion}-lib389 = %{version}-%{release}

# this is needed for using semanage from our setup scripts
Requires:         policycoreutils-python-utils
Requires:         /usr/sbin/semanage
Requires:         libsemanage-python%{python3_pkgversion}

Requires:         selinux-policy >= 3.14.1-29

# the following are needed for some of our scripts
Requires:         openldap-clients
Requires:         /usr/bin/c_rehash
Requires:         python%{python3_pkgversion}-ldap

# this is needed to setup SSL if you are not using the
# administration server package
Requires:         nss-tools
Requires:         nss >= 3.34

# these are not found by the auto-dependency method
# they are required to support the mandatory LDAP SASL mechs
Requires:         cyrus-sasl-gssapi
Requires:         cyrus-sasl-md5
Requires:         cyrus-sasl-plain

# this is needed for verify-db.pl
Requires:         libdb-utils

# Needed for password dictionary checks
Requires:         cracklib-dicts

# Needed by logconv.pl
Requires:         perl-DB_File
Requires:         perl-Archive-Tar

# Picks up our systemd deps.
%{?systemd_requires}

Obsoletes:        %{name} <= 1.3.5.4

Source0:          https://releases.pagure.org/389-ds-base/%{name}-%{version}%{?prerel}.tar.bz2
# 389-ds-git.sh should be used to generate the source tarball from git
Source1:          %{name}-git.sh
Source2:          %{name}-devel.README
%if %{bundle_jemalloc}
Source3:          https://github.com/jemalloc/%{jemalloc_name}/releases/download/%{jemalloc_ver}/%{jemalloc_name}-%{jemalloc_ver}.tar.bz2
%endif

%description
389 Directory Server is an LDAPv3 compliant server.  The base package includes
the LDAP server and command line utilities for server administration.
%if %{use_asan}
WARNING! This build is linked to Address Sanitisation libraries. This probably
isn't what you want. Please contact support immediately.
Please see http://seclists.org/oss-sec/2016/q1/363 for more information.
%endif

%package          libs
Summary:          Core libraries for 389 Directory Server
BuildRequires:    nspr-devel
BuildRequires:    nss-devel >= 3.34
BuildRequires:    openldap-devel
BuildRequires:    libdb-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    libicu-devel
BuildRequires:    pcre-devel
BuildRequires:    libtalloc-devel
BuildRequires:    libevent-devel
BuildRequires:    libtevent-devel
Requires:         krb5-libs
Requires:         libevent
BuildRequires:    systemd-devel
Provides:         svrcore = 4.1.4
Conflicts:        svrcore
Obsoletes:        svrcore <= 4.1.3

%description      libs
Core libraries for the 389 Directory Server base package.  These libraries
are used by the main package and the -devel package.  This allows the -devel
package to be installed with just the -libs package and without the main package.

%if %{use_legacy}
%package          legacy-tools
Summary:          Legacy utilities for 389 Directory Server
Obsoletes:        %{name} <= 1.4.0.9
Requires:         389-ds-base-libs = %{version}-%{release}
# for setup-ds.pl to support ipv6
Requires:         perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%if %{use_Socket6}
Requires:         perl-Socket6
%else
Requires:         perl-Socket
%endif
Requires:         perl-NetAddr-IP
# use_openldap assumes perl-Mozilla-LDAP is built with openldap support
Requires:         perl-Mozilla-LDAP
# for setup-ds.pl
Requires:         bind-utils
%global __provides_exclude_from %{_libdir}/%{pkgname}/perl
%global __requires_exclude perl\\((DSCreate|DSMigration|DSUpdate|DSUtil|Dialog|DialogManager|FileConn|Inf|Migration|Resource|Setup|SetupLog)
%{?perl_default_filter}

%description      legacy-tools
Legacy (and deprecated) utilities for 389 Directory Server. This includes
the old account management and task scripts. These are deprecated in favour of
the dscreate, dsctl, dsconf and dsidm tools.
%endif

%package          devel
Summary:          Development libraries for 389 Directory Server
Requires:         %{name}-libs = %{version}-%{release}
Requires:         pkgconfig
Requires:         nspr-devel
Requires:         nss-devel >= 3.34
Requires:         openldap-devel
Requires:         libtalloc
Requires:         libevent
Requires:         libtevent
Requires:         systemd-libs
Provides:         svrcore-devel = 4.1.4
Conflicts:        svrcore-devel
Obsoletes:        svrcore-devel <= 4.1.3

%description      devel
Development Libraries and headers for the 389 Directory Server base package.

%package          snmp
Summary:          SNMP Agent for 389 Directory Server
Requires:         %{name} = %{version}-%{release}

Obsoletes:        %{name} <= 1.4.0.0

%description      snmp
SNMP Agent for the 389 Directory Server base package.

%package -n python%{python3_pkgversion}-lib389
Summary:  A library for accessing, testing, and configuring the 389 Directory Server
BuildArch:        noarch
Requires: openssl
Requires: iproute
Recommends: bash-completion
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-distro
Requires: python%{python3_pkgversion}-pytest
Requires: python%{python3_pkgversion}-ldap
Requires: python%{python3_pkgversion}-six
Requires: python%{python3_pkgversion}-pyasn1
Requires: python%{python3_pkgversion}-pyasn1-modules
Requires: python%{python3_pkgversion}-dateutil
Requires: python%{python3_pkgversion}-argcomplete
Requires: python%{python3_pkgversion}-libselinux
Requires: python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-lib389}

%description -n python%{python3_pkgversion}-lib389
This module contains tools and libraries for accessing, testing,
 and configuring the 389 Directory Server.

%package -n cockpit-389-ds
Summary:          Cockpit UI Plugin for configuring and administering the 389 Directory Server
BuildArch:        noarch
Requires:         cockpit
Requires:         389-ds-base
Requires:         python%{python3_pkgversion}
Requires:         python%{python3_pkgversion}-lib389

%description -n cockpit-389-ds
A cockpit UI Plugin for configuring and administering the 389 Directory Server

%prep
%setup -q -n %{name}-%{version}%{?prerel}

%if %{bundle_jemalloc}
%setup -q -n %{name}-%{version}%{?prerel} -T -D -b 3
%endif

cp %{SOURCE2} README.devel

%build

OPENLDAP_FLAG="--with-openldap"
%{?with_tmpfiles_d: TMPFILES_FLAG="--with-tmpfiles-d=%{with_tmpfiles_d}"}
# hack hack hack https://bugzilla.redhat.com/show_bug.cgi?id=833529
NSSARGS="--with-nss-lib=%{_libdir} --with-nss-inc=%{_includedir}/nss3"

%if %{use_asan}
ASAN_FLAGS="--enable-asan --enable-debug"
%endif

%if %{use_rust}
RUST_FLAGS="--enable-rust"
%endif

%if %{use_legacy}
LEGACY_FLAGS="--enable-legacy --enable-perl"
%else
LEGACY_FLAGS="--disable-legacy --disable-perl"
%endif

%if %{use_clang}
export CC=clang
export CXX=clang++
CLANG_FLAGS="--enable-clang"
%endif

%if %{bundle_jemalloc}
# Override page size, bz #1545539
# 4K
%ifarch %ix86 %arm x86_64 s390x
%define lg_page --with-lg-page=12
%endif

# 64K
%ifarch ppc64 ppc64le aarch64
%define lg_page --with-lg-page=16
%endif

# Override huge page size on aarch64
# 2M instead of 512M
%ifarch aarch64
%define lg_hugepage --with-lg-hugepage=21
%endif

# Build jemalloc
pushd ../%{jemalloc_name}-%{jemalloc_ver}
%configure \
        --libdir=%{_libdir}/%{pkgname}/lib \
        --bindir=%{_libdir}/%{pkgname}/bin \
        --enable-prof
make %{?_smp_mflags}
popd
%endif

# Enforce strict linking
%define _strict_symbol_defs_build 1

# Rebuild the autotool artifacts now.
autoreconf -fiv

%configure --enable-autobind --with-selinux $TMPFILES_FLAG \
           --with-systemd \
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-systemdsystemconfdir=%{_sysconfdir}/systemd/system \
           --with-systemdgroupname=%{groupname}  \
           --libexecdir=%{_libexecdir}/%{pkgname} \
           $NSSARGS $ASAN_FLAGS $RUST_FLAGS $CLANG_FLAGS $LEGACY_FLAGS \
           --enable-cmocka \
           --enable-perl


# lib389
pushd ./src/lib389
%py3_build
popd
# argparse-manpage dynamic man pages have hardcoded man v1 in header,
# need to change it to v8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}%{?prerel}/src/lib389/man/dsconf.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}%{?prerel}/src/lib389/man/dsctl.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}%{?prerel}/src/lib389/man/dsidm.8
sed -i  "1s/\"1\"/\"8\"/" %{_builddir}/%{name}-%{version}%{?prerel}/src/lib389/man/dscreate.8

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

#make %{?_smp_mflags}
make

%install

mkdir -p %{buildroot}%{_datadir}/gdb/auto-load%{_sbindir}
mkdir -p %{buildroot}%{_datadir}/cockpit
make DESTDIR="$RPM_BUILD_ROOT" install

find %{buildroot}%{_datadir}/cockpit/389-console -type d | sed -e "s@%{buildroot}@@" | sed -e 's/^/\%dir /' > cockpit.list
find %{buildroot}%{_datadir}/cockpit/389-console -type f | sed -e "s@%{buildroot}@@" >> cockpit.list

# Copy in our docs from doxygen.
cp -r %{_builddir}/%{name}-%{version}%{?prerel}/man/man3 $RPM_BUILD_ROOT/%{_mandir}/man3

# lib389
pushd src/lib389
%py3_install
popd

mkdir -p $RPM_BUILD_ROOT/var/log/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lib/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lock/%{pkgname}

# for systemd
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/%{groupname}.wants

#remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete

%if %{use_legacy}
# make sure perl scripts have a proper shebang
sed -i -e 's|#{{PERL-EXEC}}|#!/usr/bin/perl|' $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/script-templates/template-*.pl
%endif

%if %{bundle_jemalloc}
pushd ../%{jemalloc_name}-%{jemalloc_ver}
make DESTDIR="$RPM_BUILD_ROOT" install_lib install_bin
cp -pa COPYING ../%{name}-%{version}%{?prerel}/COPYING.jemalloc
cp -pa README ../%{name}-%{version}%{?prerel}/README.jemalloc
popd
%endif

%check
# This checks the code, if it fails it prints why, then re-raises the fail to shortcircuit the rpm build.
if ! make DESTDIR="$RPM_BUILD_ROOT" check; then cat ./test-suite.log && false; fi

%post
if [ -n "$DEBUGPOSTTRANS" ] ; then
    output=$DEBUGPOSTTRANS
    output2=${DEBUGPOSTTRANS}.upgrade
else
    output=/dev/null
    output2=/dev/null
fi
# reload to pick up any changes to systemd files
/bin/systemctl daemon-reload >$output 2>&1 || :

# https://fedoraproject.org/wiki/Packaging:UsersAndGroups#Soft_static_allocation
# Soft static allocation for UID and GID
USERNAME="dirsrv"
ALLOCATED_UID=389
GROUPNAME="dirsrv"
ALLOCATED_GID=389
HOMEDIR="/usr/share/dirsrv"

getent group $GROUPNAME >/dev/null || /usr/sbin/groupadd -f -g $ALLOCATED_GID -r $GROUPNAME
if ! getent passwd $USERNAME >/dev/null ; then
    if ! getent passwd $ALLOCATED_UID >/dev/null ; then
      /usr/sbin/useradd -r -u $ALLOCATED_UID -g $GROUPNAME -d $HOMEDIR -s /sbin/nologin -c "user for 389-ds-base" $USERNAME
    else
      /usr/sbin/useradd -r -g $GROUPNAME -d $HOMEDIR -s /sbin/nologin -c "user for 389-ds-base" $USERNAME
    fi
fi

# Reload our sysctl before we restart (if we can)
sysctl --system &> $output; true

%preun
if [ $1 -eq 0 ]; then # Final removal
    # remove instance specific service files/links
    rm -rf %{_sysconfdir}/systemd/system/%{groupname}.wants/* > /dev/null 2>&1 || :
fi

%postun
if [ $1 = 0 ]; then # Final removal
    rm -rf /var/run/%{pkgname}
fi

%post snmp
%systemd_post %{pkgname}-snmp.service

%preun snmp
%systemd_preun %{pkgname}-snmp.service %{groupname}

%postun snmp
%systemd_postun_with_restart %{pkgname}-snmp.service

%if %{use_legacy}
%post legacy-tools

# START UPGRADE SCRIPT

if [ -n "$DEBUGPOSTTRANS" ] ; then
    output=$DEBUGPOSTTRANS
    output2=${DEBUGPOSTTRANS}.upgrade
else
    output=/dev/null
    output2=/dev/null
fi

# find all instances
instances="" # instances that require a restart after upgrade
ninst=0 # number of instances found in total

echo looking for instances in %{_sysconfdir}/%{pkgname} > $output 2>&1 || :
instbase="%{_sysconfdir}/%{pkgname}"
for dir in $instbase/slapd-* ; do
    echo dir = $dir >> $output 2>&1 || :
    if [ ! -d "$dir" ] ; then continue ; fi
    case "$dir" in *.removed) continue ;; esac
    basename=`basename $dir`
    inst="%{pkgname}@`echo $basename | sed -e 's/slapd-//g'`"
    echo found instance $inst - getting status  >> $output 2>&1 || :
    if /bin/systemctl -q is-active $inst ; then
       echo instance $inst is running >> $output 2>&1 || :
       instances="$instances $inst"
    else
       echo instance $inst is not running >> $output 2>&1 || :
    fi
    ninst=`expr $ninst + 1`
done
if [ $ninst -eq 0 ] ; then
    echo no instances to upgrade >> $output 2>&1 || :
    exit 0 # have no instances to upgrade - just skip the rest
fi
# shutdown all instances
echo shutting down all instances . . . >> $output 2>&1 || :
for inst in $instances ; do
    echo stopping instance $inst >> $output 2>&1 || :
    /bin/systemctl stop $inst >> $output 2>&1 || :
done
echo remove pid files . . . >> $output 2>&1 || :
/bin/rm -f /var/run/%{pkgname}*.pid /var/run/%{pkgname}*.startpid
# do the upgrade
echo upgrading instances . . . >> $output 2>&1 || :
DEBUGPOSTSETUPOPT=`/usr/bin/echo $DEBUGPOSTSETUP | /usr/bin/sed -e "s/[^d]//g"`
if [ -n "$DEBUGPOSTSETUPOPT" ] ; then
    %{_sbindir}/setup-ds.pl -$DEBUGPOSTSETUPOPT -u -s General.UpdateMode=offline >> $output 2>&1 || :
else
    %{_sbindir}/setup-ds.pl -u -s General.UpdateMode=offline >> $output 2>&1 || :
fi

# restart instances that require it
for inst in $instances ; do
    echo restarting instance $inst >> $output 2>&1 || :
    /bin/systemctl start $inst >> $output 2>&1 || :
done
#END UPGRADE
%endif

exit 0


%files
%if %{bundle_jemalloc}
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.jemalloc
%license COPYING.jemalloc
%else
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl
%endif
%dir %{_sysconfdir}/%{pkgname}
%dir %{_sysconfdir}/%{pkgname}/schema
%config(noreplace)%{_sysconfdir}/%{pkgname}/schema/*.ldif
%dir %{_sysconfdir}/%{pkgname}/config
%dir %{_sysconfdir}/systemd/system/%{groupname}.wants
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/slapd-collations.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/certmap.conf
%{_datadir}/%{pkgname}
%{_datadir}/gdb/auto-load/*
%{_unitdir}
%{_bindir}/dbscan
%{_mandir}/man1/dbscan.1.gz
%{_bindir}/ds-replcheck
%{_mandir}/man1/ds-replcheck.1.gz
%{_bindir}/ds-logpipe.py
%{_mandir}/man1/ds-logpipe.py.1.gz
%{_bindir}/ldclt
%{_mandir}/man1/ldclt.1.gz
%{_bindir}/logconv.pl
%{_mandir}/man1/logconv.pl.1.gz
%{_bindir}/pwdhash
%{_mandir}/man1/pwdhash.1.gz
%{_bindir}/readnsstate
%{_mandir}/man1/readnsstate.1.gz
#%caps(CAP_NET_BIND_SERVICE=pe) {_sbindir}/ns-slapd
%{_sbindir}/ns-slapd
%{_mandir}/man8/ns-slapd.8.gz
%{_libexecdir}/%{pkgname}/ds_systemd_ask_password_acl
%{_mandir}/man5/99user.ldif.5.gz
%{_mandir}/man5/certmap.conf.5.gz
%{_mandir}/man5/slapd-collations.conf.5.gz
%{_mandir}/man5/dirsrv.5.gz
%{_mandir}/man5/dirsrv.systemd.5.gz
%{_libdir}/%{pkgname}/python
%dir %{_libdir}/%{pkgname}/plugins
%{_libdir}/%{pkgname}/plugins/*.so
# This has to be hardcoded to /lib - $libdir changes between lib/lib64, but
# sysctl.d is always in /lib.
%{_prefix}/lib/sysctl.d/*
%dir %{_localstatedir}/lib/%{pkgname}
%dir %{_localstatedir}/log/%{pkgname}
%ghost %dir %{_localstatedir}/lock/%{pkgname}
%exclude %{_sbindir}/ldap-agent*
%exclude %{_mandir}/man1/ldap-agent.1.gz
%exclude %{_unitdir}/%{pkgname}-snmp.service
%if %{bundle_jemalloc}
%{_libdir}/%{pkgname}/lib/
%{_libdir}/%{pkgname}/bin/
%exclude %{_libdir}/%{pkgname}/bin/jemalloc-config
%exclude %{_libdir}/%{pkgname}/bin/jemalloc.sh
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc.a
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc.so
%exclude %{_libdir}/%{pkgname}/lib/libjemalloc_pic.a
%exclude %{_libdir}/%{pkgname}/lib/pkgconfig
%endif

%files devel
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%{_mandir}/man3/*
%{_includedir}/svrcore.h
%{_includedir}/%{pkgname}
%{_libdir}/libsvrcore.so
%{_libdir}/%{pkgname}/libslapd.so
%{_libdir}/%{pkgname}/libns-dshttpd.so
%{_libdir}/%{pkgname}/libsds.so
%{_libdir}/%{pkgname}/libldaputil.so
%{_libdir}/pkgconfig/svrcore.pc
%{_libdir}/pkgconfig/dirsrv.pc
%{_libdir}/pkgconfig/libsds.pc

%files libs
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%dir %{_libdir}/%{pkgname}
%{_libdir}/libsvrcore.so.*
%{_libdir}/%{pkgname}/libslapd.so.*
%{_libdir}/%{pkgname}/libns-dshttpd-*.so
%{_libdir}/%{pkgname}/libsds.so.*
%{_libdir}/%{pkgname}/libldaputil.so.*
%{_libdir}/%{pkgname}/librewriters.so*
%if %{bundle_jemalloc}
%{_libdir}/%{pkgname}/lib/libjemalloc.so.2
%endif
%if %{use_rust}
%{_libdir}/%{pkgname}/librsds.so
%endif

%if %{use_legacy}
%files legacy-tools
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%{_bindir}/infadd
%{_mandir}/man1/infadd.1.gz
%{_bindir}/ldif
%{_mandir}/man1/ldif.1.gz
%{_bindir}/migratecred
%{_mandir}/man1/migratecred.1.gz
%{_bindir}/mmldif
%{_mandir}/man1/mmldif.1.gz
%{_bindir}/rsearch
%{_mandir}/man1/rsearch.1.gz
%{_libexecdir}/%{pkgname}/ds_selinux_enabled
%{_libexecdir}/%{pkgname}/ds_selinux_port_query
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/template-initconfig
%{_mandir}/man5/template-initconfig.5.gz
%{_datadir}/%{pkgname}/properties/*.res
%{_datadir}/%{pkgname}/script-templates
%{_datadir}/%{pkgname}/updates
%{_sbindir}/ldif2ldap
%{_mandir}/man8/ldif2ldap.8.gz
%{_sbindir}/bak2db
%{_mandir}/man8/bak2db.8.gz
%{_sbindir}/db2bak
%{_mandir}/man8/db2bak.8.gz
%{_sbindir}/db2index
%{_mandir}/man8/db2index.8.gz
%{_sbindir}/db2ldif
%{_mandir}/man8/db2ldif.8.gz
%{_sbindir}/dbverify
%{_mandir}/man8/dbverify.8.gz
%{_sbindir}/ldif2db
%{_mandir}/man8/ldif2db.8.gz
%{_sbindir}/restart-dirsrv
%{_mandir}/man8/restart-dirsrv.8.gz
%{_sbindir}/start-dirsrv
%{_mandir}/man8/start-dirsrv.8.gz
%{_sbindir}/status-dirsrv
%{_mandir}/man8/status-dirsrv.8.gz
%{_sbindir}/stop-dirsrv
%{_mandir}/man8/stop-dirsrv.8.gz
%{_sbindir}/upgradedb
%{_mandir}/man8/upgradedb.8.gz
%{_sbindir}/vlvindex
%{_mandir}/man8/vlvindex.8.gz
%{_sbindir}/monitor
%{_mandir}/man8/monitor.8.gz
%{_sbindir}/dbmon.sh
%{_mandir}/man8/dbmon.sh.8.gz
%{_sbindir}/dn2rdn
%{_mandir}/man8/dn2rdn.8.gz
%{_sbindir}/restoreconfig
%{_mandir}/man8/restoreconfig.8.gz
%{_sbindir}/saveconfig
%{_mandir}/man8/saveconfig.8.gz
%{_sbindir}/suffix2instance
%{_mandir}/man8/suffix2instance.8.gz
%{_sbindir}/upgradednformat
%{_mandir}/man8/upgradednformat.8.gz
%{_mandir}/man1/dbgen.pl.1.gz
%{_bindir}/repl-monitor
%{_mandir}/man1/repl-monitor.1.gz
%{_bindir}/repl-monitor.pl
%{_mandir}/man1/repl-monitor.pl.1.gz
%{_bindir}/cl-dump
%{_mandir}/man1/cl-dump.1.gz
%{_bindir}/cl-dump.pl
%{_mandir}/man1/cl-dump.pl.1.gz
%{_bindir}/dbgen.pl
%{_mandir}/man8/bak2db.pl.8.gz
%{_sbindir}/bak2db.pl
%{_sbindir}/cleanallruv.pl
%{_mandir}/man8/cleanallruv.pl.8.gz
%{_sbindir}/db2bak.pl
%{_mandir}/man8/db2bak.pl.8.gz
%{_sbindir}/db2index.pl
%{_mandir}/man8/db2index.pl.8.gz
%{_sbindir}/db2ldif.pl
%{_mandir}/man8/db2ldif.pl.8.gz
%{_sbindir}/fixup-linkedattrs.pl
%{_mandir}/man8/fixup-linkedattrs.pl.8.gz
%{_sbindir}/fixup-memberof.pl
%{_mandir}/man8/fixup-memberof.pl.8.gz
%{_sbindir}/ldif2db.pl
%{_mandir}/man8/ldif2db.pl.8.gz
%{_sbindir}/migrate-ds.pl
%{_mandir}/man8/migrate-ds.pl.8.gz
%{_sbindir}/ns-accountstatus.pl
%{_mandir}/man8/ns-accountstatus.pl.8.gz
%{_sbindir}/ns-activate.pl
%{_mandir}/man8/ns-activate.pl.8.gz
%{_sbindir}/ns-inactivate.pl
%{_mandir}/man8/ns-inactivate.pl.8.gz
%{_sbindir}/ns-newpwpolicy.pl
%{_mandir}/man8/ns-newpwpolicy.pl.8.gz
%{_sbindir}/remove-ds.pl
%{_mandir}/man8/remove-ds.pl.8.gz
%{_sbindir}/schema-reload.pl
%{_mandir}/man8/schema-reload.pl.8.gz
%{_sbindir}/setup-ds.pl
%{_mandir}/man8/setup-ds.pl.8.gz
%{_sbindir}/syntax-validate.pl
%{_mandir}/man8/syntax-validate.pl.8.gz
%{_sbindir}/usn-tombstone-cleanup.pl
%{_mandir}/man8/usn-tombstone-cleanup.pl.8.gz
%{_sbindir}/verify-db.pl
%{_mandir}/man8/verify-db.pl.8.gz
%{_libdir}/%{pkgname}/perl
%endif

%files snmp
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README.devel
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/ldap-agent.conf
%{_sbindir}/ldap-agent*
%{_mandir}/man1/ldap-agent.1.gz
%{_unitdir}/%{pkgname}-snmp.service

%files -n python%{python3_pkgversion}-lib389
%doc LICENSE LICENSE.GPLv3+
%{python3_sitelib}/lib389*
%{_sbindir}/dsconf
%{_mandir}/man8/dsconf.8.gz
%{_sbindir}/dscreate
%{_mandir}/man8/dscreate.8.gz
%{_sbindir}/dsctl
%{_mandir}/man8/dsctl.8.gz
%{_sbindir}/dsidm
%{_mandir}/man8/dsidm.8.gz
%{_libexecdir}/%{pkgname}/dscontainer

%files -n cockpit-389-ds -f cockpit.list
%{_datarootdir}/metainfo/389-console/org.port389.cockpit_console.metainfo.xml
%doc README.md

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.4.3-1.1
- Perl 5.32 rebuild

* Fri May 29 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.4.3-1
- Bump version to 1.4.4.3
- Issue 50931 - RFE AD filter rewriter for ObjectCategory
- Issue 50860 - Port Password Policy test cases from TET to python3 part1
- Issue 51113 - Allow using uid for replication manager entry
- Issue 51095 - abort operation if CSN can not be generated
- Issue 51110 - Fix ASAN ODR warnings
- Issue 49850 - ldbm_get_nonleaf_ids() painfully slow for databases with many non-leaf entries
- Issue 51102 - RFE - ds-replcheck - make online timeout configurable
- Issue 51076 - remove unnecessary slapi entry dups
- Issue 51086 - Improve dscreate instance name validation
- Issue:51070 - Port Import TET module to python3 part1
- Issue 51037 - compiler warning
- Issue 50989 - ignore pid when it is ourself in protect_db
- Issue 51037 - RFE AD filter rewriter for ObjectSID
- Issue 50499 - Fix some npm audit issues
- Issue 51091 - healthcheck json report fails when mapping tree is deleted
- Issue 51079 - container pid start and stop issues
- Issue 49761 - Fix CI tests
- Issue 50610 - Fix return code when it's nothing to free
- Issue 50610 - memory leaks in dbscan and changelog encryption
- Issue 51076 - prevent unnecessarily duplication of the target entry
- Issue 50940 - Permissions of some shipped directories may change over time
- Issue 50873 - Fix issues with healthcheck tool
- Issue 51082 - abort when a empty valueset is freed
- Issue 50201 - nsIndexIDListScanLimit accepts any value

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.4.2-1.2
- Rebuilt for Python 3.9

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 1.4.4.2-1.1
- Rebuild for ICU 67

* Fri May 8 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.4.2-1
- Bump version to 1.4.4.2
- Issue 51078 - Add nsslapd-enable-upgrade-hash to the schema
- Issue 51054 - Revise ACI target syntax checking
- Issue 51068 - deadlock when updating the schema
- Issue 51042 - try to use both c_rehash and openssl rehash
- Issue 51042 - switch from c_rehash to openssl rehash
- Issue 50992 - Bump jemalloc version and enable profiling
- Issue 51060 - unable to set sslVersionMin to TLS1.0
- Issue 51064 - Unable to install server where IPv6 is disabled
- Issue 51051 - CLI fix consistency issues with confirmations
- Issue 50655 - etime displayed has an order of magnitude 10 times smaller than it should be
- Issue 49731 - undo db_home_dir under /dev/shm/dirsrv for now
- Issue 51054 - AddressSanitizer: heap-buffer-overflow in ldap_utf8prev
- Issue 49761 - Fix CI tests
- Issue 51047 - React deprecating ComponentWillMount
- Issue 50499 - fix npm audit issues
- Issue 50545 - Port dbgen.pl to dsctl
- Issue 51027 - Test passwordHistory is not rewritten on a fail attempt

* Wed Apr 22 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.4.1-1
- Bump version to 1.4.4.1
- Issue 51024 - syncrepl_entry callback does not contain attributes added by postoperation plugins
- Issue 50877 - task to run tests of csn generator
- Issue 49731 - undo db_home_dir under /dev/shm/dirsrv for now
- Issue 48055 - CI test - automember_plugin(part3)
- Issue 51035 - Heavy StartTLS connection load can randomly fail with err=1
- Issue 51031 - UI - transition between two instances needs improvement

* Thu Apr 16 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.4.0-1
- Bump version to 1.4.4.0
- Issue 50933 - 10rfc2307compat.ldif is not ready to be used by default
- Issue 50931 - RFE AD filter rewriter for ObjectCategory
- Issue 51016 - Fix memory leaks in changelog5_init and perfctrs_init
- Issue 50980 - RFE extend usability for slapi_compute_add_search_rewriter and slapi_compute_add_evaluator
- Issue 51008 - dbhome in containers
- Issue 50875 - Refactor passwordUserAttributes's and passwordBadWords's code
- Issue 51014 - slapi_pal.c possible static buffer overflow
- Issue 50545 - remove dbmon "incr" option from arg parser
- Issue 50545 - Port dbmon.sh to dsconf
- Issue 51005 - AttributeUniqueness plugin's DN parameter should not have a default value
- Issue 49731 - Fix additional issues with setting db home directory by default
- Issue 50337 - Replace exec() with setattr()
- Issue 50905 - intermittent SSL hang with rhds
- Issue 50952 - SSCA lacks basicConstraint:CA
- Issue 50640 - Database links: get_monitor() takes 1 positional argument but 2 were given
- Issue 50869 - Setting nsslapd-allowed-sasl-mechanisms truncates the value

* Wed Apr 1 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.3.5-1
- Bump version to 1.4.3.5
- Issue 50994 - Fix latest UI bugs found by QE
- Issue 50933 - rfc2307compat.ldif
- Issue 50337 - Replace exec() with setattr()
- Issue 50984 - Memory leaks in disk monitoring
- Issue 50984 - Memory leaks in disk monitoring
- Issue 49731 - dscreate fails in silent mode because of db_home_dir
- Issue 50975 - Revise UI branding with new minimized build
- Issue 49437 - Fix memory leak with indirect COS
- Issue 49731 - Do not add db_home_dir to template-dse.ldif
- Issue 49731 - set and use db_home_directory by default
- Issue 50971 - fix BSD_SOURCE
- Issue 50744 - -n option of dbverify does not work
- Issue 50952 - SSCA lacks basicConstraint:CA
- Issue 50976 - Clean up Web UI source directory from unused files
- Issue 50955 - Fix memory leaks in chaining plugin(part 2)
- Issue 50966 - UI - Database indexes not using typeAhead correctly
- Issue 50974 - UI - wrong title in "Delete Suffix" popup
- Issue 50972 - Fix cockpit plugin build
- Issue 49761 - Fix CI test suite issues
- Issue 50971 - Support building on FreeBSD.
- Issue 50960 - [RFE] Advance options in RHDS Disk Monitoring Framework
- Issue 50800 - wildcards in rootdn-allow-ip attribute are not accepted
- Issue 50963 - We should bundle *.min.js files of Console
- Issue 50860 - Port Password Policy test cases from TET to python3 Password grace limit section.
- Issue 50860 - Port Password Policy test cases from TET to python3 series of bugs Port final
- Issue 50954 - buildnum.py - fix date formatting issue

* Mon Mar 16 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.3.4-1
- Bump version to 1.4.3.4
- Issue 50954 - Port buildnum.pl to python(part 2)
- Issue 50955 - Fix memory leaks in chaining plugin
- Issue 50954 - Port buildnum.pl to python
- Issue 50947 - change 00core.ldif objectClasses for openldap migration
- Issue 50755 - setting nsslapd-db-home-directory is overriding db_directory
- Issue 50937 - Update CLI for new backend split configuration
- Issue 50860 - Port Password Policy test cases from TET to python3 pwp.sh
- Issue 50945 - givenname alias of gn from openldap
- Issue 50935 - systemd override in lib389 for dscontainer
- Issue 50499 - Fix npm audit issues
- Issue 49761 - Fix CI test suite issues
- Issue 50618 - clean compiler warning and log level
- Issue 50889 - fix compiler issues
- Issue 50884 - Health check tool DSEldif check fails
- Issue 50926 - Remove dual spinner and other UI fixes
- Issue 50928 - Unable to create a suffix with countryName
- Issue 50758 - Only Recommend bash-completion, not Require
- Issue 50923 - Fix a test regression
- Issue 50904 - Connect All React Components And Refactor the Main Navigation Tab Code
- Issue 50920 - cl-dump exit code is 0 even if command fails with invalid arguments
- Issue 50923 - Add test - dsctl fails to remove instances with dashes in the name
- Issue 50919 - Backend delete fails using dsconf
- Issue 50872 - dsconf can't create GSSAPI replication agreements
- Issue 50912 - RFE - add password policy attribute pwdReset
- Issue 50914 - No error returned when adding an entry matching filters for a non existing automember group
- Issue 50889 - Extract pem files into a private namespace
- Issue 50909 - nsDS5ReplicaId cant be set to the old value it had before
- Issue 50686 - Port fractional replication test cases from TET to python3 final
- Issue 49845 - Remove pkgconfig check for libasan
- Issue:50860 - Port Password Policy test cases from TET to python3 bug624080
- Issue:50860 - Port Password Policy test cases from TET to python3 series of bugs
- Issue 50786 - connection table freelist
- Issue 50618 - support cgroupv2
- Issue 50900 - Fix cargo offline build
- Issue 50898 - ldclt core dumped when run with -e genldif option

* Mon Feb 17 2020 Matus Honek <mhonek@redhat.com> - 1.4.3.3-3
- Bring back the necessary c_rehash util (#1803370)

* Fri Feb 14 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.3.3-2
- Bump version to 1.4.3.3-2
- Remove unneeded perl dependencies
- Change bash-completion to "Recommends" instead of "Requires"

* Thu Feb 13 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.3.3-1
- Bump version to 1.4.3.3
- Issue 50855 - remove unused file from UI
- Issue 50855 - UI: Port Server Tab to React
- Issue 49845 - README does not contain complete information on building
- Issue 50686 - Port fractional replication test cases from TET to python3 part 1
- Issue 49623 - cont cenotaph errors on modrdn operations
- Issue 50882 - Fix healthcheck errors for instances that do not have TLS enabled
- Issue 50886 - Typo in the replication debug message
- Issue 50873 - Fix healthcheck and virtual attr check
- Issue 50873 - Fix issues with healthcheck tool
- Issue 50028 - Add a new CI test case
- Issue 49946 - Add a new CI test case
- Issue 50117 - Add a new CI test case
- Issue 50787 - fix implementation of attr unique
- Issue 50859 - support running only with ldaps socket
- Issue 50823 - dsctl doesn't work with 'slapd-' in the instance name
- Issue 49624 - cont - DB Deadlock on modrdn appears to corrupt database and entry cache
- Issue 50867 - Fix minor buildsys issues
- Issue 50737 - Allow building with rust online without vendoring
- Issue 50831 - add cargo.lock to allow offline builds
- Issue 50694 - import PEM certs on startup
- Issue 50857 - Memory leak in ACI using IP subject
- Issue 49761 - Fix CI test suite issues
- Issue 50853 - Fix NULL pointer deref in config setting
- Issue 50850 - Fix dsctl healthcheck for python36
- Issue 49990 - Need to enforce a hard maximum limit for file descriptors
- Issue 48707 - ldapssotoken for authentication

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.3.2-1
- Bump version to 1.4.3.2
- Issue 49254 - Fix compiler failures and warnings
- Issue 50741 - cont bdb_start - Detected Disorderly Shutdown
- Issue 50836 - Port Schema UI tab to React
- Issue 50842 - Decrease 389-console Cockpit component size
- Issue 50790 - Add result text when filter is invalid
- Issue 50627 - Add ASAN logs to HTML report
- Issue 50834 - Incorrectly setting the NSS default SSL version max
- Issue 50829 - Disk monitoring rotated log cleanup causes heap-use-after-free
- Issue 50709 - (cont) Several memory leaks reported by Valgrind for 389-ds 1.3.9.1-10
- Issue 50784 - performance testing scripts
- Issue 50599 - Fix memory leak when removing db region files
- Issue 49395 - Set the default TLS version min to TLS1.2
- Issue 50818 - dsconf pwdpolicy get error
- Issue 50824 - dsctl remove fails with "name 'ensure_str' is not defined"
- Issue 50599 - Remove db region files prior to db recovery
- Issue 50812 - dscontainer executable should be placed under /usr/libexec/dirsrv/
- Issue 50816 - dsconf allows the root password to be set to nothing
- Issue 50798 - incorrect bytes in format string(fix import issue)

* Thu Jan 16 2020 Adam Williamson <awilliam@redhat.com> - 1.4.3.1-3
- Backport two more import/missing function fixes

* Wed Jan 15 2020 Adam Williamson <awilliam@redhat.com> - 1.4.3.1-2
- Backport 828aad0 to fix missing imports from 1.4.3.1

* Mon Jan 13 2020 Mark Reynolds <mreynolds@redhat.com> - 1.4.3.1-1
- Bump version to 1.4.3.1
- Issue 50798 - incorrect bytes in format string
- Issue 50545 - Add the new replication monitor functionality to UI
- Issue 50806 - Fix minor issues in lib389 health checks
- Issue 50690 - Port Password Storage test cases from TET to python3 part 1
- Issue 49761 - Fix CI test suite issues
- Issue 49761 - Fix CI test suite issues
- Issue 50754 - Add Restore Change Log option to CLI
- Issue 48055 - CI test - automember_plugin(part2)
- Issue 50667 - dsctl -l did not respect PREFIX
- Issue 50780 - More CLI fixes
- Issue 50649 - lib389 without defaults.inf
- Issue 50780 - Fix UI issues
- Issue 50727 - correct mistaken options in filter validation patch
- Issue 50779 - lib389 - conflict compare fails for DN's with spaces
- Set branch version to 1.4.3.0

* Mon Dec  9 2019 Matus Honek <mhonek@redhat.com> - 1.4.2.5-3
- Bump version to 1.4.2.5-3
- Fix python-argcomplete tinkering (#1781131)

* Fri Dec 6 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.5-2
- Bump version to 1.4.2.5-2
- Fix specfile typo (bash-completion)

* Fri Dec 6 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.5-1
- Bump version to 1.4.2.5
- Issue 50747 - Port readnsstate to dsctl
- Issue 50758 - Enable CLI arg completion
- Issue 50753 - Dumping the changelog to a file doesn't work
- Issue 50745 - ns-slapd hangs during CleanAllRUV tests
- Issue 50734 - lib389 creates non-SSCA cert DBs with misleading README.txt
- Issue 48851 - investigate and port TET matching rules filter tests(cert)
- Issue 50443 - Create a module in lib389 to Convert a byte sequence to a properly escaped for LDAP
- Issue 50664 - DS can fail to recover if an empty directory exists in db
- Issue 50736 - RetroCL trimming may crash at shutdown if trimming configuration is invalid
- Issue 50741 - bdb_start - Detected Disorderly Shutdown last time Directory Server was running
- Issue 50572 - After running cl-dump dbdir/cldb/*ldif.done are not deleted
- Issue 50701 - Fix type in lint report
- Issue 50729 - add support for gssapi tests on suse
- Issue 50701 - Add additional healthchecks to dsconf
- Issue 50711 - `dsconf security` lacks option for setting nsTLSAllowClientRenegotiation attribute
- Issue 50439 - Update docker integration for Fedora
- Issue 48851 - Investigate and port TET matching rules filter tests(last test cases for match)
- Issue 50499 - Fix npm audit issues
- Issue 50722 - Test IDs are not unique
- Issue 50712 - Version comparison doesn't work correctly on git builds
- Issue 50499 - Fix npm audit issues
- Issue 50706 - Missing lib389 dependency - packaging

* Fri Nov 15 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.4-2
- Bump version to 1.4.2.4-2
- Fix dependancy issue

* Thu Nov 14 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.4-1
- Bump version to 1.4.2.4
- Issue 50634 - Fix CLI error parsing for non-string values
- Issue 50659 - AddressSanitizer: SEGV ... in bdb_pre_close
- Issue 50716 - CVE-2019-14824 (BZ#1748199) - deref plugin displays restricted attributes
- Issue 50644 - fix regression with creating sample entries
- Issue 50699 - Add Disk Monitor to CLI and UI
- Issue 50716 - CVE-2019-14824 (BZ#1748199) - deref plugin displays restricted attributes
- Issue 50536 - After audit log file is rotated, DS version string is logged after each update
- Issue 50712 - Version comparison doesn't work correctly on git builds
- Issue 50706 - Missing lib389 dependency - packaging
- Issue 49761 - Fix CI test suite issues
- Issue 50683 - Makefile.am contains unused RPM-related targets
- Issue 50696 - Fix various UI bugs
- Issue 50641 - Update default aci to allows users to change their own password
- Issue 50007, 50648 - improve x509 handling in dsctl
- Issue 50689 - Failed db restore task does not report an error
- Issue 50199 - Disable perl by default
- Issue 50633 - Add cargo vendor support for offline builds
- Issue 50499 - Fix npm audit issues

* Sun Nov 03 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.3-1
- Bump version to 1.4.2.3
- Issue 50592 - Port Replication Tab to ReactJS
- Issue 50680 - Remove branding from upstream spec file
- Issue 50669 - Remove nunc-stans in favour of reworking current conn code (add.)
- Issue 48055 - CI test - automember_plugin(part1)
- Issue 50677 - Map subtree searches with NULL base to default naming context
- Issue 50669 - Fix RPM build
- Issue 50669 - remove nunc-stans
- Issue 49850 - cont -fix crash in ldbm_non_leaf
- Issue 50634 - Clean up CLI errors output - Fix wrong exception
- Issue 50660 - Build failure on Fedora 31
- Issue 50634 - Clean up CLI errors output
- Issue 48851 - Investigate and port TET matching rules filter tests(match more test cases)
- Issue 50428 - Log the actual base DN when the search fails with "invalid attribute request"
- Issue 49850 -  ldbm_get_nonleaf_ids() slow for databases with many non-leaf entries
- Issue 50655 - access log etime is not properly formatted
- Issue 50653 -  objectclass parsing fails to log error message text
- Issue 50646 - Improve task handling during shutdowns
- Issue 50627 - Support platforms without pytest_html
- Issue 49476 - backend refactoring phase1, fix failing tests
- Issue 49476 - refactor ldbm backend to allow replacement of BDB
- Issue 50349 - additional fix: filter schema check must handle subtypes
- Issue 48851 - investigate and port TET matching rules filter tests(indexing more test cases)
- Issue 50638 - RecursionError: maximum recursion depth exceeded while calling a Python object
- Issue 50636 - Crash during sasl bind
- Issue 50632 - Add ensure attr state so that diffs are easier from 389-ds-portal
- Issue 50619 - extend commands to have more modify options
- Issue 50499 - Fix npm audit issues

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.4.2.2-3.1
- Rebuild for ICU 65

* Fri Sep 27 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.2-3
- Bump version to 1.4.2.2-3
- Address perl provides and requires filter

* Wed Sep 25 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.2-2
- Bump version to 1.4.2.2-2
- Remove perl filter change as it broke legacy tools

* Wed Sep 25 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.2-1
- Bump version to 1.4.2.2
- Issue 50627 - Add ASAN logs to HTML report
- Issue 50545 - Port repl-monitor.pl to lib389 CLI
- Issue 50622 - ds_selinux_enabled may crash on suse
- Issue 50595 - remove syslog.target requirement
- Issue 50617 - disable cargo lock
- Issue 50620 - Fix regressions from 50506 (slapi_enry_attr_get_ref)
- Issue 50615 - Log current test name to journald
- Issue 50610 - memory leak in dbscan

* Wed Sep 25 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.2.1-1
- Bump version to 1.4.2.1
- Issue 50581 - ns-slapd crashes during ldapi search
- Issue 50604 - Fix UI validation
- Issue 50510 - etime can contain invalid nanosecond value
- Issue 50593 - Investigate URP handling on standalone instance
- Issue 50506 - Fix regression for relication stripattrs
- Issue 50580 - Perl can't be disabled in configure
- Issue 50584, 49212 - docker healthcheck and configuration
- Issue 50546 - fix more UI issues(part 2)
- Do not use comparision with "is" for empty value
- Issue 50546 - fix more UI issues
- Issue 50586 - lib389 - Fix DSEldif long line processing
- Issue 50173 - Add the validate-syntax task to the dsconf schema
- Issue 50546 - Fix various issues in UI
- Bump version to 1.4.2.0
- Issue 50576 - Same proc uid/gid maps to rootdn for ldapi sasl
- Issue 50567, 50568 - strict host check disable and display container version
- Issue 50550 - DS installer debug messages leaking to ipa-server-install
- Issue 50545 - Port fixup-memberuid and add the functionality to CLI and UI
- Issue 50572 - After running cl-dump dbdir/cldb/*ldif.done are not deleted
- Issue 50578 - Add SKIP_AUDIT_CI flag for Cockpit builds
- Issue 50349 - filter schema validation
- Issue 48055 - CI test-(Plugin configuration should throw proper error messages if not configured properly)
- Issue 49324 - idl_new fix assert
- Issue 50564 - Fix rust libraries by default and improve docker
- Issue 50206 - Refactor lock, unlock and status of dsidm account/role
- Issue 49324 - idl_new report index name in error conditions
- Issue 49761 - Fix CI test suite issues
- Issue 50506 - Fix regression from slapi_entry_attr_get_ref refactor
- Issue 50499 - Audit fix - Update npm 'eslint-utils' version
- Issue 49624 - modrdn silently fails if DB deadlock occurs
- Issue 50542 - Fix crashes in filter tests
- Issue 49761 - Fix CI test suite issues
- Issue 50542 - Entry cache contention during base search
- Issue 50462 - Fix CI tests
- Issue 50490 - objects and memory leaks
- Issue 50538 - Move CI test to individual file
- Issue 50538 - cleanAllRUV task limit is not enforced for replicated tasks
- Issue 50536 - Audit log heading written to log after every update
- Issue 50525 - nsslapd-defaultnamingcontext does not change when the assigned suffix gets deleted
- Issue 50534 - CLI change schema edit subcommand to replace
- Issue 50506 - cont Fix invalid frees from pointer reference calls
- Issue 50507 - Fix Cockpit UI styling for PF4
- Issue 48851 - investigate and port TET matching rules filter tests(indexing final)
- Issue 48851 - Add more test cases to the match test suite(mode replace)
- Issue 50530 - Directory Server not RFC 4511 compliant with requested attr "1.1"
- Issue 50529 - LDAP server returning PWP controls in different sequence
- Issue 50506 - Fix invalid frees from pointer reference calls.
- Issue 50506 - Replace slapi_entry_attr_get_charptr() with slapi_entry_attr_get_ref()
- Issue 50521 - Add regressions in CI tests
- Issue 50510 - etime can contain invalid nanosecond value
- Issue 50488 - Create a monitor for disk space usagedisk-space-mon
- Issue 50511 - lib389 PosixGroups type can not handle rdn properly
- Issue 50508 - UI - fix local password policy form

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1.6-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.1.6-1
- Bump version to 1.4.1.6
- Issue 50355 - SSL version min and max not correctly applied
- Issue 50497 - Port cl-dump.pl tool to Python using lib389
- Issue 48851 - investigate and port TET matching rules filter tests(Final)
- Issue 50417 - fix regression from previous commit
- Issue 50425 - Add jemalloc LD_PRELOAD to systemd drop-in file
- Issue 50325 - Add Security tab to UI
- Issue 49789 - By default, do not manage unhashed password
- Issue 49421 - Implement password hash upgrade on bind.
- Issue 49421 - on bind password upgrade proof of concept
- Issue 50493 - connection_is_free to trylock
- Issue 50459 - Correct issue with allocation state
- Issue 50499 - Fix audit issues and remove jquery from the whitelist
- Issue 50459 - c_mutex to use pthread_mutex to allow ns sharing
- Issue 50484 - Add a release build dockerfile and dscontainer improvements
- Issue 50486 - Update jemalloc to 5.2.0

* Mon Jul 8 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.1.5-1
- Bump version to 1.4.1.5
- Issue 50431 - Fix regression from coverity fix (crash in memberOf plugin)
- Issue 49239 - Add a new CI test case
- Issue 49997 - Add a new CI test case
- Issue 50177 - Add a new CI test case, also added fixes in lib389
- Issue 49761 - Fix CI test suite issues
- Issue 50474 - Unify result codes for add and modify of repl5 config
- Issue 50472 - memory leak with encryption
- Issue 50462 - Fix Root DN access control plugin CI tests
- Issue 50462 - Fix CI tests
- Issue 50217 - Implement dsconf security section
- Issue 48851 - Add more test cases to the match test suite.
- Issue 50378 - ACI's with IPv4 and IPv6 bind rules do not work for IPv6 clients
- Issue 50439 - fix waitpid issue when pid does not exist
- Issue 50454 - Fix Cockpit UI branding
- Issue 48851 - investigate and port TET matching rules filter tests(index)
- Issue 49232 - Truncate the message when buffer capacity is exceeded

* Tue Jun 18 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.1.4-1
- Bump version to 1.4.1.4
- Issue 49361 - Use IPv6 friendly network functions
- Issue 48851 - Investigate and port TET matching rules filter tests(bug772777)
- Issue 50446 - NameError: name 'ds_is_older' is not defined
- Issue 49602 - Revise replication status messages
- Issue 50439 - Update docker integration to work out of source directory
- Issue 50037 - revert path changes as it breaks prefix/rpm builds
- Issue 50431 - Fix regression from coverity fix
- Issue 50370 - CleanAllRUV task crashing during server shutdown
- Issue 48851 - investigate and port TET matching rules filter tests(match)
- Issue 50417 - Fix missing quote in some legacy tools
- Issue 50431 - Fix covscan warnings
- Revert "Issue 49960 - Core schema contains strings instead of numer oids"
- Issue 50426 - nsSSL3Ciphers is limited to 1024 characters
- Issue 50052 - Fix rpm.mk according to audit-ci change
- Issue 50365 - PIDFile= references path below legacy directory /var/run/
- Issue 50428 - Log the actual base DN when the search fails with "invalid attribute request"
- Issue 50329 - (2nd) Possible Security Issue: DOS due to ioblocktimeout not applying to TLS
- Issue 50417 - Revise legacy tool scripts to work with new systemd changes
- Issue 48851 - Add more search filters to vfilter_simple test suite
- Issue 49761 - Fix CI test suite issues
- Issue 49875 - Move SystemD service config to a drop-in file
- Issue 50413 - ds-replcheck - Always display the Result Summary
- Issue 50052 - Add package-lock.json and use "npm ci"
- Issue 48851 - investigate and port TET matching rules filter tests(vfilter simple)
- Issue 50355 -  NSS can change the requested SSL min and max versions
- Issue 48851 - investigate and port TET matching rules filter tests(vfilter_ld)
- Issue 50390 - Add Managed Entries Plug-in Config Entry schema
- Issue 49730 - Remove unused Mozilla ldapsdk variables

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.1.3-1.1
- Perl 5.30 rebuild

* Fri May 24 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.1.3-1
- Bump version to 1.4.1.3
- Issue 49761 - Fix CI test suite issues
- Issue 50041 - Add the rest UI Plugin tabs - Part 2
- Issue 50340 - 2nd try - structs for diabled plugins will not be freed
- Issue 50403 - Instance creation fails on 1.3.9 using perl utils and latest lib389
- Issue 50389 - ns-slapd craches while two threads are polling the same connection
- Issue 48851 - investigate and port TET matching rules filter tests(scanlimit)
- Issue 50037 - lib389 fails to install in venv under non-root user
- Issue 50112 - Port ACI test suit from TET to python3(userattr)
- Issue 50393 - maxlogsperdir accepting negative values
- Issue 50112 - Port ACI test suit from TET to python3(roledn)
- Issue 49960 - Core schema contains strings instead of numer oids
- Issue 50396 - Crash in PAM plugin when user does not exist
- Issue 50387 - enable_tls() should label ports with ldap_port_t
- Issue 50390 - Add Managed Entries Plug-in Config Entry schema
- Issue 50306 - Fix regression with maxbersize
- Issue 50384 - Missing dependency: cracklib-dicts
- Issue 49029 - [RFE] improve internal operations logging
- Issue 49761 - Fix CI test suite issues
- Issue 50374 - dsdim posixgroup create fails with ERROR
- Issue 50251 - clear text passwords visable in CLI verbose mode logging
- Issue 50378 - ACI's with IPv4 and IPv6 bind rules do not work for IPv6 clients
- Issue 48851 - investigate and port TET matching rules filter tests
- Issue 50220 - attr_encryption test suite failing
- Issue 50370 -  CleanAllRUV task crashing during server shutdown
- Issue 50340 - structs for disabled plugins will not be freed
- Issue 50164 - Add test for dscreate to basic test suite
- Issue 50363 - ds-replcheck incorrectly reports error out of order multi-valued attributes
- Issue 49730 - MozLDAP bindings have been unsupported for a while
- Issue 50353 - Categorize tests by tiers
- Issue 50303 - Add creation date to task data
- Issue 50358 -  Create a Bitwise Plugin class in plugins.py
- Remove the nss3 path prefix from the cert.h C preprocessor source file inclusion
- Issue 50329 - revert fix
- Issue 50112 - Port ACI test suit from TET to python3(keyaci)
- Issue 50344 - tidy rpm vs build systemd flag handling
- Issue 50067 - Fix krb5 dependency in a specfile
- Issue 50340 - structs for diabled plugins will not be freed
- Issue 50327 - Add replication conflict support to UI
- Issue 50327 - Add replication conflict entry support to lib389/CLI
- Issue 50329 - improve connection default parameters
- Issue 50313 - Add a NestedRole type to lib389
- Issue 50112 - Port ACI test suit from TET to python3(Delete and  Add)
- Issue 49390, 50019 - support cn=config compare operations
- Issue 50041 - Add the rest UI Plugin tabs - Part 1
- Issue 50329 - Possible Security Issue: DOS due to ioblocktimeout not applying to TLS
- Issue 49990 - Increase the default FD limits
- Issue 50306 - (cont typo) Move connection config inside struct
- Issue 50291 - Add monitor tab functionality to Cockpit UI
- Issue 50317 - fix ds-backtrace issue on latest gdb
- Issue 50305 - Revise CleanAllRUV task restart process
- Issue 49915 - Fix typo
- Issue 50026 - Audit log does not capture the operation where nsslapd-lookthroughlimit is modified
- Issue 49899 - fix pin.txt and pwdfile permissions
- Issue 49915 - Add regression test
- Issue 50303 - Add task creation date to task data
- Issue 50306 - Move connection config inside struct
- Issue 50240 - Improve task logging
- Issue 50032 - Fix deprecation warnings in tests
- Issue 50310 - fix sasl header include
- Issue 49390 - improve compare and cn=config compare tests

* Wed Apr 03 2019 Adam Williamson <awilliam@redhat.com> - 1.4.1.2-3
- Rebuild without changes to be newer than 1.4.1.2-1 (see #1694990)

* Fri Mar 29 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.1.2-2
- Bump version to 1.4.1.2-2
- Fix lib389 python requirement

* Fri Mar 29 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.1.2-1
- Bump version to 1.4.1.2-1
- Ticket 50308 - Revise memory leak fix
- Ticket 50308 - Fix memory leaks for repeat binds and replication
- Ticket 40067 - Use PKG_CHECK_MODULES to detect libraries
- Ticket 49873 - (cont 3rd) cleanup debug log
- Ticket 49873 - (cont 2nd) Contention on virtual attribute lookup
- Ticket 50292 - Fix Plugin CLI and UI issues
- Ticket 50112 - Port ACI test suit from TET to python3(misc and syntax)
- Ticket 50289 - Fix various database UI issues
- Ticket 49463 - After cleanALLruv, replication is looping on keep alive DEL
- Ticket 50300 - Fix memory leak in automember plugin
- Ticket 50265 - the warning about skew time could last forever
- Ticket 50260 - Invalid cache flushing improvements
- Ticket 49561 - MEP plugin, upon direct op failure, will delete twice the same managed entry
- Ticket 50077 - Do not automatically turn automember postop modifies on
- Ticket 50282 - OPERATIONS ERROR when trying to delete a group with automember members
- Ticket 49715 - extend account functionality
- Ticket 49873 - (cont) Contention on virtual attribute lookup
- Ticket 50260 - backend txn plugins can corrupt entry cache
- Ticket 50255 - Port password policy test to use DSLdapObject
- Ticket 49667 - 49668 - remove old spec files
- Ticket 50276 - 389-ds-console is not built on RHEL8 if cockpit_dist is already present
- Ticket 50112 - Port ACI test suit from TET to python3(Search)
- Ticket 50259 - implement dn construction test
- Ticket 50273 - reduce default replicaton agmt timeout
- Ticket 50208 - lib389- Fix issue with list all instances
- Ticket 50112 - Port ACI test suit from TET to python3(Global Group)
- Ticket 50041 - Add CLI functionality for special plugins
- Ticket 50263 - LDAPS port not listening after installation
- Ticket 49575 - Indicate autosize value errors and corrective actions
- Ticket 50137 - create should not check in non-stateful mode for exist
- Ticket 49655 - remove doap file
- Ticket 50197 - Fix dscreate regression
- Ticket 50234 - one level search returns not matching entry
- Ticket 50257 - lib389 - password policy user vs subtree checks are broken
- Ticket 50253 -  Making an nsManagedRoleDefinition type in src/lib389/lib389/idm/nsrole.py
- Ticket 49029 - [RFE] improve internal operations logging
- Ticket 50230 - improve ioerror msg when not root/dirsrv
- Ticket 50246 - Fix the regression in old control tools
- Ticket 50197 - Container integration part 2
- Ticket 50197 - Container init tools
- Ticket 50232 - export creates not importable ldif file
- Ticket 50215 - UI - implement Database Tab in reachJS
- Ticket 50243 - refint modrdn stress test
- Ticket 50238 - Failed modrdn can corrupt entry cache
- Ticket 50236 - memberOf should be more robust
- Ticket 50213 - fix list instance issue
- Ticket 50219 - Add generic filter to DSLdapObjects
- Ticket 50227 - Making an cosClassicDefinition type in src/lib389/lib389/cos.py
- Ticket 50112 - Port ACI test suit from TET to python3(modify)
- Ticket 50224 - warnings on deprecated API usage
- Ticket 50112 - Port ACI test suit from TET to python3(valueaci)
- Ticket 50112 - Port ACI test suit from TET to python3(Aci Atter)
- Ticket 50208 - make instances mark off based on dse.ldif not sysconfig
- Ticket 50170 - composable object types for nsRole in lib389
- Ticket 50199 - disable perl by default
- Ticket 50211 - Making an actual Anonymous type in lib389/idm/account.py
- Ticket 50155 - password history check has no way to just check the current password
- Ticket 49873 - Contention on virtual attribute lookup
- Ticket 50197 - Container integration improvements
- Ticket 50195 - improve selinux error messages in interactive
- Ticket 49658 - In replicated topology a single-valued attribute can diverge
- Ticket 50111 - Use pkg-config to detect icu
- Ticket 50165 - Fix issues with dscreate
- Ticket 50177 - import task should not be deleted too rapidely after import finishes to be able to query the status
- Ticket 50140 - Use high ports in container installs
- Ticket 50184 - Add cli tool parity to dsconf/dsctl
- Ticket 50159 - sssd and config display

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Mark Reynolds <mreynolds@redhat.com> - 1.4.1.1-1
-  Bump version to 1.4.1.1
-  Ticket 50151 - lib389 support cli add/replace/delete on objects
-  Ticket 50041 - CLI and WebUI - Add memberOf plugin functionality

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.4.0.20-1.2
- Rebuild for ICU 63

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.4.0.20-1.1
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Dec 14 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.20-1
- Bump version to 1.4.0.20
- Ticket 49994 - Add test for backend/suffix CLI functions
- Ticket 50090 - refactor fetch_attr() to slapi_fetch_attr()
- Ticket 50091 - shadowWarning is not generated if passwordWarning is lower than 86400 seconds (1 day)
- Ticket 50056 - Fix CLI/UI bugs
- Ticket 49864 - Revised replication status messages for transient errors
- Ticket 50071 - Set ports in local_simple_allocate function
- Ticket 50065 - lib389 aci parsing is too strict
- Ticket 50061 - Improve schema loading in UI
- Ticket 50063 - Crash after attempting to restore a single backend
- Ticket 50062 - Replace error by warning in the state machine defined in repl5_inc_run
- Ticket 50041 - Set the React dataflow foundation and add basic plugin UI
- Ticket 50028 - Revise ds-replcheck usage
- TIcket 50057 - Pass argument into hashtable_new
- Ticket 50053 - improve testcase
- Ticket 50053 - Subtree password policy overrides a user-defined password policy
- Ticket 49974 - lib389 - List instances with initconfig_dir instead of sysconf_dir
- Ticket 49984 - Add an empty domain creation to the dscreate
- Ticket 49950 -  PassSync not setting pwdLastSet attribute in Active Directory after Pw update from LDAP sync for normal user
- Ticket 50046 - Remove irrelevant debug-log messages from CLI tools
- Ticket 50022, 50012, 49956, and 49800: Various dsctl/dscreate fixes
- Ticket 49927 - dsctl db2index does not work
- Ticket 49814 - dscreate should handle selinux ports that are in a range
- Ticket 49543 - fix certmap dn comparison
- Ticket 49994 - comment out dev paths
- Ticket 49994 - Add backend features to CLI
- Ticket 48081 - Add new CI tests for password

* Thu Nov 1 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.19-1
- Bump version to 1.4.0.19
- Ticket 50026 - audit logs does not capture the operation where nsslapd-lookthroughlimit is modified
- Ticket 50020 - during MODRDN referential integrity can fail erronously while updating large groups
- Ticket 49999 - Finish up the transfer to React
- Ticket 50004 - lib389 - improve X-ORIGIN schema parsing
- Ticket 50013 - Log warn instead of ERR when aci target does not exist.
- Ticket 49975 - followup for broken prefix deployment
- Ticket 49999 - Add dist-bz2 target for Koji build system
- Ticket 49814 - Add specfile requirements for python3-libselinux
- Ticket 49814 - Add specfile requirements for python3-selinux
- Ticket 49999 - Integrate React structure into cockpit-389-ds
- Ticket 49995 - Fix Tickets with internal op logging
- Ticket 49997 - RFE: ds-replcheck could validate suffix exists and it's replicated
- Ticket 49985 - memberof may silently fails to update a member
- Ticket 49967 - entry cache corruption after failed MODRDN
- Ticket 49975 - Add missing include file to main.c
- Ticket 49814 - skip standard ports for selinux labelling
- Ticket 49814 - dscreate should set the port selinux labels
- Ticket 49856 - Remove backend option from bak2db
- Ticket 49926 - Fix various Tickets with replication UI
- Ticket 49975 - SUSE rpmlint Tickets
- Ticket 49939 - Fix ldapi path in lib389
- Ticket 49978 - Add CLI logging function for UI
- Ticket 49929 - Modifications required for the Test Case Management System
- Ticket 49979 - Fix regression in last commit
- Ticket 49979 - Remove dirsrv tests subpackage
- Ticket 49928 - Fix various small WebUI schema Tickets
- Ticket 49926 - UI - comment out dev cli patchs
- Ticket 49926 - Add replication functionality to UI

* Wed Oct 10 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.18-1
- Bump version to 1.4.0.18
- Ticket 49968 - Confusing CRITICAL message: list_candidates - NULL idl was recieved from filter_candidates_ext
- Ticket 49946 - upgrade of 389-ds-base could remove replication agreements.
- Ticket 49969 - DOS caused by malformed search operation (part 2)

* Tue Oct 9 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.17-2
- Bump version to 1.4.0.17-2
- Ticket 49969 - DOS caused by malformed search operation (security fix)
- Ticket 49943 - rfc3673_all_oper_attrs_test is not strict enough
- Ticket 49915 - Master ns-slapd had 100% CPU usage after starting replication and replication cannot finish
- Ticket 49963 - ASAN build fails on F28
- Ticket 49947 - Coverity Fixes
- Ticket 49958 - extended search fail to match entries
- Ticket 49928 - WebUI schema functionality and improve CLI part
- Ticket 49954 - On s390x arch retrieved DB page size is stored as size_t rather than uint32_t
- Ticket 49928 - Refactor and improve schema CLI/lib389 part to DSLdapObject
- Ticket 49926 - Fix replication tests on 1.3.x
- Ticket 49926 - Add replication functionality to dsconf
- Ticket 49887 - Clean up thread local usage
- Ticket 49937 - Log buffer exceeded emergency logging msg is not thread-safe (security fix)
- Ticket 49866 - fix typo in cos template in pwpolicy subtree create
- Ticket 49930 - Correction of the existing fixture function names to remove test_ prefix
- Ticket 49932 - Crash in delete_passwdPolicy when persistent search connections are terminated unexpectedly
- Ticket 48053 - Add attribute encryption test cases
- Ticket 49866 - Refactor PwPolicy lib389/CLI module
- Ticket 49877 - Add log level functionality to UI

* Fri Aug 24 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.16-1
- Bump version to 1.4.0.16
- Revert "Ticket 49372 - filter optimisation improvements for common queries"
- Revert "Ticket 49432 - filter optimise crash"
- Ticket 49887: Fix SASL map creation when --disable-perl
- Ticket 49858 - Add backup/restore and import/export functionality to WebUI/CLI

* Thu Aug 16 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.15-1
- Bump version to 1.4.0.15
- Ticket 49029 - Internal logging thread data needs to allocate int pointers
- Ticket 48061 : CI test - config
- Ticket 48377 - Only ship libjemalloc.so.2
- Ticket 49885 - On some platform fips does not exist

* Mon Aug 13 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.14-2
- Bump version to 1.4.0.14-2
- Fix legacy tool scriplet error
- Remove ldconfig calls
- Only provide libjemalloc.so.2

* Fri Aug 10 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.14-1
- Bump version to 1.4.0.14
- Ticket 49891 - Use "__python3" macro for python scripts
- Ticket 49890 - ldapsearch with server side sort crashes the ldap server
- Ticket 49029 - RFE -improve internal operations logging
- Ticket 49893 - disable nunc-stans by default
- Ticket 48377 - Update file name for LD_PRELOAD
- Ticket 49884 - Improve nunc-stans test to detect socket errors sooner
- Ticket 49888 - Use perl filter in rpm specfile
- Ticket 49866 - Add password policy features to CLI/UI
- Ticket 49881 - Missing check for crack.h
- Ticket 48056 - Add more test cases to the basic suite
- Ticket 49761 - Fix replication test suite issues
- Ticket 49381 - Refactor the plugin test suite docstrings
- Ticket 49837 - Add new password policy attributes to UI
- Ticket 49794 - RFE - Add pam_pwquality features to password syntax checking
- Ticket 49867 - Fix CLI tools' double output

* Thu Jul 19 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.13-1
- Bump version to 1.4.0.13
- Ticket 49854 - ns-slapd should create run_dir and lock_dir directories at startup
- Ticket 49806 - Add SASL functionality to CLI/UI
- Ticket 49789 - backout original security fix as it caused a regression in FreeIPA
- Ticket 49857 - RPM scriptlet for 389-ds-base-legacy-tools throws an error

* Tue Jul 17 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.12-1
- Bump version to 1.4.0.12-1
- Ticket 48377 - Move jemalloc license to /usr/share/licences
- Ticket 49813 - Revised interactive installer
- Ticket 49789 - By default, do not manage unhashed password
- Ticket 49844 - lib389: don't set up logging at module scope
- Ticket 49546 - Fix issues with MIB file
- Ticket 49840 - ds-replcheck command returns traceback errors against ldif files having garbage content when run in offline mode
- Ticket 49640 - Cleanup plugin bootstrap logging
- Ticket 49835 - lib389: fix logging
- Ticket 48818 - For a replica bindDNGroup, should be fetched the first time it is used not when the replica is started
- Ticket 49780 - acl_copyEval_context double free
- Ticket 49830 - Import fails if backend name is "default"
- Ticket 49832 - remove tcmalloc references
- Ticket 49813 - dscreate - add interactive installer
- Ticket 49808 - Add option to add backend to dscreate
- Ticket 49811 - lib389 setup.py should install autogenerated man pages
- Ticket 49795 - UI - add "action" backend funtionality
- Ticket 49588 - Add py3 support for tickets : part-3
- Ticket 49820 - lib389 requires wrong python ldap library
- Ticket 49791 - Update docker file for new dscreate options
- Ticket 49761 - Fix more CI test issues
- Ticket 49811 - Update man pages
- Ticket 49783 - UI - add server configuration backend
- Ticket 49717 - Add conftest.py for tests
- Ticket 49588 - Add py3 support for tickets
- Ticket 49793 - Updated descriptions in dscreate example INF file
- Ticket 49471 - Rename dscreate options
- Ticket 49751 - passwordMustChange attribute is not honored by a RO consumer if using "Chain on Update"
- Ticket 49734 - Fix various issues with Disk Monitoring
- Update Source0 URL in rpm/389-ds-base.spec.in


* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.11-2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.4.0.11-2.4
- Rebuild for ICU 62

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1.4.0.11-2.3
- Perl 5.28 rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0.11-2.2
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.0.11-2.1
- Perl 5.28 rebuild

* Thu Jun 21 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.11-2
- Bump version to 1.4.0.11-2
- Add python3-lib389 requirement

* Tue Jun 19 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.11-1
- Bump version to 1.4.0.11
- Test for issue #49788
- Fixing 4-byte UTF-8 character validation
- Ticket 49777 - add config subcommand to dsconf
- Ticket 49712 - lib389 CLI tools should return a result code on failures
- Issue 49588 - Add py3 support for tickets : part-2
- Remove old RHEL/fedora version checking from upstream specfile
- Ticket 48204 - remove python2 from scripts
- Ticket 49576 - ds-replcheck: fix certificate directory verification
- Bug 1591761 - 389-ds-base: Remove jemalloc exports

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0.10-2.1
- Rebuilt for Python 3.7

* Fri Jun 8 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.10-2
- Bump verision to 1.4.0.10-2
- Remove reference ro stop-dirsrv from legacy tools

* Fri Jun 8 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.10-1
- Bump verision to 1.4.0.10-1
- Ticket 49640 - Errors about PBKDF2 password storage plugin at server startup
- Ticket 49571 - perl subpackage and python installer by default
- Ticket 49740 - UI - Replication monitor color coding is not colorblind friendly
- Ticket 49741 - UI - View/Edit replication agreement hangs WebUI
- Ticket 49703 - UI - Set default values in create instance form
- Ticket 49742 - Fine grained password policy can impact search performance
- Ticket 49768 - Under network intensive load persistent search can erronously decrease connection refcnt
- Ticket 49765 - compiler warning
- Ticket 49689 - Cockpit subpackage does not build in PREFIX installations
- Ticket 49765 - Async operations can hang when the server is running nunc-stans
- Ticket 49745 - UI add filter options for error log severity levels
- Ticket 49761 - Fix test suite issues
- Ticket 49754 - instances created with dscreate can not be upgraded with setup-ds.pl
- Ticket 47902 - UI - add continuous refresh log feature
- Ticket 49381 - Add docstrings to plugin test suites - Part 1
- Ticket 49646 - Improve TLS cert processing in lib389 CLI
- Ticket 49748 - Passthru plugin startTLS option not working
- Ticket 49732 - Optimize resource limit checking for rootdn issued searches
- Ticket 48377 - Bundle jemalloc
- Ticket 49736 - Hardening of active connection list
- Ticket 48184 - clean up and delete connections at shutdown (3rd)
- Ticket 49675 - Revise coverity fix
- Ticket 49333 - Do not remove versioned man pages
- Ticket 49683 - Add support for JSON option in lib389 CLI tools
- Ticket 49704 - Error log from the installer is concatenating all lines into one
- Ticket 49726 - DS only accepts RSA and Fortezza cipher families
- Ticket 49722 - Errors log full of " WARN - keys2idl - recieved NULL idl from index_read_ext_allids, treating as empty set" messages
- Ticket 49582 - Add py3 support to memberof_plugin test suite
- Ticket 49675 - Fix coverity issues
- Ticket 49576 - Add support of ";deletedattribute" in ds-replcheck
- Ticket 49706 - Finish UI patternfly convertions
- Ticket 49684 - AC_PROG_CC clobbers CFLAGS set by --enable-debug
- Ticket 49678 - organiSational vs organiZational spelling in lib389
- Ticket 49689 - Fix local "make install" after adding cockpit subpackage
- Ticket 49689 - Move Cockpit UI plugin to a subpackage
- Ticket 49679 - Missing nunc-stans documentation and doxygen warnings
- Ticket 49588 - Add py3 support for tickets : part-1
- Ticket 49576 - Update ds-replcheck for new conflict entries
- Ticket 48184 - clean up and delete connections at shutdown (2nd try)
- Ticket 49698 - Remove unneeded patternfly files from Cockpit package
- Ticket 49581 - Fix dynamic plugins test suite
- Ticket 49665 - remove obsoleted upgrade scripts
- Ticket 49693 - A DB_DEADLOCK while adding a tombstone (RUV) leads to access of an already freed entry
- Ticket 49696 - replicated operations should be serialized
- Ticket 49669 - Invalid cachemem size can crash the server during a restore
- Ticket 49684 - AC_PROG_CC clobbers CFLAGS set by --enable-debug
- Ticket 49685 - make clean fails if cargo is not installed
- Ticket 49106 - Move ds_* scripts to libexec
- Ticket 49657 - Fix cascading replication scenario in lib389 API
- Ticket 49671 - Readonly replicas should not write internal ops to changelog
- Ticket 49673 - nsslapd-cachememsize can't be set to a value bigger than MAX_INT
- Ticket 49519 - Convert Cockpit UI to use strictly patternfly stylesheets
- Ticket 49665 - Upgrade script doesn't enable CRYPT password storage plug-in
- Ticket 49665 - Upgrade script doesn't enable PBKDF2 password storage plug-in

* Tue May 15 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.9-2
- Bump version to 1.4.0.9-2
- Add openssl-perl requirement for new python installer

* Tue May 8 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.9-1
- Bump version to 1.4.0.9
- Ticket 49661 - CVE-2018-1089 - Crash from long search filter
- Ticket 49652 - DENY aci's are not handled properly
- Ticket 49650 - lib389 enable_tls doesn't work on F28
- Ticket 49538 - replace cacertdir_rehash with openssl rehash
- Ticket 49406 - Port backend_test.py test to DSLdapObject implementation
- Ticket 49649 - Use reentrant crypt_r()
- Ticket 49642 - lib389 should generate a more complex password
- Ticket 49612 - lib389 remove_ds_instance() does not remove systemd units
- Ticket 49644 - crash in debug build

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.4.0.8-1.1
- Rebuild for ICU 61.1

* Thu Apr 19 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.8-1
- Bump version to 1.4.0.8-1
- Ticket 49639 - Crash when failing to read from SASL conn
- Ticket 49109 - nsDS5ReplicaTransportInfo should accept StartTLS as an option
- Ticket 49586 - Add py3 support to plugins test suite
- Ticket 49511 - memory leak in pwdhash

* Mon Apr 16 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.7-2
- Bump version to 1.4.0.7-2
- Fix the devel srvcore requirements

* Fri Apr 13 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.7-1
- Bump version to 1.4.0.7
- Ticket 49477 - Missing pbkdf python
- Ticket 49552 - Fix the last of the build issues on F28/29
- Ticket 49522 - Fix build issues on F28
- Ticket 49631 - same csn generated twice
- Ticket 49585 - Add py3 support to password test suite : part-3
- Ticket 49585 - Add py3 support to password test suite : part-2
- Ticket 48184 - revert previous patch around unuc-stans shutdown crash
- Ticket 49585 - Add py3 support to password test suite
- Ticket 46918 - Fix compiler warnings on arm
- Ticket 49601 - Replace HAVE_SYSTEMD define with WITH_SYSTEMD in svrcore
- Ticket 49619 - adjustment of csn_generator can fail so next generated csn can be equal to the most recent one received
- Ticket 49608 - Add support for gcc/clang sanitizers
- Ticket 49606 - Improve lib389 documentation
- Ticket 49552 - Fix build issues on F28
- Ticket 49603 - 389-ds-base package rebuilt on EPEL can't be installed due to missing dependencies
- Ticket 49593 - NDN cache stats should be under the global stats
- Ticket 49599 - Revise replication total init status messages
- Ticket 49596 - repl-monitor.pl fails to find db tombstone/RUV entry
- Ticket 49589 - merge svrcore into 389-ds-base
- Ticket 49560 - Add a test case for extract-pemfiles
- Ticket 49239 - Add a test suite for ds-replcheck tool RFE
- Ticket 49369 - merge svrcore into 389-ds-base

* Thu Mar 29 2018 Till Maas <opensource@till.name> - 1.4.0.6-3
- Remove BR on tcp_wrappers (https://bugzilla.redhat.com/show_bug.cgi?id=1518749)

* Tue Mar 6 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.6-1
- Bump version to 1.4.0.6
- Ticket 49545 - final substring extended filter search returns invalid result
- Ticket 49572 - ns_job_wait race on condvar
- Ticket 49584 - Fix Tickets with paged_results test suite
- Ticket 49161 - memberof fails if group is moved into scope
- Ticket 49447 - PBKDF2 on upgrade
- ticket 49551 - correctly handle subordinates and tombstone numsubordinates
- Ticket 49043 - Add replica conflict test suite
- Ticket 49296 - Fix race condition in connection code with  anonymous limits
- Ticket 49568 - Fix integer overflow on 32bit platforms
- Ticket 48085 - Add encryption cl5 test suite
- Ticket 49566 - ds-replcheck needs to work with hidden conflict entries
- Ticket 49519 - Add more Cockpit UI content
- Ticket 49551 - fix memory leak found by coverity
- Ticket 49551 - v3 - correct handling of numsubordinates for cenotaphs and tombstone delete
- Ticket 49278 - Add a new CI test case
- Ticket 49560 - nsslapd-extract-pemfiles should be enabled by default as openldap is moving to openssl
- Ticket 49557 - Add config option for checking CRL on outbound SSL Connections
- Ticket 49446 - Add CI test case
- Ticket 35 -    Description: Add support for managing automember to dsconf
- Ticket 49544 - cli release preperation
- Ticket 48006 - Add a new CI test case

* Mon Feb 19 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.5-1.7
- Add cyrus-sasl-plain requirement

* Thu Feb 15 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.5-1.6
- Fix python requirements for policycoreutils-python-utils

* Thu Feb 15 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.5-1.5
- Fix package requirements to use Python 3 packages for LDAP and SELinux

* Thu Feb 15 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.5-1.4
- Only exclude Ix86 arches

* Thu Feb 15 2018 Adam Williamson <awilliam@redhat.com> - 1.4.0.5-1.3
- Rebuild for libevent soname bump

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.0.5-1.2
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.5-1
- Bump version to 1.4.0.5
- CVE-2017-15134 389-ds-base: Remote DoS via search filters in slapi_filter_sprintf
- Ticket 49546 - Fix broken snmp MIB file
- Ticket 49554 - update readme
- Ticket 49554 - Update Makefile for README.md
- Ticket 49400 - Make CLANG configurable
- Ticket 49530 - Add pseudolocalization option for dbgen
- Ticket 49523 - Fixed skipif marker, topology fixture and log message
- Ticket 49544 - Double check pw prompts
- Ticket 49548 - Cockpit UI - installer should also setup Cockpit

* Fri Jan 26 2018 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.4-1
- Bump version to 1.4.0.4
- Ticket 49540 - Indexing task is reported finished too early regarding the backend status
- Ticket 49534 - Fix coverity regression
- Ticket 49544 - cli release preperation, group improvements
- Ticket 49542 - Unpackaged files on el7 break rpm build
- Ticket 49541 - repl config should not allow rid 65535 for masters
- Ticket 49370 - Add all the password policy defaults to a new local policy
- Ticket 49425 - improve demo objects for install
- Ticket 49537 - allow asan to build with stable rustc
- Ticket 49526 - Improve create_test.py script
- Ticket 49516 - Add python 3 support for replication suite
- Ticket 49534 - Fix coverity issues and regression
- Ticket 49532 - coverity issues - fix compiler warnings & clang issues
- Ticket 49531 - coverity issues - fix memory leaks
- Ticket 49463 - After cleanALLruv, there is a flow of keep alive DEL
- Ticket 49529 - Fix Coverity warnings: invalid deferences
- Ticket 49509 - Indexing of internationalized matching rules is failing
- Ticket 49527 - Improve ds* cli tool testing
- Ticket 49474 - purge saslmaps before gssapi test
- Ticket 49413 - Changelog trimming ignores disabled replica-agreement
- Ticket 49446 - cleanallruv should ignore cleaned replica Id in processing changelog if in force mode
- Ticket 49278 - GetEffectiveRights gives false-negative
- Ticket 49508 - memory leak in cn=replica plugin setup
- Ticket 48118 - Add CI test case
- Ticket 49520 - Cockpit UI - Add database chaining HTML
- Ticket 49512 - Add ds-cockpit-setup to rpm spec file
- Ticket 49523 - Refactor CI test
- Ticket 49524 - Password policy: minimum token length fails  when the token length is equal to attribute length
- Ticket 49517 - Cockpit UI - Add correct png files
- Ticket 49517 - Cockput UI - revise config layout
- Ticket 49523 - memberof: schema violation error message is confusing as memberof will likely repair target entry
- Ticket 49312 - Added a new test case for "-D configdir"
- Ticket 49512 - remove backup directories from cockpit source
- Ticket 49512 - Add initial Cockpit UI Plugin
- Ticket 49515 - cannot link, missing -fPIC
- Ticket 49474 - Improve GSSAPI testing capability
- Ticket 49493 - heap use after free in csn_as_string
- Ticket 49379 - Add Python 3 support to CI test
- Ticket 49431 - Add CI test case
- Ticket 49495 - cos stress test and improvements.
- Ticket 49495 - Fix memory management is vattr.
- Ticket 49494 - python 2 bytes mode.
- Ticket 49471 - heap-buffer-overflow in ss_unescape
- Ticket 48184 - close connections at shutdown cleanly.
- Ticket 49218 - Certmap - support TLS tests
- Ticket 49470 - overflow in pblock_get
- Ticket 49443 - Add CI test case
- Ticket 49484 - Minor cli tool fixes.
- Ticket 49486 - change ns stress core to use absolute int width.
- Ticket 49445 - Improve regression test to detect memory leak.
- Ticket 49445 - Memory leak in ldif2db
- Ticket 49485 - Typo in gccsec_defs
- Ticket 49479 - Remove unused 'batch' argument from lib389
- Ticket 49480 - Improvements to support IPA install.
- Ticket 49474 - sasl allow mechs does not operate correctly
- Ticket 49449 - Load sysctl values on rpm upgrade.
- Ticket 49374 - Add CI test case
- Ticket 49325 - fix rust linking.
- Ticket 49475 - docker poc improvements.
- Ticket 49461 - Improve db2index handling for test 49290
- Ticket 47536 - Add Python 3 support and move test case to suites
- Ticket 49444 - huaf in task.c during high load import
- Ticket 49460 - replica_write_ruv log a failure even when it succeeds
- Ticket 49298 - Ticket with test case and remove-ds.pl
- Ticket 49408 - Add a test case for nsds5ReplicaId checks
- Ticket 3 lib389 - python 3 support for subset of pwd cases
- Ticket 35 lib389 - dsconf automember support

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.4.0.3-1.2
- Rebuilt for switch to libxcrypt

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.4.0.3-1.1
- Rebuild for ICU 60.1

* Mon Nov 20 2017 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.3-1
- Bump version to 1.4.0.3
- Ticket 49457 - Fix spal_meminfo_get function prototype
- Ticket 49455 - Add tests to monitor test suit.
- Ticket 49448 - dynamic default pw scheme based on environment.
- Ticket 49298 - fix complier warn
- Ticket 49298 - Correct error codes with config restore.
- Ticket 49454 - SSL Client Authentication breaks in FIPS mode
- Ticket 49453 - passwd.py to use pwdhash defaults.
- Ticket 49427 - whitespace in fedse.c
- Ticket 49410 - opened connection can remain no longer poll, like hanging
- Ticket 48118 - fix compiler warning for incorrect return type
- Ticket 49451 - Add environment markers to lib389 dependencies
- Ticket 49325 - Proof of concept rust tqueue in sds
- Ticket 49443 - scope one searches in 1.3.7 give incorrect results
- Ticket 48118 - At startup, changelog can be erronously rebuilt after a normal shutdown
- Ticket 49412 - SIGSEV when setting invalid changelog config value
- Ticket 49441 - Import crashes - oneline fix
- Ticket 49377 - Incoming BER too large with TLS on plain port
- Ticket 49441 - Import crashes with large indexed binary  attributes
- Ticket 49435 - Fix NS race condition on loaded test systems
- Ticket 77 - lib389 - Refactor docstrings in rST format - part 2
- Ticket 17 - lib389 - dsremove support
- Ticket 3 - lib389 - python 3 compat for paged results test
- Ticket 3 - lib389 - Python 3 support for memberof plugin test suit
- Ticket 3 - lib389 - config test
- Ticket 3 - lib389 - python 3 support ds_logs tests
- Ticket 3 - lib389 - python 3 support for betxn test

* Fri Nov 3 2017 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.2-2
- Bump version to 1.4.0.2-2
- Add python-lib389 build requirements

* Fri Nov 3 2017 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.2-1
- Bump version to 1.4.0.2-1
- Ticket 48393 - fix copy and paste error
- Ticket 49439 - cleanallruv is not logging information
- Ticket 48393 - Improve replication config validation
- Ticket lib389 3 - Python 3 support for ACL test suite
- Ticket 103 - sysconfig not found
- Ticket 49436 - double free in COS in some conditions
- Ticket 48007 - CI test to test changelog trimming interval
- Ticket 49424 - Resolve csiphash alignment issues
- Ticket lib389 3 - Python 3 support for pwdPolicy_controls_test.py
- Ticket 3 - python 3 support - filter test
- Ticket 49434 - RPM build errors
- Ticket 49432 - filter optimise crash
- Ticket 49432 - Add complex fliter CI test
- Ticket 48894 - harden valueset_array_to_sorted_quick valueset  access
- Ticket 49401 - Fix compiler incompatible-pointer-types warnings
- Ticket 48681 - Use of uninitialized value in string ne at /usr/bin/logconv.pl
- Ticket 49409 - Update lib389 requirements
- Ticket 49401 - improve valueset sorted performance on delete
- Ticket 49374 -  server fails to start because maxdisksize is recognized incorrectly
- Ticket 49408 - Server allows to set any nsds5replicaid in the existing replica entry
- Ticket 49407 - status-dirsrv shows ellipsed lines
- Ticket 48681 - Use of uninitialized value in string ne at /usr/bin/logconv.pl
- Ticket 49386 - Memberof should be ignore MODRDN when the pre/post entry are identical
- Ticket 48006 - Missing warning for invalid replica backoff  configuration
- Ticket 49064 - testcase hardening
- Ticket 49064 - RFE allow to enable MemberOf plugin in dedicated consumer
- Ticket lib389 3 - python 3 support
- Ticket 49402 - Adding a database entry with the same database name that was deleted hangs server at shutdown
- Ticket 48235 - remove memberof lock (cherry-pick error)
- Ticket 49394 - build warning
- Ticket 49381 - Refactor numerous suite docstrings - Part 2
- Ticket 49394 - slapi_pblock_get may leave unchanged the provided variable
- Ticket 49403 - tidy ns logging
- Ticket 49381 - Refactor filter test suite docstrings
- Ticket 48235 - Remove memberOf global lock
- Ticket 103 - Make sysconfig where it is expected to exist
- Ticket 49400 - Add clang support to rpm builds
- Ticket 49381 - Refactor ACL test suite docstrings
- Ticket 49363 - Merge lib389
- Ticket 101 - BaseException.message has been deprecated in Python3
- Ticket 102 - referral support
- Ticket 99 - Fix typo in create_topology
- Ticket #98 - Fix dbscan output
- Ticket #77 - Fix changelogdb param issue
- Ticket #77 - Refactor docstrings in rST format - part 1
- Ticket 96 - Change binaries' names
- Ticket 77 - Add sphinx documentation
- Ticket 43 - Add support for Referential Integrity plugin
- Ticket 45 - Add support for Rootdn Access Control plugin
- Ticket 46 - dsconf support for dynamic schema reload
- Ticket 74 - Advice users to set referint-update-delay to 0
- Ticket 92 - display_attr() should return str not bytes in py3
- Ticket 93 - Fix test cases in ctl_dbtasks_test.py
- Ticket 88 - python install and remove for tests
- Ticket 85 - Remove legacy replication attribute
- Ticket 91 - Fix replication topology
- Ticket 89 - Fix inconsistency with serverid
- Ticket 79 - Fix replica.py and add tests
- Ticket 86 - add build dir to gitignore
- Ticket 83 - Add an util for generating instance parameters
- Ticket 87 - Update accesslog regec for HR etimes
- Ticket 49 - Add support for whoami plugin
- Ticket 48 - Add support for USN plugin
- Ticket 78 - Add exists() method to DSLdapObject
- Ticket 31 - Allow complete removal of some memberOf attrs
- Ticket31 - Add memberOf fix-up task
- Ticket 67 - Add ensure_int function
- Ticket 59 - lib389 support for index management.
- Ticket 67 - get attr by type
- Ticket 70 - Improve repl tools
- Ticket 50 - typo in db2* in dsctl
- Ticket 31 - Add status command and SkipNested support for MemberOf
- Ticket 31 - Add functional tests for MemberOf plugin
- Ticket 66 - expand healthcheck for Directory Server
- Ticket 69 - add specfile requires
- Ticket 31 - Initial MemberOf plugin support
- Ticket 50 - Add db2* tasks to dsctl
- Ticket 65 - Add m2c2 topology
- Ticket 63 - part 2, agreement test
- Ticket 63 - lib389 python 3 fix
- Ticket 62 - dirsrv offline log
- Ticket 60 - add dsrc to dsconf and dsidm
- Ticket 32 - Add TLS external bind support for testing
- Ticket 27 - Fix get function in tests
- Ticket 28 - userAccount for older versions without nsmemberof
- Ticket 27 - Improve dseldif API
- Ticket 30 - Add initial support for account lock and unlock.
- Ticket 29 - fix incorrect format in tools
- Ticket 28 - Change default objectClasses for users and groups
- Ticket 1 - Fix missing dn / rdn on config.
- Ticket 27 - Add a module for working with dse.ldif file
- Ticket 1 - cn=config comparison
- Ticket 21 - Missing serverid in dirsrv_test due to incorrect allocation
- Ticket 26 - improve lib389 sasl support
- Ticket 24 - Join paths using os.path.join instead of string concatenation
- Ticket 25 - Fix RUV __repr__ function
- Ticket 23 - Use DirSrv.exists() instead of manually checking for instance's existence
- Ticket 1 - cn=config comparison
- Ticket 22 - Specify a basedn parameter for IDM modules
- Ticket 19 - missing readme.md in python3
- Ticket 20 - Use the DN_DM constant instead of hard coding its value
- Ticket 19 - Missing file and improve make
- Ticket 14 - Remane dsadm to dsctl
- Ticket 16 - Reset InstScriptsEnabled argument during the init
- Ticket 14 - Remane dsadm to dsctl
- Ticket 13 - Add init function to create new domain entries
- Ticket 15 - Improve instance configuration ability
- Ticket 10 - Improve command line tool arguments
- Ticket 9 - Convert readme to MD
- Ticket 7 - Add pause and resume methods to topology fixtures
- Ticket 49172 - Allow lib389 to read system schema and instance
- Ticket 49172 - Allow lib389 to read system schema and instance
- Ticket 6 - Bump lib389 version 1.0.4
- Ticket 5 - Fix container build on fedora
- Ticket 4 - Cert detection breaks some tests
- Ticket 49137 - Add sasl plain tests, lib389 support
- Ticket 2 - pytest mark with version relies on root
- Ticket 49126 - DIT management tool
- Ticket 49101 - Python 2 generate example entries
- Ticket 49103 - python 2 support for installer
- Ticket 47747 - Add topology_i2 and topology_i3
- Ticket 49087 - lib389 resolve jenkins issues
- Ticket 48413 - Improvements to lib389 for rest
- Ticket 49083 - Support prefix for discovery of the defaults.inf file.
- Ticket 49055 - Fix debugging mode issue
- Ticket 49060 - Increase number of masters, hubs and consumers in topology
- Ticket 47747 - Add more topology fixtures
- Ticket 47840 - Add InstScriptsEnabled argument
- Ticket 47747 - Add topology fixtures module
- Ticket 48707 - Implement draft-wibrown-ldapssotoken-01
- Ticket 49022 - Lib389, py3 installer cannot create entries in backend
- Ticket 49024 - Fix paths to the dbdir parent
- Ticket 49024 - Fix db_dir paths
- Ticket 49024 - Fix paths in tools module
- Ticket 48961 - Fix lib389 minor issues shown by 48961 test
- Ticket 49010 - Lib389 fails to start with systemctl changes
- Ticket 49007 - lib389 fixes for paths to use online values
- Ticket 49005 - Update lib389 to work in containers correctly.
- Ticket 48991 - Fix lib389 spec for python2 and python3
- Ticket 48984 - Add lib389 paths module
- Ticket 48951 - dsadm dsconfig status and plugin
- Ticket 47957 - Update the replication "idle" status string
- Ticket 48951 - dsadm and dsconf base files
- Ticket 48952 - Restart command needs a sleep
- Ticket 48949 - Fix ups for style and correctness
- Ticket 48949 - added copying slapd-collations.conf
- Ticket 48949 - change default file path generation - use os.path.join
- Ticket 48949 - os.makedirs() exist_ok not python2 compatible, added try/except
- Ticket 48949 - configparser fallback not python2 compatible
- Ticket 48946 - openConnection should not fully popluate DirSrv object
- Ticket 48832 - Add DirSrvTools.getLocalhost() function
- Ticket 48382 - Fix serverCmd to get sbin dir properly
- Bug 1347760 - Information disclosure via repeated use of LDAP ADD operation, etc.
- Ticket 48937 - Cleanup valgrind wrapper script
- Ticket 48923 - Fix additional issue with serverCmd
- Ticket 48923 - serverCmd timeout not working as expected
- Ticket 48917 - Attribute presence
- Ticket 48911 - Plugin improvements for lib389
- Ticket 48911 - Improve plugin support based on new mapped objects
- Ticket 48910 - Fixes for backend tests and lib389 reliability.
- Ticket 48860 - Add replication tools
- Ticket 48888 - Correction to create of dsldapobject
- Ticket 48886 - Fix NSS SSL library in lib389
- Ticket 48885 - Fix spec file requires
- Ticket 48884 - Bugfixes for mapped object and new connections
- Ticket 48878 - better style for backend in backend_test.py
- Ticket 48878 - pep8 fixes part 2
- Ticket 48878 - pep8 fixes and fix rpm to build
- Ticket 48853 - Prerelease installer
- Ticket 48820 - Begin to test compatability with py.test3, and the new orm
- Ticket 48434 - Fix for negative tz offsets
- Ticket 48857 - Remove python-krbV from lib389
- Ticket 48820 - Fix tests to ensure they work with the new object types
- Ticket 48820 - Move Encryption and RSA to the new object types
- Ticket 48820 - Proof of concept of orm style mapping of configs and objects
- Ticket 48820 - Clitool rename
- Ticket 48431 - lib389 integrate ldclt
- Ticket 48434 - lib389 logging tools
- Ticket 48796 - add function to remove logs
- Ticket 48771 - lib389 - get ns-slapd version
- Ticket 48830 - Convert lib389 to ip route tools
- Ticket 48763 - backup should run regardless of existing backups.
- Ticket 48434 - lib389 logging tools
- Ticket 48798 - EL6 compat for lib389 tests for DH params
- Ticket 48798 - lib389 add ability to create nss ca and certificate
- Ticket 48433 - Aci linting tools
- Ticket 48791 - format args in server tools
- Ticket 48399 - Helper makefile is missing mkdir dist
- Ticket 48399 - Helper makefile is missing mkdir dist
- Ticket 48794 - lib389 build requires are on a single line
- Ticket 48660 - Add function to convert binary values in an entry to base64
- Ticket 48764 - Fix mit krb password to be random.
- Ticket 48765 - Change default ports for standalone topology
- Ticket 48750 - Clean up logging to improve command experience
- Ticket 48751 - Improve lib389 ldapi support
- Ticket 48399 - Add helper makefile to lib389 to build and install
- Ticket 48661 - Agreement test suite fails at the test_changes case
- Ticket 48407 - Add test coverage module for lib389 repo
- Ticket 48357 - clitools should standarise their args
- Ticket 48560 - Make verbose handling consistent
- Ticket 48419 - getadminport() should not a be a static method
- Ticket 48408 - RFE escaped default suffix for tests
- Ticket 48401 - Revert typecheck
- Ticket 48401 - lib389 Entry hasAttr returs dict instead of false
- Ticket 48390 - RFE Improvements to lib389 monitor features for rest389
- Ticket 48358 - Add new spec file
- Ticket 48371 - weaker host check on localhost.localdomain
- Ticket 58358 - Update spec file with pre-release versioning
- Ticket 48358 - Make Fedora packaging changes to the spec file
- Ticket 48358 - Prepare lib389 for Fedora Packaging
- Ticket 48364 - Fix test failures
- Ticket 48360 - Refactor the delete agreement function
- Ticket 48361 - Expand 389ds monitoring capabilities
- Ticket 48246 - Adding license/copyright to lib389 files
- Ticket 48340 - Add basic monitor support to lib389 https://fedorahosted.org/389/ticket/48340
- Ticket 48353 - Add Replication REST support to lib389
- Ticket 47840 - Fix regression
- Ticket 48343 - lib389 krb5 realm management https://fedorahosted.org/389/ticket/48343
- Ticket 47840 - fix lib389 to use sbin scripts  https://fedorahosted.org/389/ticket/47840
- Ticket 48335 - Add SASL support to lib389
- Ticket 48329 - Fix case-senstive scyheam comparisions
- Ticket 48303 - Fix lib389 broken tests
- Ticket 48329 - add matching rule functions to schema module
- Ticket 48324 - fix boolean capitalisation (one line) https://fedorahosted.org/389/ticket/48324
- Ticket 48321 - Improve is_a_dn check to prevent mistakes with lib389 auth https://fedorahosted.org/389/ticket/48321
- Ticket 48322 - Allow reindex function to reindex all attributes
- Ticket 48319 - Fix ldap.LDAPError exception processing
- Ticket 48318 - Do not delete a changelog while disabling a replication by suffix
- Ticket 48308 - Add __eq__ and __ne__ to Entry to allow fast comparison https://fedorahosted.org/389/ticket/48308
- Ticket 48303 - Fix lib389 broken tests - backend_test
- Ticket 48309 - Fix lib389 lib imports
- Ticket 48303 - Fix lib389 broken tests - agreement_test
- Ticket 48303 - Fix lib389 broken tests - aci_parse_test
- Ticket 48301 - add tox support
- Ticket 48204 - update lib389 for python3
- Ticket 48273 - Improve valgrind functions
- Ticket 48271 - Fix for self.prefix being none when SER_DEPLOYED_DIR is none https://fedorahosted.org/389/ticket/48271
- Ticket 48259 - Add aci parsing utilities to lib389
- Ticket 48252 - (lib389) adding get_bin_dir and dbscan
- Ticket 48247 - Change the default user to 'dirsrv'
- Ticket 47848 - Add new function to create ldif files
- Ticket 48239 - Fix for prefix allocation of un-initialised dirsrv objects
- Ticket 48237 - Add lib389 helper to enable and disable logging services.
- Ticket 48236 - Add get effective rights helper to lib389
- Ticket 48238 - Add objectclass and attribute type query mechanisms
- Ticket 48029 - Add missing replication related functions
- Ticket 48028 - add valgrind wrapper for ns-slapd
- Ticket 48028 - lib389 - add valgrind functions
- Ticket 48022 - lib389 - Add all the server tasks
- Ticket 48023 - create function to test replication between servers
- Ticket 48020 - lib389 - need to reset args_instance with  every DirSrv init
- Ticket 48000 - Repl agmts need more time to stop
- Ticket 48004 - Fix various issues
- Ticket 48000 - replica agreement pause/resume should have a short sleep
- Ticket 47990 - Add check for ".removed" instances when doing an upgrade
- Ticket 47990 - Add "upgrade" function to lib389
- Ticket 47691 - using lib389 with RPMs
- Ticket 47848 - Add support for setuptools.
- Ticket 47855 - Add function to clear tmp directory
- Ticket 47851 - Need to retrieve tmp directory path
- Ticket 47845 - add stripcsn option to tombstone fixup task
- Ticket 47851 - Add function to retrieve dirsrvtests data directory
- Ticket 47845 - Add backup/restore/fixup tombstone tasks to lib389
- Ticket 47819 - Add the new precise tombstone purging config attribute
- Ticket 47695 - Add plugins/tasks/Index
- Ticket 47648 - lib389 - add schema classes, methods
- Ticket 47671 - CI lib389: allow to open a DirSrv without having to create the instance
- Ticket 47600 - Replica/Agreement/Changelog not conform to the design
- Ticket 47652 - replica add fails: MT.list return a list not an entry
- Ticket 47635 - MT/Backend/Suffix to be conform with the design
- Ticket 47625 - CI lib389: DirSrv not conform to the design
- Ticket 47595 - fail to detect/reinit already existing instance/backup
- Ticket 47590 - CI tests: add/split functions around replication
- Ticket 47584 - CI tests: add backup/restore of an instance
- Ticket 47578 - CI tests: removal of 'sudo' and absolute path in lib389
- Ticket 47568 - Rename DSAdmin class
- Ticket 47566 - Initial import of DSadmin into 389-test repos

* Mon Oct 16 2017 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.1-2
- Bump version to 1.4.0.1-2
- Ticket 49400 - Add clang support and libatomic

* Mon Oct 9 2017 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.1-1
- Bump version to 1.4.0.1-1
- Ticket 49038 - remove legacy replication - change cleanup script precedence
- Ticket 49392 - memavailable not available
- Ticket 49235 - pbkdf2 by default
- Ticket 49279 - remove dsktune
- Ticket 49372 - filter optimisation improvements for common queries
- Ticket 49320 - Activating already active role returns error 16
- Ticket 49389 - unable to retrieve specific cosAttribute when subtree password policy is configured
- Ticket 49092 - Add CI test for schema-reload
- Ticket 49388 - repl-monitor - matches null string many times in regex
- Ticket 49387 - pbkdf2 settings were too aggressive
- Ticket 49385 - Fix coverity warnings
- Ticket 49305 - Need to wrap atomic calls
- Ticket 48973 - Indexing a ExactIA5Match attribute with a IgnoreIA5Match matching rule triggers a warning
- Ticket 49378 - server init fails
- Ticket 49305 - Need to wrap atomic calls
- Ticket 49180 - add CI test
- Ticket 49180 - errors log filled with attrlist_replace - attr_replace

* Fri Sep 22 2017 Mark Reynolds <mreynolds@redhat.com> - 1.4.0.0-1
- Bump version to 1.4.0.0-1

