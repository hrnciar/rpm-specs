Name:           perl-Algorithm-BloomFilter
Version:        0.02
Release:        4%{?dist}
Summary:        A simple bloom filter data structure
# lib/Algorithm/BloomFilter.pm
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Algorithm-BloomFilter
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Algorithm-BloomFilter-%{version}.tar.gz

# build requirements
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%description
This module implements a simple bloom filter in C/XS.

%prep
%setup -q -n Algorithm-BloomFilter-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Algorithm*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 18 2019 Emmanuel Seyman <emmanuel@seyman.fr> 0.02-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
