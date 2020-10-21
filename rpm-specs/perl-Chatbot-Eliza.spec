Name:           perl-Chatbot-Eliza
Version:        1.08
Release:        11%{?dist}
Summary:        Implementation of the Eliza algorithm
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Chatbot-Eliza
Source0:        https://cpan.metacpan.org/authors/id/G/GR/GRANTG/Chatbot-Eliza-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
This module implements the classic Eliza algorithm. The original Eliza
program was written by Joseph Weizenbaum and described in the
Communications of the ACM in 1966. Eliza is a mock Rogerian
psychotherapist. It prompts for user input, and uses a simple
transformation algorithm to change user input into a follow-up question.
The program is designed to give the appearance of understanding.

%prep
%setup -q -n Chatbot-Eliza-%{version}
cd examples
find . -type f -exec chmod a-x {} +
for i in *; do
    iconv -f latin1 -t utf8 $i > $i.utf8 && \
    touch -r $i $i.utf8 && \
    mv $i.utf8 $i
done
cd ..

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-10
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.07-2
- Perl 5.26 rebuild

* Mon Apr 10 2017 Petr Pisar <ppisar@redhat.com> - 1.07-1
- 1.07 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-4
- Perl 5.24 rebuild

* Fri Mar 18 2016 Petr Pisar <ppisar@redhat.com> - 1.06-3
- Modernize spec file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-1
- 1.06 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-4
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Petr Šabata <contyk@redhat.com> - 1.05-1
- 1.05 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.04-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1.04-14
- Perl 5.16 rebuild

* Mon Jan 16 2012 Petr Šabata <contyk@redhat.com> - 1.04-13
- A new build with UTF8 German and Norwegian translations

* Mon Jan 16 2012 Petr Šabata <contyk@redhat.com> - 1.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
- Spec cleanup

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.04-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-9
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.04-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-4.1
Rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.04-3.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Fri Oct 27 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-3
- bump

* Fri Oct 27 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-2
- change summary
- tag certain files in %%doc with %%lang

* Thu Oct 26 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-1
- Specfile autogenerated by cpanspec 1.69.1.
