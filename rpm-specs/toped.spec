# Features in Fedora/Free Electronic Lab
#  What else does this build do aside compiling toped ?
#    -  Sets global variable
# Chitlesh Goorah

#
## To download development trunk
#
# svn checkout http://toped.googlecode.com/svn/trunk/ toped-0.9.80
# tar cjf ~/rpmbuild/SOURCES/toped-0.9.80.2137svn.tar.bz2 toped-0.9.80

# Toggle the following declaration when using version controlled snapshots
%define devel 0

# Known bug reports not treated by this SPEC:
#                         10 December 2011
# TGC#117: toped crashed/freezes while editing the line      - svn2013 - filed by FEL

Name:           toped
Version:        0.9.81
Release:        27.svn2211%{?dist}
Summary:        VLSI IC Layout Editor

License:        GPLv2
URL:            http://www.toped.org.uk


%if %{?devel}
Source0:        toped-0.9.80.2137svn.tar.bz2
%else
Source0:        http://toped.googlecode.com/files/toped-0.9.8.1-r2211.tar.bz2
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  wxGTK3-devel
BuildRequires:  glew-devel
BuildRequires:  byacc
BuildRequires:  libtool
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++

Requires:       electronics-menu

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
This package contains development files for %{name}.


%description
Toped is a layout editor with CIF and GDSII export capabilities.

Toped is listed among Fedora Electronic Lab packages.

%prep
%setup -q -n %{name}-0.9.8.1
# -n %{name}-%{version}

# RHBZ#679511 - toped 0.9.70-1 not built with $RPM_OPT_FLAGS
sed -i.cflags "s|CXXFLAGS=\".*\"|CXXFLAGS=\"-std=c++14 \%{optflags} -DNDEBUG\"|g" configure

%if %{?devel}
%{__make} -f Makefile.cvs
%endif

%build

CPPFLAGS=%{optflag} 
%configure --enable-utils --disable-static

# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

# TGC#118 tpd_ifaces/Makefile requires -fpermissive
# FIXED sed -i -e "s|CXXFLAGS =|CXXFLAGS = -fpermissive|g" tpd_ifaces/Makefile

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} INSTALL="install -p" DESTDIR=%{buildroot} install

desktop-file-install --vendor ""              \
  --add-category "Electronics"                \
  --delete-original                           \
  --remove-category "Science"                 \
  --remove-category "Education"               \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
%{__cp} -p ui/%{name}_16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/toped.png
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
%{__cp} -p ui/%{name}_32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/toped.png
%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
%{__cp} -p ui/%{name}_64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/toped.png

mv %{buildroot}%{_includedir}/%{name}_0.9.* %{buildroot}%{_includedir}/%{name}-%{version}

#No translations
#%find_lang %{name}

# exporting the variable $TPD_GLOBAL
%{__mkdir} -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh << EOF
# Fedora/Free Electronic Lab
# TOPED VLSI design system
export TPD_GLOBAL=%{_datadir}/%{name}/
export TPD_LOCAL=\$HOME
EOF

rm -f `find %{buildroot} -type f -name '*.la'`

%post
%{?ldconfig}
source %{_sysconfdir}/profile.d/toped.sh

%ldconfig_postun

%files
%doc AUTHORS COPYING NEWS TODO
%{_bindir}/%{name}
%{_bindir}/gds2vrml
%{_libdir}/libtpd*.so.*
%{_libdir}/libgdsto3d.so.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/toped.png
%{_sysconfdir}/profile.d/toped.sh

%files devel
%{_libdir}/libtpd*.so
%{_libdir}/libgdsto3d.so
%{_includedir}/%{name}-%{version}


