Name:           perl-Export-Attrs
Version:        0.1.0
Release:        10%{?dist}
Summary:        The Perl 6 'is export(...)' trait as a Perl 5 attribute
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Export-Attrs
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POWERMAN/Export-Attrs-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module is a fork of Perl6::Export::Attrs created to restore
compatibility with Perl6::Export::Attrs version 0.0.3.

%prep
%setup -q -n Export-Attrs-v%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
AUTHOR_TESTING=1 RELEASE_TESTING=1 ./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Export*
%{_mandir}/man3/Export*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.0-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.0-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.0-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 24 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.1.0-2
- Take into account review feedback (#1517099)

* Fri Nov 24 2017 Emmanuel Seyman <emmanuel@seyman.fr> 0.1.0-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
