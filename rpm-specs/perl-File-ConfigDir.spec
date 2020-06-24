Name:           perl-File-ConfigDir
Version:        0.021
Release:        8%{?dist}
Summary:        Get directories of configuration files
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-ConfigDir
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-ConfigDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir) >= 0.50
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(parent)
BuildRequires:  perl(vars)
# Recommended:
BuildRequires:  perl(List::MoreUtils) >= 0.419
BuildRequires:  perl(List::MoreUtils::XS) >= 0.418
# Tests:
BuildRequires:  perl(File::Path) >= 2.00
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(local::lib) >= 1.008008
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(Test::Without::Module)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(File::HomeDir) >= 0.50
# Recommended:
Requires:       perl(List::MoreUtils) >= 0.419
# Suggests:
Suggests:       perl(local::lib) >= 1.008008

%description
This module is a helper for installing, reading and finding configuration
file locations. It's intended to work in every supported Perl5 environment
and will always try to Do The Right Thing(TM).

%prep
%setup -q -n File-ConfigDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.021-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-2
- Perl 5.28 rebuild

* Wed May 02 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-1
- 0.021 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.018-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.018-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.018-2
- Perl 5.26 rebuild

* Tue May 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.018-1
- 0.018 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-2
- Perl 5.22 rebuild

* Thu Jun 11 2015 Petr Pisar <ppisar@redhat.com> - 0.017-1
- 0.017 bump

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-2
- Perl 5.22 rebuild

* Sat Jan 17 2015 David Dick <ddick@cpan.org> - 0.015-1
- replace README by README.md

* Sat Nov 22 2014 David Dick <ddick@cpan.org> - 0.014-1
- Fix typo in pod, update README

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-2
- Perl 5.20 rebuild

* Wed Jul 23 2014 David Dick <ddick@cpan.org> - 0.013-1
- Initial release
