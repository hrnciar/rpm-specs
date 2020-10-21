Name:           perl-Mango
Version:        1.30
Release:        10%{?dist}
Summary:        Pure-Perl non-blocking I/O MongoDB driver
License:        Artistic 2.0
URL:            https://metacpan.org/release/Mango
Source0:        https://cpan.metacpan.org/authors/id/O/OD/ODC/Mango-%{version}.tar.gz
# Adjust to the changes in Mojolicious 8.50, bug #1843866,
# proposed to an upstream <https://github.com/oliwer/mango/issues/36>
Patch0:         Mango-1.30-Disable-unicode_strings-when-working-with-regular-ex.patch
BuildArch:      noarch
BuildRequires:  make
# This code is architecture-independent, but it requires at least 64-bit
# integers and these are not available on 32-bit architectures if perl is
# built without use64bitint option. We enabled use64bitint in 4:5.26.0-392.
BuildRequires:  perl-libs >= 4:5.26.0-392
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Authen::SCRAM::Client not used at tests
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Date)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
# Mojolicious version from META because this is the only versioned module in
# perl-Mojolicious RPM package
BuildRequires:  perl(Mojolicious) >= 5.40
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Mojo::IOLoop::Server)
BuildRequires:  perl(Test::More)
# Optional tests:
# Test::Pod 1.14 not used
# Test::Pod::Coverage 1.04 not used
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Authen::SCRAM::Client)
Requires:       perl(Mojo::EventEmitter)
# Mojolicious version from META because this is the only versioned module in
# perl-Mojolicious RPM package
Requires:       perl(Mojolicious) >= 5.40
# This code is architecture-independent, but it requires at least 64-bit
# integers and these are not available on 32-bit architectures if perl is
# built without use64bitint option. We enabled use64bitint in 4:5.26.0-392.
Requires:       perl-libs >= 4:5.26.0-392

%description
Mango is a pure-Perl non-blocking I/O MongoDB driver, optimized for use
with the Mojolicious real-time web framework, and with multiple event loop
support. Since MongoDB is still changing rapidly, only the latest stable
version is supported.

%prep
%setup -q -n Mango-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TEST_ONLINE TEST_POD
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-9
- Perl 5.32 rebuild

* Fri Jun 05 2020 Petr Pisar <ppisar@redhat.com> - 1.30-8
- Adjust to the changes in Mojolicious 8.50 (bug #1843866)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-2
- Perl 5.28 rebuild

* Mon Mar 19 2018 Petr Pisar <ppisar@redhat.com> - 1.30-1
- 1.30 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Petr Pisar <ppisar@redhat.com> - 1.29-3
- Enable building on 32-bit platforms since perl is built with use64bitint

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.29-2
- Perl 5.26 rebuild

* Fri Mar 10 2017 Petr Pisar <ppisar@redhat.com> 1.29-1
- Specfile autogenerated by cpanspec 1.78.
