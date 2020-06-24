%{!?javabuild:%global	javabuild 0}
%{!?utils:%global	utils 1}
%{!?gcj_support:%global	gcj_support 0}
%{!?upgrade:%global	upgrade 1}
%{!?runselftest:%global	runselftest 1}

# rhbz#1503454
%global _smp_mflags	-j1

%ifarch s390x
# rhbz#1503476
%undefine	_hardened_build
%endif
%if 0%{?fedora} == 26
%undefine	_hardened_build
%endif

%global		majorversion 3.0
%global		soversion 3
%global		prevmajorversion 2.5
%global		prevversion %{prevmajorversion}.4
%global		so_files	postgis postgis_topology rtpostgis address_standardizer
%global		configure_opts	--disable-rpath --enable-raster

%global		pg_version_minimum 9.4

%global		__provides_exclude_from %{_libdir}/pgsql

Summary:	Geographic Information Systems Extensions to PostgreSQL
Name:		postgis
Version:	%majorversion.1
Release:	7%{?dist}
License:	GPLv2+
Source0:	http://download.osgeo.org/%{name}/source/%{name}-%{version}.tar.gz
Source2:	http://download.osgeo.org/%{name}/docs/%{name}-%{version}.pdf
Source3:	http://download.osgeo.org/%{name}/source/%{name}-%{prevversion}.tar.gz
Source4:	filter-requires-perl-Pg.sh
URL:		http://www.postgis.net

BuildRequires:	perl-generators
BuildRequires:	postgresql-server-devel >= %{pg_version_minimum}
BuildRequires:	libpq-devel, json-c-devel, gcc-c++, pcre-devel, autoconf
BuildRequires:	proj-devel >= 5.2.0, geos-devel >= 3.7.1 byacc, automake
BuildRequires:	flex, java, java-devel, gtk2-devel, ant, libtool
BuildRequires:	libxml2-devel, gdal-devel >= 1.10.0, desktop-file-utils
BuildRequires:  clang llvm
BuildRequires:  libxslt docbook-dtds
%if %upgrade
BuildRequires:	postgresql-upgrade-devel
%endif
%{?postgresql_module_requires}
%if %runselftest
BuildRequires:	postgresql-test-rpm-macros
%endif


%description
PostGIS adds support for geographic objects to the PostgreSQL object-relational
database. In effect, PostGIS "spatially enables" the PostgreSQL server,
allowing it to be used as a backend spatial database for geographic information
systems (GIS), much like ESRI's SDE or Oracle's Spatial extension. PostGIS
follows the OpenGIS "Simple Features Specification for SQL" and has been
certified as compliant with the "Types and Functions" profile.


%package llvmjit
Summary:	Just-in-time compilation support for PostGIS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description llvmjit
Just-in-time compilation support for PostGIS.


%package docs
Summary:	Extra documentation for PostGIS
%description docs
The postgis-docs package includes PDF documentation of PostGIS.


%if %javabuild
%package jdbc
Summary:	The JDBC driver for PostGIS
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}, postgresql-jdbc
BuildRequires:	ant >= 0:1.6.2, junit >= 0:3.7, postgresql-jdbc

%if %{gcj_support}
BuildRequires:		gcc-java
BuildRequires:		java-1.5.0-gcj-devel
Requires(post):		%{_bindir}/rebuild-gcj-db
Requires(postun):	%{_bindir}/rebuild-gcj-db
%endif

%description jdbc
The postgis-jdbc package provides the essential jdbc driver for PostGIS.
%endif


%if %utils
%package utils
Summary:	The utils for PostGIS
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	perl-DBD-Pg

%description utils
The postgis-utils package provides the utilities for PostGIS.
%endif


%if %upgrade
%package upgrade
Summary:	Support for upgrading from the previous major release of Postgis
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	postgresql-upgrade
Provides:	bundled(postgis) = %prevversion

%description upgrade
The postgis-upgrade package contains the previous version of postgis
necessary for correct dump of schema from previous version of PostgreSQL.
%endif

