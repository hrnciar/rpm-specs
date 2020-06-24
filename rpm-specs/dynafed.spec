%if %{?fedora}%{!?fedora:0} >= 17 || %{?rhel}%{!?rhel:0} >= 7
%global boost_cmake_flags -DBOOST_INCLUDEDIR=/usr/include
%else
%global boost_cmake_flags -DBOOST_INCLUDEDIR=/usr/include/boost148 -DBOOST_LIBRARYDIR=%{_libdir}/boost148
%endif

%if %{?fedora}%{!?fedora:0} >= 17 || %{?rhel}%{!?rhel:0} >= 7
%global systemd 1
%else
%global systemd 0
%endif

%if %{?fedora}%{!?fedora:0} >=31
%global buildauthplugin 0
%else
%global buildauthplugin 1
%endif

%define _unpackaged_files_terminate_build 0

Name:				dynafed
Version:			1.5.1
Release:			3%{?dist}
Summary:			Ultra-scalable dynamic system for federating HTTP-based storage resources
License:			ASL 2.0
URL:				http://lcgdm.web.cern.ch/dynafed-dynamic-federation-project
# git clone http://gitlab.cern.ch/lcgdm/dynafed.git
# cd dynafed && git archive --prefix dynafed-1.5.0/ tags/dynafed_1_5_0a  | gzip > dynafed-1.5.0.tar.gz
Source0:			http://grid-deployment.web.cern.ch/grid-deployment/dms/lcgutil/tar/%{name}/%{name}-%{version}.tar.gz

%if %{?fedora}%{!?fedora:0} >= 17 || %{?rhel}%{!?rhel:0} >= 7
BuildRequires:  gcc-c++
BuildRequires:  boost-devel >= 1.48.0
%else
BuildRequires:  boost148-devel >= 1.48.0
%endif

BuildRequires:  cmake
BuildRequires:  dmlite-devel >= 1.13.0
BuildRequires:  dmlite-private-devel  >= 1.13.0
BuildRequires:  davix-devel >= 0.6.2
BuildRequires:  gfal2-devel
BuildRequires:  GeoIP-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libmemcached-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
%if %{?fedora}%{!?fedora:0} >=31
# Python 3 and no lcgdm
BuildRequires:  python3
BuildRequires:  python3-devel
%else
BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  lfc-devel >= 1.8.8
%endif

%if %systemd
# possible deps to configure the journal for practical logging
%else
Requires:		rsyslog
%endif


%description
The Dynafed project provides a dynamic, scalable HTTP resource
federation mechanism for distributed storage systems.
It supports backends exposing HTTP, WebDAV, S3, Azure as
access protocols. In the S3 and Azure case it hides the secret
keys and exploits pre-signed URLs.
The default deployment style is accessible by any HTTP/Webdav
compatible client. The core components can be used to design
frontends based on other protocols.

%package private-devel
Summary:			Development files for %{name}
Requires:			%{name}%{?_isa} = %{version}-%{release}
Requires:			pkgconfig

%description private-devel
Headers files for %{name}'s plugin development.

%package http-plugin
Summary:			Http and WebDav plugin for %{name}
Requires:			%{name}%{?_isa} = %{version}-%{release}
Requires:			davix-libs >= 0.5.1
Provides:                       %{name}-dav-plugin = %{version}-%{release}

%description http-plugin
Plugin for the WebDav based storage system for %{name}

%if %{?fedora}%{!?fedora:0} <=30
%package lfc-plugin
Summary:			Logical File catalog (LFC) plugin for %{name}
Requires:			%{name}%{?_isa} = %{version}-%{release}
Requires:			gfal2-plugin-lfc%{?_isa}

%description lfc-plugin
Plugin for the Logical File catalog system for %{name}

%files lfc-plugin
%{_libdir}/ugr/libugrlocplugin_lfc.so
%endif

%package dmlite-plugin
Summary:                        dmlite plugin for %{name}
Requires:                       %{name}%{?_isa} = %{version}-%{release}
Requires:                       dmlite-libs%{?_isa} >= 1.13.0

%description dmlite-plugin
Plugin for using dmlite for %{name}

%package tpc-gfal2
Summary:                        Third party copy (TPC) scripts using gfal2 for %{name}
Requires:                       %{name}%{?_isa} = %{version}-%{release}
Requires:                       gfal2-all%{?_isa} >= 2.16.0
Requires:                       davix%{?_isa} >= 0.7.0

%description tpc-gfal2
Scripts that implement the cross-protocol third party copy (TPC) using gfal2

%package dmlite-frontend
Summary:                        dmlite plugin for %{name}
Requires:                       %{name}%{?_isa} = %{version}-%{release}
Requires:                       dmlite-apache-httpd >= 1.13.0
Requires:                       dmlite-libs%{?_isa} >= 1.13.0
%if %systemd == 0
Requires:                       mod_proxy_fcgi
%endif
Requires:                       php-fpm
Requires:                       php-pecl-memcache

%description dmlite-frontend
Webdav frontend for %{name} using dmlite and lcgdm-dav



%clean
rm -rf %{buildroot};
make clean

%prep
%setup -q

%build
%if %systemd
%global systemd_cmake_flags -DRSYSLOG_SUPPORT=FALSE -DLOGROTATE_SUPPORT=FALSE
%else
%global systemd_cmake_flags -DRSYSLOG_SUPPORT=TRUE -DLOGROTATE_SUPPORT=TRUE
%endif

