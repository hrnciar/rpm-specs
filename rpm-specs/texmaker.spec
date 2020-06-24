Summary:	LaTeX editor
Name:		texmaker
Version:	5.0.4
Release:	4%{?dist}
Epoch:		1
License:	GPLv2+
URL:		http://www.xm1math.net/texmaker/
Source:		http://www.xm1math.net/texmaker/texmaker-%{version}.tar.bz2

BuildRequires:	qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	qt5-qtscript-devel
BuildRequires:	qtsingleapplication-qt5-devel
BuildRequires:	poppler-qt5-devel
BuildRequires:	hunspell-devel
BuildRequires:	zlib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib

Requires:	tetex-latex
Requires:	tetex-dvipost

# setup the .pro file to unbundle qtsingleapplication and hunspell
# also fixes a single header file to use system singleapp
Patch0:		%{name}-5.x-unbundle-qtsingleapp.patch
# fix header files to use system hunspell
Patch1:		%{name}-5.x-unbundle-hunspell.patch
# use system pdf viewers instead of hardcoded evince
Patch2:		%{name}-5.x-viewfiles.patch

%description
Texmaker is a program, that integrates many tools needed to develop 
documents with LaTeX, in just one application. 
Texmaker runs on unix, macosx and windows systems and is released under the GPL
license

%prep
%setup -q
%patch0
%patch1
%patch2

# get rid of zero-length space
sed -i 's/\xe2\x80\x8b//g' utilities/%{name}.appdata.xml

# remove bundled stuff (hunspell and qtsingleapplication)
rm -fr hunspell singleapp


%build
%{qmake_qt5} texmaker.pro
%make_build

%install
# cannot use make_install macro - inappropriate
make INSTALL_ROOT=%{buildroot} install INSTALL="install -p"

install -Dp -m 0644 utilities/texmaker16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker22x22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/texmaker.png

# Don't package these twice
rm -rf %{buildroot}%{_datadir}/%{name}/{AUTHORS,COPYING,*.desktop,tex*.png}
rm -f %{buildroot}%{_datadir}/applications/texmaker.desktop

desktop-file-install 		\
	--dir %{buildroot}%{_datadir}/applications	\
	--remove-category Publishing			\
	--remove-category X-SuSE-Core-Office		\
	--remove-category X-Mandriva-Office-Publishing	\
	--remove-category X-Misc			\
	utilities/texmaker.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%ldconfig_scriptlets

%files
%license utilities/COPYING
%doc utilities/AUTHORS doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.0.4-4
- rebuild (qt5)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 1:5.0.4-2
- rebuild

* Sun Jan 05 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:5.0.4-1
- Update to 5.0.4

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1:5.0.3-7
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1:5.0.3-6
- rebuild (qt5)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1:5.0.3-4
- rebuild (qt5)

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.0.3-3
- rebuild (qt5)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:5.0.3-11
- Update to 5.0.3

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.0.2-11
- rebuild (qt5)

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 1:5.0.2-10
- rebuild for hunspell 1.7.0

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 1:5.0.2-9
- rebuild (qt5)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-7
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.0.2-6
- rebuild (qt5)

* Tue May 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:5.0.2-5
- Drop tetex-xdvi
- use ldconfig_script macro

* Sun Feb 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.0.2-4
- rebuild (qt5)

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.0.2-3
- track qt5 private api usage

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> - 1:5.0.2-2
- rebuild for hunspell 1.6.2

