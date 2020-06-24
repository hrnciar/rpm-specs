%define luaver 5.3
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%global commit 2f2c4eb81685440968d6b238a827c09745a6d2d1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lua-sql
Version:        2.3.5
Release:        11%{?dist}
Summary:        Database connectivity for the Lua programming language

License:        MIT
URL:            http://www.keplerproject.org/luasql/
Source0:        https://github.com/keplerproject/luasql/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch1:		luasql-mariadb.patch

BuildRequires:  gcc
BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel >= 3.0
BuildRequires:  mariadb-connector-c-devel openssl-devel
BuildRequires:  libpq-devel

Requires:       lua-sql-sqlite, lua-sql-mysql, lua-sql-postgresql, lua-sql-doc

%description
LuaSQL is a simple interface from Lua to a DBMS. This package of LuaSQL
supports MySQL, SQLite and PostgreSQL databases. You can execute arbitrary SQL
statements and it allows for retrieving results in a row-by-row cursor fashion.

%package doc
Summary:        Documentation for LuaSQL
Requires:       lua >= %{luaver}
%description doc
LuaSQL is a simple interface from Lua to a DBMS. This package contains the
documentation for LuaSQL.


%package sqlite
Summary:        SQLite database connectivity for the Lua programming language
Requires:       lua >= %{luaver}
%description sqlite
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to SQLite databases.


%package mysql
Summary:        MySQL database connectivity for the Lua programming language
Requires:       lua >= %{luaver}
%description mysql
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to MySQL databases.


%package postgresql
Summary:        PostgreSQL database connectivity for the Lua programming language
Requires:       lua >= %{luaver}
%description postgresql
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to PostgreSQL databases.


%prep
%setup -q -n luasql-%{commit}
%patch1 -p1

%build
make %{?_smp_mflags} sqlite3 PREFIX=%{_prefix} DRIVER_INCS_sqlite3="`pkg-config --cflags sqlite3`" DRIVER_LIBS_sqlite3="`pkg-config --libs sqlite3`" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS"
make %{?_smp_mflags} postgres PREFIX=%{_prefix} DRIVER_INCS_postgres="" DRIVER_LIBS_postgres="-lpq" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS" WARN=
make %{?_smp_mflags} mysql PREFIX=%{_prefix} DRIVER_INCS_mysql="`mysql_config --include`" DRIVER_LIBS_mysql="`mysql_config --libs`" DEFS="%{optflags} -fPIC -std=c99 -DLUA_COMPAT_APIINTCASTS"


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT%{luapkgdir} T=sqlite3
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT%{luapkgdir} T=postgres
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT%{luapkgdir} T=mysql



%files
# There are no files in the main package

%files doc
%doc README
%doc doc/us/*

%files sqlite
%dir %{lualibdir}/luasql
%{lualibdir}/luasql/sqlite3.so

%files mysql
%dir %{lualibdir}/luasql
%{lualibdir}/luasql/mysql.so

%files postgresql
%dir %{lualibdir}/luasql
%{lualibdir}/luasql/postgres.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Tim Niemueller <tim@niemueller.de> - 2.3.5-7
- Depend on MariaDB package (bz #1493688)
- BR gcc

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.5-6
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 2.3.5-3
- Rebuild with binutils fix for ppc64le (#1475636)
- Fix build failure with MariaDB

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Adam Williamson <awilliam@redhat.com> - 2.3.5-1
- New release 2.3.5
- Rebuild against MariaDB 10.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 2.3.0-5
- rebuild for lua 5.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Tom Callaway <spot@fedoraproject.org> - 2.3.0-1
- update to 2.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 2.2.0-2
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Mar 22 2011 Tim Niemueller <tim@niemueller.de> - 2.2.0-1
- Upgrade to latest stable release 2.2.0
- Rebuilt for MySQL 5.5
- Added patch for F-14 and up

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Tim Niemueller <tim@niemueller.de> - 2.1.1-5
- Rebuilt for MySQL 5.1

* Tue Apr 08 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-4
- Main package is now pure meta package to pull in everything else, README
  moved to doc sub-package.

* Sat Apr 05 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-3
- Do not use pg_config and mysql_config, they are not good for what you think
  they should be used for, cf. #440673

* Fri Apr 04 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-2
- Fixed lua-sql-postgres requires
- Own %%{lualibdir}/luasql directory in all sub-packages

* Fri Apr 04 2008 Tim Niemueller <tim@niemueller.de> - 2.1.1-1
- Initial package

