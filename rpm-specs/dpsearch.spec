%global snapshot 2016-12-03
Name:           dpsearch
Version:        4.54
Release:        0.19.20161203snap%{?dist}
Summary:        DataparkSearch Engine

License:        GPLv2+
URL:            http://www.dataparksearch.org
Source0:        https://github.com/Maxime2/dataparksearch/archive/%{version}-2016-12-03.tar.gz
# already upstream patch for cmode not being available
Patch1:         https://github.com/Maxime2/dataparksearch/commit/0bddc2771b4a68e07a6b09190354f34cd4a734e6.patch
Source1:        dpsearch.conf
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  zlib-devel
BuildRequires:  aspell-devel
BuildRequires:  tre-devel
BuildRequires:  c-ares-devel
BuildRequires:  bind-devel
BuildRequires:  readline-devel
BuildRequires:  httpd-devel
BuildRequires:  php-devel
BuildRequires:  libidn-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
Requires:       openssl

%description
DataparkSearch Engine is a full-featured open source web-based
search engine released under the GNU General Public License
and designed to organize search within a website, group of
websites, intranet or local system. 

%package devel
Summary:        Development files for the DataparkSearch Engine
Requires:       dpsearch = %{version}-%{release}

%description devel
C development and header files for the DataparkSearch Engine.

%prep
%setup -q -n dataparksearch-%{version}-%{snapshot}

%patch1 -p1

%build
./configure \
--with-mysql \
--with-pgsql \
--prefix=%{_prefix} \
--libdir=%{_libdir}/%{name} \
--bindir=%{_bindir} \
--sbindir=%{_sbindir} \
--includedir=%{_prefix}/include/%{name} \
--datarootdir=%{_datadir}/%{name} \
--docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}} \
--sysconfdir=%{_sysconfdir}/%{name} \
--with-openssl=%{_prefix}/include/openssl
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
rm %{buildroot}/%{_libdir}/%{name}/*.a
rm %{buildroot}/%{_libdir}/%{name}/*.la

mkdir -p %{buildroot}/%{_libdir}/%{name}-cgi/
mv %{buildroot}/%{_bindir}/{filler,search,storedoc}.cgi %{buildroot}/%{_libdir}/%{name}-cgi/

install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

%files
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%{_datadir}/%{name}
%{_sbindir}/cached
%{_sbindir}/dpconv
%{_sbindir}/dpguesser
%{_sbindir}/dpurl2text
%{_sbindir}/indexer
%{_sbindir}/run-splitter
%{_sbindir}/searchd
%{_sbindir}/splitter
%{_sbindir}/stored
%{_bindir}/dps-config
%{_libdir}/%{name}-cgi/filler.cgi
%{_libdir}/%{name}-cgi/search.cgi
%{_libdir}/%{name}-cgi/storedoc.cgi

%files devel
%{_prefix}/include/%{name}
%{_libdir}/%{name}

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.19.20161203snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.18.20161203snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.17.20161203snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.16.20161203snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 4.54-0.15.20161203snap
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.14.20161203snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.13.20161203snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 4.54-0.12.20161203snap
- Rebuilt for switch to libxcrypt

* Wed Dec 13 2017 Kevin Fenzi <kevin@scrye.com> - 4.54-0.11.20140109snap
- Rebuild to use mariadb-connector-c-devel. Fixes #1494075

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.10.20140109snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.9.20140109snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.8.20140109snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.54-0.7.20140109snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 24 2015 Kevin Fenzi <kevin@scrye.com> - 4.54-0.6.20140109snap
- Update to 2014-01-09 snapshot

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.54-0.5.20131107snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.54-0.4.20131107snap
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.54-0.3.20131107snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.54-0.2.20131107snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 09 2013 Ricky Elrod <codeblock@fedoraproject.org> - 4.54-0.1.20131109snap
- Latest upstream snapshot.

* Thu Sep 19 2013 Ricky Elrod <codeblock@fedoraproject.org> - 4.54-0.1.20130919snap
- Latest upstream snapshot.
- New docdir for https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.54-0.7.20120611snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.54-0.6.20120611snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.54-0.5.20120611snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Ricky Elrod <codeblock@fedoraproject.org> - 4.54-0.4.20120611snap
- Latest upstream snapshot.

* Fri Jun 01 2012 Ricky Elrod <codeblock@fedoraproject.org> - 4.54-0.3.20120317snap
- Latest upstream snapshot.

* Wed Feb 22 2012 Ricky Elrod <codeblock@fedoraproject.org> - 4.54-0.2.20120221snap
- Relocate CGI's.

* Mon Feb 20 2012 Ricky Elrod <codeblock@fedoraproject.org> - 4.54-0.1.20120221snap
- Fixed how the -devel subpackage requires the non-devel package.
- Update to latest snapshot.
- Enable openssl compilation. The dpsearch README file adds a licensing exception, making this okay.

* Fri Feb 17 2012 Ricky Elrod <codeblock@fedoraproject.org> - 4.54-0.1.20120215snap
- Initial build.
