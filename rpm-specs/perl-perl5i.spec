Name:		perl-perl5i
Summary:	Fix as much of Perl 5 as possible in one pragma
Version:	2.13.2
Release:	14%{?dist}
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/perl5i
Source0:	http://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/perl5i-v%{version}.tar.gz
Patch0:		perl5i-v2.13.2-coercion.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter >= 4:5.10.0
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::Build) >= 0.36
# Module Runtime
BuildRequires:	perl(:VERSION) >= 5.10.0
BuildRequires:	perl(CLASS) >= 1.00
BuildRequires:	perl(Capture::Tiny) >= 0.06
BuildRequires:	perl(Carp)
BuildRequires:	perl(Carp::Fix::1_25) >= 1.000000
BuildRequires:	perl(Child) >= 0.009
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(DateTime) >= 0.47
BuildRequires:	perl(DateTime::Format::Epoch) >= 0.11
BuildRequires:	perl(DateTime::TimeZone::Tzfile) >= 0.002
BuildRequires:	perl(Devel::Declare::MethodInstaller::Simple) >= 0.006009
BuildRequires:	perl(Digest::MD5) >= 2.36
BuildRequires:	perl(Digest::SHA) >= 5.45
BuildRequires:	perl(Encode)
BuildRequires:	perl(English)
BuildRequires:	perl(File::chdir) >= 0.1002
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Hash::FieldHash) >= 0.06
BuildRequires:	perl(Hash::Merge::Simple) >= 0.04
BuildRequires:	perl(Hash::StoredIterator) >= 0.007
BuildRequires:	perl(Import::Into) >= 1.002003
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::System::Simple) >= 1.18
BuildRequires:	perl(JSON::MaybeXS) >= 1.003005
BuildRequires:	perl(List::MoreUtils) >= 0.22
BuildRequires:	perl(Modern::Perl) >= 1.03
BuildRequires:	perl(Module::Load) >= 0.16
BuildRequires:	perl(Object::ID) >= v0.1.0
BuildRequires:	perl(Path::Tiny) >= 0.036
BuildRequires:	perl(Perl6::Caller) >= 0.100
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Taint::Util) >= 0.06
BuildRequires:	perl(Text::Wrap) >= 2009.0305
BuildRequires:	perl(Time::y2038)
BuildRequires:	perl(Try::Tiny) >= 0.02
BuildRequires:	perl(Want) >= 0.18
BuildRequires:	perl(YAML::Any) >= 0.70
BuildRequires:	perl(autobox) >= 2.80
BuildRequires:	perl(autobox::Core) >= 1.0
BuildRequires:	perl(autobox::List::Util) >= 20090629
BuildRequires:	perl(autobox::dump) >= 20090426
BuildRequires:	perl(autodie) >= 2.12
BuildRequires:	perl(autovivification) >= 0.06
BuildRequires:	perl(base)
BuildRequires:	perl(constant)
BuildRequires:	perl(if)
BuildRequires:	perl(indirect) >= 0.24
BuildRequires:	perl(mro)
BuildRequires:	perl(open)
BuildRequires:	perl(overload)
BuildRequires:	perl(parent) >= 0.221
BuildRequires:	perl(true::VERSION) >= 0.16
BuildRequires:	perl(utf8::all) >= 0.015
BuildRequires:	perl(version) >= 0.77
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::CBuilder) >= 0.26
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(PerlIO)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Output) >= 0.16
BuildRequires:	perl(Test::Warn) >= 0.11
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(CLASS) >= 1.00
Requires:	perl(Capture::Tiny) >= 0.06
Requires:	perl(Carp::Fix::1_25) >= 1.000000
Requires:	perl(Child) >= 0.009
Requires:	perl(Data::Dumper)
Requires:	perl(DateTime) >= 0.47
Requires:	perl(DateTime::Format::Epoch) >= 0.11
Requires:	perl(DateTime::TimeZone::Tzfile) >= 0.002
Requires:	perl(Devel::Declare::MethodInstaller::Simple) >= 0.006009
Requires:	perl(Digest::MD5) >= 2.36
Requires:	perl(Digest::SHA) >= 5.45
Requires:	perl(English)
Requires:	perl(File::chdir) >= 0.1002
Requires:	perl(File::Spec)
Requires:	perl(Hash::FieldHash) >= 0.06
Requires:	perl(Hash::Merge::Simple) >= 0.04
Requires:	perl(Hash::StoredIterator) >= 0.007
Requires:	perl(Import::Into) >= 1.002003
Requires:	perl(IPC::System::Simple) >= 1.18
Requires:	perl(JSON::MaybeXS) >= 1.003005
Requires:	perl(List::MoreUtils) >= 0.22
Requires:	perl(Modern::Perl) >= 1.03
Requires:	perl(Module::Load) >= 0.16
Requires:	perl(Object::ID) >= v0.1.0
Requires:	perl(Path::Tiny) >= 0.036
Requires:	perl(Perl6::Caller) >= 0.100
Requires:	perl(Taint::Util) >= 0.06
Requires:	perl(Text::Wrap) >= 2009.0305
Requires:	perl(Try::Tiny) >= 0.02
Requires:	perl(Want) >= 0.18
Requires:	perl(YAML::Any) >= 0.70
Requires:	perl(autobox) >= 2.80
Requires:	perl(autobox::Core) >= 1.0
Requires:	perl(autobox::List::Util) >= 20090629
Requires:	perl(autobox::dump) >= 20090426
Requires:	perl(autodie) >= 2.12
Requires:	perl(autovivification) >= 0.06
Requires:	perl(if)
Requires:	perl(indirect) >= 0.24
Requires:	perl(parent) >= 0.221
Requires:	perl(true::VERSION) >= 0.16
Requires:	perl(utf8::all) >= 0.015

