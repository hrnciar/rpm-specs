%global use_x11_tests 1
Name:           perl-Gtk3-WebKit
Version:        0.06
Release:        20%{?dist}
Summary:        WebKit bindings for Perl
License:        LGPLv2 or Artistic 2.0
URL:            https://metacpan.org/release/Gtk3-WebKit
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POTYL/Gtk3-WebKit-%{version}.tar.gz
# Use webkit2gtk3, bug #1373410, CPAN RT#122598
Patch0:         Gtk3-WebKit-0.06-Port-to-webkitgtk4.patch
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NeedsDisplay)
BuildRequires:  perl(warnings)
# Typelib for WebKit2-4.0 is provided by webkit2gtk3
BuildRequires:  webkit2gtk3
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# Typelib for WebKit2-4.0 is provided by webkit2gtk3
Requires:       webkit2gtk3

# Do not scan documentation for dependencies
%{?perl_default_filter}

%description
This module provides the Perl bindings for the Gtk3 port of WebKit.

%prep
%setup -q -n Gtk3-WebKit-%{version}
%patch0 -p1

%build
%if %{use_x11_tests}
    xvfb-run %{__perl} Makefile.PL INSTALLDIRS=vendor
%else
    %{__perl} Makefile.PL INSTALLDIRS=vendor
%endif
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{use_x11_tests}
    xvfb-run -a make test
%else
    make test
%endif

%files
%doc Changes COPYING README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-19
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-13
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Petr Pisar <ppisar@redhat.com> - 0.06-11
- webkitgtk4 renamed to webkit2gtk3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Petr Pisar <ppisar@redhat.com> - 0.06-9
- Use webkitgtk4 (bug #1373410)
- Correct dependencies

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 David Dick <ddick@cpan.org> - 0.06-1
- Upgrade to 0.06

* Fri Feb 28 2014 David Dick <ddick@cpan.org> - 0.04-1
- Initial release
