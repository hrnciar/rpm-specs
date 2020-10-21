Name:           yadex
Version:        1.7.0
Release:        51%{?dist}
Summary:        Doom level editor
License:        GPLv2+

URL:            http://www.teaser.fr/~amajorel/yadex

Source0:        http://www.teaser.fr/~amajorel/yadex/yadex-1.7.0.tar.gz
Source1:        yadex.desktop
Source2:        yadex.png

Patch0:         http://glbsp.sourceforge.net/yadex/Yadex_170_ALL.diff
Patch1:         http://glbsp.sourceforge.net/yadex/Yadex_170_Hexen.diff
Patch2:         yadex-1.7.0-64bit.patch
Patch3:         yadex-1.7.0-destdir.patch
Patch4:         yadex-1.7.0-datadir.patch
Patch5:         yadex-1.7.0-gcc41.patch
Patch6:         yadex-1.7.0.bareelif.patch
Patch7:         yadex-1.7.0-obj-overflow.patch
# The following patch is a difference between
# the Mr.Meval's huge patch (called "allpatches")
# attached to Bug 830628 and the upstream version
# 1.7.0 with local Fedora patches #0-7.
# It finally introduces changes contained
# in the omitted HEXEN patch #1 and other fixes
Patch8:         yadex-1.7.0-mrmeval-differential-patch.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libX11-devel
BuildRequires:  boost-devel
# Required by scripts/copyright
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  gcc-c++

# Yadex needs an iwad to run.  freedoom provides a free iwad that we can use.
Requires:       freedoom xorg-x11-fonts-ISO8859-1-75dpi

%description
Yadex is a Doom level (wad) editor for Unix systems running X, including Linux.
It supports Doom alpha, Doom beta, Doom, Ultimate Doom, Final Doom, Doom II,
Heretic and also, in a more or less limited way, Hexen and Strife.

Yadex is descended from DEU 5.21. Therefore, as you might expect, it's a rather
low-level editor that requires you to take care of a lot of detail but on the
flip side allows you to control very precisely what you are doing. In addition,
it has many advanced functions that DEU didn't have, to make certain
tedious tasks easy.


%prep
%setup -q

# Removing bundled boost
rm -rf boost

%patch0 -p1
# Omitted. Patch fails to apply. Used for Hexen maps only. Needs investigation.
#%%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p1


%build

# Don't use %%configure because this is not an autotools-generated
# configure script and will choke on some of the default configure switches.
./configure --prefix=%{_prefix}

# Disabling optimizations (#830628 - crash workaround)
CXXFLAGS_NOOPT=`echo "%{optflags}" | sed "s/-O2//g"`
make CXXFLAGS="$CXXFLAGS_NOOPT" CXX="%{__cxx} -std=gnu++03" %{?_smp_mflags}


%install
make install DESTDIR="%{buildroot}"

# Remove the duplicate man pages
rm -f %{buildroot}%{_mandir}/man6/%{name}*
iconv --from=ISO-8859-1 --to=UTF-8 docsrc/%{name}.6 > docsrc/%{name}.6.new
install -p -m644 docsrc/%{name}.6.new %{buildroot}/%{_mandir}/man6/%{name}.6

# .desktop file integration
desktop-file-install                             \
        --dir %{buildroot}%{_datadir}/applications         \
        %{SOURCE1}
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-%{version}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/%{version}
%config(noreplace) %{_sysconfdir}/%{name}/%{version}/%{name}.cfg
%{_datadir}/%{name}
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/yadex.png
%doc doc/*.html docsrc/*.png
%license COPYING COPYING.LIB

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.7.0-46
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.0-44
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.7.0-41
- Fix man page.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.7.0-38
- Rebuilt for Boost 1.63

* Mon Mar 21 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.7.0-37
- Add BR: perl, perl(strict), perl(Getopt::Long) (F24FTBFS, RHBZ#1308261)
- Compile with "g++ -std=gnu++03".

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-35
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.7.0-34
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.0-32
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.7.0-31
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.7.0-28
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.7.0-26
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.7.0-25
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Fri Jan 18 2013 Jaromir Capik <jcapik@redhat.com> - 1.7.0-24
- Removing bundled boost

* Fri Jan 11 2013 Jaromir Capik <jcapik@redhat.com> - 1.7.0-23
- Fixing keyboard shortcuts for adding and deleting objects
- ... by altering the Mr'Meval's patch (#830628)

* Thu Jan 10 2013 Jaromir Capik <jcapik@redhat.com> - 1.7.0-22
- Disabling optimizations (#830628 - crash workaround)

* Thu Jan 10 2013 Jaromir Capik <jcapik@redhat.com> - 1.7.0-21
- Introducing changes from Mr.Meval's "allpatches" patch (e.g HEXEN patch)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.0-17
- Requires xorg-x11-fonts-ISO8859-1-75dpi, BZ 620251.

* Fri May 07 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.0-16
- Addition to object overflow patch.

* Thu May 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.0-15
- Re-patch for buffer overflow crash.

* Thu May 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.7.0-14
- Patch for buffer overflow crash.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Caolán McNamara - 1.7.0-12
- fix bare #elif

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 8 2008 Wart <wart at kobold.org> 1.7.0-10
- Rebuild for gcc 4.3

* Fri Sep 7 2007 Wart <wart at kobold.org> 1.7.0-9
- No longer BuildRequires: gawk due to buildroot changes

* Tue Aug 21 2007 Wart <wart at kobold.org> 1.7.0-8
- License tag clarification
- Add BuildRequires: gawk due to changes in the buildroot

* Sat Aug 11 2007 Wart <wart at kobold.org> 1.7.0-7
- Clean up .desktop file version and categories

* Tue Oct 17 2006 Wart <wart at kobold.org> 1.7.0-6
- Own an extra directory

* Sun Aug 27 2006 Wart <wart at kobold.org> 1.7.0-5
- Rebuild for FC-6

* Mon Apr 10 2006 Wart <wart at kobold.org> 1.7.0-4
- Update for modular x.org

* Fri Mar 17 2006 Wart <wart at kobold.org> 1.7.0-3
- Added patch for gcc 4.1

* Thu Mar 16 2006 Wart <wart at kobold.org> 1.7.0-2
- Added .desktop file

* Thu Mar 16 2006 Wart <wart at kobold.org> 1.7.0-1
- Initial submission to Fedora Extras
