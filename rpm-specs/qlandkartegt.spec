Name: qlandkartegt
Version: 1.8.1
Release: 26%{?dist}
Summary: GPS device mapping tool

License: GPLv3+
URL: http://www.qlandkarte.org/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# <GL/glu.h> not included by qt >= 4.8
Patch0: %{name}-1.3.0-glu.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1307966
Patch1: %{name}-1.8.1-char.patch
# fix string macros for C++11
Patch2: %{name}-1.8.1-string.patch
# update to libgps API version 7
Patch3: %{name}-1.8.1-gps.patch
# update to libgps API version 9
Patch4: %{name}-1.8.1-gps9.patch
Requires: garmindev(interface) = 1.18
Requires: gpsbabel
Requires: proj

BuildRequires: cmake
BuildRequires: qt4-devel
# Versions of qt4 older than 4.8 pulled in libGLU
BuildRequires: mesa-libGLU-devel
BuildRequires: proj-devel
BuildRequires: gdal-devel
BuildRequires: desktop-file-utils
BuildRequires: libexif-devel
BuildRequires: libdmtx-devel
BuildRequires: gpsd-devel
BuildRequires: qt-webkit-devel
BuildRequires: qtsoap-devel
BuildRequires: qextserialport-devel
BuildRequires: libjpeg-devel


%description
QLandkarte GT is the ultimate outdoor aficionado's tool for GPS maps in
GeoTiff format as well as Garmin's img vector map format. Additional it is
the PC side frontend to QLandkarte M, a moving map application for mobile
devices. And it fills the gap Garmin leaves in refusing to support Linux.
QLandkarte GT is the proof that writing portable applications for Unix,
Windows and OSX is feasible with a minimum of overhead. No excuses!

QLandkarte GT does replace the original QLandkarte with a much more
flexible architecture. It's not limited to a map format or device. Thus
if you think your Magellan GPS or other should be supported, join the team.

Additionally it is a front end to the GDAL tools, to make georeferencing
scanned maps feasible for the normal user. Compared to similar tools like
QGis, it's target users are more on the consumer side than on the scientific
one. QLandkarte GT might not let you select every possible feature of the
GDAL tools, but it will simplify their use to the demands of most users.


%prep
%autosetup -p1

# remove unbundled stuff
rm -rf 3rdparty/qtsoap 3rdparty/SerialPort/qextserialport

# create build direcotory
mkdir build


%build
%global optflags %{optflags} -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H
cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DGPX_EXTENSIONS=ON ..
make VERBOSE=1 %{?_smp_mflags}


%install
cd build
make install DESTDIR=%{buildroot}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license copying
%doc changelog.txt
%{_bindir}/%{name}
%{_bindir}/map2gcm
%{_bindir}/map2jnx
%{_bindir}/map2rmap
%{_bindir}/map2rmp
%{_bindir}/cache2gtiff
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.*


%changelog
* Thu Jun 18 2020 Björn Esser <besser82@fedoraproject.org> - 1.8.1-26
- Rebuild (gpsd)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-25
- Rebuild (gdal)

