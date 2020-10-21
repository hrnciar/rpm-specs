%{?mingw_package_header}

%global pkgname twaindsm

Name:          mingw-%{pkgname}
Version:       2.4.2
Release:       6%{?dist}
Summary:       TWAIN Data Source Manager

License:       LGPLv2+
URL:           https://github.com/twain/twain-dsm
BuildArch:     noarch
# Hopefully they'll switch to doing proper releases... (https://github.com/twain/twain-dsm/issues/3)
Source0:       https://github.com/twain/twain-dsm/raw/master/Releases/dsm_020402/tarball/%{pkgname}_%{version}.orig.tar.gz

### Upstreamable patches: https://github.com/twain/twain-dsm/pull/4
# Use TWNDSM_OS to detect platform instead of TWNDSM_CMP
# - sed -i 's/TWNDSM_CMP == TWNDSM_CMP_VISUALCPP/TWNDSM_OS == TWNDSM_OS_WINDOWS/g' src/{*.cpp,*.h}
# - sed -i 's/(TWNDSM_CMP == TWNDSM_CMP_GNUGPP)/(TWNDSM_OS == TWNDSM_OS_LINUX) || (TWNDSM_OS == TWNDSM_OS_MACOSX)/g' src/{*.cpp,*.h}
Patch0:        twaindsm_defs.patch
# Add MINGW support to the cmake file
Patch1:        twaindsm_cmake.patch
# Fix build failure due to invalid conversion
Patch2:        twaindsm_build-errors.patch

### Downstream patch (could be discussed upstream I suppose)
# Don't raise an assertion just because an error occured, leave it to the consumer to deal with the error...
Patch10:        twaindsm_assert.patch

BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++


%description
TWAIN Data Source Manager, compliant with the TWAIN specification version 2.2.

###############################################################################

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

###############################################################################

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

###############################################################################

%{?mingw_debug_package}


%prep
%autosetup -p1 -n TWAIN_DSM

# Remove build leftovers...
rm -rf src/CMakeFiles
rm -f src/CMakeCache.txt
rm -f src/cmake_install.cmake

# Fix spurious-executable-perm
chmod -x README.txt ChangeLog.txt license.txt


%build
pushd src
%mingw_cmake .
%mingw_make %{?_smp_mflags} VERBOSE=1
popd


%install
pushd src
%mingw_make DESTDIR=%{buildroot} install
popd


%files -n mingw32-%{pkgname}
%doc README.txt ChangeLog.txt
%license license.txt
%{mingw32_bindir}/twaindsm.dll
%{mingw32_libdir}/libtwaindsm.dll.a
%{mingw32_includedir}/twain.h

%files -n mingw64-%{pkgname}
%doc README.txt ChangeLog.txt
%license license.txt
%{mingw64_bindir}/twaindsm.dll
%{mingw64_libdir}/libtwaindsm.dll.a
%{mingw64_includedir}/twain.h


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.4.2-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 16 2017 Sandro Mani <manisandro@gmail.com> - 2.4.0-2
- Remove executable bit from doc and license files

* Fri Dec 15 2017 Sandro Mani <manisandro@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Sat Nov 22 2014 Sandro Mani <manisandro@gmail.com> - 2.3.1-1
- twaindsm-2.3.1
