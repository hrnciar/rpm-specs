Name:           perl-Sentry-Raven
Version:        1.12
Release:        1%{?dist}
Summary:        Perl sentry client
License:        MIT
URL:            https://metacpan.org/pod/Sentry::Raven
Source0:        https://cpan.metacpan.org/authors/id/Q/QR/QRRY/Sentry-Raven-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Sys::Hostname)
# Not available
#BuildRequires:  perl(Test::CPAN::Changes::ReallyStrict)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Perl::Critic) >= 1.03
BuildRequires:  perl(Test::Warn) >= 0.30
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI)
BuildRequires:  perl(UUID::Tiny)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module implements the recommended raven interface for posting events
to a sentry service.

%prep
%setup -q -n Sentry-Raven-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Feb 03 2020 Xavier Bachelot <xavier@bachelot.org> 1.12-1
- Update to 1.12 (RHBZ#1797378).

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Xavier Bachelot <xavier@bachelot.org> 1.11-1
- Update to 1.11 (RHBZ#1725736).

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-4
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Xavier Bachelot <xavier@bachelot.org> 1.10-2
- Specfile fixes following package review.

* Mon Oct 29 2018 Xavier Bachelot <xavier@bachelot.org> 1.10-1
- Initial package.
