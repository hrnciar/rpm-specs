%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_rpmconfigdir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}

%global qt_module qtdeclarative
#global pre rc

#global commit dd1d6b56271caf3f90e536b3ad9dab58c873f202
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
Summary:        Qt5 for Windows - QtDeclarative component

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
License:        GPLv3 with exceptions or LGPLv2 with exceptions
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Build QmlDevTools library as a shared instead of a static library
Patch1:         0001-Build-QML-dev-tools-as-shared-library.patch
Patch2:         0002-Ensure-static-plugins-are-exported.patch
Patch3:         0003-Prevent-exporting-QML-parser-symbols-on-static-build.patch


BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  /usr/bin/python

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtbase-devel = %{version}
BuildRequires:  mingw32-qt5-qtbase-static = %{version}
BuildRequires:  mingw32-bzip2-static
BuildRequires:  mingw32-freetype-static
BuildRequires:  mingw32-graphite2-static
BuildRequires:  mingw32-pcre2-static
BuildRequires:  mingw32-win-iconv-static
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtbase-devel = %{version}
BuildRequires:  mingw64-qt5-qtbase-static = %{version}
BuildRequires:  mingw64-bzip2-static
BuildRequires:  mingw64-freetype-static
BuildRequires:  mingw64-graphite2-static
BuildRequires:  mingw64-pcre2-static
BuildRequires:  mingw64-win-iconv-static
BuildRequires:  mingw64-zlib

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtDeclarative component
BuildArch:      noarch

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%package -n mingw32-qt5-qmldevtools
Summary:       Qt5 for Windows build environment
Requires:      mingw32-qt5-%{qt_module} = %{version}-%{release}

%description -n mingw32-qt5-qmldevtools
Contains the files required to get various Qt tools built
which are part of the mingw-qt5-qttools package


%package -n mingw32-qt5-qmldevtools-devel
Summary:       Qt5 for Windows build environment
Requires:      mingw32-qt5-qmldevtools = %{version}-%{release}

%description -n mingw32-qt5-qmldevtools-devel
Contains the files required to get various Qt tools built
which are part of the mingw-qt5-qttools package


%package -n mingw32-qt5-%{qt_module}-static
Summary:       Static version of the mingw32-qt5-qtdeclarative library
Requires:      mingw32-qt5-qtdeclarative = %{version}-%{release}
Requires:      mingw32-qt5-qtbase-static
BuildArch:     noarch

%description -n mingw32-qt5-%{qt_module}-static
Static version of the mingw32-qt5-qtdeclarative library.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt for Windows - QtDeclarative component
BuildArch:      noarch

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%package -n mingw64-qt5-qmldevtools
Summary:       Qt5 for Windows build environment
Requires:      mingw64-qt5-%{qt_module} = %{version}-%{release}

%description -n mingw64-qt5-qmldevtools
Contains the files required to get various Qt tools built
which are part of the mingw-qt5-qttools package


%package -n mingw64-qt5-qmldevtools-devel
Summary:       Qt5 for Windows build environment
Requires:      mingw64-qt5-qmldevtools = %{version}-%{release}

%description -n mingw64-qt5-qmldevtools-devel
Contains the files required to get various Qt tools built
which are part of the mingw-qt5-qttools package


%package -n mingw64-qt5-%{qt_module}-static
Summary:       Static version of the mingw64-qt5-qtdeclarative library
Requires:      mingw64-qt5-qtdeclarative = %{version}-%{release}
Requires:      mingw64-qt5-qtbase-static
BuildArch:     noarch

%description -n mingw64-qt5-%{qt_module}-static
Static version of the mingw64-qt5-qtdeclarative library.


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

MINGW_BUILDDIR_SUFFIX=_shared %mingw_qmake_qt5 ../%{qt_module}.pro
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make %{?_smp_mflags}


%install
MINGW_BUILDDIR_SUFFIX=_static %mingw_make install INSTALL_ROOT=%{buildroot}
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make install INSTALL_ROOT=%{buildroot}

# .prl files aren't interesting for us
find %{buildroot} -name "*.prl" -delete

