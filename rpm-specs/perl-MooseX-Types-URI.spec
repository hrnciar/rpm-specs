Name:       perl-MooseX-Types-URI
Version:    0.08
Release:    15%{?dist}
# see lib/MooseX/Types/URI.pm
License:    GPL+ or Artistic

Summary:    URI related types and coercions for Moose
Source:     https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-URI-%{version}.tar.gz
Url:        https://metacpan.org/release/MooseX-Types-URI
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:  noarch

BuildRequires: perl-generators
BuildRequires: perl(Module::Build::Tiny)
BuildRequires: perl(Moose) >= 0.50
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(namespace::clean) >= 0.08
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(URI)
BuildRequires: perl(URI::FromHash)

%{?perl_default_filter}

%description
This package provides Moose types for fun (and profit) with the URI classes.

It has slightly DWIMier types than the the URI classes have due to
implementation details, so the types should be more forgiving when
ducktyping will work anyway (e.g. URI::WithBase does not inherit URI).


%prep
%setup -q -n MooseX-Types-URI-%{version}
sed -i '1s,#!perl,#!%{__perl},' t/*.t

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc README Changes t/
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.08-1
- Update to 0.08
- Switch to the Module::Build::Tiny workflow

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-2
- Perl 5.22 rebuild

* Fri Nov 14 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.07-1
- Update to 0.07
- Tighten file listing
- Add %%license tag
- Work around rpmlint error

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.03-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.03-2
- Perl 5.16 rebuild

* Thu Jan 12 2012 Iain Arnell <iarnell@gmail.com> 0.03-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- use perl_default_filter
- use DESTDIR, not PERL_INSTALL_ROOT

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.02-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-5
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.02-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.02-1
- auto-update to 0.02 (by cpan-spec-update 0.01)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 07 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.01-1
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.1)
