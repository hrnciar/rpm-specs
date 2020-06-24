# https://github.com/anonbeat/guayadeque/commit/ed0b3ca443a26e4fa804dc5e577983eceb481bb5
%global commit0 ed0b3ca443a26e4fa804dc5e577983eceb481bb5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20200528

Name:           guayadeque
Version:        0.4.7
Release:        0.15.%{gitdate}git%{shortcommit0}%{?dist}
Summary:        Music player

# The entire source code is GPLv3+ except hmac/ which is BSD
# and ApeTag.* TagInfo.* which is LGPLv2+
License:        GPLv3+ and BSD and LGPLv2+ and wxWidgets
URL:            http://guayadeque.org/
Source0:        https://github.com/anonbeat/guayadeque/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
# For a breakdown of the licensing, see PACKAGE-LICENSING
Source1:        PACKAGE-LICENSING

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  taglib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgpod-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sqlite-devel
BuildRequires:  wxGTK3-devel
BuildRequires:  wxsqlite3-devel
BuildRequires:  dbus-devel
BuildRequires:  gettext-devel

Provides:       bundled(md5-polstra)

%description
Guayadeque is a music management program designed for all music enthusiasts. It
is Full Featured Linux media player that can easily manage large collections
and uses the Gstreamer media framework.

%define         lang_subpkg() \
%package        langpack-%{1}\
Summary:        %{2} language data for %{name}\
BuildArch:      noarch \
Requires:       %{name} = %{version}-%{release}\
Supplements:    (%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description    langpack-%{1}\
%{2} language data for %{name}.\
\
%files          langpack-%{1}\
%{_datadir}/locale/%{1}*/LC_MESSAGES/%{name}.mo

%lang_subpkg bg Bulgarian
%lang_subpkg ca_ES Catalan
%lang_subpkg cs Czech
%lang_subpkg da Danish
%lang_subpkg de German
%lang_subpkg el Greek
%lang_subpkg es Spanish
%lang_subpkg fr French
%lang_subpkg hr Croatian
%lang_subpkg hu Hungarian
%lang_subpkg is Icelandic
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg lt Lithuanian
%lang_subpkg ms "Malay (Malaysia)"
%lang_subpkg nb Norwegian
%lang_subpkg nl Dutch
%lang_subpkg pl Polish
%lang_subpkg pt Portuguese
%lang_subpkg pt_BR Brazil
%lang_subpkg ru Russian
%lang_subpkg sk Slovakian
%lang_subpkg sr "Serbian (Cyrillic and Latin)"
%lang_subpkg sv Swedish
%lang_subpkg th Thai
%lang_subpkg tr Turkish
%lang_subpkg uk Ukrainian

%prep
%autosetup -p0 -n %{name}-%{commit0}
cp -p %{SOURCE1} PACKAGE-LICENSING

%build
%cmake .                                                       \
 -DCMAKE_BUILD_TYPE='Debug'                                    \
 -DwxWidgets_CONFIG_EXECUTABLE='%{_bindir}/wx-config-3.0'      \
 -DCMAKE_EXE_LINKER_FLAGS:STRING=-lwx_gtk3u_aui-3.0            \
 -DCMAKE_CXX_FLAGS="%{optflags}"                               \
 -D_GUREVISION_:STRING='%{shortcommit0}'
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/{applications,appdata}
desktop-file-install --delete-original  \
        --dir %{buildroot}%{_datadir}/applications   \
        --remove-category Application \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%doc README
%license LICENSE PACKAGE-LICENSING
%{_bindir}/%{name}
%{_datadir}/%{name}/*.conf
%{_datadir}/%{name}/*.xml
%dir %{_datadir}/%{name}
%exclude %{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.4.7-0.15.20200528gited0b3ca
- Rebuild (jsoncpp)

* Thu May 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.14.20200528gited0b3ca
- Update to 0.4.7-0.14.20200528gited0b3ca

* Sun May 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.13.20200524gita066689
- Update to 0.4.7-0.13.20200524gita066689

* Sat May 23 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.12.20200522git41564bd
- Update to 0.4.7-0.12.20200522git41564bd

* Wed May 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.11.20200520git6be35ba
- Update to 0.4.7-0.11.20200520git6be35ba

* Fri May 08 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.10.20200507gitb08bddd
- Update to 0.4.7-0.10.20200507gitb08bddd
- Add BR pkgconfig(jsoncpp)

* Thu May 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.9.20200507git3d4ee2b
- Update to 0.4.7-0.9.20200507git3d4ee2b

* Mon Apr 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.8.20200427git42f77b6
- Update to 0.4.7-0.8.20200427git42f77b6

* Fri Apr 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.7.20200417git7de91e5
- Update to 0.4.7-0.7.20200417git7de91e5

* Thu Apr 16 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.6.20200415git08fe80e
- Update to 0.4.7-0.6.20200415git08fe80e

* Tue Feb 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.5.20200123git3ef808d
- Rebuilt

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-0.4.20200122git3ef808d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.3.20200123git3ef808d
- Update to 0.4.7-0.3.20200123git3ef808d

* Sun Dec 08 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.2.20191208git71b5e35
- Update to 0.4.7-0.2.20191208git71b5e35

* Fri Nov 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.7-0.1.20191117git89c6ab2
- Update to 0.4.7-0.1.20191117git89c6ab2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.6-1
- Update to stable 0.4.6

* Thu May 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.22.beta1gitddb8cbe
- Update to 0.4.5-0.22.beta1gitddb8cbe

* Tue Apr 16 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.21.beta1git093f588
- Update to 0.4.5-0.21.beta1git093f588

* Fri Apr 12 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.20.beta1gitdfc4acb
- Update to 0.4.5-0.20.beta1gitdfc4acb
- Add -DCMAKE_EXE_LINKER_FLAGS:STRING=-lwx_gtk3u_aui-3.0 due missing aui library

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.19.beta1git3b64a58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.18.beta13b64a58
- Update to 0.4.5-0.18.beta13b64a58

* Thu Sep 20 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.17.beta19688c4d
- Update to 0.4.5-0.17.beta19688c4d

* Thu Sep 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.16.beta1fa7ab20
- Update to 0.4.5-0.16.beta1gitfa7ab20

* Fri Aug 24 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.15.beta1gite7257da
- Update to 0.4.5-0.15.beta1gite7257da

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.14.beta1gitb3a7ec3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.13.beta1gitb3a7ec3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.12.beta1gitb3a7ec3
- Update to 0.4.5-0.12.beta1gitb3a7ec3

* Thu Oct 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.11.beta1git55efd99
- Update to 0.4.5-0.11.beta1git55efd99

* Sat Oct 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.10.beta1gitf4cd389
- Update to 0.4.5-0.10.beta1gitf4cd389

* Thu Aug 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.9.beta1git8137051
- Update to 0.4.5-0.9.beta1git8137051

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.8.beta1git35eaa95
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.7.beta1git35eaa95
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.6.beta1git35eaa95
- Update to 0.4.5-0.6.beta1git35eaa95

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-0.5.beta1gitc2d3854
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.4.beta1gitc2d3854
- Update to 0.4.5-0.4.beta1gitc2d3854

* Tue Jan 31 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.3.beta1gitfcf165e
- Update to 0.4.5-0.3.beta1gitfcf165e
- first version with proxy support

* Sun Jan 08 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.2.beta1git9fec4f7
- Update to 0.4.5-0.2.beta1git9fec4f7

* Sat Nov 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.5-0.1.beta1git5def972
- Update to 0.4.5-0.1.beta1git5def972

* Fri Nov 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.3-0.2.beta1git1943e6e
- Update to 0.4.3-0.2.beta1git1943e6e

* Fri Nov 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.3-0.1.beta1gitaf526c9
- Update to 0.4.3-0.1.beta1gitaf526c9

* Tue Nov 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.17.beta1git8706c86
- Update to 0.4.1-0.17.beta1git8706c86

* Sat Oct 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.16.beta1git45a439f
- Update to 0.4.1-0.16.beta1git45a439f

* Mon Oct 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.15.beta1gitf3a156b
- Update to 0.4.1-0.15.beta1gitf3a156b

* Thu Aug 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.14.beta1git6a66f9b
- Update to 0.4.1-0.14.beta1git6a66f9b

* Fri Jul 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.13.beta1gita2ae83e
- Update to 0.4.1-0.13.beta1gita2ae83e

* Mon Jul 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.12.beta1git2dbffbc
- Update to 0.4.1-0.12.beta1git2dbffbc
- First version with audio cd support
- Changed BR from gstreamer1-devel to gstreamer1-plugins-base-devel

* Wed Jun 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.11.beta1git1bc65f9
- Update to 0.4.1-0.11.beta1git1bc65f9
- Added BR libappstream-glib
- Added appdata.xml file
- Spec file cleanup

* Sat Jun 18 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.10.beta1git2420c01
- Update to 0.4.1-0.10.beta1git2420c01

* Mon Jun 13 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.9.beta1gitf6b11ba
- Dropped Provides: bundled(wxcurl) = wxcurl_version
  wxcurl was replaced by libcurl library directly
- Update to 0.4.1-0.9.beta1gitf6b11ba

* Wed Jun 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.8.beta1gitce1ab15
- Update to 0.4.1-0.8.beta1gitce1ab15

* Sun Jun 05 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.7.beta1git79b6383
- Documented licensing breakdown
- Added Provides: bundled(wxcurl) = wxcurl_version

* Sat Jun 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.6.beta1git79b6383
- Update to 0.4.1-0.6.beta1git79b6383
- Added wxWidgets to License tag
- Added %%dir %%{_datadir}/%%{name} because it's owned by the package
- modified macro for l10n subpackage

* Mon May 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.5.beta1git26eaf8d
- Update to 0.4.1-0.5.beta1git26eaf8d

* Wed May 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.4.beta1git13013ff
- Update to 0.4.1-0.4.beta1git13013ff
- Split locales into a l10n subpackage

* Sun May 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.3.beta1git35561f6
- Update to 0.4.1-0.3.beta1git35561f6
- Dropped BR subversion-devel
- Removed Group tag, it's obsolete
- Addes %%{name}-desktop.patch
- Dropped -DCMAKE_INSTALL_PREFIX='%%{_prefix}' because it's already in %%cmake macro 
- Changed -DCMAKE_BUILD_TYPE='Release' to -DCMAKE_BUILD_TYPE='Debug'

* Sun May 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.2.beta1gitd2c0281
- Update to 0.4.1-0.2.beta1gitd2c0281
- Mark license files as %%license where available
- Cleanup spec file

* Sat May 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-0.1.beta1git65f759c
- Update to 0.4.1-0.1.beta1git65f759c

* Sat Jul 04 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-10.svn1894
- rebuild for new svn release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-9.svn1893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.7-8.svn1893
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 05 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-7.svn1893
- dropped CMAKE_INSTALL_PREFIX because already sets by %%cmake macro
- rebuild for new wxsqlite3 version

* Fri Jan 09 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-6.svn1893
- added timeline patch to avoid crash on pause or stop

* Mon Jan 05 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-5.svn1893
- rebuild for new wxsqlite3 version

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-4.svn1893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.7-3.svn1893
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-2.svn1893
- rebuild for new svn release

* Tue Apr 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.7-1.svn1891
- removed flac dependencies
- rebuild for new release

* Sat Jan 18 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-19.svn1890
- rebuild for new svn release

* Fri Jan 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-18.svn1889
- rebuild for new svn release

* Tue Dec 3 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-17.svn1887
- rebuild for new svn release
- added compiler flag to suppress "-Wno-unused-local-typedefs" warnings

* Tue Oct 22 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-16.svn1885
- added correct license type
- removed tabs in the spec file
- added %%desktop-database because desktop entry has a 'MimeType key.
- removing .svn directory will now used before building the tarball

* Mon Oct 21 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-15.svn1885
- added command to remove .svn dirs
- added %%cmake option for svn revision

* Mon Oct 14 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-14.svn1885
- rebuild
- corrected url address

* Wed Feb 13 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-13.svn1872
- rebuild

* Wed Dec 26 2012 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-12.svn1858
- removed %%cmake flags for wxsqlite3
- rebuild
- spec file cleanup

* Sun Dec 23 2012 Martin Gansser <martinkg@fedoraproject.org> - 0.3.6-11.svn1858
- rebuild for new svn release

* Sat Dec 1 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-10.svn1848
- changed %%cmake flag for new wxsqlite3 version 
- rebuild for new release 

* Sat Nov 24 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-9.svn1845
- update CMakeLists.patch and unbundle-wxsqlite3.patch for fedora 17 / 18

* Sat Nov 24 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-8.svn1845
- added wxsqlite3 build requirenment
- added CMakeLists.patch
- changed cmake flags
- spec file cleanup
- rebuild for new svn release

* Sun Oct 21 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-7.svn1830
- added unbundle-wxsqlite3.patch
- added command to remove src/wx/wxsql* src/wxsqlite3 from source

* Sat Sep 15 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-6.svn1830
- used %%{name} in file section
- removed unnecessary Requirements

* Sun Sep 9 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-5.svn1830
- added BSD license for HMAC-SHA implementation

* Sat Sep 8 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-4.svn1830
- removed  gcc-c++ build requirement
- removed %%defattr from file section

* Fri Sep 7 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-3.svn1830
- added patch for DSO linker problem on fedora 19
- added missing build requirements

* Tue Sep 4 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-2.svn1830
- changed release tag
- changed to buildroot variante
- removed uneeded macro _pkgbuilddir
- added Provides: bundled(md5-polstra)

* Thu Aug 30 2012 Martin Gansser <linux4martin@gmx.de> - 0.3.6-2.svn1830
-  initial release for Fedora17 

