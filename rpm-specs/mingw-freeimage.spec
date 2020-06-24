
%{?mingw_package_header}

%global win32dir %{_builddir}/mingw32-%{pkgname}-%{version}-%{release}
%global win64dir %{_builddir}/mingw64-%{pkgname}-%{version}-%{release}

%global pkgname freeimage
%global ver_major 3

Name:          mingw-%{pkgname}
Version:       3.18.0
Release:       8%{?dist}
Summary:       MinGW Windows %{pkgname} library

# freeimage is tripple-licensed, see
# http://freeimage.sourceforge.net/license.html
# https://lists.fedoraproject.org/pipermail/legal/2013-October/002271.html
License:       GPLv2 or GPLv3 or MPLv1.0
BuildArch:     noarch
URL:           http://freeimage.sourceforge.net/
Source:        http://downloads.sourceforge.net/%{pkgname}/FreeImage%(echo %{version} | sed 's|\.||g').zip
# Unbundle bundled libraries
Patch0:        FreeImage_unbundle.patch
# MinGW makefile fixes
Patch1:        FreeImage_mingw.patch
# Backport fixes for CVE-2019-12211 and 2019-12213
# https://sourceforge.net/p/freeimage/svn/1825/tree//FreeImage/trunk/Source/FreeImage/PluginTIFF.cpp?diff=5a0ca8dd5a4a1f6b3942a079:1824
Patch2:         CVE-2019-12211_2019-12213.patch


BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-ilmbase
BuildRequires: mingw32-jxrlib
BuildRequires: mingw32-lcms2
BuildRequires: mingw32-LibRaw
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libpng
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libwebp
BuildRequires: mingw32-OpenEXR
BuildRequires: mingw32-openjpeg2

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-ilmbase
BuildRequires: mingw64-jxrlib
BuildRequires: mingw64-lcms2
BuildRequires: mingw64-LibRaw
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libpng
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libwebp
BuildRequires: mingw64-OpenEXR
BuildRequires: mingw64-openjpeg2


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
%{summary}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
%{summary}.


%{?mingw_debug_package}


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

# Create source lists
sh ./gensrclist.sh
sh ./genfipsrclist.sh

# Create source trees
cp -a . %{win32dir}
cp -a . %{win64dir}


%build
%mingw32_make -C %{win32dir} MINGW_TARGET=%mingw32_target -f Makefile.gnu %{?_smp_mflags}
%mingw32_make -C %{win32dir} MINGW_TARGET=%mingw32_target -f Makefile.fip %{?_smp_mflags}

%mingw64_make -C %{win64dir} MINGW_TARGET=%mingw64_target -f Makefile.gnu %{?_smp_mflags}
%mingw64_make -C %{win64dir} MINGW_TARGET=%mingw64_target -f Makefile.fip %{?_smp_mflags}


%install
install -Dpm 0755 %{win32dir}/Dist/freeimage-%ver_major.dll %{buildroot}%{mingw32_bindir}/freeimage-%ver_major.dll
install -Dpm 0644 %{win32dir}/Dist/freeimage.dll.a %{buildroot}%{mingw32_libdir}/freeimage.dll.a
install -Dpm 0644 %{win32dir}/Dist/libfreeimage.a %{buildroot}%{mingw32_libdir}/libfreeimage.a
install -Dpm 0644 %{win32dir}/Dist/FreeImage.h %{buildroot}%{mingw32_includedir}/FreeImage.h

install -Dpm 0755 %{win64dir}/Dist/freeimage-%ver_major.dll %{buildroot}%{mingw64_bindir}/freeimage-%ver_major.dll
install -Dpm 0644 %{win64dir}/Dist/freeimage.dll.a %{buildroot}%{mingw64_libdir}/freeimage.dll.a
install -Dpm 0644 %{win64dir}/Dist/libfreeimage.a %{buildroot}%{mingw64_libdir}/libfreeimage.a
install -Dpm 0644 %{win64dir}/Dist/FreeImage.h %{buildroot}%{mingw64_includedir}/FreeImage.h

