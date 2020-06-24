Name:           perl-DBIx-XHTML_Table
Version:        1.49
Release:        12%{?dist}
Summary:        SQL query result set to XHTML table
License:        Artistic 2.0
URL:            https://metacpan.org/release/DBIx-XHTML_Table
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JEFFA/DBIx-XHTML_Table-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::CSV)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
DBIx::XHTML_Table is a DBI extension that creates an XHTML table from a
database query result set. It was created to fill the gap between fetching
rows from a database and transforming them into a web browser renderable
table. DBIx::XHTML_Table is intended for programmers who want the
responsibility of presenting (decorating) data, easily. This module is
meant to be used in situations where the concern for presentation and logic
separation is overkill. Providing logic or editable data is beyond the
scope of this module, but it is capable of doing such.

%prep
%setup -q -n DBIx-XHTML_Table-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes readme.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-12
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-1
- 1.49 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-2
- Perl 5.24 rebuild

* Wed Feb 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-1
- 1.48 bump; License was changed

* Fri Feb 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.47-2
- Update license

* Thu Feb 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.47-1
- Initial release
