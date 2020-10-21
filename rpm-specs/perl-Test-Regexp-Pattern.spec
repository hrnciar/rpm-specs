Name:           perl-Test-Regexp-Pattern
Version:        0.006
Release:        6%{?dist}
Summary:        Test Regexp::Pattern patterns
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Test-Regexp-Pattern
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Test-Regexp-Pattern-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long) >= 2.50
BuildRequires:  perl(Hash::DefHash) >= 0.06
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Regexp::Pattern) >= 0.2.7
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)


Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module performs various checks on a module's Regexp::Pattern patterns.


%prep
%autosetup -n Test-Regexp-Pattern-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%license LICENSE
%{_bindir}/test-regexp-pattern
%{perl_vendorlib}/*
%{_mandir}/man1/test-regexp-pattern.1*
%{_mandir}/man3/Test::Regexp::Pattern*.*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Sandro Mani <manisandro@gmail.com> - 0.006-3
- Use NO_PERLLOCAL=1 and %%make_install

* Tue Jan 07 2020 Sandro Mani <manisandro@gmail.com> - 0.006-2
- Fix / constrain BRs
- Pass NO_PACKLIST=1 to Makefile.PL
- Run fixperms on buildroot

* Mon Jan 06 2020 Sandro Mani <manisandro@gmail.com> - 0.006-1
- Initial package
