# spec file for perl-Gtk2-AppIndicator
#
# Copyright (c) 2014-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries

Name:           perl-Gtk2-AppIndicator
Version:        0.15
Release:        25%{?dist}
Summary:        Perl extension for libappindicator
# COPYRIGHT:    GPL+ or Artistic
# LICENSE:      Artistic text
# README:       GPL+ or Artistic
## Header files exempted from copyright by LGPLv2+
# gperl.h:      LGPLv2+ (bundled from perl-Glib-devel)
# typemap:      LGPLv2+ (bundled from perl-Glib-devel)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Gtk2-AppIndicator
Source0:        https://cpan.metacpan.org/modules/by-module/Gtk2/Gtk2-AppIndicator-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
# ExtUtils::Constant || (File::Copy && File::Spec)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# pkgconf-pkg-config for pkg-config executed from Makefile.PL
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(appindicator-0.1)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Gtk2) >= 1.2
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  font(:lang=en)
BuildRequires:  perl(Test::More)
BuildRequires:  xorg-x11-server-Xvfb
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Gtk2) >= 1.2

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$

%description
This Perl module gives an interface to libappindicator.

%prep
%setup -q -n Gtk2-AppIndicator-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
xvfb-run -d make test

%files
%license LICENSE COPYRIGHT
%doc Changes README
%{perl_vendorarch}/auto/Gtk2
%{perl_vendorarch}/Gtk2
%{_mandir}/man3/Gtk2*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-24
- Perl 5.32 rebuild

* Mon Feb 10 2020 Petr Pisar <ppisar@redhat.com> - 0.15-23
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-20
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-17
- Perl 5.28 rebuild

* Thu Mar 22 2018 Petr Pisar <ppisar@redhat.com> - 0.15-16
- Modernize spec file

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 0.15-15
- missing BR on C compiler

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-6
- Perl 5.22 rebuild

* Sun Jan  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.15-5
- Drop mono_arches as libappindicator, except the mono bindings is built on all arches

* Fri Sep 19 2014 Remi Collet <remi@fedoraproject.org> 0.15-4
- add ExclusiveArch: mono_arches as libappindicator

* Sun Sep  7 2014 Remi Collet <remi@fedoraproject.org> 0.15-2
- fix BR and cleaup from review #1138980

* Sun Sep  7 2014 Remi Collet <remi@fedoraproject.org> 0.15-1
- initial package
