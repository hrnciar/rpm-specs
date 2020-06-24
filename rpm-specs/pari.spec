Name:           pari
Version:        2.11.3
Release:        1%{?dist}
Summary:        Number Theory-oriented Computer Algebra System
License:        GPLv2+
URL:            http://pari.math.u-bordeaux.fr/
Source0:        http://pari.math.u-bordeaux.fr/pub/pari/unix/%{name}-%{version}.tar.gz
Source1:        http://pari.math.u-bordeaux.fr/pub/pari/unix/%{name}-%{version}.tar.gz.asc
# Public key 0x4522e387, Bill Allombert <Bill.Allombert@math.u-bordeaux.fr>
Source2:        gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
Source3:        gp.desktop
Source4:        pari.xpm
Source5:        pari.abignore
Patch0:         pari-2.5.1-xdgopen.patch
Patch1:         pari-2.9.0-optflags.patch
Patch10:        pari-2.9.0-missing-field-init.patch
Patch11:        pari-2.9.2-declaration-not-prototype.patch
Patch12:        pari-2.9.0-clobbered.patch
Patch13:        pari-2.9.0-signed-unsigned-comparison.patch
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(x11)
BuildRequires:  sed
BuildRequires:  tex(tex)
BuildRequires:  tex(dvips)
BuildRequires:  tex-latex
BuildRequires:  xmkmf
# Test suite requirements
BuildRequires:  pari-elldata
BuildRequires:  pari-galdata
BuildRequires:  pari-galpol
BuildRequires:  pari-seadata

# Avoid doc-file dependencies and provides
%global __provides_exclude_from ^%{_datadir}/pari/PARI/
%global __requires_exclude_from ^%{_datadir}/pari/PARI/

%description
PARI is a widely used computer algebra system designed for fast computations in
number theory (factorizations, algebraic number theory, elliptic curves...),
but also contains a large number of other useful functions to compute with
mathematical entities such as matrices, polynomials, power series, algebraic
numbers, etc., and a lot of transcendental functions.

This package contains the shared libraries. The interactive
calculator PARI/GP is in package pari-gp.

%package devel
Summary:        Header files and libraries for PARI development
Requires:       %{name} = %{version}-%{release}

%description devel
Header files and libraries for PARI development.

%package gp
Summary:        PARI calculator
Requires:       %{name} = %{version}-%{release}
Requires:       bzip2
Requires:       gzip
Requires:       xdg-utils
Requires:       mimehandler(application/x-dvi)

%description gp
PARI/GP is an advanced programmable calculator, which computes
symbolically as long as possible, numerically where needed, and
contains a wealth of number-theoretic functions.

%prep
%setup -q

# Silence abidiff warnings about the size of functions_basic[] changing
cp -p %{SOURCE5} .

# Use xdg-open rather than xdvi to display DVI files (#530565)
%patch0

# Use our optflags, not upstream's
%patch1
sed -i -e "s|@OPTFLAGS@|%{optflags} -Wextra -Wstrict-prototypes -Wno-implicit-fallthrough $RPM_LD_FLAGS|" config/get_cc

# Fix compiler warnings
# http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1316
%patch10
%patch11
%patch12
%patch13

# Avoid unwanted rpaths
sed -i "s|runpathprefix='.*'|runpathprefix=''|" config/get_ld

# Verify the source file
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}

%build
./Configure \
    --prefix=%{_prefix} \
    --share-prefix=%{_datadir} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir}/man1 \
    --datadir=%{_datadir}/pari \
    --includedir=%{_includedir} \
    --with-gmp
make %{?_smp_mflags} gp

%install
make install \
  DESTDIR=%{buildroot} \
  INSTALL="install -p" \
  STRIP=/bin/true

# We move pari.cfg to the docdir
rm -fr %{buildroot}%{_prefix}/lib/pari

# Site-wide gprc
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m 644 misc/gprc.dft %{buildroot}%{_sysconfdir}/gprc

# Desktop menu entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE3}
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/pari/misc/

# Don't bother installing the simple gp wrapper script, so avoiding the
# need to patch it to fix the path to the executable
find %{buildroot} -name xgp -delete

%check
make test-all

%files
%if 0%{?_licensedir:1}
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS CHANGES* COMPAT NEW README
%doc Olinux-*/pari.cfg pari.abignore
%{_libdir}/libpari-gmp.so.%{version}
%{_libdir}/libpari-gmp.so.6

