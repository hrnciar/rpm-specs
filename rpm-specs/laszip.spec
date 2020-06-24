Name:           laszip
Version:        3.4.3
Release:        2%{?dist}
Summary:        Quickly turns bulky LAS files into compant LAZ files
License:        LGPLv2
Source0:        https://github.com/LASzip/LASzip/releases/download/%{version}/%{name}-src-%{version}.tar.gz
URL:            http://www.laszip.org/

# Restore old API for libLAS
# https://github.com/libLAS/libLAS/issues/144
Patch0:         laszip_restoreapi.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++


%description
LASzip - a free product of rapidlasso GmbH - quickly turns bulky LAS files into
compact LAZ files without information loss.

%package devel
Summary:        The development files for laszip
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for laszip


%prep
%autosetup -p1 -n %{name}-src-%{version}


%build
%cmake -DLASZIP_LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install


%ldconfig_scriptlets


%files
%doc AUTHORS
%license COPYING
%{_libdir}/liblaszip.so.8*
%{_libdir}/liblaszip_api.so.8*

%files devel
%{_includedir}/laszip/laszip_api.h
%{_includedir}/laszip/laszip_api_version.h
%{_includedir}/laszip/laszip.hpp
%{_includedir}/laszip/laszipper.hpp
%{_includedir}/laszip/lasunzipper.hpp

%{_libdir}/liblaszip.so
%{_libdir}/liblaszip_api.so


%changelog
* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 3.4.3-2
- Restore old API for libLAS

* Tue Apr 14 2020 Sandro Mani <manisandro@gmail.com> - 3.4.3-1
- Update to 3.4.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Devrim GUNDUZ <devrim@gunduz.org> 2.2.0-4
- More fixes per Fedora review:
 - Update license
 - omit liblaszip.a static library
 - fix liblaszip undefined symbols, by adding -lstdc++ CFLAG
 - omit INSTALL from %%doc
 - Own %%{_includedir}/laszip/ directory
 - devel subpkg now depends on main package
 - omit deprecated Group: tags and %%clean section
 - drop not needed dependency to cmake
 - move liblaszip.so symlink to -devel subpkg

* Fri Apr 17 2015 Devrim GUNDUZ <devrim@gunduz.org> 2.2.0-3
- Various fixes per Fedora review #1199296
  * Add devel subpackage
  * Use %%license macro
  * Use %%make_install macro
  * Get rid of BuildRoot definition
  * No need to cleanup buildroot during %%install
  * Remove %%defattr
  * Run ldconfig 
  * Fix version numbers

* Fri Mar 6 2015 Devrim GUNDUZ <devrim@gunduz.org> 2.2.0-2
- Rebuild with new liblas.

* Fri Mar 6 2015 Devrim GUNDUZ <devrim@gunduz.org> 2.2.0-2
- Rebuild with new liblas.

* Tue Jan 13 2015 Devrim GUNDUZ <devrim@gunduz.org> 2.2.0-1
- Initial packaging

