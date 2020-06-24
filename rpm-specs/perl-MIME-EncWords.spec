Name:           perl-MIME-EncWords
Version:        1.014.3
Release:        17%{?dist}
Summary:        Deal with RFC 2047 encoded words (improved)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/MIME-EncWords
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/MIME-EncWords-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# MIME::Charset::USE_ENCODE is "Encode" on recent Perl
BuildRequires:  perl(Encode) >= 1.98
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64) >= 2.13
BuildRequires:  perl(MIME::Charset) >= 1.10.1
# MIME::Charset::_Compat not used
BuildRequires:  perl(strict)
# Unicode::String not used
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(charnames)
# Encode::CN not used
# Encode::JP not used
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# MIME::Charset::USE_ENCODE is "Encode" on recent Perl
Requires:       perl(Encode) >= 1.98
Requires:       perl(MIME::Base64) >= 2.13
Requires:       perl(MIME::Charset) >= 1.10.1

# Remove under-specfied dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((MIME::Base64|MIME::Charset)\\)$

%description
MIME::EncWords is aimed to be another implementation of MIME::Words so that it
will achieve more exact conformance with RFC 2047 (former RFC 1522)
specifications. Additionally, it contains some improvements. Following synopsis
and descriptions are inherited from its inspirer, then added descriptions on
improvements (**) or changes and clarifications (*).


%prep
%setup -q -n MIME-EncWords-%{version}

cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
sed -e '/perl(MIME::EncWords)$/d'
EOF

%global __perl_provides %{_builddir}/MIME-EncWords-%{version}/%{name}-prov
chmod +x %{__perl_provides}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc ARTISTIC Changes GPL README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.014.3-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.014.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.014.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.014.3-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.014.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.014.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.014.3-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.014.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.014.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.014.3-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.014.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.014.3-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.014.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Petr Pisar <ppisar@redhat.com> - 1.014.3-4
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.014.3-2
- Perl 5.22 rebuild

* Mon Sep 29 2014 Xavier Bachelot <xavier@bachelot.org> 1.014.3-1
- Update to 1.014.3.
- Clean up specfile.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.014.2-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Xavier Bachelot <xavier@bachelot.org> 1.014.2-1
- Update to 1.014.2.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.012.6-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Xavier Bachelot <xavier@bachelot.org> 1.012.6-1
- Update to 1.012.6.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.012.4-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Xavier Bachelot <xavier@bachelot.org> 1.012.4-1
- Update to 1.012.4.

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.012.3-2
- Perl mass rebuild

* Sat Jun 04 2011 Xavier Bachelot <xavier@bachelot.org> 1.012.3-1
- Update to 1.012.3.

* Wed Jun 01 2011 Xavier Bachelot <xavier@bachelot.org> 1.012.2-1
- Update to 1.012.2.

* Mon May 30 2011 Xavier Bachelot <xavier@bachelot.org> 1.012.1-1
- Update to 1.012.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.012-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Dec 17 2010 Xavier Bachelot <xavier@bachelot.org> 1.012-1
- Update to 1.012.
- Update Source0 URL.
- Add BuildRequires for better test coverage.

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.010.101-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.010.101-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.010.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 04 2009 Xavier Bachelot <xavier@bachelot.org> 1.010.101-2
- Better Description; tag.
- Filter duplicate Provides:.
- Remove unneeded Requires:.

* Fri Apr 24 2009 Xavier Bachelot <xavier@bachelot.org> 1.010.101-1
- Specfile autogenerated by cpanspec 1.77.
