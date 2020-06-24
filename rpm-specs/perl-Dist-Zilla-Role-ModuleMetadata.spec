Name:           perl-Dist-Zilla-Role-ModuleMetadata
Version:        0.006
Release:        8%{?dist}
Summary:        Role for plugins that use Module::Metadata
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Role-ModuleMetadata
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Role-ModuleMetadata-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Module::Metadata) >= 1.000005
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
# Tests:
BuildRequires:  perl(Dist::Zilla) >= 5
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::Plugin)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
# Test::Warnings not used
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This role provides some common utilities for Dist::Zilla plugins which use
Module::Metadata and the information that it provides.

%prep
%setup -q -n Dist-Zilla-Role-ModuleMetadata-%{version}

%build
PERL_MM_FALLBACK_SILENCE_WARNING=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-2
- Perl 5.28 rebuild

* Tue Apr 10 2018 Petr Pisar <ppisar@redhat.com> - 0.006-1
- 0.006 bump

* Mon Apr 09 2018 Petr Pisar <ppisar@redhat.com> 0.005-1
- Specfile autogenerated by cpanspec 1.78.
