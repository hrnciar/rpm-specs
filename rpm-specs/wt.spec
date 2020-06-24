%global WTSRVDIR        /var/spool/wt
%global WTRUNDIR        %{WTSRVDIR}/run

%global WTRUNUSER       apache
%global WTRUNGROUP      apache

Name:           wt
Version:        4.3.0
Release:        2%{?dist}
Summary:        C++ library for developing web applications

# For a breakdown of the licensing, see PACKAGE-LICENSING
License:        GPLv2 and Boost and MIT and (Boost or MIT) and BSD and zlib
URL:            https://www.webtoolkit.eu/wt
# Following archive was made from upstream tarball downloaded from
#  https://github.com/kdeforche/wt/archive/3.3.7.tar.gz
# by running ./wt-generate-tarball.sh 3.3.7 from tarball's directory
Source0:        %{name}-%{version}-free.tar.xz
Source1:        %{name}-%{version}-PACKAGE-LICENSING
# Explain why the locale example is renamed to timezone.
Source2:        timezone-README.fedora
# Explain why the jPlayer static files are missing.
Source3:        README.fedora
# wt toolkit contains bundled non-free library (IBPP) that we cannot ship.
# Therefore we use this script to remove its code before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
#   ./wt-generate-tarball.sh UPSTREAM_VERSION
Source4:        wt-generate-tarball.sh

Patch0:         use-system-sqlite.patch
Patch1:         ssl-default-cipher-list.patch

BuildRequires:  cmake >= 3.1 boost-devel >= 1.41 gcc-c++ openssl-devel doxygen
BuildRequires:  GraphicsMagick-devel pango-devel sqlite-devel libpq-devel
BuildRequires:  mariadb-connector-c-devel libharu-devel fcgi-devel zlib-devel
BuildRequires:  qt5-qtbase-devel

# Don't use bundled glew on fedora >= 21
%if 0%{?fedora} >= 21
%global use_system_glew 1
BuildRequires:  glew-devel
%endif

# Denote the fact of bundling glew
%{!?use_system_glew:Provides: bundled(glew) = 1.10.0}

%description
Web C++ library with widget oriented API that uses well-tested patterns of
desktop GUI development tailored to the web. To the developer, it offers
abstraction of web-specific implementation details, including client-server
protocols, event handling, graphics support, graceful degradation (or
progressive enhancement), and URL handling.

%package        dbo
Summary:        Wt::Dbo ORM library and Sqlite3 back-end

%description    dbo
This package contains the Wt::Dbo Object-Relational Mapping library
and Sqlite3 back-end of it.

%package        dbo-mysql
Summary:        MySQL back-end for the Wt::Dbo ORM library
Requires:       %{name}-dbo%{?_isa} = %{version}-%{release}

%description    dbo-mysql
This package contains the MySQL back-end for the Wt::Dbo ORM library.

%package        dbo-postgres
Summary:        PostgreSQL back-end for the Wt::Dbo ORM library
Requires:       %{name}-dbo%{?_isa} = %{version}-%{release}

%description    dbo-postgres
This package contains the PostgresSQL back-end for the Wt::Dbo ORM library.
 
%package        devel
Summary:        Libraries and header files for witty web development
Requires:       %{name}%{?_isa}              = %{version}-%{release}
Requires:       %{name}-dbo%{?_isa}          = %{version}-%{release}
Requires:       %{name}-dbo-postgres%{?_isa} = %{version}-%{release}
Requires:       %{name}-dbo-mysql%{?_isa}    = %{version}-%{release}
Requires:       cmake

%description    devel
This package contains the files necessary to develop
applications using the Wt toolkit and the Wt::Dbo ORM library.

%package        examples
Summary:        Examples for Wt
License:        GPLv2 and MIT
Requires:       %{name}%{?_isa}      = %{version}-%{release}
Requires:       %{name}-dbo%{?_isa}  = %{version}-%{release}

%description    examples
This package contains programming examples distributed with official Wt
release.

%package        doc
Summary:        Documents for the Wt toolkit
# Unfortunately there are differences in doxygen output between arm and other
# architectures.
#BuildArch:      noarch

%description    doc
This package contains the documents for Wt API and examples.

%prep
%autosetup -p1

