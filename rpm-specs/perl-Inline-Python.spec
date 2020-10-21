Name:           perl-Inline-Python
Version:        0.56
Release:        14%{?dist}
Summary:        Write Perl subs and classes in Python
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Inline-Python
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NINE/Inline-Python-%{version}.tar.gz
Patch0:         Inline-Python-0.56-Use-python3.patch
BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Inline) >= 0.46
BuildRequires:  perl(Inline::denter)
BuildRequires:  perl(JSON)
BuildRequires:  perl(overload)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::ProcessTable) >= 0.53
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  python3
BuildRequires:  python3-devel
Requires:       perl(Inline) >= 0.46
Requires:       perl(Inline::denter)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Remove underspecified generated dependency
%global __requires_exclude ^perl\\(Inline\\)$

%description
The Inline::Python module allows you to put Python source code directly
"inline" in a Perl script or module. It sets up an in-process Python
interpreter, runs your code, and then examines Python's symbol table for
things to bind to Perl. The process of interrogating the Python interpreter
for global variables only occurs the first time you run your Python code. The
name-space is cached, and subsequent calls use the cached version.

%prep
%setup -q -n Inline-Python-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README ToDo
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Inline*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-13
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.56-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.56-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-5
- Use Python 3 for build

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.56-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-1
- 0.56 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.54-1
- 0.54 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-1
- 0.52 bump

* Tue Aug 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-1
- 0.50 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 24 2015 Jon Kerr Nilsen <j.k.nilsen@usit.uio.no> 0.49-3
- added two forgotten BuildRequires
* Wed Jun 24 2015 Jon Kerr Nilsen <j.k.nilsen@usit.uio.no> 0.49-2
- adjusted to fit Fedora packaging guidelines.
* Fri Jun 19 2015 Jon Kerr Nilsen <j.k.nilsen@usit.uio.no> 0.49-1
- Specfile autogenerated by cpanspec 1.78.
