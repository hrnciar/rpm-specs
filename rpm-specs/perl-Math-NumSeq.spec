Name:           perl-Math-NumSeq
Version:        74
Release:        3%{?dist}
Summary:        Number sequences
License:        GPLv3+
URL:            https://metacpan.org/release/Math-NumSeq
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-NumSeq-%{version}.tar.gz
BuildArch:      noarch

%global with_maximum_interoperation 0

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 0:5.004
BuildRequires:  perl(constant::defer) >= 1
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
# Devel::FindRef not available because it does not work since Perl 5.22.
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Factor::XS) >= 0.40
BuildRequires:  perl(Math::Libm)
BuildRequires:  perl(Math::Prime::XS) >= 0.23
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SDBM_File)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::ConsistentVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(Test::YAML::Meta)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(YAML::XS)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Temp)
Requires:       perl(Math::Trig)
Requires:       perl(Module::Load)
Requires:       perl(SDBM_File)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%if 0%{with_maximum_interoperation}
BuildRequires:  perl(Language::Expr)
BuildRequires:  perl(Language::Expr::Compiler::Perl)
BuildRequires:  perl(Math::Expression::Evaluator)
BuildRequires:  perl(Math::Symbolic)
Requires:       perl(Math::Expression::Evaluator)
Requires:       perl(Math::Symbolic)
Requires:       perl(Language::Expr)
Requires:       perl(Language::Expr::Compiler::Perl)
%endif

%description
This is a base class for some number sequences. Sequence objects can
iterate through values and some sequences have random access and/or
predicate test.

%prep
%setup -q -n Math-NumSeq-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -size 0 -delete

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes COPYING
%{perl_vendorlib}/Math/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 74-3
- Perl 5.32 rebuild

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 74-2
- Add perl(Safe) for tests

* Sun Feb 23 2020 Miro Hrončok <mhroncok@redhat.com> - 74-1
- Update to 74 (#1806236)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Miro Hrončok <mhroncok@redhat.com> - 73-1
- Update to 73 (#1737396)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 72-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 72-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 72-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 72-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 72-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 72-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 72-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Miro Hrončok <mhroncok@redhat.com> - 72-1
- New version 72 (#1359443)

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 71-8
- Disable build-time dependency on Devel::FindRef unconditionally

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 71-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 71-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 71-4
- Perl 5.22 rebuild

* Tue Jun 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 71-3
- Disable optional BR Devel::FindRef for Perl 5.22

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 71-2
- Perl 5.20 rebuild

* Sun Jun 29 2014 Miro Hrončok <mhroncok@redhat.com> - 71-1
- New version 71 (#1114326)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Miro Hrončok <mhroncok@redhat.com> - 70-1
- New version 70 (#1087328)

* Mon Feb 24 2014 Miro Hrončok <mhroncok@redhat.com> - 69-1
- New version 69 (#1066371)

* Thu Jan 30 2014 Miro Hrončok <mhroncok@redhat.com> - 68-1
- New version 68 (#1059636)

* Tue Nov 26 2013 Miro Hrončok <mhroncok@redhat.com> - 67-1
- New version 67 (#1030911)

* Wed Oct 23 2013 Miro Hrončok <mhroncok@redhat.com> - 66-1
- New version 66 (#1022678)

* Sat Oct 12 2013 Miro Hrončok <mhroncok@redhat.com> - 65-1
- New version 65 (#1016246)

* Tue Sep 17 2013 Miro Hrončok <mhroncok@redhat.com> - 64-1
- New version 64 (#1008403)

* Mon Sep 02 2013 Miro Hrončok <mhroncok@redhat.com> - 63-1
- New version 63
- %%{__perl} to perl

* Fri Aug 16 2013 Miro Hrončok <mhroncok@redhat.com> - 62-1
- New version 62
- Language::Expr dependency conditional 

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 30 2012 Miro Hrončok <miro@hroncok.cz> - 55-1
- New release
- Removed shared libs filter, noarch
- Removed deleting empty directories
- PERL_INSTALL_ROOT changed to DESTDIR
- Added some of previously removed BRs
- Sort (B)Rs lexicographically 

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 52-2
- Removed BRs provided by perl package

* Tue Oct 09 2012 Miro Hrončok <miro@hroncok.cz> 52-1
- New release

* Sun Sep 23 2012 Miro Hrončok <miro@hroncok.cz> 51-1
- Specfile autogenerated by cpanspec 1.78 and revised.
