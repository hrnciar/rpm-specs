Name:		perl-Object-ID
Version:	0.1.2
Release:	20%{?dist}
Summary:	A unique identifier for any object
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Object-ID
Source0:	https://cpan.metacpan.org/modules/by-module/Object/Object-ID-v%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::Build)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::UUID) >= 1.148
BuildRequires:	perl(Hash::FieldHash) >= 0.10
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Name) >= 0.03
BuildRequires:	perl(version) >= 0.77
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(DirHandle)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(threads)
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Data::UUID) >= 1.148

# Don't provide perl(UNIVERSAL)
%{?perl_default_filter}

%description
This is a unique identifier for any object, regardless of its type, structure
or contents. Its features are:

 * Works on ANY object of any type
 * Does not modify the object in any way
 * Does not change with the object's contents
 * Is O(1) to calculate (i.e. doesn't matter how big the object is)
 * The id is unique for the life of the process
 * The id is always a true value

%prep
%setup -q -n Object-ID-v%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Object/
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/Object::ID.3*
%{_mandir}/man3/Object::ID::ConfigData.3*
%{_mandir}/man3/UNIVERSAL::Object::ID.3*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.2-20
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.2-17
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.2-14
- Perl 5.28 rebuild

* Wed Apr 25 2018 Paul Howarth <paul@city-fan.org> - 0.1.2-13
- Spec clean-up
  - Classify buildreqs by usage
  - Drop legacy Group: tag
  - Use %%license
  - Distinguish between 'Build' script commands and options

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.2-10
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.2-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.2-5
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.2-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 18 2013 Paul Howarth <paul@city-fan.org> - 0.1.2-2
- Sanitize for Fedora submission

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 0.1.2-1
- Initial RPM version
