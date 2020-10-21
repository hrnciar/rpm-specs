%global __cmake_in_source_build 1
%global         short_name gsad

#Name not same as upstream package to match the naming convention of the OpenVAS suite
Name:           openvas-gsa
Version:        9.0.1
Release:        5%{?dist}
Summary:        Greenbone Security Assistant (GSA) is GUI to the OpenVAS

License:        GPLv2+
URL:            http://www.openvas.org
Source0:        https://github.com/greenbone/gsa/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/greenbone/gsa/releases/download/v%{version}/gsa-%{version}.tar.gz.sig#/%{name}-%{version}.tar.gz.sig

# The authenticator public key obtained from release 9.0.1
# gpg2 -vv openvas-gsa-9.0.1.tar.gz.sig
# gpg2 --search-key 9823FAA60ED1E580
# wget https://www.greenbone.net/GBCommunitySigningKey.asc
# gpg2 --import GBCommunitySigningKey.asc
# gpg2 --list-public-keys 9823FAA60ED1E580
# gpg2 --export --export-options export-minimal 8AE4BE429B60A59B311C2E739823FAA60ED1E580 > gpgkey-8AE4BE429B60A59B311C2E739823FAA60ED1E580.gpg
Source2:        gpgkey-8AE4BE429B60A59B311C2E739823FAA60ED1E580.gpg

Source3:        %{name}.logrotate
Source4:        %{name}.sysconfig


%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
Source5:        %{name}.service
%else
Source6:        %{name}.initd
%endif

Source7:        %{name}.yarnrc
# we create the offlinecache:
# cd gsa
# nodejs-yarn config set yarn-offline-mirror /tmp/npm-packages-offline-cache
# nodejs-yarn install
# cd /tmp
# tar -zcvf openvas-gsa-yarn-offline.tar.gz npm-packages-offline-cache
Source8:        %{name}-yarn-offline.tar.gz


# Put certs to /etc/pki as suggested by http://fedoraproject.org/wiki/PackagingDrafts/Certificates
# Not reported upstream as it is RedHat/Fedora specific
Patch1:         %{name}-pki.patch
#Patch3:         %{name}-polib.patch
Patch4:         %{name}-doxygen_full.patch
#Patch5:         %{name}-strncpy.patch
Patch6:		%{name}-strsignal.patch

BuildRequires:  gcc
BuildRequires:  openvas-libraries-devel >= 7.0
BuildRequires:  cmake >= 2.6.0
BuildRequires:  glib2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libxslt-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  doxygen
BuildRequires:  xmltoman
BuildRequires:  gpgme-devel
BuildRequires:  gettext
BuildRequires:  python3-polib
BuildRequires:  nodejs
BuildRequires:  yarnpkg

Requires:       logrotate
Requires:       texlive-changepage
Requires:       texlive-comment

%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
BuildRequires:          systemd
Requires(post):         systemd
Requires(preun):        systemd
Requires(postun):       systemd
%else
Requires(post):         chkconfig
Requires(preun):        chkconfig
Requires(preun):        initscripts
%endif

%description
The Greenbone Security Assistant (GSA) is a lean web service offering a user
web interface for the Open Vulnerability Assessment System (OpenVAS).
The GSA uses XSL transformation style-sheets that converts OMP responses
from the OpenVAS infrastructure into presentable HTML.

%package doc
Summary:        Development documentation for %{name}
BuildRequires:  graphviz

%description doc
You can find documentation for development of %{name} under file://%{_docdir}/%{name}-doc.
It can be used with a Browser.

%prep
#check signature
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}

%setup -q -n gsa-%{version}
%patch1 -p1 -b .pki
#%patch3 -p1 -b .polib
%patch4 -p1 -b .doxyfull
#%patch5 -p2 -b .strncpy
%patch6 -p1 -b .strsignal
tar -C .. -zxvf %{SOURCE8}

