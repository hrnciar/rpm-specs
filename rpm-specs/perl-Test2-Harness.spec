Name:           perl-Test2-Harness
%global cpan_version 1.000019
Version:        1.0.19
Release:        1%{?dist}
Summary:        Test2 Harness designed for the Test2 event system
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test2-Harness
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Harness-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID) >= 1.148
BuildRequires:  perl(Devel::Cover)
# Email::Stuffer 0.016 not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path) >= 2.11
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(goto::file) >= 0.005
# HTTP::Tiny 0.070 not used at tests
# HTTP::Tiny::Multipart not used at tests
BuildRequires:  perl(Importer) >= 0.025
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Handle) >= 1.27
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Linux::Inotify2)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Long::Jump) >= 0.000001
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::ANSIColor) >= 4.03
BuildRequires:  perl(Term::Table) >= 0.015
BuildRequires:  perl(Test2::API) >= 1.302170
BuildRequires:  perl(Test2::Event) >= 1.302170
BuildRequires:  perl(Test2::Formatter) >= 1.302170
BuildRequires:  perl(Test2::Hub)
BuildRequires:  perl(Test2::Plugin::IOEvents) >= 0.001001
BuildRequires:  perl(Test2::Plugin::MemUsage) >= 0.002003
BuildRequires:  perl(Test2::Plugin::UUID) >= 0.002001
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Util) >= 1.302170
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::Util::Table)
BuildRequires:  perl(Test2::Util::Term) >= 0.000127
BuildRequires:  perl(Test2::Util::Times)
BuildRequires:  perl(Test::Builder::Formatter) >= 1.302170
BuildRequires:  perl(Time::HiRes)
# Win32::Console::ANSI not used on Linux
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(ok)
BuildRequires:  perl(Test2::Bundle::Extended) >= 0.000127
BuildRequires:  perl(Test2::Tools::AsyncSubtest) >= 0.000127
BuildRequires:  perl(Test2::Tools::GenTemp)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::Tools::Subtest) >= 0.000127
BuildRequires:  perl(Test2::Tools::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000127
BuildRequires:  perl(Test::Builder) >= 1.302170
BuildRequires:  perl(Test::More) >= 1.302170
# Optional tests:
# t2/lib/App/Yath/Plugin/SelfTest.pm tries building a C code using a gcc and
# to run a bash script. But SelfTest.pm itself is never executed.
# bash not used
# gcc not used
# App::Yath::Plugin::Git tries "git" command
Suggests:       git-core
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Suggests:       perl(Cpanel::JSON::XS)
Requires:       perl(Data::Dumper)
Requires:       perl(Data::UUID) >= 1.148
Suggests:       perl(Devel::Cover)
Suggests:       perl(Email::Stuffer) >= 0.016
Requires:       perl(Exporter)
Requires:       perl(File::Find)
Requires:       perl(File::Path) >= 2.11
Suggests:       perl(FindBin)
Requires:       perl(goto::file) >= 0.005
Suggests:       perl(HTTP::Tiny) >= 0.070
Suggests:       perl(HTTP::Tiny::Multipart) >= 0.08
Requires:       perl(Importer) >= 0.025
Requires:       perl(IO::Compress::Bzip2)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::Uncompress::Bunzip2)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Handle) >= 1.27
Suggests:       perl(IO::Pager) >= 1.00
Suggests:       perl(JSON::MaybeXS)
Requires:       perl(JSON::PP)
Suggests:       perl(Linux::Inotify2)
Requires:       perl(Long::Jump) >= 0.000001
Suggests:       perl(Term::ANSIColor) >= 4.03
Requires:       perl(Term::Table) >= 0.015
Requires:       perl(Test2::API) >= 1.302170
Requires:       perl(Test2::Event) >= 1.302170
Requires:       perl(Test2::Formatter) >= 1.302170
Requires:       perl(Test2::Hub)
Requires:       perl(Test2::Plugin::IOEvents) >= 0.001001
Requires:       perl(Test2::Plugin::MemUsage) >= 0.002003
Requires:       perl(Test2::Plugin::UUID) >= 0.002001
Requires:       perl(Test2::Util) >= 1.302170
Requires:       perl(Test2::Util::Term) >= 0.000127
Requires:       perl(Test::Builder::Formatter) >= 1.302170

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::UUID|File::Path|goto::file|Importer|IO::Handle|Long::Jump|Term::Table|Test2::API|Test2::Formatter|Test2::Util|Test2::Util::Term)\\)$

