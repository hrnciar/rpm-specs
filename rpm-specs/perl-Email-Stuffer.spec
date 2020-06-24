Name:           perl-Email-Stuffer
Version:        0.017
Release:        8%{?dist}
Summary:        More casual approach to creating and sending emails
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Email-Stuffer
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Stuffer-%{version}.tar.gz
# Adjust to the changes in Email::MIME 1.949, bug #1843862,
# proposed to an upstream <https://github.com/rjbs/Email-Stuffer/issues/54>.
Patch0:         Email-Stuffer-0.017-Allow-un-quoted-name-in-content-type-attribute.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.5.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::MIME) >= 1.943
BuildRequires:  perl(Email::MIME::Creator)
BuildRequires:  perl(Email::Sender::Simple)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::Util) >= 1.05
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Email::Sender::Transport::Test) >= 0.120000
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
# Optional
BuildRequires:  perl(IO::All)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Email::Stuffer is a fairly casual module used to stuff things into an email
and send them. It is a high-level module designed for ease of use when
doing a very specific common task, but implemented on top of the light and
tolerable Email:: modules.

%prep
%setup -q -n Email-Stuffer-%{version}
%patch0 -p1

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 05 2020 Petr Pisar <ppisar@redhat.com> - 0.017-8
- Adjust to the changes in Email::MIME 1.949 (bug #1843862)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-2
- Perl 5.28 rebuild

* Mon Mar 12 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-1
- 0.017 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Petr Pisar <ppisar@redhat.com> - 0.016-1
- 0.016 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-2
- Perl 5.26 rebuild

* Fri Mar 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-1
- Initial release
