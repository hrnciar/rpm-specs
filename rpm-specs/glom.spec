%global apiver 1.30
%global pyapiver %%(echo %{apiver} | tr . _)
# first two digits of version
%global release_version %%(echo %{version} | awk -F. '{print $1"."$2}')

%global glibmm24_version 2.46.1
%global goocanvasmm2_version 1.90.11
%global gtkmm30_version 3.18.0
%global gtksourceviewmm3_version 3.18.0
%global libgdamm_version 4.99.10

Name:           glom
Version:        1.30.4
Release:        21%{?dist}
Summary:        Easy-to-use database designer and user interface

License:        GPLv2+
URL:            http://www.glom.org/
Source0:        https://download.gnome.org/sources/glom/%{release_version}/glom-%{version}.tar.xz
# https://bugzilla.redhat.com/show_bug.cgi?id=1674980
Patch0:         glom-deleted-moves.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils gettext-devel intltool
BuildRequires:  glibmm24-devel >= %{glibmm24_version}
BuildRequires:  libgdamm-devel >= %{libgdamm_version}
BuildRequires:  libxml++-devel >= 2.23.1
BuildRequires:  python3-devel
BuildRequires:  gtkmm30-devel >= %{gtkmm30_version}
BuildRequires:  libxslt-devel >= 1.1.10
BuildRequires:  pygobject3-devel >= 2.29.0
BuildRequires:  iso-codes-devel
BuildRequires:  itstool
BuildRequires:  gtksourceviewmm3-devel >= %{gtksourceviewmm3_version}
BuildRequires:  libarchive-devel
BuildRequires:  libgda-devel >= 5.2.1
BuildRequires:  postgresql-server
BuildRequires:  libgda-postgres >= 5.2.1
BuildRequires:  avahi-ui-devel
BuildRequires:  goocanvasmm2-devel >= %{goocanvasmm2_version}
BuildRequires:  evince-devel
BuildRequires:  libepc-devel >= 0.4.0
BuildRequires:  boost-python3-devel
BuildRequires:  libarchive > 3.0
BuildRequires:  /usr/bin/sphinx-build

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Make sure we have new enough versions of dependencies
Requires:       glibmm24%{?_isa} >= %{glibmm24_version}
Requires:       goocanvasmm2%{?_isa} >= %{goocanvasmm2_version}
Requires:       gtkmm30%{?_isa} >= %{gtkmm30_version}
Requires:       gtksourceviewmm3%{?_isa} >= %{gtksourceviewmm3_version}
Requires:       libgdamm%{?_isa} >= %{libgdamm_version}
# Glom curently only supports postgresql well and uses it by default.
Requires:       postgresql-server
# Both gda providers are dlopened by libgda. sqlite is used internally
# by glom.
Requires:       libgda-postgres%{?_isa}
Requires:       libgda-sqlite%{?_isa}

%description
Glom lets you design database systems - the database and the user
interface. Glom has high-level features such as relationships,
lookups, related fields, related records, calculated fields, drop-down
choices, searching, reports, users and groups. It has Numeric, Text,
Date, Time, Boolean, and Image field types. Glom systems require
almost no programming, but you may use Python for calculated fields or
buttons. Glom uses the PostgreSQL database backend.

%package libs
Summary:  Libraries for %{name}


%description libs
The %{name}-libs package contains shared libraries for %{name}.


%package devel
Summary:    Headers for developing programs that will use %{name}
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}


%description devel
This package contains the header files needed to develop applications
that use the %{name} libraries.


%prep
%setup -q
%patch0 -p1


%build
export PYTHON=%{__python3}
%configure \
        --disable-dependency-tracking \
        --disable-static \
        --disable-update-mime-database \
        --with-postgres-utils=/usr/bin \
        --disable-sqlite \
        --docdir=%{_datadir}/%{name}
# removing rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
%make_install
%find_lang %{name} --with-gnome
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%check
desktop-file-validate ${RPM_BUILD_ROOT}/usr/share/applications/%{name}.desktop

%ldconfig_scriptlets libs

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}_create_from_example
%{_bindir}/%{name}_export_po
%{_bindir}/%{name}_export_po_all
%{_bindir}/%{name}_import_po_all
%{_bindir}/%{name}_test_connection
%{python3_sitearch}/%{name}_%{pyapiver}.so
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/appdata/%{name}.appdata.xml

%files libs
%license COPYING
%{_libdir}/libglom-%{apiver}.so.*


