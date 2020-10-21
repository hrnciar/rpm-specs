Name:		perl-Regexp-Grammars
Version:	1.057
Release:	3%{?dist}
Summary:	Add grammatical parsing features to perl regular expressions
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Regexp-Grammars
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Regexp-Grammars-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-generators
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(B::Hooks::Parser)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Util::TypeConstraints)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%filter_from_provides /perl(Regexp)/d
%filter_provides_in %{_docdir}
%filter_setup


%description
This module adds a small number of new regular expressions constructs that
can be used to implement complete recursive-descent parsing.

These constructs use the grammar patterns that were added to perl's
regular expressions in perl 5.10.

%prep
%setup -q -n Regexp-Grammars-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}

%check
./Build test

%files
%doc Changes README demo/
%{perl_vendorlib}/Regexp/
%{_mandir}/man3/Regexp::Grammars.3pm*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.057-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.057-2
- Perl 5.32 rebuild

* Sun May 24 2020 Bill Pemberton <wfp5p@worldbroken.com> - 1.057-1
- update to 1.057

* Fri May  8 2020 Bill Pemberton <wfp5p@worldbroken.com> - 1.055-1
- update to 1.055
- fixes bug in parsing (??{...}) constructs

* Tue May  5 2020 Bill Pemberton <wfp5p@worldbroken.com> - 1.054-1
- update to 1.054
- Fixed bug in positive lookahead translation

* Mon May  4 2020 Bill Pemberton <wfp5p@worldbroken.com> - 1.053-3
-  <, %, and %% are now never treated as literal.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.052-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.052-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Bill Pemberton <wfp5p@worldbroken.com> - 1.052-1
- update to version 1.052
- fixes bug in <nocontext:> handling

* Wed Jul  3 2019 Bill Pemberton <wfp5p@worldbroken.com> - 1.051-1
- update to version 1.051
- documentation updates

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.050-2
- Perl 5.30 rebuild

* Sat Apr 27 2019 Bill Pemberton <wfp5p@worldbroken.com> - 1.050-1
- update to version 1.050
- Improved detection of explicit space matching in rules
  (now handles \h and \v as well as \s)
- Improved transparency of debugger so that it no longer injects
  spurious whitespace matching after debugged constructs

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.049-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  8 2018 Bill Pemberton <wfp5p@worldbroken.com> - 1.049-1
- update to version 1.049

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.048-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.048-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Bill Pemberton <wfp5p@worldbroken.com> - 1.048-1
- update to version 1.048

* Tue Sep 26 2017 Bill Pemberton <wfp5p@worldbroken.com> - 1.047-1
- update to version 1.047
- Fixes handling of (?>...) construct

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.045-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.045-6
- Rebuild due to bug in RPM (RHBZ #1468476)

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.045-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.045-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.045-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.045-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Bill Pemberton <wfp5p@worldbroken.com> - 1.045-1
- update to version 1.045
- fixes bug causing premature clearing of action handlers

* Mon Dec 21 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.044-1
- update to version 1.044
- attempts to preserve post-5.18 compatibility

* Wed Sep 16 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.042-1
- Update to version 1.042
- now uses B::Hooks::Parser instead of Lexical::Var

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.041-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.041-2
- Perl 5.22 rebuild

* Mon May  4 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.041-1
- Update to version 1.041
- fixes implicit whitespace-matching invalidating subrule argument lists

* Thu Mar 26 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.040-1
- Update to version 1.040
- updates tests

* Sat Feb  7 2015 Bill Pemberton <wfp5p@worldbroken.com> - 1.039-1
- Update to version 1.039

* Thu Dec 11 2014 Bill Pemberton <wfp5p@worldbroken.com> - 1.038-1
- update to version 1.038
- Fixes bug where actions persisted after a failed ->with_actions() match

* Wed Sep 17 2014 Bill Pemberton <wfp5p@worldbroken.com> - 1.036-1
- update to upstream version 1.036
- minor fix to debug behaviour

* Fri Sep 12 2014 Bill Pemberton <wfp5p@worldbroken.com> - 1.035-2
- Bump release to deal with fedpkg problems I'm having

* Fri Sep 12 2014 Bill Pemberton <wfp5p@worldbroken.com> - 1.035-1
- Update to version 1.35
- Returns the module to full functionality with perl >= 5.20

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.033-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep  2 2013 Bill Pemberton <wfp5p@worldbroken.com> - 1.033-1
- update to version 1.33

* Tue Aug 20 2013 Bill Pemberton <wfp5p@viridian.itc.virginia.edu> - 1.031-1
- update to version 1.31
- Updated warnings regarding incompatibilities with perl 5.18

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.030-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.030-2
- Perl 5.18 rebuild

* Fri Jun 28 2013 Bill Pemberton <wfp5p@virginia.edu> - 1.030-1
- update to version 1.030
- includes deprecation message for perl 5.18

* Mon May 13 2013 Bill Pemberton <wfp5p@virginia.edu> - 1.028-1
- update to verison 1.028
- fixes bug where 0 used as an atom
- fixes caching bug within interpolation support

* Mon Feb  4 2013 Bill Pemberton <wfp5p@virginia.edu> - 1.026-1
- update to version 1.026

* Thu Sep 13 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.021-4
- remove explict requires for Data::Dumper and Scalar::Util

* Wed Sep 12 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.021-3
- update Requires and BuildRequires
- remove filter_from_requires
- filter out requirements of the demo scripts
- filter out perl(Regexp) from provides

* Mon Aug 27 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.021-2
- Remove BuildRoot

* Fri Aug 24 2012 Bill Pemberton <wfp5p@virginia.edu> - 1.021-1
- Initial version

