Name:		perl-B-Hooks-Parser
Version:	0.21
Release:	5%{?dist}
Summary:	Interface to perl's parser variables
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/B-Hooks-Parser
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-Parser-%{version}.tar.gz

BuildRequires:	perl-interpreter
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(B::Hooks::EndOfScope)
BuildRequires:	perl(B::Hooks::OP::Check)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Depends) >= 0.302
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(parent)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Module::Metadata)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	coreutils
BuildRequires:	make

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides an API for parts of the perl parser. It can be used to
modify code while it's being parsed.

%prep
%setup -q -n B-Hooks-Parser-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -delete

cp LICENCE LICENSE

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes CONTRIBUTING README
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%{perl_vendorarch}/auto/B
%{perl_vendorarch}/B
%{_mandir}/man3/B::Hooks::Parser.3pm*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-2
- Perl 5.30 rebuild

* Sun Apr 14 2019 Bill Pemberton <wfp5p@worldbroken.com> - 0.21-1
- update to version 0.21
- version 0.20 would not build with a multithreaded perl

* Sun Apr 14 2019 Bill Pemberton <wfp5p@worldbroken.com> - 0.20-1
- update to version 0.20
- will now use core functions directly when available

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-7
- Add build-require gcc

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.26 rebuild

* Wed Apr  5 2017 Bill Pemberton <wfp5p@worldbroken.com> - 0.19-1
- update to version 0.19

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug  8 2016 Bill Pemberton <wfp5p@worldbroken.com> - 0.17-1
- update to version 0.17

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Bill Pemberton <wfp5p@worldbroken.com> - 0.16-2
- Update BuildRequires to add DynaLoader, strict, and warnings
- Add version requirement for  perl(ExtUtils::Depends)
- remove perl(parent) from requires
- update files section to pick up B dirs

* Wed Sep 16 2015 Bill Pemberton <wfp5p@worldbroken.com> - 0.16-1
- Initial version
