Name:		sqliteodbc
Version:	0.9996
Release:	7%{?dist}
Summary:	SQLite ODBC Driver

License:	BSD
URL:		http://www.ch-werner.de/sqliteodbc
Source:		http://www.ch-werner.de/sqliteodbc/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	libxml2-devel
BuildRequires:	sqlite-devel
BuildRequires:	sqlite2-devel
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel
BuildRequires:	%{_bindir}/iconv

Requires:	%{_bindir}/odbcinst


%description
ODBC driver for SQLite interfacing SQLite 2.x and/or 3.x using the
unixODBC or iODBC driver managers. For more information refer to:
- http://www.sqlite.org    -  SQLite engine
- http://www.unixodbc.org  -  unixODBC Driver Manager
- http://www.iodbc.org     -  iODBC Driver Manager


%prep
%setup -q
# correct EOL
for i in README; do
	sed 's#\r##g' $i > $i.tmp && \
	touch -r $i $i.tmp && \
	mv $i.tmp $i
done

# Convert encoding to UTF-8
for i in ChangeLog; do
	iconv -f ISO-8859-1 -t UTF-8 -o $i.tmp $i && \
	touch -r $i $i.tmp && \
	mv $i.tmp $i
done


%build
%configure
make %{_smp_mflags}


%install
mkdir -p %{buildroot}%{_libdir}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libsqliteodbc*.{a,la}
rm -f %{buildroot}%{_libdir}/libsqlite3odbc*.{a,la}
rm -f %{buildroot}%{_libdir}/libsqlite3_mod_*.{a,la}
# install example file
cat > odbc.ini.sample <<- 'EOD'
	# ~/.odbc.ini example file
	[mysqlitedb]
	Description=My SQLite3 test database
	Driver=SQLite3
	Database=/home/user_name/Documents/databases/testdb.sqlite
	# optional lock timeout in milliseconds
	# Timeout=2000
	# StepAPI = No|Yes
	# ShortNames = No|Yes
	# FKSupport = No|Yes
	# SyncPragma = NORMAL|OFF|FULL
	# JournalMode = WAL|MEMORY|TRUNCATE|OFF|PERSIST|DELETE
	# BigInt = No|Yes
EOD

%post
/sbin/ldconfig
if [ -x %{_bindir}/odbcinst ] ; then
	INST=$(%{_bindir}/mktemp)

	if [ -r %{_libdir}/libsqliteodbc.so ] ; then
		%{_bindir}/cat > $INST <<- 'EOD'
			[SQLITE]
			Description=SQLite ODBC 2.X
			Driver=%{_libdir}/libsqliteodbc.so
			Setup=%{_libdir}/libsqliteodbc.so
			Threading=2
			FileUsage=1
		EOD

		%{_bindir}/odbcinst -q -d -n SQLITE | %{_bindir}/grep '^\[SQLITE\]' >/dev/null || {
			%{_bindir}/odbcinst -i -d -n SQLITE -f $INST || true
		}

		%{_bindir}/cat > $INST <<- 'EOD'
			[SQLite Datasource]
			Driver=SQLITE
		EOD

		%{_bindir}/odbcinst -q -s -n "SQLite Datasource" | \
		%{_bindir}/grep '^\[SQLite Datasource\]' >/dev/null || {
			%{_bindir}/odbcinst -i -l -s -n "SQLite Datasource" -f $INST || true
		}
	fi

	if [ -r %{_libdir}/libsqlite3odbc.so ] ; then
		%{_bindir}/cat > $INST <<- 'EOD'
			[SQLITE3]
			Description=SQLite ODBC 3.X
			Driver=%{_libdir}/libsqlite3odbc.so
			Setup=%{_libdir}/libsqlite3odbc.so
			Threading=2
			FileUsage=1
		EOD

		%{_bindir}/odbcinst -q -d -n SQLITE3 | %{_bindir}/grep '^\[SQLITE3\]' >/dev/null || {
			%{_bindir}/odbcinst -i -d -n SQLITE3 -f $INST || true
		}

		%{_bindir}/cat > $INST <<- 'EOD'
			[SQLite3 Datasource]
			Driver=SQLITE3
		EOD

		%{_bindir}/odbcinst -q -s -n "SQLite3 Datasource" | \
		%{_bindir}/grep '^\[SQLite3 Datasource\]' >/dev/null || {
			%{_bindir}/odbcinst -i -l -s -n "SQLite3 Datasource" -f $INST || true
		}
	fi

	%{_bindir}/rm -f $INST || true
fi


%preun
if [ "$1" = "0" ] ; then
	test -x %{_bindir}/odbcinst && {
		%{_bindir}/odbcinst -u -d -n SQLITE || true
		%{_bindir}/odbcinst -u -l -s -n "SQLite Datasource" || true
		%{_bindir}/odbcinst -u -d -n SQLITE3 || true
		%{_bindir}/odbcinst -u -l -s -n "SQLite3 Datasource" || true
	}

	true
fi


%postun -p /sbin/ldconfig


%files
%license license.terms
%doc README ChangeLog odbc.ini.sample
%{_libdir}/*.so*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9996-6
- Fix CVE-2020-12050 (use mktemp(1) for temp. file name creation)
- Use absolute paths for binaries

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9996-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9996-1
- Update to the latest available version.

* Sat Feb 24 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9995-5
- Add missing BR (gcc)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9995-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9995-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9995-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9995-1
- Update to the latest available version.
- Start using %%license

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9994-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9994-1
- Update to the latest available version.

* Tue Sep 23 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.999-1
- Initial package.
