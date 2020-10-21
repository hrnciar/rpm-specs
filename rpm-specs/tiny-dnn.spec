%global prerelease a3
Name:           tiny-dnn
Version:        1.0.0
Release:        0.%{prerelease}.3%{?dist}.7
Summary:        Header only, dependency-free deep learning framework in C++14

License:        BSD
URL:            https://github.com/tiny-dnn/tiny-dnn/
Source0:        https://github.com/tiny-dnn/tiny-dnn/archive/v%{version}%{prerelease}/%{name}-%{version}%{prerelease}.tar.gz
# Patch to optionally use system-wide installation of gtest/gmock.
# Upstream PR: https://github.com/tiny-dnn/tiny-dnn/pull/968/
Patch0:         %{name}.distro-gmock.patch
# Do not overwrite cflags.
# Will not be merged upstream, only makes sense downstream
Patch1:         %{name}.compile-flags.patch

# Test fails on ix86.
ExcludeArch:    %{ix86}

BuildRequires:  /usr/bin/ctest
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
BuildRequires:  pkgconfig(tbb)
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-compiler

%description
tiny-dnn is a C++14 implementation of deep learning. It is suitable for deep
learning on limited computational resource, embedded systems and IoT devices.


%package        devel
Summary:        Development files for %{name}
Provides:       tiny-dnn-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%global debug_package %{nil}

%prep
%autosetup -p1 -n %{name}-%{version}%{prerelease}


%build
# This fails at link time with LTO on armv7.  Disable LTO for now
%define _lto_cflags %{nil}
%cmake -DBUILD_TESTS=ON -DUSE_SYS_GTEST=ON
%cmake_build


%install
%cmake_install


%check
%ctest --timeout 15000

%files devel
%license LICENSE
%doc README.md
%{_includedir}/tiny_dnn
%{_datadir}/TinyDNN


%changelog
* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 1.0.0-0.a3.3.7
- Disable LTO for now

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.a3.3.6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.a3.3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.a3.3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.a3.3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.a3.3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.a3.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.0.0-0.a3.3
- Provide only the devel subpackage
- Add missing BR: gcc-c++
- Virtually provide tiny-dnn-static (header only library)
- Remove BuildArch: noarch (header only library)

* Mon Jun 25 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.0.0-0.a3.2
- Update patches for F28+

* Sun Jun 24 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.0.0-0.a3.1
- Initial package
