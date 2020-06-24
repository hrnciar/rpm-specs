Name:           perl-Code-TidyAll-Plugin-Test-Vars
Version:        0.04
Release:        12%{?dist}
Summary:        Provides Test::Vars plugin for Code::TidyAll
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Code-TidyAll-Plugin-Test-Vars
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Code-TidyAll-Plugin-Test-Vars-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 0:5.006
BuildRequires:  perl-generators

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(autodie)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Code::TidyAll) >= 0.50
BuildRequires:  perl(Code::TidyAll::Plugin)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Vars) >= 0.008
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# perl-generators misses Code::TidyAll::Plugin "extends":
# c.f. lib/Code/TidyAll/Plugin/Test/Vars.pm
Requires:       perl(Code::TidyAll::Plugin)

%description
This module uses Test::Vars to detect unused variables in Perl modules.

%prep
%setup -q -n Code-TidyAll-Plugin-Test-Vars-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-12
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-3
- Perl 5.26 rebuild

* Mon Feb 13 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.04-2
- Reflect feedback from package review.

* Fri Feb 10 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.04-1
- Initial Fedora package.