#Fix encoding issues
#iconv -f Windows-1250 -t utf-8 < CHANGES > CHANGES.utf8
#touch -r CHANGES CHANGES.utf8
#mv CHANGES.utf8 CHANGES
#iconv -f Windows-1250 -t utf-8 < ChangeLog > ChangeLog.utf8
#touch -r ChangeLog ChangeLog.utf8
#mv ChangeLog.utf8 ChangeLog


%build
export CFLAGS="$RPM_OPT_FLAGS -Werror=unused-but-set-variable -lgpg-error -Wno-error=deprecated-declarations"
cp %{SOURCE7} gsa/.yarnrc
%cmake -DLOCALSTATEDIR:PATH=%{_var} -DSYSCONFDIR:PATH=/etc/ -DYARN_OFFLINE=1 -DLOGROTATE_DIR:PATH=/etc/logrotate.d/ -DDEFAULT_CONFIG_DIR:PATH=/etc/sysconfig/ .
make %{?_smp_mflags} VERBOSE=1
make doc-full

%install
%make_install

# Config directory
mkdir -p %{buildroot}/%{_sysconfdir}/openvas
chmod 755 %{buildroot}/%{_sysconfdir}/openvas

# Log directory
mkdir -p %{buildroot}/%{_var}/log/openvas
touch %{buildroot}%{_var}/log/openvas/%{name}.log

# Install log rotation stuff
install -m 644 -Dp %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{short_name}

# Install sysconfig configration
install -Dp -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
# Install systemd
install -Dp -m 644 %{SOURCE5} %{buildroot}/%{_unitdir}/%{name}.service
%else
# Install startup script
install -Dp -m 755 %{SOURCE6} %{buildroot}/%{_initddir}/%{name}
%endif

#remove some files
rm -f %{buildroot}/%{_sysconfdir}/sysconfig/%{short_name} 
rm -f %{buildroot}/%{_sysconfdir}/logrotate.d/%{short_name}
rm -f %{buildroot}/%{_unitdir}/%{short_name}.service

%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%else
#Post scripts for systemv initd
%post
# This adds the proper /etc/rc*.d links for the script
if [ "$1" -eq 1 ] ; then
        /sbin/chkconfig --add openvas-gsa
fi

%preun
if [ "$1" -eq 0 ] ; then
        /sbin/service openvas-gsa stop >/dev/null 2>&1
        /sbin/chkconfig --del openvas-gsa
fi

%postun
# only for upgrades not erasure
if [ "$1" -eq 1 ] ; then
        /sbin/service openvas-gsa condrestart  >/dev/null 2>&1
fi
%endif


%files
# -f gsad_xsl.lang
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md INSTALL.md CHANGELOG.md RELEASE.md
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/gvm/%{short_name}_log.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/gvm
%dir %{_datadir}/gvm
%dir %{_datadir}/gvm/%{short_name}
%{_sbindir}/%{short_name}
%{_mandir}/man8/%{short_name}.8*
%{_datadir}/gvm/%{short_name}/
%dir %{_localstatedir}/log/gvm/
%ghost %{_localstatedir}/log/gvm/%{short_name}.log

%if 0%{?rhel} >= 7 || 0%{?fedora} > 15
%{_unitdir}/%{name}.service
%else
%{_initrddir}/%{name}
%endif

