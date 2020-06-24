Name:           gnofract4d
Version:        4.2
Release:        1%{?dist}
Summary:        Gnofract 4D is a Gnome-based program to draw fractals
License:        LGPLv2+

URL:            http://fract4d.github.io/gnofract4d/
Source0:        https://github.com/fract4d/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libxslt
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3dist(pytest)
BuildRequires:  xorg-x11-fonts-Type1
BuildRequires:  xorg-x11-server-Xvfb

Requires:       gcc
Requires:       libgcc%{?_isa}
Requires:       glibc-devel%{?_isa}
Requires:       python3-gobject

%description
Gnofract 4D is a free, open source program which allows anyone to create
beautiful images called fractals.  The images are automatically created
by the computer based on mathematical principles.  These include the
Mandelbrot and Julia sets and many more.  You don't need to do any math:
you can explore a universe of images just using a mouse.

%prep
%setup -q

# Fix the desktop file
sed -e "s/Categories.*/Categories=Graphics;GTK;GNOME;Education;Science;Math;/" \
    -e "s/MimeType.*/&;/" \
    -i.orig %{name}.desktop
touch -r %{name}.desktop.orig %{name}.desktop
rm %{name}.desktop.orig

# Point the XSL file to where Fedora stores its docbook XSL files
sed -i 's|http://docbook.sourceforge.net/release/xsl/current|file://%{_datadir}/sgml/docbook/xsl-stylesheets|' \
    doc/gnofract4d-manual/C/gnofract4d.xsl

# Do not turn off optimization
sed -i "s/, '-O0'//" setup.py

%build
%py3_build

# Generate documentation with an X server running (on a random X server to
# avoid collisions) so pygtk doesn't bail out immediately.
let "dnum = $RANDOM % 90 + 10"
xvfb-run -a -n $dnum %{__python3} createdocs.py

%install
%py3_install

# Check the desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install the AppData file
mkdir -p %{buildroot}%{_datadir}/appdata
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

# Remove the shebangs
for fil in `find %{buildroot}%{python3_sitearch} -perm 644 -name '*.py'`; do
  sed '\|^#!/usr/bin.*python|d' $fil > $fil.new
  touch -r $fil $fil.new
  mv -f $fil.new $fil
done

# Remove duplicated docs
rm -rf %{buildroot}%{_docdir}/%{name}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/%{name}.1 %{buildroot}%{_mandir}/man1

