%global _docdir_fmt %{name}
%global abiver 4

Name:       ignition-transport
Version:    4.0.0
Release:    7%{?dist}
Summary:    A fast and efficient message passing system

License:    ASL 2.0
URL:        http://ignitionrobotics.org/libraries/transport
Source0:    http://gazebosim.org/distributions/ign-transport/releases/%{name}%{abiver}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cppzmq-devel
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  ignition-cmake-devel
BuildRequires:  ignition-msgs-devel
BuildRequires:  pkgconfig(uuid)
BuildRequires:  protobuf-devel
BuildRequires:  rubygem-ronn
BuildRequires:  zeromq-devel


%description
The ignition transport library combines ZeroMQ with Protobufs to create
a fast and efficient message passing system. Asynchronous message publication
and subscription is provided along with service calls and discovery.

%package devel
Summary: Development files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: ignition-cmake-devel
Requires: ignition-msgs-devel
Requires: cppzmq-devel

%description devel
This package contains the header files and libraries
for %{name}. If you like to develop programs using
%{name}, you will need to install
%{name}-devel.

%package doc
Summary: Development documentation for %{name}
BuildArch: noarch

%description doc
Generated API and development documentation for %{name}

%prep
%autosetup
# Required to sneak in custom CFLAGS via CMAKE_C_FLAGS_ALL
sed -i 's/unset/#unset/g' CMakeLists.txt
dos2unix README.md

%build
mkdir build
pushd build
%cmake .. \
%ifnarch x86_64
  -DSSE2_FOUND=FALSE \
%endif
  -DSSE3_FOUND=FALSE \
  -DSSSE3_FOUND=FALSE \
  -DSSE4_1_FOUND=FALSE \
  -DSSE4_2_FOUND=FALSE \
  -DCMAKE_C_FLAGS_ALL="%{optflags}" \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
popd

make -C build %{?_smp_mflags}
make -C build doc

%install
make -C build install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_usr}/lib/ruby

%check
# Firewall settings prevent most of these tests from passing.
# Disabled for now.
#make -C build test ARGS="-V" || exit 0


%files
%license COPYING
%doc README.md
%{_libdir}/*.so.*
%{_datadir}/ignition

%files devel
%{_libdir}/pkgconfig
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_includedir}/ignition

%files doc
%license COPYING
%doc build/doxygen/html

%changelog
* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 4.0.0-7
- Rebuilt for protobuf 3.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 4.0.0-5
- Rebuild for protobuf 3.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Scott K Logan <logans@cottsay.net> - 4.0.0-3
- Add Requires: ignition-cmake-devel to devel subpackage

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 4.0.0-1
- Update to version 4.0.0

* Thu Nov 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.1-11
- Adapt to new packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.0.1-8
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.1-7
- Rebuild for protobuf 3.4

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 3.0.1-6
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-3
- Rebuild for protobuf 3.3.1

* Tue Apr 04 2017 Rich Mattes <richmattes@gmail.com> - 3.0.1-2
- Devel package requires cppzmq-devel

* Mon Apr 03 2017 Rich Mattes <richmattes@gmail.com> - 3.0.1-1
- Update to release 3.0.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-2
- Rebuild for protobuf 3.2.0

* Fri Nov 18 2016 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-1
- Update to 1.4.0

* Wed Jul 20 2016 Rich Mattes <richmattes@gmail.com> - 1.3.0-1
- Update to release 1.3.0

* Tue Jul 05 2016 Rich Mattes <richmattes@gmial.com> - 1.2.0-1
- Update to release 1.2.0

* Sat Dec 05 2015 Rich Mattes <richmattes@gmail.com> - 0.7.0-1
- Initial release (rhbz#1353064)