%files gp
%{_bindir}/gp
%{_bindir}/gp-2.11
%{_bindir}/gphelp
%{_bindir}/tex2mail
%config(noreplace) %{_sysconfdir}/gprc
%dir %{_datadir}/pari/
%doc %{_datadir}/pari/PARI/
%doc %{_datadir}/pari/doc/
%doc %{_datadir}/pari/examples/
%{_datadir}/pari/misc/
%{_datadir}/pari/pari.desc
%{_datadir}/applications/*gp.desktop
%{_mandir}/man1/gp-2.11.1*
%{_mandir}/man1/gp.1*
%{_mandir}/man1/gphelp.1*
%{_mandir}/man1/pari.1*
%{_mandir}/man1/tex2mail.1*

%files devel
%{_includedir}/pari/
%{_libdir}/libpari.so

%changelog
* Thu Mar  5 2020 Jerry James <loganjerry@gmail.com> - 2.11.3-1
- Update to 2.11.3 (see CHANGES for details)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Jerry James <loganjerry@gmail.com> - 2.11.2-2
- Verify the source file

* Wed May 15 2019 Jerry James <loganjerry@gmail.com> - 2.11.2-1
- Update to 2.11.2 (see CHANGES for details)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11.1-3
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan  4 2019 Jerry James <loganjerry@gmail.com> - 2.11.1-1
- Update to 2.11.1 (see CHANGES for details)
- Drop braces patch

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 2.11.0-1
- Update to 2.11.0 (see CHANGES for details)
- Drop ellratpoints patch
- Obsolete genus2reduction

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 2.9.5-2
- Backport ellratpoints and hyperellratpoints from 2.10alpha for sagemath

* Mon May 21 2018 Paul Howarth <paul@city-fan.org> - 2.9.5-1
- Update to 2.9.5 (see CHANGES for details)

* Tue Feb  6 2018 Paul Howarth <paul@city-fan.org> - 2.9.4-2
- Switch to %%ldconfig_scriptlets
- Silence abidiff warnings about the size of functions_basic[] changing

* Tue Jan  9 2018 Paul Howarth <paul@city-fan.org> - 2.9.4-1
- Update to 2.9.4 (see CHANGES for details)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Paul Howarth <paul@city-fan.org> - 2.9.3-1
- Update to 2.9.3 (see CHANGES for details)

* Tue Jun 20 2017 Paul Howarth <paul@city-fan.org> - 2.9.2-3
- Include pari/gp desktop icon, dropped from upstream releases after 2.5.x
  (#1462987)
- Drop redundant Group: tags

* Tue Apr 18 2017 Paul Howarth <paul@city-fan.org> - 2.9.2-2
- Drop the compat library for pari 2.7 as nothing in Fedora is using it now

* Thu Apr  6 2017 Paul Howarth <paul@city-fan.org> - 2.9.2-1
- Update to 2.9.2 (see CHANGES for details)
- Build with -Wno-implicit-fallthrough because upstream code intentionally
  falls through switch cases all over the place

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.9.1-2
- Rebuild for readline 7.x

* Sun Dec  4 2016 Paul Howarth <paul@city-fan.org> - 2.9.1-1
- Update to 2.9.1 (see CHANGES for details)

* Wed Nov  2 2016 Paul Howarth <paul@city-fan.org> - 2.9.0-1
- Update to 2.9.0 (see NEW and CHANGES for details)
- Update patches as needed
- Temporarily include old version of library to avoid broken deps whilst
  migration to pari 2.9 happens in Rawhide

* Tue Jun 21 2016 Paul Howarth <paul@city-fan.org> - 2.7.6-1
- Update to 2.7.6 (see CHANGES for details)
- Simplify find command using -delete
- Specify all build requirements

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Paul Howarth <paul@city-fan.org> - 2.7.5-1
- Update to 2.7.5 (see CHANGES for details)

* Sat Jun 20 2015 Paul Howarth <paul@city-fan.org> - 2.7.4-1
- Update to 2.7.4 (see CHANGES for details)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 Paul Howarth <paul@city-fan.org> - 2.7.3-1
- Update to 2.7.3 (see CHANGES for details)

* Fri Sep 19 2014 Paul Howarth <paul@city-fan.org> - 2.7.2-1
- Update to 2.7.2 (see CHANGES for details)
- Update patches as needed
- Drop libpari-gmp.so.3 compat library
- Use %%license where possible

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul  7 2014 Paul Howarth <paul@city-fan.org> - 2.7.1-4
- Fix crash in ellmul with obsolete use of E=[a1,a2,a3,a4,a6]
  (#1104802, upstream bug #1589)

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Paul Howarth <paul@city-fan.org> - 2.7.1-2
- Temporarily include old version of library to avoid broken deps whilst
  migration to pari 2.7 happens in Rawhide

* Fri May 16 2014 Paul Howarth <paul@city-fan.org> - 2.7.1-1
- Update to 2.7.1 (see CHANGES for details)

* Mon Mar 24 2014 Paul Howarth <paul@city-fan.org> - 2.7.0-1
- Update to 2.7.0 (see NEW for details)
- Update patches as needed
- BR: pari-galpol for additional test coverage

* Sat Sep 21 2013 Paul Howarth <paul@city-fan.org> - 2.5.5-1
- Update to 2.5.5 (see CHANGES for details)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.5.4-2
- Perl 5.18 rebuild

* Tue May 14 2013 Paul Howarth <paul@city-fan.org> - 2.5.4-1
- update to 2.5.4 (see CHANGES for details)
- update missing-field-init patch

* Wed May  1 2013 Jon Ciesla <limburgher@gmail.com> - 2.5.3-3
- drop desktop vendor tag

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct  4 2012 Paul Howarth <paul@city-fan.org> - 2.5.3-1
- update to 2.5.3 (see CHANGES for details)
- further compiler warning fixes after discussion with upstream
- drop upstreamed parts of declaration-not-prototype patch

* Mon Aug  6 2012 Paul Howarth <paul@city-fan.org> - 2.5.2-1
- update to 2.5.2 (see CHANGES for details)
- drop upstreamed gcc 4.7, bug#1264 and FSF address patches

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Paul Howarth <paul@city-fan.org> - 2.5.1-1
- update to 2.5.1 (#821191; see NEW for details)
- use rpm 4.9.x requires/provides filtering
- update xdg-open patch
- drop emacs sub-package; the PARI Emacs shell is now a separate project
- drop %%defattr, redundant since rpm 4.4
- gp sub-package requires bzip2 for support of bzipped files
- make %%files list more explicit
- drop redundant buildroot definition and cleaning
- BR: xmkmf for X11 detection
- make sure we use our %%{optflags} and only those
- call pari_init_defaults() before gp_expand_path() (upstream #1264)
- fix scoping issue that manifests as a test suite failure with gcc 4.7.x and
  -ftree-dse (#821918, upstream #1314)
- fix desktop file categories
- install site-wide /etc/gprc
- update FSF address (upstream #1315)
- fix various compiler warnings (upstream #1316)
- run the full test suite in %%check
- add buildreqs for data packages needed by full test suite
- hardcode %%{_datadir} in gp.desktop so no need to fiddle with it in %%prep

* Sat Jan  7 2012 Paul Howarth <paul@city-fan.org> - 2.3.5-4
- s/\$RPM_BUILD_ROOT/%%{buildroot}/g for tidyness
- update source URL as 2.3.5 is now an OLD version

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.3.5-3.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 2.3.5-3.1
- rebuild with new gmp

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.5-3
- rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct  1 2010 Mark Chappell <tremble@fedoraproject.org> - 2.3.5-2
- switch the latex dependencies over to tex(...)

* Fri Jul  9 2010 Paul Howarth <paul@city-fan.org> - 2.3.5-1
- update to 2.3.5 (see CHANGES for details)
- filter out perl dependencies from %%{_datadir}/pari/PARI/

* Thu Jul  8 2010 Paul Howarth <paul@city-fan.org> - 2.3.4-5
- various clean-ups to pacify rpmlint:
  - uses spaces instead of tabs consistently
  - mark %%{_datadir}/emacs/site-lisp/pari/pariemacs.txt as %%doc
  - mark %%{_datadir}/pari/{PARI,doc,examples} as %%doc
  - fix permissions of gp
- don't strip gp so we get debuginfo for it
- move here documents out to separate source files
- make gp subpackage require same version-release of main package

* Wed Jul  7 2010 Paul Howarth <paul@city-fan.org> - 2.3.4-4
- apply patch from Patrice Dumas to use xdg-open rather than xdvi to display
  DVI content, and move the xdg-open requirement from the main package to the
  gp sub-package (#530565)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.3.4-1
- new release 2.3.4

* Wed Aug 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.3.3-2
- fix license tag

* Sat Feb 23 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.3.3-1
- new release 2.3.3

* Sat Feb 23 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.3.1-3
- corrected desktop file

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.1-2
- Autorebuild for GCC 4.3

* Fri Dec 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.3.1-1
- new version 2.3.1

* Fri Dec 29 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.3.0-5
- added -fno-strict-aliasing to CFLAGS and enabled ppc build

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.3.0-4
- Rebuild for FE6

* Fri May 26 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.3.0-3
- Exclude ppc for now, since test fails

* Fri May 26 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.3.0-2
- added %%check section
- use gmp

* Thu May 25 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.3.0-1
- new version 2.3.0

* Fri May 19 2006 Orion Poplawski <orion@cora.nwra.com> - 2.1.7-4
- Fix shared library builds

* Fri Dec  2 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.1.7-3
- Use none for architecture to guarantee working 64bit builds

* Fri Oct 21 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.1.7-2
- some cleanup

* Fri Sep 30 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.1.7-1
- New Version 2.1.7

* Sun Mar  6 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.1.6-1
- New Version 2.1.6

* Mon Nov 22 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.1.5-0.fdr.2
- Fixed problem with readline

* Wed Nov 12 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.1.5-0.fdr.x
- First Fedora release
