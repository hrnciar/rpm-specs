%?mingw_package_header

%global qt_module qtquickcontrols
#global pre beta

#global commit 9f085b889524a80d4064d6ac01dbdc817bb31060
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
Summary:        Qt5 for Windows - QtQuickControls component

License:        GPLv3 with exceptions or LGPLv2 with exceptions
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}
BuildRequires:  mingw32-qt5-qmldevtools-devel = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}
BuildRequires:  mingw64-qt5-qmldevtools-devel = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtQuickControls component
Requires:       mingw32-qt5-qtdeclarative

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-static
Summary:       Static version of the mingw32-qt5-qtquickcontrols library
Requires:      mingw32-qt5-%{qt_module} = %{version}-%{release}
Requires:      mingw32-qt5-qtbase-static
Requires:      mingw32-qt5-qtdeclarative-static

%description -n mingw32-qt5-%{qt_module}-static
Static version of the mingw32-qt5-qtquickcontrols library.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtQuickControls component
Requires:       mingw64-qt5-qtdeclarative

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-static
Summary:       Static version of the mingw64-qt5-qtquickcontrols library
Requires:      mingw64-qt5-%{qt_module} = %{version}-%{release}
Requires:      mingw64-qt5-qtbase-static
Requires:      mingw64-qt5-qtdeclarative-static

%description -n mingw64-qt5-%{qt_module}-static
Static version of the mingw64-qt5-qtquickcontrols library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif


%build
MINGW_BUILDDIR_SUFFIX=_static %mingw_qmake_qt5 ../%{qt_module}.pro CONFIG+=static
MINGW_BUILDDIR_SUFFIX=_static %mingw_make %{?_smp_mflags}

MINGW_BUILDDIR_SUFFIX=_shared %mingw_qmake_qt5 ../%{qt_module}.pro CONFIG+=shared
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make %{?_smp_mflags}


%install
MINGW_BUILDDIR_SUFFIX=_static %mingw_make install INSTALL_ROOT=%{buildroot}
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make install INSTALL_ROOT=%{buildroot}

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
%dir %{mingw32_libdir}/qt5/qml/QtQuick/
%{mingw32_libdir}/qt5/qml/QtQuick/Controls/
%{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/
%{mingw32_libdir}/qt5/qml/QtQuick/Extras/
%{mingw32_libdir}/qt5/qml/QtQuick/PrivateWidgets/
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.a
%exclude %{mingw32_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.a

%files -n mingw32-qt5-%{qt_module}-static
%{mingw32_libdir}/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.a

# Win64
%files -n mingw64-qt5-%{qt_module} -f mingw64-qt5-%{qt_module}.excludes
%license LICENSE.LGPL* LICENSE.GPL*
%dir %{mingw64_libdir}/qt5/qml/QtQuick/
%{mingw64_libdir}/qt5/qml/QtQuick/Controls/
%{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/
%{mingw64_libdir}/qt5/qml/QtQuick/Extras/
%{mingw64_libdir}/qt5/qml/QtQuick/PrivateWidgets/
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.a
%exclude %{mingw64_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.a

%files -n mingw64-qt5-%{qt_module}-static
%{mingw64_libdir}/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/libdialogplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.a


%changelog
* Wed Apr 08 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-1
- Update to 5.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-1
- Update to 5.13.2

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

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-1
- Update to 5.9.1

* Wed Jun 28 2017 Sandro Mani <manisandro@gmail.com> - 5.9.0-1
- Update to 5.9.0

* Tue May 09 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-2
- Rebuild for dropped 0022-Allow-usage-of-static-version-with-CMake.patch in qtbase

* Thu May 04 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-1
- Update to 5.8.0

* Mon Mar 06 2017 Martin Bříza <mbriza@redhat.com> - 5.7.1-2
- Renamed the specfile to match package name

* Mon Mar 06 2017 Martin Bříza <mbriza@redhat.com> - 5.7.1-1
- Update to 5.7.1
- Add a -static subpackage

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Martin Bříza <mbriza@redhat.com> - 5.6.0-2
- Specfile tweaks

* Fri Jul 29 2016 Przemysław Palacz <pprzemal@gmail.com> - 5.6.0-1
- Update to 5.6.0

* Wed Mar 23 2016 Przemysław Palacz <pprzemal@gmail.com> - 5.5.1-2
- Rebuilt against latest mingw-qt5-qtbase

* Mon Mar 07 2016 Przemysław Palacz <pprzemal@gmail.com> - 5.5.1-1
- Update to 5.5.1

* Tue Mar 24 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0

* Sun May 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0
- Make sure the .dll.a files are included in the main packages

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Sun Jan 12 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-2
- Don't carry .dll.debug files in main package

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Fri Nov 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-0.1.rc1
- Initial release

