%global pkgname CPANPLUS-Dist-Fedora

Name:           perl-CPANPLUS-Dist-Fedora
Version:        0.2.2
Release:        3%{?dist}
Summary:        CPANPLUS backend to build Fedora/RedHat RPMs
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CPANPLUS-Dist-Fedora
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(CPANPLUS::Dist::Base)
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Template)
BuildRequires:  perl(Text::Wrap)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This is a distribution class to create Fedora packages from CPAN modules, 
and all its dependencies. This allows you to have the most recent copies of 
CPAN modules installed, using your package manager of choice, but without 
having to wait for central repositories to be updated.

%prep
%setup -qn %{pkgname}-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.2-2
- Perl 5.32 rebuild

* Wed Jan 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.2-2
- 0.2.2 bump

* Mon Aug 26 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-1
- 0.2.1 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.0-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 0.2.0-2
- Perl 5.28 rebuild

* Mon Jul 02 2018 Petr Pisar <ppisar@redhat.com> - 0.2.0-1
- 0.2.0 bump

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.10-2
- Perl 5.28 rebuild

* Thu May 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.10-1
- 0.0.10 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.9-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.9-2
- Perl 5.24 rebuild

* Mon Feb 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.9-1
- 0.0.9 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Petr Pisar <ppisar@redhat.com> - 0.0.6-1
- 0.0.6 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.4-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.4-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 0.0.4-1
- Initial Package.
