#
##
# Default values are --with empty --with sqlite3 --with mysql --with postgresql
#                    --with odbc --without oracle 
# Note that, for Oracle, when enabled, the following options should
# also be given:
# --with-oracle-include=/opt/oracle/app/oracle/product/11.1.0/db_1/rdbms/public
# --with-oracle-lib=/opt/oracle/app/oracle/product/11.1.0/db_1/lib
# If the macros are defined, redefine them with the correct compilation flags.
%bcond_without empty
%bcond_without sqlite3
%bcond_without mysql
%bcond_without postgresql
%bcond_without odbc
%bcond_with oracle

%global _default_oracle_dir /opt/oracle/app/oracle/product/11.1.0/db_1
%{!?_with_oracle_incdir: %define _with_oracle_incdir --with-oracle-include=%{_default_oracle_dir}/rdbms/public}
%{!?_with_oracle_libdir: %define _with_oracle_libdir --with-oracle-lib=%{_default_oracle_dir}/lib}
#
##
#
Name:           soci
Version:        4.0.1.alpha2
%global ups_ver 4.0.1-alpha2
Release:        5%{?dist}
Summary:        The database access library for C++ programmers
License:        Boost
URL:            https://github.com/SOCI/%{name}
Source0:        %{url}/archive/%{ups_version}.tar.gz#/%{name}-%{version}.tar.gz

# Upstream issue: https://github.com/SOCI/soci/pull/815
#Patch0:         soci-werror.patch
# Works around a false positive -Wuninitialized error exposed by LTO
Patch1:		soci-uninit.patch

BuildRequires:  dos2unix
BuildRequires:  gcc gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel

%description
%{name} is a C++ database access library that provides the
illusion of embedding SQL in regular C++ code, staying entirely within
the C++ standard.


%{?with_sqlite3:%package        sqlite3
Summary:        SQLite3 back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  sqlite-devel

%description    sqlite3
This package contains the SQLite3 back-end for %{name}, i.e.,
dynamic library specific to the SQLite3 database. If you would like to
use %{name} in your programs with SQLite3, you will need to
install %{name}-sqlite3.}

%{?with_mysql:%package        mysql
Summary:        MySQL back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  mysql-devel

%description    mysql
This package contains the MySQL back-end for %{name}, i.e.,
dynamic library specific to the MySQL database. If you would like to
use %{name} in your programs with MySQL, you will need to
install %{name}-mysql.}

%{?with_postgresql:%package        postgresql
Summary:        PostGreSQL back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  libpq-devel

%description    postgresql
This package contains the PostGreSQL back-end for %{name}, i.e.,
dynamic library specific to the PostGreSQL database. If you would like
to use %{name} in your programs with PostGreSQL, you will need to
install %{name}-postgresql.}

%{?with_odbc:%package        odbc
Summary:        ODBC back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  unixODBC-devel

%description    odbc
This package contains the ODBC back-end for %{name}, i.e.,
dynamic library specific to the ODBC connectors. If you would like to
use %{name} in your programs with ODBC, you will need to
install %{name}-odbc.}

%{?with_oracle:%package        oracle
Summary:        Oracle back-end for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    oracle
This package contains the Oracle back-end for %{name}, i.e.,
dynamic library specific to the Oracle database. If you would like to
use %{name} in your programs with Oracle, you will need to install
%{name}-oracle.}


%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, dynamic libraries and
development documentation for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%{?with_sqlite3:%package        sqlite3-devel
Summary:        SQLite3 back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-sqlite3 = %{version}-%{release}
Requires:       sqlite-devel

%description    sqlite3-devel
This package contains the SQLite3 back-end for %{name}, i.e., header
files and dynamic libraries specific to the SQLite3 database. If you
would like to develop programs using %{name} and SQLite3, you will need
to install %{name}-sqlite3.}

%{?with_mysql:%package        mysql-devel
Summary:        MySQL back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-mysql = %{version}-%{release}
Requires:       mysql-devel

%description    mysql-devel
This package contains the MySQL back-end for %{name}, i.e., header
files and dynamic libraries specific to the MySQL database. If you
would like to develop programs using %{name} and MySQL, you will need
to install %{name}-mysql.}

