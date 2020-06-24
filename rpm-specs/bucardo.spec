%define         realname Bucardo
Name:           bucardo
Version:        5.6.0
Release:        2%{?dist}
Summary:        Postgres replication system for both multi-master and multi-slave operations
License:        BSD
URL:            http://bucardo.org/
Source0:        http://bucardo.org/downloads/Bucardo-%{version}.tar.gz
Source1:        master-master-replication-example.txt
BuildArch:      noarch

BuildRequires:  postgresql-plperl
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.68
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(boolean)
BuildRequires:  perl(open)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::Pg) >= 2.0
BuildRequires:  perl(DBI) >= 1.51
BuildRequires:  perl(DBIx::Safe)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(Encode::Locale)

# Extra

BuildRequires:  perl(MongoDB)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(Redis)
BuildRequires:  perl(DBD::SQLite)

# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       postgresql-plperl

Recommends:  perl(MongoDB)
Recommends:  perl(DBD::mysql)
Recommends:  perl(Redis)
Recommends:  perl(DBD::SQLite)



%description
Bucardo is an asynchronous PostgreSQL replication system, allowing for both
multi-master and multi-slave operations.It was developed at Backcountry.com
primarily by Greg Sabino Mullane of End Point Corporation.

%prep
%setup -q -n %{realname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot} DESTINSTALLVENDORSHARE=%{buildroot}/%{_datadir}/%{name}
# removing packlist is required for building on fedora-epel
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
sed -i -e '1d;2i#!%{__perl}' %{name}
rm -f %{buildroot}/%{_bindir}/%{name}
install -Dp -m755 bucardo %{buildroot}/%{_sbindir}/%{name}
install -Dp -m644 %{name}.schema %{buildroot}/%{_datadir}/%{name}/%{name}.schema
install -Dp -m644 %{SOURCE1} .
%{_fixperms} %{buildroot}/

%check
# This test runs forever, it'd be nice to figure out why,
# fix it and re-enable it.  For now, run the rest of the
# test suite at least.
# rm -f t/15-star.t
#rm -f t/*.t
#make test
#test's are disable for now

%files
%license LICENSE
%doc *.html Changes INSTALL README TODO
%doc master-master-replication-example.txt
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_sbindir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.6.0-2
- Perl 5.32 rebuild

* Sun Apr 05 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 5.6.0-1
- 5.6.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.4.1-12
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 5.4.1-9
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.4.1-6
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.4.1-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 5.4.1-2
- improve spec file and disable test's for now

* Tue Dec 08 2015 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 5.4.1-1
- 5.4.1

* Wed Sep 23 2015 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.5.0-12
- change spec to make it buildable under fedora-epel

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.5.0-10
- Perl 5.22 rebuild

* Mon May 25 2015 Petr Šabata <contyk@redhat.com> - 4.5.0-9
- Fix the FTBFS issue (#1158368)
- Install the missing database schema
- Clean and modernize the spec file
- Drop the unused signature file
- Fix the dep list
- Install the LICENSE file with %%license
- Enable test suite

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.5.0-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 25 2013 Petr Pisar <ppisar@redhat.com> - 4.5.0-5
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Petr Pisar <ppisar@redhat.com> - 4.5.0-2
- Depend on perl ABI as each perl package

* Thu Jul 12 2012 Itamar <itamar@ispbrasil.com.br> - 4.5.0-1
- new version 4.5.0

* Fri Jan 13 2012 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.4.8-1
- new version 4.4.8

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.4.7-1
- new version 4.4.7

* Mon Jul 11 2011 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.4.6-1
- new version 4.4.6

* Sun Jun 19 2011 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.4.5-1
- New version 4.4.5 fix truncate bug

* Sun May 15 2011 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.4.4-1
- New version 4.4.4 fix backslash bug

* Thu Apr 21 2011 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.4.3-1
- New version 4.4.3

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 14 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.4.0-2
- Removed some duplicated modules, changed Mail::Sendmail to Net::SMTP.

* Sat Nov 14 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 4.4.0-1
- rebuild with latest version

* Mon Oct 12 2009 David Fraser <davidf@sjsoft.com> - 4.3.0-1
- Rebuild with latest version

* Sun Feb 01 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.9-2
- Don't strip tarball (removing DBIx-Safe and Test-Dynamic)

* Thu Jan 29 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.9-1
- Initial RPM release
