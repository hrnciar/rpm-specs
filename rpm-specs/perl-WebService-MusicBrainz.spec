%global debug_package %{nil}

Name:           perl-WebService-MusicBrainz
Version:        1.0.5
Release:        6%{?dist}
Summary:        Perl interface to search the musicbrainz.org database
License:        Artistic 2.0 or GPL+
URL:            https://metacpan.org/release/WebService-MusicBrainz
Source0:        https://cpan.metacpan.org/authors/id/B/BF/BFAIST/WebService-MusicBrainz-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-Mojolicious
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       pkgconf-pkg-config

%{?perl_default_filter}

%description
This module will search the MusicBrainz database through their web service and
return objects with the found data.

%prep
%setup -q -n WebService-MusicBrainz-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?_with_testsuite:make test}

%files
%doc Changes README.md
%{_mandir}/man3/WebService::MusicBrainz*.3pm*
%perl_vendorlib/WebService

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.5-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.5-3
- Description change, files changes rhbz#1758929

* Mon Oct 07 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.5-2
- BuildArch noarch, License Artistic 2.0 or GPL+ rhbz#1758929

* Sun Oct 06 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.5-1
- Initial build rhbz#1758929
