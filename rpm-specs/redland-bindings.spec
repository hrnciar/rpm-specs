Name:           redland-bindings
Version:        1.0.16.1
Release:        38%{?dist}
Summary:        Redland RDF Application Framework API Bindings

License:        LGPLv2+ or GPLv2+ or ASL 2.0
URL:            http://librdf.org/
Source:         http://download.librdf.org/source/%{name}-%{version}.tar.gz
# Restore compatibility with PHP 7, bug #1350620
Patch0:         redland-bindings-1.0.16.1-Add-PHP-7-support.patch

%define         redland_ver 1.0.15
%define         redland_version %(pkg-config --modversion redland 2>/dev/null || echo %{redland_ver})

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  redland-devel >= %{redland_ver}
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Add-PHP-7-support.patch breaks older PHP, bug #1350620
BuildRequires:  php-devel >= 7
BuildRequires:  ruby
BuildRequires:  ruby-devel
# ruby testsuite
BuildRequires:  rubygem(test-unit)
BuildRequires:  swig

%description
Redland is a library that provides a high-level interface for RDF
(Resource Description Framework) implemented in an object-based API.
It is modular and supports different RDF/XML parsers, storage
mechanisms and other elements. Redland is designed for applications
developers to provide RDF support in their applications as well as
for RDF developers to experiment with the technology.

%package        common
Summary:        Redland RDF Application Framework API Bindings

%description common
Redland is a library that provides a high-level interface for RDF
(Resource Description Framework) implemented in an object-based API.
It is modular and supports different RDF/XML parsers, storage
mechanisms and other elements. Redland is designed for applications
developers to provide RDF support in their applications as well as
for RDF developers to experiment with the technology.


%{!?perl_vendorarch: %define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)}
%define perlver %(eval "`%{__perl} -V:version`"; echo $version)

%package -n     perl-redland
Summary:        Perl modules for the Redland RDF library
Requires:       redland >= %{redland_version}
Requires:       redland-bindings-common
Requires:       perl(:MODULE_COMPAT_%{perlver})

%description -n perl-redland
The perl-redland package contains the parts of Redland that provide
an interface to Perl.

%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)
%if %{php_apiver}
%{!?php_extdir: %{expand: %%global php_extdir %(php-config --extension-dir)}}
%if "%{php_version}" < "5.6"
%global ini_name     redland.ini
%else
%global ini_name     40-redland.ini
%endif
%else
# Use dummy values when building source package to prevent from RPM warnings
%global php_zend_api 0
%global php_core_api 0
%endif

%package -n     php-redland
Summary:        PHP modules for the Redland RDF library
Requires:       redland >= %{redland_version}
Requires:       redland-bindings-common
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

%description -n php-redland
The php-redland package contains the parts of Redland that provide
an interface to PHP.


%package -n     ruby-redland
Summary:        Ruby modules for the Redland RDF library
Requires:       redland >= %{redland_version}
Requires:       redland-bindings-common
Requires:       ruby(release)

%description -n ruby-redland
The ruby-redland package contains the parts of Redland that provide
an interface to Ruby.

%prep
%setup -q
%patch0 -p1

# Force swig to regenerate the wrapper
rm -f php/redland_wrap.c php/php_redland.h
rm -f perl/CORE_wrap.c

cat <<'EOF' >php/%{ini_name}
; Enable the 'Redland' extension module
extension=redland.so
EOF


%build
autoreconf
%configure \
  --without-python \
  --with-perl \
  --with-php \
  --with-ruby --with-ruby-arch-install-dir-variable=vendorarchdir \
  --with-ruby-install-dir=%{ruby_vendorarchdir}

cd perl
make MAKE_PL_OPTS="PREFIX=/usr INSTALLDIRS=vendor" %{?_smp_mflags}
cd ..

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

cd perl
make install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT PREFIX=/usr INSTALLDIRS=vendor
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
# by default CORE.so gets 0555, fix it
find $RPM_BUILD_ROOT -type f -name '*.so' -exec chmod 755 {} \;
# if we want this as documentation, it cannot be executable
chmod -x example.pl
cd ..

