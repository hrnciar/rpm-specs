Name:           glite-jobid-api-cpp
Version:        1.3.10
Release:        12%{?dist}
Summary:        Dummy base package for gLite jobid C++ API

License:        ASL 2.0
URL:            http://glite.cern.ch
Source:         http://scientific.zcu.cz/emi/emi.jobid.api-cpp/%{name}-%{version}.tar.gz

BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
This is a dummy package to build gLite jobid C++ API.


%package        devel
Summary:        C++ API handling gLite jobid
Requires:       glite-jobid-api-c-devel
Provides:       %{name} = %{version}-%{release}


%description    devel
C++ API handling gLite jobid. It is a thin wrapper of the C implementation
(glite-jobid-api-c).


%prep
%setup -q


%build
./configure --root=/ --prefix=%{_prefix}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files devel
%license LICENSE
%doc ChangeLog
%{_includedir}/glite/jobid/JobId.h


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 František Dvořák <valtri@civ.zcu.cz> - 1.3.10-8
- Packaging updates (license tag)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.10-7
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 26 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.10-1
- New release 1.3.10 (L&B 4.1.2)
- Consistent style with buildroot macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.9-1
- New release 1.3.9 (L&B 4.1.1)

* Fri Nov 22 2013 František Dvořák <valtri@civ.zcu.cz> - 1.3.8-1
- New release 1.3.8 (L&B 4.0.12)
- Perl dependencies
- Enabled parallel build
- Removed %%check target

-* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 František Dvořák <valtri@civ.zcu.cz> - 1.3.6-2
- Noarch package

* Thu May 02 2013 František Dvořák <valtri@civ.zcu.cz> - 1.3.6-1
- Initial package
