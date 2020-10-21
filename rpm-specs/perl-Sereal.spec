# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Sereal_enables_optional_test
%else
%bcond_with perl_Sereal_enables_optional_test
%endif

Name:           perl-Sereal
Version:        4.018
Release:        1%{?dist}
Summary:        Fast, compact, powerful binary (de-)serialization
# Makefile.PL defines LICENSE
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Sereal
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# blib not used
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# Devel::CheckLib not used
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Find not used
# File::Path not used
# File::Spec not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Sereal::Decoder) >= 4.018
BuildRequires:  perl(Sereal::Encoder) >= 4.018
# Tests:
# Benchmark not used
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
# Hash::Util is needed on perl >= 5.25. It's in an eval to proceed to
# num_buckets() definition with older perls.
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Decoder::Constants)
BuildRequires:  perl(Sereal::Encoder::Constants)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
# Time::HiRes not used
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
%if %{with perl_Sereal_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Deep) >= 0.110
BuildRequires:  perl(Test::Deep::NoTest)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Sereal is an efficient, compact-output, binary and feature-rich serialization
protocol. The Perl encoder is implemented as the Sereal::Encoder module, the
Perl decoder correspondingly as Sereal::Decoder. This Sereal module is a very
thin wrapper around both Sereal::Encoder and Sereal::Decoder. It depends on
both and loads both.

%prep
%setup -q -n Sereal-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Aug 04 2020 Petr Pisar <ppisar@redhat.com> - 4.018-1
- 4.018 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Petr Pisar <ppisar@redhat.com> - 4.017-1
- 4.017 bump

* Wed Jul 08 2020 Petr Pisar <ppisar@redhat.com> - 4.015-1
- 4.015 bump

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.014-2
- Perl 5.32 rebuild

* Mon Jun 15 2020 Petr Pisar <ppisar@redhat.com> - 4.014-1
- 4.014 bump

* Thu Jun 11 2020 Petr Pisar <ppisar@redhat.com> - 4.012-1
- 4.012 bump

* Tue Feb 04 2020 Petr Pisar <ppisar@redhat.com> - 4.011-1
- 4.011 bump

* Mon Feb 03 2020 Petr Pisar <ppisar@redhat.com> - 4.009-2
- Build-require Hash::Util needed for tests

* Mon Feb 03 2020 Petr Pisar <ppisar@redhat.com> - 4.009-1
- 4.009 bump

* Thu Jan 30 2020 Petr Pisar <ppisar@redhat.com> - 4.008-1
- 4.008 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.007-2
- Perl 5.30 rebuild

* Wed Apr 10 2019 Petr Pisar <ppisar@redhat.com> - 4.007-1
- 4.007 bump

* Tue Apr 09 2019 Petr Pisar <ppisar@redhat.com> - 4.006-1
- 4.006 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.005-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.005-1
- 4.005 bump

* Tue Nov 14 2017 Petr Pisar <ppisar@redhat.com> - 4.004-1
- 4.004 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.015-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Petr Pisar <ppisar@redhat.com> - 3.015-1
- 3.015 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.014-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Petr Pisar <ppisar@redhat.com> - 3.014-1
- 3.014 bump

* Wed Dec 02 2015 Petr Pisar <ppisar@redhat.com> - 3.009-1
- 3.009 bump

* Mon Nov 30 2015 Petr Pisar <ppisar@redhat.com> - 3.008-1
- 3.008 bump

* Fri Nov 27 2015 Petr Pisar <ppisar@redhat.com> - 3.007-1
- 3.007 bump

* Mon Nov 16 2015 Petr Pisar <ppisar@redhat.com> - 3.006-1
- 3.006 bump

* Tue Sep 29 2015 Petr Pisar <ppisar@redhat.com> 3.005-1
- Specfile autogenerated by cpanspec 1.78.
