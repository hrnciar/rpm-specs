Name:           perl-Hash-DefHash
Version:        0.071
Release:        6%{?dist}
Summary:        Manipulate defhash
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Hash-DefHash
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Hash-DefHash-%{version}.tar.gz
BuildArch:      noarch

# Require module version when importing Exporter (#1788170)
Patch0:         Hash-DefHash_exporer.patch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Trim::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(warnings)


Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
DefHash - Define things according to a specification, using hashes.
See the DefHash specification at https://metacpan.org/pod/DefHash.


%prep
%autosetup -p1 -n Hash-DefHash-%{version}


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
%{perl_vendorlib}/*
%{_mandir}/man3/Hash::DefHash*.*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.071-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.071-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.071-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Sandro Mani <manisandro@gmail.com> - 0.071-3
- Improve description
- Constrain Exporter dependency
- BR: perl(blib)

* Tue Jan 07 2020 Sandro Mani <manisandro@gmail.com> - 0.071-2
- Fix / constrain BRs
- Pass NO_PACKLIST=1 to Makefile.PL
- Run fixperms on buildroot

* Mon Jan 06 2020 Sandro Mani <manisandro@gmail.com> - 0.071-1
- Initial package
