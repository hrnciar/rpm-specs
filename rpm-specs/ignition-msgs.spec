%global abiver 1

Name:		ignition-msgs
Version:	1.0.0
Release:	6%{?dist}
Summary:	Common messages for the ignition framework

# Bundled gtest and python helper scripts are licensed BSD, but not included in installation
# Installed files are Apache 2
License:	ASL 2.0
URL:		http://www.ignitionrobotics.org
Source0:	http://gazebosim.org/distributions/ign-msgs/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:  ignition-cmake-devel
BuildRequires:	ignition-math-devel >= 4
BuildRequires:	protobuf-devel

%description
A standard set of message definitions, used by Ignition Transport, and
other applications.  Contains pre-compiled protobuf definitions of messages
for re-use by other libraries and applications.

%package devel
Summary: Development libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: ignition-math-devel
Requires: protobuf-devel

%description devel
%{summary}

%package doc
Summary: Development documentation for ignition-msgs
BuildArch: noarch

%description doc
Automatically generated API documentation for the ignition-msgs library

%prep
%autosetup

%build
mkdir build; cd build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake .. \
%ifnarch x86_64
  -DSSE2_FOUND=FALSE \
%endif
  -DSSE3_FOUND=FALSE \
  -DSSSE3_FOUND=FALSE \
  -DSSE4_1_FOUND=FALSE \
  -DSSE4_2_FOUND=FALSE \
  -DCMAKE_C_FLAGS_ALL="%{optflags}" \
  -DCMAKE_CXX_FLAGS_ALL="%{optflags}" \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo


make %{?_smp_mflags}
make doc

%install
%make_install -C build
rm -fr %{buildroot}%{_prefix}/lib/ruby

%check
make -C build test

%ldconfig_scriptlets

%files
%license COPYING LICENSE
%doc AUTHORS NEWS README.md
%{_libdir}/*.so.*
%{_datadir}/ignition

%files devel
%{_libdir}/*.so
%{_includedir}/ignition
%{_libdir}/cmake/%{name}%{abiver}
%{_libdir}/pkgconfig/*.pc

%files doc
%license COPYING LICENSE
%doc build/doxygen/html

%changelog
* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.0.0-6
- Rebuilt for protobuf 3.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.0.0-4
- Rebuild for protobuf 3.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Rich Mattes <richmattes@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Thu Nov 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-12
- Rebuild for protobuf 3.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.0-9
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-8
- Rebuild for protobuf 3.4

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 0.7.0-7
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-4
- Rebuild for protobuf 3.3.1

* Tue Mar 28 2017 Rich Mattes <richmattes@gmail.com> - 0.7.0-3
- Add --as-needed link flags

* Sun Mar 05 2017 Rich Mattes <richmattes@gmail.com> - 0.7.0-2
- Create a separate -doc subpackage for documentation

* Sun Mar 05 2017 Rich Mattes <richmattes@gmail.com> - 0.7.0-1
- Update to release 0.7.0

* Mon Jan 09 2017 Rich Mattes <richmattes@gmail.com> - 0.6.1-1
- Initial package
