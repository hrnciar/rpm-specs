Name:           perl-Syntax-Keyword-Try
Version:        0.18
Release:        1%{?dist}
Summary:        try/catch/finally syntax for perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Syntax-Keyword-Try/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Try-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Carp)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.88
# Optional
# not used - perl(Future)
# not packaged yet - perl(Future::AsyncAwait)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(threads)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module provides a syntax plugin that implements exception-handling
semantics in a form familiar to users of other languages, being built on a
block labeled with the try keyword, followed by at least one of a catch or
finally block.

%prep
%setup -q -n Syntax-Keyword-Try-%{version}

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Syntax*
%{_mandir}/man3/*

%changelog
* Mon Aug 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- 0.18 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Petr Pisar <ppisar@redhat.com> - 0.16-1
- 0.16 bump

* Tue Jul 21 2020 Petr Pisar <ppisar@redhat.com> - 0.15-1
- 0.15 bump

* Wed Jul 08 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-1
- 0.14 bump

* Tue Jun 30 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-1
- 0.13 bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-1
- 0.11 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-1
- 0.10 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-1
- Specfile autogenerated by cpanspec 1.78.
