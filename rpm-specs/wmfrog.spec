Name:       wmfrog
Version:    0.3.1
Release:    27%{?dist}
Summary:    A weather application, it shows the weather in a graphical way
License:    GPLv2+
URL:        http://wiki.colar.net/wmfrog_dockapp
Source0:    http://bitbucket.org/tcolar/%{name}/downloads/%{name}-%{version}.tgz
# Bug 822219, submitted to upstream.
Patch0:     %{name}-0.3.1-Skip-warning.patch
# Fix a crash with overlong wmfrog -tmp argument, bug #1422319,
# mailed to upstream.
Patch1:     %{name}-0.3.1-Fix-parsing-wmfrog-arguments.patch
# Fix building with GCC 10, mailed to an upstream
Patch2:     %{name}-0.3.1-Define-global-variables-only-once.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  perl-generators
BuildRequires:  sed
Requires:       wget

%description
This is a weather application, it shows the weather in a graphical way. The
artwork looks like a kiddo did it, but that's part of the charm… Ok, I did it
when I was 25, I'm a programmer not a designer :)

%prep
%setup -q -c
%patch0 -p1 -b .warning
%patch1 -p1
%patch2 -p1
sed -i -e 's|/lib/wmfrog|/libexec/wmfrog|' Src/Makefile
sed -i -e 's|/usr/lib/|%{_libexecdir}/|' Src/wmFrog.c
# Remove prebuilt binaries
make -C Src clean

%build
cd Src
make CFLAGS="${RPM_OPT_FLAGS}" %{?_smp_mflags}

%install
cd Src
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license COPYING
%doc CHANGES HINTS 
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Petr Pisar <ppisar@redhat.com> - 0.3.1-25
- Fix building with GCC 10

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Petr Pisar <ppisar@redhat.com> - 0.3.1-18
- Fix a crash with overlong wmfrog -tmp argument (bug #1422319)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-16
- Perl 5.24 rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-13
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.1-12
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.3.1-8
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 0.3.1-5
- Perl 5.16 rebuild

* Thu May 17 2012 Petr Pisar <ppisar@redhat.com> - 0.3.1-4
- Adjust to NOAA web page change (bug #822219)
- Depend on perl ABI
- Clean spec file

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Petr Pisar <ppisar@redhat.com> - 0.3.1-1
- 0.3.1 bump
- Fixed clouds/wind parsing issues

* Wed Sep 01 2010 Petr Pisar <ppisar@redhat.com> - 0.2.2-1
- 0.2.2 bump

* Mon Aug 09 2010 Petr Pisar <ppisar@redhat.com> - 0.2.1-2
- Change RPM group to Amusements/Graphics

* Thu Aug 05 2010 Petr Pisar <ppisar@redhat.com> - 0.2.1-1
- 0.2.1 bump
- Fix METAR parser

* Tue Aug 03 2010 Petr Pisar <ppisar@redhat.com> - 0.2.0-1
- 0.2.0 import