%{?with_postgresql:%package        postgresql-devel
Summary:        PostGreSQL back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-postgresql = %{version}-%{release}
Requires:       libpq-devel

%description    postgresql-devel
This package contains the PostGreSQL back-end for %{name}, i.e., header
files and dynamic libraries specific to the PostGreSQL database. If
you would like to develop programs using %{name} and PostGreSQL, you
will need to install %{name}-postgresql.}

%{?with_odbc:%package        odbc-devel
Summary:        ODBC back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-odbc = %{version}-%{release}
Requires:       unixODBC-devel

%description    odbc-devel
This package contains the Odbc back-end for %{name}, i.e., header
files and dynamic libraries specific to the Odbc database. If you
would like to develop programs using %{name} and Odbc, you will need
to install %{name}-odbc.}

%{?with_oracle:%package        oracle-devel
Summary:        Oracle back-end for %{name}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-oracle = %{version}-%{release}

%description    oracle-devel
This package contains the Oracle back-end for %{name}, i.e., header
files and dynamic libraries specific to the Oracle database. If you
would like to develop programs using %{name} and Oracle, you will need
to install %{name}-oracle.}


%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
#BuildRequires:  tex(latex)
#BuildRequires:  doxygen, ghostscript

%description    doc
This package contains the documentation in the HTML format of the %{name}
library. The documentation is the same as at the %{name} web page.


%prep
%setup -q -n %{name}-%{ups_ver}
#%%patch -p1
%patch1 -p1

# Rename change-log and license file, so that they comply with
# packaging standard
mv README.md README
mv CHANGES ChangeLog
mv LICENSE_1_0.txt COPYING
echo "2019-11-09:" > NEWS
echo "- Version 4.0.0" >> NEWS
echo "- See the ChangeLog file for more details." >> NEWS
# Remove the spurious executable permission
chmod a-x AUTHORS README ChangeLog COPYING NEWS
find docs -type f -exec chmod a-x {} \;
# Unix ends of line
dos2unix AUTHORS README ChangeLog COPYING NEWS

%build
# Support for building tests.
%define soci_testflags -DBUILD_TESTS="NONE"
%if %{with tests}
  %define soci_testflags -DSOCI_TEST=ON \
   -DSOCI_TEST_EMPTY_CONNSTR="dummy" \
   -DSOCI_TEST_SQLITE3_CONNSTR="test.db" \
   -DSOCI_TEST_POSTGRESQL_CONNSTR:STRING="dbname=soci_test" \
   -DSOCI_TEST_MYSQL_CONNSTR:STRING="db=soci_test user=mloskot password=pantera"
%endif

%cmake \
 -DSOCI_CXX11=ON \
 -DSOCI_EMPTY=%{?with_empty:ON}%{?without_empty:OFF} \
 -DSOCI_SQLITE3=%{?with_sqlite3:ON}%{?without_sqlite3:OFF} \
 -DSOCI_POSTGRESQL=%{?with_postgresql:ON}%{?without_postgresql:OFF} \
 -DSOCI_MYSQL=%{?with_mysql:ON}%{?without_mysql:OFF} \
 -DSOCI_ODBC=%{?with_odbc:ON}%{?without_odbc:OFF} \
 -DWITH_ORACLE=%{?with_oracle:ON %{?_with_oracle_incdir} %{?_with_oracle_libdir}}%{?without_oracle:OFF} \
 %{soci_testflags} 
%cmake_build

%install
%cmake_install

# CMake helpers 
mkdir -p %{buildroot}%{_datadir}/%{name}
mv -f %{buildroot}%{_prefix}/cmake %{buildroot}%{_datadir}/%{name}/CMake

# Remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.a

%ldconfig_scriptlets

%{?with_sqlite3:%ldconfig_scriptlets sqlite3}

%{?with_mysql:%ldconfig_scriptlets mysql}

%{?with_postgresql:%ldconfig_scriptlets postgresql}

%{?with_odbc:%ldconfig_scriptlets odbc}

%{?with_oracle:%ldconfig_scriptlets oracle}



%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_core.so.*
%{?with_empty:%{_libdir}/lib%{name}_empty.so.*}

%{?with_sqlite3:%files sqlite3
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_sqlite3.so.*}

%{?with_mysql:%files mysql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_mysql.so.*}

%{?with_postgresql:%files postgresql
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_postgresql.so.*}

%{?with_odbc:%files odbc
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_odbc.so.*}

%{?with_oracle:%files oracle
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/lib%{name}_oracle.so.*}


