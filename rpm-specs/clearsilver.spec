%define _hardened_build 1

Name:           clearsilver
Version:        0.10.5
Release:        59%{?dist}
Summary:        Fast and powerful HTML templating system
# Technically, the license is "Neotonic ClearSilver", but it is a copy of 
# ASL 1.1 with the trademarks as the only difference.
License:        ASL 1.1
URL:            http://www.clearsilver.net/
Source0:        http://www.clearsilver.net/downloads/%{name}-%{version}.tar.gz
Patch0:         clearsilver-0.10.5-fedora.patch
Patch1:		clearsilver-0.10.5-regression.patch
Patch2:		clearsilver-0.10.5-CVE-2011-4357.patch
Patch3:		clearsilver-ruby-1.9.patch
Patch4:		clearsilver-ruby-2.2.patch
# GCC 5 compatibility, bug #1190760
Patch5:		clearsilver-0.10.5-gcc5.patch
BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  httpd-devel

%description
ClearSilver is a fast, powerful, and language-neutral HTML template
system.  In both static content sites and dynamic HTML applications,
it provides a separation between presentation code and application
logic which makes working with your project easier.  The design of
ClearSilver began in 1999, and evolved during its use at onelist.com,
egroups.com, and Yahoo! Groups.  Today many other projects and
websites are using it.

%package        devel
Summary:        ClearSilver development package
Provides:	%{name}-static = %{version}-%{release}

%description devel
This package provides needed files to develop extensions
to ClearSilver.

%package     -n perl-%{name}
Summary:        Perl interface to the ClearSilver HTML templating system
BuildRequires:  perl-interpreter
%if 0%{?fedora} > 6
BuildRequires:  perl-devel
BuildRequires:  perl-generators
%endif
%if 0%{?rhel} > 7
BuildRequires:  perl-ExtUtils-MakeMaker
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       %{name}-perl = %{version}-%{release}

%description -n perl-%{name}
%{summary}.

%package     -n ruby-%{name}
Summary:        Ruby interface to the ClearSilver HTML templating system
BuildRequires:  ruby
BuildRequires:  ruby-devel
Provides:       %{name}-ruby = %{version}-%{release}

%description -n ruby-%{name}
%{summary}.

%if 0%{?rhel} > 4
%package     -n java-%{name}
Summary:        Java interface to the ClearSilver HTML templating system
BuildRequires:  java-devel
Provides:       %{name}-java = %{version}-%{release}

%description -n java-%{name}
%{summary}.
%endif

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2
touch configure
sed -i -r 's|(\$\(RUBY\) install.rb config) (--.*)|\1 --rb-dir="$(DESTDIR)%{ruby_vendorlibdir}" --so-dir="$(DESTDIR)%{ruby_vendorarchdir}" \2|' ruby/Makefile

%build
# java does not build on x86_64
%ifarch %{ix86} ppc alpha
%configure \
%if 0%{?rhel} > 4
  --with-java=%{_libdir}/jvm/java \
%endif
  --disable-csharp 
%else
%configure \
  --disable-java \
  --disable-csharp
%endif
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"
cd perl && %{__perl} Makefile.PL INSTALLDIRS=vendor && cd ..

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%ifarch %{ix86} ppc 
%if 0%{?rhel} > 4
install -dm 755 $RPM_BUILD_ROOT%{_libdir}/java
mv $RPM_BUILD_ROOT%{_libdir}{,/java}/libclearsilver-jni.so
mv $RPM_BUILD_ROOT%{_libdir}/clearsilver.jar \
  $RPM_BUILD_ROOT%{_libdir}/java/clearsilver-%{version}.jar
chmod 644 $RPM_BUILD_ROOT%{_libdir}/java/clearsilver-%{version}.jar
ln -s clearsilver-%{version}.jar $RPM_BUILD_ROOT%{_libdir}/java/clearsilver.jar
%endif
%endif

