Name:           clive
Version:        2.3.3
Release:        25%{?dist}
Summary:        Video extraction tool for user-uploaded video hosts

License:        GPLv3+
URL:            http://clive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::Base)  perl(Getopt::ArgvFile) perl(JSON::XS) perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version)) perl(Getopt::ArgvFile) perl(JSON::XS) perl(version) quvi curl

%description
clive is a video extraction tool for user-uploaded video hosts such as Youtube,
Google Video, Dailymotion, Guba, Metacafe and Sevenload.
It can be chained with 3rd party tools for subsequent video
re-encoding and and playing.

%prep
%setup -q
# use the correct quvi call
sed -i -e '15s/^.//' -e '13s/^/#/' examples/cliverc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
install -p -m 644 examples/cliverc  $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/config
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
export NO_INTERNET=1
make test


%files
%doc ChangeLog COPYING README examples/cliverc
%dir %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%config(noreplace) %{_sysconfdir}/%{name}/config


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.3-24
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.3-21
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.3-18
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.3-15
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.3-13
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.3-10
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.3-9
- Perl 5.20 rebuild

* Sun Jun 08 2014 Filipe Rosset <rosset.filipe@gmail.com> - 2.3.3-8
- rebuilt + spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 2.3.3-5
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 2.3.3-2
- Perl 5.16 rebuild

* Thu Mar 29 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.3.3-1
- Update to 2.3.3
* Mon Oct 24 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.3.2-1
- Update to 2.3.2
* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.3.1.1-2
- Perl mass rebuild
* Fri Jun 24 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.3.1.1-1
- Update to 2.3.1.1
* Sun May 22 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.3.0.3-1
- Update to 2.3.0.3
* Sun Mar 20 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.3.0.2-1
- Update to 2.3.0.2
* Tue Feb 15 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.3.0.1-1
- Update to 2.3.0.1
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sun Jan 23 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.22-1
- Update to 2.2.22
* Tue Dec 14 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.19-1
- Update to 2.2.19
* Tue Nov 30 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.18-1
- Update to 2.2.18
* Sun Nov  7 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.17-1
- Update to 2.2.17
* Wed Sep 29 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.16-1
- Update to 2.2.16
* Fri Sep 10 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.15-1
- Update to 2.2.15
* Sun Sep  5 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.14-1
- Update to 2.2.14
* Wed Aug 25 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.13-1
- Update to 2.2.13
- Add perl-URI require
* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.2.11-2
- Mass rebuild with perl-5.12.0
* Sat Apr 17 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.11-1
- Update to 2.2.11
* Mon Mar 29 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.10-1
- Update to 2.2.10
- Now using NO_INTERNET env var for tests
* Thu Feb 18 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.9-1
- Update to 2.2.9
* Fri Dec 18 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.8-1
- Update to 2.2.8
* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.2.7-2
- rebuild against perl 5.10.1
* Thu Oct  1 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.7-1
- Update to 2.2.7
* Sat Sep 19 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.6-1
- Update to 2.2.6
* Sun Aug 16 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.5-1
- Update to 2.2.5
* Sat Aug  8 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.4-2
- Add perl(Getopt::ArgvFile) as a Require
* Mon Aug  3 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.4-1
- Update to 2.2.4
- Add perl-Class-Singleton as an explicit require
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Sat Jul 11 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.2-1
- Rebuild for 2.2.2
- Now using Makefile.PL install type
* Mon Jun 22 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.2.1-1
- Rebuild for 2.2.1
* Tue May 26 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.14-1
- Rebuild for 2.1.14
* Sat May  9 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.12-1
- Rebuild for 2.1.12
* Wed May  6 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.11-1
- Rebuild for 2.1.11
* Sat Apr 18 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.10-2
- Add explicit dependencies
* Sat Apr  4 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.10-1
- Rebuild for 2.1.10
* Sat Mar 28 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.9-1
- Rebuild for 2.1.9
* Mon Mar 16 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.7-1
- Rebuild for 2.1.7
- Add Term::ReadKey explicit require
* Fri Feb 27 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.6-1
- Rebuild for 2.1.6
- Makefile usage
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Feb  4 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.4-1
- Rebuild for 2.1.4
* Thu Jan 15 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.3-1
- Rebuild for 2.1.3
- License update
* Wed Dec 31 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.2-1
- Rebuild for 2.1.2
- URLs update
* Wed Dec  3 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 2.1.0-1
- Rebuild for 2.1.0
* Sun Nov  2 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.0.2-1
- Rebuild for 1.0.2
* Wed Jul 30 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.20-1
- rebuild for 0.4.20
- licence is now GPLv3+
* Wed Jul 23 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.19-1
- rebuild for 0.4.19
* Wed Jul 16 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.18-1
- rebuild for 0.4.18
* Sun Jun 29 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.17-1
- rebuild for 0.4.17
* Fri Jun 27 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.16-3
- non-macro usage for commands
* Wed Jun 25 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.16-2
- Licence updated
- smp_mflags removed
* Sat Jun 21 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.16-1
- Rebuild for 0.4.16 version
* Tue Jun 10 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.14-3
- add sed to use python_sitelib for Makefile
* Mon Jun  9 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.14-2
- Removed ffmpeg dependancy
* Sun Jun  8 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.14-1
- Initial build

