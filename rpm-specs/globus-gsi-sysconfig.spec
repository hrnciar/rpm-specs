Name:		globus-gsi-sysconfig
%global _name %(tr - _ <<< %{name})
Version:	9.2
Release:	4%{?dist}
Summary:	Grid Community Toolkit - Globus GSI System Config Library

License:	ASL 2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-openssl-module-devel >= 3
BuildRequires:	globus-gsi-openssl-error-devel >= 2
BuildRequires:	openssl-devel
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	perl(Test::More)

%package devel
Summary:	Grid Community Toolkit - Globus GSI System Config Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Globus GSI System Config Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus GSI System Config Library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus GSI System Config Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus GSI System Config Library Documentation Files

%prep
%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir if licensedir is used
%{?_licensedir: rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE}

# Create config directory
mkdir -p %{buildroot}%{_sysconfdir}/grid-security

%check
make %{?_smp_mflags} check VERBOSE=1

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_gsi_sysconfig.so.*
%dir %{_sysconfdir}/grid-security
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%{!?_licensedir: %doc %{_pkgdocdir}/GLOBUS_LICENSE}
%{?_licensedir: %license GLOBUS_LICENSE}

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gsi_sysconfig.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%{!?_licensedir: %doc %{_pkgdocdir}/GLOBUS_LICENSE}
%{?_licensedir: %license GLOBUS_LICENSE}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 07 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.2-3
- Don't package /etc/grid-security/certificates

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.2-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 9.1-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (9.0)
  - Skip homedir test if directory does not exist
- Correct bitshift direction in perl test file (9.1)

* Thu Aug 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.1-3
- Package /etc/grid-security/certificates

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.1-1
- GT6 update: Fix typo in windows function name

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.0-1
- GT6 update: Add cert and key checks based on different uid

* Sat Sep 09 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 7.1-1
- GT6 update: Add SNI vhost cred dir support
- Enable checks

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.11-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Drop the globus-gsi-sysconfig-openssl098.patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.11-1
- GT6 update

* Thu Oct 13 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10-2
- Rebuild for openssl 1.1.0 (Fedora 26)

* Thu Sep 01 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.10-1
- GT6 update: Updates for OpenSSL 1.1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.9-1
- GT6 update

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.8-2
- Implement updated license packaging guidelines

* Mon Oct 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.8-1
- GT6 update
- Drop patch globus-gsi-sysconfig-doxygen.patch (fixed upstream)

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 6.7-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Brent Baude <baude@us.ibm.com> - 5.3-9
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Dec 05 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-8
- Remove directory man page

* Fri Oct 25 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-7
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-5
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-4
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-2
- Add build requires for TexLive 2012

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-1
- Update to Globus Toolkit 5.2.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2-1
- Update to Globus Toolkit 5.2.1
- Drop patches globus-gsi-sysconfig-deps.patch and
  globus-gsi-sysconfig-doxygen.patch (fixed upstream)

* Mon Jan 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1-2
- Fix broken links in README file

* Tue Dec 13 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1-1
- Update to Globus Toolkit 5.2.0
- Drop patch globus-gsi-sysconfig-mingw.patch (fixed upstream)

* Fri Jun 03 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-1
- Update to Globus Toolkit 5.0.4
- Drop patch globus-gsi-sysconfig-zero-size-dir.patch (fixed upstream)

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1-4
- Add README file

* Tue Mar 29 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1-3
- Allow zero-size dirs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1-1
- Update to Globus Toolkit 5.0.1
- Drop patch globus-gsi-sysconfig-doxygen.patch (fixed upstream)

* Fri Jan 22 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0-1
- Update to Globus Toolkit 5.0.0

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.2-4
- rebuilt with new openssl

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-3
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Wed Jun 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-2
- Update to official Fedora Globus packaging guidelines

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages
- Put GLOBUS_LICENSE file in extracted source tarball

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-0.3
- Adapt to updated GPT package

* Tue Oct 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1-0.1
- Autogenerated
