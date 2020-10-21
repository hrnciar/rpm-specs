%undefine __cmake_in_source_build
Name: luminance-hdr
Version: 2.6.0
Release: 9%{?dist}
Summary: A graphical tool for creating and tone-mapping HDR images

License: GPLv2+
URL: http://qtpfsgui.sourceforge.net/
Source0: http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.bz2
# fix build on non-x86 arches
Patch0: luminance-hdr-2.6.0-non-x86.patch

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
%ifarch %{?qt5_qtwebengine_arches}%{?!qt5_qtwebengine_arches:%{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
BuildRequires: qt5-qtwebengine-devel
%else
BuildRequires: qt5-qtwebkit-devel
%endif
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: OpenEXR-devel
BuildRequires: exiv2-devel
BuildRequires: fftw-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: gsl-devel
BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: LibRaw-devel
BuildRequires: libpng-devel
BuildRequires: lcms2-devel
BuildRequires: boost-devel
BuildRequires: CCfits-devel
BuildRequires: eigen3-devel
BuildRequires: gtest
BuildRequires: git

Obsoletes: qtpfsgui < 2.2.0
Provides: qtpfsgui = %{version}-%{release}

%description
Luminance is a graphical program for assembling bracketed photos into High
Dynamic Range (HDR) images.  It also provides a number of tone-mapping
operators for creating low dynamic range versions of HDR images.

%prep
%setup -q -n %{name}-%{version}%{?pre:-%{pre}}

%ifnarch %{ix86} x86_64
%patch0 -p1
%endif

# fix inconsistant newlines
%{__sed} -i 's/\r//' Changelog

%build
%{cmake} -DBUILD_SHARED_LIBS:BOOL=OFF -DCMAKE_BUILD_TYPE=Release .
%{cmake_build} %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{cmake_install}
cp -pf %{_vpath_builddir}/*.qm %{buildroot}/%{_datadir}/%{name}/i18n
mkdir -p %{buildroot}/%{_datadir}/mime/packages
cp -pf luminance-hdr.xml %{buildroot}/%{_datadir}/mime/packages
cp -pf net.sourceforge.qtpfsgui.LuminanceHDR.desktop %{buildroot}/%{_datadir}/applications

desktop-file-install --delete-original \
	--dir=%{buildroot}/%{_datadir}/applications \
	%{buildroot}/%{_datadir}/applications/net.sourceforge.qtpfsgui.LuminanceHDR.desktop

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%files
%doc AUTHORS Changelog README.md TODO
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/appdata/net.sourceforge.qtpfsgui.LuminanceHDR.appdata.xml
%{_datadir}/applications/net.sourceforge.qtpfsgui.LuminanceHDR.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
* Tue Aug 04 2020 Franco Comida <francocomida@gmail.com> - 2.6.0-9
- fix build on f33/rawhide

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 2.6.0-6
- Rebuilt for Boost 1.73

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.6.0-5
- Rebuild for new LibRaw

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.6.0-3
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Franco Comida <francocomida@gmail.com> - 2.6.0-1
- Update to Release 2.6.0

* Mon Apr 29 2019 Franco Comida <fcomida@users.sourceforge.net> - 2.5.1-20
- Fix compilation with gcc 9

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 2.5.1-19
- Rebuild for OpenEXR 2.3.0.
- Move LICENSE to %%license.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.5.1-17
- rebuild (exiv2)

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2.5.1-16
- Rebuilt for Boost 1.69

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.5.1-15
- Rebuild with fixed binutils

* Thu Jul 26 2018 Adam Williamson <awilliam@redhat.com> - 2.5.1-14
- Rebuild for new libraw

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 2.5.1-12
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 2.5.1-11
- rebuilt for cfitsio 3.420 (so version bump)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2.5.1-9
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.1-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 2.5.1-5
- Rebuilt for Boost 1.64

* Thu May 11 2017 Franco Comida <francocomida@gmail.com> - 2.5.1-4
- Fix date in specfile

* Thu May 11 2017 Franco Comida <francocomida@gmail.com> - 2.5.1-3
- Fix qtwebkit patch again

* Thu May 11 2017 Franco Comida <francocomida@gmail.com> - 2.5.1-2
- Fix qtwebkit patch

* Wed May 10 2017 Franco Comida <francocomida@gmail.com> - 2.5.1-1
- Release 2.5.1

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.5.0-4
- rebuild (exiv2)

* Tue Apr 18 2017 Franco Comida <francocomida@gmail.com> - 2.5.0-3
- Upstream retired previous 2.5.0, now it's out again. Let's start again from there.

* Mon Apr 10 2017 Dan Horák <dan[at]danny.cz> - 2.5.0-2
- fix build with qtwebengine vs. qtwebkit

* Sun Apr 09 2017 Franco Comida <francocomida@gmail.com> - 2.5.0-1
- Update to Release 2.5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-12
- Rebuilt for Boost 1.63

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 2.4.0-11
- Rebuild for new LibRaw.

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-10
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-8
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.4.0-7
- Rebuilt for Boost 1.59

* Thu Aug 20 2015 Jon Ciesla <limburgher@gmail.com> - 2.4.0-6
- Rebuild for new LibRaw.

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.4.0-4
- rebuild for Boost 1.58

* Tue Jul 07 2015 Franco Comida <francocomida@gmail.com> - 2.4.0-3
- Fix saving TMO parameters

* Sat Jul 04 2015 Franco Comida <francocomida@gmail.com> - 2.4.0-2
- Fix Application Icon Size

* Thu Jul 02 2015 Franco Comida <francocomida@gmail.com> - 2.4.0-1
- Updated to Luminance HDR 2.4.0

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-15
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.1-13
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.3.1-12
- Add an AppData file for the software center

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.3.1-11
- Rebuild for boost 1.57.0

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.1-10
- rebuild (openexr)

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.1-9
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.3.1-6
- Rebuild for boost 1.55.0

* Wed Jan 22 2014 Jon Ciesla <limburgher@gmail.com> - 2.3.1-5
- Rebuild for new LibRaw.

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-4
- rebuild (exiv2)

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-3
- rebuild (openexr)

* Fri Sep 20 2013 Dan Horák <dan[at]danny.cz> - 2.3.1-2
- fix build on non-x86 arches

* Fri Sep 13 2013 Franco Comida <francocomida@googlemail.com> - 2.3.1-1
- Updated to Luminance HDR 2.3.1

* Mon Sep 09 2013 Rex Dieter <rdieter@fedoraproject.org> 2.3.0-9
- rebuild (OpenEXR)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Jon Ciesla <limburgher@gmail.com> - 2.3.0-7
- Rebuild for new LibRaw.

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.3.0-6
- rebuild (OpenEXR)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.3.0-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.3.0-3
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Franco Comida <francocomida@googlemail.com> - 2.3.0-1
- Updated to Luminance HDR 2.3.0

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-4
- rebuild (exiv2)

* Wed Mar 28 2012 Dan Horák <dan[at]danny.cz> - 2.2.1-3
- fix build on non-x86 arches

* Tue Mar 13 2012 Franco Comida <francocomida@googlemail.com> - 2.2.1-2
- Removed unused PATH from luminance-hdr.desktop

* Sun Mar 11 2012 Franco Comida <fcomida@users.sourceforge.net> 2.2.1-1
- Updated to Luminance HDR 2.2.1

* Tue Feb 21 2012 Franco Comida <fcomida@users.sourceforge.net> 2.2.0-1
- Luminance HDR 2.2.0

