Name:           perl-MooX-Role-Logger
Version:        0.005
Release:        4%{?dist}
Summary:        Universal logging via Log::Any
License:        ASL 2.0

URL:            https://metacpan.org/release/MooX-Role-Logger
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/MooX-Role-Logger-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Test)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)


Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This role provides universal logging via Log::Any. The class using this role
doesn't need to know or care about the details of log configuration,
implementation or destination.


%prep
%autosetup -n MooX-Role-Logger-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/MooX::Role::Logger*.*
%{_mandir}/man3/MooseX::Role::Logger*.*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Sandro Mani <manisandro@gmail.com> - 0.005-2
- Fix license tag
- Fix / constrain BRs
- Pass NO_PACKLIST=1 to Makefile.PL
- Run fixperms on buildroot

* Sat Jan 04 2020 Sandro Mani <manisandro@gmail.com> - 0.005-1
- Initial package