%define __perl_requires %{SOURCE4}


%prep
%setup -q -n %{name}-%{version} -a 3

%if %upgrade
(
cd %{name}-%{prevversion}
./autogen.sh
)
%endif
cp -p %{SOURCE2} .


%build
%configure %configure_opts --with-gui --with-pgconfig=%{_bindir}/pg_server_config
sed -i 's| -fstack-clash-protection | |' postgis/Makefile
sed -i 's| -fstack-clash-protection | |' raster/rt_pg/Makefile
sed -i 's| -fstack-clash-protection | |' topology/Makefile
sed -i 's| -fstack-clash-protection | |' extensions/address_standardizer/Makefile
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%if %javabuild
export BUILDXML_DIR=%{_builddir}/%{name}-%{version}/java/jdbc
JDBC_VERSION_RPM=`rpm -ql postgresql-jdbc| grep 'jdbc2.jar$'|awk -F '/' '{print $5}'`
sed 's/postgresql.jar/'${JDBC_VERSION_RPM}'/g' $BUILDXML_DIR/build.xml > $BUILDXML_DIR/build.xml.new
mv -f $BUILDXML_DIR/build.xml.new $BUILDXML_DIR/build.xml
pushd java/jdbc
ant
popd
%endif

%if %utils
make %{?_smp_mflags} -C utils
%endif

%if %upgrade
(
# TODO: report that out-of-tree (VPATH) build is broken
cd %{name}-%{prevversion}

# first perform compat-build (against the actual PostgreSQL version).  We need
# only the so names.
%configure %configure_opts
sed -i 's| -fstack-clash-protection | |' postgis/Makefile
sed -i 's| -fstack-clash-protection | |' raster/rt_pg/Makefile
sed -i 's| -fstack-clash-protection | |' topology/Makefile
sed -i 's| -fstack-clash-protection | |' extensions/address_standardizer/Makefile
make %{?_smp_mflags}
mkdir ../compat-build
for so in %so_files; do
    find -name $so.so -exec cp {} ../compat-build/$so-%{prevmajorversion}.so \;
    find -name $so-%{prevmajorversion}.so -exec cp -t ../compat-build/ {} +
done

# Second, build feature-full build against previous PostgreSQL version.  We
# intentionally don't use %%configure here since there is too many pre-defined
# directories, and not everything from postgis-%%prevversion directory respects
# the `pg_config` output (liblwgeom especially).
./configure %configure_opts \
	--with-pgconfig=%postgresql_upgrade_prefix/bin/pg_config \
	--libdir=%postgresql_upgrade_prefix/lib \
	--includedir=%postgresql_upgrade_prefix/include
sed -i 's| -fstack-clash-protection | |' postgis/Makefile
sed -i 's| -fstack-clash-protection | |' raster/rt_pg/Makefile
sed -i 's| -fstack-clash-protection | |' topology/Makefile
sed -i 's| -fstack-clash-protection | |' extensions/address_standardizer/Makefile
make %{?_smp_mflags}
)
%endif


%install
make install DESTDIR=%{buildroot}
make %{?_smp_mflags}  -C utils install DESTDIR=%{buildroot}
make %{?_smp_mflags}  -C extensions install DESTDIR=%{buildroot}

# move application metadata to correct location
mv %{buildroot}/%{_datadir}/pgsql/applications %{buildroot}/%{_datadir}
mv %{buildroot}/%{_datadir}/pgsql/icons %{buildroot}/%{_datadir}

%if %upgrade
cd %{name}-%{prevversion}
make install DESTDIR=%{buildroot}
cd ..

# drop unused stuff from upgrade-only installation
/bin/rm -rf %buildroot%postgresql_upgrade_prefix/bin
/bin/rm -rf %buildroot%postgresql_upgrade_prefix/lib/lib*