# static files like javascript and css should not be executable
for d in src resources examples; do
    find $d -type f \( -iregex '.*\.\([hc]\|js\|css\)' -o -executable \) | \
        xargs -r chmod -v 0644
done
# locale script created in build directory causes build to fail because some
# dependent headers try to include <locale> header which is found in current
# directory. Let's rename it to timezone.
mv examples/feature/locale examples/feature/timezone
mv examples/feature/timezone/{locale,timezone}.C
sed -i 's/locale/timezone/g' \
    examples/feature/CMakeLists.txt \
    examples/feature/timezone/CMakeLists.txt

find examples -type f -name .htaccess | while read f; do
    mv -v $f `dirname $f`/htaccess
done
# conversion to UTF-8
convdir=`mktemp -d`
for f in examples/style/CornerImage.h; do
    tmpf=${convdir}/`basename $f`
    iconv -f iso-8859-2 -t UTF-8 $f >$tmpf
    mv $tmpf $f
done
rmdir $convdir

# Make sure not to be using bundled glew
%{?use_system_glew:rm -rf src/3rdparty/glew-1.10.0}

%build
mkdir wt-build
cd wt-build
## wtdbofirebird library bundles IBPP c++ client library for firebird
## that is licensed under IBPP License, which is marked as Non-Free
## by Red Hat Legal
## let's not package it, until licensing issues are solved
%cmake .. \
    -DCONNECTOR_HTTP=ON \
    -DCONNECTOR_FCGI=ON \
    -DUSE_SYSTEM_SQLITE3=ON \
    -DWT_WRASTERIMAGE_IMPLEMENTATION=GraphicsMagick \
    -DWEBUSER="%{WTRUNUSER}" \
    -DWEBGROUP="%{WTRUNGROUP}" \
    -DRUNDIR="%{WTRUNDIR}" \
    -DCONFIGDIR="%{_sysconfdir}/%{name}" \
    -DENABLE_FIREBIRD=OFF \
    -DENABLE_MYSQL=ON \
    %{?use_system_glew:-DUSE_SYSTEM_GLEW=1} \
    -DBUILD_EXAMPLES=ON \
    -DINSTALL_EXAMPLES=ON \
    -DEXAMPLES_DESTINATION=%{_lib}/Wt/examples
make %{?_smp_mflags}
make doc

%install
pushd wt-build
make install DESTDIR=${RPM_BUILD_ROOT}
install -v -m 0755 -d ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}
cp -v wt_config.xml ${RPM_BUILD_ROOT}/%{_sysconfdir}/%{name}

# makes an absolute symlink to resources directory
make_rsc_link() {
    ln -vs "%{_datadir}/Wt/resources" \
        "${RPM_BUILD_ROOT}%{_libdir}/Wt/examples/$1"
}

# installation of examples
pushd examples
for d in `find . -maxdepth 1 -mindepth 1 -type d | \
        grep -v '^\(CMakeFiles\|feature\)$'`; do
    # create a symlink for each example pointing on resources dir
    make_rsc_link $d
done
for d in `find feature -maxdepth 1 -mindepth 1 -type d | grep -v 'CMakeFiles'`;
do  # create a symlink for each feature example pointing on resources dir
    make_rsc_link $d
done
popd # examples
popd # wt-build
install -vm 644 %{SOURCE2} \
    ${RPM_BUILD_ROOT}%{_libdir}/Wt/examples/feature/timezone/README.fedora

# installation of documentation
for d in %{name} %{name}-dbo %{name}-doc; do
    install -v -m 0755 -d ${RPM_BUILD_ROOT}%{_defaultdocdir}/$d/
    cp -v LICENSE ${RPM_BUILD_ROOT}%{_defaultdocdir}/$d/
    install -vm 644  %{SOURCE1} \
        ${RPM_BUILD_ROOT}%{_defaultdocdir}/$d/PACKAGE-LICENSING
done
cp -vr README.md %{SOURCE3} ReleaseNotes.html Changelog \
    ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}/
