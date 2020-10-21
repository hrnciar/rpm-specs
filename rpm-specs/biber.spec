Name:           biber
Version:        2.14
Release:        4%{?dist}
Summary:        Command-line bibliographic manager, BibTeX replacement
License:        (GPL+ or Artistic 2.0) and Artistic 2.0
URL:            http://biblatex-biber.sourceforge.net/
Source0:        https://github.com/plk/biber/archive/v%{version}.tar.gz
# not appropriate for upstream: http://github.com/plk/biber/pull/97
Patch0:         biber-drop-builddeps-for-monolithic-build.patch
BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(autovivification)
BuildRequires:  perl(base)
BuildRequires:  perl(Business::ISBN)
BuildRequires:  perl(Business::ISMN)
BuildRequires:  perl(Business::ISSN)
BuildRequires:  perl(constant)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Uniqid)
BuildRequires:  perl(Date::Simple)
BuildRequires:  perl(DateTime::Calendar::Julian)
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Encode::EUCJPASCII)
BuildRequires:  perl(Encode::HanExtra)
BuildRequires:  perl(Encode::JIS2K)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Lingua::Translit) >= 0.28
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::MoreUtils::XS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(locale)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Log::Log4perl::Appender::File)
BuildRequires:  perl(Log::Log4perl::Appender::Screen)
BuildRequires:  perl(Log::Log4perl::Layout::PatternLayout)
BuildRequires:  perl(Log::Log4perl::Layout::SimpleLayout)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(open)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(re)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Storable)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(Sort::Key)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::BibTeX) >= 0.85
BuildRequires:  perl(Text::BibTeX::Name)
BuildRequires:  perl(Text::BibTeX::NameFormat)
BuildRequires:  perl(Text::Roman)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(Unicode::LineBreak) >= 2019.001
BuildRequires:  perl(Unicode::Normalize) >= 1.26
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(Unicode::Collate::Locale) >= 1.27
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Simple)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Writer)
# For tests
# Break build cycle biber -> texlive-plain -> texlive-biblatex -> biber
%if !%{defined perl_bootstrap}
BuildRequires:  texlive-plain
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(autovivification)
Requires:       perl(Business::ISBN)
Requires:       perl(Business::ISMN)
Requires:       perl(Business::ISSN)
# Upstream confirmed [1] deps on Encode::* and List::MoreUtils (c.f., [2]).
# [1] https://github.com/plk/biber/issues/98
# [2] https://bugzilla.redhat.com/show_bug.cgi?id=1165620
Requires:       perl(Encode::EUCJPASCII)
Requires:       perl(Encode::HanExtra)
Requires:       perl(Encode::JIS2K)
Requires:       perl(List::MoreUtils)
Requires:       perl(List::MoreUtils::XS)
Requires:       perl(LWP::UserAgent)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Mozilla::CA) >= 20141217
Requires:       perl(PerlIO::utf8_strict)
Requires:       perl(Text::BibTeX) >= 0.88
Requires:       perl(Text::Roman)
Requires:       perl(Unicode::Collate::Locale)
Requires:       perl(XML::LibXSLT)
Requires:       texlive-biblatex >= 7:svn42680
# Biber need a minimum biblatex (src: doc/biber.tex "Compatibility Matrix")
#     biber | texlive-biblatex
#     ------+-----------------
#     1.8   | 2.8a
#     2.1   | 3.0
#     2.6   | 3.5, 3.6
#     2.7   | 3.7       (#1401482)
#     2.8   | 3.8
#     2.9   | 3.9
#     2.10  | 3.10
#     2.11  | 3.11
#     2.12  | 3.12
#     2.13  | 3.13
#     2.14  | 3.14
# (biblatex also has minimum biber requirements)

# filter autogenerated runtime dep, instead use constraint above
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::BibTeX\\)$


%description
Biber is a command-line tool for dealing with bibliographic databases.
Biber offers a large superset of legacy BibTeX (texlive-bibtex)
functionality.  It is often used with the popular BibLaTeX package
(texlive-biblatex), where it is required for some features.


%prep
%setup -q -n biber-%{version}
%patch0 -p1


%build
perl Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
chmod u+w %{buildroot}%{_bindir}/*


%check
%if !%{defined perl_bootstrap}
./Build test verbose=1
%endif


%files
%doc README.md Changes TODO.org
%{_bindir}/%{name}
%{_mandir}/man3/*
%{_mandir}/man1/*
%{perl_vendorlib}/Biber*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-3
- Perl 5.32 re-rebuild of bootstrapped packages

* Wed Jun 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-2
- Perl 5.32 rebuild

* Thu May 14 2020 Tom Callaway <spot@fedoraproject.org> - 2.14-1
- update to 2.14 for TL 2020

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Colin B. Macdonald <cbm@m.fsf.org> - 2.12-1
- Update to 2.12 (bug #1773172)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-5
- Perl 5.30 rebuild

* Tue Feb 12 2019 Petr Pisar <ppisar@redhat.com> - 2.11-4
- Adapt tests to Unicode-Collate-1.27 (bug #1674692)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Colin B. Macdonald <cbm@m.fsf.org> - 2.11-2
- Re-enable tests for e.g., #1512848

* Tue Oct 16 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.11-1
- Update to 2.11

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.7-2
- Perl 5.28 rebuild

* Wed Apr 11 2018 Colin B. Macdonald <cbm@m.fsf.org> - 2.7-1
- Version bump, temporarily disable tests

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-5
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2.6-3
- cherry-pick upstream commit for #1401750.
- more BR.

* Mon Dec 05 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2.6-2
- update biblatex dep, add compatibility table to spec

* Wed Oct 12 2016 Tom Callaway <spot@fedoraproject.org> - 2.6-1
- update to 2.6

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.1-5
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.1-3
- Add another missing BR for tests.

* Sun Dec 20 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.1-2
- cherry-pick from upstream to avoid braces warning.
- enable tests, then patch and cherry-pick so they pass.
- tarball missing two files needed for tests.
- BR on perl(open) for tests.
- patches to enquiet build, fix brace warnings.
- spec formatting fixes.

* Mon Dec 14 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.1-1
- Bump to 2.1, for biblatex-3.0.
- Update deps.
- Add more deps based on upstream confirmation.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-11
- Perl 5.22 rebuild

* Tue Jun 09 2015 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-10
- Add autovivification dep (#1229816).

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-9
- Perl 5.22 rebuild

* Wed May 20 2015 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-8
- Clean up deps as per review.

* Thu Mar 19 2015 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-7
- Upstream thinks ok to relax U::C requirements.

* Wed Dec 3 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-6
- Add Requires, taken from Build.pl.

* Tue Nov 25 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-5
- Use sourceforge for Source0 instead of particular git commit.

* Tue Nov 25 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-4
- lots more BRs, perm fixes.

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-3
- update description and Summary

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-2
- Add dep on (probably overly) specific texlive-biblatex

* Tue Jan 14 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-1
- Bump to 1.8
- perl-File-Slurp-Unicode no longer needed
- add perl-autovivification dep

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> - 1.2-1
- Initial quick-and-dirty package
