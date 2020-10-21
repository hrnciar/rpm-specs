Name:           perl-Dist-Zilla-Plugin-Test-Compile
Version:        2.058
Release:        10%{?dist}
Summary:        Common tests to check syntax of your modules, only using core modules
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Test-Compile
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Test-Compile-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# XXX: BuildRequires:  perl(Data::Dumper)
# XXX: BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Data::Section) >= 0.004
BuildRequires:  perl(Dist::Zilla::Dist::Builder)
# XXX: BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Role::FileFinderUser)
BuildRequires:  perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sub::Exporter::ForMethods)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(File::pushd) >= 1.004
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::CoreList) >= 2.77
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Perl::PrereqScanner) >= 1.016
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Dist::Zilla::File::InMemory)
Requires:       perl(Dist::Zilla::Role::FileFinderUser)
Requires:       perl(Dist::Zilla::Role::FileGatherer)
Requires:       perl(Dist::Zilla::Role::FileMunger)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
Requires:       perl(Dist::Zilla::Role::TextTemplate)

%description
This is a Dist::Zilla plugin that runs at the gather files stage, providing
a test file (configurable, defaulting to t/00-compile.t).

%prep
%setup -q -n Dist-Zilla-Plugin-Test-Compile-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENCE
%doc Changes AUTHOR_PLEDGE CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.058-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.058-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.058-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.058-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.058-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.058-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.058-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.058-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.058-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Petr Šabata <contyk@redhat.com> - 2.058-1
- 2.058 bump

* Mon Aug 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.057-1
- 2.057 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.056-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.056-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.056-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Petr Šabata <contyk@redhat.com> - 2.056-1
- 2.056 bump

* Tue Oct 25 2016 Petr Šabata <contyk@redhat.com> - 2.055-1
- 2.055 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.054-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.054-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Petr Šabata <contyk@redhat.com> - 2.054-1
- 2.054 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.053-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.053-2
- Perl 5.22 rebuild

* Mon Jun 01 2015 Petr Šabata <contyk@redhat.com> - 2.053-1
- 2.053 bump

* Thu Apr 02 2015 Petr Šabata <contyk@redhat.com> - 2.052-1
- 2.052 bump

* Thu Mar 26 2015 Petr Šabata <contyk@redhat.com> 2.051-1
- Initial packaging
