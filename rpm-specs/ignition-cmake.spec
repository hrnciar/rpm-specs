%global debug_package %{nil}
%global major_version 0

Name:           ignition-cmake
Version:        0.6.1
Release:        7%{?dist}
Summary:        CMake modules to be used by the Ignition projects
Epoch:          1

#Most of the sources are Apache, but a couple of the CMake Find* modules are licensed as BSD
License:        ASL 2.0 and BSD
URL:            https://ignitionrobotics.org/libs/cmake
Source0:        http://gazebosim.org/distributions/ign-cmake/releases/%{name}-%{version}.tar.bz2
Patch0:         %{name}-0.6.1-noarch.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
This package is required to build ignition projects, as well as to link your
own projects against them. It provides modules that are used to find
dependencies of ignition projects and generate cmake targets for consumers of
ignition projects to link against.

%package devel
Summary: CMake modules to be used by the Ignition projects
BuildArch: noarch

%description devel
This package is required to build ignition projects, as well as to link your
own projects against them. It provides modules that are used to find
dependencies of ignition projects and generate cmake targets for consumers of
ignition projects to link against.

%prep
%autosetup -p1


%build
mkdir build; pushd build
%cmake .. -DBUILD_TESTING=OFF
# Remove 'bitness' check from version file
sed -i '36,$d' ignition-cmake0-config-version.cmake
popd

%make_build -C build

%install
%make_install -C build

%files devel
%{_datadir}/cmake/%{name}%{major_version}
%{_datadir}/ignition

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1:0.6.1-4
- Remove architecture check from version file

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1:0.6.1-3
- Make package architecture dependent, CMake version check is architecture-dependent (https://gitlab.kitware.com/cmake/cmake/issues/16184)

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1:0.6.1-2
- Make package noarch

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1:0.6.1-1
- Add epoch and downgrade to 0.x release series, required for gazebo9 and its dependencies

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.pre3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 19 2018 Rich Mattes <richmattes@gmail.com> - 1.0.0-0.2.pre3
- Remove shebang from non-executable scripts

* Sun May 13 2018 Rich Mattes <richmattes@gmail.com> - 1.0.0-0.1.pre3
- Initial package
