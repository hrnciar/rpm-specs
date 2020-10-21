%if 0%{?fedora} || 0%{?rhel} < 8
%global _with_qt4      1
%endif

%global commit0	   5a07df503a6f01280f493cbcc2aace462b9dee57
%global commitdate 20150629

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:	QFile extension with advisory locking functions
Name:		qtlockedfile
Version:	2.4
Release:	33.%{commitdate}git%{shortcommit0}%{?dist}

License:	GPLv3 or LGPLv2 with exceptions
URL:		http://doc.qt.digia.com/solutions/4/qtlockedfile/qtlockedfile.html
Source0:	https://github.com/qtproject/qt-solutions/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
Source1:	qtlockedfile.prf
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source2:	LICENSE.LGPL
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source3:	LGPL_EXCEPTION
# Proposed upstream in https://codereview.qt-project.org/#/c/92411/
Source4:	LICENSE.GPL3
%{?_with_qt4:BuildRequires:	qt4-devel}
BuildRequires:	qt5-qtbase-devel

%description
This class extends the QFile class with inter-process file locking capabilities.
If an application requires that several processes should access the same file,
QtLockedFile can be used to easily ensure that only one process at a time is
writing to the file, and that no process is writing to it while others are
reading it.

%if 0%{?_with_qt4}
%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt4-devel

%description devel
This package contains libraries and header files for developing applications
that use QtLockedFile.
%endif

%package qt5
Summary:	QFile extension with advisory locking functions (Qt5)
Requires:	qt5-qtbase

%description qt5
This class extends the QFile class with inter-process file locking capabilities.
If an application requires that several processes should access the same file,
QtLockedFile can be used to easily ensure that only one process at a time is
writing to the file, and that no process is writing to it while others are
reading it.
This is a special build against Qt5.

%package qt5-devel
Summary:	Development files for %{name}-qt5
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	qt5-qtbase-devel

%description qt5-devel
This package contains libraries and header files for developing applications
that use QtLockedFile with Qt5.


%prep
%setup -qn qt-solutions-%{commit0}/%{name}
# use versioned soname
sed -i s,head,%{version}, common.pri
# do not build example source
sed -i /example/d %{name}.pro
mkdir licenses
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} licenses


%build
# Does not use GNU configure
./configure -library
%if 0%{?_with_qt4}
%{qmake_qt4}
%make_build
%endif
mkdir qt5
pushd qt5
%{qmake_qt5} ..
%make_build
popd

%install
# libraries
mkdir -p %{buildroot}%{_libdir}
cp -ap lib/* %{buildroot}%{_libdir}

# headers
%if 0%{?_with_qt4}
mkdir -p %{buildroot}%{_qt4_headerdir}/QtSolutions %{buildroot}%{_qt5_headerdir}
cp -ap src/qtlockedfile.h src/QtLockedFile %{buildroot}%{_qt4_headerdir}/QtSolutions
cp -ap %{buildroot}%{_qt4_headerdir}/QtSolutions %{buildroot}%{_qt5_headerdir}
install -p -D -m644 %{SOURCE1} %{buildroot}%{_qt4_datadir}/mkspecs/features/qtlockedfile.prf
install -p -D -m644 %{SOURCE1} %{buildroot}%{_qt5_archdatadir}/mkspecs/features/qtlockedfile.prf
%else
mkdir -p %{buildroot}%{_qt5_headerdir}/QtSolutions
cp -ap src/qtlockedfile.h src/QtLockedFile %{buildroot}%{_qt5_headerdir}/QtSolutions
install -p -D -m644 %{SOURCE1} %{buildroot}%{_qt5_archdatadir}/mkspecs/features/qtlockedfile.prf 
%endif

%if 0%{?_with_qt4}
%ldconfig_scriptlets

%files
%license licenses/*
%doc README.TXT
# Caution! do not include any unversioned .so symlink (belongs to -devel)
%{_qt4_libdir}/libQtSolutions_LockedFile*.so.*

%files devel
%doc doc/html/ example/
%{_qt4_headerdir}/QtSolutions/
%{_qt4_libdir}/libQtSolutions_LockedFile*.so
%{_qt4_datadir}/mkspecs/features/qtlockedfile.prf
%endif

%ldconfig_scriptlets qt5

%files qt5
%license licenses/*
%doc README.TXT
# Caution! do not include any unversioned .so symlink (belongs to -devel)
%{_qt5_libdir}/libQt5Solutions_LockedFile*.so.*

%files qt5-devel
%doc doc/html/ example/
%{_qt5_headerdir}/QtSolutions/
%{_qt5_libdir}/libQt5Solutions_LockedFile*.so
%{_qt5_archdatadir}/mkspecs/features/qtlockedfile.prf


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-33.20150629git5a07df5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-32.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-31.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Leigh Scott <leigh123linux@gmail.com> - 2.4-30.20150629git5a07df5
- Add option to disable qt4 build which is needed for epel8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-29.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-28.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.4-27.20150629git5a07df5
- use %%make_build %%ldconfig_scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-26.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-25.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-24.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-23.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-22.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-21.20150629git5a07df5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.4-20.20160120git5a07df5
- Rebuild

* Sun Oct 11 2015 Raphael Groner <projects.rg@smart.ms> - 2.4-19.20150629git5a07df5
- rebuilt

* Mon Jul 27 2015 Raphael Groner <projects.rg@smart.ms> - 2.4-18.20150629git5a07df5
- apply Qt5 fixes of upstream (rhbz#1239869)
- use sources from github instead of gitlab
- remove obsoleted patches
- simplify installation of header files

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Rex Dieter <rdieter@fedoraproject.org> 2.4-16
- qtlockedfile.prf: use versioned lib for linking

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.4-15
- qtlockedfile.prf: use QT_INSTALL_HEADERS instead, drop DEPENDPATH

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.4-14
- fix/simplify qt5 mkspecs/features install path

* Sun Apr 26 2015 Raphael Groner <projects.rg@smart.ms> - 2.4-13
- readd lost patch

*  Sat Apr 25 2015 Raphael Groner <projects.rg@smart.ms> - 2.4-12
- add Qt5 build
- use latest commit of dedicated source folder
- remove upstreamed patch
- replace buildroot macro
- remove deprecated spec entries

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.4-10
- Fix conflicting license files
 
* Thu Aug 14 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.4-9
- Update to Digia's repository

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.4-2
- Remove unnecessary linkage to libQtGui

* Thu Apr 15 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 2.4-1
- Initial Fedora package.
