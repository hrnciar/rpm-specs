Name:             perl-re-engine-RE2
Summary:          RE2 regex engine
Version:          0.13
Release:          24%{?dist}
License:          GPL+ or Artistic
URL:              https://metacpan.org/release/re-engine-RE2
Source0:          https://cpan.metacpan.org/authors/id/D/DG/DGL/re-engine-RE2-%{version}.tar.gz

# Discussion started with upstream at:
#     https://rt.cpan.org/Public/Bug/Display.html?id=83467
Patch0:           re-engine-RE2-0.11-Unbundle-re2.patch
# Do not use global $_ in "my" (CPAN RT#108357)
Patch1:           re-engine-RE2-0.13-Do-not-use-global-in-my.patch
# Fix 01.basic.t for v5.29.9 Variable length lookbehind support (CPAN RT#129585)
Patch2:           re-engine-RE2-0.13-Fix-01-basic.t-for-Variable-length-lookbehind-support.patch

BuildRequires:    coreutils
BuildRequires:    findutils
BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    make
BuildRequires:    perl-interpreter
BuildRequires:    perl-devel
BuildRequires:    perl-generators
BuildRequires:    perl(ExtUtils::CppGuess)
BuildRequires:    perl(ExtUtils::MakeMaker)
BuildRequires:    perl(XSLoader)
BuildRequires:    perl(Test::More)
BuildRequires:    re2-devel

Requires:         perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module replaces perl's regex engine in a given lexical scope with RE2.


%prep
%setup -q -n re-engine-RE2-%{version}

# Remove incorrect executable bits
chmod -x lib/re/engine/RE2.pm

# Just to be sure we don't build against the bundled version
rm -fr re2

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -size 0 -delete

%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/re*
%{_mandir}/man3/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-23
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.13-21
- rebuild (re2)

* Thu Aug 08 2019 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.13-20
- Rebuilt for new RE2 version (BZ#1672014)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-18
- Perl 5.30 rebuild

* Thu May 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-17
- Fix 01.basic.t for v5.29.9 Variable length lookbehind support

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-14
- Perl 5.28 rebuild

* Tue Mar 13 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.13-13
- Add missing build-requirements

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-7
- Perl 5.24 rebuild

* Fri Apr 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-6
- Do not use global $_ in "my" (CPAN RT#108357)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-3
- Perl 5.22 rebuild

* Wed Apr 15 2015 Petr Pisar <ppisar@redhat.com> - 0.13-2
- Rebuild owing to C++ ABI change in GCC-5 (bug #1195351)

* Sun Jan 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.13-1
- Update to 0.13

* Sun Jan 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.12-1
- Update to 0.12
- Drop upstreamed patches

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-9
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-8
- Fix for Perl 5.20 (RT#95144)

* Mon Jun 09 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.11-7
- Fix the build with -Werror=format-security.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.11-4
- Perl 5.18 rebuild

* Wed Mar 06 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.11-3
- Petr is right, the patch does look much more readable this way.

* Thu Feb 21 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.11-2
- Remove incorrect executable bits.
- Add a missing build requirement.

* Wed Feb 20 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.11-1
- Initial package, with help from cpanspec.
