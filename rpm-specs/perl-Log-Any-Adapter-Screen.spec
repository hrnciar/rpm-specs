Name:           perl-Log-Any-Adapter-Screen
Version:        0.140
Release:        7%{?dist}
Summary:        Send logs to screen, with colors and some other features

License:        GPL+ or Artistic
URL:            https://search.cpan.org/dist/Log-Any-Adapter-Screen/
Source0:        https://www.cpan.org/modules/by-module/Log/Log-Any-Adapter-Screen-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.010
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter) >= 0.11
BuildRequires:  perl(Log::Any::Adapter::Base)
BuildRequires:  perl(Log::Any::Adapter::Util)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >=  1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This Log::Any adapter prints log messages to screen (STDERR/STDOUT).  The
messages are colored according to level (unless coloring is turned off).
It has a few other features: allow passing formatter, allow setting level
from some environment variables, add prefix/timestamps.


%prep
%autosetup -n Log-Any-Adapter-Screen-%{version} -p 1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
%make_build test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.140-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.140-6
- Perl 5.32 rebuild

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.140-5
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.140-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.140-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.140-2
- Perl 5.30 rebuild

* Mon Feb 25 2019 Björn Esser <besser82@fedoraproject.org> - 0.140-1
- Bump release to stable (#1680375)

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.140-0.3
- Changes as suggested in review (#1680375)
- Add a set of explicit BuildRequires

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.140-0.2
- Add explicit perl module compat requires

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.140-0.1
- Initial rpm release (#1680375)
