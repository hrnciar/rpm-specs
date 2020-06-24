%if 0%{?fedora}  || 0%{?rhel} < 8
%global _with_qt4      1
%endif

%global commit0 ad9bc4600ce769a8b3ad10910803cd555811b70c

Summary:    Qt library to start applications only once per user
Name:       qtsingleapplication
Version:    2.6.1
Release:    38%{?dist}

License:    GPLv3 or LGPLv2 with exceptions
URL:        http://doc.qt.digia.com/solutions/4/qtsingleapplication/qtsingleapplication.html
Source0:    https://github.com/qtproject/qt-solutions/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
# Proposed upstream in https://codereview.qt-project.org/#/c/92417/
Source1:    qtsingleapplication.prf
# Proposed upstream in https://codereview.qt-project.org/#/c/92416/
Source2:    qtsinglecoreapplication.prf
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source3:    LICENSE.GPL3
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source4:    LICENSE.LGPL
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source5:    LGPL_EXCEPTION

# Proposed upstream in https://codereview.qt-project.org/#/c/92416/
Patch0:     qtsingleapplication-build-qtsinglecoreapplication.patch
# Proposed upstream in https://codereview.qt-project.org/#/c/92415/
Patch1:     qtsingleapplication-remove-included-qtlockedfile.patch

# Features for unbundling in Qupzilla, https://github.com/QupZilla/qupzilla/issues/1503
Patch2:     qtsingleapplication-qupzilla.patch

%{?_with_qt4:BuildRequires: qt4-devel qtlockedfile-devel}
BuildRequires: qt5-qtbase-devel qtlockedfile-qt5-devel

%description
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

The QtSingleApplication class provides an interface to detect a running
instance, and to send command strings to that instance.

%if 0%{?_with_qt4}
%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   qt4-devel

%description devel
This package contains libraries and header files for developing applications
that use QtSingleApplication.

%package -n qtsinglecoreapplication
Summary:    Qt library to start applications only once per user
Requires:   qt4

%description -n qtsinglecoreapplication
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

For console (non-GUI) applications, the QtSingleCoreApplication variant
is provided, which avoids dependency on QtGui.

%package -n qtsinglecoreapplication-devel
Summary:    Development files for qtsinglecoreapplication
Requires:   qtsinglecoreapplication = %{version}-%{release}
Requires:   qt4-devel

%description -n qtsinglecoreapplication-devel
This package contains libraries and header files for developing applications
that use QtSingleCoreApplication.
%endif

%package qt5
Summary:    Qt5 library to start applications only once per user
Requires:   qt5-qtbase

%description qt5
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

This is a special build against Qt5.

%package qt5-devel
Summary:    Development files for %{name}-qt5
Requires:   %{name}-qt5 = %{version}-%{release}
Requires:   qt5-qtbase-devel

%description qt5-devel
This package contains libraries and header files for developing applications
that use QtSingleApplication with Qt5.

%package -n qtsinglecoreapplication-qt5
Summary:    Qt library to start applications only once per user (Qt5)
Requires:   qt5-qtbase

%description -n qtsinglecoreapplication-qt5
For some applications it is useful or even critical that they are started
only once by any user. Future attempts to start the application should
activate any already running instance, and possibly perform requested
actions, e.g. loading a file, in that instance.

For console (non-GUI) applications, the QtSingleCoreApplication variant
is provided, which avoids dependency on QtGui.

This is a special build against Qt5.

%package -n qtsinglecoreapplication-qt5-devel
Summary:    Development files for qtsinglecoreapplication-qt5
Requires:   qtsinglecoreapplication-qt5 = %{version}-%{release}
Requires:   qt5-qtbase-devel

%description -n qtsinglecoreapplication-qt5-devel
This package contains libraries and header files for developing applications
that use QtSingleCoreApplication.


%prep
%setup -qnqt-solutions-%{commit0}/%{name}
%patch0 -p0
%patch1 -p0
%patch2 -p1
# use versioned soname
sed -i "s,head,%(echo '%{version}' |sed -r 's,(.*)\..*,\1,'),g" common.pri

