%define         ver 2.7.0
%define         PatchLevel 0

Name:           perl-XML-Xerces
Version:        %{ver}_%{PatchLevel}
Release:        47%{?dist}
Summary:        Perl API to Xerces XML parser

License:        ASL 2.0
URL:            http://xerces.apache.org/xerces-p/
Source0:        http://www.apache.org/dist/xerces/p/XML-Xerces-%{ver}-%{PatchLevel}.tar.gz
Patch0:         %{name}-%{ver}-%{PatchLevel}-perl510.patch
Patch1:         cflags5.14.patch

BuildRequires:  gcc-c++
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Env)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  xerces-c27-devel >= %{ver}
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(lib)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
XML::Xerces is the Perl API to the Apache project's Xerces XML parser. It is
implemented using the Xerces C++ API, and it provides access to most of the C++
API from Perl.
Because it is based on Xerces-C, XML::Xerces provides a validating XML parser
that makes it easy to give your application the ability to read and write XML
data. Classes are provided for parsing, generating, manipulating, and
validating XML documents. XML::Xerces is faithful to the XML 1.0 recommendation
and associated standards (DOM levels 1, 2, and 3, SAX 1 and 2, Namespaces, and
W3C XML Schema). The parser provides high performance, modularity, and
scalability, and provides full support for Unicode.
XML::Xerces implements the vast majority of the Xerces-C API. The exception is
some functions in the C++ API which either have better Perl counterparts (such
as file I/O) or which manipulate internal C++ information that has no role in
the Perl module. 


%prep
%setup -q -n XML-Xerces-%{ver}-%{PatchLevel}
%patch0 -p1
%patch1 -p1

%build
export XERCESCROOT=%{_prefix}
export XERCES_LIB=%{_libdir}/xerces-c-%{ver}/
export XERCES_INCLUDE=%{_includedir}/xercesc-%{ver}
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes FAQ LICENSE README TODO docs samples
%{perl_vendorarch}/XML
%{perl_vendorarch}/auto/XML
%exclude %{perl_vendorarch}/auto/Handler


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0_0-47
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0_0-44
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Xavier Bachelot <xavier@bachelot.org> - 2.7.0_0-42
- Change BR: gcc to BR: gcc-c++ (FTBFS RHBZ#1606813).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0_0-40
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0_0-36
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0_0-34
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0_0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0_0-31
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0_0-30
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Xavier Bachelot <xavier@bachelot.org> - 2.7.0_0-27
- Fix Source0 URL.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.7.0_0-25
- Perl 5.18 rebuild
- Specify all dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 2.7.0_0-22
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.7.0_0-20
- Perl mass rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.7.0_0-19
- Perl mass rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.7.0_0-18
- Perl mass rebuild
- patch CFLAGS, clean spec

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.7.0_0-16
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.7.0_0-15
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.7.0_0-14
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0_0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Mar  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.7.0_0-11
- be more specific as to the library dir.

* Sat Mar  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.7.0_0-10
- tell it where the compat bits are

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.7.0_0-9
- ok, so we can't really lie to it. Use the compat BR instead.
- patch for perl 5.10 change

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.7.0_0-8
- tell the code that 2.8.0 is fine

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.7.0_0-7
- Rebuild for new perl

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.7.0_0-6
- Autorebuild for GCC 4.3

* Mon Feb 11 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.0_0-5
- Relax BR: on xerces-c-devel a bit.
- Rebuild for new xerces-c.

* Sat Jan 12 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.0_0-4
- Remove '|| :' from %%check section.

* Thu Dec 27 2007 Xavier Bachelot <xavier@bachelot.org> - 2.7.0_0-3
- Fix License: tag.
- Fix Source: URL. 
- Add strict BR: on xerces-c-devel.

* Sat Dec 22 2007 Xavier Bachelot <xavier@bachelot.org> - 2.7.0_0-2
- Clean up spec.

* Wed Aug 09 2006 Xavier Bachelot <xavier@bachelot.org> - 2.7.0_0-1
- Initial build.
