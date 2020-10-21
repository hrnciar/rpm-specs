Name:           perl-XML-TreePP
Version:        0.43
Release:        17%{?dist}
Summary:        Pure Perl implementation for parsing/writing XML documents
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/XML-TreePP
Source0:        https://cpan.metacpan.org/modules/by-module/XML/XML-TreePP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# Optional Functionality
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Lite)
BuildRequires:  perl(Jcode)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Tie::IxHash)
# Test Suite
BuildRequires:  perl(Test::More)
# Optional Tests (note: t/*_http-*.t tests require network access so we don't try to run them)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(utf8)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Recommends:     perl(Encode)
Recommends:     perl(HTTP::Lite)
Recommends:     perl(Jcode)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Tie::IxHash)

%description
Pure Perl implementation for parsing/writing XML documents

%prep
%setup -q -n XML-TreePP-%{version}

# Remove bogus exec permissions
chmod -c a-x Changes lib/XML/TreePP.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc README Changes
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/TreePP.pm
%{_mandir}/man3/XML::TreePP.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Paul Howarth <paul@city-fan.org> - 0.43-14
- Spec tidy-up
  - Use author-independent source URL
  - Classify buildreqs by usage
  - Add Recommends: for optional dependencies
  - Fix exec permissions in %%prep section
  - Drop redundant buildroot cleaning in %%install section
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Simplify find command using -delete
  - Don't need to remove empty directories from the buildroot
  - Fix permissions verbosely

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-12
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-9
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Marianne Lombard <marianne@tuxette.fr> - 0.43-1
- New version 

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-15
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-14
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.39-11
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 0.39-8
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.39-6
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.39-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Jun 27 2010 Jeroen van Meeuwen <jeroen.van.meeuwen@ergo-project.org> - 0.39-3
- Fix Source0 URL (#607878)
- Add extra build requirements for tests
- Fix executable permissions on some files (#607878)

* Sat Jun 19 2010 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.39-1
- First package
