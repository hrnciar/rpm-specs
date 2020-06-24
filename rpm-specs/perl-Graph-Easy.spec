Name:           perl-Graph-Easy
Version:        0.76
Release:        12%{?dist}
Summary:        Convert or render graphs as ASCII, HTML, SVG or via Graphviz
License:        GPLv2+ and ASL 1.1
URL:            https://metacpan.org/release/Graph-Easy
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Graph-Easy-%{version}.tar.gz
Patch0:         graph-easy-undefined-lc.patch
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 0:5.008002
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)

# avoid circular dependencies
%bcond_without bootstrap
%if %{without bootstrap}
BuildRequires:  perl(Graph::Easy::As_svg) >= 0.23
Requires:       perl(Graph::Easy::As_svg) >= 0.23
%endif

# filter unversioned provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Graph::Easy\\)$
%global __provides_exclude %__provides_exclude|perl\\(Graph::Easy::(Edge|Edge::Cell|Group|Node)\\)$

%description
Graph::Easy lets you generate graphs consisting of various shaped nodes
connected by edges (with optional labels). It can read and write graphs in a
variety of formats, as well as render them via its own grid-based layouter.
Since the layouter works on a grid (manhattan layout), the output is most
useful for flow charts, network diagrams, or hierarchy trees.

%prep
%setup -q -n Graph-Easy-%{version}
%patch0 -p 1

chmod 0644 examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES LICENSE README TODO examples
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 06 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.76-1
- 0.76 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-2
- Perl 5.22 rebuild

* Wed Nov 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.75-1
- 0.75 bump; Update BRs

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.73-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.73-2
- Perl 5.18 rebuild

* Fri Jun 07 2013 Iain Arnell <iarnell@gmail.com> 0.73-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 20 2012 Iain Arnell <iarnell@gmail.com> 0.72-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.71-2
- Perl 5.16 rebuild

* Fri Jan 06 2012 Iain Arnell <iarnell@gmail.com> 0.71-1
- update to latest upstream version
- update filtering for rpm 4.9

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.70-2
- Perl mass rebuild

* Sun Apr 24 2011 Iain Arnell <iarnell@gmail.com> 0.70-1
- Specfile autogenerated by cpanspec 1.79.
