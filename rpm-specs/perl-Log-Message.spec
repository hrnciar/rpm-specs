Name:           perl-Log-Message
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.08
Release:        22%{?dist}
Summary:        Generic message storing mechanism
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Log-Message
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(if)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(deprecate)

%description
This package enables you to do generic message logging throughout programs and
projects. Every message will be logged with stack traces, time stamps and so
on.  You can use built-in handlers immediately, or after the fact when you
inspect the error stack. It is highly configurable and let's you even provide
your own handlers for dealing with messages.

%prep
%setup -q -n Log-Message-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.08-22
- Perl 5.32 rebuild

* Thu Mar 19 2020 Petr Pisar <ppisar@redhat.com> - 1:0.08-21
- depracate module is needed on current Perl

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.08-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.08-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.08-15
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.08-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.08-10
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.08-7
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.08-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:0.08-3
- Perl 5.18 rebuild

* Mon May 20 2013 Petr Pisar <ppisar@redhat.com> - 1:0.08-2
- Correct a typo in dependencies

* Mon Apr 29 2013 Petr Pisar <ppisar@redhat.com> - 1:0.08-1
- 0.08 bump

* Thu Apr 25 2013 Petr Pisar <ppisar@redhat.com> - 1:0.06-2
- Open configuration file for reading explicitly (bug #955210)

* Thu Jan 24 2013 Petr Pisar <ppisar@redhat.com> 1:0.06-1
- Specfile autogenerated by cpanspec 1.78.
- Require deprecated module if needed