# Manually install compat-build binary.
for so in %so_files; do
%{__install} -m 644 compat-build/$so-%{prevmajorversion}.so %{buildroot}/%{_libdir}/pgsql
done
%endif

rm -f  %{buildroot}%{_datadir}/*.sql

%if %javabuild
install -d %{buildroot}%{_javadir}
install -m 755 java/jdbc/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
%if %{gcj_support}
aot-compile-rpm
%endif
strip %{buildroot}/%{_libdir}/gcj/%{name}/*.jar.so
%endif

%if %utils
install -d %{buildroot}%{_datadir}/%{name}
install -m 755 utils/*.pl %{buildroot}%{_datadir}/%{name}
%endif

find %buildroot \( -name '*.la' -or -name '*.a' \) -delete


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/shp2pgsql-gui.desktop
%if %runselftest
%postgresql_tests_run
export PGIS_REG_TMPDIR=`mktemp -d`
if ! LD_LIBRARY_PATH=%{buildroot}%_libdir make check %{_smp_mflags} ; then
    for file in $(find $PGIS_REG_TMPDIR -name '*_diff'); do
	echo "== $file =="
	cat "$file"
    done
%ifnarch %ix86 ppc64 s390x
    # rhbz#1503453
    false
%endif
fi
%endif


%if %javabuild
%if %gcj_support
%post   jdbc -p %{_bindir}/rebuild-gcj-db
%postun jdbc -p %{_bindir}/rebuild-gcj-db
%endif
%endif


%files
%license COPYING
%doc CREDITS NEWS TODO README.%{name} loader/README.* doc/%{name}.xml doc/ZMSgeoms.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/pgsql/%{name}-%{soversion}.so
%{_datadir}/pgsql/contrib/postgis-%{majorversion}/*.sql
#if {_lib} == lib64
#{_datadir}/pgsql/contrib/postgis*.sql
#endif
%{_datadir}/pgsql/extension/address_standardizer*.sql
%{_datadir}/pgsql/extension/address_standardizer*.control
%{_datadir}/pgsql/extension/postgis-*.sql
%{_datadir}/pgsql/extension/postgis_raster*.sql
%{_datadir}/pgsql/extension/postgis_topology*.sql
%{_datadir}/pgsql/extension/postgis.control
%{_datadir}/pgsql/extension/postgis_raster.control
%{_datadir}/pgsql/extension/postgis_topology.control
%{_datadir}/pgsql/extension/postgis_tiger_geocoder*.sql
%{_datadir}/pgsql/extension/postgis_tiger_geocoder.control
%{_datadir}/postgis/create_unpackaged.pl
%{_datadir}/postgis/create_spatial_ref_sys_config_dump.pl
%{_datadir}/postgis/repo_revision.pl
%{_datadir}/postgis/postgis_proc_set_search_path.pl
%{_libdir}/pgsql/address_standardizer-%{soversion}.so
%{_libdir}/pgsql/postgis_raster-%{soversion}.so
%{_libdir}/pgsql/postgis_topology-%{soversion}.so

%{_datadir}/applications/shp2pgsql-gui.desktop
%{_datadir}/icons/hicolor/*/apps/shp2pgsql-gui.png


%files llvmjit
%{_libdir}/pgsql/bitcode/address_standardizer-*
%{_libdir}/pgsql/bitcode/postgis-*
%{_libdir}/pgsql/bitcode/postgis_raster-*
%{_libdir}/pgsql/bitcode/postgis_topology-*


