Name:           perl-Workflow
Version:        1.48
Release:        5%{?dist}
Summary:        Simple, flexible system to implement work-flows
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Workflow
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASBN/Workflow-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
# glibc-common for iconv
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor) >= 0.18
BuildRequires:  perl(Class::Factory) >= 1
BuildRequires:  perl(Class::Observable) >= 1.04
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime) >= 0.15
BuildRequires:  perl(DateTime::Format::Strptime) >= 1
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::Mock) >= 0.1
BuildRequires:  perl(DBI)
BuildRequires:  perl(English)
BuildRequires:  perl(Exception::Class) >= 1.1
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Log::Dispatch) >= 2
BuildRequires:  perl(Log::Log4perl) >= 0.34
BuildRequires:  perl(Safe)
BuildRequires:  perl(XML::Simple) >= 2

# tests
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Env)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

# optional test #1
BuildRequires:  perl(Data::UUID)
# optional test #2 -- not in Fedora yet
#BuildRequires:  perl(SPOPS)

#Requires:       perl(Class::Accessor) >= 0.18
#Requires:       perl(Class::Factory) >= 1
#Requires:       perl(Class::Observable) >= 1.04
#Requires:       perl(DateTime) >= 0.15
#Requires:       perl(DateTime::Format::Strptime) >= 1
#Requires:       perl(DBD::Mock) >= 0.1
#Requires:       perl(Exception::Class) >= 1.1
#Requires:       perl(Log::Dispatch) >= 2
#Requires:       perl(Log::Log4perl) >= 0.34
#Requires:       perl(Test::Exception)
#Requires:       perl(XML::Simple) >= 2

Requires:       perl(:MODULE_COMPAT_%(eval "`/usr/bin/perl -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude}|perl\\(DBI\\)
%global __requires_exclude %{?__requires_exclude}|perl\\(Data::UUID\\)
%global __requires_exclude %{?__requires_exclude}|perl\\(File::Spec::Functions\\)

%description
The 'Workflow' Perl module implements a standalone work-flow system. It
aims to be simple but flexible and therefore powerful. Each piece of
the work-flow system has a direct and easily stated job, and hopefully
you'll find that you can put the pieces together to create very useful
systems.

%prep
%setup -q -n Workflow-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 README > README.utf8
mv README.utf8 README

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
# note: these are a little noisy.
./Build test

%files
%doc Changes README TODO doc/ eg/ struct/ 
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-4
- Perl 5.32 rebuild

* Fri Mar 13 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-3
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.48-1
- Update to 1.48
- Replace calls to %%{__perl} with /usr/bin/perl
- Use %%license to tag the LICENSE files

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-2
- Perl 5.30 re-rebuild updated packages

* Sun Jun 02 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.46-1
- Update to 1.46

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-7
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.45-1
- Update to 1.45

* Sat Jun 10 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.43-1
- Update to 1.43

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.41-2
- Perl 5.20 rebuild

* Sun Aug 17 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.41-1
- Update to 1.41

* Sun Jun 08 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.40-1
- Update to 1.40

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.39-1
- Update to 1.39

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 1.38-2
- Perl 5.18 rebuild

* Sat Jul 13 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.38-1
- Update to 1.38

* Sun Jul 07 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.37-1
- Update to 1.37

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 11 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 1.35-1
- Update to 1.35
- Remove BuildRoot and Group definitions (no longer used)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 1.34-2
- Perl 5.16 rebuild

* Fri Feb 03 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.34-1
- Update to 1.34
- Clean up spec file
- Add perl default filter
- Move the req and prov filters inline

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.32-8
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.32-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.32-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.32-1
- update to 1.32
- update br's to latest required

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.26-4
Rebuild for new perl

* Wed Apr 25 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.26-3
- bump

* Sat Apr 07 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.26-2
- add BR's for optional tests

* Sat Mar 10 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.26-1
- Specfile autogenerated by cpanspec 1.70.
