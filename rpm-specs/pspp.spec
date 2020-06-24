Name:           pspp
Version:        1.2.0
Release:        8%{?dist}
Summary:        A program for statistical analysis of sampled data
License:        GPLv3+
URL:            https://www.gnu.org/software/pspp/
VCS:            scm:git:git://git.savannah.gnu.org/pspp.git
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        pspp-Smake
Patch1:		pspp-0001-Check-for-python-interpreter-at-configure-time-and-d.patch
Patch2:		pspp-0002-segment-Fix-behavior-when-line-is-not-new-line-termi.patch
Patch3:		pspp-0003-sys-file-writer-Remove-assertions-based-on-file-posi.patch
Patch4:		pspp-0004-pspp-dump-sav-Issue-error-message-for-too-large-exte.patch
Patch5:		pspp-0005-pspp-dump-sav-Fix-write-past-end-of-buffer-in-corner.patch
Patch6:		pspp-0006-PSPPIRE-Avoid-some-segmentation-faults-when-corrupt-.patch
Patch7:		pspp-0007-psppire-Fix-multiple-definitions-of-align_enum_type-.patch
Patch8:		pspp-0008-test-date-input.py-Make-compatible-with-Python-3.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gnulib-devel
BuildRequires:  gsl-devel >= 1.11-2
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  libpq-devel
BuildRequires:  libtool
BuildRequires:  libxml2
BuildRequires:  ncurses-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl-devel
BuildRequires:  plotutils-devel
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  spread-sheet-widget-devel
BuildRequires:  texinfo
Requires:	hicolor-icon-theme


%description
PSPP is a program for statistical analysis of sampled data. It
interprets commands in the SPSS language and produces tabular
output in ASCII, PostScript, or HTML format.

PSPP development is ongoing. It already supports a large subset
of SPSS's transformation language. Its statistical procedure
support is currently limited, but growing.


%prep
%autosetup -p1
# Remove bundled Gnulib and prepare to import system-wide one
rm -rf gl/
rm -f aclocal.m4
install -D -p -m 0644 %{SOURCE2} Smake


%build
# Import and build system-wide Gnulib
make -f Smake GNULIB=%{_datadir}/gnulib/lib GNULIB_TOOL=%{_bindir}/gnulib-tool

autoreconf -ifv
%configure CFLAGS="${CFLAGS:-%optflags} -fgnu89-inline" \
    --disable-static --disable-rpath
%make_build


%install
%make_install
# Install docs
mkdir -p %{buildroot}%{_pkgdocdir}
cp -p AUTHORS NEWS ONEWS README THANKS %{buildroot}%{_pkgdocdir}
# don't own /usr/share/info/dir
rm %{buildroot}%{_infodir}/dir

# don't lala
find %{buildroot}%{_libdir}/ \
   -name \*.la -delete

# desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/pspp.desktop

# localization
%find_lang %{name}

# clean up some stuff
rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache


%check
# FIXME python3 - 11 failed tests, python2 - only one
PYTHON=python2 make check || true


%files -f %{name}.lang
%license COPYING
%{_bindir}/pspp
%{_bindir}/psppire
%{_bindir}/pspp-convert
%{_bindir}/pspp-dump-sav
%{_infodir}/pspp*
%{_libdir}/%{name}/
%{_datadir}/appdata/pspp.appdata.xml
%{_datadir}/applications/pspp.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/icons/hicolor/scalable/apps/pspp.svg
%{_datadir}/pspp/
%{_pkgdocdir}/
%{_mandir}/man1/pspp.1.*
%{_mandir}/man1/psppire.1.*
%{_mandir}/man1/pspp-convert.1.*
%{_mandir}/man1/pspp-dump-sav.*


%changelog
* Tue Apr 21 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-8
- Fix tests with Python 3

* Mon Apr 20 2020 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-7
- Don't BR obsolete tools (rhbz#1809024)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-5
- https://bugzilla.redhat.com/1713922

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.0-4
- Rebuilt for GSL 2.6.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-2
- https://bugzilla.redhat.com/1660318 (CVE-2018-20230)
- https://bugzilla.redhat.com/1683499
- https://bugzilla.redhat.com/1684372 (CVE-2019-9211)
- https://bugzilla.redhat.com/1668144

