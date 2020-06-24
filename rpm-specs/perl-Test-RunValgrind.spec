%define upstream_name    Test-RunValgrind

Name:       perl-%{upstream_name}
Version:    0.2.1
Release:    6%{?dist}

Summary:    Tests that an external program is valgrind-clean
License:    MIT
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{version}.tar.gz

Requires:  perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Module::Build) >= 0.280.0
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(Test::Trap)
BuildRequires: perl(blib)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
valgrind is an open source and convenient memory debugger that runs on some
platforms. This module runs valgrind (the
http://en.wikipedia.org/wiki/Valgrind manpage) on an executable and makes
sure that valgrind did not find any faults in it.

It originated from some code used to test the Freecell Solver executables
using valgrind, and was extracted into its own CPAN module to allow for
reuse by other projects, including fortune-mod (the
https://github.com/shlomif/fortune-mod manpage).

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Build.PL --installdirs=vendor

./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}

%files
%license LICENSE
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-6
- Perl 5.32 rebuild

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-5
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-2
- Perl 5.30 rebuild

* Tue Mar 26 2019 Shlomi Fish <shlomif@cpan.org> 0.2.0-1
- Initial Fedora package based on the Mageia one.
