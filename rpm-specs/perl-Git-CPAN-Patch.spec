Name:           perl-Git-CPAN-Patch
Summary:        Patch CPAN modules using Git
Version:        2.3.4
Release:        6%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Git-CPAN-Patch-%{version}.tar.gz
URL:            https://metacpan.org/release/Git-CPAN-Patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Archive::Any)
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(autodie)
BuildRequires:  perl(BackPAN::Index)
BuildRequires:  perl(CLASS)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::ParseDistribution)
BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(experimental)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::chmod)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Git::Repository)
BuildRequires:  perl(List::Pairwise)
# BuildRequires:  perl(LWP::Simple)
# BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MetaCPAN::API)
BuildRequires:  perl(MetaCPAN::Client)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::App)
BuildRequires:  perl(MooseX::App::Command)
BuildRequires:  perl(MooseX::App::Role)
BuildRequires:  perl(MooseX::SemiAffordanceAccessor)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Tiny)
# BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
# Tests only
BuildRequires:  git
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DDP)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Git::Repository::Plugin::AUTOLOAD)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       git
Requires:       perl(CPAN::Meta)
Requires:       perl(CPAN::ParseDistribution)
Requires:       perl(File::Copy)
Requires:       perl(LWP::Simple)
Requires:       perl(LWP::Protocol::ftp)
Requires:       perl(LWP::Protocol::http)
Requires:       perl(LWP::UserAgent)

%{?perl_default_filter}

%description
Git::CPAN::Patch provides a suite of git commands aimed at making trivially
easy the process of grabbing any distribution off CPAN, stuffing it in a
local git repository and, once gleeful hacking has been perpetrated,
sending back patches to its maintainer.

This package provides the backend Perl modules required.  For the git
commands, etc, please install the git-cpan-patch package.

%package -n git-cpan-patch
Summary:        Patch CPAN modules using Git
License:        GPL+ or Artistic
Requires:       perl-Git-CPAN-Patch = %{version}-%{release}
Requires:       git, git-email

%description -n git-cpan-patch
git-cpan-patch provides a suite of git commands aimed at making trivially
easy the process of grabbing any distribution off CPAN, stuffing it in a
local git repository and, once gleeful hacking has been perpetrated,
sending back patches to its maintainer.

%prep
%setup -q -n Git-CPAN-Patch-%{version}
# Fix shellbang
sed -i -e '1 s|^#!/usr/bin/env perl|#!perl|' bin/git-cpan

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# upstream now installs to /usr/bin; we still prefer /usr/libexec/git-core
install -d -m 0755 %{buildroot}%{_libexecdir}/git-core
mv %{buildroot}/%{_bindir}/* %{buildroot}%{_libexecdir}/git-core/

%check
git config --global user.email "perl-Git-CPAN-Patch-owner@fedoraproject.org"
git config --global user.name "perl-Git-CPAN-Patch Owner"
make test

%files
%license LICENSE
%doc AUTHOR_PLEDGE Changes README.mkdn
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files -n git-cpan-patch
%license LICENSE
%doc AUTHOR_PLEDGE Changes README.mkdn
%{_libexecdir}/*
%{_mandir}/man1/*

%changelog
* Thu Mar 12 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.4-6
- Add BR: perl(blib)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.4-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.4-1
- 2.3.4 bump

* Thu Aug 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.3-1
- 2.3.3 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.2-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.2-1
- 2.3.2 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.1-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.1-1
- 2.3.1 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.0-2
- Perl 5.24 rebuild

* Thu Apr 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.0-1
- 2.3.0 bump

* Mon Feb 08 2016 Petr Šabata <contyk@redhat.com> - 2.2.1-1
- 2.2.1 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Petr Šabata <contyk@redhat.com> - 2.2.0-1
- 2.2.0 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.0-11
- Perl 5.22 rebuild

* Mon Mar 02 2015 Petr Pisar <ppisar@redhat.com> - 2.0.3-10
- Do not use /usr/bin/env to interpret git-cpan

* Thu Dec 18 2014 Petr Šabata <contyk@redhat.com> - 2.0.3-9
- Correct MODULE_COMPAT

* Tue Dec 16 2014 Petr Šabata <contyk@redhat.com> - 2.0.3-8
- 2.0.3 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.8.0-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Petr Pisar <ppisar@redhat.com> - 0.8.0-6
- Do not test MooseX::App::Cmd::Command without Moose (bug #1089247)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.8.0-2
- Perl 5.16 rebuild

* Fri Jun 29 2012 Iain Arnell <iarnell@gmail.com> 0.8.0-1
- update to latest upstream version
- add AUTHOR_PLEDGE to docs

* Sat Feb 11 2012 Iain Arnell <iarnell@gmail.com> 0.7.0-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- add LICENSE to docs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.4.6-5
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.4.6-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 09 2011 Iain Arnell <iarnell@gmail.com> 0.4.6-2
- move git-cpan-* scripts back to libexecdir

* Sun Jan 09 2011 Iain Arnell <iarnell@gmail.com> 0.4.6-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.4.4)
- added a new br on perl(BackPAN::Index) (version 0.39)
- added a new br on perl(CLASS) (version 0)
- added a new br on perl(File::Path) (version 0)
- added a new br on perl(File::Temp) (version 0.22)
- added a new br on perl(File::chmod) (version 0)
- force-adding ExtUtils::MakeMaker as a BR
- dropped old BR on perl(Parse::BACKPAN::Packages)
- added a new req on perl(BackPAN::Index) (version 0.39)
- added a new req on perl(File::Temp) (version 0.22)
- dropped old requires on perl(Module::Build)
- dropped old requires on perl(Parse::BACKPAN::Packages)

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2.1-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2.1-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.2.1-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.2.1-1
- auto-update to 0.2.1 (by cpan-spec-update 0.01)
- altered br on perl(CPANPLUS) (0 => 0.84)
- added a new br on perl(File::chdir) (version 0)
- altered req on perl(CPANPLUS) (0 => 0.84)
- added a new req on perl(File::chdir) (version 0)

* Tue Aug 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.2.0-2
- add a BR on git, for command paths

* Tue Aug 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.2.0-1
- auto-update to 0.2.0 (by cpan-spec-update 0.01)
- added a new req on perl(CPANPLUS) (version 0)
- added a new req on perl(Module::Build) (version 0)
- added a new req on perl(Parse::BACKPAN::Packages) (version 0)
- added a new req on perl(Pod::Usage) (version 0)
- added a new req on perl(autodie) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.1.7-1
- auto-update to 0.1.7 (by cpan-spec-update 0.01)

* Tue May 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.1.6-1
- auto-update to 0.1.6 (by cpan-spec-update 0.01)
- added a new br on perl(Pod::Usage) (version 0)

* Sat Mar 28 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.1.5-1
- update to 0.1.5

* Wed Mar 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.1.4-2
- break into main package + git-cpan-patch

* Fri Mar 06 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.1.4-1
- Specfile autogenerated by cpanspec 1.77.
