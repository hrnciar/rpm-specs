Name:    pulseaudio-qt
Summary: Qt bindings for PulseAudio
Version: 1.2
Release: 1%{?dist}

License: LGPLv2+
URL:     https://cgit.kde.org/%{name}.git
Source:  https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= 5.44.0
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5DBus)

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%license COPYING.LIB
%doc README.md
%{_kf5_libdir}/libKF5PulseAudioQt.so.2
%{_kf5_libdir}/libKF5PulseAudioQt.so.%{version}.0

%files devel
%{_kf5_includedir}/KF5PulseAudioQt/
%{_kf5_libdir}/libKF5PulseAudioQt.so
%{_kf5_includedir}/pulseaudioqt_version.h
%{_kf5_libdir}/cmake/KF5PulseAudioQt/


%changelog
* Mon Mar 30 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.2-1
- first try