mkdir licenses
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} licenses

# We already disabled bundling this external library.
# But just to make sure:
rm -rf ../qtlockedfile/
sed -i 's,qtlockedfile\.h,QtSolutions/\0,' src/qtlocalpeer.h
rm src/{QtLocked,qtlocked}*

mkdir qt5
cp -p %{SOURCE1} %{SOURCE2} qt5
sed -i -r 's,-lQt,\05,' qt5/qtsingleapplication.prf
sed -i -r 's,-lQt,\05,' qt5/qtsinglecoreapplication.prf

# additional header needed for Qt5.5
sed -i -r 's,.include,\0 <QtCore/QDataStream>\n\0,' src/qtlocalpeer.h


%build
# Does not use GNU configure
./configure -library
%if 0%{?_with_qt4}
%{qmake_qt4}
%make_build
%endif
pushd qt5
%{qmake_qt5} ..
%make_build
popd


%install
# libraries
mkdir -p %{buildroot}%{_libdir}
cp -a lib/* %{buildroot}%{_libdir}
chmod 755 %{buildroot}%{_libdir}/*.so*

# headers
%if 0%{?_with_qt4}
mkdir -p %{buildroot}%{_qt4_headerdir}/QtSolutions
cp -ap \
    src/qtsingleapplication.h \
    src/QtSingleApplication \
    src/qtsinglecoreapplication.h \
    src/QtSingleCoreApplication \
    %{buildroot}%{_qt4_headerdir}/QtSolutions
mkdir -p %{buildroot}%{_qt5_headerdir}
# symlink is not possible due to split into individual subpackages
cp -ap %{buildroot}%{_qt4_headerdir}/QtSolutions %{buildroot}%{_qt5_headerdir}

mkdir -p %{buildroot}%{_qt4_datadir}/mkspecs/features %{buildroot}%{_qt5_archdatadir}/mkspecs/features
install -p -m644 %{SOURCE1} %{SOURCE2} %{buildroot}%{_qt4_datadir}/mkspecs/features
install -p -m644 qt5/*.prf %{buildroot}%{_qt5_archdatadir}/mkspecs/features
%else
mkdir -p %{buildroot}%{_qt5_headerdir}/QtSolutions %{buildroot}%{_qt5_archdatadir}/mkspecs/features
cp -ap \
    src/qtsingleapplication.h \
    src/QtSingleApplication \
    src/qtsinglecoreapplication.h \
    src/QtSingleCoreApplication \
    %{buildroot}%{_qt5_headerdir}/QtSolutions
install -p -m644 qt5/*.prf %{buildroot}%{_qt5_archdatadir}/mkspecs/features
%endif

%if 0%{?_with_qt4}
%ldconfig_scriptlets

%files
%license licenses/*
%doc README.TXT
# Caution! Unversioned .so file goes into -devel
%{_qt4_libdir}/libQtSolutions_SingleApplication*.so.*

%files devel
%doc doc/html/ examples/
%{_qt4_libdir}/libQtSolutions_SingleApplication*.so
%dir %{_qt4_headerdir}/QtSolutions/
%{_qt4_headerdir}/QtSolutions/QtSingleApplication
%{_qt4_headerdir}/QtSolutions/%{name}.h
%{_qt4_datadir}/mkspecs/features/qtsingleapplication.prf

%ldconfig_scriptlets -n qtsinglecoreapplication

%files -n qtsinglecoreapplication
%license licenses/*
# Caution! Unversioned .so file goes into -devel
%{_qt4_libdir}/libQtSolutions_SingleCoreApplication*.so.*

%files -n qtsinglecoreapplication-devel
%{_qt4_libdir}/libQtSolutions_SingleCoreApplication*.so
%dir %{_qt4_headerdir}/QtSolutions/
%{_qt4_headerdir}/QtSolutions/QtSingleCoreApplication
%{_qt4_headerdir}/QtSolutions/qtsinglecoreapplication.h
%{_qt4_datadir}/mkspecs/features/qtsinglecoreapplication.prf
%endif

%ldconfig_scriptlets qt5

%files qt5
%license licenses/*
%doc README.TXT
# Caution! Unversioned .so file goes into -devel
%{_qt5_libdir}/libQt5*SingleApplication*.so.*

%files qt5-devel
%doc doc/html/ examples/
%{_qt5_libdir}/libQt5*SingleApplication*.so
%dir %{_qt5_headerdir}/QtSolutions/
%{_qt5_headerdir}/QtSolutions/QtSingleApplication
%{_qt5_headerdir}/QtSolutions/%{name}.h
%{_qt5_archdatadir}/mkspecs/features/qtsingleapplication.prf

%ldconfig_scriptlets -n qtsinglecoreapplication-qt5

%files -n qtsinglecoreapplication-qt5
%license licenses/*
# Caution! Unversioned .so file goes into -devel
%{_qt5_libdir}/libQt5*SingleCoreApplication*.so.*

%files -n qtsinglecoreapplication-qt5-devel
%{_qt5_libdir}/libQt5*SingleCoreApplication*.so
%dir %{_qt5_headerdir}/QtSolutions/
%{_qt5_headerdir}/QtSolutions/QtSingleCoreApplication
%{_qt5_headerdir}/QtSolutions/qtsinglecoreapplication.h
%{_qt5_archdatadir}/mkspecs/features/qtsinglecoreapplication.prf


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Leigh Scott <leigh123linux@gmail.com> - 2.6.1-37
- Add option to disable qt4 build which is needed for epel8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.6.1-34
- use %make_build %%ldconfig_scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.6.1-28
- qtsinglecoreapplication should not imply widgets

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.6.1-26
- Rebuild

* Mon Sep 14 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-25
- fix versioned soname

* Sun Sep 13 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-24
- new upstream snapshot
- switch to GitHub (rhbz#1254883)
- remove upstreamed patch for QTBUG-44595

* Fri Jul 24 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-23
- simplify .qrf files, patching for qt5 is done in spec

* Thu Jul 23 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-22
- fix qt5/mkspecs again for QTBUG-44595 (rhbz#1239870)

* Mon Jul 20 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-21
- fix qt5/mkspecs
- remove obsolete clean

* Mon Jul 20 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-20
- add features for Qupzilla (rhbz#1091704)

* Mon Jul 20 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-19
- fix for QTBUG-44595
- additional header inclusion for Qt5.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Rex Dieter <rdieter@fedoraproject.org> 2.6.1-17
- .prf: use versioned libs for linking

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.6.1-16
- .prf: use QT_INSTALL_HEADERS instead, drop DEPENDPATH

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.6.1-15
- fix/simplify qt5 mkspecs/features install path
- more insurance bundled qtlockedfile is not used

* Mon Apr 27 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-14
- bump Release to identicate BR fixes

* Sat Apr 25 2015 Raphael Groner <projects.rg@smart.ms> - 2.6.1-13
- use latest commit hash of dedicated folder at upstream
- build subpackage for Qt5
- remove deprecated spec file entries
- use license macro and improve license patches
- replace with new buildroot macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.6.1-11
- Update to current repository
- Clean patches

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.6.1-6
- gcc-4.7 compilation fix

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.6.1-4
- Make the additional API patch backwards compatible

* Wed Jul 21 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.6.1-3
- Split the qtsinglecoreapplication bits into their own subpackages

* Fri Jul 16 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.6.1-2
- Add additional API to support clementine.

* Fri Jun 04 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.6.1-1
- Change version to 2.6.1. Upstream uses weird version convention 2.6_1
- Own the directory %%{_qt4_headerdir}/QtSolutions/

* Sat May 01 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.6-3
- Add comments to the extra source and patches
- Add a chmod 755 to make sure that the library gets the right permission

* Thu Apr 15 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.6-2
- Include .prf file
- Don't bundle external qtlockedfile library
- Fix typo in the description

* Sun Apr 11 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.6-1
- Initial Fedora package. Specfile partly borrowed from opensuse

* Thu Dec  3 2009 Todor Prokopov <koprok@nand.bg>
- Initial package.
