Name:           perl-Cookie-Baker
Version:        0.11
Release:        4%{?dist}
Summary:        Cookie string generator / parser
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Cookie-Baker
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cookie-Baker-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}

BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Time)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Cookie::Baker provides simple cookie string generator and parser.

%prep
%setup -q -n Cookie-Baker-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-4
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019  Ralf Corsépius <corsepiu@fedoraproject.org> - 0.11-1
- Update to 0.11.

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018  Ralf Corsépius <corsepiu@fedoraproject.org> - 0.10-1
- Update to 0.10.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.28 rebuild

* Sun Mar 04 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.09-1
- Update to 0.09.
- Spec file cosmetics.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.08-1
- Update to 0.08.
- Reflect upstream having switched to Module::Build::Tiny.

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 01 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.07-1
- Update to 0.07.

* Wed Jun 01 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.06-1
- Update to 0.06.
- Modernize spec.

* Mon Jun 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.05-1
- Initial package.
