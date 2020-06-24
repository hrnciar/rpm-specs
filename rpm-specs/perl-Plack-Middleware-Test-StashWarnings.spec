Name:           perl-Plack-Middleware-Test-StashWarnings
Version:        0.08
Release:        19%{?dist}
Summary:        Test your application's warnings
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Plack-Middleware-Test-StashWarnings
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Plack-Middleware-Test-StashWarnings-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Synopsis)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::AuthorTests)

%description
Plack::Middleware::Test::StashWarnings is a Plack middleware component to
record warnings generated by your application so that you can test them to
make sure your application complains about the right things.

%prep
%setup -q -n Plack-Middleware-Test-StashWarnings-%{version}
rm -r inc/

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-17
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-14
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-11
- Perl 5.26 rebuild

* Wed May 24 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.08-10
- Eliminate inc.
- BR: perl(Module::Install::ReadmeFromPod),
  perl(Module::Install::AuthorTests),
  perl(inc::Module::Install) (RHBZ#1455072).
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.08-6
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.08-1
- Upstream update.

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.07-4
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 16 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.07-1
- Upstream update.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 0.06-2
- Perl 5.16 rebuild

* Mon May 07 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.06-1
- Upstream update.
- Reflect upstream URL having changed.
- Spec file modernization.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.05-2
- Perl mass rebuild

* Tue Jun 21 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.05-1
- Upstream update.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.04-1
- Initial Fedora package.
