%define upstream_name    Test-Data-Split

Name:       perl-%{upstream_name}
Version:    0.2.2
Release:    1%{?dist}

Summary:    Split data-driven tests into several test scripts
License:    MIT
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{version}.tar.gz

Requires:  perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:  perl(List::MoreUtils)
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::All)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Build) >= 0.280.0
BuildRequires: perl(MooX)
BuildRequires: perl(MooX::late)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(autodie)
BuildRequires: perl(blib)
BuildRequires: perl(lib)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch:  noarch

%description
This module splits a set of data with IDs and arbitrary values into one test
file per (key+value) for easy parallelization.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%files
%license LICENSE
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

%changelog
* Tue Oct 20 2020 Shlomi Fish <shlomif@shlomifish.org> 0.2.2-1
- New version

* Thu Aug 06 2020 Shlomi Fish <shlomif@shlomifish.org> 0.2.1-8
- Rebuild due to Koschei build failure.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-6
- Perl 5.32 rebuild

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-5
- Add missing dependency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-2
- Perl 5.30 rebuild

* Tue Apr 09 2019 Shlomi Fish <shlomif@cpan.org> 0.2.1-1
- Initial Fedora package.
