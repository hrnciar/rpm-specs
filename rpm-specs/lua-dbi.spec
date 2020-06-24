%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%{!?lua_libdir: %global lua_libdir %{_libdir}/lua/%{lua_version}}
%{!?lua_pkgdir: %global lua_pkgdir %{_datadir}/lua/%{lua_version}}

%{!?lua_compat_version: %global lua_compat_version 5.1}
%{!?lua_compat_libdir: %global lua_compat_libdir %{_libdir}/lua/%{lua_compat_version}}
%{!?lua_compat_pkgdir: %global lua_compat_pkgdir %{_datadir}/lua/%{lua_compat_version}}
%{!?lua_compat_builddir: %global lua_compat_builddir %{_builddir}/compat-lua-%{name}-%{version}-%{release}}

Summary:        Database interface library for Lua
Name:           lua-dbi
Version:        0.7.2
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/mwild1/luadbi
Source0:        https://github.com/mwild1/luadbi/archive/v%{version}/luadbi-%{version}.tar.gz
Patch0:         lua-dbi-0.7.2-sqlite36.patch
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires:       lua(abi) = %{lua_version}
%else
Requires:       lua >= %{lua_version}
%endif
BuildRequires:  gcc, lua-devel, sqlite-devel
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
BuildRequires:  mariadb-connector-c-devel
%else
BuildRequires:  mysql-devel
%endif
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
BuildRequires:  libpq-devel
%else
BuildRequires:  postgresql-devel
%endif

%description
LuaDBI is a database interface library for Lua. It is designed to provide a
RDBMS agnostic API for handling database operations. LuaDBI also provides
support for prepared statement handles, placeholders and bind parameters for
all database operations.

Currently LuaDBI supports DB2, Oracle, MySQL, PostgreSQL and SQLite databases
with native database drivers.

%if 0%{?fedora} >= 20
%package -n lua%{lua_compat_version}-dbi
Summary:        Database interface library for Lua %{lua_compat_version}
Obsoletes:      lua-dbi-compat < 0.7.2
Provides:       lua-dbi-compat = %{version}-%{release}
Provides:       lua-dbi-compat%{?_isa} = %{version}-%{release}
Requires:       lua(abi) = %{lua_compat_version}
BuildRequires:  compat-lua-devel >= %{lua_compat_version}

%description -n lua%{lua_compat_version}-dbi
LuaDBI is a database interface library for Lua %{lua_compat_version}. It is designed to provide
a RDBMS agnostic API for handling database operations. LuaDBI also provides
support for prepared statement handles, placeholders and bind parameters for
all database operations.

Currently LuaDBI supports DB2, Oracle, MySQL, PostgreSQL and SQLite databases
with native database drivers.
%endif

%prep
%setup -q -n luadbi-%{version}
%patch0 -p1 -b .sqlite36

%if 0%{?fedora} >= 20
rm -rf %{lua_compat_builddir}
cp -a . %{lua_compat_builddir}
%endif

%build
%make_build free \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} LUA_INC="-I%{_includedir}" \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"

%if 0%{?fedora} >= 20
pushd %{lua_compat_builddir}
%make_build free \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_compat_version} LUA_INC="-I%{_includedir}/lua-%{lua_compat_version}" \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"
popd
%endif

%install
make install_free INSTALL='install -p' \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} LUA_INC="-I%{_includedir}" \
  LUA_CDIR=$RPM_BUILD_ROOT%{lua_libdir} LUA_LDIR=$RPM_BUILD_ROOT%{lua_pkgdir} \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"

%if 0%{?fedora} >= 20
pushd %{lua_compat_builddir}
make install_free INSTALL='install -p' \
  CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_compat_version} LUA_INC="-I%{_includedir}/lua-%{lua_compat_version}" \
  LUA_CDIR=$RPM_BUILD_ROOT%{lua_compat_libdir} LUA_LDIR=$RPM_BUILD_ROOT%{lua_compat_pkgdir} \
  MYSQL_LDFLAGS="-L%{_libdir}/mysql -lmysqlclient"
popd
%endif

%files
%license COPYING
%doc README.md
%{lua_libdir}/dbd/
%{lua_pkgdir}/DBI.lua

%if 0%{?fedora} >= 20
%files -n lua%{lua_compat_version}-dbi
%license COPYING
%doc README.md
%{lua_compat_libdir}/dbd/
%{lua_compat_pkgdir}/DBI.lua
%endif

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Robert Scheck <robert@fedoraproject.org> 0.7.2-1
- Upgrade to 0.7.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Robert Scheck <robert@fedoraproject.org> 0.5-18
- Build against mariadb-connector-c-devel rather mysql-devel for
  Fedora >= 28 (#1493634, thanks to Michal Schorm)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Robert Scheck <robert@fedoraproject.org> 0.5-13
- Really build -compat subpackage against compat-lua (#1232688)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 0.5-11
- add all new upstream fixes
- rebuild for lua 5.3
- fix compile against modern pgsql

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Jan Kaluza <jkaluza@redhat.com> - 0.5-8
- build -compat subpackage against compat-lua

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 0.5-6
- rebuild for lua 5.2

* Fri Apr 26 2013 Robert Scheck <robert@fedoraproject.org> - 0.5-5
- Added upstream patch to avoid PostgreSQL transaction warnings

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Matej Cepl <mcepl@redhat.com> - 0.5-2
- Couple of fixes to satisfy packaging review.

* Mon May 23 2011 Matěj Cepl <mcepl@redhat.com> - 0.5-1
- Initial packaging
