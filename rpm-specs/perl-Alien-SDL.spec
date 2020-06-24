Name:           perl-Alien-SDL
Version:        1.446
Release:        17%{?dist}
Summary:        Building, finding and using SDL binaries
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Alien-SDL
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FROGGS/Alien-SDL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  gcc
BuildRequires:  freetype-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Archive::Extract)
# Not needed (https://github.com/PerlGameDev/SDL/issues/234):
# Archive::Tar
# Archive::Zip
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch) >= 0.24
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Patch) >= 1.4
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Capture::Tiny)
# Tests only:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(File::ShareDir) >= 1.00

%{?perl_default_filter}
%global __requires_exclude %__requires_exclude|^perl\\(File::ShareDir\\)$

%description
In short Alien::SDL can be used to detect and get configuration settings from 
an installed SDL and related libraries. Based on your platform it offers the 
possibility to download and install pre-built binaries or to build SDL & co. 
from source codes.

%prep
%setup -q -n Alien-SDL-%{version}
sed -i 's/\r//' README

%build
perl Build.PL installdirs=vendor --travis
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-11
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-10
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.446-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.446-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-2
- Perl 5.22 rebuild

* Mon Feb 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.446-1
- 1.446 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.444-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.444-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Pisar <ppisar@redhat.com> - 1.444-1
- 1.444 bump

* Thu Apr 24 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.442-1
- 1.442 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.440-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.440-2
- Perl 5.18 rebuild

* Wed Apr 17 2013 Petr Pisar <ppisar@redhat.com> - 1.440-1
- 1.440 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.438-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 10 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.438-1
- 1.438 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.436-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.436-2
- Perl 5.16 rebuild

* Mon Jun 25 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.436-1
- 1.436 bump

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 1.434-2
- Perl 5.16 rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1.434-1
- 1.434 bump

* Mon Jan 16 2012 Marcela Mašláňová <mmaslano@redhat.com> 1.430-1
- update to 1.430

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.428-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 01 2011 Marcela Mašláňová <mmaslano@redhat.com> 1.428-1
- Specfile autogenerated by cpanspec 1.79.
