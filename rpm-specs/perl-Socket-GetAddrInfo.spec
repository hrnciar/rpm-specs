Name:           perl-Socket-GetAddrInfo
Version:        0.22
Release:        20%{?dist}
Summary:        RFC 2553's "getaddrinfo" and "getnameinfo" functions

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Socket-GetAddrInfo
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Socket-GetAddrInfo-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The RFC 2553 functions getaddrinfo and getnameinfo provide an abstracted
way to convert between a pair of host name/service name and socket
addresses, or vice versa. getaddrinfo converts names into a set of
arguments to pass to the socket() and connect() syscalls, and getnameinfo
converts a socket address back into its host name/service name pair.

%prep
%setup -q -n Socket-GetAddrInfo-%{version}


%build
%{__perl} Build.PL installdirs=vendor


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} $RPM_BUILD_ROOT/*


%check
%{?_with_tests:export I_CAN_HAS_INTERNETS=1}

./Build test


%files
%doc Changes LICENSE README
%{perl_vendorlib}/Socket*
%{_bindir}/get*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-20
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-17
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-14
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-6
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.22-2
- Perl 5.18 rebuild

* Sun Jun 09 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.22-1
- Update to 0.22
- Switch to Build.PL as a build mechanism
- Add perl default filter
- Remove no-longer-used macros

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.19-2
- Perl 5.16 rebuild

* Thu Jan 19 2012 Petr Šabata <contyk@redhat.com> - 0.19-1
- Just updating to 0.19, as it's needed by current POE::* packages

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.16-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.16-1
- Update to 0.16

* Wed Jun  2 2010 Petr Pisar <ppisar@redhat.com> - 0.15-6
- Rebuild against perl-5.12

* Fri May 07 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.15-5
- Add BR perl(ExtUtils::CChecker)
- Add BR perl(Test::Warn)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.15-2
- Mass rebuild with perl-5.12.0

* Mon Apr 19 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.15-1
- Update to 0.15

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.12-2
- rebuild against perl 5.10.1

* Thu Jul  9 2009 kwizart < kwizart at gmail.com > - 0.12-1
- Initial spec
