%global debug_package %{nil}
%global monoprefix %{_prefix}/lib

Summary: An OO statically typed language for CLI
Name: boo
Version: 0.9.7.0
Release: 16%{?dist}
License: MIT
URL: https://github.com/bamboo/boo

Source0: https://github.com/bamboo/boo/archive/alpha.tar.gz
Patch0: boo-pkgconfig_path_fix.patch
BuildRequires: mono-devel, gtksourceview2-devel, shared-mime-info, pkgconfig, nant, log4net
# Mono only available on these:
ExclusiveArch: %{mono_arches}

%description
Boo is a new object oriented statically typed programming language for the
Common Language Infrastructure with a python inspired syntax and a special
focus on language and compiler extensible.

%package devel
Summary: Development files for boo
Requires: %{name} = %{version}-%{release}

%description devel
Development files for boo

%package examples
Summary: Examples files for boo
Requires: %{name} = %{version}-%{release}

%description examples
Examples files for boo

%prep
%setup -q -n %{name}-alpha
%patch0 -p1 -b .pc-original

# Get rid of prebuilt dll files
rm -rf bin/*.dll bin/pt/*.dll
rm -rf bin/*.exe bin/pt/*.exe
rm -rf bin/*.config bin/pt/*.config

# Fix gtksourceview version
sed -i "s#gtksourceview-1.0#gtksourceview-2.0#g" default.build

# Temporary workaround: disable verification of assemblies because pedump currently segfaults on Rawhide
sed -i 's#<call target="verify-assemblies" />##g' default.build

%build
nant -D:install.prefix=%{_prefix} -D:docs.dir=%{_defaultdocdir} -D:install.booexamples=%{_datadir}/%{name}/examples

%install
nant -f:default.build install -D:install.prefix=%{_prefix} -D:install.destdir=%{buildroot} -D:docs.dir=%{_defaultdocdir} -D:install.booexamples=%{_datadir}/%{name}/examples

#Locate pc file into correct libdir
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{monoprefix}" || mv $RPM_BUILD_ROOT%{monoprefix}/pkgconfig/* $RPM_BUILD_ROOT%{_libdir}/pkgconfig/

# Prevent conflict with gtksourceview2 rpm
rm $RPM_BUILD_ROOT%{_datadir}/gtksourceview-2.0/language-specs/boo.lang

# Remove Boo.NAnt.Tasks.dll for version problem with NAnt.Core.dll
rm $RPM_BUILD_ROOT%{monoprefix}/boo/Boo.NAnt.Tasks.dll

rm $RPM_BUILD_ROOT/%{_defaultdocdir}/boo/license.txt $RPM_BUILD_ROOT/%{_defaultdocdir}/boo/version.txt $RPM_BUILD_ROOT/%{_defaultdocdir}/boo/todo.txt

%files
%doc notice.txt README.md docs/BooManifesto.sxw
%license license.txt
%{monoprefix}/boo*/
%dir %{_monodir}/boo
%{_monodir}/boo/*.dll
%{_monogacdir}/Boo*/
%{_bindir}/boo*
%{_datadir}/mime/packages/boo*
%{_datadir}/mime-info/boo*

%files devel
%{_libdir}/pkgconfig/boo.pc
#% {monoprefix}/boo/Boo.NAnt.Tasks.dll

