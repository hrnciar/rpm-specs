%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

# Building with LTO on will lead to segfaults at start
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1883675
# Disabling LTO now until upstream fix
%define _lto_cflags             %{nil}

Name:           texworks
Version:        0.6.5
Release:        6%{?dist}
Summary:        A simple IDE for authoring TeX documents

License:        GPLv2+
URL:            http://tug.org/texworks/
Source0:        https://github.com/TeXworks/texworks/archive/release-%{version}/texworks-release-%{version}.tar.gz

# Fix for FTBTS with Qt 5.15.1
# See: https://koji.fedoraproject.org/koji/taskinfo?taskID=51256818
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1883675
Patch0:         0001-Fix-build-for-qt-5.15.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  hunspell-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  lua-devel
BuildRequires:  desktop-file-utils
BuildRequires:  cmake

# Description adopted from Debian with modification
%description
TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc) documents,
with a Unicode-based, TeX-aware editor, integrated PDF viewer, and a clean,
simple interface accessible to casual and non-technical users.

You may install the texlive-* packages to make this program useful.

%prep
%setup -q -n %{name}-release-%{version}
%patch0 -p1

%build
%cmake -DWITH_PYTHON=ON -DTW_BUILD_ID=Fedora -DTeXworks_DIC_DIR=%{_datadir}/myspell -DTeXworks_PLUGIN_DIR=%{_libdir}/texworks -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
rm %{buildroot}/%{_docdir}/%{name}/COPYING

%files
%license COPYING
%{_docdir}/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/TeXworks*
%{_datadir}/metainfo/*


%changelog
* Wed Sep 30 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0.6.5-6
- fixes #1883675 by disabling LTO
- added a fix for FTBTS with QT 5.15

* Mon Aug 03 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 0.6.5-5
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.5-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5

* Wed Mar 18 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4
- Drop switches for Qt4 and Python2

* Tue Feb 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.6.3-6
- Filter private shared libraries

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.6.3-4
- Rebuild for poppler-0.84.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.3-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3 (BZ#1689560)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.6.2-15
- Switch to Python 3 for Fedora 30

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 0.6.2-14
- Rebuild for poppler-0.67.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 0.6.2-12
- Rebuild for poppler-0.63.0

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.6.2-11
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Wed Feb 14 2018 David Tardon <dtardon@redhat.com> - 0.6.2-10
- rebuild for poppler 0.62.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> - 0.6.2-8
- Rebuild for hunspell 1.6.2

* Wed Nov 08 2017 David Tardon <dtardon@redhat.com> - 0.6.2-7
- rebuild for poppler 0.61.0

* Fri Oct 06 2017 David Tardon <dtardon@redhat.com> - 0.6.2-6
- rebuild for poppler 0.60.1

* Fri Sep 08 2017 David Tardon <dtardon@redhat.com> - 0.6.2-5
- rebuild for poppler 0.59.0

* Thu Aug 03 2017 David Tardon <dtardon@redhat.com> - 0.6.2-4
- rebuild for poppler 0.57.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May  4 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Tue Mar 28 2017 David Tardon <dtardon@redhat.com> - 0.6.1-9
- rebuild for poppler 0.53.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 David Tardon <dtardon@redhat.com> - 0.6.1-7
- rebuild for poppler 0.50.0

* Tue Dec 13 2016 Caolán McNamara <caolanm@redhat.com> - 0.6.1-6
- Rebuild for hunspell 1.5.4

* Thu Nov 24 2016 Orion Poplawski <orion@cora.nwra.com> - 0.6.1-5
- Rebuild for poppler 0.49.0

* Fri Oct 21 2016 Marek Kasik <mkasik@redhat.com> - 0.6.1-4
- Rebuild for poppler-0.48.0

* Mon Jul 18 2016 Marek Kasik <mkasik@redhat.com> - 0.6.1-3
- Rebuild for poppler-0.45.0

* Tue May  3 2016 Marek Kasik <mkasik@redhat.com> - 0.6.1-2
- Rebuild for poppler-0.43.0

* Sun May  1 2016 Robin Lee <cheeselee@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Mon Apr 18 2016 Caolán McNamara <caolanm@redhat.com> - 0.6.0-2
- rebuild for hunspell 1.4.0

* Sun Apr 10 2016 Robin Lee <cheeselee@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Marek Kasik <mkasik@redhat.com> - 0.4.6-5
- Rebuild for poppler-0.40.0

* Wed Jul 22 2015 Marek Kasik <mkasik@redhat.com> - 0.4.6-4
- Rebuild (poppler-0.34.0)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.4.6-2
- Fix Qt4/ARM build with Tw_ARM2.patch
- Use Qt5 on Fedora >= 22

* Sat Apr 11 2015 Robin Lee <cheeselee@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.4.5-3
- Use unversioned docdir (BZ#993945)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.4.5-1
- Update to 0.4.5

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.4.4-2
- Rebuild (poppler-0.20.0)

* Tue May  8 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4 (#785100, #817511)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.4.3-3
- Rebuild (poppler-0.17.3)

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 0.4.3-2
- Rebuild (poppler-0.17.0)

* Thu Jul 14 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3 (BZ#718982)

* Sun Jun 26 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2
- Removed texworks-0.4.1-qmake.patch

* Tue Jun  7 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.1-2
- Include an upstreamed qmake configuration patch
- Fix myspell path
- Install the manual to path specified upstream

* Mon May 30 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1
- Obsolete texworks-0.4.0-64bit.patch, since default qmake configuration works
  with PPC64 now
- BR: dbus-devel removed

* Wed May 25 2011 Caolán McNamara <caolanm@redhat.com> - 0.4.0-3
- rebuild for new hunspell

* Wed Mar 30 2011 Dan Horák <dan[at]danny.cz> - 0.4.0-2
- fix build on non-x86 64-bit platforms

* Fri Mar 25 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
- Use uptream desktop entry file

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Apr 24 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.2.3-3
- Move to menu category 'Office'
- License tag revised to 'GPLv2+'
- Initial import to Fedora repositories

* Thu Apr 22 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.2.3-2
- Fix some strange characters in README
- Patch TeXworks.pro to use qmake mechanism to install files and fix DSO linking
  problem

* Sun Apr 11 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.2.3-1
- Initial packaging
