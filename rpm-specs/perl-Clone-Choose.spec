Name:           perl-Clone-Choose
Version:        0.010
Release:        9%{?dist}
Summary:        Choose appropriate clone utility
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Clone-Choose
Source0:        https://cpan.metacpan.org/modules/by-module/Clone/Clone-Choose-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Optional Run-time
BuildRequires:  perl(Clone) >= 0.10
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Storable)
# Tests
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Test::Without::Module)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Recommends:     perl(Module::Runtime)
Requires:       perl(Storable)

%description
%{summary}.

%prep
%setup -q -n Clone-Choose-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/Clone/
%{_mandir}/man3/Clone::Choose.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Paul Howarth <paul@city-fan.org> - 0.010-7
- Spec tidy-up
  - Use author-independent source URL
  - Drop redundant use of %%{?perl_default_filter}
  - Follow upstream guidance (META.json) on run-time dependencies
  - Use %%{make_build} and %%{make_install}
  - Fix permissions verbosely
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-2
- Perl 5.28 rebuild

* Tue Apr 17 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-1
- 0.010 bump

* Tue Apr 17 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-3
- Specify all dependencies; Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Tom Callaway <spot@fedoraproject.org> - 0.008-1
- initial package
