Name:       ramond
Version:    0.5
Release:    15%{?dist}
Summary:    Router advertisement monitoring daemon
License:    BSD
URL:        http://%{name}.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2 
Source1:    %{name}.service
# Respect distribution compiler options
Patch0:     %{name}-0.5-Respect-CFLAGS-and-LDFLAGS.patch
# Fix compiler warnings
Patch1:     %{name}-0.5-Fix-compiler-warnings-about-unused-variables-and-imp.patch
# Fix compiler warnings
Patch2:     %{name}-0.5-Fix-warnings-about-incompatible-types.patch
# Fix compiler warnings, undefined behavior on glibc
Patch3:     %{name}-0.5-Do-not-unset-variables-by-setenv.patch
# Fix building with GCC 10
Patch4:     %{name}-0.5-Fix-building-with-GCC-10.patch
BuildRequires:  apr-devel
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros

# Do not find depenendecies in the documentation
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_datadir}/doc

%description
This program monitors IPv6 networks for router advertisements. When an
advertisement is received, a configurable action occurs.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%global _hardened_build 1
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
sed -e '/All Routers Mac List/,/<\/ramond>/ c </ramond>' \
    <ramond.conf.example >ramond.conf

%install
install -d '%{buildroot}%{_sbindir}'
install -m 0755 -t '%{buildroot}%{_sbindir}' %{name}
install -d '%{buildroot}%{_sysconfdir}'
install -m 0644 -t '%{buildroot}%{_sysconfdir}' %{name}.conf
install -d '%{buildroot}%{_unitdir}'
install -m 0644 -t '%{buildroot}%{_unitdir}' '%{SOURCE1}'

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc CHANGELOG README THANKS
%doc demo.pl ramond.conf.*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Petr Pisar <ppisar@redhat.com> - 0.5-14
- Fix building with GCC 10
- Modernize a spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 0.5-10
- Modernize spec file
- Fix compiler warnigs

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 05 2013 Petr Pisar <ppisar@redhat.com> - 0.5-1
- Version 0.5 packaged


