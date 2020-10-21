Name:           perl-Tie-Cycle
Version:        1.225
Release:        11%{?dist}
Summary:        Cycle through a list of values via a scalar
License:        Artistic 2.0
URL:            https://metacpan.org/release/Tie-Cycle
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Tie-Cycle-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.95
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This Perl module can be used to go through a list over and over again.
Once you get to the end of the list, you go back to the beginning.  You
do not have to worry about any of this since the magic of tie does that
for you.

%prep
%setup -q -n Tie-Cycle-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README.pod CONTRIBUTING.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.225-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.225-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.225-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.225-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.225-7
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.225-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.225-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.225-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.225-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.225-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 1.225-1
- Update to 1.225 (#1468928)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.224-2
- Perl 5.26 rebuild

* Wed Apr 19 2017 Colin B. Macdonald <cbm@m.fsf.org> - 1.224-1
- Version bump (#1443269) and correct license.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Colin B. Macdonald <cbm@m.fsf.org> - 1.222-1
- Version bump (#1415353)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.221-2
- Perl 5.24 rebuild

* Wed Feb 03 2016 Colin B. Macdonald <cbm@m.fsf.org> - 1.221-1
- Version bump, spec file clean up

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Colin B. Macdonald <cbm@m.fsf.org> 1.21-1
- Version bump, spec file clean up

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.20-3
- Perl 5.22 rebuild

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.20-2
- clean-up following review.

* Fri Oct 03 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.20-1
- Specfile autogenerated by cpanspec 1.78
- Manually added Test::Simple dep,
  filed [upstream](https://github.com/briandfoy/tie-cycle/issues/2).

* Thu Jun 26 2014 Colin B. Macdonald <cbm@m.fsf.org> 1.19-1
- Specfile autogenerated by cpanspec 1.78.

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> 1.17-1
- Specfile autogenerated by cpanspec 1.78.
