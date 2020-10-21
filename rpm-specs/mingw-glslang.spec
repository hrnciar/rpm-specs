%{?mingw_package_header}

%global pkgname glslang

%global commit 5743eed4d16757402517a1068137f4bc1645ee87
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          mingw-%{pkgname}
Version:       11.0.0
Release:       1%{?commit:.git%{shortcommit}}%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD and GPLv3+ and ASL 2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{pkgname}
%if 0%{?commit:1}
Source0:       https://github.com/KhronosGroup/%{pkgname}/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/KhronosGroup/%{pkgname}/archive/%{version}/%{pkgname}-%{version}.tar.gz
%endif
# Remove debug suffix for mingw builds
Patch0:        glslang_debug-suffix.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-winpthreads-static

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-winpthreads-static


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{pkgname}-%{commit}
%else
%autosetup -p1 -n %{pkgname}-%{version}
%endif


%build
%mingw_cmake -DBUILD_SHARED_LIBS=OFF
%mingw_make_build


%install
%mingw_make_install

# We don't want them in here
rm -rf %{buildroot}%{mingw32_includedir}/SPIRV
rm -rf %{buildroot}%{mingw64_includedir}/SPIRV


%files -n mingw32-%{pkgname}
%{mingw32_bindir}/glslangValidator.exe
%{mingw32_bindir}/spirv-remap.exe
%{mingw32_includedir}/glslang/
%{mingw32_libdir}/libGenericCodeGen.a
%{mingw32_libdir}/libHLSL.a
%{mingw32_libdir}/libMachineIndependent.a
%{mingw32_libdir}/libOGLCompiler.a
%{mingw32_libdir}/libOSDependent.a
%{mingw32_libdir}/libSPIRV.a
%{mingw32_libdir}/libSPVRemapper.a
%{mingw32_libdir}/libglslang.a
%{mingw32_libdir}/cmake/*

%files -n mingw64-%{pkgname}
%{mingw64_bindir}/glslangValidator.exe
%{mingw64_bindir}/spirv-remap.exe
%{mingw64_includedir}/glslang/
%{mingw64_libdir}/libGenericCodeGen.a
%{mingw64_libdir}/libHLSL.a
%{mingw64_libdir}/libMachineIndependent.a
%{mingw64_libdir}/libOGLCompiler.a
%{mingw64_libdir}/libOSDependent.a
%{mingw64_libdir}/libSPIRV.a
%{mingw64_libdir}/libSPVRemapper.a
%{mingw64_libdir}/libglslang.a
%{mingw64_libdir}/cmake/*


%changelog
* Mon Aug 10 2020 Sandro Mani <manisandro@gmail.com> - 11.0.0-1
- Update to 11.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.13.3559-2.gitc9b28b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 8.13.3559-2.gitc9b28b9
- Update to git c9b28b9

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 8.13.3559-1
- Update to 8.13.3559

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.13.3496-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 7.13.3496-1
- Update to 7.13.3496

* Thu Aug 22 2019 Sandro Mani <manisandro@gmail.com> - 7.12.3352-1
- Update to 7.12.3352

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 7.11.3214.3.giteea3400
- Update to git eea3400

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.11.3214-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 7.11.3214-1
- Update to 7.11.3214

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 3.1-0.6.gite0d59bb
- Update to git e0d59bb

* Mon Feb 25 2019 Sandro Mani <manisandro@gmail.com> - 3.1-0.5.git05d12a9
- Update to git 05d12a9

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-0.4.gite0bc65b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 3.1.0-0.3.gite0bc65b
- Update to git e0bc65b

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-0.2.git3bb4c48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 3.1-0.1.git3bb4c48
- Initial package