%description
This is a test harness toolkit for Perl Test2 system. It provides a yath tool,
a command-line tool for executing the tests under the Test2 harness.

%prep
%setup -q -n Test2-Harness-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING AUTOMATED_TESTING DBI_PROFILE FAIL_ALWAYS FAIL_ONCE \
    FAILURE_DO_PASS GIT_BRANCH GIT_LONG_SHA GIT_SHORT_SHA GIT_STATUS \
    HARNESS_IS_VERBOSE \
    T2_HARNESS_IS_VERBOSE T2_HARNESS_JOB_IS_TRY T2_HARNESS_STAGE
export T2_HARNESS_JOB_COUNT=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; $j=1 unless $j; print "$j"' -- \
    %{?_smp_mflags})
export HARNESS_OPTIONS=$(perl -e \
    'for (@ARGV) { $j=$1 if m/\A-j(\d+)\z/; }; print "j$j" if $j' -- \
    %{?_smp_mflags})
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/yath
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jun 01 2020 Petr Pisar <ppisar@redhat.com> - 1.0.19-1
- 1.000019 bump

* Tue Apr 14 2020 Petr Pisar <ppisar@redhat.com> - 1.0.18-1
- 1.000018 bump

* Wed Apr 08 2020 Petr Pisar <ppisar@redhat.com> - 1.0.16-1
- 1.000016 bump

* Tue Mar 24 2020 Petr Pisar <ppisar@redhat.com> - 1.0.15-1
- 1.000015 bump

* Mon Mar 23 2020 Petr Pisar <ppisar@redhat.com> - 1.0.14-1
- 1.000014 bump

* Thu Mar 19 2020 Petr Pisar <ppisar@redhat.com> - 1.0.13-1
- 1.000013 bump

* Tue Mar 10 2020 Petr Pisar <ppisar@redhat.com> - 1.0.11-1
- 1.000011 bump

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 1.0.10-1
- 1.000010 bump

* Mon Mar 02 2020 Petr Pisar <ppisar@redhat.com> - 1.0.3-1
- 1.000003 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001099-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Petr Pisar <ppisar@redhat.com> - 0.001099-1
- 0.001099 bump

* Mon Sep 09 2019 Petr Pisar <ppisar@redhat.com> - 0.001097-1
- 0.001097 bump

* Thu Sep 05 2019 Petr Pisar <ppisar@redhat.com> - 0.001095-1
- 0.001095 bump

* Wed Sep 04 2019 Petr Pisar <ppisar@redhat.com> - 0.001093-1
- 0.001093 bump

* Mon Sep 02 2019 Petr Pisar <ppisar@redhat.com> - 0.001091-1
- 0.001091 bump

* Fri Aug 30 2019 Petr Pisar <ppisar@redhat.com> - 0.001088-1
- 0.001088 bump

* Thu Aug 29 2019 Petr Pisar <ppisar@redhat.com> - 0.001086-1
- 0.001086 bump

* Thu Aug 22 2019 Petr Pisar <ppisar@redhat.com> - 0.001085-1
- 0.001085 bump

* Mon Aug 19 2019 Petr Pisar <ppisar@redhat.com> - 0.001084-1
- 0.001084 bump

* Wed Aug 14 2019 Petr Pisar <ppisar@redhat.com> - 0.001081-1
- 0.001081 bump

* Thu Aug 01 2019 Petr Pisar <ppisar@redhat.com> 0.001080-1
- Specfile autogenerated by cpanspec 1.78.
