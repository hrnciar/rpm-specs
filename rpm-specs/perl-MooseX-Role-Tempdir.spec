Name:           perl-MooseX-Role-Tempdir
Version:        0.101
Release:        6%{?dist}
Summary:        Moose role to provide temporary directories
License:        ISC
URL:            https://metacpan.org/release/MooseX-Role-Tempdir
Source0:        https://cpan.metacpan.org/authors/id/I/IA/IAMB/MooseX-Role-Tempdir-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(MooseX::Role::Parameterized)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description
This is a very simple Moose role that provides an attribute 'tmpdir' and
creates a temporary directory (via File::Temp) to go along with it. One
temporary directory will be created for every object with this role, so
keep that in mind if you're going crazy with lots of objects or
creation/destruction.

%prep
%setup -q -n MooseX-Role-Tempdir-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
# Changes file is empty
%doc README
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.101-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.101-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.101-1
- Update to 0.101, dropping upstreamed patch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.100-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.100-7
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Jun 07 2017 Petr Pisar <ppisar@redhat.com> - 0.100-6
- Do not package empty Changes file

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.100-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Petr Pisar <ppisar@redhat.com> - 0.100-3
- Remove bogus print (bug #1348230)

* Wed Jun 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.100-2
- License changed to 'ISC License'

* Sat Jun 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.100-1
- Update to 0.100
- Switch to ExtUtils::MakeMaker as a build-system
- Tighten file listing

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-2
- Perl 5.22 rebuild

* Tue Dec 09 2014 Petr Šabata <contyk@redhat.com> 0.03-1
- Initial packaging
