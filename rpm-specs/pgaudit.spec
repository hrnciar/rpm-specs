Name:		pgaudit
Version:	1.4.0
Release:	1%{?dist}
Summary:	PostgreSQL Audit Extension

License:	PostgreSQL
URL:		http://pgaudit.org

Source0:	https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	postgresql-server-devel >= 12, postgresql-server-devel < 13
BuildRequires:	openssl-devel
BuildRequires:	clang-devel
BuildRequires:	llvm-devel

%{?postgresql_module_requires}

%description
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.


%prep
%setup -q -n %{name}-%{version}


%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%install
%make_install USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{name}.so
%{_libdir}/pgsql/bitcode/%{name}.index.bc
%{_libdir}/pgsql/bitcode/%{name}/%{name}.bc
%{_datadir}/pgsql/extension/%{name}--1.4.sql
%{_datadir}/pgsql/extension/%{name}.control


%changelog
* Fri Mar 13 2020 Devrim Gündüz <devrim@gunduz.org> - 1.4.0-1
- Update to 1.4.0 for PostgreSQL 12 support

* Sun Mar 08 2020 Patrik Novotný <panovotn@redhat.com> - 1.3.0-5
- Rebuild for PostgreSQL 12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Petr Kubat <pkubat@redhat.com> - 1.3.0-1
- rebase to latest upstream release

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 1.2.0-4
- rebuild against postgresql-server-devel (rhbz#1618698)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 - Filip Čáp <ficap@redhat.com> 1.2.0-1
- Initial RPM packaging for Fedora
- Based on Devrim Gündüz's packaging for PostgreSQL RPM Repo

* Thu Oct 27 2016 - Devrim Gündüz <devrim@gunduz.org> 1.0.0-1
- Update to 1.0.0

* Fri Oct 21 2016 - Devrim Gündüz <devrim@gunduz.org> 0.0.4-1
- Initial RPM packaging for PostgreSQL RPM Repository
