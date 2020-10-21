Name:           perl-Trace-Mask
Version:        0.000008
Release:        13%{?dist}
Summary:        Masking frames in stack traces
# License URLs in PODs are wrong
# <https://github.com/exodist/Trace-Mask/issues/2>.
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Trace-Mask
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Trace-Mask-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.03
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util) >= 1.10
BuildRequires:  perl(Scalar::Util) >= 1.10
# Test2 is the only versioned module in the perl-Test2
BuildRequires:  perl(Test2) >= 1.302026
BuildRequires:  perl(Test2::API)
# Test2::Suite is the only versioned module in the perl-Test-Suite
BuildRequires:  perl(Test2::Suite) >= 0.000030
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Subtest)
BuildRequires:  perl(Try::Tiny) >= 0.03
# Tests:
BuildRequires:  perl(Test2::Bundle::Extended)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Tools::Spec)
# Test2::Workflow is the only versioned module in the perl-Test2-Workflow
BuildRequires:  perl(Test2::Workflow) >= 0.000009
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Scalar::Util) >= 1.10

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|List::Util|Scalar::Util)\\)$

%description
This is a specification packages can follow to define behaviors stack
tracers may choose to honor. If a module implements this specification than
any compliant stack tracer will render the stack trace as desired. This
package also provides some implementations (e.g. a Carp stack tracer).

%package Test
Summary:        Tools for testing Trace::Mask compliance
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp) >= 1.03
Requires:       perl(List::Util) >= 1.10
Requires:       perl(Scalar::Util) >= 1.10
# Test2 is the only versioned module in the perl-Test2
Requires:       perl(Test2) >= 1.302026
Requires:       perl(Test2::API)
# Test2::Suite is the only versioned module in the perl-Test-Suite
Requires:       perl(Test2::Suite) >= 0.000030
Requires:       perl(Test2::Tools::Compare)
Requires:       perl(Test2::Tools::Subtest)

%description Test
This package provides tools for testing tracers. This allows you to check
that a tracer complies with the Trace::Mask specifications.

%prep
%setup -q -n Trace-Mask-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
# README.md duplicates README's content
%doc Changes README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Trace/Mask/Test.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Trace::Mask::Test.*

%files Test
%{perl_vendorlib}/Trace/Mask/Test.pm
%{_mandir}/man3/Trace::Mask::Test.*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.000008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.000008-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.000008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.000008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.000008-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.000008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.000008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.000008-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.000008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.000008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000008-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.000008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 17 2016 Petr Pisar <ppisar@redhat.com> - 0.000008-1
- 0.000008 bump

* Thu Jun 16 2016 Petr Pisar <ppisar@redhat.com> - 0.000007-3
- Adapt tests to Test2-Workflow-0.000009

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.000007-2
- Perl 5.24 rebuild

* Mon Feb 15 2016 Petr Pisar <ppisar@redhat.com> - 0.000007-1
- 0.000007 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.000006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Petr Pisar <ppisar@redhat.com> 0.000006-1
- Specfile autogenerated by cpanspec 1.78.
