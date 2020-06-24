Name:           perl-HTTP-Exception
Version:        0.04007
Release:        5%{?dist}
Summary:        Throw HTTP-Errors as (Exception::Class-) Exceptions
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTTP-Exception
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMUELLER/HTTP-Exception-%{version}.tar.gz
BuildArch:      noarch

# build requirements
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# run requirements
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exception::Class::Base)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Middleware::HTTPExceptions)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(lib)
# extended test requirements
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Every HTTP::Exception is a Exception::Class - Class. So the same
mechanisms apply as with Exception::Class-classes. In fact have a look
at Exception::Class' docs for more general information on exceptions and
Exception::Class::Base for information on what methods a caught
exception also has.

%prep
%setup -q -n HTTP-Exception-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 make test

%files
%doc Changes README
%{perl_vendorlib}/HTTP*
%{_mandir}/man3/HTTP*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.04007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.04007-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.04007-1
- Update to 0.04007

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04006-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.04006-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04006-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.04006-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.04006-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.04006-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.04006-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.04006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.04006-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.04006-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 16 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.04006-1
- Update to 0.04006

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.04004-4
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.04004-1
- Update to 0.04004

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 0.04001-2
- Perl 5.16 rebuild

* Sat Feb 25 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.04001-1
- Update to 0.04001

* Tue Feb 21 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.04000-1
- Update to 0.04 (using the version 0.04000 for rpm's sake)
- Move from the Build.PL method to the Makefile.PL one

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.03001-2
- Perl mass rebuild

* Mon Jun 20 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.03001-1
- Specfile autogenerated by cpanspec 1.78.
