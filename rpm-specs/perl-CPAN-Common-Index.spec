Name:           perl-CPAN-Common-Index
Version:        0.010
Release:        10%{?dist}
Summary:        Common library for searching CPAN modules, authors and distributions
License:        ASL 2.0
URL:            https://metacpan.org/release/CPAN-Common-Index
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Common-Index-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(parent)
BuildRequires:  perl(Search::Dict) >= 1.07
BuildRequires:  perl(Tie::Handle::SkipHeader)
BuildRequires:  perl(URI)
# Optional run-time:
BuildRequires:  perl(IO::Uncompress::Gunzip)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Recommends:     perl(IO::Uncompress::Gunzip)

%description
This module provides a common library for working with a variety of CPAN
index services. It is intentionally minimalist, trying to use as few non-
core modules as possible.

%prep
%setup -q -n CPAN-Common-Index-%{version}

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
%doc Changes CONTRIBUTING.mkdn README Todo examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-10
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Petr Pisar <ppisar@redhat.com> - 0.010-2
- Rebuild to overcome race with F27 mass rebuild side tag

* Thu Jul 27 2017 Petr Pisar <ppisar@redhat.com> - 0.010-1
- 0.010 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-2
- Perl 5.26 rebuild

* Fri May 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.007-1
- 0.007 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Petr Šabata <contyk@redhat.com> 0.006-1
- Initial packaging