%files
%doc CS_LICENSE INSTALL LICENSE README
%{_bindir}/cs
%{_bindir}/cstest
%{_bindir}/cs_static.cgi
%{_mandir}/man3/*

%files devel
%doc CS_LICENSE LICENSE
%{_includedir}/ClearSilver/
%{_libdir}/libneo_*.a

%files -n perl-clearsilver
%doc CS_LICENSE LICENSE
%defattr(-,root,root,-)
%{perl_vendorarch}/auto/ClearSilver/
%{perl_vendorarch}/ClearSilver.pm

%files -n ruby-clearsilver
%doc CS_LICENSE LICENSE
%defattr(-,root,root,-)
%{ruby_vendorarchdir}/hdf.so
%{ruby_vendorlibdir}/neo.rb

%ifarch %{ix86} ppc alpha
%if 0%{?rhel} > 4
%files -n java-clearsilver
%doc CS_LICENSE LICENSE
%defattr(-,root,root,-)
%{_libdir}/java/*clearsilver*
%endif
%endif


%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.5-59
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.5-57
- F-32: rebuild against ruby27

* Fri Dec 06 2019 Gwyn Ciesla <gwync@protonmail.com - 0.10.5-56
- Support EL-8.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.5-54
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Vít Ondruch <vondruch@redhat.com> - 0.10.5-52
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Thu Oct 04 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.10.5-51
- Drop python2.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.5-49
- Perl 5.28 rebuild

* Mon Apr 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.5-48
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.5-46
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.10.5-45
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.5-44
- F-28: rebuild for ruby25

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.5-43
- Python 2 binary package renamed to python2-clearsilver
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.5-40
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.5-38
- F-26: rebuild for ruby24

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-37
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.5-36
- Perl 5.24 rebuild

* Fri Apr 22 2016 Jon Ciesla <limburgher@gmail.com> - 0.10.5-35
- Change build order to correct Perl issue, BZ 1329524.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 0.10.5-33
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Fri Jul 17 2015 Petr Pisar <ppisar@redhat.com> - 0.10.5-32
- GCC 5 compatibility (bug #1190760)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.5-30
- Perl 5.22 rebuild

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.10.5-29
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.5-28
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Vít Ondruch <vondruch@redhat.com> - 0.10.5-25
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Enable Ruby extension on all platforms.
- Move Ruby extension into vendor directories.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.10.5-23
- Perl 5.18 rebuild

* Wed Mar 13 2013 Jon Ciesla <limburgher@gmail.com> - 0.10.5-22
- Rebuild for ruby deps.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.10.5-19
- Perl 5.16 rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 0.10.5-18
- Add hardened build.

* Tue Feb 07 2012 Jon Ciesla <limburgher@gmail.com> - 0.10.5-17
- Rebuild for new ruby.
- Added patch from https://gist.github.com/585817 for ruby 1.9.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Jon Ciesla <limburgher@gmail.com> - 0.10.5-15
- Patch for CVE-2011-4357, BZ 757543.

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.10.5-14
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.10.5-13
- Perl 5.14 mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 04 2010 Jon Ciesla <limb@jcomserv.net> - 0.10.5-11
- Added virtual provides for -static, BZ 609601.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.10.5-10
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.10.5-9
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.10.5-8
- rebuild against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 14 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.5-4
- Add patch from Kevin Kofler to fix build failures.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.10.5-3
Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.10.5-2
- Autorebuild for GCC 4.3

* Mon Jun  4 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.4-5
- Add BR perl-devel for fedora > 6

* Fri Jun 01 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.4-4
- Minor cleanups

* Fri Jun 01 2007 Jesse Keating <jkeating@redhat.com> - 0.10.4-3.1
- Disable java subpackages on el4

* Thu Apr 12 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.4-3
- Remove bogus -devel provides.

* Wed Mar 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.4-2
- Bump release.

* Wed Mar 28 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.10.4-1
- Update to 0.10.4

* Sat Dec  9 2006 Joost Soeterbroek <joost.soeterbroek@gmail.com> - 0.10.3-5
- Rebuild for python 2.5 

* Mon Aug 28 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.10.3-4
- Rebuild for Fedora Extras 6

* Thu Jun  1 2006 Paul Howarth <paul@city-fan.org> - 0.10.3-4
- ruby subpackage fix: use ruby_sitearchdir and ruby_sitelibdir

* Fri Mar 17 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.10.3-3
- fix for x86_64

* Mon Mar 13 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.10.3-1
- release 0.10.3

* Mon Feb 13 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.10.2-3
- Rebuild for Fedora Extras 5

* Fri Jan  6 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 0.10.2-2
- Rebuild with disable-ruby, disable-java for any arch other than i386
- hardcoded version in Patch0
- extra line in prep-section
- license files in all subpackages

* Thu Dec 15 2005 Joost Soeterbroek <fedora@soeterbroek.com> - 0.10.2-1
- Rebuild for 0.10.2

* Tue Nov 29 2005 Joost Soeterbroek <fedora@soeterbroek.com> - 0.10.1-1
- Rebuild for Fedora Extras

* Sun Jul 31 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.10.1-0.1
- 0.10.1, PIC issues fixed upstream.

* Sun May 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.3
- Rebuild for FC4.
- Rename subpackages to $foo-clearsilver.

* Mon Apr 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.2
- Build as PIC, fixes Ruby and Java builds on FC4.
- More parallel make fixing.

* Fri Apr  8 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.1
- First build.
