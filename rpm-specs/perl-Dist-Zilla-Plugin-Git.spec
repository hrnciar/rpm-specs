# Run optional test
%bcond_without perl_Dist_Zilla_Plugin_Git_enables_optional_test

Name:           perl-Dist-Zilla-Plugin-Git
Version:        2.047
Release:        1%{?dist}
Summary:        Update your git repository after release
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Git
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Git-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  git-core >= 1.5.4
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(version) >= 0.80
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
# DateTime not used at tests
BuildRequires:  perl(Dist::Zilla) >= 4
BuildRequires:  perl(Dist::Zilla::Plugin::GatherDir) >= 4.200016
BuildRequires:  perl(Dist::Zilla::Role::AfterBuild)
# Dist::Zilla::Role::AfterMint not used at tests
BuildRequires:  perl(Dist::Zilla::Role::AfterRelease)
BuildRequires:  perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:  perl(Dist::Zilla::Role::FilePruner)
BuildRequires:  perl(Dist::Zilla::Role::GitConfig)
# Dist::Zilla::Role::PluginBundle not used at tests
BuildRequires:  perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Git::Wrapper) >= 0.021
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Has::Sugar)
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(Path::Tiny) >= 0.048
BuildRequires:  perl(String::Formatter)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Version::Next)
# Tests:
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Plugin::Config::Git)
BuildRequires:  perl(Dist::Zilla::Role::Releaser)
BuildRequires:  perl(Dist::Zilla::Tester)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Dispatchouli)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
%if %{with perl_Dist_Zilla_Plugin_Git_enables_optional_test}
# Optional tests
BuildRequires:  gnupg
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Moose::Conflicts)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(DateTime)
Requires:       perl(Dist::Zilla::Plugin::GatherDir) >= 4.200016
Requires:       perl(Dist::Zilla::Role::AfterBuild)
Requires:       perl(Dist::Zilla::Role::AfterMint)
Requires:       perl(Dist::Zilla::Role::AfterRelease)
Requires:       perl(Dist::Zilla::Role::BeforeRelease)
Requires:       perl(Dist::Zilla::Role::FilePruner)
Requires:       perl(Dist::Zilla::Role::GitConfig)
Requires:       perl(Dist::Zilla::Role::PluginBundle)
Requires:       perl(Dist::Zilla::Role::VersionProvider)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(:VERSION\\) >= 5\\.8\\.|^perl\\(Dist::Zilla\\) >= 2\\.

%description
This set of plugins for Dist::Zilla can do interesting things for module
authors using Git (http://git-scm.com/) to track their work.

%prep
%setup -q -n Dist-Zilla-Plugin-Git-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Sep 14 2020 Petr Pisar <ppisar@redhat.com> - 2.047-1
- 2.047 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.046-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.046-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.046-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.046-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.046-2
- Perl 5.30 rebuild

* Mon Mar 18 2019 Petr Pisar <ppisar@redhat.com> - 2.046-1
- 2.046 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.045-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.045-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.045-2
- Perl 5.28 rebuild

* Mon Jun 04 2018 Petr Pisar <ppisar@redhat.com> - 2.045-1
- 2.045 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Petr Pisar <ppisar@redhat.com> - 2.043-1
- 2.043 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.042-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.042-2
- Perl 5.26 rebuild

* Mon May 15 2017 Petr Pisar <ppisar@redhat.com> - 2.042-1
- 2.042 bump

* Thu Mar 23 2017 Petr Pisar <ppisar@redhat.com> 2.041-1
- Specfile autogenerated by cpanspec 1.78.
