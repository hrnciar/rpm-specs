%{?mingw_package_header}

%global pkgname GeographicLib

Name:           mingw-%{pkgname}
Version:        1.50.1
Release:        4%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        MIT
URL:            http://geographiclib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/geographiclib/%{pkgname}-%{version}.tar.gz

# Use PythonInterp to set the python version for installation directory,
# and install python lib to arch-independent path
Patch0:         GeographicLib-python.patch

BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-python3

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-python3


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows %{pkgname} python 3 bindings

%description -n mingw32-python3-%{pkgname}
MinGW Windows %{pkgname} python 3 bindings.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows %{pkgname} python 3 bindings

%description -n mingw64-python3-%{pkgname}
MinGW Windows %{pkgname} python 3 bindings.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
MINGW_BUILDDIR_SUFFIX=py3 %mingw_cmake \
  -DCOMMON_INSTALL_PATH=ON \
  -DUSE_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DPython_ADDITIONAL_VERSIONS=3
MINGW_BUILDDIR_SUFFIX=py3 %mingw_make %{?_smp_mflags}


%install
MINGW_BUILDDIR_SUFFIX=py3 %mingw_make DESTDIR=%{buildroot} install

# Don't include data files and bindings
rm -rf %{buildroot}%{mingw32_datadir}/matlab
rm -rf %{buildroot}%{mingw64_datadir}/matlab
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{mingw32_libdir}/node_modules
rm -rf %{buildroot}%{mingw64_libdir}/node_modules


%files -n mingw32-%{pkgname}
%license LICENSE.txt
%{mingw32_bindir}/CartConvert.exe
%{mingw32_bindir}/ConicProj.exe
%{mingw32_bindir}/GeoConvert.exe
%{mingw32_bindir}/GeodSolve.exe
%{mingw32_bindir}/GeodesicProj.exe
%{mingw32_bindir}/GeoidEval.exe
%{mingw32_bindir}/Gravity.exe
%{mingw32_bindir}/MagneticField.exe
%{mingw32_bindir}/Planimeter.exe
%{mingw32_bindir}/RhumbSolve.exe
%{mingw32_bindir}/TransverseMercatorProj.exe
%{mingw32_bindir}/libGeographic.dll
%{mingw32_includedir}/%{pkgname}/
%{mingw32_libdir}/libGeographic.dll.a
%{mingw32_libdir}/cmake/GeographicLib/
%{mingw32_libdir}/pkgconfig/geographiclib.pc

%files -n mingw32-python3-%{pkgname}
%license LICENSE.txt
%{mingw32_python3_sitearch}/geographiclib/


%files -n mingw64-%{pkgname}
%license LICENSE.txt
%{mingw64_bindir}/CartConvert.exe
%{mingw64_bindir}/ConicProj.exe
%{mingw64_bindir}/GeoConvert.exe
%{mingw64_bindir}/GeodSolve.exe
%{mingw64_bindir}/GeodesicProj.exe
%{mingw64_bindir}/GeoidEval.exe
%{mingw64_bindir}/Gravity.exe
%{mingw64_bindir}/MagneticField.exe
%{mingw64_bindir}/Planimeter.exe
%{mingw64_bindir}/RhumbSolve.exe
%{mingw64_bindir}/TransverseMercatorProj.exe
%{mingw64_bindir}/libGeographic.dll
%{mingw64_includedir}/%{pkgname}/
%{mingw64_libdir}/libGeographic.dll.a
%{mingw64_libdir}/cmake/GeographicLib/
%{mingw64_libdir}/pkgconfig/geographiclib.pc

%files -n mingw64-python3-%{pkgname}
%license LICENSE.txt
%{mingw64_python3_sitearch}/geographiclib/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 1.50.1-3
- Rebuild (python-3.9)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Sandro Mani <manisandro@gmail.com> - 1.50.1-1
- Update to 1.50.1

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.50-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 1.50-1
- Update to 1.50

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 1.49-8
- Drop python2 bindings

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 1.49-6
- Add python3 subpackages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Sandro Mani <manisandro@gmail.com> - 1.49-4
- Add python bindings

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 1.49-1
- Update to 1.49

* Thu Aug 10 2017 Sandro Mani <manisandro@gmail.com> - 1.48-1
- Initial package
