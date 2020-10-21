Name:           perl-Hash-FieldHash
Version:        0.15
Release:        15%{?dist}
Summary:        Lightweight field hash implementation
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Hash-FieldHash
Source0:        https://cpan.metacpan.org/modules/by-module/Hash/Hash-FieldHash-%{version}.tar.gz
Patch0:         Hash-FieldHash-0.15-Fix-building-on-Perl-without-dot-in-INC.patch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.40.05
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(strict)
BuildRequires:  perl(XSLoader) >= 0.02
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(threads)
# Optional Tests
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Test::LeakTrace) >= 0.07
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Synopsis)
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Avoid provides from private shared objects
%{?perl_default_filter}

%description
Hash::FieldHash provides the field hash mechanism, which supports the inside-
out technique.

%prep
%setup -q -n Hash-FieldHash-%{version}

# Fix building on Perl without '.' in @INC
%patch0 -p1

%build
RELEASE_TESTING=1 perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README.md benchmark/ example/
%{perl_vendorarch}/auto/Hash/
%{perl_vendorarch}/Hash/
%{_mandir}/man3/Hash::FieldHash.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-8
- Perl 5.28 rebuild

* Fri Mar  2 2018 Paul Howarth <paul@city-fan.org> - 0.15-7
- Arch-specific package using Module::Build needs to use ExtUtils::CBuilder
  (https://bugzilla.redhat.com/show_bug.cgi?id=1547165#c7)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-3
- Perl 5.26 rebuild

* Thu May 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Fix building on Perl without '.' in @INC

* Mon Feb  6 2017 Paul Howarth <paul@city-fan.org> - 0.15-1
- Update to 0.15
  - t/orig/03_class.t failed if FamilyTreeInfo-2.3.24 was installed (GH#1)
- Classify buildreqs by usage
- Simplify find command using -empty and -delete

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.22 rebuild

* Wed Nov 12 2014 Paul Howarth <paul@city-fan.org> - 0.14-1
- Update to 0.14
  - Use Module::Build instead of Module::Install with minil(1)
  - No code changes
- Specify all dependencies
- Use %%license where possible
- Make %%files list more explicit

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-10
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 0.12-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.12-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Iain Arnell <iarnell@gmail.com> 0.12-1
- update to latest upstream version

* Tue Aug 23 2011 Iain Arnell <iarnell@gmail.com> 0.10-2
- drop unnecessary explicit buildrequires

* Thu Aug 11 2011 Iain Arnell <iarnell@gmail.com> 0.10-1
- Specfile autogenerated by cpanspec 1.78.
