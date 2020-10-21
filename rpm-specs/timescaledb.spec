Name:           timescaledb
Version:        1.7.4
Release:        1%{?dist}
Summary:        Open-source time-series database powered by PostgreSQL

License:        ASL 2.0
URL:            http://www.timescale.com
Source0:        %{name}-%{version}.tar.gz

%if 0%{?fedora} >= 30
BuildRequires:  cmake gcc openssl-devel postgresql-server-devel
%else
BuildRequires:  cmake gcc openssl-devel postgresql-devel
%endif

%{?postgresql_module_requires}

%description
TimescaleDB is an open-source database designed to make SQL scalable for
time-series data.  It is engineered up from PostgreSQL, providing automatic
partitioning across time and space (partitioning key), as well as full SQL
support.


%prep
%setup -q -n %{name}-%{version}
# Remove tsl directory containing sources licensed under Timescale license
rm -rf tsl 


%build
%if 0%{?fedora} >= 30
%cmake -DPROJECT_INSTALL_METHOD=fedora -DREGRESS_CHECKS=OFF -DAPACHE_ONLY=1 -DPG_CONFIG=%_bindir/pg_server_config
%else
%cmake -DPROJECT_INSTALL_METHOD=fedora -DREGRESS_CHECKS=OFF -DAPACHE_ONLY=1 -DPG_CONFIG=%_bindir/pg_config
%endif
%cmake_build


%install
%cmake_install


%files
%license LICENSE-APACHE
%doc README.md
%{_libdir}/pgsql/%{name}-%{version}.so
%{_libdir}/pgsql/%{name}.so
%{_datadir}/pgsql/extension/%{name}--*%{version}.sql
%{_datadir}/pgsql/extension/%{name}.control


%changelog
* Tue Sep 15 2020 Patrik Novotný <panovotn@redhat.com> - 1.7.4-1
- Rebase to upstream release 1.7.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Patrik Novotný <panovotn@redhat.com> - 1.7.1-1
- New upstream release 1.7.1

* Fri Apr 17 2020 Patrik Novotný <panovotn@redhat.com> - 1.7.0-1
- New upstream release 1.7.0

* Tue Mar 24 2020 Patrik Novotný <panovotn@redhat.com> - 1.6.1-2
- New upstream release 1.6.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Patrik Novotný <panovotn@redhat.com> - 1.5.1-1
- New upstream release 1.5.1

* Fri Nov 01 2019 Patrik Novotný <panovotn@redhat.com> - 1.5.0-1
- New upstream release 1.5.0

* Fri Sep 13 2019 Patrik Novotný <panovotn@redhat.com> - 1.4.2-1
- New upstream release 1.4.2

* Tue Aug 20 2019 Patrik Novotný <panovotn@redhat.com> - 1.4.1-1
- New upstream release: 1.4.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Patrik Novotný <panovotn@redhat.com> - 1.3.2-1
- New upstream release: 1.3.2

* Wed Jun 12 2019 Patrik Novotný <panovotn@redhat.com> - 1.3.1-1
- New upstream release: 1.3.1

* Tue May 07 2019 Patrik Novotný <panovotn@redhat.com> - 1.3.0-1
- New upstream version: 1.3.0

* Tue Mar 26 2019 Patrik Novotný <panovotn@redhat.com> - 1.2.2-2
- Add PROJECT_INSTALL_METHOD build flag for upstream telemetry

* Thu Mar 21 2019 Patrik Novotný <panovotn@redhat.com> - 1.2.2-1
- Rebase to usptream version 1.2.2

* Thu Jan 31 2019 Patrik Novotný <panovotn@redhat.com> - 1.2.0-1
- Update to upstream release 1.2.0

* Thu Jan 03 2019 Patrik Novotný <panovotn@redhat.com> - 1.1.0
- Update to upstream release 1.1.0

* Wed Sep 19 2018 panovotn@redhat.com - 0.12.0-1
- Upstream update to 0.12.0

* Wed Sep 05 2018 praiskup@redhat.com - 0.11.0-2
- rebuild against postgresql-server-devel (rhbz#1618698)

* Thu Aug  9 2018 Patrik Novotný <panovotn@redhat.com> - 0.11.0-1
- An upstream update to 0.11.0

* Tue Aug  7 2018 Patrik Novotný <panovotn@redhat.com> - 0.10.1-1
- Initial build