* Wed Sep 27 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:5.0.2-1
- Update to 5.0.2
- update patches to current version
- Add appdata file
- minor spec cleanup

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:4.5-1
- Update to version 4.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.4.1-4
- use qtsingleapplication-qt5 (#1217888), use %%qmake_qt5 macro

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:4.4.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Dec 21 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:4.4.1-2
- Reapply DE indepenedent application choice patch

* Sun Dec 21 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:4.4.1-1
- Update to latest version - 4.4.1

* Sat Dec 06 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:4.4-1
- Update to latest version 4.4
- Unbundle qtsingleapplication and use system lib
- spec file clean up

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1:4.3-1
- Updated to latest upstream release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Deji Akingunola <dakingun@gmail.com> - 4.2-1
- Disable system qtsingleapplication for now, as it doesn't support Qt5

* Mon May 19 2014 Deji Akingunola <dakingun@gmail.com> - 4.2-1
- Update to version 4.2
- Switch to building with Qt5
- Use system qtsingleapplication instead of bundled one (Patch by Ville SkyttÃ¤,BZ #1091069)

* Sat Mar 08 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.1.1-2
- Rebuild against fixed qt to fix -debuginfo (#1074041)

* Tue Mar 04 2014 Deji Akingunola <dakingun@gmail.com> - 4.1.1-1
- Update to version 4.1.1

* Sat Aug 10 2013 Deji Akingunola <dakingun@gmail.com> - 4.0.3-1
- Update to 4.0.3
- Apply patch to build on arm

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Deji Akingunola <dakingun@gmail.com> - 4.0.2-1
- Update to 4.0.2

* Fri Feb 22 2013 Deji Akingunola <dakingun@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 3.5-2
- Remove vendor tag from desktop file
- spec clean up

* Thu Sep 20 2012 Deji Akingunola <dakingun@gmail.com> - 3.5-1
- Update to 3.5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 3.2.2-2
- Rebuild (poppler-0.20.0)

* Fri Jan 27 2012 Deji Akingunola <dakingun@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 3.1-2
- Rebuild (poppler-0.17.3)

* Sat Aug 27 2011 Deji Akingunola <dakingun@gmail.com> - 3.1-1
- Update to 3.1

* Thu Apr 28 2011 Deji Akingunola <dakingun@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Tue Mar 29 2011 Deji Akingunola <dakingun@gmail.com> - 2.3-1
- Update to 2.3

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 1:2.1-5
- Rebuild (poppler-0.16.3)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 1:2.1-3
- rebuild (poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.1-2
- rebuild (poppler)

* Sun Nov 07 2010 Deji Akingunola <dakingun@gmail.com> - 2.1-1
- Update to 2.1

* Sat Nov 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0-4
- rebuilt (poppler)

* Tue Sep 28 2010 Deji Akingunola <dakingun@gmail.com> - 1:2.0-3
- Rebuild for poppler-0.15.

* Fri Aug 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 1:2.0-2
- rebuild (poppler)

* Fri Aug 06 2010 Deji Akingunola <dakingun@gmail.com> - 2.0-1
- Update to 2.0

* Wed Feb 03 2010 Deji Akingunola <dakingun@gmail.com> - 1.9.9-1
- Update to 1.9.9

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.2-4
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Mon Nov 02 2009 Deji Akingunola <dakingun@gmail.com> - 1.9.2-3
- Update with a more complete patch to use system hunspell (Caolan McNamara)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Deji Akingunola <dakingun@gmail.com> - 1.9.2-1
- New Release

* Wed May 27 2009 Deji Akingunola <dakingun@gmail.com> - 1.9.1-1
- New Release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Deji Akingunola <dakingun@gmail.com> - 1.8-1
- New Release

* Wed Jun 04 2008 Deji Akingunola <dakingun@gmail.com> - 1.7.1-1
- A bug-fix release

* Mon Apr 28 2008 Deji Akingunola <dakingun@gmail.com> - 1.7-1
- New Release

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 1.6-4
- Rebuild for gcc43

* Sat Aug 18 2007 Deji Akingunola <dakingun@gmail.com> - 1:1.6-3
- Use xdg-open instead of hardcording apps (bz#245269)

* Mon Aug 06 2007 Deji Akingunola <dakingun@gmail.com> - 1:1.6-3
- License tag update

* Thu Jun 21 2007 Deji Akingunola <dakingun@gmail.com> - 1:1.6-2%{?dist}
- Change default dvi viewer back to xdvi, and require tetex-xdvi for it

* Thu Jun 21 2007 Deji Akingunola <dakingun@gmail.com> - 1:1.6-1%{?dist}
- New Release

* Fri Jun 15 2007 Deji Akingunola <dakingun@gmail.com> - 1.5-2
- Fix for crash on x86_64 by Kevin Kofler (BZ #235546)

* Tue Jan 02 2007 Deji Akingunola <dakingun@gmail.com> - 1.5-1
- New release

* Tue Aug 29 2006 Deji Akingunola <dakingun@gmail.com> - 1.4-1
- Update to 1.4
- Add patch by Rex Dieter to enable build with qt4-4.2

* Thu May 25 2006 Deji Akingunola <dakingun@gmail.com> - 1.3-1
- Updated to 1.3 - had to add epoch to facilitate an upgrade
- New version depends on qt4
- Explicitly add tetex-dvips Requires

* Mon Feb 13 2006 Deji Akingunola <dakingun@gmail.com> - 1.12-4
- Rebuild for Fedora Extras 5

* Fri Oct 28 2005 Deji Akingunola <dakingun@gmail.com> - 1.12-3 
- Buildrequires qt-devel instead of kdelibs-devel
- Fix typos in desktop file patch
- Use use the '-p' option in the install command (Rex Dieter)

* Thu Oct 27 2005 Deji Akingunola <dakingun@gmail.com> - 1.12-2 
- Miscellaneous fixes to the spec files from Fedora Extras review,
  RH bugzilla #171195 (Aurelien Bompard)

* Sat Apr 30 2005 Deji Akingunola <dakingun@gmail.com> - 1.12-1 
- Initial release for Extras
