Name:           perl-List-SomeUtils-XS
Version:        0.58
Release:        9%{?dist}
Summary:        XS implementation for List::SomeUtils
License:        Artistic 2.0 and (GPL+ or Artistic)
URL:            https://metacpan.org/release/List-SomeUtils-XS
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-XS-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(List::SomeUtils::PP)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::SomeUtils) >= 0.56
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.006
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(List::SomeUtils::PP)
Requires:       perl(XSLoader)

%description
List::SomeUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

XS implementation is faster than List::SomeUtils.

%prep
%setup -q -n List-SomeUtils-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/List*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-2
- Perl 5.28 rebuild

* Mon Jun 11 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-1
- 0.58 bump

* Mon May 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-1
- 0.57 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-1
- 0.56 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Petr Pisar <ppisar@redhat.com> - 0.55-1
- 0.55 bump

* Thu Jun 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-1
- 0.53 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-2
- Perl 5.24 rebuild

* Mon May 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-1
- 0.52 bump

* Tue Mar 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-2
- Updated license and description

* Thu Mar 10 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-1
- Initial release
