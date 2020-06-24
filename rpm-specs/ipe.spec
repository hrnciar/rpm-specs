%global majorversion 7.2

Name:           ipe
Version:        7.2.18
Release:        1%{?dist}
Summary:        Drawing editor for creating figures in PDF or PostScript formats
# GPLv2, with an exception for the CGAL libraries.
License:        GPLv2+ with exceptions
URL:            http://ipe.otfried.org/
Source0:	https://dl.bintray.com/otfried/generic/%{name}/%{majorversion}/%{name}-%{version}-src.tar.gz
Source1:	%{name}.desktop

BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig
BuildRequires:	qt5-qtbase-devel
BuildRequires:	cairo-devel
BuildRequires:	freetype-devel
BuildRequires:	libpng-devel
BuildRequires:	lua-devel
BuildRequires:	curl-devel
BuildRequires:	gsl-devel
BuildRequires:	libjpeg-turbo-devel

Requires:       tex(latex)
Requires:       urw-fonts
Requires:       xdg-utils

Provides:       ipe(api) = %{version}
Provides:       ipetoipe = %{version}
Provides:       ipetopng = %{version}

%description
Ipe is a drawing editor for creating figures in PDF or (encapsulated)
Postscript format. It supports making small figures for inclusion into
LaTeX-documents as well as making multi-page PDF presentations that
can be shown on-line with a PDF viewer


%package devel
Summary: Development files and documentation for designing Ipelets
Requires: %{name} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description devel 
This packages contains the files necessary to develop Ipelets, which are
plugins for the Ipe editor.

%package doc
BuildArch: noarch
Summary: Documentation of Ipe
Requires: %{name} = %{version}-%{release}
%description doc
%{summary}.

%prep
%setup -n %{name}-%{version} -q
# fix files permissions
find src -type f -exec chmod -x {} +


%build
export QTDIR=%{qtdir}

pushd src
%make_build LUA_CFLAGS="`pkg-config --cflags lua`" \
     LUA_LIBS="`pkg-config --libs lua`" \
     MOC=moc-qt5 \
     IPEPREFIX="%{_prefix}" IPELIBDIR="%{_libdir}" \
     IPELETDIR="%{_libdir}/%{name}/%{version}/ipelets" \
     IPECURL=1 IPEGSL=1
popd 


%install
pushd src
make INSTALL_ROOT=%{buildroot} install \
     IPEPREFIX="%{_prefix}" IPELIBDIR="%{_libdir}" \
     IPELETDIR="%{_libdir}/%{name}/%{version}/ipelets" \
     INSTALL_PROGRAMS="install -m 0755"
popd

# Install desktop file
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license gpl.txt
%doc readme.txt news.txt

%{_bindir}/ipe
%{_bindir}/ipe6upgrade
%{_bindir}/ipecurl
%{_bindir}/ipeextract
%{_bindir}/iperender
%{_bindir}/ipescript
%{_bindir}/ipetoipe
%{_bindir}/ipepresenter

%{_libdir}/libipe.so.%{version}
%{_libdir}/libipeui.so.%{version}
%{_libdir}/libipecairo.so.%{version}
%{_libdir}/libipecanvas.so.%{version}
%{_libdir}/libipelua.so.%{version}

