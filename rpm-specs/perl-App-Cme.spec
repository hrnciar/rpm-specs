Name:           perl-App-Cme
Version:        1.031
Release:        2%{?dist}
Summary:        Check or edit configuration data with Config::Model
License:        LGPLv2+
URL:            https://metacpan.org/release/App-Cme
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/App-Cme-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.34
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(App::Cmd::Setup)
BuildRequires:  perl(base)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Config::Model) >= 2.124
# Config::Model::CursesUI - not used at test
# Config::Model::FuseUI - Fuse is not packaged yet
BuildRequires:  perl(Config::Model::Lister)
BuildRequires:  perl(Config::Model::ObjTreeScanner)
# Config::Model::SimpleUI - not used at test
# Config::Model::TermUI - not used at test
# Config::Model::TkUI - not used at test
# Config::Model::Utils::GenClassPod - not used at test
# Data::Dumper - not used at test
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::HomeDir)
# JSON - not used at test
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(open)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Hash)
# Tk - not used at test
# Tk::ErrorDialog - not used at test
BuildRequires:  perl(utf8)
BuildRequires:  perl(YAML)
# Tests
BuildRequires:  perl(App::Cmd::Tester)
BuildRequires:  perl(Probe::Perl)
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Config::Model::CursesUI)
Requires:       perl(Config::Model::FuseUI)
Requires:       perl(Config::Model::SimpleUI)
Requires:       perl(Config::Model::TermUI)
Requires:       perl(Config::Model::TkUI)
Requires:       perl(Tk)
Requires:       perl(Tk::ErrorDialog)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Config::Model\\)\s*$

%description
cme and Config::Model are quite modular. The configuration data that you
can edit depend on the other Config::Model distributions installed on your
system.

%prep
%setup -q -n App-Cme-%{version}
sed -i -e '1s|#!/usr/bin/env perl|#!perl|' bin/cme

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

# Install bash_completion script
install -D -m 0644 contrib/bash_completion.cme %{buildroot}%{_sysconfdir}/bash_completion.d/cme

%check
./Build test

%files
%license LICENSE
%doc Changes README.pod
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_sysconfdir}/bash_completion.d

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.031-1
- 1.031 bump

* Thu Sep 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.030-1
- 1.030 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.029-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.029-4
- Perl 5.30 re-rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.029-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.029-1
- 1.029 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.028-2
- Perl 5.28 rebuild

* Thu Jun 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.028-1
- 1.028 bump

* Mon Apr 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.027-1
- 1.027 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.026-1
- 1.026 bump

* Fri Dec 15 2017 Petr Pisar <ppisar@redhat.com> - 1.025-1
- 1.025 bump

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.024-1
- 1.024 bump

* Mon Sep 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-1
- 1.023 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-1
- 1.022 bump

* Mon Jun 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.021-1
- 1.021 bump

* Mon Jun 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.020-1
- 1.020 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-3
- Perl 5.26 rebuild

* Thu May 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-2
- Add BR: perl(YAML)

* Tue May 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-1
- 1.019 bump

* Mon Apr 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.018-1
- 1.018 bump

* Mon Mar 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.017-1
- 1.017 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.016-1
- 1.016 bump

* Mon Oct 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.015-1
- 1.015 bump

* Thu Sep 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.014-1
- 1.014 bump

* Mon Jul 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.013-1
- 1.013 bump

* Wed Jun 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-1
- 1.012 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-2
- Perl 5.24 rebuild

* Fri Apr 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-1
- 1.011 bump

* Wed Feb 10 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-1
- 1.010 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-2
- Updated due review comments

* Mon Jan 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-1
- Initial release
