# Run optional test
%bcond_without perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test

Name:           perl-Dist-Zilla-Plugin-Git-Contributors
Version:        0.035
Release:        7%{?dist}
Summary:        Add contributor names from git to your distribution
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Git-Contributors
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Git-Contributors-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Data::Dumper)
# This is a Dist::Zilla plugin
BuildRequires:  perl(Dist::Zilla) >= 4.300039
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Git::Wrapper) >= 0.038
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(List::UtilsBy) >= 0.04
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny) >= 0.048
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Unicode::Collate) >= 0.53
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(parent)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
# Test::Warnings not used
BuildRequires:  perl(utf8)
%if %{with perl_Dist_Zilla_Plugin_Git_Contributors_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose::Conflicts)
BuildRequires:  perl(Pod::Weaver::Section::Contributors)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper)
# This is a Dist::Zilla plugin
Requires:       perl(Dist::Zilla) >= 4.300039
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
# Git::Wrapper 0.038 from META, CPAN RT#127045
Requires:       perl(Git::Wrapper) >= 0.038

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Git::Wrapper\\)

%description
This is a Dist::Zilla plugin that extracts all names and email addresses
from git commits in your repository and adds them to the distribution
metadata under the x_contributors key.

%prep
%setup -q -n Dist-Zilla-Plugin-Git-Contributors-%{version}

%build
export PERL_MM_FALLBACK_SILENCE_WARNING=1
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
unset AUTHOR_TESTING
make test

%files
%license LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.035-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.035-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.035-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Petr Pisar <ppisar@redhat.com> - 0.035-1
- 0.035 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.034-2
- Perl 5.28 rebuild

* Mon Apr 23 2018 Petr Pisar <ppisar@redhat.com> - 0.034-1
- 0.034 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.030-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.030-2
- Perl 5.26 rebuild

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 0.030-1
- 0.030 bump

* Thu Mar 23 2017 Petr Pisar <ppisar@redhat.com> 0.029-1
- Specfile autogenerated by cpanspec 1.78.
