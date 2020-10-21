Name:           perl-Net-Facebook-Oauth2
Version:        0.12
Release:        3%{?dist}
Summary:        Simple Perl wrapper around Facebook OAuth 2.0 protocol
License:        GPL+ or Artistic
URL:            https://metacpan.org/pod/Net::Facebook::Oauth2/
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Facebook-Oauth2-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)

Requires:       perl(LWP::Protocol::https)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Net::Facebook::Oauth2 gives you a way to simply access FaceBook Oauth
2.0 protocol.

%prep
%setup -q -n Net-Facebook-Oauth2-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-2
- Perl 5.32 rebuild

* Wed Feb 05 2020 Xavier Bachelot <xavier@bachelot.org> 0.12-1
- Update to 0.12 (RHBZ#1798499).

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Xavier Bachelot <xavier@bachelot.org> 0.11-2
- Fix Source0 URL.
- Add missing BR:s.
- Replace PERL_INSTALL_ROOT with DESTDIR.
- Use %%{?perl_default_filter} macro.

* Thu Nov 07 2019 Xavier Bachelot <xavier@bachelot.org> 0.11-1
- Initial package.
