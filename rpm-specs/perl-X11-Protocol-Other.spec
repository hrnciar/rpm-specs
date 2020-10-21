Name:           perl-X11-Protocol-Other
Version:        31
Release:        5%{?dist}
Summary:        Miscellaneous X11::Protocol helpers
License:        GPLv3+
URL:            https://metacpan.org/release/X11-Protocol-Other
Source0:        https://cpan.metacpan.org/modules/by-module/X11/X11-Protocol-Other-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode) >= 1
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Encode::HanExtra) >= 0.06
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(X11::Protocol)
# Tests
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
These are some helper functions for X11::Protocol.

%prep
%setup -q -n X11-Protocol-Other-%{version}
chmod a-x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%doc Changes examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 31-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Robin Lee <cheeselee@fedoraproject.org> - 31-1
- Update to 31 (RHBZ#1727552)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 30-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 30-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 30-2
- Perl 5.26 rebuild

* Thu Apr 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 30-1
- 30 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 29-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 29-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 29-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb  2 2014 Robin Lee <cheeselee@fedoraproject.org> - 29-1
- Update to 29

* Wed Nov 13 2013 Robin Lee <cheeselee@fedoraproject.org> - 28-1
- Update to version 28

* Tue Oct  1 2013 Robin Lee <cheeselee@fedoraproject.org> - 25-1
- Update to 25

* Thu Sep 26 2013 Robin Lee <cheeselee@fedoraproject.org> - 24-1
- Update to version 24

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 23-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Petr Šabata <contyk@redhat.com> - 23-1
- 23 bump (testsuite update)

* Mon Nov 26 2012 Petr Šabata <contyk@redhat.com> - 22-1
- 22 bump (testsuite update)

* Mon Nov 05 2012 Petr Šabata <contyk@redhat.com> - 21-1
- 21 bump
- Fix the deps
- Modernize the spec a bit
- Package the examples

* Sat Aug 11 2012 Robin Lee <cheeselee@fedoraproject.org> 18-1
- Specfile autogenerated by cpanspec 1.78.
