# Force out of source build
%undefine __cmake_in_source_build

Name:           alure
Version:        1.2
Release:        21%{?dist}
Summary:        Audio Library Tools REloaded
# ALURE code is LGPLv2+; note -devel subpackage has its own license tag
License:        LGPLv2+ 
URL:            http://kcat.strangesoft.net/alure.html
Source0:        http://kcat.strangesoft.net/%{name}-releases/%{name}-%{version}.tar.bz2
Patch0:         alure-gcc47.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake, libvorbis-devel, libsndfile-devel, openal-soft-devel, flac-devel, dumb-devel, fluidsynth-devel


%description
ALURE is a utility library to help manage common tasks with OpenAL 
applications. This includes device enumeration and initialization, 
file loading, and streaming.  


%package        devel
Summary:        Development files for %{name}
# Devel doc includes some files under GPLv2+ from NaturalDocs
License:        LGPLv2+ and GPLv2+
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q 
%patch0


%build
%cmake -DBUILD_STATIC:BOOL=OFF
%cmake_build


%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
# strip installed html doc
rm -rf %{buildroot}%{_docdir}/alure/html



%ldconfig_scriptlets


%files
%doc COPYING
%{_libdir}/*.so.*
%{_bindir}/alure*


%files devel
%doc docs/html examples
%{_includedir}/AL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-9
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 30 2012 Bruno Wolff III <bruno@wolff.to> - 1.2-3
- Fix for gcc 4.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 29 2011 Julian Aloofi <julian@fedoraproject.org> - 1.2-1
- update to latest upstream release

* Sat May 28 2011 Julian Aloofi <julian@fedoraproject.org> - 1.1-1
- update to latest upstream release
- enabled FLAC, DUMB and fluidsynth support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 01 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-4
- Fixed license for -devel subpackage
- Included sample code in -devel subpackage
- Sanitized %%files

* Tue Sep 29 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-3
- Renamed from libalure to alure
- Fixed license

* Mon Sep 28 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-2
- Fix multilib pkgconfig path

* Sat Sep 26 2009 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-1
- Initial packaging 
