Summary: A simple fuzz test-case builder
Name: Simple-Fuzzer
Version: 0.7.1
Release: 12%{?dist}
License: BSD
URL: http://aconole.bytheb.org/programs/sfuzz.html
Source: http://aaron.bytheb.org/files/sfuzz-0.7-dist/sfuzz-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: openssl openssl-devel
Requires: openssl

Patch1: 0001-sfuzz-cleanup-snprintfs.patch
Patch2: 0001-configure-disable-snoop-on-OS-X.patch
Patch3: 0001-configure-Use-r-for-sed.patch
Patch4: 0001-array_fuzz-Fix-a-sizeof-issue.patch
Patch5: 0001-url-change-to-bytheb.org.patch

%description
Simple-Fuzzer (sfuzz) is a simplistic fuzz test case generator.
It is a generation-based fuzzer, intended to aid in fault finding.

%package devel
Summary: Simple Fuzzer development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the headers and other files needed for developing
plugins for Simple Fuzzer

%prep
%setup -q -n sfuzz-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure --force-symbols --aux-search-path=%{_libdir}/simple-fuzzer
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}/simple-fuzzer/
mv %{buildroot}%{_datadir}/sfuzz-db/*.so %{buildroot}%{_libdir}/simple-fuzzer/

%files
%{_bindir}/*
%{_datadir}/man/man1/*
%{_datadir}/sfuzz-db/basic.*
%{_datadir}/sfuzz-db/*.list
%{_datadir}/sfuzz-db/*.inc
%{_datadir}/sfuzz-db/server.*
%{_datadir}/sfuzz-db/*.test
%{_datadir}/sfuzz-db/*.0day
%{_datadir}/sfuzz-db/*.cfg
%{_libdir}/simple-fuzzer/*

%files devel
%{_datadir}/sfuzz-db/*.c

%license LICENSING

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Aaron Conole <aconole@redhat.com> - 0.7.1-9
- Update the requires and buildrequires to explicitly include openssl and gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Aaron Conole <aconole@redhat.com> - 0.7.1-4
- Fix a sizeof issue from the previous bug.
- Change the urls
- Fix configure

* Fri Feb 17 2017 Aaron Conole <aconole@redhat.com> - 0.7.1-3
- Fix FTBFS (#1423185)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Aaron Conole <aconole@bytheb.org> - 0.7.1-1
- Second RPM spec build
- Cleanup the spec file, add manpages

* Sat Mar  3 2012 Aaron Conole <aconole@bytheb.org> - 0.7.0-0
- First RPM spec build
