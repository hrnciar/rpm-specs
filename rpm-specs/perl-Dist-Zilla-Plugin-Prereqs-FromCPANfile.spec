Name:           perl-Dist-Zilla-Plugin-Prereqs-FromCPANfile
Version:        0.08
Release:        12%{?dist}
Summary:        Parse cpanfile for Dist::Zilla prerequisites
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Prereqs-FromCPANfile
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Zilla-Plugin-Prereqs-FromCPANfile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Dist::Zilla) >= 4.300017
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Module::CPANfile) >= 0.903
BuildRequires:  perl(Moose)
BuildRequires:  perl(Try::Tiny) >= 0.1
# Tests:
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
Requires:       perl(Dist::Zilla) >= 4.300017
Requires:       perl(Module::CPANfile) >= 0.903
Requires:       perl(Try::Tiny) >= 0.1

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::CPANfile|Try::Tiny)\\)$

%description
This is is a Dist::Zilla plugin to read cpanfile to determine prerequisites
for your distribution. This does the opposite of what
Dist::Zilla::Plugin::CPANFile does, which is to create a cpanfile using the
prerequisites collected elsewhere.

%prep
%setup -q -n Dist-Zilla-Plugin-Prereqs-FromCPANfile-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-11
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-2
- Perl 5.26 rebuild

* Thu Mar 23 2017 Petr Pisar <ppisar@redhat.com> 0.08-1
- Specfile autogenerated by cpanspec 1.78.
