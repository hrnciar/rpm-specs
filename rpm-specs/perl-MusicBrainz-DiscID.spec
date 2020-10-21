# Tests require network access

Name:           perl-MusicBrainz-DiscID
Version:        0.06
Release:        4%{?dist}
Summary:        Perl interface for the MusicBrainz libdiscid library
License:        MIT
URL:            https://metacpan.org/release/MusicBrainz-DiscID
Source0:        https://cpan.metacpan.org/authors/id/N/NJ/NJH/MusicBrainz-DiscID-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libdiscid-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
MusicBrainz::DiscID is a class to calculate a MusicBrainz DiscID from an
audio CD in the drive. The coding style is slightly different to the C
interface to libdiscid, because it makes use of perl's Object Oriented
functionality.

%prep
%setup -q -n MusicBrainz-DiscID-%{version}
chmod -c a-x examples/*.pl

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
%doc Changes README*
%{perl_vendorarch}/MusicBrainz*
%{perl_vendorarch}/auto/MusicBrainz/
%{_mandir}/man3/*.3pm*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Gerald Cox <gbcox@fedoraproject.org> - 0.06-1
- Change License to MIT per upstream request rhbz#1758925

* Mon Oct 07 2019 Gerald Cox <gbcox@fedoraproject.org> - 0.04-2
- License GPLv2+, tests require internet rhbz#1758925

* Sun Oct 06 2019 Gerald Cox <gbcox@fedoraproject.org> - 0.04-1
- Initial build rhbz#1758925
