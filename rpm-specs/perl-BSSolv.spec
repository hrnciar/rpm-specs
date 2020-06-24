%global min_libsolv_version 0.7.2

#global commit 1955d7faf7a7eacb96895a2c0e201135738f3750
#global shortcommit %(c=%{commit}; echo ${c:0:7})
#global commitdate 20191121

# for rpmdev-bumpspec to handle properly...
%global baserelease 2

Name:           perl-BSSolv
Version:        0.17
Release:        %{baserelease}%{?commit:.git%{commitdate}.%{shortcommit}}%{?dist}
Summary:        OBS solver and repository management using libsolv
License:        GPL or Artistic
URL:            https://github.com/openSUSE/perl-BSSolv
%if %{defined commit}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc
BuildRequires:  libsolv-devel >= %{min_libsolv_version}
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Test::More)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       libsolv%{?_isa} >= %{min_libsolv_version}


%description
This is a support perl module for the OBS backend. It contains functions
for repository management, dependency solving, package ordering, and meta
file creation.


%prep
%if %{defined commit}
%autosetup -n %{name}-%{commit} -p1
%else
%autosetup -p1
%endif

%build
# Ensure build flags are set
%{set_build_flags}
perl Makefile.PL
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install_vendor
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} \;
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorarch}/BSSolv.pm
%{perl_vendorarch}/auto/BSSolv
%doc README dist/perl-BSSolv.changes

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-2
- Perl 5.32 rebuild

* Mon Feb 17 2020 Neal Gompa <ngompa13@gmail.com> - 0.17-1
- Update to 0.17

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3.git20191121.1955d7f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Neal Gompa <ngompa13@gmail.com> - 0.15-2.git20191121.1955d7f
- Rebuild to deal with random Koji+Bodhi breakage

* Fri Dec 27 2019 Neal Gompa <ngompa13@gmail.com> - 0.15-1.git20191121.1955d7f
- Rebase to post-0.15 git master snapshot for modularity support

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14-4
- Rebuild for libsolv 0.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.28 rebuild

* Sun May 27 2018 Neal Gompa <ngompa13@gmail.com> - 0.14-1
- Rebase to 0.14
- Backport genmetaalgo support
- Refresh patch for building against EL libsolv
- Enable running unit tests
- Modernize spec

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.01-19.git1e18c32
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-18.git1e18c32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-17.git1e18c32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-16.git1e18c32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-15.git1e18c32
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-14.git1e18c32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Petr Pisar <ppisar@redhat.com> - 0.01-13.git1e18c32
- Fix Debian and Arch support alignent to libsolv (bug #1342160)
- Rebuild against libsolv enabled Debian and Arch package format (bug #1342160)

* Mon Jun 06 2016 Petr Pisar <ppisar@redhat.com> - 0.01-12.git1e18c32
- Align Debian and Arch support to libsolv (bug #1342160)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-11.git1e18c32
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-10.git1e18c32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-9.git1e18c32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-8.git1e18c32
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-7.git1e18c32
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-6.git1e18c32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.01-5.git1e18c32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 Josef Stribny <jstribny@redhat.com> 0.01-4.git1e18c32
- Fix license
- Add BR: perl(strict)
- Remove redundant BRs

* Sun Apr 20 2014 Josef Stribny <jstribny@redhat.com> 0.01-3.git1e18c32
- Remove libsolv dep
- use %%{?_smp_mflags} macro

* Wed Feb 19 2014 Josef Stribny <jstribny@redhat.com> 0.01-2.git1e18c32
- Clean up the spec file and changelog
- Use tarball for the sources

* Fri Feb 14 2014 Josef Stribny <jstribny@redhat.com> 0.01-1.git1e18c32
- Update to git release 1e18c32
- Fix upstream url
- Add README
- Change versioning to perl-BSSolv itself

