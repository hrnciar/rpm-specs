Name:           perl-JSON-Validator
Version:        4.00
Release:        2%{?dist}
Summary:        Validate data against a JSON schema
License:        Artistic 2.0

URL:            https://metacpan.org/release/JSON-Validator
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/JSON-Validator-%{version}.tar.gz

BuildArch:      noarch
# build dependencies
BuildRequires:  make
BuildRequires:  perl-interpreter >= 0:5.010001
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl >= 0:5.010001
# runtime deps
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Mojo::Base) >= 7.28
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::JSON::Pointer)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
# test deps
BuildRequires:  perl(Data::Validate::Domain)
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Net::IDN::Encode)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More) >= 1.30
BuildRequires:  perl(Net::IDN::Encode)
BuildRequires:  perl(Net::IDN::Encode)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(lib)
Requires:       perl(Mojolicious) >= 7.28
Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))
Suggests:       perl(YAML::XS) >= 0.67
Suggests:       perl(Term::ANSIColor)
Suggests:       perl(Mojo::UserAgent)
Suggests:       perl(Data::Validate::Domain)
Suggests:       perl(Data::Validate::IP)
Suggests:       perl(Net::IDN::Encode)

%description
JSON::Validator is a data structure validation library based around JSON
Schema. This module can be used directly with a JSON schema or you can use
the elegant DSL schema-builder JSON::Validator::joi to define the schema
programmatically.

%prep
%setup -q -n JSON-Validator-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md
%{perl_vendorlib}/JSON*
%{_mandir}/man3/JSON*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.00-2
- Perl 5.32 rebuild

* Sun Jun 14 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 4.00-1
- Update to 4.00

* Sun Mar 29 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.25-1
- Update to 3.25

* Sun Mar 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.24-1
- Update to 3.24

* Thu Feb 20 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.23-1
- Update to 3.23

* Sun Feb 16 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.22-1
- Update to 3.22

* Sun Feb 09 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.19-1
- Update to 3.19

* Sun Feb 02 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 3.18-1
- Update to 3.18

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.17-1
- Update to 3.17

* Fri Nov 01 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.16-1
- Update to 3.16

* Sun Sep 29 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.15-1
- Update to 3.15

* Sun Aug 11 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.14-1
- Update to 3.14
- Replace calls to "make pure_install" to %%{make_install}
- Replace calls to "make" to %%{make_build}
- Pass NO_PERLLOCAL to Makefile.PL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.11-2
- Perl 5.30 rebuild

* Sun May 12 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.11-1
- Update to 3.11

* Sun May 05 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.10-1
- Update to 3.10

* Sun Apr 07 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.08-1
- Update to 3.08

* Thu Mar 07 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.06-2
- Take into account review comments (#1686210)

* Wed Mar 06 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 3.06-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.