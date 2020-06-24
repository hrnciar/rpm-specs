Name:           perl-System-Command
Version:        1.121
Release:        2%{?dist}
Summary:        Object for running system commands
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/System-Command
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/System-Command-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
# IPC::Run not used on Linux
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::Command)
# Test::CPAN::Meta not used
BuildRequires:  perl(Test::Output)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Data::Dumper)
Requires:       perl(IO::Select)

# IPC::Run not used on Linux
%global __requires_exclude ^perl\\(IPC::Run\\)

%description
System::Command is a class that launches external system commands and
return an object representing them, allowing to interact with them through
their STDIN, STDOUT and STDERR handles.

%prep
%setup -q -n System-Command-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.121-2
- Perl 5.32 rebuild

* Thu Jun 04 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.121-1
- 1.121 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.119-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-2
- Perl 5.28 rebuild

* Tue Apr 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.119-1
- 1.119 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.118-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.118-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.118-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.118-1
- 1.118 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.117-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Petr Šabata <contyk@redhat.com> - 1.117-1
- 1.117 bump

* Fri Jan 08 2016 Petr Šabata <contyk@redhat.com> - 1.116-1
- 1.116 bump

* Tue Sep 29 2015 Petr Šabata <contyk@redhat.com> - 1.115-1
- 1.115 bump, test suite and docs enhancements

* Thu Sep 24 2015 Petr Šabata <contyk@redhat.com> - 1.114-1
- 1.114 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.111-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.111-2
- Perl 5.22 rebuild

* Tue Feb 17 2015 Petr Šabata <contyk@redhat.com> - 1.111-1
- 1.111 bump

* Fri Nov 14 2014 Petr Pisar <ppisar@redhat.com> - 1.110-1
- 1.110 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.100-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 1.100-2
- Perl 5.18 rebuild

* Fri Jun 21 2013 Iain Arnell <iarnell@gmail.com> 1.100-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Iain Arnell <iarnell@gmail.com> 1.09-1
- upddate to latest upstream version

* Fri Dec 07 2012 Iain Arnell <iarnell@gmail.com> 1.08-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.07-2
- Perl 5.16 rebuild

* Fri Apr 20 2012 Iain Arnell <iarnell@gmail.com> 1.07-1
- update to latest upstream version

* Fri Jan 13 2012 Iain Arnell <iarnell@gmail.com> 1.06-1
- Specfile autogenerated by cpanspec 1.78.
