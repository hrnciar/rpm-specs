Name:		perl-IO-FDPass
Version:	1.2
Release:	15%{?dist}
Summary:	Pass a file descriptor over a socket
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/IO-FDPass
Source0:	https://cpan.metacpan.org/modules/by-module/IO/IO-FDPass-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Canary::Stability)
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(Socket)
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(XSLoader)

# Avoid provides from private shared objects
%{?perl_default_filter}

%description
This small low-level module only has one purpose: pass a file descriptor to
another process, using a (streaming) UNIX domain socket (on POSIX systems) or
any (streaming) socket (on WIN32 systems). The ability to pass file descriptors
on Windows is currently the unique selling point of this module. Have I
mentioned that it is really small, too?

%prep
%setup -q -n IO-FDPass-%{version}

%build
PERL_CANARY_STABILITY_NOPROMPT=1 perl Makefile.PL \
	INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license COPYING
%else
%doc COPYING
%endif
%doc Changes README
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{_mandir}/man3/IO::FDPass.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Paul Howarth <paul@city-fan.org> - 1.2-12
- Use author-independent source URL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Paul Howarth <paul@city-fan.org> - 1.2-1
- Update to 1.2
  - Compatibility macros were still using C++ syntax, fortunately only
    affecting the Solaris platform

* Thu Sep 22 2016 Paul Howarth <paul@city-fan.org> - 1.1-3
- Incorporate package review feedback (#1378014)
  - Silence rpmlint warning about capitalization of UNIX in %%description
  - Quieten interaction with Canary::Stability during build process

* Wed Sep 21 2016 Paul Howarth <paul@city-fan.org> - 1.1-2
- Sanitize for Fedora submission

* Sat Sep 10 2016 Paul Howarth <paul@city-fan.org> - 1.1-1
- Initial RPM build
