Name:           perl-SQL-SplitStatement
Version:        1.00020
Release:        18%{?dist}
Summary:        Split any SQL code into atomic statements
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/SQL-SplitStatement
Source0:        https://cpan.metacpan.org/authors/id/E/EM/EMAZEP/SQL-SplitStatement-%{version}.tar.gz
# Fixes incompatibility with Getopt::Long v2.48
# https://rt.cpan.org/Ticket/Display.html?id=108595
Patch0:         perl-SQL-SplitStatement-1.00020-getopt-long-compat.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(SQL::Tokenizer) >= 0.22
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script::Run)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is a simple module which tries to split any SQL code, even including
non-standard extensions (for the details see the "SUPPORTED DBMSs" section
of the module documentation), into the atomic statements it is composed of.

%prep
%setup -q -n SQL-SplitStatement-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
# The LICENSE file is outdated and contains the wrong address for the FSF
# https://rt.cpan.org/Ticket/Display.html?id=107996
%license LICENSE
%{_bindir}/sql-split
%{perl_vendorlib}/SQL
%{_mandir}/man1/sql-split*
%{_mandir}/man3/SQL*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.00020-17
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00020-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.00020-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.00020-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.00020-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 08 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.00020-4
- Patch package to fix incompatibility with perl-Getopt-Long (#1278707)

* Thu Oct 29 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.00020-3
- Take into account review comments (#1276161)

* Thu Oct 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.00020-2
- Clean up the spec file

* Sat Oct 17 2015 Adam Williamson <awilliam@redhat.com> - 1.00020-1
- initial package
