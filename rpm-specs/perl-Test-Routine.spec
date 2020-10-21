Name:           perl-Test-Routine
Summary:        Composable units of assertion
Version:        0.027
Release:        7%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Routine
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Routine-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Method::Signatures)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Test::Abortable)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.96

Requires:       perl(Moose::Meta::Method)
Requires:       perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Test::Routine is a very simple framework for writing your tests as
composable units of assertion. In other words: roles.


%prep
%setup -q -n Test-Routine-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::Routine*3pm*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.027-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.027-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.027-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.027-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.027-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.027-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 02 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.027-1
- Update to 0.027

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.025-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.025-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.025-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.025-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.025-2
- Perl 5.26 rebuild

* Sun Apr 23 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.025-1
- Update to 0.025

* Sun Feb 12 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.024-1
- Update to 0.024

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.023-1
- Update to 0.023

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 16 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.020-5
- Add perl(Math::Trig) as a BR
- Use DESTDIR instead of PERL_INSTALL_ROOT
- Pass NO_PACKLIST=1 to ExtUtils::MakeMaker

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-3
- Perl 5.22 rebuild

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-2
- Perl 5.20 rebuild

* Sat Sep 06 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.020-1
- Update to 0.020

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.019-2
- Perl 5.20 rebuild

* Sun Aug 31 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.019-1
- Update to 0.019
- Drop upstreamed patch
- Use %%license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.015-5
- Perl 5.18 rebuild
- Adjust to Test-Simple-0.98_05 (CPAN RT#87615, #87616)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.015-2
- Add missing build requirements.

* Wed Jan 02 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.015-1
- Initial package for Fedora, with help from cpanspec.
