# Run optional tests
%{bcond_without perl_TryCatch_enables_optional_test}

Name:           perl-TryCatch
Version:        1.003002
Release:        23%{?dist}
Summary:        First class try catch semantics for Perl, without source filters
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/TryCatch
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASH/TryCatch-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# perl-podlators (pod2text) not used
BuildRequires:  perl(ExtUtils::Depends) >= 0.302
# File::Copy::Recursive not used
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install) >= 0.79
BuildRequires:  perl(Module::Install::Can)
BuildRequires:  perl(Module::Install::Metadata)
# Path::Class not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  perl(B::Hooks::OP::PPAddr) >= 0.03
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Declare) >= 0.005007
BuildRequires:  perl(Devel::Declare::Context::Simple)
BuildRequires:  perl(Devel::PartialDump)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::clean) >= 0.20
BuildRequires:  perl(Parse::Method::Signatures) >= 1.003012
BuildRequires:  perl(Scope::Upper) >= 0.06
BuildRequires:  perl(Sub::Exporter) >= 0.979
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_TryCatch_enables_optional_test}
# Optional tests:
BuildRequires:  perl(MooseX::Types::Structured)
# XML::SAX::Base useless without XML::SAX::Expat
# XML::SAX::Expat not yet packaged
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(B::Hooks::EndOfScope) >= 0.12
Requires:       perl(B::Hooks::OP::PPAddr) >= 0.03
Requires:       perl(Devel::Declare) >= 0.005007
Requires:       perl(namespace::clean) >= 0.20
Requires:       perl(Parse::Method::Signatures) >= 1.003012
Requires:       perl(Scope::Upper) >= 0.06
Requires:       perl(Sub::Exporter) >= 0.979

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((B::Hooks::EndOfScope|B::Hooks::OP::PPAddr|Devel::Declare|namespace::clean|Parse::Method::Signatures|Scope::Upper|Sub::Exporter)\\)$

%description
This module aims to provide a nicer syntax and method to catch errors in
Perl, similar to what is found in other languages (such as Java, Python or
C++). The standard method of using eval {}; if ($@) {} is often prone to
subtle bugs, primarily that its far too easy to stomp on the error in error
handlers. And also eval/if isn't the nicest idiom.

%prep
%setup -q -n TryCatch-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README eg
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/TryCatch*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.003002-23
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.003002-20
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.003002-17
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.003002-13
- Perl 5.26 rebuild

* Wed May 24 2017 Petr Pisar <ppisar@redhat.com> - 1.003002-12
- Fix building on Perl without "." in @INC (CPAN RT#121846)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 30 2016 Petr Pisar <ppisar@redhat.com> - 1.003002-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.003002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003002-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.003002-7
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.003002-6
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.003002-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Petr Šabata <contyk@redhat.com> - 1.003002-1
- 1.003002 bump
- XML tests fixes

* Wed Mar 20 2013 Petr Šabata <contyk@redhat.com> - 1.003001-1
- 1.003001 bump
- The bench* scripts are now documentation (eg)

* Fri Feb 22 2013 Petr Šabata <contyk@redhat.com> - 1.003000-7
- Patch the failing invalid.t (rt#81978) and fix the BRs list

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 1.003000-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.003000-2
- Perl mass rebuild

* Mon Mar 21 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.003000-1
- Specfile autogenerated by cpanspec 1.79.
