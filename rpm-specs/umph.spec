Name:           umph
Version:        0.2.5
Release:        14%{?dist}
Summary:        Command line tool for parsing video links from Youtube feeds

License:        GPLv3+
URL:            http://code.google.com/p/umph/
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Getopt::ArgvFile) perl(XML::DOM)

%description
umph is a command line tool for parsing video links from Youtube feeds,
such as playlists, favorites and uploads. The parsed video links are printed
to the standard output each separated with a newline. 

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
# to avoid useless perllocal.pod file installation
sed -i -e 's/pure_install doc_install/pure_install/' Makefile
# useless file
sed -i -e '/\.packlist/d' Makefile
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT



%files
%doc ChangeLog COPYING README NEWS
%attr(755, -,-) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.2.5-3
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.5-1
- Update to 0.2.5
* Sun Jul 15 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.3-1
- Update to 0.2.3
* Sun Sep  4 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.0-1
- Update to 0.2.0
* Mon Aug 15 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.1.8-2
- Fix license and file section for the man page
* Mon May 23 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.1.8-1
- Initial build

