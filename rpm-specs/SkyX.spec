Name:           SkyX
Version:        0.4
Release:        26%{?dist}
Summary:        Photo-realistic sky simulator

License:        LGPLv2+
URL:            http://www.paradise-sandbox.com/#hydraxskyx.php
Source0:        http://modclub.rigsofrods.com/xavi/SkyX/SkyX-v0.4.rar
Source1:        http://modclub.rigsofrods.com/xavi/SkyX/SkyX-v0.3_CMake.rar
# This patch contains some modifications made by the Gazebo project.
# It is mostly comment changes, but there are some API extensions needed
# by the gazebo robot simulator.
Patch0:         skyx_gazebo.patch
# This patch fixes some issues with building against Ogre 1.9.
# Not submitted upstream
Patch1:         %{name}-0.4-ogre19.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  ogre-devel
BuildRequires:  ois-devel
BuildRequires:  dos2unix
BuildRequires:  unar

%description
SkyX is a photo-realistic, simple and fast sky simulator.  It can be used
with the OGRE engine.

%package devel
Summary: Development files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -T -c
unar %{SOURCE0}
mv SkyX-v0.4/* .
unar %{SOURCE1}
cp -r SkyX-v0.3/* .
rm -rf SkyX-v0.*
rm -f SkyXCommon/Bin/Media/packs/OgreCore.zip

%patch0 -p1
%patch1 -p0 -b .ogre19

# Remove Windows line endings
dos2unix Readme.txt License.txt
# Convert to UTF8
iconv -f ISO-8859-15 -t UTF-8 License.txt > License.conv && mv -f License.{conv,txt}
iconv -f ISO-8859-15 -t UTF-8 Readme.txt > Readme.conv && mv -f Readme.{conv,txt}

%build
mkdir build
cd build
%cmake .. \
  -DSKYX_BUILD_SAMPLES=OFF 
make %{?_smp_mflags}


%install
make -C build install DESTDIR=%{buildroot}
mv %{buildroot}/SKYX/cmake %{buildroot}%{_datadir}/SKYX
%if "%{_lib}" == "lib64"
mv %{buildroot}/%{_usr}/lib %{buildroot}%{_libdir}
%endif

%ldconfig_scriptlets

%files
%doc License.txt Readme.txt
%{_libdir}/*.so.*
%exclude %{_datadir}/SKYX/cmake
%{_datadir}/SKYX

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/SKYX
%{_datadir}/SKYX/cmake

%changelog
* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 0.4-26
- Fix string quoting for rpm >= 4.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4-18
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4-16
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.4-14
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.4-12
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4-10
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 0.4-9
- Rebuild for boost 1.57.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Rich Mattes <richmattes@gmail.com> - 0.4-7
- Rebuild for ogre 1.9
- Update upstream URL

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Petr Machata <pmachata@redhat.com> - 0.4-5
- Rebuild for boost 1.55.0

* Sun Oct 20 2013 Rich Mattes <richmattes@gmail.com> - 0.4-4
- Fix build on i686 systems
- Correct project URL
- Correct license field (License.txt indicates LGPLv2+)

* Sun Oct 06 2013 Rich Mattes <richmattes@gmail.com> - 0.4-3
- Added patch containing Gazebo extensions

* Tue Aug 06 2013 Rich Mattes <richmattes@gmail.com> - 0.4-2
- Use upstream sources and unar

* Sun Jun 09 2013 Rich Mattes <richmattes@gmail.com> - 0.4-1
- Update to release 0.4

* Sun Jun 09 2013 Rich Mattes <richmattes@gmail.com> - 0.3.1-1
- Initial release
