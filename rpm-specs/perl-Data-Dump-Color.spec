Name:           perl-Data-Dump-Color
Version:        0.241
Release:        8%{?dist}
Summary:        Like Data::Dump, but with color
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Data-Dump-Color
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Data-Dump-Color-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util::LooksLikeNumber)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Data::Dump::Filtered)
Requires:       perl(Data::Dump::FilterContext)
Requires:       perl(MIME::Base64)

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Win32::Console::ANSI\\)

%description
This module aims to be a drop-in replacement for Data::Dump. It adds colors
to dumps. For more information, see Data::Dump. This documentation explains
what's different between this module and Data::Dump.

%prep
%setup -q -n Data-Dump-Color-%{version}
chmod +x share/examples/*.pl
perl -pi -e 's|^#! ?perl|#!%{__perl}|' share/examples/example2.pl

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.241-7
- Perl 5.32 rebuild

* Tue Mar 03 2020 Petr Pisar <ppisar@redhat.com> - 0.241-6
- Build-require blib module for the tests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.241-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.241-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.241-1
- Update to 0.241
- Drop Group tag

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.240-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.240-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.240-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.240-1
- 0.240 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-2
- Perl 5.22 rebuild

* Mon Nov 03 2014 Petr Šabata <contyk@redhat.com> - 0.23-1
- 0.23 bugfix bump

* Tue Oct 21 2014 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump

* Mon Sep 15 2014 Petr Šabata <contyk@redhat.com> - 0.21-2
- Correct the dep list

* Wed Sep 10 2014 Petr Šabata <contyk@redhat.com> 0.21-1
- Initial packaging
