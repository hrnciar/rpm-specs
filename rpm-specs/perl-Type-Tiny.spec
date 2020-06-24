Name:           perl-Type-Tiny
Version:        1.010002
Release:        2%{?dist}
Summary:        Tiny, yet Moo(se)-compatible type constraint
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Type-Tiny
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-%{version}.tar.gz
BuildArch:      noarch

# --with reply_plugin
#	Default: --without
# Missing deps (perl(Reply::Plugin))
# Marked as unstable (cf. lib/Reply/Plugin/TypeTiny.pm)
%bcond_with reply_plugin

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-interpreter >= 0:5.006001
BuildRequires:  perl-generators
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter::Tiny) >= 0.040
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Tester) >= 0.109
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

# optional
# N/A in Fedora: BuildRequires:  perl(Class::InsideOut)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Devel::LexAlias) >= 0.05
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Exporter) >= 5.59
BuildRequires:  perl(Function::Parameters)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(JSON::PP) >= 2.27105
# N/A in Fedora: BuildRequires:  perl(Kavorka)
# N/A in Fedora: BuildRequires:  perl(match::simple)
BuildRequires:  perl(Method::Generate::Accessor)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
# N/A in Fedora: BuildRequires:  perl(Moops)
BuildRequires:  perl(Moose) >= 2.0400
BuildRequires:  perl(Moose::Meta::TypeCoercion)
BuildRequires:  perl(Moose::Meta::TypeCoercion::Union)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Class)
BuildRequires:  perl(Moose::Meta::TypeConstraint::DuckType)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Enum)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Union)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Getopt) >= 0.63
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Meta::TypeConstraint)
BuildRequires:  perl(Mouse::Util)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(MouseX::Types)
# N/A in Fedora: BuildRequires:  perl(MouseX::Types::Common)
BuildRequires:  perl(MouseX::Types::Moose)
BuildRequires:  perl(mro)
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(re)
BuildRequires:  perl(Ref::Util::XS) > 0.100
%{?with_reply_plugin:BuildRequires:  perl(Reply::Plugin)}
%if !%{defined perl_bootstrap}
# Build-cycle: perl-Return-Type → perl-Type-Tiny
BuildRequires:  perl(Return::Type) >= 0.004
%endif
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Sub::Exporter::Lexical) >= 0.092291
BuildRequires:  perl(Specio)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Sub::Quote)
# N/A in Fedora: BuildRequires:  perl(Switcheroo)
%{?with_reply_plugin:BuildRequires:  perl(Term::ANSIColor)}
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Type::Tie)
# N/A in Fedora: BuildRequires:  perl(Type::Tiny::XS)
%if !%{defined perl_bootstrap}
# Build-cycle: perl-Types-Path-Tiny → perl-Type-Tiny
BuildRequires:  perl(Types::Path::Tiny)
%endif
BuildRequires:  perl(Validation::Class) >= 7.900017
BuildRequires:  perl(Validation::Class::Simple)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(B::Deparse)
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)

%description
Type::Tiny is a tiny class for creating Moose-like type constraint objects
which are compatible with Moo, Moose and Mouse.

%package -n perl-Test-TypeTiny
Summary: Test::TypeTiny module

%description -n perl-Test-TypeTiny
Test::TypeTiny module.

%prep
%setup -q -n Type-Tiny-%{version}
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes CREDITS NEWS README
%license LICENSE COPYRIGHT
%{perl_vendorlib}/*
%{!?with_reply_plugin:%exclude %{perl_vendorlib}/Reply}
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/Test
%exclude %{_mandir}/man3/Test::TypeTiny.3pm*

%files -n perl-Test-TypeTiny
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::TypeTiny.3pm*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.010002-2
- Perl 5.32 rebuild

* Wed May 06 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.010002-1
- Update to 1.010002.

* Thu Mar 26 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.010001-1
- Update to 1.010001.

* Thu Mar 05 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.010000-1
- Update to 1.010000.

* Wed Feb 12 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.008005-1
- Update to 1.008005.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.008003-1
- Update to 1.008003.

* Tue Jan 14 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.008002-1
- Update to 1.008002.
- Add BR: perl(Specio), perl(Specio::Library::Builtins,
  perl(Test::Memory::Cycle).

* Thu Dec 19 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.008000-1
- Update to 1.008000.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.004004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.004004-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.004004-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.004004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.004004-1
- Update to 1.004004.

* Tue Aug 07 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.004002-1
- Update to 1.004002.
- Add BR: perl(IO::String).
- Add and comment out BR: perl(MouseX::Types::Common).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.002002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.002002-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.002002-2
- Perl 5.28 rebuild

* Mon May 21 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.002002-1
- Update to 1.002002.
- Add BR: perl(Ref::Util::XS).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.002001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.002001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.002001-1
- Update to 1.002001.

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.002000-2
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Jun 07 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.002000-1
- Update to 1.002000.

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.000006-7
- Perl 5.26 rebuild

* Mon Mar 20 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000006-6
- Don't BR: perl(Return::Type), perl(Types::Path::Tiny) if perl_bootstrapping
  (From ppisar@redhat.com, RHBZ#1433344)

* Mon Feb 13 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000006-5
- Add further optional part of testsuites: BR: perl(Validation::Class),
  perl(Validation::Class::Simple).

* Fri Feb 10 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000006-4
- Add further optional part of testsuite: BR: perl(Return::Type).

* Thu Feb 09 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000006-3
- Add further optional part of testsuite: BR: perl(Type::Tie).

* Thu Feb 09 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000006-2
- Add more optional parts of testsuite:
  - BR: perl(Sub::Exporter::Lexical).
  - BR: perl(Types::Path::Tiny).

* Thu Feb 02 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000006-1
- Update to 1.000006.
- Add BuildRequires: perl(Function::Parameters)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.000005-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.000005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000005-5
- Modernize spec.
- Add COPYRIGHT to %%license.

* Tue Jul 21 2015 Petr Pisar <ppisar@redhat.com> - 1.000005-4
- Specify all dependencies (bug #1245096)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.000005-2
- Perl 5.22 rebuild

* Mon Oct 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000005-1
- Upstream update.

* Thu Sep 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.000004-2
- Perl 5.20 rebuild

* Thu Sep 04 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000004-1
- Upstream update.

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.000003-2
- Perl 5.20 rebuild

* Sun Aug 31 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000003-1
- Upstream update.

* Fri Aug 22 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000002-1
- Upstream update.
- Update deps.

* Mon Aug 18 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000000-1
- Upstream update.

* Thu Jul 24 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.046-1
- Upstream update.

* Mon Jun 23 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.044-1
- Upstream update.
- Spec file cosmetics.
- BR: perl(Test::Moose), perl(MooseX::Getopt).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.042-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.042-1
- Upstream update.
- Split out perl(Test::TypeTiny) to avoid deps on perl(Test::*).

* Fri Mar 21 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.040-1
- Initial Fedora package.
