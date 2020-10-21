Name:           perl-Redis
Version:        1.998
Release:        1%{?dist}
Summary:        Perl binding for Redis database
License:        ASL 2.0
URL:            https://metacpan.org/release/Redis
Source0:        https://cpan.metacpan.org/modules/by-module/Redis/Redis-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
# Module
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::Timeout) >= 0.29
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP) >= 1.19
BuildRequires:  redis
# Author Tests (not run)
%if 0
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
# Release Tests
BuildRequires:  perl(Test::CPAN::Meta)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(IO::Socket::Timeout) >= 0.29
Requires:       perl(Time::HiRes)

%description
Pure perl bindings for http://redis.io/

%prep
%setup -q -n Redis-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG REDIS_DEBUG REDIS_SERVER REDIS_SERVER_PATH
RELEASE_TESTING=1 ./Build test

%files
%license LICENSE
%doc Changes README scripts/ tools/
%{perl_vendorlib}/Redis.pm
%{perl_vendorlib}/Redis/
%{_mandir}/man3/Redis.3*
%{_mandir}/man3/Redis::Hash.3*
%{_mandir}/man3/Redis::List.3*
%{_mandir}/man3/Redis::Sentinel.3*

%changelog
* Tue Aug 18 2020 Petr Pisar <ppisar@redhat.com> - 1.998-1
- 1.998 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.996-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.996-3
- Perl 5.32 rebuild

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.996-2
- Add missing BR

* Fri Mar 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.996-1
- 1.996 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.995-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Paul Howarth <paul@city-fan.org> - 1.995-3
- Spec tidy-up
  - Switch to upstream's preferred flow, using Module::Build::Tiny
  - Classify buildreqs by usage
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.995-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.995-1
- 1.995 bump

* Mon Jul 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.994-1
- 1.994 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.991-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.991-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Petr Pisar <ppisar@redhat.com> - 1.991-8
- Adjust tests to changes in Redis 4.0.11 (bug #1624360)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.991-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.991-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.991-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.991-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.991-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.991-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.991-1
- 1.991 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.982-2
- Perl 5.24 rebuild

* Wed Mar 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.982-1
- 1.982 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.981-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.981-1
- 1.981 bump

* Fri Jul 17 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.979-1
- 1.979 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.978-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.978-2
- Perl 5.22 rebuild

* Sun Feb 01 2015 David Dick <ddick@cpan.org> - 1.978-1
- Upgrade to 1.978.

* Thu Oct 09 2014 David Dick <ddick@cpan.org> - 1.976-1
- Upgrade to 1.976.

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.975-2
- Perl 5.20 rebuild

* Tue Aug 05 2014 David Dick <ddick@cpan.org> - 1.975-1
- Upgrade to 1.975.  Include patched fixes from previous version, documentation clarifications

* Fri May 16 2014 David Dick <ddick@cpan.org> - 1.974-1
- Initial release
