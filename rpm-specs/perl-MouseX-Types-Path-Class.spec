Name:		perl-MouseX-Types-Path-Class
Summary:	A Path::Class type library for Mouse
Version:	0.07
Release:	19%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/MouseX-Types-Path-Class
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MASAKI/MouseX-Types-Path-Class-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl(Module::Install::AuthorTests)
BuildRequires:	perl(Module::Install::ReadmeFromPod)
BuildRequires:	perl(Module::Install::ReadmeMarkdownFromPod)
BuildRequires:	perl(Module::Install::Repository)
# Module Runtime
BuildRequires:	perl(Mouse) >= 0.39
BuildRequires:	perl(MouseX::Types) >= 0.02
BuildRequires:	perl(MouseX::Types::Mouse)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Optional Functionality
BuildRequires:	perl(MouseX::Getopt) >= 0.22
# Test Suite
BuildRequires:	perl(Test::More) >= 0.94
BuildRequires:	perl(Test::UseAllModules)
# Author Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Test::Spelling), aspell-en
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Mouse) >= 0.39
Requires:	perl(MouseX::Getopt) >= 0.22
Requires:	perl(MouseX::Types) >= 0.02

# Filter under-specified dependencies
%global __requires_exclude ^perl\\(MouseX::Types\\)$

%description
MouseX::Types::Path::Class creates common Mouse types, coercions and option
specifications useful for dealing with Path::Class objects as Mouse attributes.

Coercions (see Mouse::Util::TypeConstraints) are made from both Str and
ArrayRef to both Path::Class::Dir and Path::Class::File objects. If you have
MouseX::Getopt installed, the Getopt option type ("=s") will be added for both
Path::Class::Dir and Path::Class::File.

%prep
%setup -q -n MouseX-Types-Path-Class-%{version}

# Unbundle inc::Module::Install; we'll use the system version instead
rm -rf inc/
perl -ni -e 'print unless /^inc\//;' MANIFEST

# Avoid the need for Module::Install::AuthorRequires and
# all of upstream's toolchain modules as a result of the unbundling
perl -ni -e 'print unless /author_requires/;' Makefile.PL

# F19's dictionary doesn't have coercions
echo coercions >> xt/03_podspell.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test TEST_POD=1

%files
%doc Changes README
%{perl_vendorlib}/MouseX/
%{_mandir}/man3/MouseX::Types::Path::Class.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-19
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-13
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-10
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-5
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Paul Howarth <paul@city-fan.org> - 0.07-2
- Incorporate feedback from package review (#1088931)
  - Bump MouseX::Getopt version requirement to 0.22
  - Add versioned runtime dependencies on Mouse and MouseX::Types
  - Actually unbundle inc::Module::Install instead of just claiming to
- Include author test build requirements

* Thu Apr 17 2014 Paul Howarth <paul@city-fan.org> - 0.07-1
- Initial RPM version
