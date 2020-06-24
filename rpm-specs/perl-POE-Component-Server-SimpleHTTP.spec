# Run optional test
%bcond_without perl_POE_Component_Server_SimpleHTTP_enables_optional_test

Name:           perl-POE-Component-Server-SimpleHTTP
Version:        2.28
Release:        6%{?dist}
Summary:        Serve HTTP requests in POE
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/POE-Component-Server-SimpleHTTP
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Component-Server-SimpleHTTP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Moose) >= 0.9
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::POE) >= 0.205
BuildRequires:  perl(POE) >= 1.0000
BuildRequires:  perl(POE::Component::SSLify) >= 0.04
BuildRequires:  perl(POE::Filter::HTTPD)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(POE::Filter::HTTP::Parser) >= 1.06
BuildRequires:  perl(POE::Kernel)
BuildRequires:  perl(Test::More) >= 0.47
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
BuildRequires:  perl(Test::POE::Client::TCP) >= 1.24
%if %{with perl_POE_Component_Server_SimpleHTTP_enables_optional_test}
# Optional tests only
BuildRequires:  perl(POE::Component::Client::HTTP) >= 0.82
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(HTTP::Request)
Requires:       perl(Moose) >= 0.9
Requires:       perl(Moose::Object)
Requires:       perl(MooseX::POE) >= 0.205
Requires:       perl(POE) >= 1.0000
Recommends:     perl(POE::Component::SSLify) >= 0.04
Requires:       perl(Storable)
Requires:       perl(Sys::Hostname)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Moose|MooseX::POE|POE)\\)$

%description
This module makes serving up HTTP requests a breeze in POE.

%prep
%setup -q -n POE-Component-Server-SimpleHTTP-%{version}
sed -i -e 's/\r$//g' examples/*

%build
yes | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README Changes Changes.old examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.28-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.28-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Petr Pisar <ppisar@redhat.com> - 2.28-1
- 2.28 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-2
- Perl 5.26 rebuild

* Fri Mar 10 2017 Petr Pisar <ppisar@redhat.com> - 2.26-1
- 2.26 bump

* Tue Feb 21 2017 Petr Pisar <ppisar@redhat.com> - 2.24-1
- 2.24 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-2
- Perl 5.24 rebuild

* Thu Feb 25 2016 Petr Šabata <contyk@redhat.com> - 2.22-1
- 2.22 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Petr Šabata <contyk@redhat.com> - 2.20-1
- 2.20 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-6
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 2.18-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Petr Šabata <contyk@redhat.com> - 2.18-1
- 2.18 bump, drop the MooseX::AttributeHelpers dependency
- Modernize the spec a little

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Petr Šabata <contyk@redhat.com> - 2.16-1
- 2.16 bump (Module::Install updated)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Petr Pisar <ppisar@redhat.com> - 2.14-2
- Perl 5.16 rebuild

* Tue Jan 17 2012 Petr Šabata <contyk@redhat.com> - 2.14-1
- 2.14 bump
- Spec cleanup
- Filter out underspecified dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.06-5
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 2.06-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.06-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Dec 09 2010 Iain Arnell <iarnell@gmail.com> 2.06-1
- update to latest upstream version
- fixes FTBFS RHBZ#660836
- clean up spec for modern rpmbuild

* Wed Jun 23 2010 Petr Pisar <ppisar@redhat.com> - 2.04-1
- 2.04 bump (bug #602616)
- Clean dependencies up

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.0-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.0-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 2.0-1
- auto-update to 2.0 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(Moose) (version 0.81)
- added a new br on perl(MooseX::AttributeHelpers) (version 0)
- added a new br on perl(MooseX::POE) (version 0.205)
- added a new req on perl(Moose) (version 0.81)
- added a new req on perl(MooseX::AttributeHelpers) (version 0)
- added a new req on perl(MooseX::POE) (version 0.205)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.58-1
- auto-update to 1.58 (by cpan-spec-update 0.01)
- added a new br on perl(Storable) (version 0)
- added a new br on perl(Sys::Hostname) (version 0)
- added a new br on perl(POE::Filter::HTTP::Parser) (version 0.02)
- added a new br on perl(Socket) (version 0)
- added a new br on perl(Test::POE::Client::TCP) (version 0.1)
- altered br on perl(POE) (0 => 1.0000)
- altered br on perl(Test::More) (0 => 0.47)
- added a new br on perl(Carp) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.48-1
- update to 1.48

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.23-3
- rebuild for new perl

* Sat Apr 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.23-2
- additional testing BR

* Sat Apr 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.23-1
- update to 1.23
- update source URL (maintainer changed)
- add BR's for potential perl splittage
- add BR's for tests -- note pod coverage fails, so we just leave that one
  commented out

* Fri Sep 29 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.13-1
- update to 1.13
- add examples/ to %%doc; correct encoding in %%prep
- explicitly requires perl(HTTP::Base); was missed due to a use base construct

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.11-3
- bump for mass rebuild

* Fri Aug 18 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.11-2
- bump

* Wed Aug 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.11-1
- Specfile autogenerated by cpanspec 1.68.
- Initial spec file for F-E
