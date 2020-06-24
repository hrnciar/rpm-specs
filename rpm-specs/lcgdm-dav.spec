%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}

Name:		lcgdm-dav
Version:	0.22.0
Release:	5%{?dist}
Summary:	HTTP/DAV front end to the DPM/LFC services
License:	ASL 2.0
URL:		https://svnweb.cern.ch/trac/lcgdm
# The source of this package was pulled from upstream's vcs. Use the
# following commands to generate the tarball:
# git clone https://gitlab.cern.ch/lcgdm/lcgdm-dav.git --depth 1 --branch master lcgdm-dav-0.22.0
# pushd lcgdm-dav-0.22.0
# git checkout lcgdm-dav_0_22_0b
# popd
# tar czf lcgdm-dav-0.22.0.tar.gz lcgdm-dav-0.22.0 --exclude-vcs
Source0:	%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:	cmake3
BuildRequires:	dmlite-devel >= 1.11.0
BuildRequires:	gridsite-devel
BuildRequires:	gsoap-devel
BuildRequires:	httpd-devel
BuildRequires:	json-c-devel
BuildRequires:	openssl-devel
BuildRequires:	subversion
BuildRequires:  libbsd-devel
BuildRequires:  gcc

Provides:	DPM-httpd-client = 1.2.1-6
Obsoletes:	DPM-httpd-client <= 1.2.1-5

%description
This package provides the HTTP/DAV front end to the LCGDM components 
(DPM and LFC).

The Disk Pool Manager (DPM) is a lightweight grid storage component, allowing
access to data using commonly used grid protocols. The LCG File Catalog (LFC)
is the main catalog being used by grid communities for both file bookkeeping
and meta-data.

%package libs
Summary:	Common libraries for the lcgdm-dav

%description libs
The lcgdm-dav specific client common libraries, with support for multiple
stream transfers, certificate delegation, among other features.

%package devel
Summary:	Development libraries and headers for lcgdm-dav
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The lcgdm-dav development libraries and headers, with support for multiple
stream transfers, certificate delegation, among other features.

%package -n mod_lcgdm_dav
Summary:    Apache modules built on top of dmlite providing DAV access.
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
Requires:   httpd%{?_isa}
Requires:   httpd-mmn = %{_httpd_mmn}

%description -n mod_lcgdm_dav
Apache modules built on top of dmlite providing DAV access.

%package server
Summary:	HTTP/DAV front end to the DPM and LFC services
Provides:	DPM-httpd = 1.2.2-5
Obsoletes:	DPM-httpd <= 1.2.2-4
Provides:	DPM-httpd-cgi = 1.3.2-7
Obsoletes:	DPM-httpd-cgi <= 1.3.2-6
Provides:	mod_dpmput = 1.2.1-5
Obsoletes:	mod_dpmput <= 1.2.1-4
Requires:	gridsite%{?_isa} >= 1.7
Requires:	httpd%{?_isa}
Requires:	httpd-mmn = %{_httpd_mmn}
Requires:	mod_ssl%{?_isa}
Requires:	mod_lcgdm_dav%{?_isa} = %{version}-%{release}
Requires:	dmlite-libs%{?_isa} >= 1.11.0

%description server
The lcgdm-dav server package providing the HTTP and DAV front end to the LCGDM
(DPM and LFC) services.

%prep
%setup -q

%build
./buildcurl.sh
%cmake3 . -DCMAKE_INSTALL_PREFIX=/

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%ldconfig_scriptlets libs

%files
%{_bindir}/htcopy
%{_mandir}/man1/htcopy.1*
%doc src/client/README LICENSE

%files libs
%{_libdir}/liblcgdmhtext.so.*
%{_libdir}/libmacaroons.so*
%doc README LICENSE

%files devel
%{_includedir}/lcgdm-dav
%{_libdir}/liblcgdmhtext.so