# The .dll's are installed in both %%{mingw32_bindir} and %%{mingw32_libdir}
# One copy of the .dll's is sufficient
rm -f %{buildroot}%{mingw32_libdir}/*.dll
rm -f %{buildroot}%{mingw64_libdir}/*.dll

# Prevent file conflict with mingw-qt4
mv %{buildroot}%{mingw32_bindir}/qmlplugindump.exe %{buildroot}%{mingw32_bindir}/qmlplugindump-qt5.exe
mv %{buildroot}%{mingw64_bindir}/qmlplugindump.exe %{buildroot}%{mingw64_bindir}/qmlplugindump-qt5.exe

# Remove unneeded files
rm -f %{buildroot}%{_prefix}/%{mingw32_target}/lib/libQt5QmlDevTools.la
rm -f %{buildroot}%{_prefix}/%{mingw32_target}/lib/pkgconfig/Qt5QmlDevTools.pc
rm -f %{buildroot}%{_prefix}/%{mingw32_target}/lib/libQt5QmlDevTools.a
rm -f %{buildroot}%{_prefix}/%{mingw64_target}/lib/libQt5QmlDevTools.la
rm -f %{buildroot}%{_prefix}/%{mingw64_target}/lib/pkgconfig/Qt5QmlDevTools.pc
rm -f %{buildroot}%{_prefix}/%{mingw64_target}/lib/libQt5QmlDevTools.a

# Create a list of .dll.debug files which need to be excluded from the main packages
# Note: the .dll.debug files aren't created yet at this point (as it happens after
# the %%install section). Therefore we have to assume that all .dll files will
# eventually get a .dll.debug counterpart
find %{buildroot}%{mingw32_libdir}/qt5 | grep .dll\$ | sed s@"^%{buildroot}"@"%%exclude "@ | sed s/".dll\$"/".dll.debug"/ > mingw32-qt5-%{qt_module}.excludes
find %{buildroot}%{mingw64_libdir}/qt5 | grep .dll\$ | sed s@"^%{buildroot}"@"%%exclude "@ | sed s/".dll\$"/".dll.debug"/ > mingw64-qt5-%{qt_module}.excludes


# Win32
%files -n mingw32-qt5-%{qt_module} -f mingw32-qt5-%{qt_module}.excludes
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt5Qml.dll
%{mingw32_bindir}/Qt5QmlModels.dll
%{mingw32_bindir}/Qt5QmlWorkerScript.dll
%{mingw32_bindir}/Qt5Quick.dll
%{mingw32_bindir}/Qt5QuickParticles.dll
%{mingw32_bindir}/Qt5QuickShapes.dll
%{mingw32_bindir}/Qt5QuickTest.dll
%{mingw32_bindir}/Qt5QuickWidgets.dll
%{mingw32_bindir}/qmlplugindump-qt5.exe
%{mingw32_bindir}/qmlscene.exe
%{mingw32_bindir}/qml.exe
%{mingw32_bindir}/qmleasing.exe
%{mingw32_bindir}/qmlpreview.exe
%{mingw32_bindir}/qmlprofiler.exe
%{mingw32_bindir}/qmltestrunner.exe
%{mingw32_includedir}/qt5/QtPacketProtocol/
%{mingw32_includedir}/qt5/QtQml/
%{mingw32_includedir}/qt5/QtQmlDebug/
%{mingw32_includedir}/qt5/QtQmlModels/
%{mingw32_includedir}/qt5/QtQmlWorkerScript/
%{mingw32_includedir}/qt5/QtQuick/
%{mingw32_includedir}/qt5/QtQuickParticles/
%{mingw32_includedir}/qt5/QtQuickShapes/
%{mingw32_includedir}/qt5/QtQuickTest/
%{mingw32_includedir}/qt5/QtQuickWidgets/
%{mingw32_libdir}/libQt5Qml.dll.a
%{mingw32_libdir}/libQt5QmlModels.dll.a
%{mingw32_libdir}/libQt5QmlWorkerScript.dll.a
%{mingw32_libdir}/libQt5Quick.dll.a
%{mingw32_libdir}/libQt5QuickParticles.dll.a
%{mingw32_libdir}/libQt5QuickShapes.dll.a
%{mingw32_libdir}/libQt5QuickTest.dll.a
%{mingw32_libdir}/libQt5QuickWidgets.dll.a
%{mingw32_libdir}/cmake/Qt5PacketProtocol/
%{mingw32_libdir}/cmake/Qt5Qml/
%{mingw32_libdir}/cmake/Qt5QmlDebug/
%{mingw32_libdir}/cmake/Qt5QmlDevTools/
%{mingw32_libdir}/cmake/Qt5QmlImportScanner/
%{mingw32_libdir}/cmake/Qt5QmlModels/
%{mingw32_libdir}/cmake/Qt5QmlWorkerScript/
%{mingw32_libdir}/cmake/Qt5Quick/
%{mingw32_libdir}/cmake/Qt5QuickCompiler/
%{mingw32_libdir}/cmake/Qt5QuickParticles/
%{mingw32_libdir}/cmake/Qt5QuickShapes/
%{mingw32_libdir}/cmake/Qt5QuickTest/
%{mingw32_libdir}/cmake/Qt5QuickWidgets/
%{mingw32_libdir}/pkgconfig/Qt5Qml.pc
%{mingw32_libdir}/pkgconfig/Qt5QmlModels.pc
%{mingw32_libdir}/pkgconfig/Qt5QmlWorkerScript.pc
%{mingw32_libdir}/pkgconfig/Qt5Quick.pc
%{mingw32_libdir}/pkgconfig/Qt5QuickTest.pc
%{mingw32_libdir}/pkgconfig/Qt5QuickWidgets.pc
%dir %{mingw32_libdir}/qt5/plugins/qmltooling/
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_debugger.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_inspector.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_local.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_messages.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_native.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_nativedebugger.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_preview.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_profiler.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_quickprofiler.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_server.dll
%{mingw32_libdir}/qt5/plugins/qmltooling/qmldbg_tcp.dll
%dir %{mingw32_libdir}/qt5/qml
%{mingw32_libdir}/qt5/qml/builtins.qmltypes
%dir %{mingw32_libdir}/qt5/qml/Qt
%dir %{mingw32_libdir}/qt5/qml/Qt/labs
%dir %{mingw32_libdir}/qt5/qml/Qt/labs/animation
%{mingw32_libdir}/qt5/qml/Qt/labs/animation/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/Qt/labs/animation/qmldir
%{mingw32_libdir}/qt5/qml/Qt/labs/animation/labsanimationplugin.dll
%dir %{mingw32_libdir}/qt5/qml/Qt/labs/folderlistmodel
%{mingw32_libdir}/qt5/qml/Qt/labs/folderlistmodel/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/Qt/labs/folderlistmodel/qmldir
%{mingw32_libdir}/qt5/qml/Qt/labs/folderlistmodel/qmlfolderlistmodelplugin.dll
%dir %{mingw32_libdir}/qt5/qml/Qt/labs/qmlmodels
%{mingw32_libdir}/qt5/qml/Qt/labs/qmlmodels/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/Qt/labs/qmlmodels/qmldir
%{mingw32_libdir}/qt5/qml/Qt/labs/qmlmodels/labsmodelsplugin.dll
%dir %{mingw32_libdir}/qt5/qml/Qt/labs/settings
%{mingw32_libdir}/qt5/qml/Qt/labs/settings/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/Qt/labs/settings/qmldir
%{mingw32_libdir}/qt5/qml/Qt/labs/settings/qmlsettingsplugin.dll
%dir %{mingw32_libdir}/qt5/qml/Qt/labs/sharedimage
%{mingw32_libdir}/qt5/qml/Qt/labs/sharedimage/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/Qt/labs/sharedimage/qmldir
%{mingw32_libdir}/qt5/qml/Qt/labs/sharedimage/sharedimageplugin.dll
%dir %{mingw32_libdir}/qt5/qml/Qt/labs/wavefrontmesh
%{mingw32_libdir}/qt5/qml/Qt/labs/wavefrontmesh/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/Qt/labs/wavefrontmesh/qmldir
%{mingw32_libdir}/qt5/qml/Qt/labs/wavefrontmesh/qmlwavefrontmeshplugin.dll
%dir %{mingw32_libdir}/qt5/qml/QtQml
%{mingw32_libdir}/qt5/qml/QtQml/qmlplugin.dll
%{mingw32_libdir}/qt5/qml/QtQml/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQml/qmldir
%dir %{mingw32_libdir}/qt5/qml/QtQml/Models.2
%{mingw32_libdir}/qt5/qml/QtQml/Models.2/modelsplugin.dll
%{mingw32_libdir}/qt5/qml/QtQml/Models.2/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQml/Models.2/qmldir
%dir %{mingw32_libdir}/qt5/qml/QtQml/StateMachine
%{mingw32_libdir}/qt5/qml/QtQml/StateMachine/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQml/StateMachine/qmldir
%{mingw32_libdir}/qt5/qml/QtQml/StateMachine/qtqmlstatemachine.dll
%dir %{mingw32_libdir}/qt5/qml/QtQml/WorkerScript.2
%{mingw32_libdir}/qt5/qml/QtQml/WorkerScript.2/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQml/WorkerScript.2/qmldir
%{mingw32_libdir}/qt5/qml/QtQml/WorkerScript.2/workerscriptplugin.dll
%dir %{mingw32_libdir}/qt5/qml/QtQuick.2
%{mingw32_libdir}/qt5/qml/QtQuick.2/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQuick.2/qmldir
%{mingw32_libdir}/qt5/qml/QtQuick.2/qtquick2plugin.dll
%dir %{mingw32_libdir}/qt5/qml/QtQuick/
%dir %{mingw32_libdir}/qt5/qml/QtQuick/Layouts
%{mingw32_libdir}/qt5/qml/QtQuick/Layouts/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQuick/Layouts/qmldir
%{mingw32_libdir}/qt5/qml/QtQuick/Layouts/qquicklayoutsplugin.dll
%dir %{mingw32_libdir}/qt5/qml/QtQuick/LocalStorage
%{mingw32_libdir}/qt5/qml/QtQuick/LocalStorage/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQuick/LocalStorage/qmldir
%{mingw32_libdir}/qt5/qml/QtQuick/LocalStorage/qmllocalstorageplugin.dll
%dir %{mingw32_libdir}/qt5/qml/QtQuick/Particles.2
%{mingw32_libdir}/qt5/qml/QtQuick/Particles.2/particlesplugin.dll
%{mingw32_libdir}/qt5/qml/QtQuick/Particles.2/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQuick/Particles.2/qmldir
%dir %{mingw32_libdir}/qt5/qml/QtQuick/Shapes
%{mingw32_libdir}/qt5/qml/QtQuick/Shapes/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQuick/Shapes/qmldir
%{mingw32_libdir}/qt5/qml/QtQuick/Shapes/qmlshapesplugin.dll
%dir %{mingw32_libdir}/qt5/qml/QtQuick/Window.2
%{mingw32_libdir}/qt5/qml/QtQuick/Window.2/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtQuick/Window.2/qmldir
%{mingw32_libdir}/qt5/qml/QtQuick/Window.2/windowplugin.dll
%dir %{mingw32_libdir}/qt5/qml/QtTest
%{mingw32_libdir}/qt5/qml/QtTest/SignalSpy.qml
%{mingw32_libdir}/qt5/qml/QtTest/TestCase.qml
%{mingw32_libdir}/qt5/qml/QtTest/plugins.qmltypes
%{mingw32_libdir}/qt5/qml/QtTest/qmldir
%{mingw32_libdir}/qt5/qml/QtTest/qmltestplugin.dll
%{mingw32_libdir}/qt5/qml/QtTest/testlogger.js
%{mingw32_datadir}/qt5/mkspecs/features/qmlcache.prf
%{mingw32_datadir}/qt5/mkspecs/features/qtquickcompiler.prf
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_packetprotocol_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qml.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qml_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qmldebug_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qmldevtools_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qmlmodels.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qmlmodels_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qmltest.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qmltest_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qmlworkerscript.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qmlworkerscript_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_quick.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_quick_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_quickparticles_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_quickshapes_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_quickwidgets.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_quickwidgets_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_debugger.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_inspector.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_local.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_messages.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_native.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_nativedebugger.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_preview.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_profiler.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_quickprofiler.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_server.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_tcp.pri

%files -n mingw32-qt5-qmldevtools
%{_prefix}/%{mingw32_target}/bin/qt5/qmlcachegen
%{_prefix}/%{mingw32_target}/bin/qt5/qmlimportscanner
%{_prefix}/%{mingw32_target}/bin/qt5/qmllint
%{_prefix}/%{mingw32_target}/bin/qt5/qmlmin
%{_prefix}/%{mingw32_target}/lib/libQt5QmlDevTools.so

%files -n mingw32-qt5-qmldevtools-devel
%{_prefix}/%{mingw32_target}/lib/libQt5QmlDevTools.so.5*

%files -n mingw32-qt5-%{qt_module}-static
%{mingw32_libdir}/libQt5PacketProtocol.a
%{mingw32_libdir}/libQt5QmlDebug.a
%{mingw32_libdir}/libQt5Qml.a
%{mingw32_libdir}/libQt5QmlModels.a
%{mingw32_libdir}/libQt5QmlWorkerScript.a
%{mingw32_libdir}/libQt5Quick.a
%{mingw32_libdir}/libQt5QuickParticles.a
%{mingw32_libdir}/libQt5QuickShapes.a
%{mingw32_libdir}/libQt5QuickTest.a
%{mingw32_libdir}/libQt5QuickWidgets.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_debugger.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_inspector.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_local.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_messages.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_native.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_nativedebugger.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_preview.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_profiler.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_quickprofiler.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_server.a
%{mingw32_libdir}/qt5/plugins/qmltooling/libqmldbg_tcp.a
%{mingw32_libdir}/qt5/qml/Qt/labs/animation/liblabsanimationplugin.a
%{mingw32_libdir}/qt5/qml/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.a
%{mingw32_libdir}/qt5/qml/Qt/labs/qmlmodels/liblabsmodelsplugin.a
%{mingw32_libdir}/qt5/qml/Qt/labs/settings/libqmlsettingsplugin.a
%{mingw32_libdir}/qt5/qml/Qt/labs/sharedimage/libsharedimageplugin.a
%{mingw32_libdir}/qt5/qml/Qt/labs/wavefrontmesh/libqmlwavefrontmeshplugin.a
%{mingw32_libdir}/qt5/qml/QtQml/libqmlplugin.a
%{mingw32_libdir}/qt5/qml/QtQml/Models.2/libmodelsplugin.a
%{mingw32_libdir}/qt5/qml/QtQml/StateMachine/libqtqmlstatemachine.a
%{mingw32_libdir}/qt5/qml/QtQml/WorkerScript.2/libworkerscriptplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick.2/libqtquick2plugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Layouts/libqquicklayoutsplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/LocalStorage/libqmllocalstorageplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Particles.2/libparticlesplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Shapes/libqmlshapesplugin.a
%{mingw32_libdir}/qt5/qml/QtQuick/Window.2/libwindowplugin.a
%{mingw32_libdir}/qt5/qml/QtTest/libqmltestplugin.a

# Win64
%files -n mingw64-qt5-%{qt_module} -f mingw64-qt5-%{qt_module}.excludes
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5Qml.dll
%{mingw64_bindir}/Qt5QmlModels.dll
%{mingw64_bindir}/Qt5QmlWorkerScript.dll
%{mingw64_bindir}/Qt5Quick.dll
%{mingw64_bindir}/Qt5QuickParticles.dll
%{mingw64_bindir}/Qt5QuickShapes.dll
%{mingw64_bindir}/Qt5QuickTest.dll
%{mingw64_bindir}/Qt5QuickWidgets.dll
%{mingw64_bindir}/qmlplugindump-qt5.exe
%{mingw64_bindir}/qmlscene.exe
%{mingw64_bindir}/qml.exe
%{mingw64_bindir}/qmleasing.exe
%{mingw64_bindir}/qmlpreview.exe
%{mingw64_bindir}/qmlprofiler.exe
%{mingw64_bindir}/qmltestrunner.exe
%{mingw64_includedir}/qt5/QtPacketProtocol/
%{mingw64_includedir}/qt5/QtQml/
%{mingw64_includedir}/qt5/QtQmlDebug/
%{mingw64_includedir}/qt5/QtQmlModels/
%{mingw64_includedir}/qt5/QtQmlWorkerScript/
%{mingw64_includedir}/qt5/QtQuick/
%{mingw64_includedir}/qt5/QtQuickParticles/
%{mingw64_includedir}/qt5/QtQuickShapes/
%{mingw64_includedir}/qt5/QtQuickTest/
%{mingw64_includedir}/qt5/QtQuickWidgets/
%{mingw64_libdir}/libQt5Qml.dll.a
%{mingw64_libdir}/libQt5QmlModels.dll.a
%{mingw64_libdir}/libQt5QmlWorkerScript.dll.a
%{mingw64_libdir}/libQt5Quick.dll.a
%{mingw64_libdir}/libQt5QuickParticles.dll.a
%{mingw64_libdir}/libQt5QuickShapes.dll.a
%{mingw64_libdir}/libQt5QuickTest.dll.a
%{mingw64_libdir}/libQt5QuickWidgets.dll.a
%{mingw64_libdir}/cmake/Qt5PacketProtocol/
%{mingw64_libdir}/cmake/Qt5Qml/
%{mingw64_libdir}/cmake/Qt5QmlDebug/
%{mingw64_libdir}/cmake/Qt5QmlDevTools/
%{mingw64_libdir}/cmake/Qt5QmlImportScanner/
%{mingw64_libdir}/cmake/Qt5QmlModels/
%{mingw64_libdir}/cmake/Qt5QmlWorkerScript/
%{mingw64_libdir}/cmake/Qt5Quick/
%{mingw64_libdir}/cmake/Qt5QuickCompiler/
%{mingw64_libdir}/cmake/Qt5QuickParticles/
%{mingw64_libdir}/cmake/Qt5QuickShapes/
%{mingw64_libdir}/cmake/Qt5QuickTest/
%{mingw64_libdir}/cmake/Qt5QuickWidgets/
%{mingw64_libdir}/pkgconfig/Qt5Qml.pc
%{mingw64_libdir}/pkgconfig/Qt5QmlModels.pc
%{mingw64_libdir}/pkgconfig/Qt5QmlWorkerScript.pc
%{mingw64_libdir}/pkgconfig/Qt5Quick.pc
%{mingw64_libdir}/pkgconfig/Qt5QuickTest.pc
%{mingw64_libdir}/pkgconfig/Qt5QuickWidgets.pc
%dir %{mingw64_libdir}/qt5/plugins/qmltooling/
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_debugger.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_inspector.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_local.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_messages.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_native.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_nativedebugger.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_preview.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_profiler.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_quickprofiler.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_server.dll
%{mingw64_libdir}/qt5/plugins/qmltooling/qmldbg_tcp.dll
%dir %{mingw64_libdir}/qt5/qml
%{mingw64_libdir}/qt5/qml/builtins.qmltypes
%dir %{mingw64_libdir}/qt5/qml/Qt
%dir %{mingw64_libdir}/qt5/qml/Qt/labs
%dir %{mingw64_libdir}/qt5/qml/Qt/labs/animation
%{mingw64_libdir}/qt5/qml/Qt/labs/animation/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/Qt/labs/animation/qmldir
%{mingw64_libdir}/qt5/qml/Qt/labs/animation/labsanimationplugin.dll
%dir %{mingw64_libdir}/qt5/qml/Qt/labs/folderlistmodel
%{mingw64_libdir}/qt5/qml/Qt/labs/folderlistmodel/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/Qt/labs/folderlistmodel/qmldir
%{mingw64_libdir}/qt5/qml/Qt/labs/folderlistmodel/qmlfolderlistmodelplugin.dll
%dir %{mingw64_libdir}/qt5/qml/Qt/labs/qmlmodels
%{mingw64_libdir}/qt5/qml/Qt/labs/qmlmodels/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/Qt/labs/qmlmodels/qmldir
%{mingw64_libdir}/qt5/qml/Qt/labs/qmlmodels/labsmodelsplugin.dll
%dir %{mingw64_libdir}/qt5/qml/Qt/labs/settings
%{mingw64_libdir}/qt5/qml/Qt/labs/settings/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/Qt/labs/settings/qmldir
%{mingw64_libdir}/qt5/qml/Qt/labs/settings/qmlsettingsplugin.dll
%dir %{mingw64_libdir}/qt5/qml/Qt/labs/sharedimage
%{mingw64_libdir}/qt5/qml/Qt/labs/sharedimage/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/Qt/labs/sharedimage/qmldir
%{mingw64_libdir}/qt5/qml/Qt/labs/sharedimage/sharedimageplugin.dll
%dir %{mingw64_libdir}/qt5/qml/Qt/labs/wavefrontmesh
%{mingw64_libdir}/qt5/qml/Qt/labs/wavefrontmesh/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/Qt/labs/wavefrontmesh/qmldir
%{mingw64_libdir}/qt5/qml/Qt/labs/wavefrontmesh/qmlwavefrontmeshplugin.dll
%dir %{mingw64_libdir}/qt5/qml/QtQml
%{mingw64_libdir}/qt5/qml/QtQml/qmlplugin.dll
%{mingw64_libdir}/qt5/qml/QtQml/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQml/qmldir
%dir %{mingw64_libdir}/qt5/qml/QtQml/Models.2
%{mingw64_libdir}/qt5/qml/QtQml/Models.2/modelsplugin.dll
%{mingw64_libdir}/qt5/qml/QtQml/Models.2/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQml/Models.2/qmldir
%dir %{mingw64_libdir}/qt5/qml/QtQml/StateMachine
%{mingw64_libdir}/qt5/qml/QtQml/StateMachine/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQml/StateMachine/qmldir
%{mingw64_libdir}/qt5/qml/QtQml/StateMachine/qtqmlstatemachine.dll
%dir %{mingw64_libdir}/qt5/qml/QtQml/WorkerScript.2
%{mingw64_libdir}/qt5/qml/QtQml/WorkerScript.2/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQml/WorkerScript.2/qmldir
%{mingw64_libdir}/qt5/qml/QtQml/WorkerScript.2/workerscriptplugin.dll
%dir %{mingw64_libdir}/qt5/qml/QtQuick.2
%{mingw64_libdir}/qt5/qml/QtQuick.2/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQuick.2/qmldir
%{mingw64_libdir}/qt5/qml/QtQuick.2/qtquick2plugin.dll
%dir %{mingw64_libdir}/qt5/qml/QtQuick/
%dir %{mingw64_libdir}/qt5/qml/QtQuick/Layouts
%{mingw64_libdir}/qt5/qml/QtQuick/Layouts/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQuick/Layouts/qmldir
%{mingw64_libdir}/qt5/qml/QtQuick/Layouts/qquicklayoutsplugin.dll
%dir %{mingw64_libdir}/qt5/qml/QtQuick/LocalStorage
%{mingw64_libdir}/qt5/qml/QtQuick/LocalStorage/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQuick/LocalStorage/qmldir
%{mingw64_libdir}/qt5/qml/QtQuick/LocalStorage/qmllocalstorageplugin.dll
%dir %{mingw64_libdir}/qt5/qml/QtQuick/Particles.2
%{mingw64_libdir}/qt5/qml/QtQuick/Particles.2/particlesplugin.dll
%{mingw64_libdir}/qt5/qml/QtQuick/Particles.2/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQuick/Particles.2/qmldir
%dir %{mingw64_libdir}/qt5/qml/QtQuick/Shapes
%{mingw64_libdir}/qt5/qml/QtQuick/Shapes/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQuick/Shapes/qmldir
%{mingw64_libdir}/qt5/qml/QtQuick/Shapes/qmlshapesplugin.dll
%dir %{mingw64_libdir}/qt5/qml/QtQuick/Window.2
%{mingw64_libdir}/qt5/qml/QtQuick/Window.2/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtQuick/Window.2/qmldir
%{mingw64_libdir}/qt5/qml/QtQuick/Window.2/windowplugin.dll
%dir %{mingw64_libdir}/qt5/qml/QtTest
%{mingw64_libdir}/qt5/qml/QtTest/SignalSpy.qml
%{mingw64_libdir}/qt5/qml/QtTest/TestCase.qml
%{mingw64_libdir}/qt5/qml/QtTest/plugins.qmltypes
%{mingw64_libdir}/qt5/qml/QtTest/qmldir
%{mingw64_libdir}/qt5/qml/QtTest/qmltestplugin.dll
%{mingw64_libdir}/qt5/qml/QtTest/testlogger.js
%{mingw64_datadir}/qt5/mkspecs/features/qmlcache.prf
%{mingw64_datadir}/qt5/mkspecs/features/qtquickcompiler.prf
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_packetprotocol_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qml_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qml.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qmldebug_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qmldevtools_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qmlmodels.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qmlmodels_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qmltest.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qmltest_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qmlworkerscript.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qmlworkerscript_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_quick.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_quick_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_quickparticles_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_quickshapes_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_quickwidgets.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_quickwidgets_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_debugger.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_inspector.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_local.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_messages.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_native.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_nativedebugger.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_preview.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_profiler.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_quickprofiler.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_server.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_plugin_qmldbg_tcp.pri

%files -n mingw64-qt5-qmldevtools
%{_prefix}/%{mingw64_target}/bin/qt5/qmlcachegen
%{_prefix}/%{mingw64_target}/bin/qt5/qmlimportscanner
%{_prefix}/%{mingw64_target}/bin/qt5/qmllint
%{_prefix}/%{mingw64_target}/bin/qt5/qmlmin
%{_prefix}/%{mingw64_target}/lib/libQt5QmlDevTools.so

%files -n mingw64-qt5-qmldevtools-devel
%{_prefix}/%{mingw64_target}/lib/libQt5QmlDevTools.so.5*

%files -n mingw64-qt5-%{qt_module}-static
%{mingw64_libdir}/libQt5PacketProtocol.a
%{mingw64_libdir}/libQt5QmlDebug.a
%{mingw64_libdir}/libQt5Qml.a
%{mingw64_libdir}/libQt5QmlModels.a
%{mingw64_libdir}/libQt5QmlWorkerScript.a
%{mingw64_libdir}/libQt5Quick.a
%{mingw64_libdir}/libQt5QuickParticles.a
%{mingw64_libdir}/libQt5QuickShapes.a
%{mingw64_libdir}/libQt5QuickTest.a
%{mingw64_libdir}/libQt5QuickWidgets.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_debugger.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_inspector.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_local.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_messages.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_native.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_nativedebugger.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_preview.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_profiler.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_quickprofiler.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_server.a
%{mingw64_libdir}/qt5/plugins/qmltooling/libqmldbg_tcp.a
%{mingw64_libdir}/qt5/qml/Qt/labs/animation/liblabsanimationplugin.a
%{mingw64_libdir}/qt5/qml/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.a
%{mingw64_libdir}/qt5/qml/Qt/labs/qmlmodels/liblabsmodelsplugin.a
%{mingw64_libdir}/qt5/qml/Qt/labs/settings/libqmlsettingsplugin.a
%{mingw64_libdir}/qt5/qml/Qt/labs/sharedimage/libsharedimageplugin.a
%{mingw64_libdir}/qt5/qml/Qt/labs/wavefrontmesh/libqmlwavefrontmeshplugin.a
%{mingw64_libdir}/qt5/qml/QtQml/libqmlplugin.a
%{mingw64_libdir}/qt5/qml/QtQml/Models.2/libmodelsplugin.a
%{mingw64_libdir}/qt5/qml/QtQml/StateMachine/libqtqmlstatemachine.a
%{mingw64_libdir}/qt5/qml/QtQml/WorkerScript.2/libworkerscriptplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick.2/libqtquick2plugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Layouts/libqquicklayoutsplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/LocalStorage/libqmllocalstorageplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Particles.2/libparticlesplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Shapes/libqmlshapesplugin.a
%{mingw64_libdir}/qt5/qml/QtQuick/Window.2/libwindowplugin.a
%{mingw64_libdir}/qt5/qml/QtTest/libqmltestplugin.a


%changelog
* Tue Apr 07 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-1
- Update to 5.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-1
- Update to 5.13.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Wed Sep 25 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-1
- Update to 5.12.5

* Mon Aug 26 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-3
- Rebuild to fix pkg-config files (#1745257)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-1
- Update to 5.12.4

* Wed Apr 17 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-1
- Update to 5.12.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Sandro Mani <manisandro@gmail.com> - 5.11.3-1
- Update to 5.11.3

* Sat Sep 22 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-1
- Update to 5.11.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Sandro Mani <manisandro@gmail.com> - 5.11.1-1
- Update to 5.11.1

* Wed May 30 2018 Sandro Mani <manisandro@gmail.com> - 5.11.0-1
- Update to 5.11.0

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-2
- Add missing BR: gcc-c++, make
- BR /usr/bin/python

* Thu Feb 15 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-1
- Update to 5.10.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Sandro Mani <manisandro@gmail.com> - 5.10.0-1
- Update to 5.10.0

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 5.9.3-1
- Update to 5.9.3

* Tue Oct 10 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-1
- Update to 5.9.2

* Wed Aug 09 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-4
- Force old debuginfo package logic for now

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-1
- Update to 5.9.1

* Wed Jun 14 2017 Sandro Mani <manisandro@gmail.com> - 5.9.0-1
- Update to 5.9.0

* Tue May 09 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-2
- Rebuild for dropped 0022-Allow-usage-of-static-version-with-CMake.patch in qtbase

* Fri Apr 28 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-1
- Update to 5.8.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Sandro Mani <manisandro@gmail.com> - 5.7.1-1
- Update to 5.7.1

* Thu Aug 25 2016 Martin Bříza <mbriza@redhat.com> - 5.6.0-2
- Fix crashes in the QML engine related to dead store elimination

* Mon Mar 28 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-1
- Update to 5.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.1-1
- Update to 5.5.1

* Thu Aug  6 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 21 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1

* Mon Dec 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0
- Added -static subpackages (RHBZ #1123776)

* Sat Sep 20 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.2-1
- Update to 5.3.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul  6 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0

* Sat Feb  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Sun Jan 12 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-4
- Don't carry .dll.debug files in main package

* Mon Jan  6 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-3
- Dropped manual rename of import libraries

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-2
- Removed BR: mingw{32,64}-qt5-qtjsbackend (unnecessary as of Qt 5.2)

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0

* Fri Nov 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.0-0.1.rc1
- Update to 5.2.0 RC1

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1

* Fri Aug  2 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-2
- Make sure the QmlDevTools library is built as a shared library
- Added mingw{32,64}-qt5-qmldevtools-devel subpackages

* Thu Jul 11 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0
- Added mingw{32,64}-qt5-qmldevtools subpackages
- Changed URL to http://qt-project.org/

* Sun May 26 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2
- Own the folders %%{mingw32_datadir}/qt5/qml, %%{mingw32_datadir}/qt5/qml/Qt,
  %%{mingw32_datadir}/qt5/qml/Qt/labs, %%{mingw64_datadir}/qt5/qml,
  %%{mingw64_datadir}/qt5/qml/Qt and %%{mingw64_datadir}/qt5/qml/Qt/labs

* Sat Feb  9 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1

* Thu Jan  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-1
- Update to Qt 5.0.0 Final

* Sun Nov 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.2.beta1.git20121111.dd1d6b56
- Update to 20121111 snapshot (rev dd1d6b56)
- Rebuild against latest mingw-qt5-qtbase
- Dropped pkg-config rename hack as it's unneeded now
- Dropped upstreamed patch

* Wed Sep 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.1.beta1
- Initial release

