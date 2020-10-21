Name:           tinyobjloader
Version:        1.0.6
Release:        9%{?dist}
Summary:        Tiny wavefront obj loader

License:        MIT
URL:            https://github.com/syoyo/tinyobjloader
Source0:        https://github.com/syoyo/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Tiny but powerful single file wavefront obj loader written in C++. No
dependency except for C++ STL. It can parse over 10M polygons with moderate
memory and time.

%package devel
Summary: Development files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%summary

%prep
%autosetup -n %{name}-%{version}


%build
%cmake \
  -DTINYOBJLOADER_COMPILATION_SHARED=ON
%cmake_build


%install
%cmake_install
rm -rf %{buildroot}/%{_docdir}

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/tiny_obj_loader.h
%{_libdir}/*.so
%{_libdir}/%{name}
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-3
- Fix ISA macro

* Wed Nov 29 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-2
- Don't remove buildroot in install

* Wed Nov 29 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-1
- Initial package 
