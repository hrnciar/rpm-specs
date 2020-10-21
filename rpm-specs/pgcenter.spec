# Review request: https://bugzilla.redhat.com/show_bug.cgi?id=1302053
Summary:            Top-like PostgreSQL statistics viewer
Name:               pgcenter
Version:            0.3.0
Release:            10%{?dist}
License:            BSD
URL:                https://github.com/lesovsky/pgcenter

Source0:            https://github.com/lesovsky/%{name}/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:      libpq-devel ncurses-devel

%description
PostgreSQL provides various statistics which includes information about
tables, indexes, functions and other database objects and their usage.
Moreover, statistics has detailed information about connections, current
queries and database operations (INSERT/DELETE/UPDATE). But most of this
statistics are provided as permanently incremented counters. The pgcenter
provides convenient interface to this statistics and allow viewing statistics
changes in time interval, e.g. per second. The pgcenter provides fast access
for database management task, such as editing configuration files, reloading
services, viewing log files and canceling or terminating database backends
(by pid or using state mask). However if need execute some specific
operations, pgcenter can start psql session for this purposes.

%prep
%setup -qn %{name}-%{version}

%build
make %{?_smp_mflags} NCONFIG='%(ls %{_bindir}/ncurses[56]-config)'

%install
%{make_install}
install -Dpm 644 doc/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license COPYRIGHT
%doc README.md doc/Changelog
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 02 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 0.3.0-1
- Update by mail author request to version 0.3.0.

* Sat Feb 06 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 0.2.0-3
- Package approved to Fedora.
- Add doc/Changelog and man page as suggested.

* Fri Jan 29 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 0.2.0-2
- In rawhide ncurses 6 landed. Account both 5 and 6.
- Use %%license for COPYRIGHT file.

* Mon Jan 25 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 0.2.0-1
- Import http://testing.yum.kaos.io/SRPMS/repoview/pgcenter.html
- Change BR postgresql94-devel -> postgresql-devel
- Spec cleanup and full rewrite.

* Sat Dec 19 2015 Anton Novojilov <andy@essentialkaos.com> - 0.2.0-0
- Added iostat
- Added nicstat
- pg_stat_statements fixes
- One key shortcut for config editing
- Other fixes and improvements

* Wed Oct 21 2015 Anton Novojilov <andy@essentialkaos.com> - 0.1.3-0
- Added pg_stat_statements improvements
- Added query detailed report based on pg_stat_statements
- Added memory system statistics
- Added support for 9.1

* Wed Sep 09 2015 Anton Novojilov <andy@essentialkaos.com> - 0.1.2-0
- Initial build
