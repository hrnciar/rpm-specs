%global		soversion	2.0

Name:		nvidia-texture-tools
Version:	2.0.8
Release:	22%{?dist}
Summary:	Collection of image processing and texture manipulation tools
License:	MIT
URL:		http://code.google.com/p/nvidia-texture-tools/
Source0:	http://nvidia-texture-tools.googlecode.com/files/%{name}-%{version}-1.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	help2man
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	openjpeg-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
# g++ 4.7 does not include unistd.h by default to avoid namespace polution
Patch0:		%{name}-%{version}-gcc4.7.patch
# use a saner type for int64 and uint64 generic typedefs that are unlikely
# to conflict with other headers that do not use long long on 64 bit
Patch1:		%{name}-%{version}-wordsize.patch
# from 0ad sources
Patch2:		%{name}-%{version}-png-api.patch
# add soversion to libraries
Patch3:		%{name}-%{version}-soversion.patch
# install libraries in proper directory
Patch4:		%{name}-%{version}-libdir.patch
# add arm support
Patch5:         %{name}-arm.patch
# add aarch64 support
Patch6:         %{name}-aarch64.patch
# Return NULL not false on pointer returning functions
Patch7:		%{name}-bool-null.patch
# add MIPS support
Patch8:		%{name}-mips.patch
# add S390 support
Patch9:		%{name}-s390.patch
# add PPCLE support
Patch10:	%{name}-ppcle.patch

%description
The NVIDIA Texture Tools is a collection of image processing and texture
manipulation tools, designed to be integrated in game tools and asset
conditioning pipelines.

The primary features of the library are mipmap and normal map generation,
format conversion and DXT compression.

DXT compression is based on Simon Brown's squish library. The library also
contains an alternative GPU-accelerated compressor that uses CUDA and is
one order of magnitude faster.

%package	devel
Summary:	Development libraries/headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Headers and libraries for development with %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
mkdir -p build
pushd build
    %cmake -DNVTT_SHARED=1 -DCMAKE_SKIP_RPATH=1 ..
    make %{?_smp_mflags}
popd

sed -e 's/\r//' -i NVIDIA_*.txt

%install
make -C build install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
pushd $RPM_BUILD_ROOT/%{_bindir}
    export LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:
    for bin in *; do
	help2man --no-info ./$bin > $RPM_BUILD_ROOT/%{_mandir}/man1/$bin.1
    done
popd

%check
make -C build filtertest

%ldconfig_scriptlets

%files
%doc NVIDIA_Texture_Tools_LICENSE.txt
%doc NVIDIA_Texture_Tools_README.txt
%{_bindir}/*
%{_libdir}/lib*.%{version}
%{_libdir}/lib*.%{soversion}
%{_mandir}/man1/*

%files		devel
%doc ChangeLog
%{_includedir}/nvtt
%{_libdir}/lib*.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-17
- Correct FTBFS in rawhide (#1424003)
- Add support for MIPS (#1366716)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 17 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-13
- Correct FTBFS in rawhide (#1307810)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.8-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.8-8
- add patch to fix ftbfs on aarch64

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Dennis Gilmore <dennis@ausil.us> - 2.0.8-6
- fix build on arm

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 2.0.8-4
- rebuild due to "jpeg8-ABI" feature drop

* Wed Dec 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-3
- Correct source url (#823096).
- No need for a -progs subpackage (#823096).

* Wed May 30 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-2
- Rename tools subpackage to progs.

* Fri May 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-1
- Initial nvidia-texture-tools spec.