cd php
# the php bindings need DESTDIR
make DESTDIR=$RPM_BUILD_ROOT install
# .so's need to be executable for rpm to strip them
chmod +x $RPM_BUILD_ROOT%{php_extdir}/redland.so
# configuration file
install -D %{ini_name} $RPM_BUILD_ROOT%{php_inidir}/%{ini_name}
cd ..

cd ruby
# the ruby bindings need DESTDIR
make DESTDIR=$RPM_BUILD_ROOT install
# .so's need to be executable for rpm to strip them
chmod +x $RPM_BUILD_ROOT%{ruby_vendorarchdir}/redland.so
cd ..

%check
# make check hints at some ruby fail, not sure if that's a real problem
# or something specific to the tests themselves -- rex
make check ||:
%{_bindir}/php \
    -n -d extension_dir=${RPM_BUILD_ROOT}%{php_extdir} \
    -d extension=redland.so \
    -m | grep redland

%files common
%doc AUTHORS COPYING COPYING.LIB ChangeLog
%doc LICENSE.txt NEWS README TODO
%doc LICENSE.html NEWS.html README.html TODO.html
%doc LICENSE-2.0.txt NOTICE
%doc RELEASE.html

%files -n perl-redland
%doc docs/perl.html
%attr(664,root,root) %doc perl/example.pl
%{perl_vendorarch}/auto/
%{perl_vendorarch}/RDF/
%{_mandir}/man3/RDF::Redland*.3pm*

%files -n php-redland
%doc docs/php.html
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/redland.so

%files -n ruby-redland
%doc docs/ruby.html
%doc ruby/example.rb

