Name:           perl-Regexp-Pattern-License
Version:        3.4.0
Release:        3%{?dist}
Summary:        Regular expressions for legal licenses
License:        GPLv3+

URL:            https://metacpan.org/release/String-Copyright
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASS/Regexp-Pattern-License-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(open)
BuildRequires:  perl(Regexp::Pattern)
BuildRequires:  perl(re::engine::RE2)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Regexp::Pattern)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Regexp::Pattern::License provides a hash of regular expression patterns related
to legal software licenses.


%prep
%autosetup -n Regexp-Pattern-License-v%{version}


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
%{_mandir}/man3/Regexp::Pattern::License*.*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.0-2
- Perl 5.32 rebuild

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Mon May 18 2020 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Mon Apr 06 2020 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Sun Feb 23 2020 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Mon Feb 10 2020 Sandro Mani <manisandro@gmail.com> - 3.1.102-1
- Update to 3.1.102

* Fri Jan 31 2020 Sandro Mani <manisandro@gmail.com> - 3.1.101-1
- Update to 3.1.101

* Tue Jan 28 2020 Sandro Mani <manisandro@gmail.com> - 3.1.100-1
- Update to 3.1.100

* Mon Jan 13 2020 Sandro Mani <manisandro@gmail.com> - 3.1.99-1
- Update to 3.1.99

* Fri Jan 03 2020 Sandro Mani <manisandro@gmail.com> - 3.1.95-1
- Update to 3.1.95

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Sandro Mani <manisandro@gmail.com> - 3.1.94-1
- Update to 3.1.94

* Sun Jun 09 2019 Sandro Mani <manisandro@gmail.com> - 3.1.93-1
- Update to 3.1.93

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.92-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.92-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.1.92-2
- Perl 5.28 rebuild

* Fri Apr 06 2018 Sandro Mani <manisandro@gmail.com> - 3.1.92-1
- Update to 3.1.92

* Thu Apr 05 2018 Sandro Mani <manisandro@gmail.com> - 3.1.91-1
- Update to 3.1.91

* Sat Feb 10 2018 Sandro Mani <manisandro@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Sandro Mani <manisandro@gmail.com> - 3.0.31-1
- Initial package