%changelog
* Wed Aug 19 2020 Jeff Law <law@redhat.com> - 0.9.81-27.svn2211
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-26.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-25.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Scott Talbert <swt@techie.net> - 0.9.81-24.svn2211
- Rebuild with wxWidgets GTK3 build

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-23.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-22.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Scott Talbert <swt@techie.net> - 0.9.81-21.svn2211
- Add missing BR for gcc-c++ to fix FTBFS
- Rebuild with wxWidgets 3.0 (GTK+2 build)

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.9.81-20.svn2211
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-19.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-18.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.81-17.svn2211
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-16.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-15.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-14.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.81-13.svn2211
- Rebuild for glew 2.0.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.81-12.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.9.81-11.svn2211
- Rebuild for glew 1.13

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.81-10.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.81-9.svn2211
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.81-8.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.81-7.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.9.81-6.svn2211
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.81-5.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.81-4.svn2211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.9.81-3.svn2211
- Rebuild for glew 1.9.0

* Tue Sep 25 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.81-2.svn2211
- Build with $RPM_OPT_FLAGS (#679511).

* Sat Aug 11 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.81-1.svn2211
- Update to 0.9.8.1

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 0.9.80-3.svn2137
- Rebuild for new glew

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.80-2.svn2137
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 30 2012 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.80-1.svn2137
- New upstream release

* Thu Dec 15 2011 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.70.1-3.svn2018
- TGC#118: tpd_ifaces/Makefile requires -fpermissive - svn2013 - filed by FEL
- TGC#119: static definitions for cadence techfile converter - svn2013 - filed by FEL

* Sat Dec 10 2011 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.70.1-3.svn2013
- Bugfix release - critical issue related to the AREF structures in GDSII.

* Mon Jun 20 2011 Adam Jackson <ajax@redhat.com> - 0.9.70.1-2.svn1794
- Rebuild for new glew soname

* Tue Mar 08 2011 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.70.1-1.svn1794
- Bugfix release - critical issue related to the AREF structures in GDSII.

* Sat Mar 05 2011 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.70-2.svn1789
- Fixed Issue 96 in toped: Ghost polygons appears on Zoom
- Fixed Issue 97 in toped: GDS aref's are broken

* Thu Feb 17 2011 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.70-1
- New Upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 18 2010 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.65-1
- New Upstream release

* Sat Apr 08 2010 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.60-1
- 0.9.6 stable release
- OASIS (Open Artwork Interchange Standard) import, complies with SEMI P39-308 standard paper.
- Calibre DRC viewer

* Thu Dec 10 2009 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.51-1
- 0.9.51 release to fix start-up crash with Mesa DRI on Intel(R) 945GM - RHBZ 541879

* Sun Oct 03 2009 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.5-1
- 0.9.5 stable release

* Sat Oct 03 2009 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.5-0.1
- 0.9.5 test release

* Tue Aug 04 2009 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.4-1
- 0.9.4 final release

* Sat Aug 01 2009 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.4-0.2.rc1
- Testing for upstream D-1 for 0.94 release - svn rev 1161

* Sat Aug 01 2009 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.4-0.1.rc1
- 0.9.4 release candidate 1

* Tue Mar 10 2009 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.2-4
- bug fix for cif and gdsII import and export

- disabling rpath
- fixing rpmlint warning: unused-direct-shlib-dependencies
- fixed multiple menu entries

* Mon Nov 10 2008 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.2-1
- New upstream release

* Fri Jul 26 2008 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.0-2
- Bug fix 451218

* Sun May 25 2008 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.9.0-1
- New upstream release

* Fri Oct 12 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.6-1
- New upstream release

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.8.5-2
- mass rebuild for fedora 8 - BuildID

* Sat Mar 10 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.5-1
- New upstream release

* Mon Feb 26 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.2-8
- fixed for rawhide compat-wxGTK26

* Fri Dec 29 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.2-7
- patch for wxWidgets-2.8

* Mon Dec 25 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.2-6
- Fixed fedora vendor

* Mon Dec 25 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.2-5
- Rebuild for development

* Mon Dec 25 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.2-4
- Fixed kmenu desktop file to science menu

* Sun Dec 24 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.2-3
- FC6 rebuilt
- removed fedora vendor

* Mon Sep 27 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.2-2
- Removed the devel package

* Mon Sep 27 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.2-1
- New upstream release 0.8.2

* Wed Sep 27 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.1-2
- Icons received by upstream (by mail)

* Mon Sep 18 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.8.1-1
- initial package
