Name:           perl-HTTP-MultiPartParser
Version:        0.02
Release:        12%{?dist}
Summary:        HTTP MultiPart Parser
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTTP-MultiPartParser
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/HTTP-MultiPartParser-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 1:5.8.1

BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Deep)

BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

BuildRequires:  %{__make}

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class provides a low-level API for processing MultiPart MIME data
streams conforming to MultiPart types as defined in RFC 2616.

%prep
%setup -q -n HTTP-MultiPartParser-%{version}
%{__rm} -rf inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README eg/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-2
- Perl 5.26 rebuild

* Tue Apr 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-1
- Upstream update.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.01-2
- Reflect feedback from review.

* Sat Oct 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.01-1
- Initial Fedora package.
