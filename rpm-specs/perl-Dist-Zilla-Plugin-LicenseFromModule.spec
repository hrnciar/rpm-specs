Name:           perl-Dist-Zilla-Plugin-LicenseFromModule
Version:        0.07
Release:        6%{?dist}
Summary:        Extract license and copyright from its main module file
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-LicenseFromModule
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-LicenseFromModule-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# This is a Dist::Zilla plugin
BuildRequires:  perl(Dist::Zilla) >= 4.30003
BuildRequires:  perl(Dist::Zilla::Role::LicenseProvider)
BuildRequires:  perl(Module::Load) >= 0.32
BuildRequires:  perl(Moose)
BuildRequires:  perl(Software::LicenseUtils)
# Optional run-time:
# Prefer Pod::Escapes over Pod::Text
BuildRequires:  perl(Pod::Escapes)
# Tests:
BuildRequires:  perl(JSON)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# This is a Dist::Zilla plugin
Requires:       perl(Dist::Zilla) >= 4.30003
Requires:       perl(Dist::Zilla::Role::LicenseProvider)
Requires:       perl(Module::Load) >= 0.32
# Optional run-time:
# Prefer Pod::Escapes over Pod::Text
Recommends:     perl(Pod::Escapes)
Suggests:       perl(Pod::Text)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Module::Load\\)$

%description
This is is a Dist::Zilla plugin to extract license, author and copyright year
from your main module's POD document.

%prep
%setup -q -n Dist-Zilla-Plugin-LicenseFromModule-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Petr Pisar <ppisar@redhat.com> - 0.07-1
- 0.07 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-2
- Perl 5.26 rebuild

* Thu Mar 23 2017 Petr Pisar <ppisar@redhat.com> 0.05-1
- Specfile autogenerated by cpanspec 1.78.