%{?mingw_package_header}

%global qt_module qtmultimedia
#global pre beta

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.14.2
Release:        1%{?dist}
Summary:        Qt5 for Windows - QtMultimedia component

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License:        GPLv3 with exceptions or LGPLv2 with exceptions
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-angleproject >= 0-0.16.git8613f49
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}
BuildRequires:  mingw32-openal-soft

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-angleproject >= 0-0.16.git8613f49
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}
BuildRequires:  mingw64-openal-soft


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtMultimedia component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtMultimedia component

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif


%build
%mingw_qmake_qt5 ../%{qt_module}.pro
%mingw_make %{?_smp_mflags}


%install
%mingw_make install INSTALL_ROOT=%{buildroot}

# .prl files aren't interesting for us
find %{buildroot} -name "*.prl" -delete

# Create a list of .dll.debug files which need to be excluded from the main packages
# We do this to keep the %%files section as clean/readable as possible (otherwise every
# single file and directory would have to be mentioned individually in the %%files section)
# Note: the .dll.debug files aren't created yet at this point (as it happens after
# the %%install section). Therefore we have to assume that all .dll files will
# eventually get a .dll.debug counterpart
find %{buildroot}%{mingw32_prefix} | grep .dll | grep -v .dll.a | sed s@"^%{buildroot}"@"%%exclude "@ | sed s/".dll\$"/".dll.debug"/ > mingw32-qt5-%{qt_module}.excludes
find %{buildroot}%{mingw64_prefix} | grep .dll | grep -v .dll.a | sed s@"^%{buildroot}"@"%%exclude "@ | sed s/".dll\$"/".dll.debug"/ > mingw64-qt5-%{qt_module}.excludes


# Win32
%files -n mingw32-qt5-%{qt_module} -f mingw32-qt5-%{qt_module}.excludes
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt5Multimedia.dll
%{mingw32_bindir}/Qt5MultimediaQuick.dll
%{mingw32_bindir}/Qt5MultimediaWidgets.dll
%{mingw32_includedir}/qt5/QtMultimedia/
%{mingw32_includedir}/qt5/QtMultimediaQuick/
%{mingw32_includedir}/qt5/QtMultimediaWidgets/
%{mingw32_libdir}/libQt5Multimedia.dll.a
%{mingw32_libdir}/libQt5MultimediaQuick.dll.a
%{mingw32_libdir}/libQt5MultimediaWidgets.dll.a
%{mingw32_libdir}/cmake/Qt5Multimedia/
%{mingw32_libdir}/cmake/Qt5MultimediaQuick/
%{mingw32_libdir}/cmake/Qt5MultimediaWidgets/
%{mingw32_libdir}/pkgconfig/Qt5Multimedia.pc
%{mingw32_libdir}/pkgconfig/Qt5MultimediaWidgets.pc
%{mingw32_libdir}/qt5/plugins/audio/
%{mingw32_libdir}/qt5/plugins/mediaservice/
%{mingw32_libdir}/qt5/plugins/playlistformats/
%{mingw32_libdir}/qt5/qml/QtMultimedia/
%{mingw32_libdir}/qt5/qml/QtAudioEngine/
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_multimedia.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module} -f mingw64-qt5-%{qt_module}.excludes
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5Multimedia.dll
%{mingw64_bindir}/Qt5MultimediaQuick.dll
%{mingw64_bindir}/Qt5MultimediaWidgets.dll
%{mingw64_includedir}/qt5/QtMultimedia/
%{mingw64_includedir}/qt5/QtMultimediaQuick/
%{mingw64_includedir}/qt5/QtMultimediaWidgets/
%{mingw64_libdir}/libQt5Multimedia.dll.a
%{mingw64_libdir}/libQt5MultimediaQuick.dll.a
%{mingw64_libdir}/libQt5MultimediaWidgets.dll.a
%{mingw64_libdir}/cmake/Qt5Multimedia/
%{mingw64_libdir}/cmake/Qt5MultimediaQuick/
%{mingw64_libdir}/cmake/Qt5MultimediaWidgets/
%{mingw64_libdir}/pkgconfig/Qt5Multimedia.pc
%{mingw64_libdir}/pkgconfig/Qt5MultimediaWidgets.pc
%{mingw64_libdir}/qt5/plugins/audio/
%{mingw64_libdir}/qt5/plugins/mediaservice/
%{mingw64_libdir}/qt5/plugins/playlistformats/
%{mingw64_libdir}/qt5/qml/QtMultimedia/
%{mingw64_libdir}/qt5/qml/QtAudioEngine/
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_multimedia.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri


%changelog
* Wed Apr 08 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-1
- Update to 5.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-1
- Update to 5.13.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Sep 26 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-1
- Update to 5.12.5

* Tue Aug 27 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-3
- Rebuild to fix pkg-config files (#1745257)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-1
- Update to 5.12.4

* Thu Apr 18 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-1
- Update to 5.12.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Sandro Mani <manisandro@gmail.com> - 5.11.3-1
- Update to 5.11.3

* Sun Sep 23 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-1
- Update to 5.11.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Sandro Mani <manisandro@gmail.com> - 5.11.1-1
- Update to 5.11.1

* Wed May 30 2018 Sandro Mani <manisandro@gmail.com> - 5.11.0-1
- Update to 5.11.0

* Fri Feb 16 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-1
- Update to 5.10.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Sandro Mani <manisandro@gmail.com> - 5.10.0-1
- Update to 5.10.0

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 5.9.3-1
- Update to 5.9.3

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-1
- Update to 5.9.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-2
- Rebuild for mingw-angleproject-0-0.19.git8613f49

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-1
- Update to 5.9.1

* Wed Jun 28 2017 Sandro Mani <manisandro@gmail.com> - 5.9.0-1
- Update to 5.9.0

* Tue May 09 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-2
- Rebuild for dropped 0022-Allow-usage-of-static-version-with-CMake.patch in qtbase

* Thu May 04 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-1
- Update to 5.8.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Sandro Mani <manisandro@gmail.com> - 5.7.1-1
- Update to 5.7.1

* Thu Apr  7 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-1
- Update to 5.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-1
- Update to 5.5.1

* Fri Aug  7 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 22 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1

* Tue Dec 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0

* Sat Sep 20 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.2-1
- Update to 5.3.2

* Tue Jul  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Sun Mar 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-2
- Make sure we're built against mingw-qt5-qtbase >= 5.2.1 (RHBZ 1077213)

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-3
- Previous commit caused .dll.a files to disappear

* Sun Jan 12 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-2
- Don't carry .dll.debug files in main package

* Wed Jan  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0
- Dropped manual rename of import libraries
- Added license

* Fri Nov 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-0.1.rc1
- Update to 5.2.0 RC1

* Sun Jul 14 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Fri May 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2

* Sat Feb  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Sat Jan 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-1
- Update to Qt 5.0.0 Final

* Mon Nov 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.2.beta1.git20121112.a73dfa7c
- Update to 20121112 snapshot (rev a73dfa7c)
- Rebuild against latest mingw-qt5-qtbase
- Dropped pkg-config rename hack as it's unneeded now

* Wed Sep 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.1.beta1
- Initial release