# Filter underspecified dependencies
%global __requires_exclude ^perl\\(CLASS\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Carp::Fix::1_25\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Devel::Declare::MethodInstaller::Simple\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Hash::FieldHash\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Hash::StoredIterator\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Import::Into\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Module::Load\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Try::Tiny\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Want\\)$
%global __requires_exclude %__requires_exclude|^perl\\(autobox\\)$
%global __requires_exclude %__requires_exclude|^perl\\(autobox::Core\\)$
%global __requires_exclude %__requires_exclude|^perl\\(autobox::List::Util\\)$
%global __requires_exclude %__requires_exclude|^perl\\(autobox::dump\\)$
%global __requires_exclude %__requires_exclude|^perl\\(autodie\\)$
%global __requires_exclude %__requires_exclude|^perl\\(autovivification\\)$
%global __requires_exclude %__requires_exclude|^perl\\(parent\\)$

%description
Perl 5 has a lot of warts. There's a lot of individual modules and techniques
out there to fix those warts. perl5i aims to pull the best of them together
into one module so you can turn them on all at once.

This includes adding features, changing existing core functions and changing
defaults. It will likely not be 100%% backwards compatible with Perl 5, though
it will be 99%%, perl5i will try to have a lexical effect.

Please add to this imaginary world and help make it real, either by telling
me what Perl looks like in your imagination
(http://github.com/schwern/perl5i/issues) or make a fork (forking on github is
like a branch you control) and implement it yourself.

%prep
%setup -q -n perl5i-v%{version}

# Fix coercion warnings in 0.pm and 1.pm as per existing fixes in 2.pm
%patch0

%build
perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{_bindir}/perl5i
%{perl_vendorlib}/perl5i.pm
%{perl_vendorlib}/perl5i/
%doc %{perl_vendorlib}/perl5ifaq.pod
%{_mandir}/man3/perl5i.3*
%{_mandir}/man3/perl5i::Meta.3*
%{_mandir}/man3/perl5i::Signature.3*
%{_mandir}/man3/perl5i::latest.3*
%{_mandir}/man3/perl5ifaq.3*

%changelog
* Mon Mar  9 2020 Paul Howarth <paul@city-fan.org> - 2.13.2-14
- This package uses English

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.2-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.2-8
- Perl 5.28 rebuild

* Wed Feb 21 2018 Paul Howarth <paul@city-fan.org> - 2.13.2-7
- Fix coercion warnings in 0.pm and 1.pm as per existing fixes in 2.pm
- BR: coreutils, gcc and perl-devel

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.2-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 12 2016 Paul Howarth <paul@city-fan.org> - 2.13.2-1
- Update to 2.13.2
  - Prevent 'perl5i -e' from segfaulting (GH#269)
  - Fix stat() and lstat() for Perl 5.24 (GH#291)
  - Spelling fixes from Debian (GH#294)
  - "siganture" typo fixes (GH#295)
  - extra_compiler_flags are passed through when building the perl5i executable
  - Kwalitee fixups (GH#289)
  - Now testing against Perl 5.22 (GH#292)
  - Now using JSON::MaybeXS instead of JSON (GH#288)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.1-6
- Perl 5.24 rebuild

* Thu Apr 28 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.1-5
- Fixed stat() and lstat() calls for perl 5.23.3+

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.1-2
- Perl 5.22 rebuild

* Wed Jan  7 2015 Paul Howarth <paul@city-fan.org> - 2.13.1-1
- Update to 2.13.1
  - Upgrade utf8::all requirement to get consistent @ARGV behaviour
  - The latest autodie is recommended for load time and memory usage
    improvements (GH#284)
  - Change how we import utf8::all so @ARGV is translated appropriately
    (GH#279)
  - Update autobox to avoid segfaults during global destruction (GH#283,
    CPAN RT#71777)

* Tue Sep  9 2014 Paul Howarth <paul@city-fan.org> - 2.13.0-4
- Add upstream fix for compatibility with utf8::all ≳ 0.013 (#1134872)

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.0-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Paul Howarth <paul@city-fan.org> - 2.13.0-1
- Update to 2.13.0
  - $scalar->path will return a Path::Tiny object using the contents of
    $scalar, which makes working with files much, much easier (GH#229, GH#247)
  - The project has moved to the evalEmpire organization to allow broader
    project admin options (http://github.com/evalEmpire/perl5i)
  - Added a project rationale (GH#226, GH#252)
  - Fixed a crash if the perl5i command line is fed a null byte
    (GH#269, GH#273)
  - Stop using deprecated Hash::StoreIterator::eech() (GH#270)
  - The methods() meta method now ignores subroutines declared with func()
    (GH#222, GH#253)
- Use %%license

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 12 2013 Paul Howarth <paul@city-fan.org> - 2.12.0-3
- Add missing dependencies (#998496)
  - BR: perl(lib) for the build process
  - BR: perl(Carp), perl(Data::Dumper), perl(Encode), perl(File::Spec),
    perl(if), perl(IO::Handle), perl(POSIX), perl(Scalar::Util) and
    perl(Sub::Name) for the module
  - BR: perl(Config), perl(Exporter), (File::Temp) and perl(PerlIO) for the
    test suite
  - R: perl(Data::Dumper), perl(File::Spec) and perl(if) for runtime

* Mon Aug 19 2013 Paul Howarth <paul@city-fan.org> - 2.12.0-2
- Sanitize for Fedora submission

* Fri Aug 16 2013 Paul Howarth <paul@city-fan.org> - 2.12.0-1
- Initial RPM version
