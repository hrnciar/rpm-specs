%{?mingw_package_header}

%global pkgname jxrlib

Name:          mingw-%{pkgname}
Version:       1.1
Summary:       MinGW Windows JPEG XR library
Release:       10%{?dist}

BuildArch:     noarch
License:       BSD
URL:           https://jxrlib.codeplex.com/
# Annoying download links on CodePlex...
Source0:       http://jxrlib.codeplex.com/downloads/get/685250#/jxrlib_%(echo %{version} | tr . _).tar.gz
Source1:       CMakeLists.txt

# Fix some warnings
Patch0:        jxrlib_warnings.patch
# Mingw build fixes
Patch1:        jxrlib_mingw.patch

BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc


%description
MinGW Windows JPEG XR library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows JPEG XR library

%description -n mingw32-%{pkgname}
MinGW Windows JPEG XR library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows JPEG XR library

%description -n mingw64-%{pkgname}
MinGW Windows JPEG XR library.


%{?mingw_debug_package}


%prep
%setup -q -n %{pkgname}

# Sanitize charset and line endings
for file in `find . -type f -name '*.c' -or -name '*.h' -or -name '*.txt'`; do
  iconv --from=ISO-8859-15 --to=UTF-8 $file > $file.new && \
  sed -i 's|\r||g' $file.new && \
  touch -r $file $file.new && mv $file.new $file
done

# Remove file which already exists as part of the mingw headers
rm -f common/include/guiddef.h

%patch0 -p1
%patch1 -p1

cp -a %{SOURCE1} .


%build
%mingw_cmake
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%{mingw32_bindir}/libjpegxr.dll
%{mingw32_bindir}/libjxrglue.dll
%{mingw32_bindir}/JxrDecApp.exe
%{mingw32_bindir}/JxrEncApp.exe
%{mingw32_includedir}/jxrlib/
%{mingw32_libdir}/libjpegxr.dll.a
%{mingw32_libdir}/libjxrglue.dll.a

%files -n mingw64-%{pkgname}
%{mingw64_bindir}/libjpegxr.dll
%{mingw64_bindir}/libjxrglue.dll
%{mingw64_bindir}/JxrDecApp.exe
%{mingw64_bindir}/JxrEncApp.exe
%{mingw64_includedir}/jxrlib/
%{mingw64_libdir}/libjpegxr.dll.a
%{mingw64_libdir}/libjxrglue.dll.a


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 06 2015 Sandro Mani <manisandro@gmail.com> - 1.1-1
- Initial package
