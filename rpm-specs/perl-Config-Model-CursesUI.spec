Name:           perl-Config-Model-CursesUI
Version:        1.106
Release:        12%{?dist}
Summary:        Curses interface to edit config data
License:        LGPLv2+
URL:            https://metacpan.org/release/Config-Model-CursesUI
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-CursesUI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model) >= 0.637
BuildRequires:  perl(Config::Model::Exception)
BuildRequires:  perl(Config::Model::ObjTreeScanner)
BuildRequires:  perl(Curses::UI) >= 0.9606
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class provides a Curses::UI interface to configuration data managed by
Config::Model.

%prep
%setup -q -n Config-Model-CursesUI-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-11
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.106-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.106-2
- Perl 5.26 rebuild

* Sun May 14 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.106-1
- Update to 1.106

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.105-2
- Perl 5.24 rebuild

* Tue Mar 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.105-1
- 1.105 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.104-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.104-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.104-12
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.104-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.104-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.104-9
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.104-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.104-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.104-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 1.104-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.104-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.104-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.104-2
- Perl mass rebuild

* Wed Mar 9 2011 david.hannequin@gmail.com 1.104-1
- update from upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.103-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.103-5
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Jun 27 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 1.103-4
- Rebuild for perl-5.12.

* Sun Nov 8 2009 david.hannequin@gmail.com 1.103-3
- Fix license

* Tue Oct 27 2009 david.hannequin@gmail.com 1.103-2
- Add build require Test::More

* Mon Aug 03 2009 david.hannequin@gmail.com 1.103-1
- Initial release 
