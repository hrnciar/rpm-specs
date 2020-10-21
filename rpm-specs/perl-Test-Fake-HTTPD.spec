Name:           perl-Test-Fake-HTTPD
Version:        0.09
Release:        1%{?dist}
Summary:        Fake HTTP server module for testing
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Fake-HTTPD

Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASAKI/Test-Fake-HTTPD-%{version}.tar.gz

# Adds SSL key and certification assignment
Patch0:         ssl-parameters-assignment.patch

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Daemon::SSL)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)

# Testing
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork) >= 0.29
BuildRequires:  perl(Test::UseAllModules)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(HTTP::Daemon::SSL)

%description
Test::Fake::HTTPD is a fake HTTP server module for testing.
Written by NAKAGAWA Masaki <masaki@cpan.org>.

%prep
%setup -q -n Test-Fake-HTTPD-%{version}
%patch0 -p0

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_privlib}/*
%{_mandir}/man3/*


%changelog
* Sun Aug 16 2020 Denis Fateyev <denis@fateyev.com> - 0.09-1
- Update to 0.09 release
- Dropped obsolete patch

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-14
- Perl 5.32 re-rebuild updated packages

* Fri Jun 26 2020 Björn Esser <besser82@fedoraproject.org> - 0.08-13
- Perl 5.32 rebuild, again

* Fri Jun 26 2020 Petr Pisar <ppisar@redhat.com> - 0.08-12
- Use 2048-bit RSA testing certificate with SHA-256 (bug #1851243)

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-8
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-2
- Perl 5.26 rebuild

* Tue Mar 07 2017 Denis Fateyev <denis@fateyev.com> - 0.08-1
- Update to 0.08 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.24 rebuild

* Mon Feb 15 2016 Denis Fateyev <denis@fateyev.com> - 0.07-2
- Spec cleanup

* Fri Feb 12 2016 Denis Fateyev <denis@fateyev.com> - 0.07-1
- Initial release
