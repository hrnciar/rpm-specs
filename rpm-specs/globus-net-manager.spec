Name:		globus-net-manager
%global _name %(tr - _ <<< %{name})
Version:	1.4
Release:	3%{?dist}
Summary:	Grid Community Toolkit - Network Manager Library

License:	ASL 2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15.27
BuildRequires:	globus-xio-devel >= 5
%if %{?fedora}%{!?fedora:0} >= 30 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	python3-devel
%else
BuildRequires:	python2-devel
%endif
BuildRequires:	doxygen

Requires:	globus-common%{?_isa} >= 15.27

%package devel
Summary:	Grid Community Toolkit - Network Manager Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package -n globus-xio-net-manager-driver
Summary:	Grid Community Toolkit - Globus XIO Network Manager Driver
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	globus-xio%{?_isa} >= 5

%package -n globus-xio-net-manager-driver-devel
Summary:	Grid Community Toolkit - Globus XIO Network Manager Driver Development Files
Requires:	globus-xio-net-manager-driver%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Network Manager Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Network Manager Library

The Globus Neteork Manager Library is a plug-in point for network management
tasks, such as:
 - selectively open ports in a firewall and allow these ports to be closed
   when transfers are complete
 - configure a virtual circuit based on a site policy and route traffic
   over this circuit
 - route network traffic related to a task over a particular network

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Network Manager Library Development Files

%description -n globus-xio-net-manager-driver
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The globus-xio-net-manager-driver package contains:
Globus XIO Network Manager Driver

%description -n globus-xio-net-manager-driver-devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The globus-xio-net-manager-driver-devel package contains:
Globus XIO Network Manager Driver Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Network Manager Library Documentation Files

%prep
%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%if %{?fedora}%{!?fedora:0} >= 30 || %{?rhel}%{!?rhel:0} >= 8
export PYTHON_CONFIG=%{__python3}-config
%else
export PYTHON_CONFIG=%{__python2}-config
%endif

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --enable-python

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

%check
GLOBUS_HOSTNAME=localhost make %{?_smp_mflags} check VERBOSE=1

%ldconfig_scriptlets

%ldconfig_scriptlets -n globus-xio-net-manager-driver

%files
%{_libdir}/libglobus_net_manager.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%{!?_licensedir: %doc %{_pkgdocdir}/GLOBUS_LICENSE}
%{?_licensedir: %license GLOBUS_LICENSE}

%files devel
%{_includedir}/globus/globus_net_manager.h
%{_includedir}/globus/globus_net_manager_attr.h
%{_libdir}/libglobus_net_manager.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n globus-xio-net-manager-driver
# This is a loadable module (plugin)
%{_libdir}/libglobus_xio_net_manager_driver.so

%files -n globus-xio-net-manager-driver-devel
%{_includedir}/globus/globus_xio_net_manager_driver.h
%{_libdir}/pkgconfig/globus-xio-net-manager-driver.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%{!?_licensedir: %doc %{_pkgdocdir}/GLOBUS_LICENSE}
%{?_licensedir: %license GLOBUS_LICENSE}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.4-1
- Check python-config for --embed flag (python 3.8 compatibility)
- Drop patch globus-net-manager-python-embed.patch

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3-2
- Check python-config for --embed flag (python 3.8 compatibility)

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3-1
- Doxygen fixes (1.2)
- Python 3 support (1.3)
- Build using Python 3 for Fedora 30+
- Enable checks

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.1-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (1.0)
- Merge GT6 update 0.18 into GCT (1.1)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.18-1
- GT6 update: Fix pre-connect not using changed remote contact

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.17-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.17-1
- GT6 update: Fix .pc typo
- Drop patch globus-net-manager-pkgconfig.patch (fixed upstream)

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.16-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section
- Fix misspelled dependency in pkgconfig file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.16-1
- GT 6 update: Exclude tests from doc

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.15-1
- GT6 update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.14-1
- GT6 update (pre_connect return attrs get set on attr, not handle)

* Tue Nov 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.13-1
- GT6 update (Remove unused code)

* Mon Jul 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.12-1
- GT6 update (Fix memory leaks, NULL pointer derefs, and dead assignments)

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.10-1
- GT6 update (Fix uninitialized value, Remove unused variables)

* Sat Jun 20 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.9-1
- GT6 update (cleanups)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.8-1
- GT6 update (fix for attr not being used on connect)

* Mon Mar 30 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.7-1
- GT6 update (add file parameter to logging driver to set a file to log to)

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-2
- Implement updated license packaging guidelines

* Thu Jan 15 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-1
- GT6 update (test enhancements)
- Extend package description

* Thu Jan 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2-1
- Initial packaging