install -Dpm 0755 %{win32dir}/Dist/freeimageplus-%ver_major.dll %{buildroot}%{mingw32_bindir}/freeimageplus-%ver_major.dll
install -Dpm 0644 %{win32dir}/Dist/freeimageplus.dll.a %{buildroot}%{mingw32_libdir}/freeimageplus.dll.a
install -Dpm 0644 %{win32dir}/Dist/libfreeimageplus.a %{buildroot}%{mingw32_libdir}/libfreeimageplus.a
install -Dpm 0644 %{win32dir}/Dist/FreeImagePlus.h %{buildroot}%{mingw32_includedir}/FreeImagePlus.h

install -Dpm 0755 %{win64dir}/Dist/freeimageplus-%ver_major.dll %{buildroot}%{mingw64_bindir}/freeimageplus-%ver_major.dll
install -Dpm 0644 %{win64dir}/Dist/freeimageplus.dll.a %{buildroot}%{mingw64_libdir}/freeimageplus.dll.a
install -Dpm 0644 %{win64dir}/Dist/libfreeimageplus.a %{buildroot}%{mingw64_libdir}/libfreeimageplus.a
install -Dpm 0644 %{win64dir}/Dist/FreeImagePlus.h %{buildroot}%{mingw64_includedir}/FreeImagePlus.h


%files -n mingw32-%{pkgname}
%license license-fi.txt license-gplv2.txt license-gplv3.txt
%{mingw32_bindir}/freeimage-%ver_major.dll
%{mingw32_bindir}/freeimageplus-%ver_major.dll
%{mingw32_includedir}/FreeImage.h
%{mingw32_includedir}/FreeImagePlus.h
%{mingw32_libdir}/freeimage.dll.a
%{mingw32_libdir}/freeimageplus.dll.a

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libfreeimage.a
%{mingw32_libdir}/libfreeimageplus.a

%files -n mingw64-%{pkgname}
%license license-fi.txt license-gplv2.txt license-gplv3.txt
%{mingw64_bindir}/freeimage-%ver_major.dll
%{mingw64_bindir}/freeimageplus-%ver_major.dll
%{mingw64_includedir}/FreeImage.h
%{mingw64_includedir}/FreeImagePlus.h
%{mingw64_libdir}/freeimage.dll.a
%{mingw64_libdir}/freeimageplus.dll.a

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libfreeimage.a
%{mingw64_libdir}/libfreeimageplus.a


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-7
- Backport fixes for CVE-2019-12211 and 2019-12213

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-6
- Rebuild (OpenEXR)

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-5
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Sandro Mani <manisandro@gmail.com> - 3.18.0-3
- Rebuild (IlmBase, OpenEXR)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 3.18.0-1
- Update to 3.18.0

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 3.17.0-13
- Rebuild (LibRaw)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Sandro Mani <manisandro@gmail.com> - 3.17.0-10
- Rebuild (OpenEXR)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Sandro Mani <manisandro@gmail.com> - 3.17.0-8
- Rebuild (LibRaw)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 3.17.0-6
- Rebuild (libwebp)

* Sun Jan 01 2017 Sandro Mani <manisandro@gmail.com> - 3.17.0-5
- Rebuild (LibRaw)

* Tue Oct 04 2016 Sandro Mani <manisandro@gmail.com> - 3.17.0-4
- Fix CVE-2016-5684 (rhbz#1381517)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Sandro Mani <manisandro@gmail.com> - 3.17.0-2
- Rebuild (libwebp)

* Sat Nov 14 2015 Sandro Mani <manisandro@gmail.com> - 3.17.0-1
- Update to 3.17.0
- Add fix for CVE-2015-0852 (#1257859)

* Sun Aug 23 2015 Sandro Mani <manisandro@gmail.com> - 3.15.4-7
- Rebuild (LibRaw)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Sandro Mani <manisandro@gmail.com> - 3.15.4-5
- Rebuild (ilmbase, OpenEXR)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Sandro Mani <manisandro@gmail.com> - 3.15.4-3
- Delete Source/ZLib folder
- Convert Whatsnew.txt, license-gplv3.txt to UTF-8

* Thu Jan 16 2014 Sandro Mani <manisandro@gmail.com> - 3.15.4-2
- Completely unbundle libraries (thanks to František Dvořák)

* Tue Jan 07 2014 Sandro Mani <manisandro@gmail.com> - 3.15.4-1
- Initial package
