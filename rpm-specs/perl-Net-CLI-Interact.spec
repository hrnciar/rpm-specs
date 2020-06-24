Name:           perl-Net-CLI-Interact
Version:        2.300003
Release:        5%{?dist}
Summary:        Toolkit for CLI Automation
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-CLI-Interact
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-CLI-Interact-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# ExtUtils::CBuilder not needed on Linux
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Mix)
BuildRequires:  perl(File::ShareDir)
# FileHandle not used at tests
BuildRequires:  perl(IO::Pty)
# IPC::Run not used at tests
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatch::Config)
BuildRequires:  perl(Log::Dispatch::Configurator::Any)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
# Net::Telnet not used at tests
BuildRequires:  perl(Path::Class)
# POSIX not used at tests
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Time::HiRes)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Automating command line interface (CLI) interactions is not a new idea, but
can be tricky to implement. This module aims to provide a simple and
manageable interface to CLI interactions, supporting:

%prep
%setup -q -n Net-CLI-Interact-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.300003-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.300003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.300003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.300003-2
- Perl 5.30 rebuild

* Mon May 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.300003-1
- 2.300003 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.300002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.300002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.300002-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.300002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.300002-1
- 2.300002 bump

* Thu Aug 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.200009-1
- 2.200009 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.200006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.200006-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.200006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.200006-1
- 2.200006 bump

* Tue Jun 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.200005-1
- 2.200005 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.200002-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.200002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Petr Pisar <ppisar@redhat.com> - 2.200002-1
- 2.200002 bump

* Tue Aug 11 2015 Petr Šabata <contyk@redhat.com> - 2.131260-7
- Prevent FTBFS by correcting the build time dependency list
- Trimmed the runtime dep list too; all of them were autodetected

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.131260-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.131260-5
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.131260-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.131260-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.131260-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Simone Caronni <negativo17@gmail.com> 2.131260-1
- Update to 2.131260.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.122100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 03 2012 "Simone Caronni <negativo17@gmail.com>" 1.122100-2
- Regenerated with cpanspec 1.78.
- Added perl module compat.
- Removed duplicate Requires.

* Thu Aug 30 2012 Simone Caronni <negativo17@gmail.com> - 1.122100-1
- First build.