%files examples
%{_datadir}/%{name}/examples/*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.9.7.0-13
- Enable ppc64 again. Add build dependancy on log4net.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Timotheus Pokorra <tp@tbits.net> - 0.9.7.0-9
- ExcludeArch ppc64 because it fails to build there. see bug 1555649

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7.0-4
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 0.9.7.0-2
- Prevent boo.lang conflict with gtksourceview
- Remove Boo.NAnt.Tasks.dll for problem with NAnt.Core.dll version

* Wed Jun 17 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 0.9.7.0-1
- Update to 0.9.7.0 from bamboo source
- Add examples subpackage

* Wed Jun 17 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 0.9.4.9-14
- Fix for build for mono 4
- Use mono macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.4.9-12
- Rebuild (mono4)

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.4.9-11
- update mime scriptlet

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 08 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.4.9-9
- Remove %%arm from ExclusiveArch for lack of nant (#1106011)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Christian Krause <chkr@fedoraproject.org> - 0.9.4.9-3
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Tue Apr 19 2011 Dan Horák <dan[at]danny.cz> - 0.9.4.9-2
- updated the supported arch list

* Fri Feb 18 2011 Paul Lange <palango@gmx.de> - 0.9.4.9-1
- update to 0.9.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.3457-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.9.3.3457-1
- Update to newest version
- Alter BR nant to BR nant-devel

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.9.2.3383-3
- ExcludeArch sparc64

* Tue Oct 06 2009 Paul Lange <palango@gmx.de> - 0.9.2.3383-2
- Move Boo.NAnt.Tasks.dll to boo-devel

* Wed Sep 16 2009 Paul Lange <palango@gmx.de> - 0.9.2.3383-1
- Update to boo 0.9.2
- remove libdir patch

* Fri Aug 28 2009 Paul Lange <palango@gmx.de> - 0.9.1.3287-3
- Fix executable paths

* Thu Aug 27 2009 Michel Salim <salimma@fedoraproject.org> - 0.9.1.3287-2
- Fix libdir in boo.pc to use %%{_libdir}
- Summary no longer repeats package name

* Sun Aug 02 2009 Paul Lange <palango@gmx.de> - 0.9.1.3287-1
- Update to boo 0.9.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1.2865-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8.1.2865-7
- Include missing directory entries (#473630).

* Mon Apr 20 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.8.1.2865-6
- Fix FTBFS: added boo-mono.patch

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1.2865-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Apr 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8.1.2865-4
- get rid of prebuilt binary files

* Tue Mar  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.8.1.2865-3
- Rebuild for new nant (causes broken deps)

* Sat Feb 23 2008 David Nielsen <gnomeuser@gmail.com> - 0.8.1-2865-2
- Nope, ppc still broken (#434631)

* Sat Feb 23 2008 David Nielsen <gnomeuser@gmail.com> - 0.8.1-2865-1
- Bump to 0.8.1
- Exclude Visual Studio Environment buildtarget
- Reenable ppc

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.0.2730-9
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.8.0-2730-7
- spec fix

* Wed Dec 19 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.8.0-2730-6
- remove ppc build
- fix libdir problem for pc file

* Sun Dec 16 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.8.0-2730-5
- reenable ppc

* Thu Nov 22 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.8.0-2730-4
- fixes to patches for corrected libdirs

* Sat Nov 17 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.8.0-2730-3
- Added exclusivearch

* Sun Nov 11 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.8.0-2730-2
- large bump
- removed fc5 and fc6 bit6
- removed MS update builds from default build
- fixed problem with the boo.pc file

* Sun Feb 18 2007 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-2237-13
- fix for correct libdir in bin scripts

* Wed Dec 20 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6-2237-11
- fix for correct libdir

* Thu Sep 14 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6.2237-9
- rebuild

* Mon Aug 07 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6.2237-8
- adds conditional for boo.lang - not required in FC6

* Wed Jul 26 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6.2237-7
- claims ownership of monodir-boo now

* Tue Jul 25 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6.2237-6
- replaced monodir for libdir in devel
- fixed tab-spaces problem
- removed rm rf from the prep step
- added update-mime-database

* Sun Jul 23 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6.2237-5
- removed nodebug
- removed redefine of libdir
- removed buildarch
- added BR nant

* Sat Jun 17 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6.2237-3
- removed exclusivearch
- changed BR
- removed R
- altered nant to /usr/bin/nant

* Thu Jun 08 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6.2237-1
- Spec file fixes
- Fix for gtksourceview-1.0 langspecs
- Added fixed libdir
- rebuild for mono 1.1.15

* Thu Jun 08 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.6.2237-1
- Bump to 0.7.6-2237
- Added R nant
- Multiple fixes to the install as it uses nant rather than make install
- Removed some bits from the files section as they're no longer in boo

* Wed May 31 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.5.2013-7
- Added devel files
- Added doc to files section instead of adding the files manually
- Added fix for x86_64

* Mon May 08 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.5.2013-6
- Altered again for mock and x86_64

* Fri Apr 28 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.5.2003-5
- added shared mime to satisfy mock

* Sat Apr 22 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.5.2003-4
- Removal of the always usr-lib, but now use the system used in f-spot
- include archs mono is available on
- added requires: mono-core, gtksourceview
- changed BR to include gtksourceview-sharp
- removes the conflict in the language-specs with gtksourceview package

* Tue Apr 18 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.5.2003-3
- Spec file tweaks
- libdir is now usr-lib irrespective of hardware built on
- Added docs to package

* Mon Apr 17 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.5.2003-2
- Small fix to the spec file

* Sat Apr 15 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.7.5.2003-1
- Initial import and debug for FE (spec file based on the mono project one)
