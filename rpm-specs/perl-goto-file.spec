Name:           perl-goto-file
Version:        0.005
Release:        4%{?dist}
Summary:        Stop parsing the current file and move on to a different one
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/goto-file
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/goto-file-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Filter::Util::Call)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(ok)
# Test2::IPC version from Test2 in META
BuildRequires:  perl(Test2::IPC) >= 1.302095
BuildRequires:  perl(Test2::Require::RealFork)
BuildRequires:  perl(Test2::V0) >= 0.000074
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
It is rare, but there are times where you want to swap out the currently
compiling file for a different one. This Perl module does that. From the point
you use the module perl will be parsing the new file instead of the original.

%prep
%setup -q -n goto-file-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Petr Pisar <ppisar@redhat.com> 0.005-1
- Specfile autogenerated by cpanspec 1.78.
