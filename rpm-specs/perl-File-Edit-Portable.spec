Name:           perl-File-Edit-Portable
Version:        1.24
Release:        15%{?dist}
Summary:        Read and write files while keeping the original line-endings intact
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-Edit-Portable

Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEVEB/File-Edit-Portable-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)

# Testing
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Tempdir)
BuildRequires:  perl(Mock::Sub) >= 1.06
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::CheckManifest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The default behavior of perl is to read and write files using the
Operating System's (OS) default record separator (line ending). If you open
a file on an OS where the record separators are that of another OS, things
can and do break.

%prep
%setup -q -n File-Edit-Portable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test AUTHOR_TESTING=1

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-11
- Perl 5.30 rebuild

* Sat Mar 30 2019 Denis Fateyev <denis@fateyev.com> - 1.24-10
- Dropped RELEASE tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.24-2
- Perl 5.24 rebuild

* Mon Mar 21 2016 Denis Fateyev <denis@fateyev.com> - 1.24-1
- Update to 1.24 release

* Sat Feb 27 2016 Denis Fateyev <denis@fateyev.com> - 1.20-1
- Update to 1.20 release

* Wed Feb 10 2016 Denis Fateyev <denis@fateyev.com> - 1.18-1
- Update to 1.18 release

* Sat Jan 23 2016 Denis Fateyev <denis@fateyev.com> - 1.16-1
- Update to 1.16 release

* Wed Dec 09 2015 Denis Fateyev <denis@fateyev.com> - 1.11-1
- Update to 1.11 release

* Wed Nov 25 2015 Denis Fateyev <denis@fateyev.com> - 1.10-1
- Initial release
