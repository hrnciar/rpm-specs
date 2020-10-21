Name:           perl-Catalyst-View-Mason
Version:        0.19
Release:        19%{?dist}
Summary:        Mason View Class
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Catalyst-View-Mason
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-View-Mason-%{version}.tar.gz
# Use stderr capturing mechanims that works with Catalyst > 5.90079,
# bug #1190033, CPAN RT#102381
Patch0:         Catalyst-View-Mason-0.19-Use-Capture-Tiny-IO-Capture.patch

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst) >= 5.50
BuildRequires:  perl(Catalyst::Helper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTML::Mason)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::More)
Requires:       perl(Catalyst) >= 5.50
Requires:       perl(Catalyst::View)
Requires:       perl(parent)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Want to use a Mason component in your Catalyst views? No problem!
Catalyst::View::Mason comes to the rescue.

%prep
%setup -q -n Catalyst-View-Mason-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-18
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.19-13
- Clean up spec file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-6
- Perl 5.24 re-rebuild of bootstrapped packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.22 rebuild

* Tue May 19 2015 Petr Pisar <ppisar@redhat.com> - 0.19-2
- Use stderr capturing mechanims that works with Catalyst > 5.90079
  (bug #1190033)

* Thu Jan 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.19-1
- Update to 0.19
- Drop no-longer-used macros and steps
- Tighten file listing

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-14
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Petr Pisar <ppisar@redhat.com> - 0.18-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.18-7
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.18-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-4
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.18-2
- rebuild against perl 5.10.1

* Sun Aug 23 2009 Iain Arnell <iarnell@gmail.com> 0.18-1
- update to latest upstream (for compatibility with Catalyst::Runtime 5.80010)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Iain Arnell 0.17-1
- Specfile autogenerated by cpanspec 1.77.
