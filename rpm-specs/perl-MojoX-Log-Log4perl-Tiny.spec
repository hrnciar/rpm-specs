Name:           perl-MojoX-Log-Log4perl-Tiny
Version:        0.01
Release:        5%{?dist}
Summary:        Minimalistic Log4perl adapter for Mojolicious
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/MojoX-Log-Log4perl-Tiny
Source0:        https://cpan.metacpan.org/authors/id/Y/YO/YOWCOW/MojoX-Log-Log4perl-Tiny-%{version}.tar.gz

BuildArch:      noarch
# build dependencies
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny)
# runtime dependencies
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(strict)
# test dependencies
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))
Requires:       perl(Log::Log4perl)

%description
MojoX::Log::Log4perl::Tiny allows you to replace default Mojolicious
logging Mojo::Log with your existing Log::Log4perl::Logger instance.

%{?perl_default_filter}

%prep
%setup -q -n MojoX-Log-Log4perl-Tiny-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/MojoX*
%{_mandir}/man3/MojoX*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.01-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.01-2
- Take into account review comments (#1747152)

* Wed Aug 28 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.01-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
