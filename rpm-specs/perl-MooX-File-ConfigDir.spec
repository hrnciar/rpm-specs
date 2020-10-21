Name:           perl-MooX-File-ConfigDir
Version:        0.007
Release:        9%{?dist}
Summary:        Moo eXtension for File::ConfigDir
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/MooX-File-ConfigDir
Source0:        https://cpan.metacpan.org/modules/by-module/MooX/MooX-File-ConfigDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ConfigDir) >= 0.018
BuildRequires:  perl(FindBin)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role) >= 1.003000
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(warnings)
Requires:       perl(File::ConfigDir) >= 0.018
Requires:       perl(Moo::Role) >= 1.003000
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(File::ConfigDir\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo::Role\\)$

%description
This module is a helper for easily find configuration file locations.
Whether to use this information for find a suitable place for installing
them or looking around for finding any piece of settings, heavily depends
on the requirements.

%prep
%setup -q -n MooX-File-ConfigDir-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-2
- Perl 5.28 rebuild

* Fri May 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-1
- 0.007 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-2
- Perl 5.26 rebuild

* Tue May 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-1
- 0.006 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-1
- 0.005 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.004-2
- Perl 5.22 rebuild

* Sun Jan 18 2015 David Dick <ddick@cpan.org> - 0.004-1
- Add README.md

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-2
- Perl 5.20 rebuild

* Tue Jul 22 2014 David Dick <ddick@cpan.org> - 0.003-1
- Initial release
