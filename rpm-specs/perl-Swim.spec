Name:           perl-Swim
Version:        0.1.48
Release:        3%{?dist}
Summary:        See What I Mean is a plain text markup language
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Swim
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Swim-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(HTML::Escape)
# IPC::Run not used
BuildRequires:  perl(Pegex) >= 0.41
BuildRequires:  perl(Pegex::Base)
BuildRequires:  perl(Pegex::Grammar)
BuildRequires:  perl(Pegex::Parser)
BuildRequires:  perl(Pegex::Tree)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(YAML::XS)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
BuildRequires:  perl(TestML::Bridge)
BuildRequires:  perl(TestML::Run::TAP)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Hash::Merge)
Requires:       perl(IPC::Run)
Requires:       perl(Pegex) >= 0.41
Requires:       perl(Pegex::Grammar)
Requires:       perl(Pegex::Tree)
Requires:       perl(Text::Autoformat)
Requires:       perl(YAML::XS)

%description
Swim (See What I Mean) is a plain text markup language that converts to many
formats: HTML, MarkDown, POD, Formatted Plain Text, LaTeX, DocBook, roff,
AsciiDoc, MediaWiki. The Swim framework is easily extensible, so adding new
outputs is easy.

%prep
%setup -q -n Swim-%{version}
# Remove bundled modules
rm -rf ./inc/lib
perl -i -ne 'print $_ unless m{^inc/lib/}' MANIFEST
# Fix shebang
perl -i -pe 's/^#!.*/#!perl/' bin/swim

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING SWIM_LINK_FORMAT_HACK SWIM_PEGEX_DEBUG SWIM_PEGEX_TREE
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{_bindir}/swim
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.48-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Petr Pisar <ppisar@redhat.com> - 0.1.48-1
- 0.1.48 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.46-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.46-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Petr Pisar <ppisar@redhat.com> - 0.1.46-7
- Old TestML API moved to TestML1 name space (bug #1650156)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.46-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.46-5
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.46-2
- Perl 5.26 rebuild

* Mon Mar 13 2017 Petr Pisar <ppisar@redhat.com> 0.1.46-1
- Specfile autogenerated by cpanspec 1.78.
