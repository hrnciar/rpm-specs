Name:           perl-Crypt-OpenSSL-X509
Version:        1.813
Release:        3%{?dist}
Summary:        Perl interface to OpenSSL for X509
License:        GPL+ or Artistic 
URL:            https://metacpan.org/release/Crypt-OpenSSL-X509
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASBN/Crypt-OpenSSL-X509-%{version}.tar.gz
# Respect distribution compiler flags
Patch0:         Crypt-OpenSSL-X509-1.813-Do-not-hard-code-CFLAGS.patch
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Compiler)
BuildRequires:  perl(Module::Install::External)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  openssl
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
# Run-time:
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DynaLoader)

%description
Crypt::OpenSSL::X509 - Perl extension to OpenSSL's X509 API.

%prep
%setup -q -n Crypt-OpenSSL-X509-%{version}
%patch0 -p1
# Remove bundled modules
rm -rf ./inc

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.813-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.813-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Wes Hardaker <wjhns174@hardakers.net> - 1.813-1
- upgrade to latest 1.813

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.812-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.812-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.812-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.812-1
- 1.812 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.808-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.808-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.808-1
- 1.808 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.807-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.807-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.807-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.807-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 27 2016 Petr Pisar <ppisar@redhat.com> - 1.807-2
- Adjust to OpenSSL 1.1.0 (bug #1383759)

* Wed Aug 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.807-1
- 1.807 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.806-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.806-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.806-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.806-2
- Perl 5.22 rebuild

* Wed Jun 10 2015 Petr Pisar <ppisar@redhat.com> - 1.806-1
- 1.806 bump

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.803-6
- Perl 5.22 rebuild

* Wed Feb 11 2015 Petr Pisar <ppisar@redhat.com> - 1.803-5
- Fix condition negation (bug #1190816)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.803-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.803-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.803-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 20 2013 Wes Hardaker <wjhns174@hardakers.net> - 1.803-1
- upgrade to latest 1.803

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.800.2-7
- Perl 5.18 rebuild
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.800.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.800.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.800.2-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.800.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.800.2-2
- Perl mass rebuild

* Wed May 11 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.800.2-1
- Another upstream minor release

* Thu May  5 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.800.1-2
- added new sources

* Thu May  5 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.800.1-1
- Update to the upstream 1.800.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Wes Hardaker <wjhns174@hardakers.net> - 1.6-1
- Updated to the upstream: 1.6

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.4-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Sep  9 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.4-2
- removed broken tests that are probably related to patches applied to
  the main openssl base

* Thu Sep  9 2010 Wes Hardaker <wjhns174@hardakers.net> - 1.4-1
- Update to the upstream

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.7-7
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.7-6
- rebuild against perl 5.10.1

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 0.7-5
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.7-2
- rebuild with new openssl

* Mon Jul 21 2008 Wes Hardaker <wjhns174@hardakers.net> - 0.7-1
- Updated to upstream 0.7

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6-2
Rebuild for new perl

* Mon Feb 25 2008 Wes Hardaker <wjhns174@hardakers.net> - 0.6-1
- bump to upstream 0.6

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5-4
- Autorebuild for GCC 4.3

* Thu Dec  6 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.5-3
- Bump to force rebuild with new openssl lib version

* Fri Nov  9 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.5-2
- Update license tag to the proper new wording

* Fri Nov  9 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.5-1
- update to upstream 0.5 containing a MANIFEST fix
- Add Test::Pod and Module::Install to build requirements

* Mon May 14 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.4-3
- BuildRequire perl(Test::More) perl(Test::Pod)
- Fixed source code URL

* Tue May  8 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.4-2
- Add BuildRequire openssl-devel
- Don't manually require openssl
- Use vendorarch instead of vendorlib 

* Thu Apr 19 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.4-1
- Initial version