%files devel
%{_includedir}/glom-%{apiver}/
%{_libdir}/libglom-%{apiver}.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/devhelp/
%doc %{_docdir}/libglom-%{apiver}/
%doc %{_docdir}/pyglom_%{pyapiver}/

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.30.4-19
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.30.4-18
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.30.4-16
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Jonathan Wakely <jwakely@redhat.com> - 1.30.4-14
- Add missing BuildRequires: gcc-c++ and patch to fix invalid value type

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.30.4-12
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.30.4-10
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.30.4-7
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.30.4-6
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.30.4-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 14 2016 Kalev Lember <klember@redhat.com> - 1.30.4-2
- Rebuilt for libgettextpo soname change

* Thu Jun 09 2016 Kalev Lember <klember@redhat.com> - 1.30.4-1
- Update to 1.30.4

* Fri Mar 11 2016 Kalev Lember <klember@redhat.com> - 1.30.3-1
- Update to 1.30.3

* Thu Mar 03 2016 Kalev Lember <klember@redhat.com> - 1.30.2-1
- Update to 1.30.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.30.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.30.1-2
- Rebuilt for Boost 1.60

* Sat Dec 12 2015 Kalev Lember <klember@redhat.com> - 1.30.1-1
- Update to 1.30.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 23 2015 Kalev Lember <klember@redhat.com> - 1.30.0-1
- Update to 1.30.0
- Switch to Python 3
- Add a fully versioned dependency on -libs subpackage

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.28.4-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.28.4-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.28.4-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 14 2015 Kalev Lember <kalevlember@gmail.com> - 1.28.4-1
- Update to 1.28.4
- Simplify macro usage
- Drop huge ChangeLog file
- Use license macro for the COPYING file
- Tighten library dependencies with the _isa macro

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.27.1-4
- Rebuild for boost 1.57.0

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.27.1-3
- Rebuild for boost 1.57.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.27.1-2
- fix/update icon/mime scriptlets

* Sun Sep 14 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 1.27.1-1
- Upstream 1.27.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.26.0-3
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.26.0-2
- rebuild for boost 1.55.0

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 1.26.0-1
- Update to 1.26.0
- Drop obsolete scrollkeeper handling
- Modernize rpm scriptlets

* Mon Nov  4 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 1.24.2-1
- upstream 1.24.2

