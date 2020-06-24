Name:           perl-Dist-Zilla-Plugin-GithubMeta
Version:        0.58
Release:        9%{?dist}
Summary:        Automatically include GitHub meta information in META.yml
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-GithubMeta
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Dist-Zilla-Plugin-GithubMeta-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types::URI)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
Dist::Zilla::Plugin::GithubMeta is a Dist::Zilla plugin to include
GitHub meta information in META.yml.  It automatically detects if the
distribution directory is under git version control and whether the
origin is a GitHub repository and will set the repository and homepage
meta in META.yml to the appropriate URLs for GitHub.

%prep
%setup -q -n Dist-Zilla-Plugin-GithubMeta-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-9
- Perl 5.32 rebuild

* Fri Mar 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-8
- Add perl(blib) for tests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.58-2
- Perl 5.28 rebuild

* Mon Jun 04 2018 Petr Šabata <contyk@redhat.com> - 0.58-1
- 0.58 bump

* Mon May 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-1
- 0.56 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 08 2015 Petr Šabata <contyk@redhat.com> - 0.54-1
- 0.54 bump

* Sun Jun 21 2015 Petr Šabata <contyk@redhat.com> - 0.52-1
- 0.52 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-2
- Perl 5.22 rebuild

* Fri May 15 2015 Petr Šabata <contyk@redhat.com> 0.50-1
- Initial packaging
