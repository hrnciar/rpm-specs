Name:           perl-File-Rsync
Version:        0.49
Release:        6%{?dist}
Summary:        Perl module interface to rsync
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-Rsync/
Source0:        http://www.cpan.org/authors/id/L/LE/LEAKIN/File-Rsync-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(:VERSION) >= 5.008
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  rsync
Requires:       rsync
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Perl Convenience wrapper for the rsync(1) program. Written for rsync-
2.3.2 and updated for rsync-3.1.1 but should perform properly with most
recent versions.

%prep
%setup -q -n File-Rsync-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changelog README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-2
- Perl 5.30 rebuild

* Tue Feb 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.49-1
- Specfile autogenerated by cpanspec 1.78.
