Name:           perl-Plack-Middleware-RemoveRedundantBody
Version:        0.09
Release:        3%{?dist}
Summary:        Plack::Middleware which sets removes body for HTTP response if it's not required
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Plack-Middleware-RemoveRedundantBody
Source0:        https://cpan.metacpan.org/modules/by-module/Plack/Plack-Middleware-RemoveRedundantBody-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Util)
# Tests
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module removes body in HTTP response, if it's not required.

%prep
%setup -q -n Plack-Middleware-RemoveRedundantBody-%{version}

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
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-1
- 0.09 bump

* Mon Jul 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-1
- 0.08 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-2
- Perl 5.28 rebuild

* Fri Mar 02 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-1
- 0.07 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-1
- 0.06 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-2
- Perl 5.22 rebuild

* Sat Nov 22 2014 David Dick <ddick@cpan.org> - 0.05-1
- Initial release