cp -vr INSTALL*.html doc/* ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}-doc/

pushd ${RPM_BUILD_ROOT}
mkdir -vp .%{WTSRVDIR}
mkdir -vp .%{WTRUNDIR}

# cleanup
for d in examples reference; do
    if [[ -e .%{_defaultdocdir}/%{name}-doc/$d/html/installdox ]]; then
        rm -v .%{_defaultdocdir}/%{name}-doc/$d/html/installdox
    fi
done
rm -v .%{_defaultdocdir}/%{name}-doc/main
find .%{_libdir}/Wt/examples -regex '.*/\(CMakeFiles\|.*\.cmake\|Doxygen\)' | \
    xargs rm -rfv
# these scripts were used to generate pictures
find .%{_datadir}/Wt/resources -name 'generate.sh' | xargs rm -v
popd

%ldconfig_scriptlets
%ldconfig_scriptlets   dbo
%ldconfig_scriptlets   dbo-mysql
%ldconfig_scriptlets   dbo-postgres

%files
%config(noreplace) %{_sysconfdir}/%{name}/wt_config.xml
%{_libdir}/libwt.so.*
%{_libdir}/libwtfcgi.so.*
%{_libdir}/libwthttp.so.*
%{_libdir}/libwttest.so.*
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/README.md
%doc %{_defaultdocdir}/%{name}/README.fedora
%doc %{_defaultdocdir}/%{name}/LICENSE
%doc %{_defaultdocdir}/%{name}/ReleaseNotes.html
%doc %{_defaultdocdir}/%{name}/Changelog
%doc %{_defaultdocdir}/%{name}/PACKAGE-LICENSING
%dir %{_datadir}/Wt
%dir %{_datadir}/Wt/resources
%{_datadir}/Wt/resources/*
%dir %{WTSRVDIR}
%dir %{WTRUNDIR}

%files dbo
%dir %{_defaultdocdir}/%{name}-dbo
%doc %{_defaultdocdir}/%{name}-dbo/LICENSE
%doc %{_defaultdocdir}/%{name}-dbo/PACKAGE-LICENSING
%{_libdir}/libwtdbo.so.*
%{_libdir}/libwtdbosqlite3.so.*

%files dbo-mysql
%{_libdir}/libwtdbomysql.so.*

%files dbo-postgres
%{_libdir}/libwtdbopostgres.so.*

%files devel
# header files
%dir %{_includedir}/Wt
%{_includedir}/Wt/*
%{_libdir}/*.so
%dir %{_libdir}/cmake/wt
%{_libdir}/cmake/wt/*.cmake

%files examples
%dir %{_libdir}/Wt
%dir %{_libdir}/Wt/examples
%{_libdir}/Wt/examples/*

%files doc
%dir %{_defaultdocdir}/%{name}-doc
%doc %{_defaultdocdir}/%{name}-doc/LICENSE
%doc %{_defaultdocdir}/%{name}-doc/PACKAGE-LICENSING
%{_defaultdocdir}/%{name}-doc/*.html
%dir %{_defaultdocdir}/%{name}-doc/images
%dir %{_defaultdocdir}/%{name}-doc/reference
%dir %{_defaultdocdir}/%{name}-doc/tutorial
%dir %{_defaultdocdir}/%{name}-doc/examples
%{_defaultdocdir}/%{name}-doc/images/*
%{_defaultdocdir}/%{name}-doc/reference/*
%{_defaultdocdir}/%{name}-doc/tutorial/*
%{_defaultdocdir}/%{name}-doc/examples/*
%{_defaultdocdir}/%{name}-doc/*.dox

%changelog
* Mon Jun 15 2020 Jonathan Wakely <jwakely@redhat.com> - 4.3.0-2
- Replace BuildRequires: qt5-devel with qt5-qtbase-devel

* Thu Mar 26 2020 Michal Minář <miminar@redhat.com> - 4.3.0-1
- New upstream version 4.3.0

* Fri Mar 20 2020 Michal Minář <miminar@redhat.com> - 4.2.2-2
- Fixed -examples' dependencies

* Tue Mar 17 2020 Michal Minář <miminar@redhat.com> - 4.2.2-1
- New upstream version 4.2.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 4.1.0-2
- Add missing #include for gcc-10

* Mon Aug 19 2019 Michal Minář <miminar@redhat.com> - 4.1.0-1
- New upstream version.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Michal Minář <miminar@redhat.com> - 4.0.5-1
- New upstream version 4.0.5

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 4.0.3-3
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 4.0.3-2
- Rebuilt for glew 2.1.0

* Mon Jul 23 2018 <miminar@redhat.com> - 4.0.3-1
- New upstream version 4.0.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Michal Minář <miminar@redhat.com> - 4.0.2-3
- New upstream version 4.0.2
- Compatibility fix for boost 1.66
- Depend on mariadb-connector-c-devel

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.3.7-6
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Björn Esser <besser82@fedoraproject.org> - 3.3.7-3
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Apr 23 2017 Michal Minar <miminar@redhat.com> 3.3.7-1
- New upstream version 3.3.7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 3.3.6-2
- Rebuild for glew 2.0.0

* Mon Aug 08 2016 Michal Minar <miminar@redhat.com> 3.3.6-1
- New upstream version 3.3.6

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 3.3.5-0.6.rc2
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-0.5.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 3.3.5-0.4.rc2
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 3.3.5-0.3.rc2
- Rebuild for glew 1.13

* Wed Nov 18 2015 Michal Minar <miminar@redhat.com> 3.3.5-0.2.rc2
- Made doc package archfull.

* Wed Nov 18 2015 Michal Minar <miminar@redhat.com> 3.3.5-0.1.rc2
- New upstream version 3.3.5-rc2

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.3.4-6
- Rebuilt for Boost 1.59

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.3.4-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.3.4-3
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Michal Minar <miminar@redhat.com> 3.3.4-1
- New upstream version 3.3.4

* Mon Feb 09 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.3.3-4
- Add wt-3.3.3-boost-1.57.patch (Fix boost-1.57 FTBFS).
- Replace bogus BR: boost-devel%%{_isa} with BR: boost-devel.
- Unbundle GLEW.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Michal Minar <miminar@redhat.com> 3.3.3-2
- Reenabled raster image support.

* Wed Jun 11 2014 Michal Minar <miminar@redhat.com> 3.3.3-1
- New upstream version 3.3.3.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 3.3.2-3
- rebuild for boost 1.55.0

* Fri Mar 21 2014 Michal Minar <miminar@redhat.com> 3.3.2-2
- Got rid of bundled sqlite libraries.

* Fri Mar 14 2014 Michal Minar <miminar@redhat.com> 3.3.2-1
- Update to 3.3.2

* Sun Sep 22 2013 Michal Minar <miminar@redhat.com> 3.3.1-0.1.rc1
- Update to 3.3.1-rc1.
- Added dbo-mysql subpackage with MySQL backend library.
- Unversioned doc directories.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 3.3.0-3
- Rebuild for boost 1.54.0

* Wed Jun 26 2013 Michal Minar <miminar@redhat.com> 3.3.0-2
- Using LZMA2 compression for source archive.

* Thu Jun 20 2013 Michal Minar <miminar@redhat.com> 3.3.0-1
- Version 3.3.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.2.3-2
- Rebuild for Boost-1.53.0

* Wed Dec 26 2012 Michal Minar <miminar@redhat.com> - 3.2.3-1
- Version 3.2.3

* Mon Dec 24 2012 Rex Dieter <rdieter@fedoraproject.org> 3.2.2-7.p1
- rebuild (GraphicsMagick)

* Thu Sep 13 2012 Michal Minar <miminar@redhat.com> - 3.2.2-6.p1
- fixed changelog line

* Wed Sep 12 2012 Michal Minar <miminar@redhat.com> - 3.2.2-5.p1
- Added wt-generate-tarball.sh script for source tarball generation
  from upstream tarball, in order to remove the IBPP non-free library
  from source.

* Mon Sep 03 2012 Michal Minar <miminar@redhat.com> - 3.2.2-4.p1
- separated doc dirs for independent subpackages -dbo and -doc

* Fri Aug 24 2012 Michal Minar <miminar@redhat.com> - 3.2.2-3.p1
- Own examples directory.
- Include a copy of license in wt-doc.
- Added License tag for wt-examples.

* Fri Aug 24 2012 Michal Minar <miminar@redhat.com> - 3.2.2-2.p1
- Not packaging back-end due to licensing issues.

* Tue Aug 21 2012 Michal Minar <miminar@redhat.com> - 3.2.2-1.p1
- Initial Package for FE.
