Name:           perl-Throwable
Version:        0.200013
Release:        15%{?dist}
Summary:        Role for classes that can be thrown
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Throwable
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Throwable-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::StackTrace) >= 1.32
BuildRequires:  perl(Module::Runtime) >= 0.002
BuildRequires:  perl(Moo) >= 1.000001
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Devel::StackTrace) >= 1.32
Requires:       perl(overload)

%{?perl_default_filter}

%description
Throwable is a role for classes that are meant to be thrown as exceptions
to standard program flow. It is very simple and does only two things: saves
any previous value for $@ and calls die $self.

%prep
%setup -q -n Throwable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.200013-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.200013-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.200013-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.200013-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.200013-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.200013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Petr Šabata <contyk@redhat.com> - 0.200013-1
- 0.200013 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.200012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.200012-2
- Perl 5.22 rebuild

* Tue Sep 30 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.200012-1
- 0.200012 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.102080-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102080-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.102080-11
- Remove bogus R: perl(ExtUtils::MakeMaker) (RHBZ #1052853).
- Remove redundant R: perl(Moose).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102080-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.102080-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102080-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102080-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.102080-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102080-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.102080-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102080-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.102080-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Jul 30 2010 Iain Arnell <iarnell@gmail.com> 0.102080-1
- update to latest upstream
- update spec for modern rpmbuild

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.101110-2
- Mass rebuild with perl-5.12.0

* Sat Apr 24 2010 Iain Arnell <iarnell@gmail.com> 0.101110-1
- update to latest upstream version
- use perl_default_filter and DESTDIR

* Sat Feb 27 2010 Iain Arnell <iarnell@gmail.com> 0.100090-2
- BR perl(Pod::Coverage::TrustPod)

* Thu Jan 14 2010 Iain Arnell 0.100090-1
- Specfile autogenerated by cpanspec 1.78.
