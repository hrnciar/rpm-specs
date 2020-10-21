Name:		perl-File-Copy-Recursive-Reduced
Version:	0.006
Release:	9%{?dist}
Summary:	Recursive copying of files and directories within Perl 5 toolchain
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/File-Copy-Recursive-Reduced
Source0:	https://cpan.metacpan.org/modules/by-module/File/File-Copy-Recursive-Reduced-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(lib)
BuildRequires:	perl(Path::Tiny)
BuildRequires:	perl(Test::More) >= 0.44
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This library is intended as a not-quite-drop-in replacement for certain
functionality provided by CPAN distribution File-Copy-Recursive. The library
provides methods similar enough to that distribution's fcopy() and dircopy()
functions to be usable in those CPAN distributions often described as being
part of the Perl toolchain.

%prep
%setup -q -n File-Copy-Recursive-Reduced-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README Todo
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Copy::Recursive::Reduced.3*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-2
- Perl 5.28 rebuild

* Tue Apr 24 2018 Paul Howarth <paul@city-fan.org> - 0.006-1
- Update to 0.006
  - File::Copy::Recursive 0.41 has been released to CPAN and addresses the
    problem which was the focus of File::Copy::Recursive::Reduced; Hence, FCR2
    is now feature-complete

* Fri Apr 20 2018 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005
  - Introduce rcopy(), a stripped-down replacement for
    File::Copy::Recursive::rcopy()
  - Implement copying of symlinks within all three public functions; at this
    point we should be able to make substitutions for File::Copy::Recursive's
    fcopy(), dircopy() and rcopy() functions in a large proportion of toolchain
    libraries, particularly in test suites

* Wed Apr 18 2018 Paul Howarth <paul@city-fan.org> - 0.003-1
- Initial RPM version
