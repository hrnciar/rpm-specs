# Run optinonal test
%bcond_without perl_Dist_Zilla_Plugins_CJM_enables_optional_test

Name:           perl-Dist-Zilla-Plugins-CJM
Version:        6.000
Release:        9%{?dist}
Summary:        Christopher J. Madsen's Dist::Zilla plugins
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Plugins-CJM
Source0:        https://cpan.metacpan.org/modules/by-module/Dist/Dist-Zilla-Plugins-CJM-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(CPAN::Meta::Converter) >= 2.101550
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(Data::Dumper)
# A Dist::Zilla plugin, version from META
BuildRequires:  perl(Dist::Zilla) >= 6
BuildRequires:  perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:  perl(Dist::Zilla::Plugin::MakeMaker) >= 4.300009
BuildRequires:  perl(Dist::Zilla::Plugin::ModuleBuild)
BuildRequires:  perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:  perl(Dist::Zilla::Role::FilePruner)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::Releaser)
BuildRequires:  perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir) >= 0.81
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(version) >= 0.77
# Tests:
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
%if %{with perl_Dist_Zilla_Plugins_CJM_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Fatal)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(CPAN::Meta::Converter) >= 2.101550
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Data::Dumper)
# A Dist::Zilla plugin, version from META
Requires:       perl(Dist::Zilla) >= 6
Requires:       perl(Dist::Zilla::Plugin::InlineFiles)
Requires:       perl(Dist::Zilla::Plugin::ModuleBuild)
Requires:       perl(Dist::Zilla::Role::BeforeRelease)
Requires:       perl(Dist::Zilla::Role::FilePruner)
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::Releaser)
Requires:       perl(Dist::Zilla::Role::VersionProvider)
Requires:       perl(File::Copy)
Requires:       perl(File::HomeDir) >= 0.81

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(CPAN::Meta::Requirements\\)$

%description
This is a collection of plugins Christopher J. Madsen has written for
Dist::Zilla, a Perl build an release management tool.

%prep
%setup -q -n Dist-Zilla-Plugins-CJM-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.000-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.000-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.000-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Petr Pisar <ppisar@redhat.com> - 6.000-1
- 6.000 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.27-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Petr Pisar <ppisar@redhat.com> 4.27-1
- Specfile autogenerated by cpanspec 1.78.
