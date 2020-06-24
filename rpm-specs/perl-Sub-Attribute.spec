Name:           perl-Sub-Attribute
Version:        0.07
Release:        5%{?dist}
Summary:        Reliable subroutine attribute handlers
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Sub-Attribute/
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Sub-Attribute-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# Run-time
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(attributes)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(strict)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Trigger) >= 0.14
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
# Optional tests
# Test::Pod 1.14
# Test::Pod::Coverage 1.04
# Test::Synopsis
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(parent) >= 0.221

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(parent\\)$

%description
Sub::Attribute is a role to define attribute handlers for specific
subroutine attributes.

%prep
%setup -q -n Sub-Attribute-%{version}
sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' example/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test SUB_ATTRIBUTE_DEBUG=0

%files
%doc CHANGELOG example README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sub*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-2
- Perl 5.30 rebuild

* Tue May 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-1
- Specfile autogenerated by cpanspec 1.78.