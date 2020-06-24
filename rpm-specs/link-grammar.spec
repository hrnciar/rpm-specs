Summary: A full-service natural language dependency parser
Name: link-grammar
Version: 5.8.0
Release: 2%{?dist}
License: LGPLv2+
Source: http://www.abisource.com/downloads/link-grammar/%{version}/link-grammar-%{version}.tar.gz
URL: http://abisource.com/projects/link-grammar/
BuildRequires: hunspell-devel, java-devel, jpackage-utils, libedit-devel, ant, perl-devel, python3-devel
BuildRequires: perl-generators, minisat2-devel, autoconf, automake, libtool, autoconf-archive, gcc-c++

%description
A full-service natural language dependency parser for
English and Russian, with prototypes for other assorted languages.

%package devel
Summary: Support files necessary to compile applications with liblink-grammar
Requires: link-grammar = %{version}-%{release}

%description devel
Libraries, headers, and support files needed for using liblink-grammar.

%package java
Summary: Java libraries for liblink-grammar
Requires: java-headless >= 1:1.6.0
Requires: jpackage-utils
Requires: link-grammar = %{version}-%{release}

%description java
Java libraries for liblink-grammar

%package java-devel
Summary: Support files necessary to compile Java applications with liblink-grammar
Requires: link-grammar-java = %{version}-%{release}
Requires: link-grammar-devel = %{version}-%{release}

%description java-devel
Libraries for developing Java components using liblink-grammar.

%package perl
Summary: Perl libraries for liblink-grammar
Requires: perl-interpreter
Requires: link-grammar = %{version}-%{release}

%description perl
Perl libraries for liblink-grammar

%package python3
Summary: Python 3 libraries for liblink-grammar
Requires: link-grammar = %{version}-%{release}

%description python3
Python 3 libraries for liblink-grammar

%prep
%setup -q

