Name:           perl-MooseX-Types-NetAddr-IP
Version:        0.07
Release:        9%{?dist}
Summary:        NetAddr::IP related types and coercions for Moose
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/MooseX-Types-NetAddr-IP
Source0:        https://cpan.metacpan.org/authors/id/T/TC/TCAINE/MooseX-Types-NetAddr-IP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(Moose) >= 0.41
BuildRequires:  perl(MooseX::Types) >= 0.19
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::clean) >= 0.08
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This package provides internet address types for Moose.

%prep
%autosetup -n MooseX-Types-NetAddr-IP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.07-2
- Constrain perl(ExtUtils::MakeMaker) to 6.76

* Mon Dec 04 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.07-1
- Specfile autogenerated by cpanspec 1.78.
