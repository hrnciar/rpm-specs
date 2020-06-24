Name:           perl-HTML-Selector-XPath
Version:        0.25
Release:        6%{?dist}
Summary:        CSS Selector to XPath compiler
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-Selector-XPath
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/HTML-Selector-XPath-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 1:5.8.1
BuildRequires:  perl-generators

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::More)

BuildRequires:  perl(inc::Module::Install)

# for improved tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(Test::Pod) >= 1.00

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
HTML::Selector::XPath is a utility function to compile CSS2 selector to the
equivalent XPath expression.

%prep
%setup -q -n HTML-Selector-XPath-%{version}
rm -r inc
sed -i -e '/^inc\/.*$/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-1
- Update to 0.25.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-2
- Perl 5.26 rebuild

* Fri Mar 24 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.23-1
- Update to 0.23.
- BR: %%{__make}, %%{__perl}.

* Thu Mar 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.22-1
- Update to 0.22 (RHBZ#1435194).
- Modernize spec.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.20-1
- Upstream update to 0.20.

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-5
- Modernize spec.
- Remove inc/.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-3
- Perl 5.22 rebuild

* Thu Sep 04 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-2
- Perl 5.20 rebuild

* Wed Sep 03 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-1
- Upstream update.

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.16-1
- Upstream update.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.15-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 04 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.15-1
- Upstream update.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.14-2
- Perl 5.16 rebuild

* Wed Jan 18 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.14-1
- Upstream update.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.12-1
- Upstream update.

* Sat Oct 22 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.09-1
- Upstream update.

* Mon Sep 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.08-1
- Upstream update.

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-2
- Perl mass rebuild

* Sun Mar 27 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.07-1
- Upstream update.

* Fri Feb 18 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.06-2
- Fix bogus changelog entry.

* Fri Feb 18 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.06-1
- Upstream update.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.04-1
- Initial Fedora package.