* Mon May 11 2020 Dan Horák <dan[at]danny.cz> - 1.8.1-24
- rebuild for proj packaging change (#1831138, #1834093, #1832466)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-23
- Rebuild (gdal)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.8.1-20
- Rebuild (gpsd)

* Thu Feb 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.8.1-19
- rebuilt (proj)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Dan Horák <dan[at]danny.cz> - 1.8.1-16
- fix FTBFS with C++11

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Dan Horák <dan[at]danny.cz> - 1.8.1-14
- Rebuilt for gpsd 3.17

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Dan Horák <dan@danny.cz> - 1.8.1-9
- Rebuilt for proj 4.9.3

* Mon Feb 15 2016 Dan Horák <dan@danny.cz> - 1.8.1-8
- fix FTBFS (#1307966)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Dan Horák <dan@danny.cz> - 1.8.1-6
- rebuild for GDAL 2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 12 2015 Dan Horák <dan[at]danny.cz> - 1.8.1-3
- rebuild for proj 4.1 and gpsd 3.11

* Sat Feb 21 2015 Dan Horák <dan[at]danny.cz> - 1.8.1-2
- update to 1.8.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 19 2014 Dan Horák <dan[at]danny.cz> - 1.7.7-1
- update to 1.7.7

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Dan Horák <dan[at]danny.cz> - 1.7.6-2
- unbundle qextserial library (#872883)

* Sun Feb 16 2014 Dan Horák <dan[at]danny.cz> - 1.7.6-1
- update to 1.7.6

* Tue Nov 26 2013 Dan Horák <dan[at]danny.cz> - 1.7.5-2
- rebuilt for gpsd 3.10

* Sat Oct 12 2013 Dan Horák <dan[at]danny.cz> - 1.7.5-1
- update to 1.7.5

* Mon Sep 16 2013 Dan Horák <dan[at]danny.cz> - 1.7.4-1
- update to 1.7.4

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 1.7.3-2
- Rebuild for gdal 1.10.0

* Sun Aug 18 2013 Dan Horák <dan[at]danny.cz> - 1.7.3-1
- update to 1.7.3

* Sun Jul 28 2013 Dan Horák <dan[at]danny.cz> 1.7.1-2
- proj-epsg is needed for online maps

* Thu Jul 11 2013 Dan Horák <dan[at]danny.cz> 1.7.1-1
- update to 1.7.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.6.0-2
- rebuild due to "jpeg8-ABI" feature drop

* Sun Nov 25 2012 Dan Horák <dan[at]danny.cz> 1.6.0-1
- update to 1.6.0

* Tue Oct 16 2012 Dan Horák <dan[at]danny.cz> 1.5.3-1
- update to 1.5.3

* Wed Aug 29 2012 Dan Horák <dan[at]danny.cz> 1.5.1-1
- update to 1.5.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Dan Horák <dan[at]danny.cz> 1.5.0-1
- update to 1.5.0

* Wed May 23 2012 Dan Horák <dan[at]danny.cz> 1.4.2-1
- update to 1.4.2

* Mon Apr 16 2012 Dan Horák <dan[at]danny.cz> 1.4.0-2
- fix crash when editing diary (#812605)

* Mon Feb 27 2012 Dan Horák <dan[at]danny.cz> 1.4.0-1
- update to 1.4.0

* Thu Jan 05 2012 Dan Horák <dan[at]danny.cz> 1.3.2-1
- update to 1.3.2

* Thu Dec 01 2011 Dan Horák <dan[at]danny.cz> 1.3.1-1
- update to 1.3.1

* Mon Nov 14 2011 Dan Horák <dan[at]danny.cz> 1.3.0-1
- update to 1.3.0

* Sun Oct 23 2011 Dan Horák <dan[at]danny.cz> 1.2.4-1
- update to 1.2.4

* Wed Aug 31 2011 Dan Horák <dan[at]danny.cz> 1.2.3-1
- update to 1.2.3

* Tue Aug 23 2011 Tom Callaway <spot@fedoraproject.org> - 1.2.2-2
- fix compile against qt 4.8 (ensure libGLU-devel)

* Tue Jul 12 2011 Dan Horák <dan[at]danny.cz> 1.2.2-1
- update to 1.2.2

* Thu Jun 30 2011 Dan Horák <dan[at]danny.cz> 1.2.1-1
- update to 1.2.1

* Thu Jun 16 2011 Dan Horák <dan[at]danny.cz> 1.2.0-1
- update to 1.2.0

* Wed Jun 15 2011 Dan Horák <dan[at]danny.cz> 1.1.2-2
- fix crash with 3D map if no map is selected (#641545)

* Mon May 23 2011 Dan Horák <dan[at]danny.cz> 1.1.2-1
- update to 1.1.2

* Sat Mar 19 2011 Dan Horák <dan[at]danny.cz> 1.1.1-1
- update to 1.1.1

* Thu Feb 17 2011 Dan Horák <dan[at]danny.cz> 1.1.0-1
- update to 1.1.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Dan Horák <dan[at]danny.cz> 1.0.1-1
- update to 1.0.1

* Sat Jan  1 2011 Dan Horák <dan[at]danny.cz> 1.0.0-2
- needs BR: qt-webkit-devel on F >= 14

* Sat Jan  1 2011 Dan Horák <dan[at]danny.cz> 1.0.0-1
- update to 1.0.0

* Wed Dec  8 2010 Dan Horák <dan[at]danny.cz> 0.20.3-1
- update to 0.20.3

* Fri Nov 19 2010 Dan Horák <dan[at]danny.cz> 0.20.2-1
- update to 0.20.2

* Wed Nov  3 2010 Dan Horák <dan[at]danny.cz> 0.20.1-1
- update to 0.20.1

* Mon Sep 27 2010 Dan Horák <dan[at]danny.cz> 0.19.2-1
- update to 0.19.2

* Mon Sep 13 2010 Dan Horák <dan[at]danny.cz> 0.19.1-1
- update to 0.19.1

* Mon Aug 16 2010 Dan Horák <dan[at]danny.cz> 0.19.0-1
- update to 0.19.0

* Sun Jul  4 2010 Dan Horák <dan[at]danny.cz> 0.18.4-1
- update to 0.18.4

* Sun Jul  4 2010 Dan Horák <dan[at]danny.cz> 0.18.3-2
- newer garmindev is needed

* Sat Jul  3 2010 Dan Horák <dan[at]danny.cz> 0.18.3-1
- update to 0.18.3
- dropped the gtkstyle hack

* Wed May 12 2010 Dan Horák <dan[at]danny.cz> 0.18.2-1
- update to 0.18.2

* Sat Apr  3 2010 Dan Horák <dan[at]danny.cz> 0.18.1-1
- update to 0.18.1

* Sat Mar  6 2010 Dan Horák <dan[at]danny.cz> 0.18.0-1
- update to 0.18.0

* Sat Feb  6 2010 Dan Horák <dan[at]danny.cz> 0.17.1-1
- update to 0.17.1

* Tue Jan 26 2010 Dan Horák <dan[at]danny.cz> 0.17.0-2
- added 2 fixes from upstream

* Mon Jan 25 2010 Dan Horák <dan[at]danny.cz> 0.17.0-1
- update to 0.17.0

* Wed Dec 23 2009 Dan Horák <dan[at]danny.cz> 0.16.1-1
- update to 0.16.1

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.16.0-3
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Fri Nov  6 2009 Dan Horák <dan[at]danny.cz> 0.16.0-2
- don't build the 3rd party stuff as shared libraries

* Tue Oct 27 2009 Dan Horák <dan[at]danny.cz> 0.16.0-1
- update to 0.16.0

* Sat Sep 19 2009 Dan Horák <dan[at]danny.cz> 0.15.1-1
- update to 0.15.1

* Tue Aug 18 2009 Dan Horák <dan[at]danny.cz> 0.15.0-1
- update to 0.15.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Dan Horak <dan[at]danny.cz> 0.14.1-1
- update to 0.14.1
- add workaround for #498111

* Wed Apr 15 2009 Dan Horak <dan[at]danny.cz> 0.11.1-1
- update to 0.11.1

* Tue Mar 10 2009 Dan Horak <dan[at]danny.cz> 0.11.0-1
- update to 0.11.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  6 2009 Dan Horak <dan[at]danny.cz> 0.10.0-1
- update to 0.10.0

* Fri Jan  2 2009 Dan Horak <dan[at]danny.cz> 0.9.3-1
- update to 0.9.3

* Tue Dec 23 2008 Dan Horak <dan[at]danny.cz> 0.9.2-1
- update to 0.9.2

* Fri Dec  5 2008 Dan Horak <dan[at]danny.cz> 0.9.1-1
- update to 0.9.1

* Tue Nov 25 2008 Dan Horak <dan[at]danny.cz> 0.9.0-1
- update to 0.9.0
- drop upstreamed sources and patch

* Wed Nov 19 2008 Dan Horak <dan[at]danny.cz> 0.8.1-3
- require garmindev(interface) = 1.15 for correct interraction with the Germin GPS drivers
- add comment to the patch0

* Sun Nov 16 2008 Dan Horak <dan[at]danny.cz> 0.8.1-2
- add patch for bigendian arches

* Fri Nov 14 2008 Dan Horak <dan[at]danny.cz> 0.8.1-1
- initial Fedora version
