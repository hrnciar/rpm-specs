Name:           perl-YAML-PP
Version:        0.022
Release:        2%{?dist}
Summary:        YAML 1.2 processor
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/YAML-PP/
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-PP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.07
BuildRequires:  perl(Term::ANSIColor) >= 4.02
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
# Tests
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Tie::IxHash)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(boolean)
Requires:       perl(B::Deparse)
Requires:       perl(HTML::Entities)
Requires:       perl(JSON::PP)
Requires:       perl(Scalar::Util) >= 1.07
Requires:       perl(Term::ANSIColor)
Requires:       perl(Tie::IxHash)

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Scalar::Util\\)$

%description
YAML::PP is a modern, modular YAML processor.
It aims to support YAML 1.2 and YAML 1.1. See http://yaml.org/.

%prep
%setup -q -n YAML-PP-%{version}

for i in `find e* -type f`; do
    chmod -x $i
    sed -i -e '1s|#!.*perl|%(perl -MConfig -e 'print $Config{startperl}')|' $i
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md etc examples README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.022-2
- Perl 5.32 rebuild

* Wed May 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.022-1
- 0.022 bump

* Mon Mar 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.021-1
- 0.021 bump

* Tue Feb 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-1
- 0.020 bump

* Fri Feb 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.019-1
- 0.019 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.018-1
- Specfile autogenerated by cpanspec 1.78.