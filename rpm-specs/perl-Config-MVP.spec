Name:           perl-Config-MVP
Version:        2.200011
Release:        9%{?dist}
Summary:        Multivalue-property package-oriented configuration
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Config-MVP
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Config-MVP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Class::Load) >= 0.17
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 0.91
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::OneArgNew)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Role::HasMessage)
BuildRequires:  perl(Role::Identifiable::HasIdent)
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Throwable)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# not automatically detected
Requires:       perl(Throwable)
Requires:       perl(Role::Identifiable::HasIdent)
Requires:       perl(Role::HasMessage)
Requires:       perl(StackTrace::Auto)
Requires:       perl(MooseX::OneArgNew)

%{?perl_default_filter}

%description
MVP is a mechanism for loading configuration (or other information) for
libraries. It doesn't read a file or a database. It's a helper for
things that do.

%prep
%setup -q -n Config-MVP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.200011-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.200011-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.200011-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.200011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.200011-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.200011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.200011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.200011-2
- Perl 5.28 rebuild

* Sun Apr 22 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.200011-1
- Update to 2.200011

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.200010-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.200010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.200010-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.200010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.200010-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.200010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.200010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.200010-2
- Perl 5.22 rebuild

* Sun Mar 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.200010-1
- Update to 2.200010

* Sun Mar 08 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.200009-1
- Update to 2.200009

* Mon Nov 10 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.200008-1
- Update to 2.200008
- Use the %%license tag

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.200003-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.200003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 2.200003-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.200003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 2.200003-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.200002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.200002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 2.200002-2
- Perl 5.16 rebuild

* Mon Mar 19 2012 Iain Arnell <iarnell@gmail.com> 2.200002-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.200001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.200001-3
- Perl mass rebuild

* Fri Apr 08 2011 Iain Arnell <iarnell@gmail.com> 2.200001-2
- explicitly declare undetected requires

* Thu Mar 31 2011 Iain Arnell <iarnell@gmail.com> 2.200001-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.101650-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.101650-2
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 16 2010 Iain Arnell <iarnell@gmail.com> 2.101650-1
- update to latest upstream

* Mon Jun 07 2010 Iain Arnell <iarnell@gmail.com> 2.101540-1
- update to latest upstream version
- BR perl(Try::Tiny)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.100780-2
- Mass rebuild with perl-5.12.0

* Sat Mar 20 2010 Iain Arnell <iarnell@gmail.com> 0.100780-1
- update to latest upstream version

* Thu Feb 18 2010 Iain Arnell <iarnell@gmail.com> 0.093350-1
- Specfile autogenerated by cpanspec 1.78.
- Tweak for tests
- perl_default_filter
