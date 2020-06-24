Name:           glite-jobid-api-c
Version:        2.2.13
Release:        13%{?dist}
Summary:        C library handling gLite jobid

License:        ASL 2.0
URL:            http://glite.cern.ch
Source:         http://scientific.zcu.cz/emi/emi.jobid.api-c/%{name}-%{version}.tar.gz

BuildRequires:  libtool
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  pkgconfig

%description
C library handling gLite jobid.


%package        devel
Summary:        Development files for gLite jobid C library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development libraries and header files for gLite jobid
C library.


%prep
%setup -q


%build
./configure --root=/ --prefix=%{_prefix} --libdir=%{_lib}
CFLAGS="%{?optflags}" LDFLAGS="%{?__global_ldflags}" make %{?_smp_mflags}


%check
CFLAGS="%{?optflags}" LDFLAGS="%{?__global_ldflags}" make check


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la


%ldconfig_scriptlets


%files
%license LICENSE
%doc ChangeLog
%{_libdir}/libglite_jobid.so.2
%{_libdir}/libglite_jobid.so.2.*

%files devel
%dir %{_includedir}/glite
%dir %{_includedir}/glite/jobid
%{_includedir}/glite/jobid/strmd5.h
%{_includedir}/glite/jobid/cjobid.h
%{_libdir}/libglite_jobid.so


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 František Dvořák <valtri@civ.zcu.cz> - 2.2.13-9
- Packaging updates (gcc-c++ BR, license tag)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 František Dvořák <valtri@civ.zcu.cz> - 2.2.13-1
- New release 2.2.13 (L&B 4.1.2)
- Consistent style with buildroot macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 František Dvořák <valtri@civ.zcu.cz> - 2.2.12-1
- New release 2.2.12 (L&B 4.1.1)

* Fri Nov 22 2013 František Dvořák <valtri@civ.zcu.cz> - 2.2.11-1
- New release 2.2.11 (L&B 4.0.12)
- Not used arch-specific BuildRequires
- Perl dependencies
- Enabled parallel build
- The find command replaced by wildcards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 02 2013 František Dvořák <valtri@civ.zcu.cz> - 2.2.9-1
- Initial package
