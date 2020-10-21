%global __cmake_in_source_build 1

%global commit cedd544e36c98820d5f454cd53908f1ecce14213
%global gittag %{commit}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20200509

Name:           libmml
Version:        2.4
Release:        9.%{commitdate}git%{shortcommit}%{?dist}
Summary:        MML Widget
License:        GPLv3 or LGPLv2 with exceptions
URL:            https://github.com/copasi/copasi-dependencies/tree/master/src/mml
Source0:        https://gitlab.com/anto.trande/mml/-/archive/%{commit}/mml-%{commit}.tar.gz
Patch0:         %{name}-build.patch

BuildRequires:  gcc-c++, cmake
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xmu)

%description
The QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

############### QT5 ######################
%package        qt5
Summary:        Qt5/OpenGL-based MML Widget
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(qwt)
Buildrequires:  qt5-rpm-macros, qt5-qtbase-devel
Requires:       pkgconfig(Qt5Core)
Provides:       libqtmmlwidget%{?_isa} = %{version}-%{release}

%description    qt5
The Qt5 QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

%package        qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-qt5-devel package contains Qt5 libraries and header files for
developing applications that use %{name}.

############### QT4 ######################
%package        qt4
Summary:        Qt4/OpenGL-based MML Widget
BuildRequires:  pkgconfig(Qt)
BuildRequires:  pkgconfig(qwt5-qt4)
Requires:       pkgconfig(QtCore)
Provides:       libqtmmlwidget-qt4%{?_isa} = %{version}-%{release}

%description    qt4
The Qt4 QtMmlWidget component renders mathematical formulas written in
MathML 2.0.

%package        qt4-devel
Summary:        Development files for %{name}-qt4
Requires:       %{name}-qt4%{?_isa} = %{version}-%{release}

%description    qt4-devel
The %{name}-qt4-devel package contains Qt4 libraries and header files for
developing applications that use %{name}.

%prep
%setup -qc -n mml-%{commit}

pushd mml-%{commit}
%patch0 -p0
popd

mv mml-%{commit} qt5; cp -a qt5 qt4

%build
############### QT5 ######################
pushd qt5
mkdir -p build && cd build
# -Werror=format-security/ flag prevents compilation
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CXXFLAGS=$SETOPT_FLAGS
%cmake -Wno-dev \
 -DSELECT_QT=Qt5 \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt5 \
 -DQWT_VERSION_STRING:STRING=$(pkg-config --modversion qwt) \
 -DQWT_LIBRARY:FILEPATH=%{_qt5_libdir}/libqwt-qt5.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt5_headerdir}/qwt \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt5_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt5_headerdir}/%{name}-qt5 ..
%make_build
cd ..
popd

############### QT4 ######################
pushd qt4
mkdir -p build && cd build
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
export CXXFLAGS=$SETOPT_FLAGS
%cmake -Wno-dev \
 -DSELECT_QT=Qt4 \
 -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_bindir}/qmake-qt4 \
 -DQWT_VERSION_STRING:STRING=$(pkg-config --modversion qwt5-qt4) \
 -DQWT_LIBRARY:FILEPATH=%{_qt4_libdir}/libqwt5-qt4.so \
 -DQWT_INCLUDE_DIR:PATH=%{_qt4_headerdir}/qwt5-qt4 \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt4_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt4_headerdir}/%{name}-qt4 ..
%make_build
cd ..
popd

%install
############### QT5 ######################
pushd qt5/build
%make_install
popd

############### QT4 ######################
pushd qt4/build
%make_install
popd

%ldconfig_scriptlets qt5
%ldconfig_scriptlets qt4

############### QT5 ######################
%files qt5
%license qt5/LGPL_EXCEPTION.txt qt5/LICENSE.LGPL
%{_qt5_libdir}/%{name}.so.*

%files qt5-devel
%dir %{_qt5_headerdir}
%{_qt5_headerdir}/%{name}-qt5/
%{_qt5_libdir}/%{name}.so

############### QT4 ######################
%files qt4
%license qt4/LGPL_EXCEPTION.txt qt4/LICENSE.LGPL
%{_qt4_libdir}/%{name}-qt4.so.*

%files qt4-devel
%{_qt4_headerdir}/%{name}-qt4/
%{_qt4_libdir}/%{name}-qt4.so

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9.20200509gitcedd544
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8.20200509gitcedd544
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.4-7.20200509gitcedd544
- Move code to GitLab repository
- Rebuild new commit

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-6.20180425git07159b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5.20180425git07159b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4.20180425git07159b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3.20180425git07159b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-2.20180425git07159b0
- Co-own /usr/lib*/qt5 directory
- Include GPLv3 as used license for files of a Qt Solutions component

* Sat May 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4-1.20180425git07159b0
- First rpm
- Use CMake method