%if %buildauthplugin
%global authplug_cmake_flags -DAUTHPYTHON_PLUGIN=TRUE
%else
%global authplug_cmake_flags -DAUTHPYTHON_PLUGIN=FALSE
%endif

%cmake \
-DDOC_INSTALL_DIR=%{_docdir}/%{name}-%{version} \
-DAPACHE_SITES_INSTALL_DIR=%{_sysconfdir}/httpd/conf.d \
-DOUT_OF_SOURCE_CHECK=FALSE \
%{systemd_cmake_flags} \
%{boost_cmake_flags} \
%{authplug_cmake_flags} \
.
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%post
/sbin/ldconfig
/sbin/service rsyslog condrestart || true
## conf file plugin path transition
## sed -i 's@/usr/lib\([0-9]*\)/ugr@/usr/lib\1/dynafed@g' /etc/ugr.conf || true

%postun
/sbin/ldconfig

%post dmlite-frontend
/sbin/ldconfig
/sbin/service rsyslog condrestart || true
/sbin/service httpd condrestart  || true

%files
%{_libdir}/libugrconnector.so.*
%{_libdir}/ugr/libugrgeoplugin_geoip.so
%{_libdir}/ugr/libugrgeoplugin_mmdb.so
%{_libdir}/ugr/libugrnoloopplugin.so
%config(noreplace) %{_sysconfdir}/ugr/ugr.conf
%config(noreplace) %{_sysconfdir}/ugr/conf.d/*
%if %systemd
# possible config to configure the journal for practical logging
%else
%config(noreplace) %{_sysconfdir}/rsyslog.d/*
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%endif
%doc RELEASE-NOTES
%doc doc/whitepaper/Doc_DynaFeds.pdf
%if %buildauthplugin
%{_libdir}/ugr/libugrauthplugin_python*.so
%endif

%files private-devel
%{_libdir}/libugrconnector.so
%dir %{_includedir}/ugr
%{_includedir}/ugr/*
%{_libdir}/pkgconfig/*

%files http-plugin
%{_libdir}/ugr/libugrlocplugin_dav.so
%{_libdir}/ugr/libugrlocplugin_http.so
%{_libdir}/ugr/libugrlocplugin_s3.so
%{_libdir}/ugr/libugrlocplugin_azure.so
%{_libdir}/ugr/libugrlocplugin_davrucio.so
%config(noreplace) %{_libexecdir}/ugr/ugrextchecksum.sh


%files dmlite-plugin
%defattr (-,root,root)
%attr (-,root,root)
%{_libdir}/ugr/libugrlocplugin_dmliteclient.so
%config(noreplace) %{_sysconfdir}/ugr/ugrdmliteclientORA.conf
%config(noreplace) %{_sysconfdir}/ugr/ugrdmliteclientMY.conf

%files tpc-gfal2
%defattr (-,root,root)
%attr (-,root,root)
%config(noreplace) %{_libexecdir}/ugr/ugrpullscript_gfal.sh
%config(noreplace) %{_libexecdir}/ugr/ugrpushscript_gfal.sh

%files dmlite-frontend
%defattr (-,root,root)
%{_libdir}/ugr/libugrdmlite.so
%config(noreplace) %{_sysconfdir}/ugr/ugrdmlite.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/zlcgdm-ugr-dav.conf
/var/www/html/dashboard/*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.5.1-2
- Rebuild for protobuf 3.11

* Fri Nov 01 2019 Oliver Keeble <oliver.keeble@cern.ch> - 1.5.1-1
- Remove LFC and python2 on fedora >= 31

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Andrea Manzi <andrea.manzi@cern.ch> - 1.5.0-1
- Upstream 1.5.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 1.4.0-2
- Rebuilt for Boost 1.69

* Thu Dec 06 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.4.0-1
- Upstream 1.4.0

* Fri Nov 30 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.3.3-1
- Upstream 1.3.3

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.2-3
- Rebuild for protobuf 3.6

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 11 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.3.2-1
- New upstream release

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.1-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.3.1-8
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-7
- Rebuild for protobuf 3.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.3.1-3
- Rebuilt for Boost 1.64

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.3.1-2
- Rebuild for protobuf 3.3.1

* Tue May 30 2017 Andrea Manzi <amanzi at cern.ch> - 1.3.1-1
 - new upstream  release

* Wed Apr 12 2017 Andrea Manzi <amanzi at cern.ch> - 1.3.0-1
 - new upstream release

* Tue Mar 14 2017 Andrea Manzi <amanzi at cern.ch> - 1.2.5-1
 - new bug fix release

* Tue Feb 21 2017 Andrea Manzi <amanzi at cern.ch> - 1.2.4-1
 - new bug fix release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-4
- Rebuild for protobuf 3.2.0

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-3
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.3-2
- Rebuild for protobuf 3.1.0

* Wed Oct 26 2016 Fabrizio Furano <furano at cern.ch> - 1.2.3-1
 - new bug fix release
* Fri Jul 01 2016 Fabrizio Furano <furano at cern.ch> - 1.2.2-2
 - fixing dependency issue in EL7 and F25
* Wed May 18 2016 Fabrizio Furano <furano at cern.ch> - 1.2.1-1
 - Little packaging fixes for inclusion into EPEL
* Fri Jun 01 2012 Adrien Devresse <adevress at cern.ch> - 0.0.2-0.1-2012052812snap
 - initial draft
