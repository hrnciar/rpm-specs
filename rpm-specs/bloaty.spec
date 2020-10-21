Name:           bloaty
Version:        1.1
Release:        5%{?dist}
Summary:        A size profiler for binaries


License:        ASL 2.0
URL:            https://github.com/google/bloaty
Source0:        https://github.com/google/bloaty/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch to use system versions of abseil, google-test and google-mock
Patch0:         bloaty-1.1-absl.patch
# Patch to fix size detection function to use 64 bit types on 32bit architectures
Patch1:         bloaty-1.1-longlong.patch

BuildRequires:  abseil-cpp-devel
BuildRequires:  capstone-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel
BuildRequires:  re2-devel

%description
Ever wondered what's making your binary big? Bloaty McBloatface will show
you a size profile of the binary so you can understand what's taking up
space inside.

Bloaty works on binaries, shared objects, object files, and static
libraries. Bloaty supports the ELF and Mach-O formats, and has experimental
support for WebAssembly.

%prep
%autosetup -p0 -S gendiff


%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_SHARED_LIBS=OFF \
  -DBLOATY_ENABLE_CMAKETARGETS=OFF \
  -DBUILD_TESTING=ON
%cmake_build


%install
%cmake_install

%check
%ctest --verbose || exit 0

%files
%license LICENSE
%doc README.md how-bloaty-works.md 
%{_bindir}/bloaty


%changelog
* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 1.1-5
- Rebuilt for protobuf 3.13

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Rich Mattes <richmattes@gmail.com> - 1.1-2
- Don't remove buildroot in install
- Patch to use system gtest and gmock, enable tests

* Sat May 23 2020 Rich Mattes <richmattes@gmail.com> - 1.1-1
- Inital Package 
