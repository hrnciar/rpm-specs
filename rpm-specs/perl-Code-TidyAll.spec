Name:           perl-Code-TidyAll
Version:        0.78
Release:        3%{?dist}
Summary:        Engine for tidyall, your all-in-one code tidier and validator
# lib/Test/Code/TidyAll.pm:     GPL+ or Artistic
# LICENSE:                      GPL+ or Artistic
## Not in the binary package
# etc/editors/tidyall.el:       GPLv2+
# node_modules/jshint/node_modules/cli/node_modules/glob/LICENSE:   BSD
# node_modules/js-beautify/node_modules/mkdirp/node_modules/minimist/LICENSE:  MIT
# php5/usr/share/php/PHP/CodeSniffer/Standards/PEAR/Docs/Commenting/FileCommentStandard.xml: MIT
# php5/usr/share/php/test/PHP_CodeSniffer/CodeSniffer/Standards/Squiz/Tests/Commenting/FileCommentUnitTest.js: PHP
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Code-TidyAll
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Code-TidyAll-%{version}.tar.gz
Source1:        README.nodejs_plugins
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(IPC::System::Simple)
# Not used for tests - perl(JSON::MaybeXS)
# Not used for tests - perl(List::Compare)
BuildRequires:  perl(List::SomeUtils)
# Not used for tests - perl(Log::Any)
# Not used for tests - perl(Mason::Tidy)
# Not used for tests - perl(Mason::Tidy::App)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2.000000
BuildRequires:  perl(Moo::Role)
# Not used for tests - perl(Parallel::ForkManager)
BuildRequires:  perl(Path::Tiny) >= 0.098
# Not used for tests - perl(Perl::Tidy)
# Not used for tests - perl(Perl::Tidy::Sweetened)
# Not used for tests - perl(Pod::Checker)
# Not used for tests - perl(Pod::Spell)
# Not used for tests - perl(Pod::Tidy)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Specio) >= 0.40
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::Path::Tiny) >= 0.04
BuildRequires:  perl(Specio::Library::String)
# Not used for tests - perl(SVN::Look)
BuildRequires:  perl(Text::Diff) >= 1.44
# Not used for tests - perl(Test::Builder)
# Not used for tests - perl(Text::Diff)
# Not used for tests - perl(Text::Diff::Table)
# Not used for tests - perl(Text::ParseWords)
BuildRequires:  perl(Time::Duration::Parse)
BuildRequires:  perl(Try::Tiny)
# Tests
BuildRequires:  perl(autodie)
# Not used for tests - perl(Encode)
BuildRequires:  perl(lib)
BuildRequires:  perl(lib::relative)
BuildRequires:  perl(Test::Class::Most)
# Not used for tests - perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       aspell
Requires:       git
Requires:       nodejs
Requires:       perl-Mason-Tidy
Requires:       perl-Perl-Critic
Requires:       php-pear-PHP-CodeSniffer
Requires:       subversion
Requires:       perl(Getopt::Long)
Requires:       perl(Parallel::ForkManager) >= 1.19


%description
This is the engine used by tidyall. You can call this API from your own
program instead of executing tidyall.

tidyall is all-in-one code tidier and validator.

%prep
%setup -q -n Code-TidyAll-%{version}
cp %{SOURCE1} .

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.md README.nodejs_plugins CONTRIBUTING.md
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-2
- Perl 5.32 rebuild

* Mon Apr 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.78-1
- 0.78 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-1
- 0.75 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-2
- Perl 5.30 rebuild

* Tue May 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-1
- 0.74 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.73-1
- 0.73 bump

* Wed Jan 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.72-1
- 0.72 bump

* Mon Sep 17 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.71-1
- 0.71 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-2
- Perl 5.28 rebuild

* Fri Apr 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-1
- 0.70 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-1
- 0.69 bump

* Mon Oct 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.68-1
- 0.68 bump

* Tue Sep 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.67-1
- 0.67 bump

* Wed Aug 02 2017 Petr Pisar <ppisar@redhat.com> - 0.65-1
- 0.65 bump

* Tue Aug 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.64-1
- 0.64 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Petr Pisar <ppisar@redhat.com> - 0.63-1
- 0.63 bump

* Fri Jul 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-1
- 0.62 bump

* Mon Jul 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-1
- 0.61 bump

* Tue Jul 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-1
- 0.60 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-2
- Perl 5.26 rebuild

* Mon May 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-1
- 0.59 bump

* Mon Mar 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-1
- 0.58 bump

* Mon Feb 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-1
- 0.57 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-1
- 0.56 bump

* Wed Nov 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-1
- 0.55 bump

* Mon Oct 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-1
- 0.54 bump

* Tue Oct 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-1
- 0.53 bump

* Tue Sep 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-1
- 0.52 bump

* Mon Jul 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-1
- 0.49 bump

* Fri Jun 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.48-1
- 0.48 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.47-2
- Perl 5.24 rebuild

* Tue May 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.47-1
- 0.47 bump

* Tue Apr 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.46-1
- 0.46 bump

* Mon Apr 11 2016 Petr Pisar <ppisar@redhat.com> - 0.44-1
- 0.44 bump

* Tue Mar 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-1
- 0.43 bump

* Fri Mar 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-1
- 0.42 bump

* Mon Feb 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-1
- 0.40 bump

* Mon Feb 15 2016 Petr Pisar <ppisar@redhat.com> - 0.39-1
- 0.39 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Petr Pisar <ppisar@redhat.com> - 0.38-1
- 0.38 bump

* Tue Dec 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-1
- 0.37 bump
- Update due to review comments

* Thu Dec 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-1
- Initial import
