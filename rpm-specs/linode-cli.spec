Name:           linode-cli
Version:        1.4.5
Release:        17%{?dist}
Summary:        Official command-line interface to the Linode platform
License:        Artistic or GPLv2
URL:            https://github.com/linode/cli/
Source0:        https://github.com/linode/cli/archive/v%{version}.tar.gz#/cli-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
BuildRequires:  perl(WebService::Linode)
Requires:       perl(WebService::Linode)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Linode CLI is a simple command-line interface to the Linode platform.

%prep
%setup -qn cli-%{version}
rm -frv lib/WebService*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1

%install
%make_install
chmod -v 755 %{buildroot}%{_bindir}/linode*

%files
%doc Changes LICENSE README.md
%{_bindir}/linode*
%{perl_vendorlib}/*
%{_mandir}/man1/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.5-16
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.5-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.5-10
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.5-7
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.5-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.5-2
- Perl 5.22 rebuild

* Sun Jan 25 2015 Christopher Meng <rpm@cicku.me> - 1.4.5-1
- Update to 1.4.5

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.2-3
- Perl 5.20 rebuild

* Thu Jul 31 2014 Christopher Meng <rpm@cicku.me> - 1.3.2-2
- Fix binaries perms to 755
- Add missing BRs.

* Wed May 21 2014 Christopher Meng <rpm@cicku.me> - 1.3.2-1
- Update to 1.3.2

* Tue Jan 28 2014 Christopher Meng <rpm@cicku.me> - 1.0.0-1
- Initial Package.