%if %javabuild
%files jdbc
%doc java/jdbc/COPYING_LGPL java/jdbc/README
%attr(755,root,root) %{_javadir}/%{name}.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*.jar.so
%{_libdir}/gcj/%{name}/*.jar.db
%endif
%endif


%if %upgrade
%files upgrade
%postgresql_upgrade_prefix/*
%_libdir/pgsql/*-%{prevmajorversion}.so
%endif


%if %utils
%files utils
%doc utils/README
%dir %{_datadir}/%{name}/
%doc %{_datadir}/doc/pgsql/extension/README.address_standardizer
%{_datadir}/%{name}/test_estimation.pl
%{_datadir}/%{name}/profile_intersects.pl
%{_datadir}/%{name}/test_joinestimation.pl
%{_datadir}/%{name}/create_extension_unpackage.pl
%{_datadir}/%{name}/create_undef.pl
%{_datadir}/%{name}/%{name}_proc_upgrade.pl
%{_datadir}/%{name}/%{name}_restore.pl
%{_datadir}/pgsql/contrib/postgis-%{majorversion}/postgis_restore.pl
%{_datadir}/%{name}/read_scripts_version.pl
%{_datadir}/%{name}/test_geography_estimation.pl
%{_datadir}/%{name}/test_geography_joinestimation.pl
%endif


%files docs
%doc postgis*.pdf


%changelog
* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 3.0.1-7
- Rebuild (gdal)

* Mon May 04 2020 Sandro Mani <manisandro@gmail.com> - 3.0.1-6
- Pass --with-pgconfig=%%{_bindir}/pg_server_config

* Sun May 03 2020 Sandro Mani <manisandro@gmail.com> - 3.0.1-5
- Move postgis-upgrade to 2.5.4

* Wed Apr 22 2020 Björn Esser <besser82@fedoraproject.org> - 3.0.1-4
- Re-enable selftests

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 3.0.1-3
- Rebuild (json-c)
- Disable selftests, as they seem to be flaky

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 3.0.1-2
- Rebuild (gdal)

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Sun Feb 16 2020 Devrim Gündüz <devrim@gunduz.org> - 3.0.0-1
- Update to 3.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 4 2019 Devrim Gündüz <devrim@gunduz.org> - 2.5.3-1
- Update to 2.5.3
- Update prev version to 2.4.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 4 2019 Devrim Gündüz <devrim@gunduz.org> - 2.5.1-1
- Update to 2.5.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Petr Kubat <pkubat@redhat.com> - 2.5.0-1
- update to 2.5.0, per NEWS file:
  https://svn.osgeo.org/postgis/tags/2.5.0/NEWS

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 2.4.3-6
- rebuild against postgresql-server-devel (rhbz#1618698)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Pavel Raiskup <praiskup@redhat.com> - 2.4.3-4
- postgresql.spec moved testing macros to postgresql-test-rpm-macros

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 2.4.3-3
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Pavel Raiskup <praiskup@redhat.com> - 2.4.3-1
- rebase to latest upstream release (rhbz#1513788)

* Fri Dec 15 2017 Björn Esser <besser82@fedoraproject.org> - 2.4.1-4
- Add patch for changes in json-c >= 0.13

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.4.1-3
- Rebuilt for libjson-c.so.3

* Thu Oct 26 2017 Pavel Raiskup <praiskup@redhat.com> - 2.4.1-2
- upgrade: drop not-used /bin directory and liblwgeom (rhbz#1055293)
- upgrade: confess that we bundle postgis = prevversion

* Mon Oct 23 2017 Pavel Raiskup <praiskup@redhat.com> - 2.4.1-1
- update to 2.4.1, per NEWS file:
  https://svn.osgeo.org/postgis/tags/2.4.1/NEWS

* Wed Oct 18 2017 Pavel Raiskup <praiskup@redhat.com> - 2.4.0-2
- build against json-c again (rhbz#1484031)
- post/postun set for jdbc sub-package (rhbz#979685)

* Tue Oct 17 2017 Pavel Raiskup <praiskup@redhat.com> - 2.4.0-1
- install desktop files into /usr/share/applications
- optimize build without %%upgrade
- drop explicit requires on libraries (resolved by implicit lib*.so*())
- enable build testsuite
- disable hardening on f26 (all arches) and on s390x (all distros)

* Tue Oct 10 2017 Pavel Raiskup <praiskup@redhat.com> - 2.4.0-1
- provide postgis-upgrade package (rhbz#1475177)

* Mon Oct 09 2017 Pavel Raiskup <praiskup@redhat.com> - 2.4.0-1
- update to 2.4.0, per upstream release notes
  https://postgis.net/2017/09/30/postgis-2.4.0/

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 2 2017 Devrim Gündüz <devrim@gunduz.org> - 2.3.3-1
- Update to 2.3.3, per changes described at
  http://postgis.net/2017/07/01/postgis-2.3.3/
  rhbz #1467032

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Devrim Gündüz <devrim@gunduz.org> - 2.3.2-1
- Update to 2.3.2, per changes described at
  http://postgis.net/2017/01/31/postgis-2.3.2/
  rhbz#1418136

* Wed Jan 25 2017 Devrim Gündüz <devrim@gunduz.org> - 2.3.1-2
- Rebuild against Proj 4.9.3

* Wed Nov 30 2016 Devrim Gündüz <devrim@gunduz.org> - 2.3.1-1
- Update to 2.3.1, per changes described at
  http://postgis.net/2016/11/28/postgis-2.3.1
- Update previous version to 2.2.4
- Fix a few rpmlint warnings.

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 2.3.0-3
- bump: build in rawhide hit too early

* Fri Oct 07 2016 Petr Kubat <pkubat@redhat.com> - 2.3.0-2
- Rebuild for PostgreSQL 9.6.0

* Tue Sep 27 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 2.3.0-1
- Update to 2.3.0, per changes described at
  http://postgis.net/2016/09/26/postgis-2.3.0/

* Fri Mar 25 2016 Devrim Gündüz <devrim@gunduz.org> - 2.2.2-1
- Update to 2.2.2, per changes described at
  http://postgis.net/2016/03/22/postgis-2.2.2

* Mon Feb 15 2016 Pavel Raiskup <praiskup@redhat.com> - 2.2.1-3
- install address_standardizer module (rhbz#1307872)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Jozef Mlich <jmlich@redhat.com> - 2.2.1-1
- Rebuild to 2.2.1, per changes described at:
  http://svn.osgeo.org/postgis/tags/2.2.1/NEWS

* Sun Aug 30 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.8-2
- Rebuild again for GDAL 2.0

* Tue Jul 28 2015 Devrim Gündüz <devrim@gunduz.org> - 2.1.8-1
- Update to 2.1.8, per changes described at:
  http://svn.osgeo.org/postgis/tags/2.1.8/NEWS
- Rebuilt for GDAL 2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 1 2015 Devrim Gündüz <devrim@gunduz.org> - 2.1.7-1
- Update to 2.1.7, per changes described at:
  http://svn.osgeo.org/postgis/tags/2.1.7/NEWS

* Fri Mar 27 2015 Devrim Gündüz <devrim@gunduz.org> - 2.1.6-1
- Update to 2.1.6, per changes described at:
  http://postgis.net/2015/03/20/postgis-2.1.6

* Wed Mar 11 2015 Devrim Gündüz <devrim@gunduz.org> - 2.1.5-3
- Rebuild for Proj 4.9.1
- Add patch to fix FTBFS -- patch by Sandro Mani <manisandro@gmail.com>

* Thu Jan 08 2015 Jozef Mlich <jmlich@redhat.com> - 2.1.5-2
- disable json-c/geojson just for upgrade part of postgis

* Mon Dec 22 2014 Devrim Gündüz <devrim@gunduz.org> - 2.1.5-1
- Update to 2.1.5, per changes described at:
  http://postgis.net/2014/12/18/postgis-2.1.5 and
  http://postgis.net/2014/09/10/postgis-2.1.4

* Mon Aug 18 2014 Jozef Mlich <jmlich@redhat.com> - 2.1.3-5
- Dropped json-c because it is not building anymore
  Resolves: #1129292

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Jozef Mlich <jmlich@redhat.com> - 2.1.3-3
- Removing static libraries
  Resolves: #979179

* Mon Jun 09 2014 Jozef Mlich <jmlich@redhat.com> - 2.1.3-2
- removing sinjdoc from BuildRequires as it is not available
  in rawhide anymore

* Mon Jun 09 2014 Jozef Mlich <jmlich@redhat.com> - 2.1.3-1
- Rebase to 2.1.3 and 2.0.6 (security bugfixes, feature bugfixes)
  see http://svn.osgeo.org/postgis/tags/2.1.3/NEWS
- json_c turned on
- installation of .so file of previous version moved into install section

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Devrim Gündüz <devrim@gunduz.org> - 2.1.1-2
- Install postgis-2.0.so file, by compiling it from 2.0 sources
  Fixes bz #1055293.

* Thu Dec 12 2013 Devrim Gündüz <devrim@gunduz.org> - 2.1.1-1
- Update to 2.1.1

* Fri Oct 25 2013 Dan Horák <dan[at]danny.cz> - 2.1.0-2
- fix build on non-x86 64-bit arches

* Thu Sep 12 2013 Devrim Gündüz <devrim@gunduz.org> - 2.1.0-1
- Update to 2.1.0, per changes described at:
  http://svn.osgeo.org/postgis/tags/2.1.0/NEWS

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-4
- Rebuild for gdal 1.10.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0.3-2
- Perl 5.18 rebuild

* Wed Mar 6 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 2.0.3-1
- Update to 2.0.3, and build against GeOS 3.3.8.
- Update all URLs.

* Fri Jan 25 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 2.0.2-2
- Rebuilt against geos 3.3.7.
- Apply changes for PostgreSQL 9.2 and extensions.

* Wed Jan 16 2013 Devrim GÜNDÜZ <devrim@gunduz.org> - 2.0.2-1
- Update to 2.0.2, for various changes described at:
  http://www.postgis.org/news/20121203/

* Tue Nov 13 2012 Devrim GÜNDÜZ <devrim@gunduz.org> - 2.0.1-1
- Update to 2.0.1, so it works against PostgreSQL 9.2,
  which also fixes #872710.
- Add deps for gdal.
- Don't build JDBC portions. I have already disabled it in
  upstream packaging 8 months ago.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 4 2011 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.5.3-2
- Provide postgis.jar instead of provide postgis-1.5.2.jar,
  per #714856

* Tue Oct 4 2011 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.5.3-1
- Update to 1.5.3

* Tue Apr 19 2011 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.5.2-1
- Update to 1.5.2

* Sun Apr 03 2011 Nils Philippsen <nils@redhat.com> - 1.5.1-3
- cope with PostgreSQL 9.0 build environment
- require pgsql version used for building

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 11 2010 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.5.1-1
- Update to 1.5.1

* Tue Jan 12 2010 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.5.0-1
- Update to 1.5.0
- Trim changelog a bit.

* Wed Jan 6 2010 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.4.1-2
- Add shp2pgsql-{cli-gui} among installed files.

* Sun Dec 20 2009 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.4.1-1
- Update to 1.4.1

* Thu Dec 03 2009 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.4.1-rc2_1.2
- Fix spec per rawhide report.

* Tue Dec 01 2009 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.4.1-rc2_1.1
- Update spec for rc2 changes.

* Mon Nov 30 2009 Devrim GUNDUZ <devrim@gunduz.org> - 1.4.1rc2-1
- Update to 1.4.1rc2

* Mon Nov 23 2009 Devrim GUNDUZ <devrim@gunduz.org> - 1.4.1rc1-1
- Update to 1.4.1rc1

* Sun Nov 22 2009 Devrim GÜNDÜZ <devrim@gunduz.org> - 1.4.0-2
- Fix spec, per bz #536860

* Mon Jul 27 2009 Devrim GUNDUZ <devrim@gunduz.org> - 1.4.0-1
- Update to 1.4.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 6 2009 Devrim GUNDUZ <devrim@gunduz.org> - 1.4.0rc1-1
- Update to 1.4.0rc1
- Fix spec for 1.4