%{ruby_vendorarchdir}/redland.so
%{ruby_vendorarchdir}/rdf

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.16.1-37
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.16.1-35
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.16.1-33
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.16.1-31
- F-30: rebuild against ruby26

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.16.1-30
- Remove Python 2 subpackage python2-redland (#1628780)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.16.1-28
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.16.1-26
- F-28: rebuild for ruby25

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.16.1-25
- Rename python subpackage to python2-redland

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.0.16.1-24
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Tue Sep 26 2017 Petr Pisar <ppisar@redhat.com> - 1.0.16.1-23
- Fix building source package (bug #1482157)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Petr Pisar <ppisar@redhat.com> - 1.0.16.1-20
- Build against PHP 7 (bug #1350620)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.16.1-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16.1-17
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.16.1-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 1.0.16.1-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.16.1-12
- Perl 5.22 rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.16.1-11
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.16.1-10
- Perl 5.20 rebuild
- Regenerated the perl wrapper

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Remi Collet <rcollet@redhat.com> - 1.0.16.1-8
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add PHP extension configuration file

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Vít Ondruch <vondruch@redhat.com> - 1.0.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.16.1-4
- Perl 5.18 rebuild

* Tue Mar 26 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.16.1-3
- rebuild (for fixed redland)

* Tue Mar 26 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.16.1-2
- BR: rubygem(minitest) rubygem(test-unit)

* Tue Feb 19 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.16.1-1
- 1.0.16.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.0.14.1-2
- Perl 5.16 rebuild

* Tue Mar 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.14.1-1
- 1.0.14.1
- move all patch/autofoo ops to %%prep
- %%check: run 'make check'

* Wed Feb 29 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.13.1-6
- Proper rebuilt for Ruby 1.9.3 (fix file placement and ruby(abi)).

* Mon Feb 20 2012 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.13.1-5
- require the right ruby abi

* Wed Feb 15 2012 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.13.1-4
- rebuild for new ruby with a patch

* Sat Jan 21 2012 Remi Collet <remi@fedoraproject.org> - 1.0.13.1-3
- build against PHP 5.4
- provided php wrapper is unusable, regenerate it
- fix php ABI check

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.13.1-1
- Updated for redland 1.0.14

* Tue Jun 21 2011 Petr Sabata <contyk@redhat.com> - 1.0.11.1-7
- Perl mass rebuild

* Thu Mar 03 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.11.1-6
- Renamed base package to common, as suggested by Orcan.

* Mon Feb 07 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.11.1-5
- Clarify license based on https://github.com/dajobe/redland-bindings/commit/e5cf494c69f541ad3d357b69c821a85865dbdbc4
- More changes from package review
- Incorporate upstream ruby patch
- Incorporate upstream python patch

* Sat Jan 22 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.11.1-4
- Updates after package review
- Adhere to ruby/python/php macros and guidelines
- Add comments linking to upstream patches
- Support parallel make
- Remove brp-python-bytecompile
- Remove unneeded BuildRequires
- Change php module to executable so it gets stripped
- Change permissions on example for documentation

* Mon Dec 20 2010 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.11.1-3
- make sure the requires require our redland version or later.

* Wed Dec 01 2010 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.11.1-2
- build --with-redland=system so we don't need to patch configure

* Sat Nov 27 2010 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.11.1-1
- update to newest version for F-14, building against redland 1.0.12

* Tue Apr 06 2010 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.7.1-2
- fix centos detection

* Thu May 22 2008 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.7.1-1
- update to newest version

* Sat Jun 17 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.4.1-2
- added db4-devel
- added patches for python and ruby sitearch, so 64-bit build works
- use brb-python-bytecompile so we have .pyc and .pyo on < FC5
- fix up perl installed files
- added php bindings

* Sun May 14 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.4.1-1
- new release
- added openssl-devel, postgresql-devel,sqlite-devel and mysql-devel
  buildrequires

* Sat Apr 08 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.3.1-1
- update to latest release

* Sat Apr 08 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.2.1-1
- packaged for Fedora Extras

* Wed Nov 3 2004  Dave Beckett <dave.beckett@bristol.ac.uk>
- Added redland-ruby include wrapper classes
- BuildRequires: perl, python2-devel, ruby-devel

* Tue Nov 2 2004   Dave Beckett <dave.beckett@bristol.ac.uk>
- License now LGPL/Apache 2
- Added LICENSE-2.0.txt and NOTICE

* Mon Jul 19 2004  Dave Beckett <dave.beckett@bristol.ac.uk>
- split redland to give redland-bindings
- requires redland 0.9.17

* Mon Jul 12 2004  Dave Beckett <dave.beckett@bristol.ac.uk>
- put /usr/share/redland/Redland.i in redland-devel

* Wed May  5 2004  Dave Beckett <dave.beckett@bristol.ac.uk>
- require raptor 1.3.0
- require rasqal 0.2.0

* Fri Jan 30 2004  Dave Beckett <dave.beckett@bristol.ac.uk>
- require raptor 1.2.0
- update for removal of python distutils
- require python 2.2.0+
- require perl 5.8.0+
- build and require mysql
- do not build and require threestore

* Sun Jan 4 2004  Dave Beckett <dave.beckett@bristol.ac.uk>
- added redland-python package
- export some more docs

* Mon Dec 15 2003 Dave Beckett <dave.beckett@bristol.ac.uk>
- require raptor 1.1.0
- require libxml 2.4.0 or newer
- added pkgconfig redland.pc
- split redland/devel package shared libs correctly

* Mon Sep 8 2003 Dave Beckett <dave.beckett@bristol.ac.uk>
- require raptor 1.0.0

* Thu Sep 4 2003 Dave Beckett <dave.beckett@bristol.ac.uk>
- added rdfproc

* Thu Aug 28 2003 Dave Beckett <dave.beckett@bristol.ac.uk>
- patches added post 0.9.13 to fix broken perl UNIVERSAL::isa

* Thu Aug 21 2003 Dave Beckett <dave.beckett@bristol.ac.uk>
- Add redland-db-upgrade.1
- Removed duplicate perl CORE shared objects

* Sun Aug 17 2003 Dave Beckett <dave.beckett@bristol.ac.uk>
- Updates for new perl module names.

* Tue Apr 22 2003 Dave Beckett <dave.beckett@bristol.ac.uk>
- Updated for Redhat 9, RPM 4

* Wed Feb 12 2003 Dave Beckett <dave.beckett@bristol.ac.uk>
- Updated for redland 0.9.12

* Fri Jan 4 2002 Dave Beckett <dave.beckett@bristol.ac.uk>
- Updated for new Perl module names

* Fri Sep 14 2001 Dave Beckett <dave.beckett@bristol.ac.uk>
- Added shared libraries

