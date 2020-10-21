Name:           perl-Net-Pcap
Version:        0.18
Release:        16%{?dist}
Summary:        Interface to pcap(3) LBL packet capture library

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-Pcap
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAPER/Net-Pcap-%{version}.tar.gz
# Adapt a test to libpcap-1.8.0, bug #1375919, CPAN RT#117831
Patch0:         Net-Pcap-0.18-Adapt-a-test-to-libpcap-1.8.0.patch
# Fix build with libpcap-1.9.0, bug #1612860
Patch1:         Net-Pcap-0.18-Fix-build-with-libpcap-1.9.0.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
# ExtUtils::Constant || File::Copy
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
# DynaLoader not used if XSLoader is available
BuildRequires:  perl(Exporter)
# Sys::Hostname not used at tests
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More) >= 0.45
# Optional tests:
# POE not usefull without POE::Component::Pcap
# POE::Component::Pcap not yet packaged
BuildRequires:  perl(Test::Distribution)
# Test::Spelling not used
# Test::Portability::Files not used
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# DynaLoader not used if XSLoader is available
Requires:  perl(XSLoader)

%{?perl_default_filter}

%description
perl-Net-Pcap provides Perl bindings to the LBL pcap(3) library.

%prep
%setup -q -n Net-Pcap-%{version}
%patch0 -p1
%patch1 -p1

for f in README Changes ; do
  iconv -f iso-8859-1 -t utf-8 $f >$f.conv && mv -f $f.conv $f
done

chmod 0644 eg/*

sed -i -e '1s~#!perl~#!%{__perl}~' t/*.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%doc eg/ t/
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net
%{_mandir}/man?/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-15
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-10
- Fix build with libpcap-1.9.0 (bug #1612860)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 05 2016 Petr Pisar <ppisar@redhat.com> - 0.18-2
- Adapt a test to libpcap-1.8.0 (bug #1375919)

* Mon May 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- 0.18 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 15 2015 Petr Pisar <ppisar@redhat.com> - 0.17-10
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-8
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.17-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Iain Arnell <iarnell@gmail.com> 0.17-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.16-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 18 2011 Iain Arnell <iarnell@gmail.com> 0.16-12
- rename patch and clarify that it's EU:MM related, not EU::CB

* Fri Jun 17 2011 Iain Arnell <iarnell@gmail.com> 0.16-11
- patch to workaround ExtUtils::CBuilder behavior change
  see http://rt.perl.org/rt3/Public/Bug/Display.html?id=89478

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-10
- Perl mass rebuild

* Tue Jun 14 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-9
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-7
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-6
- Mass rebuild with perl-5.12.0

* Wed Mar 03 2010 Iain Arnell <iarnell@gmail.com> 0.16-5
- include patch from Jose Pedro Oliveira to fix eg/pcapdump (BZ#569915)

* Tue Mar 02 2010 Iain Arnell <iarnell@gmail.com> 0.16-4
- include examples as documentation
- use perl_default_filter and DESTDIR
- silence rpmlint

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.16-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 0.16-1
- New upstream release

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.14-4
- rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.14-3
- Autorebuild for GCC 4.3

* Tue May 08 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.14-2
- Add missing BR
- Chance License to GPL or Artistic
- Update %%files
- Include t/ in %%doc
* Thu May 03 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.14-1
- Initial build
