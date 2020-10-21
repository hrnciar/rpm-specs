%{?mingw_package_header}

%global pkgname qscintilla
%global scintilla_ver 3.5.4

Name:          mingw-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Version:       2.11.5
Release:       1%{?dist}
BuildArch:     noarch

License:       GPLv3
Url:           http://www.riverbankcomputing.com/software/qscintilla/
Source0:       https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla-%{version}.tar.gz

# Tweak python bindings configure script for mingw
Patch0:        qscintilla_configure.patch

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-python3
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qtscript
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-python3-qt5

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-python3
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qtscript
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-python3-qt5

Provides: bundled(scintilla) = %{scintilla_ver}


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 library

%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 library.


%package -n mingw32-python3-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 Python 3 bindings
Requires:      mingw32-%{pkgname}-qt5 = %{version}-%{release}
Requires:      mingw32-python3-qt5

%description -n mingw32-python3-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 Python 3 bindings.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 library

%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 library.


%package -n mingw64-python3-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 Python 3 bindings
Requires:      mingw64-%{pkgname}-qt5 = %{version}-%{release}
Requires:      mingw64-python3-qt5

%description -n mingw64-python3-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 Python 3 bindings.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n QScintilla-%{version}


%build
cp -a Qt4Qt5 Qt5/
pushd Qt5
%mingw_qmake_qt5 ../qscintilla.pro
%mingw_make %{?_smp_mflags}
popd

# Python3
cp -a Python Qt5_Python3_win32
pushd Qt5_Python3_win32
%{mingw32_python3} configure.py \
    --pyqt=PyQt5 \
    --sip=/usr/bin/mingw32-sip \
    --qmake=%{mingw32_qmake_qt5} \
    --qsci-incdir=../Qt5 --qsci-libdir=../Qt5/build_win32/release \
    --verbose
%mingw32_make %{?_smp_mflags}
popd

cp -a Python Qt5_Python3_win64
pushd Qt5_Python3_win64
%{mingw64_python3} configure.py \
    --pyqt=PyQt5 \
    --sip=/usr/bin/mingw64-sip \
    --qmake=%{mingw64_qmake_qt5} \
    --qsci-incdir=../Qt5 --qsci-libdir=../Qt5/build_win64/release \
    --verbose
%mingw64_make %{?_smp_mflags}
popd



%install
pushd Qt5
%mingw_make install INSTALL_ROOT=%{buildroot}
popd
%mingw32_make install INSTALL_ROOT=%{buildroot} -C Qt5_Python3_win32
%mingw64_make install INSTALL_ROOT=%{buildroot} -C Qt5_Python3_win64

%find_lang qscintilla --with-qt
grep "%{mingw32_datadir}/qt5/translations" qscintilla.lang > mingw32-qscintilla-qt5.lang
grep "%{mingw64_datadir}/qt5/translations" qscintilla.lang > mingw64-qscintilla-qt5.lang

# Fix library names and installation folders
mkdir -p %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw32_libdir}/qscintilla2_qt5.dll %{buildroot}%{mingw32_bindir}/qscintilla2_qt5.dll

mkdir -p %{buildroot}%{mingw64_bindir}
mv %{buildroot}%{mingw64_libdir}/qscintilla2_qt5.dll %{buildroot}%{mingw64_bindir}/qscintilla2_qt5.dll

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-%{pkgname}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-%{pkgname}.debugfiles


%files -n mingw32-%{pkgname}-qt5 -f mingw32-qscintilla-qt5.lang -f mingw32-%{pkgname}.debugfiles
%license LICENSE
%{mingw32_bindir}/qscintilla2_qt5.dll
%{mingw32_libdir}/libqscintilla2_qt5.dll.a
%{mingw32_includedir}/qt5/Qsci/
%{mingw32_datadir}/qt5/mkspecs/features/qscintilla2.prf

%files -n mingw32-python3-%{pkgname}-qt5 -f mingw32-%{pkgname}.debugfiles
%{mingw32_python3_sitearch}/PyQt5/Qsci.py*
%{mingw32_python3_sitearch}/QScintilla-%{version}.dist-info/
%{mingw32_datadir}/qt5/qsci/
%{mingw32_datadir}/sip/PyQt5/Qsci


%files -n mingw64-%{pkgname}-qt5 -f mingw64-qscintilla-qt5.lang -f mingw64-%{pkgname}.debugfiles
%license LICENSE
%{mingw64_bindir}/qscintilla2_qt5.dll
%{mingw64_libdir}/libqscintilla2_qt5.dll.a
%{mingw64_includedir}/qt5/Qsci/
%{mingw64_datadir}/qt5/mkspecs/features/qscintilla2.prf

%files -n mingw64-python3-%{pkgname}-qt5 -f mingw64-%{pkgname}.debugfiles
%{mingw64_python3_sitearch}/PyQt5/Qsci.py*
%{mingw64_python3_sitearch}/QScintilla-%{version}.dist-info/
%{mingw64_datadir}/qt5/qsci/
%{mingw64_datadir}/sip/PyQt5/Qsci


%changelog
* Wed Jul 29 2020 Sandro Mani <manisandro@gmail.com> - 2.11.5-1
- Update to 2.11.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 2.11.2-9
- Rebuild (python-3.9)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-7
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Sep 30 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-6
- Rebuild (python 3.8)

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-5
- Drop python2 bindings

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-3
- Fix another incorrect requires

* Mon Jul 22 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-2
- Fix incorrect requires

* Fri Jul 19 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-1
- Update to 2.11.2

* Thu May 02 2019 Sandro Mani <manisandro@gmail.com> - 2.11.1-2
- Fix debug file in non-debug subpackage
- Add python3 subpackages
- Drop Qt4 build support

* Mon Feb 18 2019 Sandro Mani <manisandro@gmail.com> - 2.11.1-1
- Update to 2.11.1

* Wed Feb 13 2019 Sandro Mani <manisandro@gmail.com> - 2.11-1
- Update to 2.11

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 2.10.8-1
- Update to 2.10.8

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 2.10.7-1
- Update to 2.10.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Sandro Mani <manisandro@gmail.com> - 2.10.4-1
- Update to 2.10.4

* Thu Mar 08 2018 Sandro Mani <manisandro@gmail.com> - 2.10.3-1
- Update to 2.10.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Sandro Mani <manisandro@gmail.com> - 2.10.2-1
- Update to 2.10.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 2.10.1-3
- Rebuild (mingw-filesystem)

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 2.10.1-2
- Disable qt4 build by default

* Thu Aug 10 2017 Sandro Mani <manisandro@gmail.com> - 2.10.1-1
- Update to 2.10.1

* Tue May 09 2017 Sandro Mani <manisandro@gmail.com> - 2.10.0-2
- Add Qt5 python bindings

* Thu Apr 20 2017 Sandro Mani <manisandro@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Tue Jan 17 2017 Sandro Mani <manisandro@gmail.com> - 2.9.4-1
- Update to 2.9.4

* Fri Jan 22 2016 Sandro Mani <manisandro@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Thu Aug 13 2015 Sandro Mani <manisandro@gmail.com> - 2.9-2
- Enable python bindings

* Fri Jun 26 2015 Sandro Mani <manisandro@gmail.com> - 2.9-1
- Initial package