* Sun Nov  3 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 1.24.1-1
- upstream 1.24.1 (fixes RHBZ #1022294)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.22.1-5
- Rebuild for boost 1.54.0

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1.22.1-4
- Rebuilt for gtksourceview3 soname bump

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.22.1-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.22.1-2
- Rebuild for Boost-1.53.0

* Wed Nov 14 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.22.%{minor_version}-1
- upstream 1.22.1

* Sun Oct 21 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.22.0-1
- upstream 1.22.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.6-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.18.6-1
- upstream 1.18.6

* Tue Oct 11 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.18.4-1
- upstream 1.18.4

* Sun Aug 28 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.18.3-2
- recompile against newer libepc

* Sat Jul 23 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.18.3-1
- upstream 1.8.3

* Mon Apr 18 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.18.1-1
- upstream 1.18.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1.16.1-1
- Update to upsteam release 1.16.1
- Drop unneeded BR: gnome-vfsmm

* Fri Jul 30 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1.15.1-1
- Update to upsteam release 1.15.1

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Apr 28 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1.14.1-1
- Update to upstream release 1.14.1
- Added libglom and pyglom documentation
- Add BR python-sphinx (python documentation)

* Thu Feb 18 2010 Denis Leroy <denis@poolshark.org> - 1.13.4-1
- Update to unstable release 1.13.4
- Added boost-devel BR

* Tue Jan  5 2010 Denis Leroy <denis@poolshark.org> - 1.12.4-1
- Update to upstream 1.12.4

* Wed Nov  4 2009 Denis Leroy <denis@poolshark.org> - 1.12.3-1
- Update to upstream 1.12.3, regression fix from 1.12.2

* Sun Oct 25 2009 Denis Leroy <denis@poolshark.org> - 1.12.2-1
- Update to upstream 1.12.2
- Fixed gnome-python2-gda run-time Require (#530656)

* Sat Sep 26 2009 Denis Leroy <denis@poolshark.org> - 1.12.0-1
- Update to upstream 1.12.0
- BRs update, library versioning update

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Denis Leroy <denis@poolshark.org> - 1.10.1-1
- Update to stable upstream 1.10.1, bugfix release

* Sat Apr  4 2009 Denis Leroy <denis@poolshark.org> - 1.10.0-3
- Requires libgda-sqlite 

* Wed Mar 25 2009 Denis Leroy <denis@poolshark.org> - 1.10.0-2
- Fixed libs rpmlint complaints

* Mon Mar 23 2009  <denis@poolshark.org> - 1.10.0-1
- Update to 1.10.0
- Disable sqlite backend, has very limited functionality
- Split libs and devel packages

* Wed Mar  4 2009 Denis Leroy <denis@poolshark.org> - 1.9.3-1
- Update to upstream 1.9.3
- Now provides sqlite backend

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Denis Leroy <denis@poolshark.org> - 1.9.0-1
- Update to upstream 1.9.0
- Updated list of BRs

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.17-3
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.17-2
- Rebuild for Python 2.6

* Tue Jun 17 2008 Denis Leroy <denis@poolshark.org> - 1.6.17-1
- Update to 1.6.17
- gcc 4.3 patch upstreamed

* Tue May  6 2008 Denis Leroy <denis@poolshark.org> - 1.6.15-1
- Update to upstream 1.6.15, fixes connection issue

* Sun Mar 23 2008 Denis Leroy <denis@poolshark.org> - 1.6.10-1
- Update to upstream 1.6.10, buxfix release

* Mon Feb 11 2008 Denis Leroy <denis@poolshark.org> - 1.6.8-1
- Update to 1.6.8, bugfix release
- Added patch for g++ 4.3

* Tue Jan 29 2008 Denis Leroy <denis@poolshark.org> - 1.6.7-1
- Update to upstream 1.6.7, bugfix release, BR versions updated

* Wed Jan 23 2008 Denis Leroy <denis@poolshark.org> - 1.6.6-1
- Update to upstream 1.6.6, with fix for database closing bug

* Mon Nov 19 2007 Denis Leroy <denis@poolshark.org> - 1.6.4-1
- Update to upstream 1.6.4, many bug fixes

* Wed Sep 12 2007 Denis Leroy <denis@poolshark.org> - 1.6.0-1
- Update to 1.6.0, updated BRs

* Thu Aug 23 2007 Denis Leroy <denis@poolshark.org> - 1.5.2-2
- License tag update

* Tue Jun 19 2007 Denis Leroy <denis@poolshark.org> - 1.5.2-1
- Update to 1.5.2
- Now using libgda 3.0

* Thu Apr  5 2007 Denis Leroy <denis@poolshark.org> - 1.4.3-1
- Update to 1.4.3

* Thu Mar 22 2007 Denis Leroy <denis@poolshark.org> - 1.4.2-1
- Update to 1.4.2
- Removed avahi dependency

* Thu Mar 15 2007 Denis Leroy <denis@poolshark.org> - 1.4.0-1
- Update to 1.4.0

* Fri Mar  9 2007 Denis Leroy <denis@poolshark.org> - 1.3.11-1
- Update to 1.3.11
- Updated dependencies, added postgres deps

* Mon Dec 11 2006 Denis Leroy <denis@poolshark.org> - 1.2.2-3
- Fixed python2.5 path
- Added patch to fix python 2.5 compile

* Fri Dec  8 2006 Denis Leroy <denis@poolshark.org> - 1.2.2-2
- Fixed source upload

* Fri Dec  8 2006 Denis Leroy <denis@poolshark.org> - 1.2.2-1
- Update to 1.2.2

* Tue Nov 21 2006 Denis Leroy <denis@poolshark.org> - 1.2.1-2
- Update to 1.2.1

* Thu Oct 19 2006 Denis Leroy <denis@poolshark.org> - 1.2.0-2
- Rebuild with correct sources files

* Wed Oct 18 2006 Denis Leroy <denis@poolshark.org> - 1.2.0-1
- Update to 1.2.0
- Added omf directory

* Sun Oct  8 2006 Denis Leroy <denis@poolshark.org> - 1.0.7-1
- Update to 1.0.7

* Fri Oct  6 2006 Denis Leroy <denis@poolshark.org> - 1.0.5-4
- fixed x86_64 spec, vfsmm patch no longer needed

* Thu Oct  5 2006 Denis Leroy <denis@poolshark.org> - 1.0.5-3
- Added scrollkeeper db updates
- Added mime-type key to desktop file
- Added autoreconf and patch to fix rpath problem

* Wed Oct  4 2006 Denis Leroy <denis@poolshark.org> - 1.0.5-2
- Fixed BRs
- Enabled scrollkeeper

* Tue Oct  3 2006 Denis Leroy <denis@poolshark.org> - 1.0.5-1
- Update to 1.0.5

* Thu Aug  3 2006 Denis Leroy <denis@poolshark.org> - 1.0.4-1
- First version

