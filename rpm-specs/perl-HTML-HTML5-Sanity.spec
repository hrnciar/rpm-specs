Name:           perl-HTML-HTML5-Sanity
Version:        0.105
Release:        5%{?dist}
Summary:        Make HTML5 DOM trees less insane
# CONTRIBUTING: CC-BY-SA
# COPYRIGHT:    Public Domain
# LICENSE:      GPL+ or Artistic
License:        (GPL+ or Artistic) and CC-BY-SA and Public Domain
URL:            https://metacpan.org/release/HTML-HTML5-Sanity
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/HTML-HTML5-Sanity-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Locale::Country)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.70
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
BuildRequires:  perl(XML::LibXML::Debugging)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(XML::LibXML) >= 1.70

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::LibXML\\)$

%description
The Document Object Model (DOM) generated by HTML::HTML5::Parser meets the
requirements of the HTML5 specification, but will probably catch a lot of
people by surprise. This Perl module returns the DOM with corrected xml:lang
attributes.

%prep
%setup -q -n HTML-HTML5-Sanity-%{version}

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
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.105-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.105-2
- Perl 5.30 rebuild

* Fri Apr 26 2019 Petr Pisar <ppisar@redhat.com> 0.105-1
- Specfile autogenerated by cpanspec 1.78.