%files -n mod_lcgdm_dav
%{_libdir}/httpd/modules/mod_lcgdm_ns.so
%{_libdir}/httpd/modules/mod_lcgdm_disk.so
%{_libdir}/httpd/modules/mod_lcgdm_dav.so
%{_datadir}/%{name}/*

%files server
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%config(noreplace) %{_sysconfdir}/cron.d/*

%changelog
* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 0.22.0-5
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Oliver Keeble <oliver.keeble@cern.ch> - 0.22.0
- New upstream release, rebuild for dmlite 1.11.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Björn Esser <besser82@fedoraproject.org> - 0.20.0-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1) on fc28

* Wed Mar 07 2018 Oliver Keeble <oliver.keeble@cern.ch> - 0.20.0-1
- New upstream release

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.19.0-4
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 0.19.0-2
- Rebuilt for libjson-c.so.3

* Tue Sep 19 2017 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.19.0-1
- New upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Andrea Manzi <amanzi@cern.ch> - 0.18.2-2
- Rebuild for gsoap 2.8.48 (Fedora 27)

* Tue May 30 2017 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.18.2-1
- New upstream release

* Tue May 09 2017 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.18.1-4
- Patch an uninitialized buffer

* Wed Apr 19 2017 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.18.1-3
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.18.0-1
- New upstream release

* Wed May 04 2016 Andrea Manzi <amanzi@cern.ch> - 0.17.1-3
- Rebuild for gsoap 2.8.30 (Fedora 25)

* Fri Mar 11 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.17.1-2
- Split lcgdm-dav-server + mod_lcgdm_dav

* Wed Mar 09 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.17.1-1
- New upstream release

* Tue Feb 02 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.16.0-3
- Rebuilt for gsoap 2.8.28

* Tue Dec 01 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.16.0-2
- Add missing files

* Thu Jul 23 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.16.0-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.15.1-2
- Rebuilt for gsoap 2.8.21

* Mon Oct 13 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.15.1-1
- New upstream release

* Fri Sep 26 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.15.0-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 0.14.1-6
- Patch for building against json-c-0.12-2 

* Fri Jul 25 2014 Adrien Devresse <adevress at cern.ch> - 0.14.1-5
- Rebuilt for libjson update 

* Mon Jul 14 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.14.1-3
- Rebuilt for gsoap 2.8.17

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Alejandro Alvarez <aalvarez@cern.ch> - 0.14.1-2
- Upstream patch: fix for mod_lcgdm_disk context leaking

* Wed Mar 12 2014 Alejandro Alvarez <aalvarez@cern.ch> - 0.14.1-1
- Update for upstream release 0.14.1 

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 0.13.0-4
- fix _httpd_mmn expansion in absence of httpd-devel

* Thu Oct 17 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.13.0-3
- Rebuilt for updated gsoap dependencies

* Mon Sep 23 2013 Adrien Devresse <adevress at cern.ch>  - 0.13.0-2
 - Rebuilt for gridsite 2.0 release

* Thu Sep 19 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.13.0-1
- Update for new upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.12.2-1
- Update for new upstream release

* Tue Mar 05 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.12.1-2
- Upstream patch: mod_lcgdm_disk url-decodes received parameters

* Fri Feb 08 2013 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.12.1-1
- Update for new upstream release (patch for segfault)

* Wed Feb 06 2013 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.12.0-1
- Update for new upstream release

* Tue Jan 29 2013 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.11.0-2
- Added patch for apache 2.4 api change

* Wed Nov 14 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.11.0-1
- Update for new upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.8.0-1
- Update for new upstream release
- Added build dependencies on json-c-devel and neon-devel
- Added provides/requires for compatibility with gLite packaging

* Fri Mar 30 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.7.0-2
- Update for httpd-mmn

* Fri Mar 16 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.7.0-1
- Update for new upstream release
- Added dependency on httpd-mmn for lcgdm-dav-server (bug #803063)

* Fri Feb 10 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.5.4-3
- Rebuilt for updated gsoap dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.5.4-1
- Removed -server scriptlets (other httpd modules do not provide them)
- Renamed lcgdm-dav.conf to zlcgdm-dav.conf to fix load order

* Thu Dec 08 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.5.3-1
- Removed useless BuildRequires from -devel package
- Updated scriplets to reload httpd
- Update for upstream patch release (gives own dir for static files)

* Mon Dec 05 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.5.2-1
- Dropped init scripts (use the standard httpd ones instead)
- Dropped ldconfig from -devel scriptlets
- Added dependency on mod_ssl for server package
- Added man page for htcopy tool
- Update for upstream patch release

* Mon Nov 07 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.5.1-1
- Fixed issue with CFLAGS not being taken into account
 
* Fri Nov 04 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.5.0-2
- Added proper details on tarball generation
- svn module renamed upstream from dpm-webdav to lcgdm-dav
- Removed useless BuildRequires
- Optional BuildRequires for curl-devel (name changed to libcurl-devel in >EL5)
- Removed useless Requires on libs package
- Removed doc entries from sub-packages
- Relocate init script to initrddir

* Mon Oct 17 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.5.0-1
- Initial build
