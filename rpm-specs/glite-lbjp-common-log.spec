%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           glite-lbjp-common-log
Version:        1.3.11
Release:        12%{?dist}
Summary:        Definitions of glite common logging formats for LB and JP

License:        ASL 2.0
URL:            http://glite.cern.ch
Source:         http://scientific.zcu.cz/emi/emi.lbjp-common.log/%{name}-%{version}.tar.gz

BuildRequires:  libtool
BuildRequires:  log4c-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  pkgconfig

%description
Definitions of glite common logging formats for LB and JP.


%package        devel
Summary:        Development files for gLite L&B/JP common log module
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development libraries and header files for gLite L&B/JP
common log module.


%prep
%setup -q


%build
perl ./configure --root=/ --prefix=%{_prefix} --libdir=%{_lib} --docdir=%{_pkgdocdir}
CFLAGS="%{?optflags}" LDFLAGS="%{?__global_ldflags}" make %{?_smp_mflags}


%check
CFLAGS="%{?optflags}" LDFLAGS="%{?__global_ldflags}" make check


%install
make install DESTDIR=%{buildroot}
install -m 0644 ChangeLog LICENSE %{buildroot}%{_pkgdocdir}
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la


%ldconfig_scriptlets


%files
%dir %{_pkgdocdir}/
%dir %{_sysconfdir}/glite-lb
%config(noreplace) %{_sysconfdir}/glite-lb/log4crc
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/LICENSE
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/log4crc.example-debugging
%doc %{_pkgdocdir}/log4crc.example-production
%{_libdir}/libglite_lbu_log.so.1
%{_libdir}/libglite_lbu_log.so.1.*

%files devel
%dir %{_includedir}/glite
%dir %{_includedir}/glite/lbu
%{_includedir}/glite/lbu/log.h
%{_libdir}/libglite_lbu_log.so


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.11-1
- New release 1.3.11 (L&B 4.1.2)
- Consistent style with buildroot macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.10-1
- New release 1.3.10 (L&B 4.1.1)

* Fri Nov 22 2013 František Dvořák <valtri@civ.zcu.cz> - 1.3.9-1
- New release 1.3.9 (L&B 4.0.12)
- Cflags and docdir patches not needed anymore
- Enabled parallel build
- The find command replaced by wildcards

* Thu Aug 22 2013 František Dvořák <valtri@civ.zcu.cz> - 1.3.8-2
- Removed arch-specific BuildRequires
- Updated packaging of documentation

* Wed Jul 03 2013 František Dvořák <valtri@civ.zcu.cz> - 1.3.8-1
- Initial package
