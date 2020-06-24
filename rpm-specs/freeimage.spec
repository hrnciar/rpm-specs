# https://bugzilla.redhat.com/show_bug.cgi?id=1676717
%undefine _ld_as_needed

%define major 3

Name:           freeimage
Version:        3.18.0
Release:        8%{?dist}
Summary:        Multi-format image decoder library

# freeimage is tripple-licensed, see
# http://freeimage.sourceforge.net/license.html
# https://lists.fedoraproject.org/pipermail/legal/2013-October/002271.html
License:        GPLv2 or GPLv3 or MPLv1.0
URL:            http://freeimage.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/FreeImage%(echo %{version} | sed 's|\.||g').zip
# Unbundle bundled libraries
Patch0:         FreeImage_unbundle.patch
# Fix incorrect path in doxyfile
Patch1:         FreeImage_doxygen.patch
# Fix incorrect variable names in BIGENDIAN blocks
Patch2:         FreeImage_bigendian.patch
# Backport fixes for CVE-2019-12211 and 2019-12213
# https://sourceforge.net/p/freeimage/svn/1825/tree//FreeImage/trunk/Source/FreeImage/PluginTIFF.cpp?diff=5a0ca8dd5a4a1f6b3942a079:1824
Patch3:         CVE-2019-12211_2019-12213.patch
Patch4:         substream.patch

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  jxrlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  LibRaw-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  openjpeg2-devel

%description
FreeImage is a library for developers who would like to support popular
graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by
today's multimedia applications.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        plus
Summary:        C++ wrapper for FreeImage

%description    plus
The %{name}-plus package contains the C++ wrapper library for %{name}.


%package        plus-devel
Summary:        Development files for %{name}-devel
Requires:       %{name}-plus%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    plus-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}-plus.


%prep
%autosetup -p1 -n FreeImage

# remove all included libs to make sure these don't get used during compile
rm -r Source/Lib* Source/ZLib Source/OpenEXR

# clear files which cannot be built due to dependencies on private headers
# (see also unbundle patch)
> Source/FreeImage/PluginG3.cpp
> Source/FreeImageToolkit/JPEGTransform.cpp

# sanitize encodings / line endings
for file in `find . -type f -name '*.c' -or -name '*.cpp' -or -name '*.h' -or -name '*.txt' -or -name Makefile`; do
  iconv --from=ISO-8859-15 --to=UTF-8 $file > $file.new && \
  sed -i 's|\r||g' $file.new && \
  touch -r $file $file.new && mv $file.new $file
done


%build
sh ./gensrclist.sh
sh ./genfipsrclist.sh
%ifarch %{power64} %{mips32} aarch64
%make_build -f Makefile.gnu CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LDFLAGS="%{__global_ldflags}"
%make_build -f Makefile.fip CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" LDFLAGS="%{__global_ldflags}"
%else
%make_build -f Makefile.gnu CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"
%make_build -f Makefile.fip CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"
%endif

pushd Wrapper/FreeImagePlus/doc
doxygen FreeImagePlus.dox
popd


%install
install -Dpm 755 Dist/lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}-%{version}.so
ln -s lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}.so

install -Dpm 755 Dist/lib%{name}plus-%{version}.so %{buildroot}%{_libdir}/lib%{name}plus-%{version}.so
ln -s lib%{name}plus-%{version}.so %{buildroot}%{_libdir}/lib%{name}plus.so

install -Dpm 644 Source/FreeImage.h %{buildroot}%{_includedir}/FreeImage.h
install -Dpm 644 Wrapper/FreeImagePlus/FreeImagePlus.h %{buildroot}%{_includedir}/FreeImagePlus.h

# install missing symlink (was giving no-ldconfig-symlink rpmlint errors)
ldconfig -n %{buildroot}%{_libdir}


%ldconfig_scriptlets

%ldconfig_scriptlets plus


%files
%license license-*.txt
%doc Whatsnew.txt
%{_libdir}/lib%{name}-%{version}.so
%{_libdir}/lib%{name}.so.%major

%files devel
%doc Examples
%{_includedir}/FreeImage.h
%{_libdir}/lib%{name}.so

%files plus
%doc Wrapper/FreeImagePlus/WhatsNew_FIP.txt
%{_libdir}/lib%{name}plus-%{version}.so
%{_libdir}/lib%{name}plus.so.%major

%files plus-devel
%doc Wrapper/FreeImagePlus/html
%{_includedir}/FreeImagePlus.h
%{_libdir}/lib%{name}plus.so


%changelog
* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.18.0-8
- Rebuild for new LibRaw

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-6
- Backport fixes for CVE-2019-12211 and 2019-12213

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 3.18.0-4
- Rebuild for OpenEXR 2.3.0.

* Wed Feb 13 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-3
- Disable --Wl,--as-needed (#1676717)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 3.18.0-1
- Update to 3.18.0

* Thu Jul 19 2018 Adam Williamson <awilliam@redhat.com> - 3.17.0-16
- Rebuild for new libraw
- fPIC for aarch64 also

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.coM> - 3.17.0-14
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 3.17.0-9
- Rebuild (libwebp)

* Tue Dec 27 2016 Jon Ciesla <limburgher@gmail.com> - 3.17.0-8
- Rebuild for new LibRaw.

* Tue Oct 04 2016 Sandro Mani <manisandro@gmail.com> - 3.17.0-7
- Fix CVE-2016-5684 (rhbz#1381517)

* Fri Aug 12 2016 Michal Toman <mtoman@fedoraproject.org> - 3.17.0-6
- -fPIC on 32-bit MIPS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.17.0-4
- Rebuilt for libwebp soname bump

* Thu Oct 15 2015 Karsten Hopp <karsten@redhat.com> 3.17.0-3
- ppc64 and ppc64le need -fPIC (rhbz#1272048)

* Wed Sep 30 2015 Sandro Mani <manisandro@gmail.com> - 3.17.0-2
- Fix under-linked library

* Thu Sep 17 2015 Sandro Mani <manisandro@gmail.com> - 3.17.0-1
- Update to 3.17.0
- Add fix for CVE-2015-0852 (#1257859)
- Put freeimage-plus in separate package

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.10.0-24
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 3.10.0-23
- rebuild (gcc5)

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 3.10.0-22
- rebuild (openexr), tighten subpkg deps via %%{?_isa}

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.10.0-19
- rebuild (openexr)

* Mon Sep 09 2013 Bruno Wolff III <bruno@wolff.to> 3.10.0-18
- Rebuild for ilmbase related soname bumps

* Mon Aug 26 2013 Jon Ciesla <limburgher@gmail.com> - 3.10.0-17
- libmng rebuild.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.10.0-15
- rebuild (OpenEXR)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.10.0-13
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.10.0-12
- rebuild against new libjpeg

* Fri Aug  3 2012 Tom Lane <tgl@redhat.com> 3.10.0-11
- Add patch for libtiff 4.0 API changes
Resolves: #845407

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 13 2012 Bruno Wolff III <bruno@wolff.to> 3.10.0-9
- Update for libpng 1.5 API

* Thu Feb 09 2012 Rex Dieter <rdieter@fedoraproject.org> 3.10.0-8
- rebuild (openjpeg)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.10.0-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.10.0-4
- rebuild (openjpeg)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 18 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 3.10.0-1
- Initial Fedora package
