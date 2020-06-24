Name:           perl-Test-MemoryGrowth
Version:        0.04
Release:        2%{?dist}
Summary:        Assert that code does not cause growth in memory usage
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-MemoryGrowth
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-MemoryGrowth-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
# Devel::MAT::Dumper is optional
# XXX: BuildRequires:  perl(Devel::MAT::Dumper)
BuildRequires:  perl(Test::Builder::Module)
# Tests only
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Recommends:     perl(Devel::Gladiator)

%description
This module provides a function to check that a given block of code does
not result in the process consuming extra memory once it has finished.
Despite the name of this module it does not, in the strictest sense of the
word, test for a memory leak: that term is specifically applied to cases
where memory has been allocated but all record of it has been lost, so it
cannot possibly be reclaimed. While the method employed by this module can
detect such bugs, it can also detect cases where memory is still referenced
and reachable, but the usage has grown more than would be expected or
necessary.

%prep
%setup -q -n Test-MemoryGrowth-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-2
- Perl 5.32 rebuild

* Thu Jun 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-1
- 0.04 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-1
- 0.03 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Petr Šabata <contyk@redhat.com> 0.02-1
- Initial packaging
