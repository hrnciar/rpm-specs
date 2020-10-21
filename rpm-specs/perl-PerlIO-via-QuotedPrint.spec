Name:           perl-PerlIO-via-QuotedPrint
Version:        0.08
Release:        457%{?dist}
Summary:        PerlIO layer for quoted-printable strings
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/PerlIO-via-QuotedPrint
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/PerlIO-via-QuotedPrint-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
# Devel::Required not useful
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Conflicts:      perl < 4:5.22.0-347

%description
This module implements a PerlIO layer that works on files encoded in the
quoted-printable format. It will decode from quoted-printable while
reading from a handle, and it will encode as quoted-printable while
writing to a handle.

%prep
%setup -q -n PerlIO-via-QuotedPrint-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
# TODO is empty
%doc CHANGELOG README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-456
- Increase release to favour standalone package

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-349
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Petr Pisar <ppisar@redhat.com> 0.08-348
- Specfile autogenerated by cpanspec 1.78.