%dir %{_libdir}/ipe
%{_libdir}/ipe/%{version}/ipelets/*

%dir %{_datadir}/ipe
%dir %{_datadir}/ipe/%{version}
%{_datadir}/ipe/%{version}/icons
%{_datadir}/ipe/%{version}/lua
%{_datadir}/ipe/%{version}/styles

%{_datadir}/applications/*%{name}*.desktop

%{_mandir}/man1/ipe.1.gz
%{_mandir}/man1/ipe6upgrade.1.gz
%{_mandir}/man1/ipeextract.1.gz
%{_mandir}/man1/iperender.1.gz
%{_mandir}/man1/ipescript.1.gz
%{_mandir}/man1/ipetoipe.1.gz

%files devel
%license gpl.txt
%doc readme.txt news.txt
%{_includedir}/*.h
%{_libdir}/libipe.so
%{_libdir}/libipeui.so
%{_libdir}/libipecairo.so
%{_libdir}/libipecanvas.so
%{_libdir}/libipelua.so

%files doc
%license gpl.txt
%doc readme.txt gpl.txt news.txt
%{_datadir}/%{name}/%{version}

%changelog
* Wed May 20 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.18-1
- Update to 7.2.18

* Fri May 08 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.17-1
- Update to 7.2.17

* Fri May 01 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.16-1
- Update to 7.2.16
- Drop upstreamed patch
- Modernize spec file

* Sun Apr 19 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.14-1
- Update to 7.2.14

* Sun Mar 08 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.13-1
- Update to 7.2.13

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.12-3
- Add patch to fix compilation issues with gcc-10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.12-1
- Update to 7.2.12

* Sat Mar 09 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.11-2
- Add ipepresenter to files section

* Sat Mar 09 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.11-1
- Update to 7.2.11

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.9-1
- Update to 7.2.9

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.7-6
- Fix FTBFS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.7-1
- Update to 7.2.7

* Sun Oct 02 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.6-1
- Update to 7.2.6

* Wed Jul 27 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.5-1
- Update to 7.2.5

* Sun Jun 26 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.4-1
- Update to 7.2.4

* Sat Jun 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.3-1
- Update to 7.2.3

* Fri Mar 18 2016 Laurent Rineau <lrineau@renoir.geometryfactory.com> - 7.2.2-2
- Remove the BR qt4-devel

* Tue Mar 08 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.2.2-1
- Update to 7.2.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.1.10-1
- Update to 7.1.10
- Added BR: qt5-qtbase-devel
- Minor spec file clean up

* Thu Oct 29 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.1.9-1
- Updated to 7.1.9

* Tue Oct 06 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.1.8-1
- Updated to latest upstream version
- Updated source to point to github
- Update package URL
- Added libjpeg-turbo-devel as BR

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 7.1.7-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 29 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.1.7-1
- Update to 7.1.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 7.1.5-1
- Updated to latest upstream version
- Added BuildRequires for turbojpeg-devel

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug  5 2013 Laurent Rineau <lrineau@renoir.geometryfactory.com> - 7.1.4-1
- New upstream release

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 7.1.2-4
- Remove --vendor from desktop-file-install for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 7.1.2-1
- Release 7.1.2, fix FTBFS since F-12

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.10-5
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 13 2010  <Laurent.Rineau__fedora@normalesup.org> - 7.0.10-2
- Fix URL, following rules from https://fedoraproject.org/wiki/Packaging:SourceURL#Sourceforge.net

* Tue Jan 12 2010  <Laurent.Rineau__fedora@normalesup.org> - 7.0.10-1
- New upstream major version

* Sun Jan 10 2010  <Laurent.Rineau__fedora@normalesup.org> - 6.0-0.33.pre32patch1%{?dist}
- Update URL of Source0

* Thu Aug 20 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 6.0-0.32.pre32patch1%{?dist}
- New upstream release
- ipe5toxml no longer shipped
- Patch ipe-6.0pre30-pdftex1.40.patch is obsoleted

* Thu Aug 20 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 6.0-0.31.pre30%{?dist}
- Requires tex(latex) instead of tetex (replaced by TeXLive)
- Add default attributes (error reported by rpmlint)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.30.pre30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009  <Laurent.Rineau__fedora@normalesup.org> - 6.0-0.29.pre30%{?dist}
- noarch ipe-doc

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.28.pre30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 28 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.27.pre30%{?dist}
- Add an upstream patch (Patch2), that should fix the incompatibility with
  pdfTeX-1.40 (TeXLive 2007), which is in Fedora 9.

* Tue Mar  4 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.25.pre30%{?dist}
- Fix the URL: tag. (rebuild needed)

* Thu Feb 14 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.24.pre30%{?dist}
- Fixes for gcc-4.3.

* Tue Dec  4 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.23.pre30%{?dist}
- New upstream release.
- Patch "pre28-patch1" is now obsolete.
- Change the License: tag, to states that there is an exception for
  CGAL. The license is now "GPLv2+ with exceptions".

* Sat Nov 17 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.22.pre28%{?dist}
- Make ipe use xdg-open (from package xdg-utils), instead of htmlview.

* Mon Sep 17 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.21.pre28%{?dist}
- New upstream patch.

* Mon Aug 27 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.20.pre28%{?dist}
- Change the URL, in Source0.

* Fri Aug 24 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.19.pre28%{?dist}
- New patch: no longer check the version of freetype at runtime

* Fri Aug 24 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 6.0-0.18.pre28%{?dist}
- New License: tag.
- Rebuild for F-8.

* Wed Jan 17 2007 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.17.pre28
- Provides ipe(api)

* Wed Jan 17 2007 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.15.pre28
- New upstream version.
- Patch4 is no longer needed.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 6.0-0.14.pre27
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.13.pre27
- Add BR: pkgconfig.

* Tue Sep 26 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.12.pre27
- New upstream version.
- Remove Patch0 (ipe-6.0pre26-printf-size_t), fixed upstream.
- Remove Patch1 (ipe-6.0pre26-ipelet-pro_files), fixed upstream.
- Remove Patch2 (ipe-6.0pre26-initui.cpp), fixed upstream.
- Remove Patch3 (ipe-6.0pre26-libpath), fixed upstream.

* Thu Aug 31 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.11.pre26
- New try to rebuild ipe-6.0pre26 for FC-6 mass rebuild.
- New patch: ipe_6.0pre26-qmake-defines.patch
  This patch changes the dealing of macros whose values should contain double
  quotes (needed under FC-6, which has qmake-4.2).
- New comments around the patches, to describe them.

* Mon Aug 28 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.10.pre26
- Rebuild for FC-6.

* Thu Jul 20 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.9.pre26
- Remove the BR: nas-devel, now that qt4 has stripped -laudio from its pkgconfig files.

* Thu Jul 20 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.8.pre26
- New patch ipe_6.0pre26-libpath.patch, to be able to compile ipe even if another version is installed.
  This patch make use LIBPATH instead of explicit flags such as "-L../../build/lib/", in pro files.
- Modification of ipe_6.0pre26-ipelet-pro_files.patch, so that CONFIG+="plugin", and never CONFIG+="qt plugin", in ipelets pro files.
- Temporarely, add BuildRequires: nas-devel. qt4-devel should require it.

* Tue Jul  4 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.7.pre26
- In %%files, use libipe.so.1*, instead of libipe.so.*
- Make sub-package %%{name}-doc depend on %%{name}

* Wed Jun 28 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.6.pre26
- Added a patch, ipe_6.0pre26-initui.cpp.patch, to fix temporarely an upstream bug: QMenu aboutToshow() signal has a lowercase "a".

* Tue Jun 20 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.5.pre26
- New patch ipe-6.0pre26-ipelet-pro_files.patch: fix the pro files of ipelets: the configshould be "plugin" instead of "dll".
- Cleanup of the %%files directives: do not own directories which are created by the main package in subpackages.

* Sun May 28 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.4.pre26
- No longer hardcode qt4 prefix. Use pkg-config instead.

* Sun May 21 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.3.pre26
- Added a desktop file for Ipe.

* Sun May 21 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.2.pre26
- Fix directories ownership.
- ipelets/*.so are now in -devel.
- Creation of -doc subpackage.

* Tue May  9 2006 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 6.0-0.1.pre26
- Initial revision.