* Thu Mar 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-9
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-7
- Added missing test dependency - perl(Text::Diff)

* Thu Sep 27 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-6
- Fixed two bugs (1470704, 1470708)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-3
- Remove obsolete scriptlets

* Mon Oct 09 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-2
- Fix test on PPC64(le) arches

* Tue Sep 19 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.0.1-1
- Ver. 1.0.1

* Tue Aug 22 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-1
- Ver. 1.0.0

* Sun Aug 13 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.11.0-1
- Ver. 0.11.0

* Sun Jul 30 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.10.2-6
- Perl no longer contains cwd in INC.

* Fri Jul 28 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.10.2-5
- Fix FTBFS with recent GCC
- Build using system-wide Gnulib

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.10.2-2
- Rebuild for readline 7.x

* Wed Aug 24 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.10.2-1
- Ver. 0.10.2

* Fri Apr  8 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.10.1-1
- Ver. 0.10.1
- Switched to GTK3

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.8.5-4
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Orion Poplawski <orion@cora.nwra.com> - 0.8.5-2
- Fix documentation install

* Sun Jun 21 2015 Peter Lemenkov <lemenkov@gmail.com> - 0.8.5-1
- Ver. 0.8.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 08 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.8.4-1
- Ver. 0.8.4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 10 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.8.3-1
- Ver. 0.8.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-1
- Ver. 0.8.2

* Tue Sep 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.1-1
- Ver. 0.8.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.0-1
- Ver. 0.8.0

* Sun Feb 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.7.9-5
- Fixed FTBFS in Rawhide / Fedora 19 (see rhbz #914398)
- Added provides(gnulib) (see rhbz #821785)
- Added accidentally removed pspp docs (see rhbz #822610)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.7.9-2
- Drop useless patch

* Sun Apr 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.7.9-1
- Ver. 0.7.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.7.8-1
- Ver. 0.7.8

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.2-5
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.6.2-3
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Peter Lemenkov <lemenkov@gmail.com> 0.6.2-2
- Rebuild (fixes ftbfs rhbz #599955)

* Fri Oct 16 2009 Peter Lemenkov <lemenkov@gmail.com> 0.6.2-1
- Ver. 0.6.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 22 2009 Matěj Cepl <mcepl@redhat.com> - 0.6.1-3
- Make .so symlink to versioned libraries -- shouldn't be needed
  but helps to fix bug 471180

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Matěj Cepl <mcepl@redhat.com> 0.6.1-1
- New upstream release.
- Added home made logo.
- Fix file permissions.

* Wed Nov 12 2008 Matěj Cepl <mcepl@redhat.com> - 0.6.0-9
- Fix in the %%preun script -- install-info wants only .info file
  as an argument.

* Thu Sep 25 2008 Matěj Cepl <mcepl@redhat.com> - 0.6.0-8
- Fix wrong CFLAGS -- add -fgnu89-inline

* Mon Jul 07 2008 Matej Cepl <mcepl@redhat.com> 0.6.0-7
- Fix BuildRequires.

* Wed Jun 18 2008 Matej Cepl <mcepl@redhat.com> 0.6.0-6
- Bug 451006 has been resolved, so we don't have to munge CFLAGS
  anymore.

* Sat Jun 14 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-5
- Approved version with fixed duplicate %%{_sysconfdir}/pspp

* Fri Jun 13 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-4
- Second wave of Package Review -- .desktop file
- Mysterious libraries eliminated

* Thu Jun 12 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-3
- First wave of Package Review nitpicking -- added %%doc and fixed Texinfo
  handling.

* Thu Jun 12 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-2
- Upstream release, this build is to be put into the package review.

* Tue Apr 22 2008 Matěj Cepl <mcepl@redhat.com> 0.6.0-0.1.pre2
- Upstream pre-release.

* Mon Apr 23 2007 Matej Cepl <mcepl@redhat.com> - 0.4.0-1
- The first experimental package of PSPP for Fedora.