%files devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*.h
%{?with_empty:%{_includedir}/%{name}/empty/}
%{_libdir}/lib%{name}_core.so
%{?with_empty:%{_libdir}/lib%{name}_empty.so}
%{_datadir}/%{name}/CMake

%{?with_sqlite3:%files sqlite3-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/sqlite3/
%{_libdir}/lib%{name}_sqlite3.so}

%{?with_mysql:%files mysql-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/mysql
%{_libdir}/lib%{name}_mysql.so}

%{?with_postgresql:%files postgresql-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/postgresql
%{_libdir}/lib%{name}_postgresql.so}

%{?with_odbc:%files odbc-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/odbc/
%{_libdir}/lib%{name}_odbc.so}

%{?with_oracle:%files oracle-devel
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/oracle
%{_libdir}/lib%{name}_oracle.so}


%files doc
%doc AUTHORS ChangeLog COPYING NEWS README docs

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.alpha2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.alpha2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Jeff Law <law@redhat.com> 4.0.1.alpha2-3
- Work around false positive uninitialized warning exposed by LTO

* Thu Jun 04 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> 4.0.1.alpha2-2
- C++-11 flag is now set to on by default

* Thu Jun 04 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> 4.0.1.alpha2-1
- Upstream update

* Thu Jun 04 2020 Denis Arnaud <denis.arnaud_fedora@m4x.org> 4.0.1.alpha1-1
- Attempt to rebuild on armv7hl
- Uptream update

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> 4.0.0-3
- Update to upstream release 4.0.0

* Tue Nov 05 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> 4.0.0-2
- Update to upstream release 4.0.0-rc2

* Sat Oct 26 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> 4.0.0-1
- Update to upstream release 4.0.0-rc1
- Slightly modernized the RPM spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-18
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-15
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-12
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-10
- Rebuilt for Boost 1.63

* Fri Jan 13 2017 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.2.3-9
- Fixed compilation issues with C++11 (deprecation of auto_ptr)

* Mon May 16 2016 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-8
- Rebuilt for linker errors in boost (#1331983)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.2.3-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.2.3-3
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.2.3-1
- Update to 3.2.3 (#1210126)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.2.2-5
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.2.2-2
- Rebuild for boost 1.55.0

* Sat Oct 19 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.2.2-1
- Upstream integration

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 3.2.1-2
- Rebuild for boost 1.54.0

* Mon May 20 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.2.1-1
- Upstream integration

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 31 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.1.0-1
- Upstream integration
- New CMake build system

* Sat Jul 23 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.0.0-23
- Rebuild for Boost-1.47.0-2

* Sun Jul 03 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.0.0-22
- Now links with the multi-threaded versions of the Boost libraries

* Mon Apr 25 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.0.0-21
- Rebuild for Boost-1.46.1-2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-19
- Fixed a compilation error with g++ 4.6 on default constructor definition
- Split the big patch into smaller pieces

* Tue Sep 07 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-18
- Fixed bug #631175 (https://bugzilla.redhat.com/show_bug.cgi?id=631175)

* Sat Jan 23 2010 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-16
- Added a missing cstring header include for g++-4.4 compatibility

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.0-15
- Rebuild for Boost soname bump

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 09 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-13
- Introduced distinct dependencies for different distributions

* Tue May 05 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-12
- Removed the dependency on the version of Boost, and on CPPUnit

* Tue May 05 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-11
- Removed the dependency on Latex for documentation delivery

* Tue May 05 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-10
- Burried the Boost Fusion header include for core/test/common-tests.h

* Tue May 05 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-9
- Added a missing cstdio header include for g++-4.4 compatibility

* Tue May 05 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-8
- Added missing cstdio header includes for g++-4.4 compatibility

* Tue May 05 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-7
- Added a missing cstdio header include for g++-4.4 compatibility

* Sat May 02 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-6
- Removed the unused build conditionals

* Tue Apr 28 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-5
- Simplified the conditional build rules within the RPM specification file

* Sat Apr 18 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-4
- Fixed an issue about OPTFLAGS compilation

* Tue Apr 14 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-3
- Restarted from pristine version 3.0.0 of upstream (SOCI) project

* Sat Apr  4 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-2
- Specific RPM for each back-end

* Fri Mar 27 2009 Denis Arnaud <denis.arnaud_fedora@m4x.org> 3.0.0-1
- First RPM release

