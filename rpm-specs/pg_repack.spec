Name:           pg_repack
Version:        1.4.5
Release:        2%{?dist}
Summary:        Reorganize tables in PostgreSQL databases without any locks

License:        BSD
URL:            http://reorg.github.io/%{name}/
Source0:        https://github.com/reorg/%{name}/archive/ver_%{version}.tar.gz

BuildRequires:  postgresql, gcc, openssl-devel, postgresql-server
BuildRequires:  postgresql-libs, postgresql-devel
BuildRequires:  readline-devel, zlib-devel, postgresql-static
BuildRequires:  python3-docutils
%{?postgresql_module_requires}

%description
pg_repack is a PostgreSQL extension which lets you remove
bloat from tables and indexes, and optionally
restore the physical order of clustered indexes.
Unlike CLUSTER and VACUUM FULL it works online,
without holding an exclusive lock on the processed tables during processing.
pg_repack is efficient to boot,
with performance comparable to using CLUSTER directly.

Please check the documentation (in the doc directory or online)
for installation and usage instructions.
%prep
%setup -n %{name}-ver_%{version} -q


%build

make %{?_smp_mflags}
cd doc
make


%install
%make_install

%files
%{_bindir}/%{name}
%{_libdir}/pgsql/%{name}.so
%{_libdir}/pgsql/bitcode/%{name}.index.bc
%{_libdir}/pgsql/bitcode/%{name}/pgut/pgut-spi.bc
%{_libdir}/pgsql/bitcode/%{name}/repack.bc
%{_datadir}/pgsql/extension/%{name}.control
%{_datadir}/pgsql/extension/%{name}--%{version}.sql

%license COPYRIGHT

%doc README.rst
%doc doc/%{name}.html
%doc doc/%{name}.rst
%doc doc/%{name}_jp.html
%doc doc/%{name}_jp.rst
%doc doc/release.html
%doc doc/release.rst


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Aug 21 2019 Filip Januš <fjanus@redhat.com> 1.4.5-1
- Initial packaging
