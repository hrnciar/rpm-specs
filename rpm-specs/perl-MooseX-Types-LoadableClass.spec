Name:           perl-MooseX-Types-LoadableClass
Version:        0.015
Release:        10%{?dist}
Summary:        ClassName type constraint with coercion to load the class
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/MooseX-Types-LoadableClass
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-LoadableClass-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.030
# Run-time:
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
ClassName type constraint with coercion to load the class.

%prep
%setup -q -n MooseX-Types-LoadableClass-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install '--destdir=%{buildroot}' --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENCE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.015-1
- Update to 0.015

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.014-2
- Use %%license tag

* Sat Aug 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.014-1
- Update to 0.014

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-2
- Perl 5.22 rebuild

* Fri Nov 21 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.013-1
- Update to 0.13
- Tighten file listing

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.012-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 09 2014 Petr Pisar <ppisar@redhat.com> - 0.012-1
- 0.012 bump

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.008-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.008-2
- Perl 5.16 rebuild

* Wed Mar 14 2012 Iain Arnell <iarnell@gmail.com> 0.008-1
- update to latest upstream

* Tue Feb 21 2012 Iain Arnell <iarnell@gmail.com> 0.007-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 29 2011 Iain Arnell <iarnell@gmail.com> 0.006-1
- Specfile autogenerated by cpanspec 1.78.