%check
%{__python3} ./test.py

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%docdir %{_datadir}/gnome/help/%{name}/
%{_datadir}/gnome/help/%{name}/
%{_datadir}/mime/packages/%{name}-mime.xml
%{_datadir}/pixmaps/%{name}*
%{_mandir}/man1/%{name}*
%{python3_sitearch}/*.egg-info
%{python3_sitearch}/fract4d/
%{python3_sitearch}/fract4d_compiler/
%{python3_sitearch}/fract4dgui/

%changelog
* Fri May 29 2020 Jerry James <loganjerry@gmail.com> - 4.2-1
- Version 4.2
- Upstream now installs the header files needed at runtime
- Add a check script

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1-3
- Rebuilt for Python 3.9

* Tue May 19 2020 Jerry James <loganjerry@gmail.com> - 4.1-2
- Install header files needed at runtime (bz 1837317)

* Sun May 10 2020 Jerry James <loganjerry@gmail.com> - 4.1-1
- Version 4.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-2
- Rebuilt for Python 3.7

* Sat Apr 28 2018 Jerry James <loganjerry@gmail.com> - 4.0.1-1
- New upstream version
- Drop upstreamed -refcount patch
- Upstream now has the higher resolution icon, too; use it
- Project now requires python3 instead of python2

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 3.14.1-22
- Install a higher resolution icon

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 3.14.1-21
- BR gcc-c++ instead of gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.14.1-19
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.1-15
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 23 2016 Jerry James <loganjerry@gmail.com> - 3.14.1-14
- Fix inverted test in -refcount patch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Jerry James <loganjerry@gmail.com> - 3.14.1-12
- Update -refcount patch again to fix still more crashes
- Update URLs
- Add gmp-devel, gmpy, and libpng-devel BRs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.14.1-10
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar  9 2015 Jerry James <loganjerry@gmail.com> - 3.14.1-9
- Update -refcount patch to fix bz 1199824

* Wed Nov 12 2014 Jerry James <loganjerry@gmail.com> - 3.14.1-8
- Add -refcount patch to attempt to fix bz 1033441 and bz 1131717
- Minor spec file cleanups

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 3.14.1-7
- update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Jerry James <loganjerry@gmail.com> - 3.14.1-4
- Simplify Xvfb usage
- Add an AppData file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Jerry James <loganjerry@gmail.com> - 3.14.1-2
- Rebuild for libpng 1.6
- Fix bogus changelog dates

* Fri Mar 15 2013 Jerry James <loganjerry@gmail.com> - 3.14.1-1
- New upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.14-3
- rebuild due to "jpeg8-ABI" feature drop

* Thu Nov  8 2012 Jerry James <loganjerry@gmail.com> - 3.14-2
- Fix bz 872853 by doing the following:
- Add missing tutorial*.xml files from upstream git
- BR libxslt to get xsltproc
- BR docbook-style-xsl, required by the doc files
- BR xorg packages so pygtk is able to generate the PNG files
- Run createdocs.py after building

* Thu Jul 26 2012 Jerry James <loganjerry@gmail.com> - 3.14-1
- New upstream release (fixes bz 665571, 834382, and 843224)
- Require glibc-devel (fixes bz 725205)
- Filter provides of private Python shared objects
- Ship the man page
- Spec file cleanups

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.13-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Adam Tkac <atkac redhat com> - 3.13-1
- rebuild to ensure F14 has higher NVR than F13
- following changes have been merged from F13 [Stewart Adam]
  - Update to 3.13
  - Require gcc (fixes #571970)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Aug 14 2009 Stewart Adam <s.adam at diffingo.com> - 3.12-3
- Disable make check, it seems to cause extremely long build times (>24h)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Stewart Adam <s.adam at diffingo.com> - 3.12-1
- Update to 3.12

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Stewart Adam <s.adam at diffingo.com> - 3.10-2
- Use a random X display number from :10 to :99 to avoid "display in use"
  errors while building

* Thu Feb 19 2009 Stewart Adam <s.adam at diffingo.com> - 3.10-1
- Update to 3.10

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.9-2
- Rebuild for Python 2.6

* Sat Jul 19 2008 Stewart Adam <s.adam at diffingo.com> - 3.9-1
- Update to 3.9

* Sat Feb 16 2008 Stewart Adam <s.adam at diffingo.com> - 3.8-1
- Update to 3.8

* Fri Dec 28 2007 Stewart Adam <s.adam at diffingo.com> - 3.7-1
- Update to 3.7
- Drop obsolete patches

* Sun Nov 18 2007 Stewart Adam <s.adam at diffingo.com> - 3.6-4
- Fix .desktop file location
- Fix Source0 URL
- Own /usr/share/gnofract4d

* Sun Nov 18 2007 Stewart Adam <s.adam at diffingo.com> - 3.6-3
- BR xorg-x11-xinit, pygtk2-devel >= 2.6

* Sat Nov 17 2007 Stewart Adam <s.adam at diffingo.com> - 3.6-2
- License is actually LGPLv2+ because of lex.py, yacc.py, FCTGen.py
- Add patch for test suite files since two tests are invalid
- Update MIME and desktop databases
- Use virtual X for GUI test suite
- Remove redundant BR
- Remove redundant entries from %%files
- Fix rpmlint's errors about executable files/shebangs

* Wed Nov 14 2007 Stewart Adam <s.adam at diffingo.com> - 3.6-1
- Update to 3.6
- Make Source0 a URL again
- License is no longer GPL
- Update spec for Fedora (re)review
- Add patch to generate a valid .desktop file

* Mon Aug 28 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.14-4
- Rebuild for FC6

* Thu Jul 20 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.14-3
- fixed bz# 192878

* Sun May 21 2006 Michael J. Knox <michael[AT]Knox.net.nz> - 2.14-2
- fixed files list for x86_64 builds

* Wed May 17 2006 Michael J. Knox <michael[AT]Knox.net.nz> - 2.14-1
- version bump and spec clean

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Feb 13 2005 Throsten Leemhuis <fedora at leemhuis dot info> 0:2.6-2
- "sed -i s|/usr/lib/|%%{_libdir}|g setup.cfg" on x86_64

* Tue Feb 01 2005 Panu Matilainen <pmatilai@welho.com> 0:2.6-1
- update to 2.6
- drop epoch 0 and fedora.us release tag
- run update-desktop-database on post+postun

* Sun Oct 03 2004 Panu Matilainen <pmatilai@welho.com> 0:2.1-0.fdr.1
- update to 2.1

* Tue Jul 06 2004 Panu Matilainen <pmatilai@welho.com> 0:2.0-0.fdr.1
- update to 2.0
- quite a few dependency changes because of switch to python etc

* Mon May 31 2004 Panu Matilainen <pmatilai@welho.com> 0:1.9-0.fdr.3
- fix build against newer gtk (gtk-buildfix patch)

* Tue Dec 23 2003 Panu Matilainen <pmatilai@welho.com> 0:1.9-0.fdr.2
- address issues in #1114
- huh, this requires g++ to run...

* Mon Dec 15 2003 Panu Matilainen <pmatilai@welho.com> 0:1.9-0.fdr.1
- update to 1.9
- drop patch (no longer needed to build)
- add translations now that there is one


* Sun Dec 07 2003 Panu Matilainen <pmatilai@welho.com> 0:1.8-0.fdr.1
- Initial Fedora packaging.
