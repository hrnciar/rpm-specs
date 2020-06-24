Name:           perl-Tk-ProgressBar-Mac
Version:        1.2
Release:        31%{?dist}
Summary:        Mac ProgressBar for Perl::Tk

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Tk-ProgressBar-Mac
Source0:        http://cpan.org/modules/by-module/Tk/Tk-ProgressBar-Mac-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::MMutil)
BuildRequires:  xorg-x11-server-Xvfb, xorg-x11-fonts-base
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This widget provides a dynamic image that looks just like
a Mac OS 9 progress bar.  Packed around it are four
Frames, north, south, east and west, within which you can
stuff additional widgets. For example, see how Tk::Copy::Mac
uses several Labels and a CollapsableFrame widget to create
a reasonable facsimile of a Macintosh copy dialog.


%prep
%setup -q -n Tk-ProgressBar-Mac-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
# disabled by default because it needs an x screen
%{?_with_tests:make test}

%files
%doc README
%{perl_vendorlib}/Tk*
%{_mandir}/man3/Tk*.3*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-29
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-26
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-23
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-21
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-18
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-17
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.2-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.2-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.2-9
- Add BR: perl(Tk::MMutil).

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.2-8
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.2-6
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.2-5
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.2-4
- rebuild against perl 5.10.1

* Mon Sep 14 2009 David Hannequin <david.hannequin@gmail.com> 1.2-3
- Fix license 

* Tue May 30 2009 David Hannequin <david.hannequin@gmail.com> 1.2-2
- delete _xvfb
- modify man page

* Thu May 21 2009 David Hannequin <david.hannequin@gmail.com> 1.2-1
- First release.

