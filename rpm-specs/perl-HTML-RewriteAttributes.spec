Name:           perl-HTML-RewriteAttributes
Version:        0.05
Release:        22%{?dist}
Summary:        Concise attribute rewriting
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-RewriteAttributes
Source0:        https://cpan.metacpan.org/authors/id/T/TS/TSIBLEY/HTML-RewriteAttributes-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(URI)
BuildRequires:  perl(Test::More)

BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
HTML::RewriteAttributes is designed for simple yet powerful HTML attribute
rewriting.

%prep
%setup -q -n HTML-RewriteAttributes-%{version}
rm -r inc/
sed -i -e '/^inc\/.*$/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-22
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-19
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-16
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-13
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-11
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-9
- Modernize spec.
- Remove inc/.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-7
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.05-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.05-1
- Upstream update.
- Spec file cleanup.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.04-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 06 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.04-1
- Upstream update.

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Ralf Corsépius <corsepiu@fedoraproject.org> 0.03-1
- Specfile autogenerated by cpanspec 1.77.
