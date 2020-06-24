%{?mingw_package_header}

%global commit 67f4838659f475d618c120e13d1a196d7e00ba4b
%global shortcommit %(c=%{commit}; echo ${c:0:7})


%global pkgname spirv-tools
%global srcname SPIRV-Tools

Name:          mingw-%{pkgname}
Version:       2019.5
Release:       4%{?commit:.git%{shortcommit}}%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       ASL 2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
%if 0%{?commit:1}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
%endif

# Fix installation dir for cmake modules
Patch0:        spirv-tool_cmake-install.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-python3
BuildRequires: mingw32-spirv-headers
BuildRequires: mingw32-winpthreads
BuildRequires: mingw32-winpthreads-static

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-python3
BuildRequires: mingw64-spirv-headers
BuildRequires: mingw64-winpthreads
BuildRequires: mingw64-winpthreads-static


%description
MinGW Windows %{pkgname}.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.


%{?mingw_debug_package}


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{srcname}-%{commit}
%else
%autosetup -p1 -n %{srcname}-%{version}
%endif


%build
MINGW32_CMAKE_ARGS="-DSPIRV-Headers_SOURCE_DIR=%{mingw32_prefix} -DPYTHON_EXECUTABLE=%{mingw32_python3}" \
MINGW64_CMAKE_ARGS="-DSPIRV-Headers_SOURCE_DIR=%{mingw64_prefix} -DPYTHON_EXECUTABLE=%{mingw64_python3}" \
%mingw_cmake
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%{mingw32_bindir}/libSPIRV-Tools-link.dll
%{mingw32_bindir}/libSPIRV-Tools-opt.dll
%{mingw32_bindir}/libSPIRV-Tools-reduce.dll
%{mingw32_bindir}/libSPIRV-Tools-shared.dll
%{mingw32_bindir}/libSPIRV-Tools.dll
%{mingw32_bindir}/spirv-as.exe
%{mingw32_bindir}/spirv-cfg.exe
%{mingw32_bindir}/spirv-dis.exe
%{mingw32_bindir}/spirv-lesspipe.sh
%{mingw32_bindir}/spirv-link.exe
%{mingw32_bindir}/spirv-opt.exe
%{mingw32_bindir}/spirv-reduce.exe
%{mingw32_bindir}/spirv-val.exe
%{mingw32_includedir}/spirv-tools/
%{mingw32_libdir}/libSPIRV-Tools-link.dll.a
%{mingw32_libdir}/libSPIRV-Tools-opt.dll.a
%{mingw32_libdir}/libSPIRV-Tools-reduce.dll.a
%{mingw32_libdir}/libSPIRV-Tools-shared.dll.a
%{mingw32_libdir}/libSPIRV-Tools.dll.a
%{mingw32_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{mingw32_libdir}/pkgconfig/SPIRV-Tools.pc
%{mingw32_libdir}/cmake/*

%files -n mingw64-%{pkgname}
%{mingw64_bindir}/libSPIRV-Tools-link.dll
%{mingw64_bindir}/libSPIRV-Tools-opt.dll
%{mingw64_bindir}/libSPIRV-Tools-reduce.dll
%{mingw64_bindir}/libSPIRV-Tools-shared.dll
%{mingw64_bindir}/libSPIRV-Tools.dll
%{mingw64_bindir}/spirv-as.exe
%{mingw64_bindir}/spirv-cfg.exe
%{mingw64_bindir}/spirv-dis.exe
%{mingw64_bindir}/spirv-lesspipe.sh
%{mingw64_bindir}/spirv-link.exe
%{mingw64_bindir}/spirv-opt.exe
%{mingw64_bindir}/spirv-reduce.exe
%{mingw64_bindir}/spirv-val.exe
%{mingw64_includedir}/spirv-tools/
%{mingw64_libdir}/libSPIRV-Tools-link.dll.a
%{mingw64_libdir}/libSPIRV-Tools-opt.dll.a
%{mingw64_libdir}/libSPIRV-Tools-reduce.dll.a
%{mingw64_libdir}/libSPIRV-Tools-shared.dll.a
%{mingw64_libdir}/libSPIRV-Tools.dll.a
%{mingw64_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{mingw64_libdir}/pkgconfig/SPIRV-Tools.pc
%{mingw64_libdir}/cmake/*


%changelog
* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 2019.5-4.git67f4838
- Rebuild (python-3.9)

* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 2019.5-3.git67f4838
- Update to git 67f4838

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 2019.5-2.git97f1d48
- Update to git 97f1d48

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 2019.5-1
- Update to 2019.5

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.4-4.git3e4abc9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 2019.4-3.git3e4abc9
- Update to git 3e4abc9

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 2019.4-2
- Rebuild (python 3.8)

* Sun Aug 11 2019 Sandro Mani <manisandro@gmail.com> - 2019.4-1
- Update to 2019.4

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 2019.3-4.git3726b50
- Drop unnecessary BR: python2

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 2019.3-3.git3726b50
- Update to git 3726b50

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Sandro Mani <manisandro@gmail.com> - 2019.3-1
- Update to 2019.3

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 2019.2-2
- Switch to python3

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 2019.2-1
- Update to 2019.2

* Mon Feb 11 2019 Sandro Mani <manisandro@gmail.com> - 2019.1-1
- Update to 2019.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Sandro Mani <manisandro@gmail.com> - 2018.4-1
- Update to 2018.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.0-0.2.git26a698c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 2018.3.0-0.1.git26a698c
- Initial package
