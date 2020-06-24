Summary:       DjVu viewer
Name:          djview4
Version:       4.10.6
Release:       13%{?dist}
License:       GPLv2+
URL:           http://djvu.sourceforge.net/djview4.html
Source0:       http://downloads.sourceforge.net/project/djvu/DjView/4.10/djview-%{version}.tar.gz
Source20:      qmake-qt5.sh
Patch1:        djview-4.8-include.patch
Patch2:        djview4-aarch64.patch
# don't strip -g flags even without --enable-debug
Patch3:        djview-4.10.6-debug.patch
Patch4:        djview4-disable-workaround-qt55.patch
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel
BuildRequires: desktop-file-utils
BuildRequires: djvulibre-devel >= 3.5.19 
# For plugin, see #756950
BuildRequires: glib2-devel
BuildRequires: libtiff-devel

%description 
DjView4 is a DjVu document viewer with the following features:
 o continuous scrolling of pages
 o side-by-side display of pages
 o display thumbnails as a grid
 o display outlines
 o page names supported
 o metadata dialog

It is based on DjVuLibre and Qt5.

%package       plugin
Summary:       Browser plugin for DjVu viewer
Requires:      %{name} = %{version}-%{release}

%description   plugin
This package provides a browser plugin for the DjVu document viewer.

%prep
%setup -q -n djview-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .debug
%patch4 -p1

%build
CFLAGS="%{optflags}"; export CFLAGS
CXXFLAGS="%{optflags}"; export CXXFLAGS
LDFLAGS="%{?__global_ldflags}"; export LDFLAGS

# avoid possible FTBFS if qt3 is installed
QTDIR=

# force use of custom/local qmake, to inject proper build flags (above)
install -m755 -D %{SOURCE20} bin/qmake-qt5
PATH=`pwd`/bin:%{_qt5_bindir}:$PATH; export PATH

%configure \
  --enable-nsdejavu \
  QMAKE="`pwd`/bin/qmake-qt5"

make %{?_smp_mflags} V=1 \
  QMAKE="`pwd`/bin/qmake-qt5"

%install
make DESTDIR=%{buildroot} INSTALL="%{__install} -p" \
     install plugindir=%{_libdir}/mozilla/plugins

# djview is taken from djvulibre
mv %{buildroot}%{_bindir}/djview %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_mandir}/man1/djview.1* %{buildroot}%{_mandir}/man1/%{name}.1*

%files
%doc COPYRIGHT COPYING NEWS README
%{_bindir}/%{name}
%dir %{_datadir}/djvu
%{_datadir}/djvu/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/djvulibre-%{name}.desktop
%{_datadir}/icons/hicolor/32x32/mimetypes/djvulibre-%{name}.png
%{_datadir}/icons/hicolor/64x64/mimetypes/djvulibre-%{name}.png
%{_datadir}/icons/hicolor/scalable/mimetypes/djvulibre-%{name}.svgz

%files plugin
%{_libdir}/mozilla
%{_mandir}/man1/nsdejavu.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.10.6-9
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Terje Rosten <terje.rosten@ntnu.no> - 4.10.6-4
- build with tiff support (rhbz#1397006)

* Fri Jul 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.10.6-3
- fix djview4-debuginfo harder (#1314996)

* Sat Mar 05 2016 Rex Dieter <rdieter@fedoraproject.org> 4.10.6-2
- djview4-debuginfo 4.10.6-1 contains no sources (1314996)

* Mon Feb 29 2016 Terje Rosten <terje.rosten@ntnu.no> - 4.10.6-1
- 4.10.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Terje Rosten <terje.rosten@ntnu.no> - 4.10.5-1
- 4.10.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.9-7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Sep 05 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 4.9-6
- Add AArch64 support

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 François Cami <fcami@fedoraproject.org> - 4.9-2
- remove all traces of djview-4.8-swap.patch.

* Thu May 23 2013 François Cami <fcami@fedoraproject.org> - 4.9-1
- new upstream release
- drop "-n djview-%%{version}" during setup, the new tarball expands to %%{name}-%%{version}
- remove djview-4.8-swap.patch
- add a header to djvulibre-djview4.desktop

* Sat Feb 23 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 4.8-9
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.8-5
- Add glib2 to buildreq

* Tue Nov 29 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.8-4
- Build with correct options

* Mon Nov 28 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.8-3
- Enable browser plugin
- Add patch to fix includes for plugin

* Mon Oct 03 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.8-2
- Add patch to build with newer gcc

* Fri Sep 30 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.8-1
- 4.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Terje Rosten <terje.rosten@ntnu.no> - 4.6-1
- 4.6

* Sun Dec 06 2009 Terje Rosten <terje.rosten@ntnu.no> - 4.5-1
- 4.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 4.4-1
- 4.4
- Own all dirs

* Sat Jan 17 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 4.3-3
- Rebuild with new djvulibre

* Tue Aug 12 2008 Terje Rosten <terje.rosten@ntnu.no> - 4.3-2
- Add gtk-update-icon-cache scriptlet

* Fri Apr 25 2008 Terje Rosten <terje.rosten@ntnu.no> - 4.3-1
- 4.3
- Loads of fixes

* Sat Jan 27 2007 Leon Bottou <leonb@users.sourceforge.net> 4.0-1
- initial release.

