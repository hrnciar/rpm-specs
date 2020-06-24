Name:           perl-Mojolicious-Plugin-OAuth2
Version:        1.58
Release:        2%{?dist}
Summary:        A Mojolicious plugin that allows OAuth2 authentication

License:        Artistic 2.0
URL:            https://metacpan.org/release/Mojolicious-Plugin-OAuth2
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/Mojolicious-Plugin-OAuth2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious) >= 7.53
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Mojolicious::Plugin)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:  perl(IO::Socket::SSL)
Requires:  perl(Mojolicious) >= 7.53
Requires:  perl(Mojolicious::Plugin)

%{?perl_default_filter}

%description
This Mojolicious plugin allows you to easily authenticate against a OAuth2
provider. It includes configurations for a few popular providers, but you can
add your own easily as well.

%prep
%setup -q -n Mojolicious-Plugin-OAuth2-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.58-1
- Update to 1.58

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Mike Oliver <mike@mklvr.io> - 1.57-1
- Initial package creation
