Name:           perl-Module-Runtime-Conflicts
Version:        0.003
Release:        13%{?dist}
Summary:        Provide information on conflicts for Module::Runtime
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Module-Runtime-Conflicts
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Module-Runtime-Conflicts-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Dist::CheckConflicts)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

Requires:       perl(Dist::CheckConflicts)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides conflicts checking for Module::Runtime, which had a
recent release that broke some versions of Moose. It is called from
Moose::Conflicts and moose-outdated.

%prep
%setup -q -n Module-Runtime-Conflicts-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING README
%license LICENCE
%{perl_vendorlib}/Module*
%{_mandir}/man3/Module*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 24 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.003-1
- Update to 0.003

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-2
- Perl 5.22 rebuild

* Sun Mar 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.002-1
- Update to 0.002

* Mon Nov 24 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.001-3
- Add perl(strict) as a BuildRequires

* Mon Nov 24 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.001-2
- Version the requirements of Module::Build::Tiny and Test::More

* Sun Nov 23 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.001-1
- Specfile autogenerated by cpanspec 1.78.
