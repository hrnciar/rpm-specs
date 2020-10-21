Name:           perl-Text-Template-Simple
Version:        0.91
Release:        8%{?dist}
Summary:        Simple text template engine
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Text-Template-Simple
Source0:        https://cpan.metacpan.org/authors/id/B/BU/BURAK/Text-Template-Simple-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
# XXX: BuildRequires:  perl(File::Basename)
# XXX: BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.6
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Data::Dumper) >= 2.101
BuildRequires:  perl(Devel::Size) >= 0.77
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Fcntl) >= 1.03
BuildRequires:  perl(File::stat)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
# XXX: BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Safe) >= 2.06
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::Table) >= 1.107
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp) >= 0.12
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More) >= 0.40
BuildRequires:  perl(vars)
# Optional tests only
BuildRequires:  perl(Pod::Simple) >= 3.05
BuildRequires:  perl(Test::Pod) >= 1.26
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Data::Dumper) >= 2.101
Requires:       perl(Devel::Size) >= 0.77
Requires:       perl(Digest::MD5)
Requires:       perl(Fcntl) >= 1.03
Requires:       perl(File::Find)
Requires:       perl(File::Spec) >= 0.6
Requires:       perl(File::stat)
Requires:       perl(IO::File)
Requires:       perl(IO::Handle)
Requires:       perl(Perl::Tidy)
Requires:       perl(Safe) >= 2.06
Requires:       perl(Symbol)
Requires:       perl(Text::Table) >= 1.107

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$

%description
%{summary}.

%prep
%setup -q -n Text-Template-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes eg etc/flowchart.txt TODO
%{_bindir}/tts
%{_mandir}/man1/tts*
%{_mandir}/man3/Text*
%{perl_vendorlib}/Text*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.91-7
- Perl 5.32 rebuild

* Wed Mar 11 2020 Petr Pisar <ppisar@redhat.com> - 0.91-6
- Build-require blib for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.91-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.91-1
- Update to 0.91
- Drop no-longer-needed patch
- Switch to a Makefile.PL-based build system

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-7
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-4
- Perl 5.26 rebuild

* Tue May 16 2017 Petr Pisar <ppisar@redhat.com> - 0.90-3
- Fix building on Perl without "." in @INC (CPAN RT#121697)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 10 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.90-1
- Update to 0.90

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.86-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.86-2
- Perl 5.22 rebuild

* Tue Apr 14 2015 Petr Šabata <contyk@redhat.com> 0.86-1
- Initial packaging
