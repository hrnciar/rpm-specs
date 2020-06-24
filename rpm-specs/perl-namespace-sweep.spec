Name:           perl-namespace-sweep
Version:        0.006
Release:        11%{?dist}
Summary:        Sweep up imported subs in your classes
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/namespace-sweep
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FRIEDO/namespace-sweep-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators

BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.09
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Package::Stash) >= 0.33
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Identify) >= 0.04
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Optional testsuite requirements
BuildRequires:	perl(Moo)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Mouse)


Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Because Perl methods are just regular subroutines, it's difficult to tell
what's a method and what's just an imported function. As a result, imported
functions can be called as methods on your objects. This pragma will delete
imported functions from your class's symbol table, thereby ensuring that
your interface is as you specified it. However, code inside your module
will still be able to use the imported functions without any problems.

%prep
%setup -q -n namespace-sweep-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-2
- Perl 5.26 rebuild

* Mon Feb 13 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.006-1
- Initial Fedora package.
