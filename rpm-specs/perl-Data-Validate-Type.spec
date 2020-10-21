Name:           perl-Data-Validate-Type
Version:        1.6.0
Release:        13%{?dist}
Summary:        Public interface to Params::Util offering data type validation functions
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Validate-Type
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUBERTG/Data-Validate-Type-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module presents an alternative API to Params::Util which fixes a number
of drawbacks (function names start with an underscore, are uppercase and don't
pass PerlCritic validation).

%prep
%setup -q -n Data-Validate-Type-v%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-12
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-3
- Perl 5.26 rebuild

* Sun Mar 26 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.6.0-2
- Update license field

* Sun Mar 26 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.6.0-1
- Update to 1.6.0
- Rework dependencies

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.1-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.1-3
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.1-2
- Perl 5.20 rebuild

* Sun Jun 15 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.5.1-1
- Update to 1.5.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.5.0-1
- Update to 1.5.0

* Sun Apr 27 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.4.3-1
- Update to 1.4.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.4.2-2
- Perl 5.18 rebuild

* Wed May 08 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.4.2-1
- Update to 1.4.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 25 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 1.4.0-1
- Update to 1.4.0

* Sun Sep 23 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 1.3.1-1
- Update to 1.3.1

* Fri Sep 14 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 1.3.0-2
- Take into account package review (#855665)

* Sun Sep 09 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.3.0-1
- Initial creation