%files doc
%doc gsad/doc/generated/*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jeff Law <law@redhat.com> - 9.0.1-3
- Use strsignal not sys_siglist
- Use __cmake_in_source_build 1

* Sat May 30 2020 josef radinger <cheese@nosuchhost.net> - 9.0.1-2
- remove /etc/openvas/
- /var/log/gvm/gsad.log instead of /var/log/openvas/openvas.log
- use new name in logrotate

* Sat May 23 2020 josef radinger <cheese@nosuchhost.net> - 9.0.1-1
- bump version
- remove patch2
- remove patch3
- update patch4
- remove patch5
- add gpg-check
- reorder sources
- no more CHANGES
- README.md -> README and several other filoes now in %%doc
- BuildRequires on nodejs and yarnpkg
- add offline yarn-cache with needed packages
- use -DYARN_OFFLINE=1
- remove -f gsad_xsl.lang
- LICENSE instead of COPYING
- files-section: gvm instead of openvas
- add to cmake: DEFAULT_CONFIG_DIR and LOGROTATE_DIR
- move docs
- remove errornous files
- specfile-cleanup

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Fabian Affolter <mail@fabian-affolter.ch> - 8.0.0-1
- Update to latest upstream version 8.0.0 (rhbz#1592943)

* Wed Feb 27 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-10
- rebuild against new libraries

* Tue Feb 05 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-9
- fix patch5

* Tue Feb 05 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-8
- rename unreleased subpackage developerdocs to doc
- fix Werror=stringop-truncation with patch5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-6
- split development-docs into subpackage developerdocs

* Sun Jan 27 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-5
- add graphviz to BuildRequires
- add development-docs into %%doc-dir
- add openvas-gsa-doxygen_full.patch

* Sun Jan 27 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-4
- add patch2 (fix for french translation)
- add patch3 to disable non-working check for polib
- add . to cmake 

* Fri Jan 18 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-3
- fresh build

* Fri Jan 18 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-2
- switch to python3 explicitly in buildrequires
- fix date in changelog

* Fri Jan 11 2019 josef radinger <cheese@nosuchhost.net> - 7.0.3-1
- bump version
- new openvas-libraries
- new source-url
- no more Changelog
- cleanup specfile

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 7.0.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Michal Ambroz <rebus at, seznam.cz> - 7.0.2-2
- fix build dependencies to include python for po files

* Sun Apr 23 2017 Michal Ambroz <rebus at, seznam.cz> - 7.0.2-1
- bump to OpenVas-9 version 7.0.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.11-1
- bump to OpenVas-8 version 6.0.11

* Fri Apr 29 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.10-3
- sync releases

* Fri Apr 29 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.10-1
- bump to OpenVas-8 version 6.0.10

* Thu Feb 25 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.9-4
- added compatibility definition for EPEL7 MHD version <= 0.9.33

* Thu Feb 25 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.9-3
- patch obsolete libmicrohttpd API for MHD_HTTP_METHOD_NOT_ACCEPTABLE 

* Wed Feb 24 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.9-2
- patch obsolete libmicrohttpd API for MHD_create_response_from_data

* Tue Feb 23 2016 Michal Ambroz <rebus at, seznam.cz> - 6.0.9-1
- bump to OpenVas-8 version 6.0.9

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 05 2015 Kalev Lember <klember@redhat.com> - 6.0.6-3
- Rebuilt for libmicrohttpd soname bump

* Sun Oct 04 2015 josef radinger <cheese@nosuchhost.net> - 6.0.6-2
- add Requires on texlive-comment and texlive-changepage

* Tue Sep 29 2015 josef radinger <cheese@nosuchhost.net> - 6.0.6-1
- bump version

* Sat Aug 22 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.5-1
- bump to OpenVas-8 version 6.0.5
- 1254456 - fix logrotate script

* Wed Jul 15 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.4-1
- bump to OpenVas-8 version 6.0.4

* Wed Jun 24 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.3-4
- import to Fedora repository

* Wed Jun 17 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.3-3
- changes from package review

* Wed Jun 17 2015 Michal Ambroz <rebus at, seznam.cz> - 6.0.3-1
- bump to OpenVas-8 version 6.0.3

* Tue Nov 04 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.4-2
- remove sysvinit support
- add setgroups patch as noted by the rpmlint
- fixed encoding problems for the changelogs
- marked logrotate script as config

* Tue Nov 04 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.4-1
- bump to OpenVas-7 version 5.0.4

* Tue Sep 16 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.3-1
- bump to OpenVas-7 version 5.0.3

* Tue Sep 02 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.2-1
- bump to OpenVas-7 version 5.0.2

* Tue Jun 17 2014 Michal Ambroz <rebus at, seznam.cz> - 5.0.1-1
- initial build of OpenVas-7 version 5.0.1

