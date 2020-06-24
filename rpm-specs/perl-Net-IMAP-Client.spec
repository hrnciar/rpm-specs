Name:           perl-Net-IMAP-Client
Version:        0.9505
Release:        6%{?dist}
Summary:        IMAP client library for Perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-IMAP-Client
Source0:        http://www.cpan.org/authors/id/G/GA/GANGLION/Net-IMAP-Client-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(vars)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(overload)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::MIME::Header)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Net::IMAP::Client provides methods to access an IMAP server. It aims to
provide a simple and clean API, while employing a rigorous parser for IMAP
responses in order to create Perl data structures from them. The code is
simple, clean and extensible.


%prep
%setup -q -n Net-IMAP-Client-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}


%check
make test


%files
%{perl_vendorlib}/*
%{_mandir}/man3/*
%doc Changes META.json README
%exclude %{perl_vendorarch}/auto/Net/IMAP/Client/.packlist


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.9505-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9505-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9505-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.9505-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9505-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.9505-1
- Initial packaging, based on cpanspec 1.78