%build
# help configure find jni.h
export JAVA_HOME=%{java_home}
autoreconf -if
%configure --disable-static --enable-pthreads --disable-aspell --enable-perl-bindings
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
#make
# currently the build system can not handle smp_flags properly
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT/%{_datadir}/java/linkgrammar-%{version}.jar $RPM_BUILD_ROOT/%{_datadir}/java/linkgrammar.jar
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/perl5/
mv $RPM_BUILD_ROOT/usr/local/lib*/perl5/* $RPM_BUILD_ROOT/%{_libdir}/perl5/
find $RPM_BUILD_ROOT/%{_libdir}/ -name '*.la' | xargs rm -f


%files
%license LICENSE
%doc AUTHORS
%{_bindir}/*
%{_libdir}/liblink-grammar.so.*
%{_datadir}/link-grammar
%{_mandir}/man1/link-parser.1*

%files devel
%{_libdir}/liblink-grammar.so
%{_libdir}/pkgconfig/link-grammar.pc
%{_includedir}/link-grammar

%files java
%{_libdir}/liblink-grammar-java.so.*
%{_javadir}/linkgrammar.jar

%files java-devel
%{_libdir}/liblink-grammar-java.so

%files perl
%{_libdir}/perl5/*

%files python3
%{python3_sitelib}/linkgrammar*

%ldconfig_scriptlets

%ldconfig_scriptlets java

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.8.0-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 5.8.0-1
- 5.8.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.7.0-1
- 5.7.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.6.2-4
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Jan Beran <jaberan@redhat.com> - 5.6.2-3
- Avoid using compression format while listing manpages

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.6.2-1
- 5.6.2

* Tue May 28 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.6.1-1
- 5.6.1

* Wed Mar 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.6.0-1
- 5.6.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 5.5.1-5
- rebuild for hunspell 1.7.2

* Thu Oct 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.5.1-2
- Drop python2.

* Mon Jul 30 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.5.1-1
- 5.5.1.

* Sun Jul 22 2018 Niels de Vos <ndevos@redhat.com> - 5.5.0-4
- Add gcc-c++ to BuildRequires (#1604705)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-2
- Rebuilt for Python 3.7

* Tue May 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.5.0-1
- 5.5.0

* Mon Mar 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.4.4-1
- 5.4.4

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 5.4.3-1
- 5.4.3

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> - 5.4.2-2
- rebuild for hunspell 1.6.2

* Fri Oct 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 5.4.2-1
- 5.4.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 5.4.0-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Gwyn Ciesla <limburgher@gmail.com> - 5.4.0-1
- 5.4.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 5.3.16-3
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Apr 17 2017 Gwyn Ciesla <limburgher@gmail.com> - 5.3.16-1
- 5.3.16

* Mon Feb 13 2017 Jon Ciesla <limburgher@gmail.com> - 5.3.15-1
- 5.3.15

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Jon Ciesla <limburgher@gmail.com> - 5.3.14-1
- 5.3.14

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.3.13-3
- Rebuild for Python 3.6

* Tue Dec 13 2016 Caolán McNamara <caolanm@redhat.com> - 5.3.13-2
- rebuild for latest hunspell

* Mon Nov 21 2016 Jon Ciesla <limburgher@gmail.com> - 5.3.13-1
- 5.3.13.

* Fri Nov 18 2016 Jon Ciesla <limburgher@gmail.com> - 5.3.12-1
- 5.3.12.
- Ship Python2 bindings.

* Wed Sep 28 2016 Jon Ciesla <limburgher@gmail.com> - 5.3.11-2
- Ship Python3 bindings.
- Spec cleanup.

* Tue Sep 27 2016 Jon Ciesla <limburgher@gmail.com> - 5.3.11-1
- Fix minisat conflict

* Thu Sep 15 2016 Jon Ciesla <limburgher@gmail.com> - 5.3.10-1
- 5.3.10.

* Mon Aug 29 2016 Jon Ciesla <limburgher@gmail.com> - 5.3.9-1
- 5.3.9.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.0.8-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 5.0.8-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Jon Ciesla <limburgher@gmail.com> - 5.0.8-2
- Made summary and description more accurate per Linas Vepstas.

* Tue Jun 24 2014 Jon Ciesla <limburgher@gmail.com> - 5.0.8-1
- Latest upstream to fix FTBFS BZ 1106100, License change.
- Include JAVA_HOME from Yaakov Selkowitz's patch.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Jon Ciesla <limburgher@gmail.com> - 4.8.6-2
- Switch to java-headless, BZ 1068372.

* Wed Feb 12 2014 Jon Ciesla <limburgher@gmail.com> - 4.8.6-1
- 4.8.6.
- Drop versioned java jars, BZ 1022140.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Jon Ciesla <limburgher@gmail.com> - 4.7.11-2
- Migrate from aspell to hunspell, BZ 961933.

* Mon Apr 01 2013 Johannes Lips <Johannes.Lips@googlemail.com> - 4.7.11-1
- Update to recent upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Johannes Lips <Johannes.Lips@googlemail.com> - 4.7.9-1
- Update to recent upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 02 2011 Johannes Lips <Johannes.Lips@googlemail.com> - 4.7.4-1
- Update to recent upstream version
- added libgcj-devel as build requirement

* Fri May 28 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 4.6.7-3
- fix BuildRequires

* Fri May 28 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 4.6.7-2
- have the java-devel package Require the -devel package

* Fri May 28 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 4.6.7-1
- update to 4.6.7
- drop static libs
- get rid of rpath
- fix man page ownership
- add java subpackages
- fix defattr invocations

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.3.5-3
- fix license tag

* Thu Jul 10 2008 Marc Maurer <uwog@abisource.com> 4.3.5-2
- Move the man-page from -devel to the main package

* Thu Jul 10 2008 Marc Maurer <uwog@abisource.com> 4.3.5-1
- New upstream version, fixes bug 434650
- Update URL
- Package man-page

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.2.5-2
- Autorebuild for GCC 4.3

* Mon Nov 12 2007 Marc Maurer <uwog@uwog.net> 4.2.5-1
- New upstream version, fixes bug 371221.

* Mon Sep 11 2006 Marc Maurer <uwog@abisource.com> 4.2.2-2.fc6
- Rebuild for FC6

* Wed Apr 12 2006 Marc Maurer <uwog@abisource.com> 4.2.2-1
- New upstream version

* Mon Apr 10 2006 Marc Maurer <uwog@abisource.com> 4.2.1-2
- Rebuild

* Mon Apr 10 2006 Marc Maurer <uwog@abisource.com> 4.2.1-1
- New upstream version

* Wed Feb 15 2006 Marc Maurer <uwog@abisource.com> 4.1.3-4
- Rebuild for Fedora Extras 5
- Use %%{?dist} in the release name

* Wed Aug 10 2005 Marc Maurer <uwog@abisource.com> - 4.1.3-3
- Set the buildroot to the standard Fedora buildroot
- Make the package own the %%{_datadir}/link-grammar
  directory (thanks go to Aurelien Bompard for both issues)

* Wed Aug 10 2005 Marc Maurer <uwog@abisource.com> - 4.1.3-2
- Remove epoch
- Make rpmlint happy

* Sun Aug 7 2005 Marc Maurer <uwog@abisource.com> - 1:4.1.3-1
- Initial version
