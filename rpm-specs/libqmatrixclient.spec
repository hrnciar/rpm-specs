Name: libqmatrixclient
Version: 0.5.3.2
Release: 1%{?dist}

Summary: Qt5 library to write cross-platform clients for Matrix
License: LGPLv2
URL: https://github.com/quotient-im/libQuotient
Source0: https://github.com/quotient-im/libQuotient/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5LinguistTools)

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
The Quotient project aims to produce a Qt5-based SDK to develop applications
for Matrix. libQuotient is a library that enables client applications. It is
the backbone of Quaternion, Spectral and other projects. Versions 0.5.x and
older use the previous name - libQMatrixClient.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n libQuotient-%{version}
mkdir -p %{_target_platform}
rm -rf 3rdparty

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DQMATRIXCLIENT_INSTALL_EXAMPLE=OFF \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH="include/QMatrixClient" \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}
rm -rf %{buildroot}%{_datadir}/ndk-modules

%files
%license COPYING
%doc README.md CONTRIBUTING.md
%{_libdir}/libQMatrixClient.so.0*

%files devel
%{_includedir}/QMatrixClient/
%{_libdir}/cmake/QMatrixClient/
%{_libdir}/pkgconfig/QMatrixClient.pc
%{_libdir}/libQMatrixClient.so

%changelog
* Wed Apr 01 2020 Brendan Early <mymindstorm@evermiss.net> - 0.5.3.2-1
- Version 0.5.3.2


* Thu Mar 05 2020 Brendan Early <mymindstorm@evermiss.net> - 0.5.2-1
- Downgrade to version 0.5.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.3.20200121gite3a5b3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.2.20200121gite3a5b3a
- Updated to version 0.6.0-git.
