
Summary: Gstreamer phonon backend for Qt4
Name:    phonon-qt4-backend-gstreamer
Version: 4.9.1
Release: 10%{?dist}

License: LGPLv2+
URL:     http://phonon.kde.org/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/phonon/phonon-backend-gstreamer/%{version}/phonon-backend-gstreamer-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0) pkgconfig(gstreamer-audio-1.0) pkgconfig(gstreamer-video-1.0)

Requires: gstreamer1-plugins-good%{?_isa}

BuildRequires: automoc4
BuildRequires: cmake >= 2.8.9
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: pkgconfig(phonon) > 4.10
BuildRequires: pkgconfig(QtOpenGL)

%global phonon_version %(pkg-config --modversion phonon 2>/dev/null || echo 4.10)

Provides: phonon-backend%{?_isa} = %{phonon_version}

Obsoletes: phonon-backend-gstreamer < 2:4.9.1-10
Provides:  phonon-backend-gstreamer = 2:%{version}-%{release}
Provides:  phonon-backend-gstreamer%{?_isa} = 2:%{version}-%{release}

%description
%{summary}.


%prep
%autosetup -n phonon-gstreamer-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} .. \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DUSE_INSTALL_PLUGIN:BOOL=ON
popd

%make_build -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%license COPYING.LIB
%{_kde4_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_kde4_datadir}/kde4/services/phononbackends/gstreamer.desktop
%{_datadir}/icons/hicolor/*/apps/phonon-gstreamer.*


%changelog
* Wed Jan 22 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-10
- first try at compat phonon-qt4-backend-gstreamer
