# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname HTML-Restrict

Summary:        Perl module to strip unwanted HTML tags and attributes
Name:           perl-HTML-Restrict
Version:        3.0.0
Release:        5%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{pkgname}-v%{version}.tar.gz
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo) >= 1.002000
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Type::Tiny) >= 1.002001
BuildRequires:  perl(Types::Standard) >= 1.000001
BuildRequires:  perl(URI)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.22 
BuildArch:      noarch

%description
A perl module that uses HTML::Parser to strip HTML from text in a
restrictive manner. By default all HTML is restricted, but default
behaviour may be altered by supplying own tag rules.

%prep
%setup -q -n %{pkgname}-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

# Don't add dependencies for %%doc
chmod -x examples/*
sed -i -e '1s|#!/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|' examples/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS README.md examples
%{perl_vendorlib}/HTML/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.0-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.0.0-1
- 3.0.0 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.0-2
- Perl 5.30 rebuild

* Thu Feb 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.0-1
- 2.5.0 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.0-2
- Perl 5.28 rebuild

* Sun Apr 01 2018 Robert Scheck <robert@fedoraproject.org> 2.3.0-1
- Upgrade to 2.3.0 (#1562631)
- Initial spec file for Fedora and Red Hat Enterprise Linux
