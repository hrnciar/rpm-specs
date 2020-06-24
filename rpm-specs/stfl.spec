Name:           stfl
Version:        0.22
Release:        35%{?dist}
Summary:        The Structured Terminal Forms Language/Library

License:        LGPLv3+
URL:            http://www.clifford.at/stfl/
Source0:        http://www.clifford.at/stfl/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  swig

%description
STFL is a library which implements a curses-based widget set for text
terminals.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        perl
Summary:        Perl binding for STFL
Requires:       %{name} = %{version}-%{release}

%description    perl
Perl binding for STFL


%package        ruby
Summary:        Ruby binding for STFL
Requires:       %{name} = %{version}-%{release}
Requires:       ruby(release)

%description    ruby
Ruby binding for STFL.


%prep
%setup -q
## ensures that _stfl.so doesn't end up in lib-dynload
## - http://www.rocklinux.net/pipermail/stfl/2009-June/000113.html
sed -i.path \
 -e '/mkdir.*lib-dynload/d' \
 -e '/cp/s|lib-dynload||' \
 python/Makefile.*
## creates an soname symlink for the shared library
## - http://www.rocklinux.net/pipermail/stfl/2009-June/000114.html
## add the new line needed (the part starting with \n) If you know a better way with sed to do it, please educate me
sed -i.soname \
 -e 's|\(.*ln -fs.*/\)\(libstfl\.so\)$|\1\2\n\1\$(SONAME)|' \
 Makefile
## fixes undefined-non-weak-symbol rpmlint warnings
## - http://www.rocklinux.net/pipermail/stfl/2009-October/000116.html
sed -i.ldflags -e 's|\(-shared\)|\1 \$(LDLIBS)|' Makefile
## fixes libdir for other arch than x86 
## - http://www.rocklinux.net/pipermail/stfl/2009-October/000118.html
sed -i.path -e 's|libdir=.*|libdir=%{_libdir}|' stfl.pc.in
sed -i.cflags -e 's|-Os||' Makefile
# fix paths in Makefile.cfg
sed -i.path -e 's|lib$|%{_lib}|' -e 's|/usr/local$|%{_prefix}|' Makefile.cfg

%build
# building with smp flags causes random failures
export CFLAGS="%{optflags}"
# test with explicit prefix and echo
#make prefix=/usr libdir=%{_lib}
#echo %ruby_sitearch
#echo `ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"] '`
sed -i 's|ruby extconf.rb|ruby extconf.rb --vendor|' ruby/Makefile.snippet

# Parallel build is unstable :/
#make  %{?_smp_mflags}
make


%install
%make_install
# give the shared libraries executable permissions so they get stripped
# also fixes the 0555 permissions on the perl bindings
find %{buildroot} -name '*.so' -exec chmod 755 {} ';'
# perl ignores empty .bs files
find %{buildroot} -name '*.bs' -size 0c -exec rm -f {} ';'
# fedora doesn't ship static libraries
rm -f %{buildroot}%{_libdir}/libstfl.a
## remove unneeded files
rm -f %{buildroot}%{perl_vendorarch}/example.pl
rm -f %{buildroot}%{perl_vendorarch}/auto/stfl/.packlist
rm -f %{buildroot}%{perl_archlib}/perllocal.pod


%ldconfig_scriptlets


%files
%doc README COPYING
%{_libdir}/*.so.0*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/stfl.pc

%files perl
%dir %{perl_vendorarch}/auto/stfl
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/auto/stfl/*

%files ruby
%{ruby_vendorarchdir}/stfl.so


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-35
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-32
- Perl 5.30 rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.22-30
- Subpackage python2-stfl has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-28
- Perl 5.28 rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.22-27
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.22-25
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.22-24
- Python 2 binary package renamed to python2-stfl
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-21
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Vít Ondruch <vondruch@redhat.com> - 0.22-19
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-18
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-17
- Perl 5.24 rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Vít Ondruch <vondruch@redhat.com> - 0.22-15
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-13
- Perl 5.22 rebuild

* Mon Jan 19 2015 Vít Ondruch <vondruch@redhat.com> - 0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-11
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Disable parallel build, since it is unstable.

* Sat Mar 29 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.22-7
- Fix rhbz #993383, spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.22-5
- Perl 5.18 rebuild

* Wed Mar 27 2013 Vít Ondruch <vondruch@redhat.com> - 0.22-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Sun Feb 24 2013 Ben Boeckel <mathstuf@gmail.com> - 0.22-3
- Fix soversion glob

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Ben Boeckel <mathstuf@gmail.com> - 0.22-1
- Update to 0.22

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.21-18
- Perl 5.16 rebuild

* Wed Feb 08 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.21-17
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.21-15
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.21-14
- Perl 5.14 mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Dan Horák <dan[at]danny.cz> 0.21-12
- prefix/libdir handling is broken in the Makefile chains

* Tue Sep 07 2010 thomas Janssen <thomasj@fedoraproject.org 0.21-11
- find out what FTBFS

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.21-10
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.21-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.21-8
- rebuild against perl 5.10.1

* Tue Oct 20 2009 Thomas Janssen <thomasj@fedoraproject.org> 0.21-7
- Removed empty %%doc
- Changed sed commands

* Tue Oct 06 2009 Thomas Janssen <thomasj@fedoraproject.org> 0.21-6
- Changed CFLAGS again

* Tue Oct 06 2009 Thomas Janssen <thomasj@fedoraproject.org> 0.21-5
- Better use of sed
- Fixed CFLAGS
- Use of rm instead of exclude
- Removed empty doc

* Mon Oct 05 2009 Thomas Janssen <thomasj@fedoraproject.org> 0.21-4
- Removed unneeded requires
- Removed dupe docs
- removed patches and make use of sed
- fixed stfl.pc.in for x86_64

* Fri Oct 02 2009 Thomas Janssen <thomasj@fedoraproject.org> 0.21-3
- fixed installed rpmlint output

* Fri Oct 02 2009 Thomas Janssen <thomasj@fedoraproject.org> 0.21-2
- Added Requires: pkgconfig
- Mentioned to upstream the rpmlint warnings
- http://www.rocklinux.net/pipermail/stfl/2009-October/000115.html
- Minor spec changes

* Sun Jun 28 2009 Byron Clark <byron@theclarkfamily.name> 0.21-1
- New upstream release
- Stop placing _stfl.so in lib-dynload
- Add patch to properly create soname symlink for shared lib.

* Wed Jun 10 2009 Byron Clark <byron@theclarkfamily.name> 0.20-5
- Stop using both python_sitelib and python_sitearch
- Modify stfl-pythonpaths.patch to only use python_sitearch

* Sat Jun 6 2009 Byron Clark <byron@theclarkfamily.name> 0.20-4
- Don't explicitly require python and perl

* Thu May 21 2009 Byron Clark <byron@theclarkfamily.name> 0.20-3
- Use the patches that have been sent upstream

* Thu May 21 2009 Byron Clark <byron@theclarkfamily.name> 0.20-2
- Add the minimal docs

* Thu May 21 2009 Byron Clark <byron@theclarkfamily.name> 0.20-1
- Initial release
