Name:           perl-POSIX-strftime-Compiler
Version:        0.42
Release:        12%{?dist}
Summary:        GNU C library compatible strftime for loggers and servers
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/POSIX-strftime-Compiler
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/POSIX-strftime-Compiler-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter >= 0:5.008004
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
POSIX::strftime::Compiler provides GNU C library compatible strftime(3).
But this module will not affected by the system locale. This feature is
useful when you want to write loggers, servers and portable applications.

%prep
%setup -q -n POSIX-strftime-Compiler-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.42-1
- Update to 0.42.

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.41-4
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-2
- Perl 5.22 rebuild

* Thu Jan 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.41-1
- Upstream update.
- Remove BR: perl(CPAN::Meta), BR: perl(CPAN::Meta::Prereqs).

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-2
- Perl 5.20 rebuild

* Thu Aug 21 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.40-1
- Fix Australia/Darwin test (RHBZ#1132033).

* Mon Jun 23 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.32-1
- Upstream update.
- Spec cosmetics.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.31-1
- Specfile autogenerated by cpanspec 1.78.
