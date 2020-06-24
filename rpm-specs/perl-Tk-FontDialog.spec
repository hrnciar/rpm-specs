%global use_x11_tests 1

Name:           perl-Tk-FontDialog
Version:        0.18
Release:        10%{?dist}
Summary:        Font dialog widget for perl/Tk
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Tk-FontDialog
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-FontDialog-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(strict)
BuildRequires:  perl(Tk) >= 800
BuildRequires:  perl(Tk::Font)
BuildRequires:  perl(Tk::HList)
BuildRequires:  perl(Tk::ItemStyle)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(charnames)
BuildRequires:  perl(Test::More)
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Tk::HList)
Requires:       perl(Tk::ItemStyle)

%description
This module implements a font dialog widget for perl/Tk.

%prep
%setup -q -n Tk-FontDialog-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{use_x11_tests}
    xvfb-run -d make test
%else
    make test
%endif

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-8
- Perl 5.30 rebuild

* Wed May 15 2019 Petr Pisar <ppisar@redhat.com> - 0.18-7
- Modernize spec file

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-1
- Initial release
